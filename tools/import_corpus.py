#!/usr/bin/env python3
"""CP6 full-corpus import orchestrator for the frozen Cloudflare checkout.
Requires a local checkout; refuses wrong SHA unless --allow-sha is supplied.
Generates Nift content, tracked.json, route manifests, copies static assets, and
reports unresolved dynamic/data families. It never silently skips a docs page.
"""
from __future__ import annotations
import argparse, hashlib, json, shutil, subprocess, sys
from pathlib import Path
import import_cloudflare as ic
from import_cloudflare import convert

PIN='bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf'
ROOT=Path(__file__).resolve().parents[1]
ic._BODY_DIR = ROOT / 'content/.markup/bodies'
ic._BODY_NEXT = 0

def git_sha(p):
    return subprocess.check_output(['git','-C',str(p),'rev-parse','HEAD'],text=True).strip()
def route_for(rel):
    s=rel.as_posix(); s=s.rsplit('.',1)[0]
    if s.endswith('/index'): s=s[:-6]
    if s=='index': return '/'
    return '/'+s.strip('/')+'/'
def name_for(route): return '/' if route=='/' else route.strip('/')+'/'
def output_for(route): return 'index.html' if route=='/' else route.strip('/')+'/index.html'
def copy_tree(src,dst):
    if not src.exists(): return 0
    n=0
    for p in src.rglob('*'):
        if p.is_file():
            q=dst/p.relative_to(src); q.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(p,q); n+=1
    return n

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('upstream'); ap.add_argument('--allow-sha',action='store_true'); ap.add_argument('--dry-run',action='store_true'); a=ap.parse_args()
    up=Path(a.upstream).resolve(); docs=up/'src/content/docs'
    if not docs.is_dir(): sys.exit('missing src/content/docs')
    sha=git_sha(up)
    if sha!=PIN and not a.allow_sha: sys.exit(f'upstream SHA {sha} != pinned {PIN}')
    pages=[]; failures=[]
    for p in sorted(docs.rglob('*')):
        if p.suffix not in {'.md','.mdx'}: continue
        rel=p.relative_to(docs); route=route_for(rel)
        try: fm,body=convert(p.read_text(),p)
        except Exception as e: failures.append(str(e)); continue
        pages.append((p,rel,route,fm,body))
    routes=[x[2] for x in pages]
    dup=sorted({r for r in routes if routes.count(r)>1})
    if failures or dup:
        for x in failures: print(x,file=sys.stderr)
        if dup: print('route collisions: '+', '.join(dup),file=sys.stderr)
        return 2
    if a.dry_run:
        print(json.dumps({'sha':sha,'docs':len(pages),'routes':len(routes)},indent=2)); return 0
    content=ROOT/'content/docs'; shutil.rmtree(content,ignore_errors=True)
    tracked=[]
    for p,rel,route,fm,body in pages:
        name=name_for(route)
        q=ROOT/'content'/Path(name.strip('/')+'/index.md'); q.parent.mkdir(parents=True,exist_ok=True); q.write_text(body)
        tracked.append({'name':name,'title':fm.get('title') or rel.stem.replace('-',' ').title(),'template':'templates/docs.html','output':output_for(route)})
    # Preserve the bespoke Nift landing page at /; upstream docs/index is not the landing route.
    base=json.loads((ROOT/'.nift/tracked.json').read_text()); home=[x for x in base.get('tracked',[]) if x.get('name')=='/']
    tracked=[x for x in tracked if x['name']!='/']
    (ROOT/'.nift/tracked.json').write_text(json.dumps({'tracked':home+tracked},indent=2)+'\n')
    static_count=copy_tree(up/'public',ROOT/'public')
    # Keep source assets under a deterministic public namespace; later component transforms may rewrite references.
    asset_count=copy_tree(up/'src/assets',ROOT/'public/assets/upstream')
    manifest={'upstream_sha':sha,'docs_source_count':len(pages),'tracked_docs_count':len(tracked),'static_files_copied':static_count,'source_assets_copied':asset_count,'routes':sorted(r for r in routes if r!='/')}
    out=ROOT/'reports/cp6'; out.mkdir(parents=True,exist_ok=True); (out/'expected-routes.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(f'imported {len(tracked)} docs routes; copied {static_count} public files and {asset_count} source assets')
    return 0
if __name__=='__main__': raise SystemExit(main())
