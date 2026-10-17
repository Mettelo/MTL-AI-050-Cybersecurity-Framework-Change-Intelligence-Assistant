"""Frozen-demo structural evaluation. Not semantic AI performance."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app import read, write, validate, digest
from engine import build
from collections import Counter

source=read('data/reference/demo.json')
draft=build(source)
valid=validate(draft)
quotes=[c for r in draft['records'] for c in r['citations']]
result={'scope':'Frozen demo structural checks only; no semantic or model benchmark claim',
    'project':draft['project'],'input_sha256':digest(source),'output_sha256':digest(draft),
    'records':len(draft['records']),'record_kinds':dict(Counter(r['kind'] for r in draft['records'])),
    'citation_valid_count':len(quotes) if valid else 0,'citation_total':len(quotes),
    'baseline_repeat_identical':digest(draft)==digest(build(source)),
    'semantic_benchmark':'pending independently adjudicated gold',
    'local_model_evaluation':'not executed; no model runtime assumed',
    'human_uat':'pending domain reviewer'}
if 'coverage' in draft: result['inventory_coverage']=draft['coverage']
write('evaluation/baseline_results.json',result)
print(__import__('json').dumps(result,indent=2))
