#!/usr/bin/env python3
"""Generate deterministic CP7 navigation data from the frozen docs checkout."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import yaml


PIN = 'bc2bdaee16098ec1b0bb782b80cf3a73f9557ddf'
FRONT = re.compile(r'^---\n(.*?)\n---\n?', re.S)


def route_for(relative):
    value = relative.as_posix().rsplit('.', 1)[0]
    if value.endswith('/index'):
        value = value[:-6]
    return '/' if value == 'index' else f'/{value.strip("/")}/'


def humanize(value):
    return value.replace('-', ' ').replace('_', ' ').strip().title()


def frontmatter(path):
    raw = path.read_text(errors='replace')
    match = FRONT.match(raw)
    if not match:
        return {}, raw
    try:
        data = yaml.safe_load(match.group(1).expandtabs(2)) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f'{path}: invalid navigation frontmatter: {exc}') from exc
    return data if isinstance(data, dict) else {}, raw[match.end():]


def sidebar_data(meta):
    value = meta.get('sidebar', {})
    if value is False:
        return {'disabled': True}
    return value if isinstance(value, dict) else {}


def badge_value(value):
    if isinstance(value, str):
        text, variant = value, 'default'
    elif isinstance(value, dict):
        text = str(value.get('text', ''))
        variant = str(value.get('variant', 'default'))
    else:
        return None
    variants = {'beta': 'caution', 'new': 'note', 'deprecated': 'danger', 'legacy': 'danger'}
    return {'text': text, 'variant': variants.get(text.casefold(), variant)} if text else None


def page_record(path, docs_root):
    relative = path.relative_to(docs_root)
    meta, body = frontmatter(path)
    sidebar = sidebar_data(meta)
    route = route_for(relative)
    title = str(meta.get('title') or humanize(relative.stem))
    label = str(sidebar.get('label') or title)
    external = meta.get('external_link')
    href = str(external or route)
    external_target = href.startswith(('http://', 'https://')) or href.startswith('/api/')
    return {
        'source': relative.as_posix(),
        'parts': relative.with_suffix('').parts,
        'route': route,
        'href': href,
        'title': title,
        'label': label,
        'order': sidebar.get('order'),
        'hidden': sidebar.get('hidden') is True,
        'disabled': sidebar.get('disabled') is True,
        'hideChildren': meta.get('hideChildren') is True,
        'hideIndex': sidebar.get('hideIndex') is True or (
            (sidebar.get('group') or {}).get('hideIndex') is True
            if isinstance(sidebar.get('group'), dict) else False),
        'groupLabel': (sidebar.get('group') or {}).get('label')
            if isinstance(sidebar.get('group'), dict) else None,
        'groupBadge': badge_value((sidebar.get('group') or {}).get('badge'))
            if isinstance(sidebar.get('group'), dict) else None,
        'badge': badge_value(sidebar.get('badge')),
        'template': meta.get('template'),
        'external': external_target,
        'redirect': external is not None,
        'body': body,
    }


def sort_key(node):
    order = node.get('order')
    return (order is None, float(order or 0), node['label'].casefold(), node['id'])


def link_node(record):
    ident = 'page:' + record['source'].rsplit('.', 1)[0].replace('/', ':')
    label = record['label']
    if record['external'] or (record['redirect'] and record['href'] != record['route']):
        label += ' ↗'
    return {
        'kind': 'link', 'id': ident, 'label': label, 'href': record['href'],
        'route': record['route'], 'order': record['order'],
        'external': record['external'], 'neverActive': record['redirect'],
        'badge': record['badge'], 'searchText': label.casefold(),
    }


def directory_node(path_parts, records, is_root=False):
    index = next((record for record in records if record['parts'][-1] == 'index'), None)
    direct = [record for record in records if len(record['parts']) == len(path_parts) + 1
              and record['parts'][-1] != 'index']
    child_names = sorted({record['parts'][len(path_parts)] for record in records
                          if len(record['parts']) > len(path_parts) + 1})
    children = []
    if index and not index['hidden'] and not index['hideIndex']:
        overview = link_node(index)
        overview['label'] = index['label'] if is_root else 'Overview'
        overview['searchText'] = overview['label'].casefold()
        children.append(overview)
    for record in direct:
        if not record['hidden']:
            children.append(link_node(record))
    for child_name in child_names:
        child_parts = path_parts + (child_name,)
        child_records = [record for record in records
                         if record['parts'][:len(child_parts)] == child_parts]
        child_index = next((record for record in child_records
                            if len(record['parts']) == len(child_parts) + 1
                            and record['parts'][-1] == 'index'), None)
        if child_index and child_index['hideChildren']:
            if not child_index['hidden']:
                children.append(link_node(child_index))
            continue
        nested = directory_node(child_parts, child_records)
        if not nested['children']:
            continue
        label = (child_index or {}).get('groupLabel') or (child_index or {}).get('title') or humanize(child_name)
        children.append({
            'kind': 'group', 'id': 'group:' + ':'.join(child_parts),
            'label': label, 'order': (child_index or {}).get('order'),
            'badge': (child_index or {}).get('groupBadge'), 'children': nested['children'],
            'href': child_index['href'] if child_index and not child_index['external'] else None,
            'searchText': str(label).casefold(),
        })
    children.sort(key=sort_key)
    return {'children': children}


def flatten(nodes, ancestors=()):
    sequence = []
    index = {}
    for node in nodes:
        if node['kind'] == 'link':
            if not node['external'] and not node['neverActive']:
                sequence.append(node)
                index[node['route']] = (node, list(ancestors))
        else:
            child_sequence, child_index = flatten(node['children'], ancestors + (node['id'],))
            sequence.extend(child_sequence)
            index.update(child_index)
    return sequence, index


def product_labels(upstream, products):
    labels = {}
    directory = upstream / 'src/content/directory'
    for product in products:
        source = directory / f'{product}.yaml'
        if not source.exists():
            labels[product] = humanize(product)
            continue
        data = yaml.safe_load(source.read_text()) or {}
        entry = data.get('entry') or {}
        labels[product] = str(entry.get('title') or data.get('name') or humanize(product))
    return labels


def generate(upstream, destination, upstream_sha=PIN):
    docs_root = upstream / 'src/content/docs'
    paths = sorted(path for path in docs_root.rglob('*') if path.suffix in {'.md', '.mdx'})
    records = [page_record(path, docs_root) for path in paths]
    products = sorted({record['parts'][0] for record in records if record['parts']})
    labels = product_labels(upstream, products)
    output_products = {}
    route_context = {}

    for product in products:
        product_records = [record for record in records if record['parts'][0] == product]
        tree = directory_node((product,), product_records, is_root=True)['children']
        sequence, route_index = flatten(tree)
        tree_json = json.dumps(tree, sort_keys=True, separators=(',', ':'))
        output_products[product] = {
            'id': product, 'label': labels[product], 'root': f'/{product}/',
            'treeHash': hashlib.sha256(tree_json.encode()).hexdigest()[:16],
            'children': tree,
        }
        for position, node in enumerate(sequence):
            route = node['route']
            active, ancestors = route_index[route]
            previous = sequence[position - 1] if position else None
            following = sequence[position + 1] if position + 1 < len(sequence) else None
            route_context[route] = {
                'productId': product, 'activeNodeId': active['id'],
                'activeAncestorIds': ancestors,
                'previous': ({'href': previous['href'], 'label': previous['label']}
                             if previous else None),
                'next': ({'href': following['href'], 'label': following['label']}
                         if following else None),
            }
        for record in product_records:
            route_context.setdefault(record['route'], {
                'productId': product, 'activeNodeId': None,
                'activeAncestorIds': [], 'previous': None, 'next': None,
            })

    home_groups = {}
    directory = upstream / 'src/content/directory'
    for source in sorted(directory.glob('*.yaml')):
        data = yaml.safe_load(source.read_text()) or {}
        entry = data.get('entry') or {}
        url = entry.get('url')
        if not url or entry.get('hide') is True:
            continue
        group = str(entry.get('group') or 'Other')
        home_groups.setdefault(group, []).append({
            'label': str(entry.get('title') or data.get('name') or humanize(source.stem)),
            'href': str(url),
        })
    home = [{'label': label, 'links': sorted(links, key=lambda item: item['label'].casefold())}
            for label, links in sorted(home_groups.items())]
    document = {
        'schemaVersion': 1,
        'source': {'upstreamSha': upstream_sha},
        'products': output_products,
        'routes': route_context,
        'home': home,
    }
    destination.parent.mkdir(parents=True, exist_ok=True)
    product_dir = destination.parent / 'navigation'
    product_dir.mkdir(parents=True, exist_ok=True)
    for stale in product_dir.glob('*.json'):
        stale.unlink()
    for product, product_data in output_products.items():
        product_routes = {route: context for route, context in route_context.items()
                          if context['productId'] == product}
        payload = {
            'schemaVersion': 1,
            'source': {'upstreamSha': upstream_sha},
            'product': product_data,
            'routes': product_routes,
        }
        (product_dir / f'{product}.json').write_text(
            json.dumps(payload, sort_keys=True, separators=(',', ':')) + '\n')
    manifest = {
        'schemaVersion': 1,
        'source': {'upstreamSha': upstream_sha},
        'products': {product: {key: value for key, value in data.items()
                              if key != 'children'}
                     for product, data in output_products.items()},
        'home': home,
    }
    destination.write_text(json.dumps(manifest, sort_keys=True, separators=(',', ':')) + '\n')
    return document
