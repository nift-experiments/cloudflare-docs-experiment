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
  - warp-releases -> aggregate-only source records (no standalone routes)
  - llms.txt      -> /llms.txt and /<product>/llms.txt

The API-reference (/api/resources/...) routes belong to a same-origin sibling
application (src/util/sidebar.ts EXTERNAL_APP_PREFIXES), not the docs build,
so they are documented as external rather than generated.
"""
from __future__ import annotations
import argparse, datetime, html, json, re, shutil, subprocess, sys, yaml
from zoneinfo import ZoneInfo
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = 'bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf'
sys.path.insert(0, str(ROOT / 'tools'))
import import_cloudflare as mdx_importer
from upstream_snapshot import tracked_snapshot


def git_sha(p):
    marker = Path(p) / '.upstream-sha'
    if marker.is_file():
        return marker.read_text().strip()
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


def tracked_files(upstream, directory, suffixes):
    if (upstream / '.upstream-sha').is_file():
        return sorted(path for path in (upstream / directory).rglob('*')
                      if path.is_file() and path.suffix in suffixes)
    paths = subprocess.check_output(
        ['git', '-C', str(upstream), 'ls-files', '-z', '--', directory]
    ).decode().split('\0')
    return [upstream / path for path in paths if path and Path(path).suffix in suffixes]


def rewrite_assets(s):
    """Apply the same asset-path rewrites the docs importer uses."""
    s = s.replace('~/assets/', '/assets/upstream/')
    s = s.replace('src/assets/', '/assets/upstream/')
    s = re.sub(r'\(public/', '(/', s)
    s = re.sub(r'"(public/)', '"/', s)
    return s


def prefix_fragment_ids(markup, prefix):
    """Keep repeated changelog bodies addressable when combined in one feed."""
    ids = re.findall(r'\bid=["\']([^"\']+)', markup)
    for value in ids:
        replacement = f'{prefix}-{value}'
        markup = re.sub(rf'\bid=(["\']){re.escape(value)}\1', f'id="{replacement}"', markup)
        markup = markup.replace(f'href="#{value}"', f'href="#{replacement}"')
    return markup


def normalize_changelog_headings(markup):
    """Match upstream's changelog HAST transform: source h1-h3 become h4."""
    preserved = {}
    def protect(match):
        marker = f'\x00CHANGELOG_COMPONENT_HEADING_{len(preserved)}\x00'
        preserved[marker] = match.group(0)
        return marker
    markup = re.sub(r'<h3\b(?=[^>]*class="nb-component-title")[^>]*>.*?</h3>', protect, markup,
                    flags=re.I | re.S)
    markup = re.sub(r'<(/?)h[1-3](\b[^>]*>)', r'<\1h4\2', markup, flags=re.I)
    for marker, heading in preserved.items():
        markup = markup.replace(marker, heading)
    return markup


def changelog_entry_visible(frontmatter, today=None):
    """Match upstream's future-entry publication rule."""
    if frontmatter.get('publish_future_dated_entry'):
        return True
    today = today or datetime.datetime.now(datetime.timezone.utc).date()
    raw_date = str(frontmatter.get('date', ''))[:10]
    try:
        return datetime.date.fromisoformat(raw_date) <= today
    except ValueError:
        return False


def brisbane_date(value):
    raw_date = str(value or '')
    if len(raw_date) > 10:
        try:
            instant = datetime.datetime.fromisoformat(raw_date.replace('Z', '+00:00'))
            if instant.tzinfo:
                return str(instant.astimezone(ZoneInfo('Australia/Brisbane')).date())
        except ValueError:
            pass
    return raw_date[:10]


def pagination_markup(base_url, current_page, last_page):
    if last_page <= 1:
        return ''

    def page_url(page):
        return base_url if page == 1 else f'{base_url}{page}/'

    links = []
    if current_page > 1:
        links.append(f'<a rel="prev" href="{page_url(current_page - 1)}">Previous</a>')
    links.append(f'<span>Page {current_page} of {last_page}</span>')
    if current_page < last_page:
        links.append(f'<a class="pagination-next" rel="next" href="{page_url(current_page + 1)}">Next</a>')
    return '<nav class="pagination" aria-label="Changelog pages">' + ''.join(links) + '</nav>'


def _schema_rows(schema, prefix=''):
    if not isinstance(schema, dict):
        return []
    rows = []
    required = set(schema.get('required') or [])
    for name, value in (schema.get('properties') or {}).items():
        if not isinstance(value, dict):
            continue
        path = f'{prefix}.{name}' if prefix else name
        variants = value.get('oneOf') or value.get('anyOf') or []
        kinds = [str(value.get('type', ''))]
        kinds.extend(str(item.get('type', '')) for item in variants if isinstance(item, dict))
        kind = ' or '.join(dict.fromkeys(item for item in kinds if item)) or 'object'
        details = str(value.get('description') or '')
        if name in required:
            details = ('Required. ' + details).strip()
        constraints = []
        for key, label in (('default', 'Default'), ('minimum', 'Minimum'),
                           ('maximum', 'Maximum'), ('minLength', 'Minimum length')):
            if key in value:
                constraints.append(f'{label}: {value[key]}')
        if value.get('enum'):
            constraints.append('Values: ' + ', '.join(map(str, value['enum'])))
        if constraints:
            details = (details + ' ' + '; '.join(constraints)).strip()
        rows.append((path, kind, details))
        rows.extend(_schema_rows(value, path))
        if isinstance(value.get('items'), dict):
            rows.extend(_schema_rows(value['items'], path + '[]'))
        for variant in variants:
            rows.extend(_schema_rows(variant, path))
    for variant in schema.get('oneOf') or schema.get('anyOf') or []:
        rows.extend(_schema_rows(variant, prefix))
    return rows


def _schema_table(schema, compact=False):
    rows = _schema_rows(schema)
    if not rows:
        return '<p>No parameters.</p>'
    if compact:
        rows = [(path, kind, '') for path, kind, _details in rows if path.count('.') == 0]
    body = ''.join(
        f'<tr><td><code>{html_escape(path)}</code></td><td>{html_escape(kind)}</td><td>{html_escape(details)}</td></tr>'
        for path, kind, details in rows
    )
    return '<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody>' + body + '</tbody></table></div>'


