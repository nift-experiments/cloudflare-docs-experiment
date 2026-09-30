#!/usr/bin/env python3
"""Deterministic Cloudflare page-head metadata for imported Nift pages."""
from __future__ import annotations

import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin

import yaml


ORIGIN = 'https://developers.cloudflare.com'
SITE_TITLE = 'Cloudflare Docs'
DEFAULT_DESCRIPTION = "Cloudflare's documentation."
DEFAULT_IMAGE = '/og-docs.png'
CHANGELOG_IMAGE = '/og-changelog.png'
NOINDEX_SECTIONS = {'email-security'}


class _FirstParagraph(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.parts = []
        self.done = False

    def handle_starttag(self, tag, _attrs):
        if self.done:
            return
        if tag == 'p' and not self.depth:
            self.depth = 1
        elif self.depth:
            self.depth += 1

    def handle_endtag(self, tag):
        if not self.depth:
            return
        self.depth -= 1
        if tag == 'p' and not self.depth:
            self.done = True

    def handle_data(self, data):
        if self.depth:
            self.parts.append(data)


def directory_metadata(upstream: Path):
    sections = {}
    products = {}
    for path in sorted((upstream / 'src/content/directory').glob('*.yaml')):
        data = yaml.safe_load(path.read_text()) or {}
        entry = data.get('entry') or {}
        meta = data.get('meta') or {}
        product = str(entry.get('title') or data.get('name') or path.stem)
        products[path.stem] = product
        sections[path.stem] = {
            'product': product,
            'group': str(entry.get('group') or ''),
            'title_suffix': str(meta.get('title') or SITE_TITLE),
        }
    return sections, products


def _plain_description(value):
    value = str(value or '')
    value = re.sub(r'!\[([^]]*)\]\([^)]*\)', r'\1', value)
    value = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', value)
    value = re.sub(r'[*_~`]+', '', value)
    return re.sub(r'\s+', ' ', html.unescape(value)).strip()


def derive_description(body):
    parser = _FirstParagraph()
    parser.feed(body)
    description = re.sub(r'\s+', ' ', ''.join(parser.parts)).strip()
    if description:
        return description
    if re.search(r'<[A-Za-z][^>]*>', body):
        return None
    text = re.sub(r'^\s*(?:#{1,6}\s+.*|<[^>]+>)\s*$', '', body, flags=re.M)
    for paragraph in re.split(r'\n\s*\n', text):
        plain = _plain_description(paragraph)
        if plain:
            return plain
    return None


def extract_embedded_head(body, metadata):
    """Lift legacy body-level title overrides into the generated document head."""
    matches = list(re.finditer(r'<head\b[^>]*>(.*?)</head>', body, re.I | re.S))
    if not matches:
        return body, metadata
    metadata = dict(metadata or {})
    head = list(metadata.get('head') or [])
    if not any(isinstance(item, dict) and item.get('tag') == 'title' for item in head):
        for match in matches:
            title = re.search(r'<title\b[^>]*>(.*?)</title>', match.group(1), re.I | re.S)
            if title:
                head.append({'tag': 'title',
                             'content': re.sub(r'\s+', ' ', html.unescape(title.group(1))).strip()})
                break
    metadata['head'] = head
    for match in reversed(matches):
        body = body[:match.start()] + body[match.end():]
    return body, metadata


def _head_title_override(metadata):
    for item in metadata.get('head') or []:
        if isinstance(item, dict) and item.get('tag') == 'title' and item.get('content'):
            return str(item['content'])
    return None


def _format_content_type(raw):
    return raw[:1].upper() + raw[1:].replace('-', ' ') if raw else ''


def _canonical(route, override=None):
    target = str(override or route)
    return urljoin(ORIGIN + '/', target).replace('@', '%40')


def _structured_data(schema_type, canonical, title, description, image,
                     content_type, metadata):
    data = {
        '@context': 'https://schema.org',
        '@type': schema_type,
        '@id': canonical + '#page',
        'headline': title,
    }
    if description:
        data['description'] = _plain_description(description)
    data.update({
        'url': canonical,
        'inLanguage': 'en',
        'image': image,
    })
    if content_type in {'changelog', 'changelog-entry'} and metadata.get('date'):
        data['datePublished'] = str(metadata['date'])[:10]
    data['publisher'] = {
        '@type': 'Organization',
        'name': 'Cloudflare',
        'description': ('One platform for your apps, agents, and workforce. '
                        'Build, secure, and scale without managing infrastructure'),
        'url': 'https://www.cloudflare.com/',
        'sameAs': [
            'https://github.com/cloudflare',
            'https://www.linkedin.com/company/cloudflare',
            'https://x.com/cloudflare',
        ],
        'logo': {'@type': 'ImageObject', 'url': ORIGIN + '/logo.svg'},
        'address': {
            '@type': 'PostalAddress',
            'streetAddress': '101 Townsend St',
            'addressLocality': 'San Francisco',
            'addressRegion': 'CA',
            'postalCode': '94107',
            'addressCountry': 'US',
        },
        'contactPoint': [
            {'@type': 'ContactPoint', 'contactType': 'Customer Support',
             'url': 'https://support.cloudflare.com/', 'availableLanguage': ['English']},
            {'@type': 'ContactPoint', 'contactType': 'Sales',
             'url': 'https://www.cloudflare.com/contact/', 'availableLanguage': ['English']},
        ],
    }
    data['isPartOf'] = {
        '@type': 'WebSite', '@id': ORIGIN + '/#website',
        'name': SITE_TITLE, 'url': ORIGIN + '/',
    }
    tags = metadata.get('tags') or []
    if tags:
        data['keywords'] = [str(tag) for tag in tags]
    return json.dumps(data, ensure_ascii=True, separators=(',', ':')).replace('<', '\\u003c')


def build_head(route, title, metadata=None, body='', sections=None, products=None,
               markdown=False):
    metadata = metadata or {}
    sections = sections or {}
    products = products or {}
    section = route.strip('/').split('/', 1)[0] if route != '/' else ''
    section_meta = sections.get(section)
    title_override = _head_title_override(metadata)
    title_suffix = (str(metadata.get('title_suffix')) if metadata.get('title_suffix')
                    else section_meta.get('title_suffix') if section_meta else None)
    base_title = title_override.split(' | ')[0] if title_override else title
    full_title = (f'{base_title} · {title_suffix}' if title_suffix
                  else title_override or f'{title} | {SITE_TITLE}')
    description = metadata.get('description') or derive_description(body)
    if description:
        description = re.sub(r'\s+', ' ', str(description)).strip()
    external_link = metadata.get('external_link')
    noindex = bool(metadata.get('noindex') or external_link or section in NOINDEX_SECTIONS)
    canonical = _canonical(route, metadata.get('canonical'))
    page_url = urljoin(ORIGIN + '/', route)
    raw_content_type = str(metadata.get('pcx_content_type') or '')
    if not raw_content_type and re.match(r'^/(?:ai|workers-ai)/models/.+', route):
        raw_content_type = 'reference'
    if not raw_content_type and route.startswith('/changelog/post/'):
        raw_content_type = 'changelog-entry'
    content_type = _format_content_type(raw_content_type)
    is_changelog = raw_content_type in {'changelog', 'changelog-entry'}
    schema_type = ('WebPage' if route == '/' or raw_content_type in {
        'navigation', 'overview', 'reference-architecture-diagram'} else
        'BlogPosting' if is_changelog else 'TechArticle')
    image_path = str(metadata.get('socialImage') or
                     (CHANGELOG_IMAGE if is_changelog else DEFAULT_IMAGE))
    image = urljoin(ORIGIN + '/', image_path)
    product = section_meta.get('product') if section_meta else None
    product_group = section_meta.get('group') if section_meta else None
    product_names = [products[item] for item in metadata.get('products') or []
                     if item in products]

    esc = lambda value: html.escape(str(value), quote=True)
    lines = [
        f'<title>{esc(full_title)}</title>',
        '<meta name="generator" content="Nift">',
    ]
    if description:
        lines.append(f'<meta name="description" content="{esc(description)}">')
    if noindex:
        lines.append('<meta name="robots" content="noindex">')
    lines.extend([
        f'<link rel="canonical" href="{esc(canonical)}">',
        '<link rel="sitemap" href="/sitemap-index.xml">',
    ])
    if markdown:
        markdown_href = urljoin(ORIGIN + '/', route.lstrip('/') + 'index.md')
        lines.append(f'<link rel="alternate" type="text/markdown" href="{esc(markdown_href)}">')
    if raw_content_type == 'changelog':
        rss_href = urljoin(ORIGIN + '/', route.lstrip('/') + 'index.xml')
        lines.append(f'<link rel="alternate" type="application/rss+xml" href="{esc(rss_href)}">')
    lines.append(f'<meta property="og:title" content="{esc(full_title if title_suffix else title)}">')
    lines.extend([
        '<meta property="og:type" content="article">',
        f'<meta property="og:site_name" content="{SITE_TITLE}">',
        '<meta property="og:locale" content="en">',
    ])
    if description:
        lines.append(f'<meta property="og:description" content="{esc(description)}">')
    lines.extend([
        f'<meta property="og:url" content="{esc(page_url)}">',
        f'<meta property="image" content="{esc(image)}">',
        f'<meta property="og:image" content="{esc(image)}">',
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:site" content="@cloudflare">',
        f'<meta property="twitter:image" content="{esc(image)}">',
    ])
    if product:
        lines.extend([
            f'<meta name="pcx_product" content="{esc(product)}">',
            f'<meta name="algolia_product_filter" content="{esc(product)}">',
        ])
    if product_group:
        lines.append(f'<meta name="pcx_content_group" content="{esc(product_group)}">')
    if content_type:
        lines.extend([
            f'<meta name="pcx_content_type" content="{esc(content_type)}">',
            f'<meta name="algolia_content_type" content="{esc(content_type)}">',
        ])
    if product_names:
        lines.append(f'<meta name="pcx_additional_products" content="{esc(",".join(product_names))}">')
    tags = metadata.get('tags') or []
    if tags:
        lines.append(f'<meta name="pcx_tags" content="{esc(",".join(map(str, tags)))}">')
    structured = _structured_data(schema_type, canonical, full_title, description,
                                  image, raw_content_type, metadata)
    if not noindex:
        lines.append(f'<script type="application/ld+json">{structured}</script>')
    if external_link:
        lines.append(f'<meta http-equiv="refresh" content="0; url={esc(external_link)}">')
    for item in metadata.get('head') or []:
        if not isinstance(item, dict) or item.get('tag') == 'title':
            continue
        tag = str(item.get('tag') or '').lower()
        if tag not in {'meta', 'link', 'script'}:
            continue
        attrs = ''.join(f' {esc(key)}="{esc(value)}"'
                        for key, value in (item.get('attrs') or {}).items())
        content = str(item.get('content') or '').replace('<', '\\u003c')
        lines.append(f'<{tag}{attrs}>{content}</{tag}>' if content else f'<{tag}{attrs}>')
    return {
        'schema': 1,
        'route': route,
        'full_title': full_title,
        'canonical': canonical,
        'description': str(description or ''),
        'noindex': noindex,
        'markdown': markdown,
        'head_html': ''.join(lines),
    }


def add_frontmatter(body, page_head):
    if not body.strip():
        body = ''
    if body.startswith('---\n'):
        match = re.match(r'^---\n(.*?)\n---\n?', body, re.S)
        if match:
            existing = yaml.safe_load(match.group(1)) or {}
            if isinstance(existing, dict):
                existing['cp9'] = page_head
                body = body[match.end():]
                return ('---\n' + yaml.safe_dump(existing, sort_keys=True,
                                                  allow_unicode=True, width=10**9) +
                        '---\n' + body)
    return ('---\n' + yaml.safe_dump({'cp9': page_head}, sort_keys=True,
                                      allow_unicode=True, width=10**9) + '---\n' + body)


def apply_to_content(path, route, title, metadata=None, sections=None,
                     products=None, markdown=False):
    body = path.read_text()
    page_head = build_head(route, title, metadata, body, sections, products, markdown)
    path.write_text(add_frontmatter(body, page_head))
    return page_head
