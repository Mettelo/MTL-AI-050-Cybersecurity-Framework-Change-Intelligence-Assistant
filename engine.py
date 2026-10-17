"""Core outcome crosswalk comparison. Unmapped is not confirmed removal/addition."""
import re
import zipfile
import xml.etree.ElementTree as ET
import hashlib
NS={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def xlsx(path,sheet):
    with zipfile.ZipFile(path) as z:
        strings=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            strings=[''.join(e.itertext()) for e in ET.fromstring(z.read('xl/sharedStrings.xml'))]
        for row in ET.fromstring(z.read(f'xl/worksheets/sheet{sheet}.xml')).findall('.//s:row',NS):
            values={}
            for c in row.findall('s:c',NS):
                col=re.match(r'[A-Z]+',c.get('r'))[0]; v=c.find('s:v',NS)
                value=v.text if v is not None else ''
                if c.get('t')=='s': value=strings[int(value)] if value else ''
                elif c.get('t')=='inlineStr': value=''.join(c.find('s:is',NS).itertext())
                values[col]=value
            yield values

def core(path,sheet,version):
    rows={}
    for row in xlsx(path,sheet):
        text=row.get('C',''); m=re.match(r'^([A-Z]{2}\.[A-Z]{2}-\d+):\s*(.+)',text,re.S)
        if m and not m[2].lstrip().startswith('[Withdrawn:'):
            rows[m[1]]={'text':m[2].strip(),'locator':f'{path.name}:sheet{sheet}:{m[1]}','version':version}
    return rows

def prepare(path,meeting):
    # Directory must contain the three source files documented in data/README.md.
    old=core(path/'csf11.xlsx',1,'1.1'); new=core(path/'csf20.xlsx',2,'2.0')
    assert len(old)==108 and len(new)==106, f'Unexpected outcome inventory: {len(old)}, {len(new)}'
    mappings=[]
    for row in xlsx(path/'crosswalk.xlsx',1):
        n,o=row.get('A',''),row.get('C','')
        if n in new and o in old and [o,n] not in mappings: mappings.append([o,n])
    assert mappings, 'No crosswalk relationships parsed'
    return {'old':old,'new':new,'mappings':mappings,'source_sha256':
        {n:hashlib.sha256((path/n).read_bytes()).hexdigest() for n in ('csf11.xlsx','csf20.xlsx','crosswalk.xlsx')}}

def build(data):
    old,new=data['old'],data['new']; evidence={}; records=[]
    for version,rows in [('1.1',old),('2.0',new)]:
        for k,v in rows.items(): evidence[version+':'+k]=v
    pairs=data['mappings']; assert all(o in old and n in new for o,n in pairs)
    used_old={p[0] for p in pairs}; used_new={p[1] for p in pairs}
    def add(o,n):
        cites=[]
        for version,k,rows in [('1.1',o,old),('2.0',n,new)]:
            if k: cites.append({'source':version+':'+k,'quote':rows[k]['text']})
        if not o: kind='addition_candidate'
        elif not n: kind='removal_candidate'
        elif old[o]['text']==new[n]['text']: kind='unchanged_text'
        else: kind='changed_text'
        cardinality={'old_to_new':sum(p[0]==o for p in pairs) if o else 0,
                     'new_from_old':sum(p[1]==n for p in pairs) if n else 0}
        records.append({'id':f'R{len(records)+1:04d}','kind':kind,'text':f'{o or "(no mapped predecessor)"} -> {n or "(no mapped successor)"}',
            'details':{'old_id':o,'new_id':n,'cardinality':cardinality,
            'alignment_basis':'NIST crosswalk' if o and n else 'No crosswalk link; requires source review',
            'possible_impact':'Review governance roles, policy ownership and oversight evidence.' if n and n.startswith('GV.') else
            'Review affected policy, control evidence and responsibilities; organisational relevance remains to be assessed.',
            'impact_status':'hypothesis; no legal/compliance determination','owner':None,'priority':None,
            'review_instruction':'Check both documents; distinguish moved, split, merged, revised, genuinely new or withdrawn outcomes.'},'citations':cites})
    for o,n in sorted(pairs): add(o,n)
    for o in sorted(set(old)-used_old): add(o,None)
    for n in sorted(set(new)-used_new): add(None,n)
    sections={}
    for version,rows in [('1.1',old),('2.0',new)]:
        sections[version]={'functions':sorted({k.split('.')[0] for k in rows}),
            'categories':sorted({k.split('-')[0] for k in rows})}
    return {'project':'MTL-AI-050','mode':'crosswalk-assisted-text-diff','records':records,'evidence':evidence,
        'section_inventory':sections,
        'coverage':{'old':len(old),'new':len(new),'relationships':len(pairs)},
        'limitations':['Core outcomes only; narrative sections, Profiles and Tiers require separate human analysis.',
            'Unmapped outcomes are candidates, not proven additions/removals; relationships are not equivalence.']}