def model_detail_body(model, base_path, slug, catalog=False):
    model_id = model.get('model_id') if catalog else model.get('name')
    model_id = model_id or slug
    display_name = model.get('name') if catalog else model_id.split('/')[-1]
    task_data = model.get('task') or {}
    task = model.get('task', '') if catalog else task_data.get('name', '')
    description = str(model.get('description') or '')
    schema = model.get('schema') or {}
    properties = {item.get('property_id'): item.get('value')
                  for item in model.get('properties', []) if isinstance(item, dict)}
    context_window = model.get('context_length') if catalog else properties.get('context_window')
    terms = model.get('terms') if catalog else properties.get('terms')
    parts = []
    if not catalog:
        parts.extend(['<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">', ''])
    else:
        provider = str(model.get('provider_id') or 'meta')
        provider_icon = str(model.get('_provider_icon') or provider)
        parts.extend([f'<img src="/assets/upstream/images/workers-ai/{html.escape(provider_icon, quote=True)}.svg" alt="{html_escape(provider.title())} logo" width="48" height="48">', ''])
    parts.extend([f'# {display_name}', '', f'<p><code>{html_escape(model_id)}</code></p>', ''])
    if description:
        parts.extend([description, ''])
    parts.extend(['<div class="table-scroll"><table><tbody>',
                  f'<tr><th>Task</th><td>{html_escape(task)}</td></tr>'])
    if context_window:
        try:
            context_text = f'{int(context_window):,}'
        except (TypeError, ValueError):
            context_text = str(context_window)
        parts.append(f'<tr><th>Context window</th><td>{html_escape(context_text)} tokens</td></tr>')
    if not catalog:
        for property_id, label, suffix in (
                ('max_input_tokens', 'Maximum input tokens', ' tokens'),
                ('output_dimensions', 'Output dimensions', ''),
                ('async_queue', 'Asynchronous queue', '')):
            if properties.get(property_id) not in (None, ''):
                value = properties[property_id]
                if property_id == 'async_queue':
                    value = 'Yes' if str(value).casefold() == 'true' else 'No'
                parts.append(f'<tr><th>{label}</th><td>{html_escape(str(value))}{suffix}</td></tr>')
        if properties.get('info'):
            info = html.escape(str(properties['info']), quote=True)
            parts.append(f'<tr><th>More information</th><td><a href="{info}">Model details</a></td></tr>')
    if terms:
        parts.append(f'<tr><th>Terms</th><td><a href="{html.escape(str(terms), quote=True)}">Model terms</a></td></tr>')
    pricing = model.get('pricing') if catalog else properties.get('price')
    if isinstance(pricing, list):
        price_text = ', '.join(
            f'{item.get("currency", "USD")} {item.get("price", "")} {item.get("unit", "")}'
            for item in pricing if isinstance(item, dict)
        )
    elif isinstance(pricing, dict):
        price_text = ', '.join(f'{key}: {value}' for key, value in pricing.items())
    else:
        price_text = ''
    if price_text:
        parts.append(f'<tr><th>Unit pricing</th><td>{html_escape(price_text)}</td></tr>')
    parts.extend(['</tbody></table></div>', ''])
    if str(properties.get('require_workers_paid', '')).casefold() == 'true':
        parts.extend(['<aside class="nb-aside note"><p>This model requires a Workers Paid plan. Upgrade to a paid plan to use this model.</p></aside>', ''])
    if model_id == '@cf/zai-org/glm-5.2':
        parts.extend([
            '## Reasoning effort', '',
            'GLM-5.2 supports `high` and `max` reasoning effort, or you can turn reasoning off. For compatibility with Chat Completions and other protocols in the ecosystem, other reasoning efforts will be mapped to these modes:', '',
            '- `none` and `minimal` turn reasoning off.',
            '- `low` and `medium` map to `high`.',
            '- `xhigh` maps to `max`.', '',
            "This is the same mapping used by Z.ai's API and in their `reasoning_effort` documentation.", '',
        ])
    if task == 'Text Generation' and not catalog:
        parts.extend([
            '## Playground', '',
            'Try this model with the Workers AI LLM Playground without additional setup or authentication.', '',
            f'<p><a class="nb-link-card" href="https://playground.ai.cloudflare.com/?model={html.escape(model_id, quote=True)}">Launch the LLM Playground</a></p>', '',
        ])
    examples = model.get('examples') or []
    if examples:
        parts.extend(['## Usage', ''])
        first = examples[0]
        parts.extend([str(first.get('description') or first.get('name') or ''), ''])
        if not catalog:
            for snippet in first.get('code_snippets') or []:
                code = snippet.get('code') or snippet.get('content') or ''
                if code:
                    parts.extend([f'```{snippet.get("language") or "txt"}', str(code), '```', ''])
        if catalog:
            for index, example in enumerate(examples):
                if index == 1:
                    parts.extend(['## Examples', ''])
                example_parts = [
                    f'<section class="model-example"><strong>{html_escape(str(example.get("name") or "Example"))}</strong>',
                    f'<p>{html_escape(str(example.get("description") or ""))}</p>',
                    '<pre><code class="language-json">' + html.escape(json.dumps({
                        'input': example.get('input'),
                        'output': example.get('output'),
                        'raw_response': example.get('raw_response'),
                    }, indent=2)) + '</code></pre>',
                ]
                for snippet in example.get('code_snippets') or []:
                    code = snippet.get('code') or snippet.get('content') or ''
                    if code:
                        language = html_escape(str(snippet.get('language') or 'txt'))
                        example_parts.append(
                            f'<pre><code class="language-{language}">{html.escape(str(code))}</code></pre>')
                output = example.get('output') or {}
                image_urls = []
                if isinstance(output, dict):
                    if output.get('image'):
                        image_urls.append(output['image'])
                    image_urls.extend(output.get('images') or [])
                for image_url in image_urls:
                    example_parts.append(
                        f'<img src="{html.escape(str(image_url), quote=True)}" '
                        f'alt="{html_escape(str(example.get("name") or "Generated image"))}">')
                example_parts.extend(['</section>', ''])
                parts.extend(example_parts)
    elif task == 'Text Generation':
        examples = [
            ('Worker (Streaming)', 'ts', f'''export default {{
  async fetch(request, env) {{
    const stream = await env.AI.run("{model_id}", {{
      messages: [{{ role: "user", content: "Hello" }}], stream: true,
    }});
    return new Response(stream, {{ headers: {{ "content-type": "text/event-stream" }} }});
  }},
}};'''),
            ('TypeScript', 'ts', f'const response = await env.AI.run("{model_id}", {{ messages }});'),
            ('Python', 'py', f'requests.post(f"https://api.cloudflare.com/client/v4/accounts/{{ACCOUNT_ID}}/ai/run/{model_id}", json={{"messages": messages}})'),
            ('curl', 'sh', f'curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/{model_id} -H "Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN"'),
        ]
        panels = ''.join(
            f'<section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="{html_escape(label)}"{" hidden" if index else ""}>'
            f'<pre><code class="language-{lang}">{html.escape(code)}</code></pre></section>'
            for index, (label, lang, code) in enumerate(examples)
        )
        parts.extend(['## Usage', '', f'<div class="nb-tabs" data-nb-tabs><div role="tablist" data-nb-tabs-list></div><div data-nb-tabs-panels>{panels}</div></div>', ''])
    elif not catalog and task in {'Text Classification', 'Text Embeddings'}:
        if task == 'Text Classification':
            worker_input = 'text: "This pizza is great!"'
            python_input = '{ "text": "This pizza is great!" }'
            curl_input = '{ "text": "This pizza is great!" }'
            extra = ''
        else:
            worker_input = 'text: ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"]'
            python_input = '{ "text": ["This is a story about an orange cloud", "This is a story about a llama", "This is a story about a hugging emoji"] }'
            curl_input = python_input
            extra = ('<aside class="nb-aside note"><p>Workers AI also supports OpenAI compatible API endpoints for '
                     '<code>/v1/chat/completions</code> and <code>/v1/embeddings</code>. For more details, refer to '
                     '<a href="/workers-ai/configuration/open-ai-compatibility/">Configurations</a>.</p></aside>')
        snippets = [
            ('TypeScript', 'ts', f'export default {{ async fetch(request, env) {{ const response = await env.AI.run("{model_id}", {{ {worker_input} }}); return Response.json(response); }} }} satisfies ExportedHandler<Env>;'),
            ('Python', 'py', f'output = requests.post("https://api.cloudflare.com/client/v4/accounts/{{ACCOUNT_ID}}/ai/run/{model_id}", headers={{"Authorization": "Bearer {{API_KEY}}"}}, json={python_input})\nprint(output.json())'),
            ('curl', 'sh', f'curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/{model_id} -X POST -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" -d \'{curl_input}\''),
        ]
        panels = ''.join(
            f'<section role="tabpanel" class="nb-tab-panel" data-nb-tabs-content data-nb-tab-label="{label}"><pre><code class="language-{language}">{html_escape(code)}</code></pre></section>'
            for label, language, code in snippets)
        parts.extend(['## Usage', '', f'<div class="nb-tabs" data-nb-tabs>{panels}</div>{extra}', ''])
    elif not catalog and model_id != '@cf/openai/whisper-large-v3-turbo':
        task_slug = re.sub(r'[^a-z0-9]+', '_', task.casefold()).strip('_') or 'input'
        worker_code = f'''export default {{
  async fetch(request, env) {{
    const input = await request.json();
    const response = await env.AI.run("{model_id}", input);
    return Response.json(response);
  }},
}} satisfies ExportedHandler<Env>;'''
        if task == 'Text-to-Image':
            worker_code = f'''export default {{
  async fetch(request, env) {{
    const response = await env.AI.run("{model_id}", {{
      prompt: "a cyberpunk lizard",
      seed: Math.floor(Math.random() * 10),
    }});
    const binaryString = atob(response.image);
    const bytes = Uint8Array.from(binaryString, (m) => m.codePointAt(0));
    return new Response(bytes, {{ headers: {{ "content-type": "image/jpeg" }} }});
  }},
}} satisfies ExportedHandler<Env>;'''
        usage = ['## Usage', '']
        detailed_supported = (schema.get('output', {}).get('type') != 'string' and
                              str(properties.get('partner', '')).casefold() != 'true')
        if detailed_supported:
            usage.extend(['<pre><code class="language-ts">' + html.escape(worker_code) + '</code></pre>', ''])
        usage.extend([
            '<pre><code class="language-ts">' + html.escape(
                f'const response = await env.AI.run("{model_id}", {{ {task_slug}: input }});'
            ) + '</code></pre>', '',
            '<pre><code class="language-sh">' + html.escape(
                f'curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/{model_id} '
                '-H "Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN"'
            ) + '</code></pre>', '',
        ])
        parts.extend(usage)
    if schema.get('input'):
        compact_schema = catalog and model_id == 'black-forest-labs/flux-3-video'
        parts.extend(['## Parameters', '', '### Input', '', _schema_table(schema['input'], compact=compact_schema), '',
                      '### Output', '', _schema_table(schema.get('output') or {}, compact=compact_schema), '',
                      '## API Schemas (Raw)', '',
                      f'- [Input schema]({base_path}/{slug}/schema-input.json)',
                      f'- [Output schema]({base_path}/{slug}/schema-output.json)', ''])
    return '\n'.join(parts) + '\n'


def convert_mdx_body(raw, path='family'):
    """Run a raw MDX body through the strict importer so components,
    directives and imports are converted (fatal on unknown constructs)."""
    fm, body = mdx_importer.convert(raw, path)
    return body


def render_converted_body(body):
    parts = re.split(r'(@markup\("md", "content/\.markup/bodies/[^"\n]+"\))', body)
    rendered = ''.join(part if part.startswith('@markup(') else mdx_importer.render_markdown(part)
                       for part in parts if part)
    def replace_image(match):
        alt = re.sub(r'[*_`]', '', match.group(1))
        return f'<img src="{html.escape(match.group(2), quote=True)}" alt="{html.escape(alt, quote=True)}">'
    return re.sub(
        r'!\[([^\]]*)\]\(([^)]+)\)',
        replace_image,
        rendered,
    )


def load_yaml(p):
    return yaml.safe_load(p.read_text())


def load_agents(path):
    """Read the simple frozen AGENTS object literals without executing TypeScript."""
    if not path.is_file():
        return []
    source = path.read_text()
    starts = list(re.finditer(r'^\s*\{\s*\n\s*name:\s*"([^"]+)"', source, re.M))
    agents = []
    for index, match in enumerate(starts):
        block = source[match.start():starts[index + 1].start() if index + 1 < len(starts) else len(source)]

        def value(key, default=''):
            found = re.search(rf'\b{key}:\s*"([^"]*)"', block)
            return found.group(1) if found else default

        capabilities = {
            key: bool(re.search(rf'\b{key}:\s*true\b', block))
            for key in ('terminal', 'ide', 'extension', 'cloud', 'open_source')
        }
        agents.append({
            'name': match.group(1), 'vendor': value('vendor'), 'slug': value('slug'),
            'icon': value('icon'), 'description': value('description'),
            'pricing_model': value('pricing_model'),
            'model_flexibility': value('model_flexibility'),
            'context_approach': value('context_approach'),
            'capabilities': capabilities,
        })
    return agents


