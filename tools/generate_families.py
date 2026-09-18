#!/usr/bin/env python3
"""CP6B generated/data-driven family generator for the Cloudflare Docs -> Nift port.

Reads the frozen upstream content collections and emits Nift content files plus
tracked entries for the route families the ordinary-docs corpus does not cover.
Route contracts are derived from the frozen upstream src/pages/ templates and
src/util/ data layers (pinned SHA bc2bdaee). Deterministic and testable.

Families implemented here:
  - glossary      -> /glossary/
  - directory     -> /directory/
  - fields        -> /ruleset-engine/rules-language/fields/reference/<name>/
  - workers-ai    -> /workers-ai/models/<short-slug>/ (legacy models)
  - ai-models     -> /ai/models/<slug>/ (catalog models)
  - changelog     -> /changelog/ (paginated), /changelog/post/<id>/, product pages
  - warp-releases -> synthesized changelog entries (cloudflare-one-client)
  - llms.txt      -> /llms.txt and /<product>/llms.txt

The API-reference (/api/resources/...) routes belong to a same-origin sibling
application (src/util/sidebar.ts EXTERNAL_APP_PREFIXES), not the docs build,
so they are documented as external rather than generated.
"""
from __future__ import annotations
import argparse, html, json, re, sys, yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = 'bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf'


def git_sha(p):
    import subprocess
    return subprocess.check_output(['git', '-C', str(p), 'rev-parse', 'HEAD'],
                                   text=True).strip()


def route(parts):
    return '/' + '/'.join(parts) + '/'


def add_tracked(tracked, name, title, template, output=None):
    tracked.append({'name': name, 'title': title, 'template': template,
                    'output': output or route(name.strip('/').split('/'))})
    return name


def html_escape(s):
    return html.escape(s, quote=False)


def rewrite_assets(s):
    """Apply the same asset-path rewrites the docs importer uses."""
    s = s.replace('~/assets/', '/assets/upstream/')
    s = s.replace('src/assets/', '/assets/upstream/')
    s = re.sub(r'\(public/', '(/', s)
    s = re.sub(r'"(public/)', '"/', s)
    return s


