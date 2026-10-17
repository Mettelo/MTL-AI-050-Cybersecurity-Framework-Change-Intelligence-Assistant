import json,unittest
from pathlib import Path
from engine import build,prepare

class FrameworkCases(unittest.TestCase):
    def setUp(self):self.data=json.loads(Path('data/reference/demo.json').read_text())
    def test_complete_inventory_coverage(self):
        d=build(self.data)
        old={r['details']['old_id'] for r in d['records']} - {None}
        new={r['details']['new_id'] for r in d['records']} - {None}
        self.assertEqual(old,set(self.data['old']));self.assertEqual(new,set(self.data['new']))
        self.assertEqual((len(old),len(new)),(108,106))
    def test_matched_records_cite_both_versions(self):
        for r in build(self.data)['records']:
            if r['details']['old_id'] and r['details']['new_id']:
                self.assertEqual({c['source'].split(':')[0] for c in r['citations']},{'1.1','2.0'})
    def test_unmapped_is_candidate(self):
        self.data['mappings']=[]
        self.assertEqual({r['kind'] for r in build(self.data)['records']},{'addition_candidate','removal_candidate'})
    def test_many_to_many_preserved(self):
        d=build(self.data)
        self.assertTrue(any(r['details']['cardinality']['old_to_new']>1 for r in d['records']))
        self.assertTrue(any(r['details']['cardinality']['new_from_old']>1 for r in d['records']))
