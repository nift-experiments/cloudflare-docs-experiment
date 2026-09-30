---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-typescript-v6.0.0/
  description: New updates and improvements at Cloudflare.
  full_title: Cloudflare TypeScript SDK v6.0.0 Released · Changelog
  head_html: <title>Cloudflare TypeScript SDK v6.0.0 Released · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-typescript-v6.0.0/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Cloudflare TypeScript SDK v6.0.0 Released · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-typescript-v6.0.0/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-typescript-v6.0.0/#page","headline":"Cloudflare TypeScript SDK v6.0.0 Released \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-30-cloudflare-typescript-v6.0.0/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-30-cloudflare-typescript-v6.0.0/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 30, 2026</time><h2 id="post-title">Cloudflare TypeScript SDK v6.0.0 Released</h2>
<div class="changelog-badges"><span>sdk</span></div><div class="changelog-body"><p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-typescript/compare/v6.0.0-beta.2...v6.0.0">v6.0.0-beta.2...v6.0.0</a></p>
<p>This is a major version release of the Cloudflare TypeScript SDK. It includes 11 entirely new top-level API resources, new sub-resources and methods across 50+ existing resources, SDK infrastructure improvements, and breaking changes to the generated API surface from the v5.x line.</p>
<p><strong>Please ensure you read through the list of changes below before moving to this version</strong> - this will help you understand any down or upstream issues it may cause to your environments.</p>
<h4 id="breaking-changes">Breaking Changes</h4>
<h4 id="sdk-infrastructure">SDK Infrastructure</h4>
<ul>
<li><strong>Retry-After handling changed</strong>: The SDK now respects any server-specified <code>Retry-After</code> value for rate-limited requests. Previously, values over 60 seconds were ignored and a default backoff was used instead.</li>
<li><strong>Empty response handling</strong>: Responses with <code>content-length: 0</code> now return <code>undefined</code> instead of attempting to parse the body.</li>
<li><strong>Environment variable reading</strong>: Empty string env vars (for example, <code>CLOUDFLARE_API_TOKEN=&quot;&quot;</code>) are now treated as unset.</li>
<li><strong>Path query parameter merging</strong>: URL search params embedded in endpoint paths are now extracted and merged into the query object.</li>
</ul>
<h4 id="removed-endpoints-17">Removed Endpoints (17)</h4>
<p>17 HTTP endpoints were removed from the SDK, affecting <code>abuse-reports</code>, <code>cloudforce-one</code>, <code>dlp/profiles/predefined</code>, <code>email-security/investigate</code>, <code>email-security/settings</code>, and <code>intel/ip-list</code>.</p>
<h4 id="method-signature-changes">Method Signature Changes</h4>
<ul>
<li><code>client.ai.toMarkdown.transform(file, \{ ...params \})</code> -&gt; <code>client.ai.toMarkdown.transform(\{ ...params \})</code> -- <code>file</code> moved from positional arg into params body</li>
<li><code>client.radar.ai.toMarkdown.create(body, \{ ...params \})</code> -&gt; <code>client.radar.ai.toMarkdown.create(\{ ...params \})</code> -- <code>body</code> moved from positional arg into params</li>
<li><code>client.abuseReports.create(reportType, \{ ...params \})</code> -&gt; <code>client.abuseReports.create(reportParam, \{ ...params \})</code> -- positional arg renamed</li>
<li><code>client.iam.userGroups.members.create(userGroupId, [ ...body ])</code> -&gt; <code>client.iam.userGroups.members.create(userGroupId, [ ...members ])</code> -- body array param renamed</li>
</ul>
<h4 id="renamed-client-paths">Renamed Client Paths</h4>
<ul>
<li><code>client.originTLSClientAuth.hostnames.certificates</code> -&gt; <code>client.originTLSClientAuth.zoneCertificates</code></li>
<li><code>client.radar.netflows</code> -&gt; <code>client.radar.netFlows</code> (casing change)</li>
</ul>
<h4 id="return-type-changes-179">Return Type Changes (179)</h4>
<ul>
<li><strong>133 methods now return <code>null</code></strong> instead of a typed response object. This primarily affects delete operations across <code>accounts</code>, <code>cache</code>, <code>d1</code>, <code>filters</code>, <code>firewall</code>, <code>hyperdrive</code>, <code>iam</code>, <code>kv</code>, <code>logpush</code>, <code>logs</code>, <code>r2</code>, <code>stream</code>, <code>workers</code>, <code>zero-trust</code>, <code>zones</code>, and others.</li>
<li><strong>17 methods changed pagination type</strong> (for example, <code>KeysCursorPaginationAfter</code> -&gt; <code>KeysCursorLimitPagination</code>).</li>
<li><strong>29 methods changed to a different named type</strong> (for example, <code>CloudflaredCreateResponse</code> -&gt; <code>CloudflareTunnel</code>).</li>
</ul>
<h4 id="removed-types-43">Removed Types (43)</h4>
<p>24 shared types removed from root namespace (<code>ASN</code>, <code>AuditLog</code>, <code>Member</code>, <code>Permission</code>, <code>Role</code>, <code>Subscription</code>, <code>Token</code>, etc.). 19 response types consolidated or renamed.</p>
<h4 id="resource-restructuring">Resource Restructuring</h4>
<p>19 resources were restructured from single files to directories. Public API client paths are unchanged, but deep imports may break.</p>
<h4 id="new-top-level-resources">New Top-Level Resources</h4>
<p>11 entirely new resources added to the client:</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Client Path</th>
<th>Methods</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>AI Search</td>
<td><code>client.aiSearch</code></td>
<td>46</td>
<td>Instances, namespaces, tokens, and items</td>
</tr>
<tr>
<td>Connectivity</td>
<td><code>client.connectivity</code></td>
<td>5</td>
<td>Directory service APIs</td>
</tr>
<tr>
<td>Email Sending</td>
<td><code>client.emailSending</code></td>
<td>7</td>
<td>Send and send_raw endpoints</td>
</tr>
<tr>
<td>Fraud</td>
<td><code>client.fraud</code></td>
<td>2</td>
<td>Fraud detection API</td>
</tr>
<tr>
<td>Google Tag Gateway</td>
<td><code>client.googleTagGateway</code></td>
<td>2</td>
<td>Google Tag Gateway management</td>
</tr>
<tr>
<td>Organizations</td>
<td><code>client.organizations</code></td>
<td>8</td>
<td>Organization profiles and audit logs</td>
</tr>
<tr>
<td>R2 Data Catalog</td>
<td><code>client.r2DataCatalog</code></td>
<td>11</td>
<td>R2 Data Catalog routes</td>
</tr>
<tr>
<td>Realtime Kit</td>
<td><code>client.realtimeKit</code></td>
<td>54</td>
<td>Realtime Kit APIs</td>
</tr>
<tr>
<td>Resource Tagging</td>
<td><code>client.resourceTagging</code></td>
<td>9</td>
<td>Resource tagging routes</td>
</tr>
<tr>
<td>Token Validation</td>
<td><code>client.tokenValidation</code></td>
<td>13</td>
<td>Token validation rules</td>
</tr>
<tr>
<td>Vulnerability Scanner</td>
<td><code>client.vulnerabilityScanner</code></td>
<td>21</td>
<td>Vulnerability scanning</td>
</tr>
</tbody>
</table>
<h4 id="new-sub-resources-on-existing-resources">New Sub-Resources on Existing Resources</h4>
<ul>
<li><strong>browser-rendering</strong>: <code>crawl</code>, <code>devtools</code> - Crawl endpoints and DevTools methods</li>
<li><strong>cache</strong>: <code>origin-cloud-regions</code> - Origin cloud regions resource</li>
<li><strong>dns</strong>: <code>usage</code> - DNS records usage endpoints</li>
<li><strong>d1</strong>: <code>time-travel</code> - Time travel get_bookmark and restore</li>
<li><strong>email-security</strong>: <code>phishguard</code> - Phishguard reports endpoint</li>
<li><strong>pipelines</strong>: <code>sinks</code>, <code>streams</code> - Pipelines restructure</li>
<li><strong>radar</strong>: <code>agent-readiness</code>, <code>geolocations</code>, <code>post-quantum</code> - New analytics endpoints</li>
<li><strong>workers</strong>: <code>observability</code> - Observability destinations</li>
<li><strong>zones</strong>: <code>environments</code> - Zone environments endpoints</li>
<li><strong>api-gateway</strong>: <code>labels</code> - Labels endpoints</li>
<li><strong>brand-protection</strong>: <code>v2</code> - V2 endpoints</li>
<li><strong>alerting</strong>: <code>silences</code> - Alert silencing API</li>
<li><strong>billing</strong>: <code>usage</code> - Billable usage PayGo endpoint</li>
<li><strong>iam</strong>: <code>sso</code> - SSO Connectors resource</li>
<li><strong>queues</strong>: <code>getMetrics</code> method - Queues metrics endpoint</li>
<li><strong>registrar</strong>: <code>registration-status</code>, <code>update-status</code> - Registrar API convergence</li>
<li><strong>zero-trust</strong>: DLP settings, DEX rules, Access Users, WARP Connector, WARP Subnets, Gateway PAC files, Gateway tenants</li>
</ul>
<h4 id="bug-fixes">Bug Fixes</h4>
<ul>
<li>Resolved type errors from codegen overwriting manual fixes</li>
<li>Fixed <code>post()</code> usage for to-markdown endpoints to resolve async type error</li>
<li>Added least-privilege permissions to all workflow jobs</li>
<li>Reverted erroneous removal of rulesets resource methods and types</li>
<li>Resolved prettier formatting errors in codegen output</li>
</ul>
<h4 id="deprecations">Deprecations</h4>
<p>The following resources now include <code>@deprecated</code> annotations on some methods:</p>
<p><code>accounts</code>, <code>addressing</code>, <code>ai-gateway</code>, <code>aisearch</code>, <code>api-gateway</code>, <code>billing</code>, <code>cloudforce-one</code>, <code>custom-nameservers</code>, <code>dns</code>, <code>email-routing</code>, <code>email-security</code>, <code>filters</code>, <code>firewall</code>, <code>images</code>, <code>intel</code>, <code>keyless-certificates</code>, <code>kv</code>, <code>logpush</code>, <code>origin-tls-client-auth</code>, <code>page-shield</code>, <code>pages</code>, <code>pipelines</code>, <code>radar</code>, <code>rate-limits</code>, <code>registrar</code>, <code>rulesets</code>, <code>ssl</code>, <code>user</code>, <code>workers</code>, <code>workers-for-platforms</code>, <code>zero-trust</code>, <code>zones</code></p>
<h4 id="get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-typescript/releases/tag/v6.0.0">Download TypeScript SDK v6.0.0</a></li>
<li><a href="https://developers.cloudflare.com/api/sdks/typescript/">TypeScript SDK documentation</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-typescript/blob/main/CHANGELOG.md">Full Changelog</a></li>
</ul>
</div></article></div>
