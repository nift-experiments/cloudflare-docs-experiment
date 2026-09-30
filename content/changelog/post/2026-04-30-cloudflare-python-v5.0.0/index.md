---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-python-v5.0.0/
  description: New updates and improvements at Cloudflare.
  full_title: Cloudflare Python SDK v5.0.0 Released · Changelog
  head_html: <title>Cloudflare Python SDK v5.0.0 Released · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-python-v5.0.0/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Cloudflare Python SDK v5.0.0 Released · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-python-v5.0.0/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-python-v5.0.0/#page","headline":"Cloudflare Python SDK v5.0.0 Released \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-python-v5.0.0/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-30-cloudflare-python-v5.0.0/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 30, 2026</time><h2 id="post-title">Cloudflare Python SDK v5.0.0 Released</h2>
<div class="changelog-badges"><span>sdk</span></div><div class="changelog-body"><p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-python/compare/v4.3.1...v5.0.0">v4.3.1...v5.0.0</a></p>
<p>This is a major release of the Cloudflare Python SDK. It drops support for Python 3.8, adds 11 new API services, introduces optional aiohttp backend support for improved async concurrency, and includes hundreds of type and method updates across the entire API surface.</p>
<p><strong>Please review the breaking changes below before upgrading.</strong> A migration guide is available at <a href="https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md">v5.0.0 Migration Guide</a>.</p>
<h4 id="breaking-changes">Breaking Changes</h4>
<ul>
<li><strong>Python 3.8 is no longer supported.</strong> The minimum required version is now Python 3.9.</li>
<li><strong><code>typing-extensions</code> minimum version bumped</strong> from <code>&gt;=4.10</code> to <code>&gt;=4.14</code>.</li>
</ul>
<p>The following resources have breaking changes. See the <a href="https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md">v5.0.0 Migration Guide</a> for detailed migration instructions.</p>
<ul>
<li><code>abusereports</code></li>
<li><code>acm.totaltls</code></li>
<li><code>apigateway.configurations</code></li>
<li><code>cloudforceone.threatevents</code></li>
<li><code>d1.database</code></li>
<li><code>intel.indicatorfeeds</code></li>
<li><code>logpush.edge</code></li>
<li><code>origintlsclientauth.hostnames</code></li>
<li><code>queues.consumers</code></li>
<li><code>radar.bgp</code></li>
<li><code>rulesets.rules</code></li>
<li><code>schemavalidation.schemas</code></li>
<li><code>snippets</code></li>
<li><code>zerotrust.dlp</code></li>
<li><code>zerotrust.networks</code></li>
</ul>
<h4 id="features">Features</h4>
<h4 id="aiohttp-backend-support">aiohttp Backend Support</h4>
<p>The async client now supports an optional <code>aiohttp</code> HTTP backend for improved concurrency performance. Install with <code>pip install cloudflare[aiohttp]</code> and use <code>DefaultAioHttpClient()</code> as the <code>http_client</code> parameter.</p>
<h4 id="python-3-13-and-3-14-support">Python 3.13 and 3.14 Support</h4>
<p>Python 3.13 and 3.14 are now tested and supported.</p>
<h4 id="new-services">New Services</h4>
<p>The following top-level resources are new in this release:</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Client Path</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>AI Search</td>
<td><code>aisearch</code></td>
<td>AI-powered search capabilities</td>
</tr>
<tr>
<td>Connectivity</td>
<td><code>connectivity</code></td>
<td>Connectivity testing and diagnostics</td>
</tr>
<tr>
<td>Email Sending</td>
<td><code>email_sending</code></td>
<td>Email send and send_raw endpoints</td>
</tr>
<tr>
<td>Fraud</td>
<td><code>fraud</code></td>
<td>Fraud detection and prevention</td>
</tr>
<tr>
<td>Google Tag Gateway</td>
<td><code>google_tag_gateway</code></td>
<td>Google Tag Gateway management</td>
</tr>
<tr>
<td>Organizations</td>
<td><code>organizations</code></td>
<td>Organization audit logs and management</td>
</tr>
<tr>
<td>R2 Data Catalog</td>
<td><code>r2_data_catalog</code></td>
<td>R2 Data Catalog operations</td>
</tr>
<tr>
<td>Realtime Kit</td>
<td><code>realtime_kit</code></td>
<td>Realtime communication (Calls/TURN)</td>
</tr>
<tr>
<td>Resource Tagging</td>
<td><code>resource_tagging</code></td>
<td>Resource tagging and labeling</td>
</tr>
<tr>
<td>Token Validation</td>
<td><code>token_validation</code></td>
<td>Token validation configuration and rules</td>
</tr>
<tr>
<td>Vulnerability Scanner</td>
<td><code>vulnerability_scanner</code></td>
<td>Vulnerability scanning, credential sets, and target environments</td>
</tr>
</tbody>
</table>
<h4 id="new-endpoints-on-existing-services">New Endpoints on Existing Services</h4>
<ul>
<li><strong>api_gateway</strong>: Labels endpoints</li>
<li><strong>billing</strong>: Billable usage PayGo endpoint</li>
<li><strong>brand_protection</strong>: v2 endpoints</li>
<li><strong>browser_rendering</strong>: DevTools methods</li>
<li><strong>cache</strong>: Origin cloud regions resource</li>
<li><strong>custom_origin_trust_store</strong>: Custom origin trust store</li>
<li><strong>dns</strong>: <code>dns_records/usage</code> endpoints</li>
<li><strong>email_security</strong>: Phishguard reports endpoint</li>
<li><strong>iam</strong>: User groups and user group members resources</li>
<li><strong>radar</strong>: Botnet Threat Feed and Post-Quantum endpoints</li>
<li><strong>workers</strong>: Observability Destinations resources</li>
<li><strong>zero_trust</strong>: Access Users, DEX rules, Device IP Profile, Device Subnet, WARP Connector connections and failover, WARP Subnet, Gateway PAC files</li>
<li><strong>zones</strong>: Zone environments endpoints</li>
</ul>
<h4 id="bug-fixes">Bug Fixes</h4>
<ul>
<li>Fixed <code>polymorphic_serialization</code> parameter in <code>model_dump</code> overrides</li>
<li>Added <code>BaseModel</code> base to response <code>SchemaFieldStruct</code>/<code>SchemaFieldList</code> stubs in Pipelines</li>
<li>Added missing <code>model_rebuild</code>/<code>update_forward_refs</code> for <code>SharedEntryCustomEntry</code> classes in DLP</li>
<li>Made <code>RunQueryParametersNeedleValue</code> a <code>BaseModel</code> with <code>arbitrary_types_allowed</code> in Workers</li>
<li>Removed duplicate <code>notification_url</code> field in webhook response types for Stream</li>
<li>Resolved pre-existing codegen type errors</li>
<li>Fixed <code>type: ignore[call-arg]</code> placement for mypy compatibility in Radar</li>
</ul>
<h4 id="deprecations">Deprecations</h4>
<p>Resources with <code>@deprecated</code> annotations on some methods include: <code>accounts</code>, <code>addressing</code>, <code>ai-gateway</code>, <code>aisearch</code>, <code>api-gateway</code>, <code>billing</code>, <code>cloudforce-one</code>, <code>dns</code>, <code>email-routing</code>, <code>email-security</code>, <code>filters</code>, <code>firewall</code>, <code>images</code>, <code>intel</code>, <code>kv</code>, <code>logpush</code>, <code>origin-tls-client-auth</code>, <code>pages</code>, <code>pipelines</code>, <code>radar</code>, <code>rate-limits</code>, <code>registrar</code>, <code>rulesets</code>, <code>ssl</code>, <code>user</code>, <code>workers</code>, <code>workers-for-platforms</code>, <code>zero-trust</code>, <code>zones</code></p>
<h4 id="get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-python/releases/tag/v5.0.0">Download Python SDK v5.0.0</a></li>
<li><a href="https://developers.cloudflare.com/api/sdks/python/">Python SDK documentation</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md">Migration Guide</a></li>
</ul>
</div></article></div>