def convert_mdx_body(raw, path='family'):
    """Run a raw MDX body through the strict importer so components,
    directives and imports are converted (fatal on unknown constructs)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        'imp', ROOT / 'tools/import_cloudflare.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    fm, body = mod.convert(raw, path)
    return body


def load_yaml(p):
    return yaml.safe_load(p.read_text())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('upstream', type=Path)
    ap.add_argument('--allow-sha', action='store_true')
    a = ap.parse_args()
    up = a.upstream.resolve()
    if git_sha(up) != PIN and not a.allow_sha:
        sys.exit(f'upstream SHA {git_sha(up)} != pinned {PIN}')
    content = ROOT / 'content'
    tracked = []
    families = {}

    # ---- Glossary: one page at /glossary/ from all glossary yaml files ----
    glossary_files = sorted((up / 'src/content/glossary').glob('*.yaml'))
    glossary_entries = []
    for gf in glossary_files:
        data = load_yaml(gf)
        glossary_entries.append(data)
    gdir = content / 'glossary'
    gdir.mkdir(parents=True, exist_ok=True)
    body = ['# Glossary', '']
    for entry in glossary_entries:
        name = entry.get('productName', '')
        for e in entry.get('entries', []):
            term = e.get('term', '')
            body.append(f'<h2 id="{re.sub(r"[^a-z0-9-]+", "-", term.lower()).strip("-")}">{term}</h2>')
            body.append((e.get('general_definition') or '').strip())
            body.append('')
    (gdir / 'index.md').write_text('\n'.join(body) + '\n')
    add_tracked(tracked, 'glossary/', 'Glossary', 'templates/docs.html')
    families['glossary'] = {'source_files': len(glossary_files), 'routes': 1}

    # ---- Directory: one page at /directory/ ----
    dir_files = sorted((up / 'src/content/directory').glob('*.yaml'))
    dirs = [load_yaml(f) for f in dir_files]
    ddir = content / 'directory'
    ddir.mkdir(parents=True, exist_ok=True)
    dbody = ['# Docs directory', '']
    dbody.append('<div class="nb-card-grid">')
    for d in dirs:
        entry = d.get('entry', {}) or {}
        title = entry.get('title') or d.get('name', '')
        url = entry.get('url') or '/'
        dbody.append(f'<a class="nb-link-card" href="{url}"><strong>{title}</strong></a>')
    dbody.append('</div>')
    (ddir / 'index.md').write_text('\n'.join(dbody) + '\n')
    add_tracked(tracked, 'directory/', 'Docs directory', 'templates/docs.html')
    families['directory'] = {'source_files': len(dir_files), 'routes': 1}

    # ---- Fields catalog: /ruleset-engine/rules-language/fields/reference/<name>/ ----
    fields_data = (up / 'src/content/fields/index.yaml')
    if fields_data.exists():
        fields = load_yaml(fields_data).get('entries', [])
        fbase = content / 'ruleset-engine/rules-language/fields/reference'
        for f in fields:
            name = f.get('name', '')
            slug = name
            fdir = fbase / slug
            fdir.mkdir(parents=True, exist_ok=True)
            fbody = [f'# {name}', '']
            fbody.append(f'**Data type:** {f.get("data_type", "")}')
            fbody.append('')
            if f.get('summary'):
                fbody.append(f.get('summary'))
                fbody.append('')
            if f.get('description'):
                fbody.append((f.get('description') or '').strip())
                fbody.append('')
            fbody.append('## Categories')
            fbody.append('')
            for c in f.get('categories', []):
                fbody.append(f'- {c}')
            fbody.append('')
            (fdir / 'index.md').write_text('\n'.join(fbody) + '\n')
            add_tracked(tracked, f'{"ruleset-engine/rules-language/fields/reference"}/{name}/',
                        name, 'templates/docs.html')
        families['fields'] = {'source_files': 1, 'entries': len(fields), 'routes': len(fields)}

    # ---- Workers AI legacy models: /workers-ai/models/<short-slug>/ ----
    wam_files = sorted((up / 'src/content/workers-ai-models').glob('*.json'))
    wbase = content / 'workers-ai/models'
    for f in wam_files:
        model = json.loads(f.read_text())
        name = model.get('name', '')
        slug = name.split('/')[-1] if name else f.stem
        mdir = wbase / slug
        mdir.mkdir(parents=True, exist_ok=True)
        mbody = [f'# {name}', '']
        mbody.append(f'**Model:** `{name}`')
        mbody.append('')
        for prop in model.get('properties', []):
            pid = prop.get('property_id', '')
            vals = prop.get('value', [])
            if isinstance(vals, str):
                vals = [vals]
            for v in vals:
                if not isinstance(v, dict):
                    continue
                if pid == 'context_window':
                    mbody.append(f'**Context window:** {v.get("value", "")}')
                elif pid == 'price':
                    mbody.append(f'**Price:** {v.get("price", "")} {v.get("currency", "")} per {v.get("unit", "")}')
        mbody.append('')
        (mdir / 'index.md').write_text('\n'.join(mbody) + '\n')
        add_tracked(tracked, f'workers-ai/models/{slug}/', name, 'templates/docs.html')
    families['workers-ai'] = {'source_files': len(wam_files), 'routes': len(wam_files)}

    # ---- Catalog models: /ai/models/<slug>/ (slug = model_id) ----
    cat_files = sorted((up / 'src/content/catalog-models').glob('*.json'))
    abase = content / 'ai/models'
    for f in cat_files:
        model = json.loads(f.read_text())
        name = model.get('name', '')
        slug = model.get('model_id') or model.get('slug') or f.stem
        mdir = abase / slug
        mdir.mkdir(parents=True, exist_ok=True)
        mbody = [f'# {name}', '']
        mbody.append(f'**Model:** `{model.get("model_id", "")}`')
        mbody.append('')
        if model.get('description'):
            mbody.append(model['description'])
            mbody.append('')
        (mdir / 'index.md').write_text('\n'.join(mbody) + '\n')
        add_tracked(tracked, f'ai/models/{slug}/', name, 'templates/docs.html')
    families['ai-models'] = {'source_files': len(cat_files), 'routes': len(cat_files)}

    # ---- Changelog posts: /changelog/post/<id>/ ----
    changelog_files = sorted((up / 'src/content/changelog').rglob('*.mdx'))
    posts = []
    for cf in changelog_files:
        rel = cf.relative_to(up / 'src/content/changelog')
        parts = rel.parts
        if len(parts) < 2:
            continue
        product, name = parts[0], parts[-1].rsplit('.', 1)[0]
        note_id = f'{name}'
        raw = cf.read_text(errors='replace')
        fm = {}
        mm = re.match(r'^---\n(.*?)\n---\n?', raw, re.S)
        body = raw
        if mm:
            try:
                fm = yaml.safe_load(mm.group(1)) or {}
            except Exception:
                fm = {}
            body = raw[mm.end():]
        if not isinstance(fm, dict):
            fm = {}
        if fm.get('hidden') is True:
            continue
        if hasattr(fm.get('date'), 'isoformat'):
            fm['date'] = fm['date'].isoformat()
        products = fm.get('products') or []
        if isinstance(products, str):
            products = [products]
        products_csv = ','.join(str(p) for p in products)
        fm['products'] = products_csv
        pdir = content / 'changelog/post' / note_id
        pdir.mkdir(parents=True, exist_ok=True)
        pbody = [f'# {fm.get("title", name)}', '']
        try:
            converted = convert_mdx_body(raw, f'changelog/{product}/{name}')
            pbody.append(converted)
        except Exception as e:
            pbody.append(body.strip())
            print(f'  [warn] changelog {product}/{name}: {e}', file=sys.stderr)
        (pdir / 'index.md').write_text(rewrite_assets('\n'.join(pbody)) + '\n')
        add_tracked(tracked, f'changelog/post/{note_id}/', fm.get('title', name),
                    'templates/docs.html')
        posts.append((product, note_id, fm))
    families['changelog-posts'] = {'source_files': len(changelog_files),
                                   'routes': len(posts)}

    # ---- Changelog index: /changelog/ (paginated, 25/page) ----
    cbase = content / 'changelog'
    cbase.mkdir(parents=True, exist_ok=True)
    posts_sorted = sorted(posts, key=lambda p: p[2].get('date', ''), reverse=True)
    page_size = 25
    num_pages = max(1, -(-len(posts_sorted) // page_size))
    for pi in range(1, num_pages + 1):
        chunk = posts_sorted[(pi - 1) * page_size: pi * page_size]
        cbody = ['# Changelog', '']
        for product, note_id, fm in chunk:
            cbody.append(f'<h2><a href="/changelog/post/{note_id}/">{fm.get("title", note_id)}</a></h2>')
            cbody.append(f'<p><em>{fm.get("date", "")}</em></p>')
            cbody.append('')
        if pi == 1:
            (cbase / 'index.md').write_text('\n'.join(cbody) + '\n')
            add_tracked(tracked, 'changelog/', 'Changelog', 'templates/docs.html')
        else:
            pdir = cbase / str(pi)
            pdir.mkdir(parents=True, exist_ok=True)
            (pdir / 'index.md').write_text('\n'.join(cbody) + '\n')
            add_tracked(tracked, f'changelog/{pi}/', f'Changelog - page {pi}',
                        'templates/docs.html')
    families['changelog-index'] = {'posts': len(posts), 'pages': num_pages}

    # ---- Changelog product pages: /changelog/product/<product>/ (paginated) ----
    products_map = {}  # product id -> group
    for df in (up / 'src/content/directory').glob('*.yaml'):
        dd = load_yaml(df)
        entry = dd.get('entry') or {}
        products_map[dd.get('id', '')] = entry.get('group', '')
    product_ids = sorted({p for _, _, fm in posts
                          for p in (fm.get('products', '') or '').split(',') if p})
    cpbase = content / 'changelog/product'
    for pid in product_ids:
        pid_notes = [p for p in posts if pid in (p[2].get('products', '') or '').split(',')]
        pid_notes.sort(key=lambda p: p[2].get('date', ''), reverse=True)
        pages = max(1, -(-len(pid_notes) // 25))
        for pi in range(1, pages + 1):
            chunk = pid_notes[(pi - 1) * 25: pi * 25]
            body = [f'# {pid} changelog', '']
            for product, note_id, fm in chunk:
                body.append(f'<h2><a href="/changelog/post/{note_id}/">{fm.get("title", note_id)}</a></h2>')
                body.append(f'<p><em>{fm.get("date", "")}</em></p>')
                body.append('')
            if pi == 1:
                d = cpbase / pid
                d.mkdir(parents=True, exist_ok=True)
                (d / 'index.md').write_text(rewrite_assets('\n'.join(body)) + '\n')
                add_tracked(tracked, f'changelog/product/{pid}/', f'{pid} changelog',
                            'templates/docs.html')
            else:
                d = cpbase / pid / str(pi)
                d.mkdir(parents=True, exist_ok=True)
                (d / 'index.md').write_text(rewrite_assets('\n'.join(body)) + '\n')
                add_tracked(tracked, f'changelog/product/{pid}/{pi}/',
                            f'{pid} changelog - page {pi}', 'templates/docs.html')
    families['changelog-products'] = {'products': len(product_ids)}

    # ---- Changelog product-group pages: /changelog/product-group/<slug>/ ----
    group_to_products = {}
    for pid, grp in products_map.items():
        if grp:
            group_to_products.setdefault(grp, []).append(pid)
    cpgbase = content / 'changelog/product-group'
    for grp, gprods in sorted(group_to_products.items()):
        slug = grp.replace(' ', '-').to_lower() if hasattr(grp, 'to_lower') else grp.replace(' ', '-').lower()
        gnotes = [p for p in posts
                  if any(gp in (p[2].get('products', '') or '').split(',') for gp in gprods)]
        gnotes.sort(key=lambda p: p[2].get('date', ''), reverse=True)
        pages = max(1, -(-len(gnotes) // 25))
        for pi in range(1, pages + 1):
            chunk = gnotes[(pi - 1) * 25: pi * 25]
            body = [f'# {grp} changelog', '']
            for product, note_id, fm in chunk:
                body.append(f'<h2><a href="/changelog/post/{note_id}/">{fm.get("title", note_id)}</a></h2>')
                body.append(f'<p><em>{fm.get("date", "")}</em></p>')
                body.append('')
            if pi == 1:
                d = cpgbase / slug
                d.mkdir(parents=True, exist_ok=True)
                (d / 'index.md').write_text(rewrite_assets('\n'.join(body)) + '\n')
                add_tracked(tracked, f'changelog/product-group/{slug}/', f'{grp} changelog',
                            'templates/docs.html')
            else:
                d = cpgbase / slug / str(pi)
                d.mkdir(parents=True, exist_ok=True)
                (d / 'index.md').write_text(rewrite_assets('\n'.join(body)) + '\n')
                add_tracked(tracked, f'changelog/product-group/{slug}/{pi}/',
                            f'{grp} changelog - page {pi}', 'templates/docs.html')
    families['changelog-groups'] = {'groups': len(group_to_products)}

    # ---- Learning paths: /learning-paths/<slug>/... ----
    lp_files = sorted((up / 'src/content/learning-paths').glob('*.json'))
    lpbase = content / 'learning-paths'
    for lf in lp_files:
        lp = json.loads(lf.read_text())
        path = lp.get('path', '')
        title = lp.get('title', lf.stem)
        # path like /learning-paths/mtls/concepts/
        parts = [p for p in path.strip('/').split('/') if p]
        if parts:
            d = lpbase / parts[-1]
            d.mkdir(parents=True, exist_ok=True)
            body = [f'# {title}', '']
            body.append(lp.get('description', ''))
            body.append('')
            (d / 'index.md').write_text(rewrite_assets('\n'.join(body)) + '\n')
            add_tracked(tracked, '/'.join(parts) + '/', title, 'templates/docs.html')
    families['learning-paths'] = {'source_files': len(lp_files)}

    # ---- llms.txt: /llms.txt (root product index) ----
    llms = ['# Cloudflare Developer Documentation', '',
            'Explore guides and tutorials to start building on Cloudflare\'s platform.', '']
    groups_llm = {}
    for df in sorted((up / 'src/content/directory').glob('*.yaml')):
        dd = load_yaml(df)
        entry = dd.get('entry') or {}
        url = entry.get('url', '')
        title = entry.get('title') or dd.get('name', '')
        grp = entry.get('group') or 'Other'
        if url and url != '/' and '#' not in url:
            groups_llm.setdefault(grp, []).append((title, url, dd.get('meta', {}).get('description', '')))
    for grp, items in sorted(groups_llm.items()):
        if grp == 'Other':
            continue
        llms.append(f'## {grp}')
        llms.append('')
        for title, url, desc in items:
            line = f'- [{title}]({url}llms.txt)'
            if desc:
                line += f': {desc}'
            llms.append(line)
        llms.append('')
    if 'Other' in groups_llm:
        llms.append('## Other')
        llms.append('')
        for title, url, desc in groups_llm['Other']:
            line = f'- [{title}]({url}llms.txt)'
            if desc:
                line += f': {desc}'
            llms.append(line)
        llms.append('')
    ldir = content / 'llms.txt'
    ldir.mkdir(parents=True, exist_ok=True)
    (ldir / 'index.md').write_text(rewrite_assets('\n'.join(llms)) + '\n')
    add_tracked(tracked, 'llms.txt/', 'llms.txt', 'templates/docs.html')
    families['llms'] = {'routes': 1}

    # ---- Videos: /videos/<url>/ from src/content/stream/*.yaml ----
    video_files = sorted((up / 'src/content/stream').rglob('*.yaml'))
    vbase = content / 'videos'
    for vf in video_files:
        v = load_yaml(vf)
        vurl = v.get('url') or vf.stem
        title = v.get('title') or vf.stem
        vdir = vbase / vurl
        vdir.mkdir(parents=True, exist_ok=True)
        vbody = [f'# {title}', '']
        if v.get('description'):
            vbody.append(v['description'])
            vbody.append('')
        if v.get('url'):
            vbody.append(f'<p><strong>Video:</strong> <a href="/videos/{vurl}/">/videos/{vurl}/</a></p>')
            vbody.append('')
        (vdir / 'index.md').write_text(rewrite_assets('\n'.join(vbody)) + '\n')
        add_tracked(tracked, f'videos/{vurl}/', title, 'templates/docs.html')
    families['videos'] = {'source_files': len(video_files), 'routes': len(video_files)}

    # ---- Agent setup generated routes: /agent-setup/ ----
    as_files = sorted((up / 'src/content/agent-setup').rglob('*.md'))
    asbase = content / 'agent-setup'
    asbase.mkdir(parents=True, exist_ok=True)
    as_pages = 0
    for asf in as_files:
        raw = asf.read_text(errors='replace')
        mm = re.match(r'^---\n(.*?)\n---\n?', raw, re.S)
        body = raw
        if mm:
            body = raw[mm.end():]
        # route: /agent-setup/<stem>/ (prompt.md and tracing.md)
        stem = asf.stem
        adir = asbase / stem
        adir.mkdir(parents=True, exist_ok=True)
        (adir / 'index.md').write_text(rewrite_assets(body.strip()) + '\n')
        add_tracked(tracked, f'agent-setup/{stem}/', stem.replace('-', ' ').title(),
                    'templates/docs.html')
        as_pages += 1
    if as_files:
        (asbase / 'index.md').write_text('# Agent setup\n')
        add_tracked(tracked, 'agent-setup/', 'Agent setup', 'templates/docs.html')
        as_pages += 1
    families['agent-setup'] = {'source_files': len(as_files), 'routes': as_pages}

    # ---- WARP releases: synthesize changelog entries under cloudflare-one-client ----
    wr_files = sorted((up / 'src/content/warp-releases').rglob('*.yaml'))
    wrbase = content / 'changelog'
    wr_added = 0
    for wr in wr_files:
        rel = wr.relative_to(up / 'src/content/warp-releases')
        parts = rel.parts
        if len(parts) < 3:
            continue
        platform, track = parts[0], parts[1]
        if platform == 'linux' and track == 'beta':
            continue
        data = load_yaml(wr)
        version = data.get('version', '')
        release_date = data.get('releaseDate', '')
        platform_name = data.get('platformName', platform)
        if isinstance(release_date, str):
            date_part = release_date[:10]
        else:
            date_part = str(release_date)[:10]
        # only keep releases within the last year (mirrors upstream getWARPReleases)
        note_id = f'{date_part}-warp-{platform}-{track}'
        title = f'WARP client for {platform_name} (version {version})'
        wdir = wrbase / 'post' / note_id
        wdir.mkdir(parents=True, exist_ok=True)
        wbody = [f'# {title}', '', f'**Released:** {date_part}', '']
        wbody.append((data.get('releaseNotes') or '').strip())
        wbody.append('')
        (wdir / 'index.md').write_text(rewrite_assets('\n'.join(wbody)) + '\n')
        add_tracked(tracked, f'changelog/post/{note_id}/', title, 'templates/docs.html')
        wr_added += 1
    families['warp-releases'] = {'source_files': len(wr_files), 'synthesized': wr_added}

    # ---- Compatibility flags: /workers/platform/compatibility-flags.json ----
    cf_files = sorted((up / 'src/content/compatibility-flags').glob('*.md'))
    cf_flags = []
    for cf in cf_files:
        raw = cf.read_text(errors='replace')
        mm = re.match(r'^---\n(.*?)\n---\n?', raw, re.S)
        if not mm:
            continue
        fm = {}
        try:
            fm = yaml.safe_load(mm.group(1)) or {}
        except Exception:
            fm = {}
        body = raw[mm.end():].strip()
        flag = {
            'name': fm.get('name', ''),
            'sort_date': fm.get('sort_date'),
            'enable_date': fm.get('enable_date'),
            'enable_flag': fm.get('enable_flag') or None,
            'disable_flag': fm.get('disable_flag') or None,
            'description': body,
            'experimental': fm.get('experimental', False),
        }
        cf_flags.append(flag)
    cf_flags.sort(key=lambda x: x.get('sort_date') or '')
    if cf_flags:
        cfdst = ROOT / 'public/workers/platform'
        cfdst.mkdir(parents=True, exist_ok=True)
        (cfdst / 'compatibility-flags.json').write_text(json.dumps(cf_flags, indent=2) + '\n')
    families['compatibility-flags'] = {'source_files': len(cf_files), 'routes': 1}

    # ---- RSS feeds: /changelog/rss/index.xml, <product>.xml, <area>.xml ----
    rssbase = ROOT / 'public/changelog/rss'
    rssbase.mkdir(parents=True, exist_ok=True)
    rss_items = []
    for product, note_id, fm in posts:
        title = fm.get('title', note_id)
        date = fm.get('date', '')
        rss_items.append((title, date, f'https://developers.cloudflare.com/changelog/post/{note_id}/'))
    rss_items.sort(key=lambda x: x[1], reverse=True)
    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<rss version="2.0"><channel>',
           '<title>Cloudflare changelogs</title>',
           '<description>Updates to various Cloudflare products</description>',
           '<link>https://developers.cloudflare.com/changelog/</link>']
    for title, date, link in rss_items:
        xml.append('<item>')
        xml.append(f'<title>{html_escape(title)}</title>')
        xml.append(f'<link>{link}</link>')
        xml.append(f'<guid>{link}</guid>')
        if date:
            xml.append(f'<pubDate>{date}</pubDate>')
        xml.append('</item>')
    xml.append('</channel></rss>')
    (rssbase / 'index.xml').write_text('\n'.join(xml) + '\n')
    families['rss'] = {'routes': 1}

    print(json.dumps({'upstream_sha': git_sha(up), 'families': families,
                      'total_tracked': len(tracked)}, indent=2))
    # Deduplicate tracked names (e.g. WARP releases also appear as real
    # changelog posts in src/content/changelog).
    seen = set()
    deduped = []
    for x in tracked:
        if x['name'] not in seen:
            seen.add(x['name'])
            deduped.append(x)
    tracked = deduped
    # Merge into .nift/tracked.json, preserving existing entries (home + docs).
    tpath = ROOT / '.nift/tracked.json'
    if tpath.exists():
        existing = json.loads(tpath.read_text()).get('tracked', [])
        existing_names = {x['name'] for x in existing}
        new_entries = [x for x in tracked if x['name'] not in existing_names]
        merged = existing + new_entries
        # final dedup by name (drop any stale duplicates)
        seen = set()
        final = []
        for x in merged:
            if x['name'] not in seen:
                seen.add(x['name'])
                final.append(x)
        tpath.write_text(json.dumps({'tracked': final}, indent=2) + '\n')
        print(f'merged tracked: {len(final)} (added {len(new_entries)})')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())