#!/usr/bin/env python3
"""Strict Cloudflare MDX -> Nift staging importer.
Unknown JSX components are fatal; no silent flattening is permitted.
This is intentionally dependency-free so the migration does not acquire a Node toolchain.
"""
from __future__ import annotations
import argparse, html, json, re, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MODEL=json.loads((ROOT/'compatibility/content-model.json').read_text())
KNOWN=set(MODEL['components'])
SELF_CLOSING=re.compile(r'<([A-Z][A-Za-z0-9_.]*)\b([^<>]*?)/>')
PAIR=re.compile(r'<([A-Z][A-Za-z0-9_.]*)\b([^<>]*?)>([\s\S]*?)</\1>')
IMPORT=re.compile(r'^\s*import\s+.*?;?\s*$',re.M)
EXPORT=re.compile(r'^\s*export\s+.*?;?\s*$',re.M)
FRONT=re.compile(r'^---\n([\s\S]*?)\n---\n?')

def attrs(s):
    out={}
    for m in re.finditer(r'([:\w-]+)\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|\{([^{}]*)\})',s): out[m.group(1)]=next((x for x in m.groups()[1:] if x is not None),'')
    return out

def render(name,a,body=''):
    at=attrs(a); title=html.escape(at.get('title') or at.get('text') or name)
    if name=='Aside': return f'<aside class="nb-aside {html.escape(at.get("type","note"))}">{body}</aside>'
    if name=='Badge' or name=='InlineBadge': return f'<span class="nb-badge">{html.escape(at.get("text", body or name))}</span>'
    if name in {'Card','LinkCard','LinkTitleCard','ListCard'}:
        href=html.escape(at.get('href','#'),quote=True); return f'<a class="nb-card nb-link-card" href="{href}"><strong>{title}</strong>{body}</a>'
    if name in {'CardGrid','FourCardGrid'}: return f'<div class="nb-card-grid">{body}</div>'
    if name=='Steps': return f'<div class="nb-steps">{body}</div>'
    if name=='Step': return f'<section class="nb-step">{body}</section>'
    if name=='Details': return f'<details class="nb-details"><summary>{title}</summary>{body}</details>'
    if name=='FileTree': return f'<pre class="nb-file-tree">{body}</pre>'
    if name in {'Tabs','PackageManagers'}: return f'<div class="nb-tabs" data-nb-tabs>{body}</div>'
    if name=='TabItem':
        label=html.escape(at.get('label',at.get('value','Tab'))); ident='tab-'+re.sub(r'[^a-z0-9]+','-',label.lower()).strip('-')
        return f'<section class="nb-tab-panel" id="{ident}" data-tab-label="{label}">{body}</section>'
    cls=MODEL['components'][name]
    if cls=='browser-interactive': return f'<div class="nb-interactive-component" data-cf-component="{name}">{body}</div>'
    if cls=='data-generated': return f'<div class="nb-data-component" data-cf-component="{name}">{body}</div>'
    return f'<div class="nb-{re.sub(r"(?<!^)(?=[A-Z])","-",name).lower()}">{body}</div>'

def convert(text,path='<memory>'):
    fm={}; m=FRONT.match(text)
    if m:
        for line in m.group(1).splitlines():
            if ':' in line and not line.startswith((' ','\t')): fm[line.split(':',1)[0].strip()]=line.split(':',1)[1].strip().strip('"\'')
        text=text[m.end():]
    names=set(re.findall(r'</?([A-Z][A-Za-z0-9_.]*)\b',text)); unknown=sorted(names-KNOWN)
    if unknown: raise ValueError(f'{path}: unknown MDX components: {", ".join(unknown)}')
    text=IMPORT.sub('',text); text=EXPORT.sub('',text)
    # bounded repeated reduction handles ordinary nested components; unresolved JSX is fatal.
    for _ in range(64):
        old=text
        text=SELF_CLOSING.sub(lambda m:render(m.group(1),m.group(2)),text)
        text=PAIR.sub(lambda m:render(m.group(1),m.group(2),m.group(3)),text)
        if text==old: break
    remain=re.findall(r'</?([A-Z][A-Za-z0-9_.]*)\b',text)
    if remain: raise ValueError(f'{path}: unresolved nested MDX: {sorted(set(remain))}')
    return fm,text.strip()+"\n"

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('source'); ap.add_argument('output'); args=ap.parse_args()
    src,out=Path(args.source),Path(args.output); failures=[]; count=0
    for p in src.rglob('*'):
        if p.suffix not in {'.md','.mdx'}: continue
        try: fm,body=convert(p.read_text(),p); q=out/p.relative_to(src); q=q.with_suffix('.md'); q.parent.mkdir(parents=True,exist_ok=True); q.write_text(body); count+=1
        except Exception as e: failures.append(str(e))
    if failures:
        print('\n'.join(failures),file=sys.stderr); return 2
    print(f'imported {count} files')
    return 0
if __name__=='__main__': raise SystemExit(main())
