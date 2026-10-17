"""Download official resources locally. Never commit the raw source directory."""
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen
from datetime import datetime, timezone

def main():
    sources=json.loads(Path('data/metadata/resources.json').read_text(encoding='utf-8'))
    root=Path('data/raw'); root.mkdir(parents=True,exist_ok=True)
    manifest=[]
    for s in sources:
        path=root/s['filename']
        if not path.exists():
            with urlopen(s['url'],timeout=180) as r: content=r.read()
            path.write_bytes(content)
        content=path.read_bytes()
        manifest.append({**s,'sha256':hashlib.sha256(content).hexdigest(),'bytes':len(content),
                         'checked_utc':datetime.now(timezone.utc).isoformat()})
    Path('data/metadata/download_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print('Local sources and manifest ready. Compare hashes with baseline_manifest.json before benchmark reproduction.')

if __name__=='__main__': main()
