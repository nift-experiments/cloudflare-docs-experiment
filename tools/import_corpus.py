#!/usr/bin/env python3
"""CP6 full-corpus import orchestrator for the frozen Cloudflare checkout.
Requires a local checkout; refuses wrong SHA unless --allow-sha is supplied.
Generates Nift content, tracked.json, route manifests, copies static assets, and
reports unresolved dynamic/data families. It never silently skips a docs page.
"""
from __future__ import annotations
import argparse, hashlib, html, json, re, shutil, subprocess, sys, tempfile, yaml
from pathlib import Path
import import_cloudflare as ic
from import_cloudflare import convert
from generate_navigation import frontmatter, generate as generate_navigation, route_for
from upstream_snapshot import tracked_snapshot

PIN='bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf'
ROOT=Path(__file__).resolve().parents[1]

def git_sha(p):
    marker=Path(p)/'.upstream-sha'
    if marker.is_file(): return marker.read_text().strip()
    return subprocess.check_output(['git','-C',str(p),'rev-parse','HEAD'],text=True).strip()
def require_clean(p):
    if subprocess.check_output(['git','-C',str(p),'status','--porcelain'],text=True).strip():
        sys.exit(f'upstream worktree is dirty: {p}')
def tracked_paths(p, directory):
    if (Path(p)/'.upstream-sha').is_file():
        return [path.relative_to(p).as_posix() for path in (Path(p)/directory).rglob('*')
                if path.is_file()]
    return subprocess.check_output(
        ['git','-C',str(p),'ls-files','-z','--',directory],
    ).decode().split('\0')
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
    ic.require_cmarkgfm()
    source_up=Path(a.upstream).resolve(); docs=source_up/'src/content/docs'
    if not docs.is_dir(): sys.exit('missing src/content/docs')
    sha=git_sha(source_up)
    if sha!=PIN and not a.allow_sha: sys.exit(f'upstream SHA {sha} != pinned {PIN}')
    require_clean(source_up)
    up=tracked_snapshot(source_up,sha); docs=up/'src/content/docs'
    ic.configure_source_root(up)
    ic.configure_partials(up/'src/content/partials')
    presets_path=up/'src/content/pages-framework-presets/index.yaml'
    presets=yaml.safe_load(presets_path.read_text()).get('build_configs',{}) if presets_path.is_file() else {}
    ic.configure_pages_build_presets(presets)
    build_environments=[]
    for environment_path in sorted((up/'src/content/pages-build-environment').glob('*.yaml')):
        environment=yaml.safe_load(environment_path.read_text()) or {}
        environment['id']=environment_path.stem
        build_environments.append(environment)
    ic.configure_pages_build_environments(build_environments)
    glossaries={}
    for glossary_path in (up/'src/content/glossary').glob('*.yaml'):
        glossaries[glossary_path.stem]=yaml.safe_load(glossary_path.read_text()) or {}
    ic.configure_glossaries(glossaries)
    release_notes={}
    for release_path in (up/'src/content/release-notes').glob('*.yaml'):
        release_notes[release_path.stem]=yaml.safe_load(release_path.read_text()) or {}
    ic.configure_release_notes(release_notes)
    notifications_path=up/'src/content/notifications/index.yaml'
    notifications=(yaml.safe_load(notifications_path.read_text()) or {}).get('entries',[]) if notifications_path.is_file() else []
    ic.configure_notifications(notifications)
    compatibility_flags=[]
    for flag_path in sorted((up/'src/content/compatibility-flags').glob('*.md')):
        flag_fm,flag_body=frontmatter(flag_path)
        flag_data=dict(flag_fm)
        flag_data['body']=flag_body
        compatibility_flags.append(flag_data)
    ic.configure_compatibility_flags(compatibility_flags)
    warp_releases=[]
    for release_path in sorted((up/'src/content/warp-releases').rglob('*.yaml')):
        release=yaml.safe_load(release_path.read_text()) or {}
        release['_track']='/'.join(release_path.relative_to(up/'src/content/warp-releases').parts[:2])
        warp_releases.append(release)
    ic.configure_warp_releases(warp_releases)
    directory_entries=[]
    for directory_path in sorted((up/'src/content/directory').glob('*.yaml')):
        directory=yaml.safe_load(directory_path.read_text()) or {}
        directory['_id']=directory_path.stem
        directory_entries.append(directory)
    ic.configure_directory_entries(directory_entries)
    changelog_products=set()
    for changelog_path in sorted((up/'src/content/changelog').rglob('*.mdx')):
        changelog_fm,_=frontmatter(changelog_path)
        if changelog_fm.get('hidden') is True:
            continue
        changelog_products.add(changelog_path.relative_to(up/'src/content/changelog').parts[0])
        products=changelog_fm.get('products') or []
        if isinstance(products,str): products=[products]
        changelog_products.update(str(product) for product in products)
    ic.configure_changelog_products(changelog_products)
    dash_routes={}
    for dash_path in sorted((up/'src/content/dash-routes').glob('*.json')):
        dash_routes[dash_path.stem]=json.loads(dash_path.read_text())
    ic.configure_dash_routes(dash_routes)
    agents_source=(up/'src/components/agent-setup/agents.ts').read_text()
    agents=[]
    for block in re.finditer(r'\{\s*name:\s*"([^"]+)".*?slug:\s*"([^"]+)".*?description:\s*"([^"]+)"', agents_source, re.S):
        agents.append({'name':block.group(1),'slug':block.group(2),'description':block.group(3)})
    ic.configure_agents(agents)
    videos=[yaml.safe_load(path.read_text()) or {}
            for path in sorted((up/'src/content/stream').rglob('*.yaml'))]
    ic.configure_videos(videos)
    wrangler_script='''
import { experimental_getWranglerCommands as getCommands } from "wrangler";
const { registry } = getCommands();
const flatten = (subtree, out = []) => {
  for (const value of subtree.values()) {
    if (value.definition?.type === "command") out.push(value.definition);
    else flatten(value.subtree, out);
  }
  return out;
};
const result = {};
for (const [name, node] of registry.subtree.entries()) {
  result[name] = node.definition?.type === "command" ? [node.definition] : flatten(node.subtree);
}
console.log(JSON.stringify(result));
'''
    wrangler_snapshot=ROOT/'compatibility/wrangler-commands.json'
    if wrangler_snapshot.is_file():
        wrangler_commands=json.loads(wrangler_snapshot.read_text())
    else:
        wrangler_commands=json.loads(subprocess.check_output(
            ['node','--input-type=module','-e',wrangler_script],cwd=up,text=True,
            stderr=subprocess.DEVNULL))
    ic.configure_wrangler_commands(wrangler_commands)
    tracked_docs=tracked_paths(up,'src/content/docs')
    doc_files=[up/path for path in tracked_docs if path and Path(path).suffix in {'.md','.mdx'}]
    tracked_content=tracked_paths(up,'src/content')
    component_usage={}
    for source_name in tracked_content:
        if not source_name or Path(source_name).suffix != '.mdx': continue
        source_text=(up/source_name).read_text(errors='replace')
        protected,_placeholders=ic.protect_code(source_text)
        imported_components=ic.imported_component_names(source_text)
        for component in re.findall(r'<([A-Z][A-Za-z0-9]*)\b',protected):
            if component not in imported_components: continue
            usage=component_usage.setdefault(component,{'count':0,'pages':set()})
            usage['count']+=1; usage['pages'].add(source_name)
        for _match in re.finditer(r'^```mermaid\b',source_text,re.M):
            usage=component_usage.setdefault('Mermaid',{'count':0,'pages':set()})
            usage['count']+=1; usage['pages'].add(source_name)
    ic.configure_component_usage({name:{'count':value['count'],'pages':sorted(value['pages'])}
                                  for name,value in component_usage.items()})
    resources=[]
    for p in doc_files:
        rel=p.relative_to(docs); fm,_body=frontmatter(p)
        resource_id=rel.with_suffix('').as_posix()
        if resource_id.endswith('/index'): resource_id=resource_id[:-6]
        products=fm.get('products') or []
        if isinstance(products,str): products=[products]
        resources.append({
            'id':resource_id.strip('/'), 'route':route_for(rel,fm),
            'title':fm.get('title') or rel.stem.replace('-',' ').title(),
            'description':fm.get('description') or '',
            'pcx_content_type':fm.get('pcx_content_type'),
            'products':products, 'reviewed':str(fm.get('reviewed') or ''),
            'difficulty':str(fm.get('difficulty') or ''),
            'sidebar':fm.get('sidebar') or {}, 'tags':fm.get('tags') or [],
            'external_link':fm.get('external_link'),
        })
    ic.configure_resources(resources)
    with tempfile.TemporaryDirectory() as body_tmp:
        ic.configure_body_output(body_tmp, reset=True)
        pages=[]; failures=[]
        for p in doc_files:
            rel=p.relative_to(docs)
            source_fm,_source_body=frontmatter(p)
            route=route_for(rel,source_fm)
            conversion_metadata=dict(source_fm); conversion_metadata['_route']=route
            try: _converted_fm,body=convert(p.read_text(),p,metadata=conversion_metadata)
            except Exception as e: failures.append(str(e)); continue
            fm=source_fm
            if fm.get('summary'):
                body = f'<p class="article-summary">{html.escape(str(fm["summary"]))}</p>\n' + body
            pages.append((p,rel,route,fm,body))
        routes=[x[2] for x in pages]
        dup=sorted({r for r in routes if routes.count(r)>1})
        if failures or dup:
            for x in failures: print(x,file=sys.stderr)
            if dup: print('route collisions: '+', '.join(dup),file=sys.stderr)
            return 2
        if a.dry_run:
            print(json.dumps({'sha':sha,'docs':len(pages),'routes':len(routes)},indent=2)); return 0
        ic.record_ordinary_body_boundary()
        body_dir=ROOT/'content/.markup/bodies'
        shutil.rmtree(body_dir,ignore_errors=True)
        body_dir.parent.mkdir(parents=True,exist_ok=True)
        shutil.copytree(body_tmp,body_dir)
        content=ROOT/'content/docs'; shutil.rmtree(content,ignore_errors=True)
        tracked=[]
        for p,rel,route,fm,body in pages:
            name=name_for(route)
            q=ROOT/'content'/Path(name.strip('/')+'/index.md'); q.parent.mkdir(parents=True,exist_ok=True); q.write_text(body)
            template='templates/splash-md.html' if fm.get('template') == 'splash' else 'templates/docs.html'
            tracked.append({'name':name,'title':fm.get('title') or rel.stem.replace('-',' ').title(),'template':template,'output':output_for(route)})
    previous_manifest=ROOT/'reports/cp6/expected-routes.json'
    previous_routes=set()
    if previous_manifest.is_file():
        previous_routes=set(json.loads(previous_manifest.read_text()).get('routes',[]))
    generated_manifest=ROOT/'reports/cp6/expected-generated-routes.json'
    generated_routes=set()
    if generated_manifest.is_file():
        generated_routes=set(json.loads(generated_manifest.read_text()).get('routes',[]))
    stale_routes=previous_routes-set(routes)-generated_routes
    for stale in stale_routes:
        shutil.rmtree(ROOT/'content'/stale.strip('/'),ignore_errors=True)
        shutil.rmtree(ROOT/'public'/stale.strip('/'),ignore_errors=True)
    # Preserve the bespoke Nift landing page at /; upstream docs/index is not the landing route.
    base=json.loads((ROOT/'.nift/tracked.json').read_text()); home=[x for x in base.get('tracked',[]) if x.get('name')=='/']
    tracked=[x for x in tracked if x['name']!='/']
    (ROOT/'.nift/tracked.json').write_text(json.dumps({'tracked':home+tracked},indent=2)+'\n')
    static_count=copy_tree(up/'public',ROOT/'public')
    # Keep source assets under a deterministic public namespace; later component transforms may rewrite references.
    asset_count=copy_tree(up/'src/assets',ROOT/'public/assets/upstream')
    markdown_count=0
    for source,_rel,route,_fm,_body in pages:
        if route=='/': continue
        markdown=ROOT/'public'/route.strip('/')/'index.md'
        markdown.parent.mkdir(parents=True,exist_ok=True)
        markdown.write_text(frontmatter(source)[1].strip()+'\n')
        markdown_count+=1
    navigation=generate_navigation(up,ROOT/'public/assets/navigation.json',sha)
    manifest={'upstream_sha':sha,'docs_source_count':len(pages),'tracked_docs_count':len(tracked),'static_files_copied':static_count,'source_assets_copied':asset_count,'routes':sorted(r for r in routes if r!='/')}
    manifest['stale_routes_removed']=len(stale_routes)
    manifest['markdown_endpoints']=markdown_count
    manifest['navigation_products']=len(navigation['products'])
    out=ROOT/'reports/cp6'; out.mkdir(parents=True,exist_ok=True); (out/'expected-routes.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(f'imported {len(tracked)} docs routes; copied {static_count} public files and {asset_count} source assets; generated {markdown_count} markdown endpoints')
    return 0
if __name__=='__main__': raise SystemExit(main())
