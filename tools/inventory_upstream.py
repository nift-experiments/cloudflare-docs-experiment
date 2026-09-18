#!/usr/bin/env python3
import argparse,collections,json,re,subprocess
from pathlib import Path
COMP=re.compile(r'<([A-Z][A-Za-z0-9_.:-]*)\b'); IMP=re.compile(r'^\s*import\s+.+?\s+from\s+["\']([^"\']+)["\']',re.M); FRONT=re.compile(r'^---\s*\n(.*?)\n---',re.S); KEY=re.compile(r'^([A-Za-z_][\w-]*):',re.M)
def git(r,*a):
 try:return subprocess.check_output(['git','-C',str(r),*a],text=True).strip()
 except:return None
def main():
 ap=argparse.ArgumentParser();ap.add_argument('upstream',type=Path);ap.add_argument('-o','--output',type=Path,default=Path('reports/upstream-inventory.json'));a=ap.parse_args();r=a.upstream.resolve()
 if not (r/'src/content/docs').is_dir():raise SystemExit('not a cloudflare-docs checkout')
 fs=[p for p in r.rglob('*') if p.is_file() and '.git' not in p.parts and 'node_modules' not in p.parts]; ex=collections.Counter(p.suffix or '(none)' for p in fs);prod=collections.Counter();co=collections.Counter();im=collections.Counter();fk=collections.Counter();docs=[]
 for p in fs:
  rel=p.relative_to(r).as_posix()
  if rel.startswith('src/content/docs/') and p.suffix in {'.md','.mdx'}:
   docs.append(p);prod[rel.split('/')[3]]+=1
   s=p.read_text(errors='replace');co.update(COMP.findall(s));im.update(IMP.findall(s));m=FRONT.match(s);fk.update(KEY.findall(m.group(1)) if m else [])
 d={'schema':1,'git':{'head':git(r,'rev-parse','HEAD'),'branch':git(r,'branch','--show-current')},'totals':{'files':len(fs),'bytes':sum(p.stat().st_size for p in fs),'docs_pages':len(docs),'products':len(prod)},'extensions':ex.most_common(),'docs_by_product':prod.most_common(),'mdx_components':co.most_common(),'mdx_import_sources':im.most_common(),'frontmatter_keys':fk.most_common()};a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,indent=2)+'\n');print('wrote',a.output,len(docs),'docs pages')
if __name__=='__main__':main()
