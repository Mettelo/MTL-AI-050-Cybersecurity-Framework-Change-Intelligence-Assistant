import copy
import tempfile
import unittest
from pathlib import Path
from app import digest, validate, review, export, ai
from engine import build
import json

class EvidenceControls(unittest.TestCase):
    def setUp(self):
        Path('runs').mkdir(exist_ok=True)
        self.d=build(json.loads(Path('data/reference/demo.json').read_text(encoding='utf-8')))
        self.decisions={r['id']:{'status':'accept','note':'Synthetic test review only'} for r in self.d['records']}
    def test_citations_resolve(self):
        self.assertTrue(validate(self.d))
    def test_reject_unknown_source(self):
        d=copy.deepcopy(self.d); d['records'][0]['citations'][0]['source']='invented'
        with self.assertRaises(AssertionError): validate(d)
    def test_reject_fabricated_quote(self):
        d=copy.deepcopy(self.d); d['records'][0]['citations'][0]['quote']='FABRICATED QUOTE 12345'
        with self.assertRaises(AssertionError): validate(d)
    def test_pending_review_blocked(self):
        x=copy.deepcopy(self.decisions); x[next(iter(x))]['status']='pending'
        with self.assertRaises(AssertionError): review(self.d,x,'tester')
    def test_partial_review_blocked(self):
        x=copy.deepcopy(self.decisions); x.pop(next(iter(x)))
        with self.assertRaises(AssertionError): review(self.d,x,'tester')
    def test_edit_invalidates_approval(self):
        approval=review(self.d,self.decisions,'tester')
        d=copy.deepcopy(self.d); d['records'][0]['text']+=' changed'
        with tempfile.TemporaryDirectory(dir='runs') as t:
            with self.assertRaises(AssertionError): export(d,approval,Path(t)/'export.csv')
    def test_export_only_accepted(self):
        x=copy.deepcopy(self.decisions); x[next(iter(x))]['status']='reject'
        with tempfile.TemporaryDirectory(dir='runs') as t:
            p=Path(t)/'export.csv'; export(self.d,review(self.d,x,'tester'),p)
            import csv
            with p.open(encoding='utf-8',newline='') as f: self.assertEqual(len(list(csv.DictReader(f))),len(x)-1)
    def test_reproducible(self):
        source=json.loads(Path('data/reference/demo.json').read_text(encoding='utf-8'))
        self.assertEqual(digest(self.d),digest(build(source)))
    def test_local_ai_accepts_grounded_json(self):
        from unittest.mock import patch
        from io import BytesIO
        row=self.d['records'][0]
        proposal={'record_id':row['id'],'text':'Provisional interpretation; reviewer must verify.', 'citations':row['citations']}
        response=json.dumps({'message':{'content':json.dumps({'proposals':[proposal]})}}).encode()
        with patch('app.urlopen',return_value=BytesIO(response)):
            d=ai(copy.deepcopy(self.d),'test-model')
        self.assertTrue(validate(d));self.assertTrue(d['ai']['semantic_review_required'])
    def test_local_ai_fabricated_citation_rejected(self):
        from unittest.mock import patch
        from io import BytesIO
        row=self.d['records'][0]
        proposal={'record_id':row['id'],'text':'Invented finding','citations':[{'source':'invented','quote':'fake'}]}
        response=json.dumps({'message':{'content':json.dumps({'proposals':[proposal]})}}).encode()
        with patch('app.urlopen',return_value=BytesIO(response)):
            with self.assertRaises(AssertionError): ai(copy.deepcopy(self.d),'test-model')

if __name__=='__main__': unittest.main()
