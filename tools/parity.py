#!/usr/bin/env python3
import argparse,difflib,hashlib,json,subprocess,urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin
class N(HTMLParser):
 def __init__(s):super().__init__(convert_charrefs=True);s.o=[]
 def handle_starttag(s,t,a):s.o.append('<'+t+''.join(f' {k}={json.dumps(v or "")}' for k,v in sorted(a) if not k.startswith('data-astro-'))+'>')
 def handle_endtag(s,t):s.o.append('</'+t+'>')
 def handle_data(s,d):
  d=' '.join(d.split());s.o.extend([d] if d else [])
def get(b,r):
 u=urljoin(b.rstrip('/')+'/',r.lstrip('/'));q=urllib.request.Request(u,headers={'User-Agent':'nift-parity/1'});x=urllib.request.urlopen(q,timeout=30);return x.status,x.read().decode('utf8','replace'),u
def norm(h):p=N();p.feed(h);return '\n'.join(p.o)
def shot(u,p,w,h):return subprocess.run(['chromium','--headless','--disable-gpu','--no-sandbox',f'--window-size={w},{h}',f'--screenshot={p}',u],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=60).returncode
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--upstream',required=True);ap.add_argument('--nift',required=True);ap.add_argument('--routes',default='parity/golden-routes.txt');ap.add_argument('--out',default='reports/parity');ap.add_argument('--screenshots',action='store_true');ap.add_argument('--width',type=int,default=1440);ap.add_argument('--height',type=int,default=1200);a=ap.parse_args();rs=[x.strip() for x in Path(a.routes).read_text().splitlines() if x.strip() and not x.startswith('#')];o=Path(a.out);o.mkdir(parents=True,exist_ok=True);rows=[]
 for i,r in enumerate(rs):
  z={'route':r}
  try:
   us,uh,uu=get(a.upstream,r);ns,nh,nu=get(a.nift,r);U,V=norm(uh),norm(nh);z.update(upstream_status=us,nift_status=ns,upstream_bytes=len(uh.encode()),nift_bytes=len(nh.encode()),normalized_equal=U==V,upstream_sha256=hashlib.sha256(U.encode()).hexdigest(),nift_sha256=hashlib.sha256(V.encode()).hexdigest())
   if U!=V:(o/f'{i:03d}.diff').write_text('\n'.join(difflib.unified_diff(U.splitlines(),V.splitlines(),fromfile='upstream',tofile='nift'))[:2000000])
   if a.screenshots:
    sd=o/'screenshots';sd.mkdir(exist_ok=True);z['upstream_screenshot_rc']=shot(uu,sd/f'{i:03d}-upstream.png',a.width,a.height);z['nift_screenshot_rc']=shot(nu,sd/f'{i:03d}-nift.png',a.width,a.height)
  except Exception as e:z['error']=str(e)
  rows.append(z);print(r,z.get('normalized_equal','ERROR'))
 (o/'summary.json').write_text(json.dumps({'schema':1,'upstream':a.upstream,'nift':a.nift,'routes':rows},indent=2)+'\n');print(len(rows),'routes checked')
if __name__=='__main__':main()
