#!/usr/bin/env python3
"""Compare CP6 expected route manifest with Nift output and scan local links/assets."""
import argparse,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
HREF=re.compile(r'''(?:href|src)=["']([^"'#?]+)''',re.I)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--public',default=str(ROOT/'public')); a=ap.parse_args(); pub=Path(a.public)
 m=json.loads((ROOT/'reports/cp6/expected-routes.json').read_text()); exp=set(m['routes'])|{'/'}
 actual={'/'+p.parent.relative_to(pub).as_posix().strip('/')+'/' for p in pub.rglob('index.html')}; actual={'/' if x=='//' else x for x in actual}
 missing=sorted(exp-actual); broken=[]
 for f in pub.rglob('*.html'):
  for u in HREF.findall(f.read_text(errors='ignore')):
   if u.startswith(('http:','https:','mailto:','tel:','data:','//')): continue
   target=(pub/u.lstrip('/')) if u.startswith('/') else (f.parent/u)
   if u.endswith('/') or target.is_dir(): target=target/'index.html'
   if not target.exists(): broken.append((str(f.relative_to(pub)),u))
 print(json.dumps({'expected':len(exp),'actual_index_routes':len(actual),'missing_routes':missing,'broken_local_refs':broken[:500],'broken_count':len(broken)},indent=2))
 return 2 if missing or broken else 0
if __name__=='__main__': raise SystemExit(main())