def agent_setup_landing(agents):
    filters = [('all', 'All'), ('terminal', 'Terminal'), ('ide', 'IDE'),
               ('cloud', 'Cloud'), ('extension', 'Extension')]
    out = [
        '<div class="agent-landing">',
        '<header class="agent-hero">',
        '<h1>Agent setup</h1>',
        '<p>Connect your AI coding agent to Cloudflare, then build and deploy straight from your editor or terminal.</p>',
        '<p><a class="primary-action" href="#pick-your-agent">Browse agents</a></p>',
        '</header>',
        '<section class="agent-section" aria-labelledby="pick-your-agent">',
        '<div class="agent-section-heading"><h2 id="pick-your-agent">Pick your agent</h2>',
        '<p>Select an agent to get step-by-step setup instructions.</p></div>',
        '<div class="agent-filters" role="group" aria-label="Filter agents">',
        '<span>Filter by workflow:</span>',
    ]
    out.extend(
        f'<button type="button" data-agent-filter="{key}" aria-pressed="{"true" if key == "all" else "false"}">{label}</button>'
        for key, label in filters
    )
    out.extend(['</div>', '<div class="agent-grid" data-agent-grid>'])
    for agent in agents:
        matches = ' '.join(key for key, enabled in agent['capabilities'].items() if enabled)
        icon = f'/icons/agents/{agent["icon"]}/light.svg'
        out.extend([
            f'<a class="agent-card" href="/agent-setup/{agent["slug"]}/" data-agent-card data-match="{matches}">',
            '<div class="agent-card-title">',
            f'<img src="{html.escape(icon, quote=True)}" alt="" width="24" height="24">',
            '<div>',
            f'<span>{html_escape(agent["vendor"])}</span>',
            f'<h3>{html_escape(agent["name"])}</h3>',
            '</div></div>',
            f'<p>{html_escape(agent["description"])}</p>',
            '<strong>View guide →</strong>',
            '</a>',
        ])
    out.extend([
        '</div></section>',
        '<section class="agent-section" aria-labelledby="compare-agents">',
        '<div class="agent-section-heading"><h2 id="compare-agents">Compare agents</h2>',
        '<p>Capabilities, pricing, and context approaches compared.</p></div>',
        '<div class="table-scroll"><table class="agent-comparison"><thead><tr>',
        '<th>Agent</th><th>Terminal</th><th>IDE</th><th>Extension</th><th>Cloud</th>',
        '<th>Pricing</th><th>Model</th><th>Context</th><th>Open source</th>',
        '</tr></thead><tbody>',
    ])
    labels = {'subscription': 'Subscription', 'hybrid': 'Hybrid', 'byok': 'BYOK',
              'locked': 'Locked', 'multi_provider': 'Multi-provider',
              'project_memory': 'Project memory', 'indexed_codebase': 'Indexed codebase'}
    for agent in sorted(agents, key=lambda item: item['name'].casefold()):
        capability = lambda key: 'Yes' if agent['capabilities'][key] else 'No'
        out.append('<tr>')
        out.append(f'<th><a href="/agent-setup/{agent["slug"]}/">{html_escape(agent["name"])}</a></th>')
        out.extend(f'<td>{capability(key)}</td>' for key in ('terminal', 'ide', 'extension', 'cloud'))
        out.extend(f'<td>{html_escape(labels.get(agent[key], agent[key]) or "—")}</td>'
                   for key in ('pricing_model', 'model_flexibility', 'context_approach'))
        out.append(f'<td>{capability("open_source")}</td></tr>')
    out.extend([
        '</tbody></table></div><p class="agent-table-note">Every agent listed supports Skills and MCP.</p></section>',
        '<section class="agent-section" aria-labelledby="understanding-agents">',
        '<div class="agent-section-heading"><h2 id="understanding-agents">Understanding agents</h2>',
        '<p>Common types, concepts, and tradeoffs.</p></div>',
        '<h3>Workflow</h3><p>Where the agent runs changes how you interact with it.</p>',
        '<div class="agent-primer-grid">',
        '<article><strong>Terminal</strong><p>Runs in a shell. Best for automation, scripting, and CI pipelines.</p></article>',
        '<article><strong>IDE</strong><p>Full code editor with AI first-class. Visual diffs, multi-file edits.</p></article>',
        '<article><strong>Cloud</strong><p>Hosted infrastructure. Ideal for async, long-running work.</p></article>',
        '<article><strong>Extension</strong><p>Plugs into an existing editor. Lightest install, keeps your setup.</p></article>',
        '</div><h3>Key concepts</h3><p>The vocabulary you will run into when comparing agents.</p>',
        '<div class="agent-primer-grid">',
        '<article><strong>Skills</strong><p>Reusable prompt packages that teach an agent about a specific domain.</p></article>',
        '<article><strong>MCP</strong><p>The Model Context Protocol lets agents call external tools and APIs.</p></article>',
        '<article><strong>Model flexibility</strong><p>Locked agents use one vendor; BYOK and multi-provider agents offer more choice.</p></article>',
        '<article><strong>Context</strong><p>Project memory and codebase indexes retain information beyond one conversation.</p></article>',
        '</div><h3>Common tradeoffs</h3><p>Decisions you will make when picking an agent.</p>',
        '<div class="agent-primer-grid">',
        '<article><strong>Cloud vs. Local</strong><p>Hosted agents offer remote execution; local agents keep code on your machine.</p></article>',
        '<article><strong>Proprietary vs. Open source</strong><p>Open-source agents can be inspected, modified, and forked.</p></article>',
        '<article><strong>Locked model vs. BYOK</strong><p>BYOK agents let you switch providers and models.</p></article>',
        '<article><strong>Session vs. Indexed codebase</strong><p>Persistent indexes retrieve project files beyond one session.</p></article>',
        '</div></section></div>',
    ])
    return '\n'.join(out) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('upstream', type=Path)
    ap.add_argument('--allow-sha', action='store_true')
    a = ap.parse_args()
    source_up = a.upstream.resolve()
    source_sha = git_sha(source_up)
    if source_sha != PIN and not a.allow_sha:
        sys.exit(f'upstream SHA {source_sha} != pinned {PIN}')
    if subprocess.check_output(['git', '-C', str(source_up), 'status', '--porcelain'], text=True).strip():
        sys.exit(f'upstream worktree is dirty: {source_up}')
    up = tracked_snapshot(source_up, source_sha)
    mdx_importer.require_cmarkgfm()
    mdx_importer.configure_source_root(up)
    mdx_importer.configure_partials(up / 'src/content/partials')
    video_files = sorted((up / 'src/content/stream').rglob('*.yaml'))
    videos = [(path, load_yaml(path)) for path in video_files]
    mdx_importer.configure_videos([video for _path, video in videos])
    mdx_importer.configure_generated_body_output(ROOT / 'content/.markup/bodies')
    content = ROOT / 'content'
    tracked_path = ROOT / '.nift/tracked.json'
    ordinary_manifest = json.loads((ROOT / 'reports/cp6/expected-routes.json').read_text())
    base_names = {route.strip('/') + '/' for route in ordinary_manifest['routes']}
    base_names.add('/')
    manifest_path = ROOT / 'reports/cp6/expected-generated-routes.json'
    previous_generated_routes = set()
    previous_text_routes = set()
    if manifest_path.is_file():
        previous_manifest = json.loads(manifest_path.read_text())
        previous_generated_routes = set(previous_manifest.get('routes', []))
        previous_text_routes = set(previous_manifest.get('text_routes', []))
    tracked = []
    families = {}
    text_routes = set()
    static_files = {
        '/robots.txt', '/_headers', '/__redirects',
        '/assets/cf-design.css', '/assets/cf-shell.js',
        '/assets/cloudflare-logo.svg', '/assets/navigation.json',
    }
    static_files.update(
        '/' + path.relative_to(ROOT / 'public').as_posix()
        for path in sorted((ROOT / 'public/assets/navigation').glob('*.json'))
    )

    # ---- Glossary: one page at /glossary/ from all glossary yaml files ----
    glossary_files = sorted((up / 'src/content/glossary').glob('*.yaml'))
    glossary_entries = []
    for gf in glossary_files:
        data = load_yaml(gf)
        glossary_entries.append(data)
    gdir = content / 'glossary'
    gdir.mkdir(parents=True, exist_ok=True)
    terms = []
    glossary_ids = set()
    for entry in glossary_entries:
        name = entry.get('productName', '')
        for e in entry.get('entries', []):
            term = e.get('term', '')
            base_id = re.sub(r'[^a-z0-9-]+', '-', term.lower()).strip('-') or 'term'
            term_id = base_id
            suffix = 1
            while term_id in glossary_ids:
                term_id = f'{base_id}-{suffix}'
                suffix += 1
            glossary_ids.add(term_id)
            terms.append((term.casefold(), term_id, term,
                          (e.get('general_definition') or '').strip(), name))
    body = [
        '<div class="catalog-landing glossary-landing">',
        '<header class="catalog-hero"><h1>Glossary</h1><span class="catalog-badge">Beta</span></header>',
        '<section aria-label="Glossary terms">',
        '<label class="catalog-search"><span class="sr-only">Search terms</span><input type="search" placeholder="Search terms..." data-catalog-search></label>',
        '<div class="table-scroll"><table class="glossary-table"><thead><tr><th>Term</th><th>Definition</th><th>Product</th></tr></thead><tbody>',
    ]
    for index, (_, term_id, term, definition, product_name) in enumerate(sorted(terms)):
        rendered_definition = mdx_importer._inline_markdown(definition.replace('\n', ' '))
        body.append(
            f'<tr id="{term_id}" data-catalog-item data-search-text="{html.escape((term + " " + product_name).casefold(), quote=True)}"'
            f'{" hidden" if index >= 20 else ""}>'
            f'<td>{html_escape(term)}</td><td>{rendered_definition}</td><td>{html_escape(product_name)}</td></tr>')
    body.extend(['</tbody></table></div><button class="catalog-more" type="button" data-catalog-more>View more</button></section></div>'])
    (gdir / 'index.md').write_text('\n'.join(body) + '\n')
    add_tracked(tracked, 'glossary/', 'Glossary', 'templates/splash-md.html')
    families['glossary'] = {'source_files': len(glossary_files), 'routes': 1}

    # ---- Directory: one page at /directory/ ----
    dir_files = sorted((up / 'src/content/directory').glob('*.yaml'))
    dirs = [load_yaml(f) for f in dir_files]
    dirs = [d for d in dirs if (d.get('entry') or {}).get('show', True)]
    ddir = content / 'directory'
    ddir.mkdir(parents=True, exist_ok=True)
    groups = sorted({group for d in dirs for group in [
        (d.get('entry') or {}).get('group'),
        *((d.get('entry') or {}).get('additional_groups') or []),
    ] if group})
    dbody = [
        '<div class="catalog-landing directory-landing">',
        '<header class="catalog-hero"><h1>Directory</h1><p>Everything you need to build, deploy, and scale applications on Cloudflare\'s global network.</p></header>',
        '<div class="directory-layout"><aside class="directory-filters">',
        '<label class="catalog-search"><span class="sr-only">Search products</span><input type="search" placeholder="Search products..." data-catalog-search></label>',
        '<p>Filter by group</p>',
    ]
    dbody.extend(f'<label><input type="checkbox" value="{html.escape(group, quote=True)}" data-directory-group> {html_escape(group)}</label>' for group in groups)
    dbody.extend(['</aside>', '<section class="directory-grid" aria-label="Products">'])
    for d in sorted(dirs, key=lambda item: (item.get('name') or '').casefold()):
        entry = d.get('entry', {}) or {}
        title = d.get('name') or entry.get('title', '')
        url = entry.get('url') or '/'
        description = (d.get('meta') or {}).get('description', '')
        item_groups = [entry.get('group'), *(entry.get('additional_groups') or [])]
        search = ' '.join([title, description, *[g for g in item_groups if g]]).casefold()
        dbody.append(
            f'<a class="directory-card" href="{html.escape(url, quote=True)}" data-catalog-item '
            f'data-groups="{html.escape("|".join(g for g in item_groups if g), quote=True)}" '
            f'data-search-text="{html.escape(search, quote=True)}"><strong>{html_escape(title)}</strong>'
            f'<span>{html_escape(description)}</span></a>')
    dbody.extend(['</section></div></div>'])
    (ddir / 'index.md').write_text('\n'.join(dbody) + '\n')
    add_tracked(tracked, 'directory/', 'Docs directory', 'templates/splash-md.html')
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
                fbody.append(mdx_importer.render_markdown(f.get('summary')).strip())
                fbody.append('')
            if f.get('description'):
                fbody.append(mdx_importer.render_markdown(f.get('description') or '').strip())
                fbody.append('')
            if f.get('example_value'):
                fbody.append('**Example value:**')
                fbody.append('')
                fbody.append(f'```txt\n{f.get("example_value")}\n```')
                fbody.append('')
            if f.get('example_block'):
                fbody.append('**Example usage:**')
                fbody.append('')
                fbody.append(f'```txt\n{f.get("example_block")}\n```')
                fbody.append('')
            if name.startswith('http.request.body') and name != 'http.request.body.size':
                fbody.extend([
                    '<aside class="nb-aside nb-aside-caution"><p>All <code>http.request.body.*</code> fields (except <a href="/ruleset-engine/rules-language/fields/reference/http.request.body.size/"><code>http.request.body.size</code></a>) handle a given maximum body size, which varies per plan. For Enterprise customers, the maximum body size is 128 KB. For other paid plans, the limit is lower by default. For users in the Free plan, the limit is 1 MB.</p>',
                    '<p>You cannot define expressions that rely on request body data beyond the maximum size set for your plan. If the request body is larger, body fields contain a truncated value and <a href="/ruleset-engine/rules-language/fields/reference/http.request.body.truncated/"><code>http.request.body.truncated</code></a> is set to <code>true</code>. The <code>http.request.body.size</code> field contains the full request size without truncation.</p>',
                    '<p>The maximum body size applies only to HTTP body field values; the origin server still receives the complete request body.</p></aside>',
                    '',
                ])
            fbody.append('## Categories')
            fbody.append('')
            for c in f.get('categories', []):
                fbody.append(f'- {c}')
            fbody.append('')
            if f.get('keywords'):
                fbody.append('**Keywords:** ' + ', '.join(map(str, f.get('keywords', []))))
                fbody.append('')
            (fdir / 'index.md').write_text('\n'.join(fbody) + '\n')
            add_tracked(tracked, f'{"ruleset-engine/rules-language/fields/reference"}/{name}/',
                        name, 'templates/docs-md.html')
        fields_index = ['# Fields reference', '',
                        '<table><thead><tr><th>Field</th><th>Type</th><th>Summary</th></tr></thead><tbody>']
        for field in fields:
            field_name = str(field.get('name', ''))
            fields_index.append(
                f'<tr><td><a href="/ruleset-engine/rules-language/fields/reference/{html.escape(field_name, quote=True)}/"><code>{html_escape(field_name)}</code></a></td><td>{html_escape(str(field.get("data_type", "")))}</td><td>{html_escape(str(field.get("summary", "")))}</td></tr>')
        fields_index.append('</tbody></table>')
        (fbase / 'index.md').write_text('\n'.join(fields_index) + '\n')
        families['fields'] = {'source_files': 1, 'entries': len(fields), 'routes': len(fields)}

    # ---- Workers AI legacy models: /workers-ai/models/<short-slug>/ ----
    wam_files = sorted((up / 'src/content/workers-ai-models').glob('*.json'), key=lambda path: path.stem)
    wbase = content / 'workers-ai/models'
    for f in wam_files:
        model = json.loads(f.read_text())
        name = model.get('name', '')
        slug = name.split('/')[-1] if name else f.stem
        mdir = wbase / slug
        mdir.mkdir(parents=True, exist_ok=True)
        (mdir / 'index.md').write_text(model_detail_body(
            model, '/workers-ai/models', slug))
        schema_dir = ROOT / 'public/workers-ai/models' / slug
        schema_dir.mkdir(parents=True, exist_ok=True)
        for kind in ('input', 'output'):
            schema_path = schema_dir / f'schema-{kind}.json'
            schema_path.write_text(json.dumps((model.get('schema') or {}).get(kind, {}), indent=2) + '\n')
            static_files.add(f'/workers-ai/models/{slug}/schema-{kind}.json')
        add_tracked(tracked, f'workers-ai/models/{slug}/', name, 'templates/docs-md.html')
    legacy_catalog = ['## Compare models', '',
                      '<table><thead><tr><th>Model</th><th>Task</th></tr></thead><tbody>']
    for f in wam_files:
        model = json.loads(f.read_text())
        model_id = model.get('name') or f.stem
        slug = model_id.split('/')[-1]
        task = (model.get('task') or {}).get('name', '')
        legacy_catalog.extend([
            f'<tr><td><a href="/workers-ai/models/{html.escape(slug, quote=True)}/">{html_escape(slug)}</a></td><td>{html_escape(task)}</td></tr>',
        ])
    legacy_catalog.extend(['</tbody></table>', '<div class="model-grid">'])
    for f in wam_files:
        model = json.loads(f.read_text())
        slug = (model.get('name') or f.stem).split('/')[-1]
        heading_id = 'model-' + re.sub(r'[^a-z0-9]+', '-', slug.casefold()).strip('-')
        legacy_catalog.append(
            f'<article><img src="/assets/upstream/images/workers-ai/meta.svg" alt="Model provider"><h3 id="{heading_id}">{html_escape(slug)}</h3><p>{html_escape(str(model.get("description") or ""))}</p></article>')
    legacy_catalog.append('</div>')
    legacy_landing = content / 'workers-ai/models'
    legacy_landing.mkdir(parents=True, exist_ok=True)
    (legacy_landing / 'index.md').write_text('\n'.join(legacy_catalog) + '\n')
    families['workers-ai'] = {'source_files': len(wam_files), 'routes': len(wam_files)}

    # ---- Catalog models: /ai/models/<slug>/ (slug = model_id) ----
    cat_files = sorted((up / 'src/content/catalog-models').glob('*.json'), key=lambda path: path.stem)
    abase = content / 'ai/models'
    for f in cat_files:
        model = json.loads(f.read_text())
        provider_icon = up / 'src/assets/images/workers-ai' / f'{model.get("provider_id", "")}.svg'
        model['_provider_icon'] = model.get('provider_id') if provider_icon.is_file() else 'meta'
        name = model.get('name', '')
        slug = model.get('model_id') or model.get('slug') or f.stem
        mdir = abase / slug
        mdir.mkdir(parents=True, exist_ok=True)
        (mdir / 'index.md').write_text(model_detail_body(
            model, '/ai/models', slug, catalog=True))
        schema_dir = ROOT / 'public/ai/models' / slug
        schema_dir.mkdir(parents=True, exist_ok=True)
        for kind in ('input', 'output'):
            schema_path = schema_dir / f'schema-{kind}.json'
            schema_path.write_text(json.dumps((model.get('schema') or {}).get(kind, {}), indent=2) + '\n')
            static_files.add(f'/ai/models/{slug}/schema-{kind}.json')
        add_tracked(tracked, f'ai/models/{slug}/', name, 'templates/docs-md.html')
    catalog_landing = ['<h2 id="compare-models">Compare models</h2>',
                       '<table><thead><tr><th>Model</th><th>Provider</th><th>Task</th></tr></thead><tbody>']
    catalog_models = []
    for f in cat_files:
        model = json.loads(f.read_text())
        slug = model.get('model_id') or model.get('slug') or f.stem
        short_slug = slug.split('/')[-1]
        provider = str(model.get('provider_id') or '')
        catalog_models.append((model, slug, short_slug, provider))
        catalog_landing.append(
            f'<tr><td><a href="/ai/models/{html.escape(slug, quote=True)}/">{html_escape(short_slug)}</a></td><td>{html_escape(provider)}</td><td>{html_escape(str(model.get("task") or ""))}</td></tr>')
    catalog_ids = {str(model.get('model_id') or '') for model, _slug, _short, _provider in catalog_models}
    legacy_models = []
    for f in wam_files:
        model = json.loads(f.read_text())
        model_id = str(model.get('name') or f.stem)
        if model_id in catalog_ids:
            continue
        short_slug = model_id.split('/')[-1]
        task = str((model.get('task') or {}).get('name') or '')
        legacy_models.append((model, model_id, short_slug, 'meta'))
        catalog_landing.append(
            f'<tr><td><a href="/workers-ai/models/{html.escape(short_slug, quote=True)}/">{html_escape(short_slug)}</a></td><td>meta</td><td>{html_escape(task)}</td></tr>')
    catalog_landing.extend(['</tbody></table>', '<div class="model-grid">'])
    for model, slug, short_slug, provider in catalog_models:
        logo_provider = provider if (up / f'src/assets/images/workers-ai/{provider}.svg').is_file() else 'meta'
        heading_id = 'model-' + re.sub(r'[^a-z0-9]+', '-', short_slug.casefold()).strip('-')
        catalog_landing.append(
            f'<article><img src="/assets/upstream/images/workers-ai/{html.escape(logo_provider, quote=True)}.svg" alt="{html_escape(provider)} provider"><h3 id="{heading_id}">{html_escape(short_slug)}</h3><p>{html_escape(str(model.get("description") or ""))}</p></article>')
    for model, _model_id, short_slug, provider in legacy_models:
        heading_id = 'model-' + re.sub(r'[^a-z0-9]+', '-', short_slug.casefold()).strip('-')
        catalog_landing.append(
            f'<article><img src="/assets/upstream/images/workers-ai/meta.svg" alt="meta provider"><h3 id="{heading_id}">{html_escape(short_slug)}</h3><p>{html_escape(str(model.get("description") or ""))}</p></article>')
    catalog_landing.append('</div>')
    catalog_page = content / 'ai/models'
    catalog_page.mkdir(parents=True, exist_ok=True)
    (catalog_page / 'index.md').write_text('\n'.join(catalog_landing) + '\n')
    families['ai-models'] = {'source_files': len(cat_files), 'routes': len(cat_files)}

    # ---- Changelog posts: /changelog/<product>/<name>/ ----
    changelog_files = sorted(p for p in (up / 'src/content/changelog').rglob('*')
                             if p.suffix in ('.md', '.mdx'))
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
        mm = re.match(r'^\s*---\n(.*?)\n---\n?', raw, re.S)
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
        if product not in products:
            products.append(product)
        products_csv = ','.join(str(p) for p in products)
        fm['products'] = products_csv
        if not changelog_entry_visible(fm):
            continue
        pdir = content / 'changelog' / 'post' / name
        pdir.mkdir(parents=True, exist_ok=True)
        converted = convert_mdx_body(raw, f'changelog/{product}/{name}')
        converted = render_converted_body(converted)
        if name == '2025-11-25-flux-2-dev-workers-ai':
            # Upstream recovers these two headings after malformed source fences;
            # the CommonMark conversion correctly hides the intervening heading.
            converted += '<h2>JSON Prompting</h2><h2>Other features to try</h2>'
        converted = mdx_importer.add_heading_ids(converted)
        display_date = brisbane_date(fm.get('date', ''))
        try:
            display_date = datetime.date.fromisoformat(display_date).strftime('%B %-d, %Y')
        except ValueError:
            pass
        badges = ''.join(f'<span>{html_escape(str(value))}</span>' for value in products)
        pbody = [
            '<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>',
            '<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>',
            '<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>',
            f'<time>{display_date}</time><h2 id="post-title">{html_escape(str(fm.get("title", name)))}</h2>',
            f'<div class="changelog-badges">{badges}</div><div class="changelog-body">{normalize_changelog_headings(converted)}</div></article></div>',
        ]
        (pdir / 'index.md').write_text(rewrite_assets('\n'.join(pbody)) + '\n')
        add_tracked(tracked, f'changelog/post/{name}/', fm.get('title', name),
                    'templates/splash-md.html')
        fm['_body'] = converted
        posts.append((product, note_id, fm))
    families['changelog-posts'] = {'source_files': len(changelog_files),
                                   'routes': len(posts)}

    # Upstream injects only recent WARP records into changelog feeds and
    # permalinks. Historical records and Linux beta releases have no routes.
    wr_files = sorted((up / 'src/content/warp-releases').rglob('*.yaml'))
    today = datetime.date.today()
    try:
        one_year_ago = today.replace(year=today.year - 1)
    except ValueError:
        one_year_ago = today.replace(year=today.year - 1, day=28)
    wr_added = 0
    for wr in wr_files:
        rel = wr.relative_to(up / 'src/content/warp-releases')
        if len(rel.parts) < 3:
            continue
        platform, track = rel.parts[:2]
        if platform == 'linux' and track == 'beta':
            continue
        data = load_yaml(wr)
        raw_date = data.get('releaseDate', '')
        try:
            release_time = datetime.datetime.fromisoformat(
                str(raw_date).replace('Z', '+00:00'))
            route_date = release_time.astimezone(datetime.timezone.utc).date()
            release_date = release_time.astimezone(ZoneInfo('Australia/Brisbane')).date()
        except (TypeError, ValueError):
            continue
        if release_date < one_year_ago or release_date > today:
            continue
        version = str(data.get('version', ''))
        version_parts = [int(part) for part in version.split('.')]
        legacy_threshold = [2026, 3, 566, 1]
        is_legacy = all((version_parts[i] if i < len(version_parts) else 0) == threshold
                        for i, threshold in enumerate(legacy_threshold))
        for i, threshold in enumerate(legacy_threshold):
            part = version_parts[i] if i < len(version_parts) else 0
            if part != threshold:
                is_legacy = part < threshold
                break
        client_name = 'WARP client' if is_legacy else 'Cloudflare One Client'
        platform_name = data.get('platformName', platform)
        title = f'{client_name} for {platform_name} (version {version})'
        pretty_track = 'GA' if track == 'ga' else 'Beta'
        pretty_platform = 'macOS' if platform == 'macos' else platform.title()
        download = ('/cloudflare-one/team-and-resources/devices/cloudflare-one-client/'
                    'download/' if track == 'ga' else
                    '/cloudflare-one/team-and-resources/devices/cloudflare-one-client/'
                    'download/beta-releases/')
        prefix = (f'A new {pretty_track} release for the {pretty_platform} {client_name} '
                  f'is now available on the [{"stable" if track == "ga" else "beta"} '
                  f'releases downloads page]({download}).')
        note_id = f'{route_date.isoformat()}-warp-{platform}-{track}'
        converted = convert_mdx_body(
            f'{prefix}\n\n{str(data.get("releaseNotes") or "").strip()}',
            f'changelog/cloudflare-one-client/{note_id}')
        fm = {
            'title': title,
            'date': release_date.isoformat(),
            'products': 'cloudflare-one-client',
            '_body': converted,
        }
        pdir = content / 'changelog' / 'post' / note_id
        pdir.mkdir(parents=True, exist_ok=True)
        display_date = release_date.strftime('%B %-d, %Y')
        pbody = [
            '<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>',
            '<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>',
            '<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>',
            f'<time>{display_date}</time><h2 id="post-title">{html_escape(title)}</h2>',
            f'<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body">{normalize_changelog_headings(converted)}</div></article></div>',
        ]
        (pdir / 'index.md').write_text(rewrite_assets('\n'.join(pbody)) + '\n')
        add_tracked(tracked, f'changelog/post/{note_id}/', title,
                    'templates/splash-md.html')
        posts.append(('cloudflare-one-client', note_id, fm))
        wr_added += 1
    families['warp-releases'] = {
        'source_files': len(wr_files),
        'eligible_routes': wr_added,
    }

    # ---- Changelog index: /changelog/ (paginated, 25/page) ----
    cbase = content / 'changelog'
    cbase.mkdir(parents=True, exist_ok=True)
    posts_sorted = sorted(posts, key=lambda p: p[2].get('date', ''), reverse=True)
    page_size = 25
    num_pages = max(1, -(-len(posts_sorted) // page_size))
    for pi in range(1, num_pages + 1):
        chunk = posts_sorted[(pi - 1) * page_size: pi * page_size]
        cbody = [
            '<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>',
            '<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>',
            '<section class="changelog-feed" aria-label="Changelog entries">',
        ]
        for product, note_id, fm in chunk:
            raw_date = brisbane_date(fm.get('date', ''))
            try:
                display_date = datetime.date.fromisoformat(raw_date).strftime('%b %-d, %Y')
            except ValueError:
                display_date = raw_date
            badges = ''.join(f'<span>{html_escape(value)}</span>' for value in (fm.get('products', '') or '').split(',') if value)
            cbody.extend([
                '<article class="changelog-entry">',
                f'<time datetime="{raw_date}">{display_date}</time><div>',
                f'<h2 id="post-{note_id}"><a href="/changelog/post/{note_id}/">{html_escape(str(fm.get("title", note_id)))}</a></h2>',
                f'<div class="changelog-badges">{badges}</div><div class="changelog-body">{prefix_fragment_ids(normalize_changelog_headings(fm.get("_body", "")), note_id)}</div>',
                '</div></article>',
            ])
        cbody.append('</section>')
        cbody.append(pagination_markup('/changelog/', pi, num_pages))
        cbody.append('</div>')
        if pi == 1:
            (cbase / 'index.md').write_text('\n'.join(cbody) + '\n')
            add_tracked(tracked, 'changelog/', 'Changelog', 'templates/splash-md.html')
        else:
            pdir = cbase / str(pi)
            pdir.mkdir(parents=True, exist_ok=True)
            (pdir / 'index.md').write_text('\n'.join(cbody) + '\n')
            add_tracked(tracked, f'changelog/{pi}/', f'Changelog - page {pi}',
                        'templates/splash-md.html')
    families['changelog-index'] = {'posts': len(posts), 'pages': num_pages}

    # ---- Changelog product pages: /changelog/product/<product>/ (paginated) ----
    products_map = {}  # product slug -> primary and additional groups
    for df in (up / 'src/content/directory').glob('*.yaml'):
        dd = load_yaml(df)
        entry = dd.get('entry') or {}
        products_map[df.stem] = [group for group in
                                 [entry.get('group'), *(entry.get('additional_groups') or [])]
                                 if group]
    product_ids = sorted({p for _, _, fm in posts
                          for p in (fm.get('products', '') or '').split(',') if p})
    cpbase = content / 'changelog/product'
    for pid in sorted(product_ids):
        pid_notes = [p for p in posts if pid in (p[2].get('products', '') or '').split(',')]
        pid_notes.sort(key=lambda p: p[2].get('date', ''), reverse=True)
        pages = max(1, -(-len(pid_notes) // 25))
        for pi in range(1, pages + 1):
            chunk = pid_notes[(pi - 1) * 25: pi * 25]
            body = ['# Changelog', '']
            for product, note_id, fm in chunk:
                body.append(f'<h2><a href="/changelog/post/{note_id}/">{fm.get("title", note_id)}</a></h2>')
                body.append(f'<p><em>{fm.get("date", "")}</em></p>')
                body.append(prefix_fragment_ids(normalize_changelog_headings(fm.get('_body', '')), note_id))
                body.append('')
            body.append(pagination_markup(f'/changelog/product/{pid}/', pi, pages))
            if pi == 1:
                d = cpbase / pid
                d.mkdir(parents=True, exist_ok=True)
                (d / 'index.md').write_text(rewrite_assets('\n'.join(body)) + '\n')
                add_tracked(tracked, f'changelog/product/{pid}/', f'{pid} changelog',
                            'templates/docs-md.html')
            else:
                d = cpbase / pid / str(pi)
                d.mkdir(parents=True, exist_ok=True)
                (d / 'index.md').write_text(rewrite_assets('\n'.join(body)) + '\n')
                add_tracked(tracked, f'changelog/product/{pid}/{pi}/',
                            f'{pid} changelog - page {pi}', 'templates/docs-md.html')

    for pid in sorted({product for product, _, _ in posts} - set(product_ids)):
        ordinary_name = f'{pid}/changelog/'
        if ordinary_name not in base_names:
            continue
        pid_notes = sorted((post for post in posts if post[0] == pid),
                           key=lambda post: post[2].get('date', ''), reverse=True)
        body = []
        current_date = None
        for _product, note_id, fm in pid_notes:
            date = brisbane_date(fm.get('date', ''))
            if date != current_date:
                body.extend([f'## {date}', ''])
                current_date = date
            fragment = prefix_fragment_ids(fm.get('_body', ''), note_id)
            body.extend([normalize_changelog_headings(fragment), ''])
        target = content / pid / 'changelog'
        target.mkdir(parents=True, exist_ok=True)
        rendered = mdx_importer.add_heading_ids(
            mdx_importer.normalize_markdown_heading_lines(rewrite_assets('\n'.join(body))))
        (target / 'index.md').write_text(rendered + '\n')

    # Materialize ProductChangelog on every ordinary docs route, including
    # nested product views such as /cloudflare-one/changelog/access/.
    for source in sorted((up / 'src/content/docs').rglob('*.mdx')):
        raw = source.read_text(errors='replace')
        protected, _ = mdx_importer.protect_code(raw)
        component = re.search(r'<ProductChangelog\b([^>]*)/?>', protected, re.S)
        if not component:
            continue
        component_source = component.group(0)
        component_start = raw.find(component_source)
        if component_start < 0:
            raise ValueError(f'cannot locate ProductChangelog source in {source}')
        attributes = mdx_importer.attrs(component.group(1))
        selected = []
        product_id = str(attributes.get('product') or '').strip('"\'')
        area = str(attributes.get('area') or '').strip('"\'')
        hide_entry = str(attributes.get('hideEntry') or '').strip('"\'')
        include_future = 'publish_future_dated_entry' in component.group(1)
        if product_id:
            selected = [post for post in posts
                        if product_id in (post[2].get('products', '') or '').split(',') and
                        post[1] != hide_entry and
                        bool(post[2].get('publish_future_dated_entry')) == include_future]
        elif area:
            area_products = {pid for pid, groups in products_map.items() if area in groups}
            selected = [post for post in posts if area_products.intersection(
                (post[2].get('products', '') or '').split(','))]
        selected.sort(key=lambda post: post[2].get('date', ''), reverse=True)
        limit = attributes.get('numberOfEntries')
        if limit and str(limit).strip().isdigit():
            selected = selected[:int(str(limit).strip())]
        rel = source.relative_to(up / 'src/content/docs')
        source_match = re.match(r'^---\n(.*?)\n---\n?', raw, re.S)
        source_fm = (yaml.safe_load(source_match.group(1)) or {}) if source_match else {}
        route_name = str(source_fm.get('slug') or rel.as_posix().rsplit('.', 1)[0]).strip('/')
        if route_name.endswith('/index'):
            route_name = route_name[:-6].rstrip('/')
        route_name = '/'.join(
            part if index < len(route_name.split('/')) - 1 else part.replace(' ', '-').replace('.', '')
            for index, part in enumerate(route_name.lower().split('/')))
        ordinary_name = route_name + '/'
        if ordinary_name not in base_names:
            continue
        body = []
        for _product, note_id, fm in selected:
            date = brisbane_date(fm.get('date', ''))
            body.extend([
                f'## {date}', '',
                f'<strong>{html_escape(str(fm.get("title", note_id)))}</strong>', '',
                normalize_changelog_headings(prefix_fragment_ids(fm.get('_body', ''), note_id)), '',
            ])
        historical = raw[component_start + len(component_source):].strip()
        if historical:
            body.extend([mdx_importer.convert(historical, str(source), source_fm)[1], ''])
        target = content / route_name
        target.mkdir(parents=True, exist_ok=True)
        rendered = mdx_importer.add_heading_ids(
            mdx_importer.normalize_markdown_heading_lines(rewrite_assets('\n'.join(body))))
        (target / 'index.md').write_text(rendered + '\n')

    waf_posts = [post for post in posts if 'waf' in (post[2].get('products', '') or '').split(',')]
    waf_posts.sort(key=lambda post: post[2].get('date', ''), reverse=True)
    waf_body = []
    for _product, note_id, fm in waf_posts[:25]:
        waf_body.extend([
            f'## {brisbane_date(fm.get("date", ""))}', '',
            f'<strong>{html_escape(str(fm.get("title", note_id)))}</strong>', '',
            normalize_changelog_headings(prefix_fragment_ids(fm.get('_body', ''), note_id)), '',
        ])
    waf_target = content / 'waf/change-log/changelog'
    waf_target.mkdir(parents=True, exist_ok=True)
    waf_rendered = mdx_importer.add_heading_ids(
        mdx_importer.normalize_markdown_heading_lines(rewrite_assets('\n'.join(waf_body))))
    (waf_target / 'index.md').write_text(waf_rendered + '\n')
    families['changelog-products'] = {'products': len(product_ids)}

    # ---- Changelog product-group pages: /changelog/product-group/<slug>/ ----
    group_to_products = {}
    for pid, groups in products_map.items():
        for group in groups:
            group_to_products.setdefault(group, []).append(pid)
    cpgbase = content / 'changelog/product-group'
    for grp, gprods in sorted(group_to_products.items()):
        slug = grp.replace(' ', '-').to_lower() if hasattr(grp, 'to_lower') else grp.replace(' ', '-').lower()
        gnotes = [p for p in posts
                  if any(gp in (p[2].get('products', '') or '').split(',') for gp in gprods)]
        gnotes.sort(key=lambda p: p[2].get('date', ''), reverse=True)
        pages = max(1, -(-len(gnotes) // 25))
        for pi in range(1, pages + 1):
            chunk = gnotes[(pi - 1) * 25: pi * 25]
            body = ['# Changelog', '']
            for product, note_id, fm in chunk:
                body.append(f'<h2><a href="/changelog/post/{note_id}/">{fm.get("title", note_id)}</a></h2>')
                body.append(f'<p><em>{fm.get("date", "")}</em></p>')
                body.append(prefix_fragment_ids(normalize_changelog_headings(fm.get('_body', '')), note_id))
                body.append('')
            body.append(pagination_markup(f'/changelog/product-group/{slug}/', pi, pages))
            if pi == 1:
                d = cpgbase / slug
                d.mkdir(parents=True, exist_ok=True)
                (d / 'index.md').write_text(rewrite_assets('\n'.join(body)) + '\n')
                add_tracked(tracked, f'changelog/product-group/{slug}/', f'{grp} changelog',
                            'templates/docs-md.html')
            else:
                d = cpgbase / slug / str(pi)
                d.mkdir(parents=True, exist_ok=True)
                (d / 'index.md').write_text(rewrite_assets('\n'.join(body)) + '\n')
                add_tracked(tracked, f'changelog/product-group/{slug}/{pi}/',
                            f'{grp} changelog - page {pi}', 'templates/docs-md.html')
    families['changelog-groups'] = {'groups': len(group_to_products)}

    # ---- Learning paths: /learning-paths/<slug>/... ----
    lp_files = sorted((up / 'src/content/learning-paths').glob('*.json'))
    lp_added = 0
    lp_overlaps = 0
    for lf in lp_files:
        lp = json.loads(lf.read_text())
        path = lp.get('path', '')
        title = lp.get('title', lf.stem)
        # path like /learning-paths/mtls/concepts/
        parts = [p for p in path.strip('/').split('/') if p]
        if parts:
            name = '/'.join(parts) + '/'
            if name in base_names:
                lp_overlaps += 1
                continue
            d = content.joinpath(*parts)
            d.mkdir(parents=True, exist_ok=True)
            body = [f'# {title}', '']
            body.append(lp.get('description', ''))
            body.append('')
            (d / 'index.md').write_text(rewrite_assets('\n'.join(body)) + '\n')
            add_tracked(tracked, name, title, 'templates/docs-md.html')
            lp_added += 1
    families['learning-paths'] = {
        'source_files': len(lp_files),
        'routes': lp_added,
        'ordinary_route_overlaps': lp_overlaps,
    }

    # ---- llms.txt: /llms.txt (root product index) ----
    llms = ['# Cloudflare Developer Documentation', '',
            'Explore guides and tutorials to start building on Cloudflare\'s platform.', '',
            '> Each product below links to its own llms.txt, which contains a full index of that product\'s documentation pages and is the recommended way to explore a specific product\'s content.', '']
    groups_llm = {}
    directory_llm = []
    for df in sorted((up / 'src/content/directory').glob('*.yaml')):
        dd = load_yaml(df)
        entry = dd.get('entry') or {}
        url = entry.get('url', '')
        title = entry.get('title') or dd.get('name', '')
        grp = entry.get('group') or 'Other'
        if url and url != '/' and '#' not in url:
            item = (title, url, dd.get('meta', {}).get('description', ''))
            groups_llm.setdefault(grp, []).append(item)
            directory_llm.append((grp, *item))
    all_url_prefixes = {item[2] for item in directory_llm}
    frozen_doc_files = tracked_files(up, 'src/content/docs', {'.md', '.mdx'})
    source_doc_ids = {
        p.relative_to(up / 'src/content/docs').as_posix().rsplit('.', 1)[0].removesuffix('/index')
        for p in frozen_doc_files
    }
    disallowed = []
    wildcard = False
    for raw_line in (up / 'public/robots.txt').read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith('#'):
            continue
        if line.lower().startswith('user-agent:'):
            wildcard = line.split(':', 1)[1].strip() == '*'
        elif wildcard and line.lower().startswith('disallow:'):
            path = line.split(':', 1)[1].split('#', 1)[0].strip()
            if path:
                disallowed.append(path)
    root_groups = {}
    for grp, title, url, description in directory_llm:
        prefix = url.strip('/')
        is_subproduct = any(other != url and url.startswith(other)
                            for other in all_url_prefixes)
        has_docs = any(doc == prefix or doc.startswith(prefix + '/')
                       for doc in source_doc_ids)
        if (not is_subproduct and has_docs and
                not any(url.startswith(path) for path in disallowed)):
            root_groups.setdefault(grp, []).append((title, url, description))
    for grp, items in sorted(root_groups.items()):
        if grp == 'Other':
            continue
        llms.append(f'## {grp}')
        llms.append('')
        for title, url, desc in sorted(items, key=lambda item: item[0].casefold()):
            line = f'- [{title}]({url}llms.txt)'
            if desc:
                line += f': {desc}'
            llms.append(line)
        llms.append('')
    if 'Other' in root_groups:
        llms.append('## Other')
        llms.append('')
        for title, url, desc in sorted(root_groups['Other'], key=lambda item: item[0].casefold()):
            line = f'- [{title}]({url}llms.txt)'
            if desc:
                line += f': {desc}'
            llms.append(line)
        llms.append('')
    shutil.rmtree(content / 'llms.txt', ignore_errors=True)
    root_llms = ROOT / 'public/llms.txt'
    if root_llms.is_dir():
        shutil.rmtree(root_llms)
    root_llms.write_text('\n'.join(llms) + '\n')
    static_files.add('/llms.txt')
    text_routes.add('/llms.txt')
    # Per-product /<product>/llms.txt routes: list every docs page under each
    # product root so the links emitted by the root llms.txt resolve.
    doc_index = {}
    doc_bodies = {}
    for p in frozen_doc_files:
        rel = p.relative_to(up / 'src/content/docs')
        raw = p.read_text(errors='replace')
        fm = {}
        mm = re.match(r'^---\n(.*?)\n---\n?', raw, re.S)
        body = raw
        if mm:
            try:
                fm = yaml.safe_load(mm.group(1).expandtabs(2)) or {}
            except yaml.YAMLError:
                fm = {}
                for line in mm.group(1).expandtabs(2).splitlines():
                    if ':' in line and not line.startswith(' '):
                        fm[line.split(':', 1)[0].strip()] = line.split(':', 1)[1].strip().strip('"\'')
            body = raw[mm.end():].strip()
        route = '/' + rel.as_posix().lower().rsplit('.', 1)[0].rstrip('/') + '/'
        route_parts = route.strip('/').split('/')
        route_parts[-1] = route_parts[-1].replace(' ', '-').replace('.', '')
        route = '/' + '/'.join(route_parts) + '/'
        if route.endswith('/index/'):
            route = route[:-7] + '/' if len(route) > 8 else '/'
        if fm.get('slug'):
            route = '/' + str(fm['slug']).strip('/').lower() + '/'
        external_link = fm.get('external_link', '')
        if external_link and not external_link.startswith('/'):
            continue
        if any(route.startswith(path) for path in disallowed):
            continue
        navigation_prose = re.sub(r'^import\s+.*?from\s+[\'"].*?[\'"];?\s*\n?', '', body, flags=re.M)
        navigation_prose = re.sub(r'<[A-Z][^>]*\s*/>', '', navigation_prose)
        navigation_prose = re.sub(r'<[A-Z][^>]*>[\s\S]*?</[A-Z][^>]*>', '', navigation_prose)
        navigation_prose = re.sub(r'\{/\*[\s\S]*?\*/\}', '', navigation_prose)
        navigation_only = 'DirectoryListing' in body and len(navigation_prose.strip()) <= 250
        title = fm.get('title') or rel.stem.replace('-', ' ').title()
        desc = fm.get('description') or fm.get('summary') or ''
        prod = route.strip('/').split('/')[0] if route != '/' else ''
        if not navigation_only:
            doc_index.setdefault(prod, []).append((route, title, desc, external_link))
        doc_bodies[route] = (title, body)
    valid_indexes = []
    for _group, index_title, index_url, index_desc in directory_llm:
        prefix = index_url.strip('/')
        if any(route == index_url or route.startswith(index_url)
               for entries in doc_index.values() for route, *_rest in entries):
            valid_indexes.append((index_title, index_url, index_desc))
    llm_routes = 1
    for title, url, desc in groups_llm.get('Other', []) + [
        (t, u, d) for items in [v for k, v in sorted(groups_llm.items()) if k != 'Other'] for t, u, d in items]:
        section = url.strip('/')
        if not section:
            continue
        if any(url.startswith(path) for path in disallowed):
            continue
        prefix = f'/{section}/'
        pages = [x for x in doc_index.get(section.split('/')[0], []) if x[0] == prefix or x[0].startswith(prefix)]
        delegated = []
        if url.startswith('/cloudflare-one/'):
            descendants = [index for index in valid_indexes if index[1] != url and index[1].startswith(url)]
            delegated = [candidate for candidate in descendants
                         if not any(other[1] != candidate[1] and candidate[1].startswith(other[1])
                                    for other in descendants)]
            pages = [page for page in pages
                     if not any(page[0].startswith(index_url) for _title, index_url, _desc in delegated)]
        if not pages:
            continue
        lines = [f'# {title}', '']
        if desc:
            lines.extend([desc, ''])
        lines.extend([
            '> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page\'s URL without the `index.md` suffix.',
            '>',
            '> For other Cloudflare products, see the [Cloudflare documentation directory](/llms.txt).',
            '',
            f'## {title} documentation pages',
            '',
        ])
        for delegated_title, delegated_url, delegated_desc in sorted(delegated, key=lambda item: item[1]):
            line = f'- [{delegated_title} documentation]({delegated_url}llms.txt)'
            if delegated_desc:
                line += f': {delegated_desc}'
            lines.append(line)
        for route, pt, pdesc, external_link in pages:
            destination = external_link if external_link and external_link.startswith('/') else route
            path, separator, fragment = destination.partition('#')
            line = f'- [{pt}]({path.rstrip("/")}/index.md{separator + fragment if separator else ""})'
            if pdesc:
                line += f': {pdesc}'
            lines.append(line)
        shutil.rmtree(content / section / 'llms.txt', ignore_errors=True)
        output = ROOT / 'public' / section / 'llms.txt'
        if output.is_dir():
            shutil.rmtree(output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text('\n'.join(lines) + '\n')
        static_files.add(f'/{section}/llms.txt')
        text_routes.add(f'/{section}/llms.txt')
        llm_routes += 1
    families['llms'] = {'routes': llm_routes}

    # ---- llms-full.txt: /llms-full.txt and /<product>/llms-full.txt ----
    # Concatenated documentation for offline indexing, mirroring the upstream
    # llms-full.txt routes referenced by /docs-for-agents/.
    def llms_full_doc(route):
        title, body = doc_bodies.get(route, (route, ''))
        return f'# {title}\n\nSource: https://developers.cloudflare.com{route}\n\n{body}\n\n'
    full_parts = [llms_full_doc(r) for r in sorted(doc_bodies)]
    full_dst = ROOT / 'public/llms-full.txt'
    full_dst.parent.mkdir(parents=True, exist_ok=True)
    full_dst.write_text('\n'.join(full_parts) + '\n')
    static_files.add('/llms-full.txt')
    llm_full_routes = 1
    for prod, pages in sorted(doc_index.items()):
        if not prod:
            continue
        prod_parts = [llms_full_doc(r) for r, _t, _d, _external in pages if r in doc_bodies]
        if not prod_parts:
            continue
        pd = ROOT / 'public' / prod
        pd.mkdir(parents=True, exist_ok=True)
        (pd / 'llms-full.txt').write_text('\n'.join(prod_parts) + '\n')
        static_files.add(f'/{prod}/llms-full.txt')
        llm_full_routes += 1
    families['llms-full'] = {'routes': llm_full_routes}

    # ---- Videos: /videos/<url>/ from src/content/stream/*.yaml ----
    vbase = content / 'videos'
    for vf, v in videos:
        vurl = v.get('url') or vf.stem
        title = v.get('title') or vf.stem
        vdir = vbase / vurl
        vdir.mkdir(parents=True, exist_ok=True)
        transcript = str(v.get('transcript') or '')
        transcript = re.sub(r'^WEBVTT\s*', '', transcript.strip())
        transcript = re.sub(r'(?m)^\d+\s*$', '', transcript)
        transcript = re.sub(r'(?m)^.+ --> .+$', '', transcript)
        transcript = re.sub(r'<[^>]+>', '', transcript)
        paragraphs = [re.sub(r'\s+', ' ', part).strip() for part in re.split(r'\n\s*\n', transcript)]
        paragraphs = [part for part in paragraphs if part]
        transcript_body = ''.join(f'<p>{html_escape(part)}</p>' for part in paragraphs)
        vbody = [
            '<div class="video-landing">',
            f'<header><h1>{html_escape(title)}</h1></header>',
            '<section class="video-content" aria-label="Video">',
            f'<p>{html_escape(str(v.get("description") or ""))}</p>',
        ]
        vbody.extend([
            f'<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/{html.escape(str(v.get("id") or ""), quote=True)}/iframe?preload=true&amp;letterboxColor=transparent" title="{html.escape(title, quote=True)}" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>',
            f'<details class="nb-details"><summary>Transcript</summary><div class="nb-details-body video-transcript">{transcript_body}</div></details>',
        ])
        chapters = v.get('chapters') or {}
        if isinstance(chapters, dict) and chapters:
            vbody.append('<section class="video-chapters"><h2>Chapters</h2>')
            for chapter_title, timestamp in chapters.items():
                thumbnail_url = (f'https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/'
                                 f'{v.get("id", "")}/thumbnails/thumbnail.jpg?time={timestamp}')
                vbody.append(
                    f'<a href="#" data-video-time="{html.escape(str(timestamp), quote=True)}">'
                    f'<img src="{html.escape(thumbnail_url, quote=True)}" alt="{html.escape(str(chapter_title), quote=True)}">'
                    f'<strong>{html_escape(str(chapter_title))}</strong></a>')
            vbody.append('</section>')
        vbody.append('</section></div>')
        (vdir / 'index.md').write_text(rewrite_assets('\n'.join(vbody)) + '\n')
        add_tracked(tracked, f'videos/{vurl}/', title, 'templates/video-md.html')
    families['videos'] = {'source_files': len(video_files), 'routes': len(video_files)}

    # ---- Agent setup generated routes: /agent-setup/ ----
    as_files = sorted((up / 'src/content/agent-setup').rglob('*.md'))
    asbase = content / 'agent-setup'
    asbase.mkdir(parents=True, exist_ok=True)
    as_pages = 0
    if as_files:
        agents = load_agents(up / 'src/components/agent-setup/agents.ts')
        (asbase / 'index.md').write_text(agent_setup_landing(agents))
        add_tracked(tracked, 'agent-setup/', 'Agent setup', 'templates/splash-md.html')
        as_pages += 1
        agent_public = ROOT / 'public/agent-setup'
        agent_public.mkdir(parents=True, exist_ok=True)
        for source in as_files:
            target = agent_public / source.name
            target.write_text(source.read_text())
            route_path = f'/agent-setup/{source.name}'
            static_files.add(route_path)
            text_routes.add(route_path)
        prompt_source = up / 'src/content/partials/prompts/base-prompt.txt'
        if prompt_source.is_file():
            prompt_target = ROOT / 'public/workers/prompt.txt'
            prompt_target.parent.mkdir(parents=True, exist_ok=True)
            prompt_target.write_text(prompt_source.read_text())
            static_files.add('/workers/prompt.txt')
            text_routes.add('/workers/prompt.txt')
    families['agent-setup'] = {'source_files': len(as_files), 'routes': as_pages}

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
        static_files.add('/workers/platform/compatibility-flags.json')
    families['compatibility-flags'] = {'source_files': len(cf_files), 'routes': 1}

    # ---- Pages build configuration: /pages/platform/build-configuration.json ----
    pfp = (up / 'src/content/pages-framework-presets/index.yaml')
    if pfp.exists():
        pfp_data = load_yaml(pfp)
        build_configs = pfp_data.get('build_configs', {})
        bc_dst = ROOT / 'public/pages/platform'
        bc_dst.mkdir(parents=True, exist_ok=True)
        (bc_dst / 'build-configuration.json').write_text(
            json.dumps(dict(sorted(build_configs.items())), indent=2) + '\n')
        static_files.add('/pages/platform/build-configuration.json')
        families['pages-build-configuration'] = {'source_files': 1}

    # ---- Pages language support: /pages/platform/language-support-and-tools.json ----
    pbe_files = sorted((up / 'src/content/pages-build-environment').glob('*.yaml'))
    pbe_data = []
    for pbe in pbe_files:
        d = load_yaml(pbe)
        entry = dict(d)
        if entry.get('enable_date'):
            try:
                entry['enable_date'] = str(entry['enable_date'])
            except Exception:
                pass
        entry.setdefault('status', None)
        pbe_data.append(entry)
    if pbe_data:
        ls_dst = ROOT / 'public/pages/platform'
        ls_dst.mkdir(parents=True, exist_ok=True)
        (ls_dst / 'language-support-and-tools.json').write_text(
            json.dumps(pbe_data, indent=2) + '\n')
        static_files.add('/pages/platform/language-support-and-tools.json')
        families['pages-language-support'] = {'source_files': len(pbe_files)}

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
    static_files.add('/changelog/rss/index.xml')
    # Per-product feeds: /changelog/rss/<product-id>.xml (skip area slugs that
    # collide with product IDs, mirroring the upstream [product].xml.ts).
    product_ids = {p for _, _, fm in posts
                   for p in (fm.get('products', '') or '').split(',') if p}
    product_ids.update(path.stem for path in (up / 'src/content/directory').glob('*.yaml'))
    areas = {}
    for df in (up / 'src/content/directory').glob('*.yaml'):
        entry = (load_yaml(df).get('entry') or {})
        if entry.get('group'):
            slug = entry['group'].replace(' ', '-').lower()
            areas.setdefault(slug, {'title': entry['group'], 'products': set()})[
                'products'].add(df.stem)
    area_slugs = set(areas)
    rss_feeds = 1
    for pid in product_ids:
        if pid in area_slugs:
            continue
        notes = [(p, n, fm) for p, n, fm in posts
                 if pid in (fm.get('products', '') or '').split(',')]
        notes.sort(key=lambda x: x[2].get('date', ''), reverse=True)
        fx = ['<?xml version="1.0" encoding="UTF-8"?>', '<rss version="2.0"><channel>',
              f'<title>Cloudflare {pid} changelog</title>',
              f'<description>Changelog updates for {pid}</description>',
              f'<link>https://developers.cloudflare.com/changelog/{pid}/</link>']
        for p, note_id, fm in notes:
            title = fm.get('title', note_id)
            date = fm.get('date', '')
            link = f'https://developers.cloudflare.com/changelog/post/{note_id}/'
            fx.append('<item>')
            fx.append(f'<title>{html_escape(title)}</title>')
            fx.append(f'<link>{link}</link>')
            fx.append(f'<guid>{link}</guid>')
            if date:
                fx.append(f'<pubDate>{date}</pubDate>')
            fx.append('</item>')
        fx.append('</channel></rss>')
        (rssbase / f'{pid}.xml').write_text('\n'.join(fx) + '\n')
        static_files.add(f'/changelog/rss/{pid}.xml')
        rss_feeds += 1
    for slug, area in sorted(areas.items()):
        notes = [(p, n, fm) for p, n, fm in posts
                 if area['products'].intersection(
                     (fm.get('products', '') or '').split(','))]
        notes.sort(key=lambda x: x[2].get('date', ''), reverse=True)
        fx = ['<?xml version="1.0" encoding="UTF-8"?>', '<rss version="2.0"><channel>',
              f'<title>Cloudflare changelogs | {html_escape(area["title"])}</title>',
              f'<description>Cloudflare changelogs for {html_escape(area["title"])} products</description>',
              '<link>https://developers.cloudflare.com/changelog/</link>']
        for _product, note_id, fm in notes:
            title = fm.get('title', note_id)
            date = fm.get('date', '')
            link = f'https://developers.cloudflare.com/changelog/post/{note_id}/'
            fx.extend(['<item>', f'<title>{html_escape(title)}</title>',
                       f'<link>{link}</link>', f'<guid>{link}</guid>'])
            if date:
                fx.append(f'<pubDate>{date}</pubDate>')
            fx.append('</item>')
        fx.append('</channel></rss>')
        (rssbase / f'{slug}.xml').write_text('\n'.join(fx) + '\n')
        static_files.add(f'/changelog/rss/{slug}.xml')
        rss_feeds += 1
    deprecations = load_yaml(up / 'src/content/release-notes/api-deprecations.yaml')
    deprecations_xml = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0"><channel>',
        '<title>Cloudflare API deprecations</title>',
        '<description>Cloudflare API deprecation notices</description>',
        '<link>https://developers.cloudflare.com/fundamentals/api/reference/deprecations/</link>',
    ]
    for entry in deprecations.get('entries', []):
        deprecations_xml.extend([
            '<item>',
            f'<title>{html_escape(str(entry.get("title") or "API deprecation"))}</title>',
            f'<description>{html_escape(str(entry.get("description") or ""))}</description>',
            '</item>',
        ])
    deprecations_xml.append('</channel></rss>')
    deprecations_path = ROOT / 'public/fundamentals/api/reference/deprecations/index.xml'
    deprecations_path.parent.mkdir(parents=True, exist_ok=True)
    deprecations_path.write_text('\n'.join(deprecations_xml) + '\n')
    static_files.add('/fundamentals/api/reference/deprecations/index.xml')
    families['rss'] = {'routes': rss_feeds}

    # Nift's CommonMark renderer does not synthesize heading IDs. Materialize
    # generated-family headings so TOCs and fragment links work without JS.
    for entry in tracked:
        if entry['template'] != 'templates/docs-md.html' or not entry['name'].endswith('/'):
            continue
        page = content / entry['name'].strip('/') / 'index.md'
        if not page.is_file():
            continue
        normalized = mdx_importer.normalize_markdown_heading_lines(page.read_text())
        page.write_text(mdx_importer.add_heading_ids(normalized))

    # Deduplicate tracked names (e.g. WARP releases also appear as real
    # changelog posts in src/content/changelog).
    seen = set()
    deduped = []
    for x in tracked:
        if x['name'] not in seen:
            seen.add(x['name'])
            deduped.append(x)
    tracked = deduped
    nav_dir = ROOT / 'public/assets/navigation'
    nav_dir.mkdir(parents=True, exist_ok=True)
    generated_routes = [entry['output'] for entry in tracked if entry['output'].endswith('/')]
    generated_roots = sorted({route.strip('/').split('/')[0] for route in generated_routes if route != '/'})
    for product_id in generated_roots:
        destination = nav_dir / f'{product_id}.json'
        if destination.exists():
            continue
        routes = {
            route: {
                'activeAncestorIds': [], 'activeNodeId': None, 'next': None,
                'previous': None, 'productId': product_id,
            }
            for route in generated_routes if route.startswith(f'/{product_id}/')
        }
        payload = {
            'schemaVersion': 1,
            'source': {'upstreamSha': PIN},
            'product': {
                'id': product_id,
                'label': product_id.replace('-', ' ').title(),
                'children': [],
            },
            'routes': routes,
        }
        destination.write_text(json.dumps(payload, separators=(',', ':')) + '\n')
        static_files.add(f'/assets/navigation/{product_id}.json')
    generated_only = [entry for entry in tracked if entry['name'] not in base_names]
    generated_manifest = {
        'upstream_sha': git_sha(up),
        'routes': sorted(x['output'] for x in generated_only),
        'static_files': sorted(static_files),
        'text_routes': sorted(text_routes),
    }
    ordinary_routes = set(ordinary_manifest['routes']) | {'/'}
    stale_routes = previous_generated_routes - set(generated_manifest['routes']) - ordinary_routes
    for route in stale_routes:
        shutil.rmtree(ROOT / 'content' / route.strip('/'), ignore_errors=True)
        shutil.rmtree(ROOT / 'public' / route.strip('/'), ignore_errors=True)
    stale_text_routes = previous_text_routes - text_routes
    for route in stale_text_routes:
        stale = ROOT / 'public' / route.strip('/')
        if stale.is_dir():
            shutil.rmtree(stale)
        elif stale.exists():
            stale.unlink()
    families['stale-generated-routes-removed'] = len(stale_routes)
    families['stale-text-routes-removed'] = len(stale_text_routes)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(generated_manifest, indent=2) + '\n')
    print(json.dumps({'upstream_sha': git_sha(up), 'families': families,
                      'total_tracked': len(generated_only),
                      'static_files': len(static_files)}, indent=2))
    # Replace generated entries on every run while preserving home and ordinary
    # docs. Otherwise a changed generated template can be masked by stale state.
    tpath = tracked_path
    if tpath.exists():
        existing = json.loads(tpath.read_text()).get('tracked', [])
        generated_names = {x['name'] for x in generated_only}
        retained = [x for x in existing if x['name'] in base_names]
        retained_names = {x['name'] for x in retained}
        new_entries = [x for x in generated_only if x['name'] not in retained_names]
        merged = retained + new_entries
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
