"""Behavior checks for expanded production coverage. Standard library only."""
import copy
import importlib.util
import json
import re
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PROD = ROOT / 'skills/production'
spec = importlib.util.spec_from_file_location('readiness', PROD / 'scripts/readiness.py')
readiness = importlib.util.module_from_spec(spec)
spec.loader.exec_module(readiness)
REGISTRY = readiness.load_registry(PROD / 'references')
NEW_PARTS = {'mcp', 'agent', 'deployment', 'sync', 'realtime', 'device', 'supply-chain'}


def fixture(part, kind='other'):
    checks = [{'id': cid, 'surface': 'runtime', 'status': 'pass',
               'severity': 'high', 'core_flow': True,
               'evidence': 'Synthetic test harness: advertised behavior exercised.'}
              for cid, pid in REGISTRY.items() if pid == part]
    return {'schema_version': '1.0', 'product': {'name': 'Synthetic fixture'},
            'run': {'date': '2026-10-20', 'profile': 'spot-audit', 'parts_in_scope': [part]},
            'surfaces': [{'id': 'runtime', 'name': 'Test runtime', 'kind': kind, 'core': True}],
            'checks': checks}


class ProductionCoverage(unittest.TestCase):
    def test_new_parts_drive_all_gate_states_and_render(self):
        for part in NEW_PARTS:
            with self.subTest(part=part):
                p = fixture(part)
                errors, warnings = readiness.validate(p, REGISTRY)
                self.assertEqual(errors, [])
                self.assertEqual(warnings, [])
                r = readiness.compute(p, REGISTRY)
                self.assertEqual(r['decision'], 'GO')
                self.assertEqual(r['overall']['coverage'], 100)
                self.assertEqual(r['parts'][0]['summary']['assessed'],
                                 f"{len(p['checks'])}/{len(p['checks'])}")
                p['checks'][0].update(status='fail', severity='critical')
                r = readiness.compute(p, REGISTRY)
                self.assertEqual(r['decision'], 'NO_GO')
                self.assertEqual(r['surfaces'][0]['decision'], 'NO_GO')
                self.assertIn(p['checks'][0]['id'] + '@runtime', r['blockers'])
                self.assertIn('NO-GO', readiness.render(p, r))
                p['checks'][0]['status'] = 'not_verified'
                r = readiness.compute(p, REGISTRY)
                self.assertEqual(r['decision'], 'HOLD')
                self.assertEqual(len(r['verification_required']), 1)
                p['checks'][0].update(status='fail', severity='high', core_flow=False)
                self.assertEqual(readiness.compute(p, REGISTRY)['decision'], 'GO_WITH_CONDITIONS')
                p['checks'][0].update(severity='critical', risk_accepted_by='Fixture owner, written test acceptance')
                self.assertEqual(readiness.compute(p, REGISTRY)['decision'], 'GO_WITH_CONDITIONS')

    def test_missing_part_cannot_become_ready(self):
        p = fixture('mcp')
        p['checks'] = []
        r = readiness.compute(p, REGISTRY)
        self.assertEqual(r['decision'], 'HOLD')
        self.assertIn('mcp', r['unassessed_parts'])

    def test_optional_part_exclusion_has_a_reason_and_preserves_existing_scope(self):
        p = fixture('security')
        p['run']['parts_in_scope'].append('mcp')
        p['parts'] = [{'id': 'mcp', 'applicable': False, 'reason': 'No MCP implementation'}]
        r = readiness.compute(p, REGISTRY)
        self.assertEqual(r['decision'], 'GO')
        self.assertEqual(next(x for x in r['parts'] if x['id'] == 'mcp')['summary']['status'], 'not_applicable')

    def test_multi_surface_isolation_failure_is_ranked_first(self):
        p = fixture('mcp', 'mcp-server')
        p['surfaces'].append({'id': 'client', 'name': 'Test client', 'kind': 'mcp-client'})
        p['checks'].append({'id': 'MCP-11', 'surface': 'client', 'status': 'fail',
                            'severity': 'critical', 'core_flow': True, 'evidence': 'Synthetic unauthorized read'})
        self.assertEqual(readiness.validate(p, REGISTRY)[0], [])
        r = readiness.compute(p, REGISTRY)
        self.assertEqual(r['surfaces'][0]['id'], 'client')
        self.assertEqual(r['surfaces'][0]['decision'], 'NO_GO')
        self.assertEqual(r['surfaces'][1]['decision'], 'GO')

    def test_schema_and_registry_cover_same_parts(self):
        schema = json.loads((PROD / 'assets/payload.schema.json').read_text())
        self.assertEqual(set(schema['$defs']['partId']['enum']), set(readiness.PART_BY_ID))
        self.assertEqual(set(REGISTRY.values()), set(readiness.PART_BY_ID))

    def test_synthetic_mcp_example_is_complete_and_holds(self):
        p = json.loads((PROD / 'assets/mcp-example-payload.json').read_text())
        errors, warnings = readiness.validate(p, REGISTRY)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])
        self.assertEqual({c['id'] for c in p['checks']}, {cid for cid, part in REGISTRY.items() if part == 'mcp'})
        r = readiness.compute(p, REGISTRY)
        self.assertEqual(r['decision'], 'HOLD')
        self.assertIn('MCP-11@local-mcp', r['verification_required'])

    def test_registry_cannot_hide_duplicate_or_unknown_check_definitions(self):
        ids = []
        for path in (PROD / 'references').glob('*-audit.md'):
            ids.extend(re.findall(r'^\| ([A-Z0-9]+-\d\d) \|', path.read_text(), re.M))
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), set(REGISTRY))

    def test_custom_checks_and_duplicate_rejection(self):
        p = fixture('device')
        custom = {'id': 'DEV-C01', 'surface': 'runtime', 'status': 'fail',
                  'severity': 'critical', 'core_flow': True, 'evidence': 'Synthetic failed interlock'}
        p['checks'].append(custom)
        self.assertEqual(readiness.validate(p, REGISTRY)[0], [])
        self.assertEqual(readiness.compute(p, REGISTRY)['decision'], 'NO_GO')
        p['checks'].append(copy.deepcopy(custom))
        self.assertTrue(any('duplicate' in e for e in readiness.validate(p, REGISTRY)[0]))


if __name__ == '__main__':
    unittest.main()
