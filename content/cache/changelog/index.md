---
cp9:
  canonical: https://developers.cloudflare.com/cache/changelog/
  description: Track the latest updates and changes to Cloudflare Cache features.
  full_title: Changelog · Cloudflare Cache (CDN) docs
  head_html: <title>Changelog · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Track the latest updates and changes to Cloudflare Cache features."><link rel="canonical" href="https://developers.cloudflare.com/cache/changelog/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/changelog/index.md"><link rel="alternate" type="application/rss+xml" href="https://developers.cloudflare.com/cache/changelog/index.xml"><meta property="og:title" content="Changelog · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Track the latest updates and changes to Cloudflare Cache features."><meta property="og:url" content="https://developers.cloudflare.com/cache/changelog/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Changelog"><meta name="algolia_content_type" content="Changelog"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/cache/changelog/#page","headline":"Changelog \u00b7 Cloudflare Cache (CDN) docs","description":"Track the latest updates and changes to Cloudflare Cache features.","url":"https://developers.cloudflare.com/cache/changelog/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/changelog/
  schema: 1
---
<h2 id="2026-09-02">2026-09-02</h2>

<strong>Configure Origin Range Requests with the Rulesets API</strong>

<p>The Rulesets API now supports Origin Range Requests in Cache Rules. This setting lets Cloudflare fetch large files from your origin in cache-aligned byte ranges. Cloudflare may expand a client range and issue several single-range origin requests.</p>
<p>Set <code>origin_range_requests.mode</code> to <code>on</code>, <code>off</code>, or <code>default</code> for any traffic matched by a Cache Rule.</p>
<p>To override Cloudflare's default Origin Range Requests behavior, set the mode to <code>off</code>. The following rule turns off generated origin range requests for all traffic without changing cache eligibility:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;expression&quot;: &quot;true&quot;,&#10;  &quot;action&quot;: &quot;set_cache_settings&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;origin_range_requests&quot;: {&#10;      &quot;mode&quot;: &quot;off&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Origin Range Requests do not make otherwise ineligible content cacheable. If your origin ignores <code>Range</code> and returns a complete <code>200 OK</code>, Cloudflare can use the response but must download the complete file. Origins should honor <code>Accept-Encoding: identity</code> and return consistent, unencoded partial responses.</p>
<p>For configuration details and mode behavior, refer to <a href="/cache/how-to/cache-rules/settings/#origin-range-requests">Origin Range Requests in Cache Rules</a>. For client responses and the complete origin contract, refer to <a href="/cache/reference/range-requests/">Range request behavior</a>.</p>


<h2 id="2026-07-02">2026-07-02</h2>

<strong>Cache multiple versions of a URL with Vary</strong>

<p>Your origin can serve different responses for the same URL — different languages based on <code>Accept-Language</code>, or different formats based on <code>Accept</code> — by returning a <a href="https://www.rfc-editor.org/rfc/rfc9110.html#name-vary"><code>Vary</code></a> response header. Cloudflare's cache now honors that header directly in <a href="/cache/how-to/cache-rules/">Cache Rules</a>, so the same URL can hold multiple cached versions and each request is matched to the right one. Content that previously had to bypass cache to stay correct can now be cached, following standard <a href="https://www.rfc-editor.org/rfc/rfc9111.html#name-calculating-cache-keys-with">HTTP caching behavior</a>.</p>
<h4 id="2026-07-02-vary-for-cache-rules-what-changed">What changed</h4>
<p>Your origin now decides which request headers matter by listing them in its <code>Vary</code> response, and you control how Cloudflare treats each one. When you have enabled Vary using a cache rule and a response includes a <code>Vary</code> header, the request headers listed become part of the cache key.</p>
<p>For each header your origin varies on, choose one of three actions:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Behavior</th>
<th>Best for</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>normalize</code></td>
<td>Converts equivalent header values to the same cache key value before matching, collapsing redundant versions.</td>
<td>Most <code>Accept</code>, <code>Accept-Language</code>, and <code>Accept-Encoding</code> use cases.</td>
</tr>
<tr>
<td><code>passthrough</code></td>
<td>Uses the raw header value to select the cached version and forwards it to the origin unchanged.</td>
<td>When byte-for-byte differences in the header value should create versions.</td>
</tr>
<tr>
<td><code>bypass</code></td>
<td>Bypasses cache whenever this header name appears in the origin's <code>Vary</code> response.</td>
<td>Per-user values, or headers with too many possible values to cache safely.</td>
</tr>
</tbody>
</table>
<h4 id="2026-07-02-vary-for-cache-rules-benefits">Benefits</h4>
<ul>
<li><strong>Higher cache hit ratios</strong>: <code>normalize</code> treats semantically equivalent headers as one version. For example, <code>Accept-Language: en-US, fr;q=0.8</code> and <code>Accept-Language: fr;q=0.8, en-GB</code> both resolve to the same cache key, so you serve more requests from cache instead of the origin.</li>
<li><strong>Correct content negotiation</strong>: Requests always receive the cached version that matches their headers, so language and format variants stay accurate.</li>
<li><strong>No origin or Worker changes required</strong>: If your origin already sends <code>Vary</code>, you configure the behavior entirely in Cache Rules.</li>
<li><strong>Standards-aligned</strong>: Cache key calculation follows RFC 9111, and <code>Vary: *</code> continues to bypass cache as required by RFC 9110.</li>
</ul>
<h4 id="2026-07-02-vary-for-cache-rules-availability">Availability</h4>
<p>Vary in Cache Rules is available on all plans (Free, Pro, Business, and Enterprise). For per-request control in Workers subrequests, use the <a href="/workers/runtime-apis/request/#the-cfvary-property"><code>cf.vary</code></a> property.</p>
<h4 id="2026-07-02-vary-for-cache-rules-get-started">Get started</h4>
<p>Configure Vary in the <a href="https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules">Cloudflare dashboard</a> under <strong>Caching</strong> &gt; <strong>Cache Rules</strong>, or through the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a>. To learn how Vary affects cache keys and how each action works, refer to <a href="/cache/concepts/vary/">Vary</a> and the <a href="/cache/how-to/cache-rules/settings/#vary">Cache Rules Vary setting</a>.</p>


<h2 id="2026-05-26">2026-05-26</h2>

<strong>BYPASS status now returned for uncacheable responses</strong>

<p>Cloudflare now returns a <code>BYPASS</code> <a href="/cache/concepts/cache-responses/">cache status</a> whenever a response is not cacheable, instead of the previous mix of <code>BYPASS</code> and <code>MISS</code> that depended on why Cloudflare chose not to cache the response.</p>
<p>There are multiple reasons Cloudflare may refuse to cache a response — for example, the response exceeds the <a href="/cache/concepts/default-cache-behavior/#cacheable-size-limits">maximum cacheable file size</a> for your plan, the origin sends <code>Cache-Control: no-cache</code>, <code>private</code>, or <code>max-age=0</code>, the response includes a <code>Set-Cookie</code> header, or the request includes an <code>Authorization</code> header.</p>
<p>Previously, only some of these conditions returned <code>BYPASS</code>. Others — such as responses exceeding the maximum cacheable file size — returned <code>MISS</code> on every request, regardless of whether <a href="/cache/concepts/cache-control/#origin-cache-control-behavior">Origin Cache Control</a> was on or off. Because the response could never be cached, every subsequent request also returned <code>MISS</code>, which looked indistinguishable from a broken cache and made it hard to tell whether Cloudflare was trying and failing to cache the asset or had deliberately chosen not to cache it.</p>
<p><code>BYPASS</code> now consistently signals that Cloudflare refused to cache the response, regardless of the reason. <code>MISS</code> is reserved for cacheable responses that simply were not in the local cache at request time.</p>
<h4 id="2026-05-26-bypass-status-for-uncacheable-responses-what-to-expect-in-your-analytics">What to expect in your analytics</h4>
<p>After this change rolls out, you should see:</p>
<ul>
<li><strong>MISS rate decreases</strong>: Uncacheable responses no longer count as cache misses.</li>
<li><strong>BYPASS rate increases</strong>: These same responses are now reported as bypasses.</li>
<li><strong>Cache hit ratio increases</strong>: Hit ratio calculations no longer include uncacheable traffic that could never have been cached, giving you a more accurate view of cache effectiveness.</li>
</ul>
<p>Your total request volume and origin traffic are unchanged — only the cache status label is different.</p>
<h4 id="2026-05-26-bypass-status-for-uncacheable-responses-browser-cache-ttl-behavior-is-preserved">Browser cache TTL behavior is preserved</h4>
<p>The cache status label is the only thing changing — browser cache TTL handling for any given response is identical to what it was before:</p>
<ul>
<li>Responses that historically returned <code>MISS</code> because Cloudflare refused to cache them (for example, responses over the maximum cacheable file size) now return <code>BYPASS</code>, but continue to have browser cache TTL applied — exactly as they did when they were labeled <code>MISS</code>.</li>
<li>Responses that historically returned <code>BYPASS</code> and skipped browser cache TTL continue to skip browser cache TTL.</li>
</ul>
<p>In both cases, the decision to apply browser cache TTL depends on the underlying reason Cloudflare did not cache the response, not on the new <code>BYPASS</code> label.</p>


<h2 id="2026-05-04">2026-05-04</h2>

<strong>Pingora now powers Cloudflare's cache</strong>

<p>Cloudflare's cache now runs on a new proxy built on <a href="https://github.com/cloudflare/pingora">Pingora</a>, the Rust-based framework that already serves a significant portion of Cloudflare's network traffic. The new proxy is faster, more memory-safe, and designed to evolve our cache architecture. It delivers immediate performance improvements and enables new caching capabilities.</p>
<h4 id="2026-05-04-pingora-powers-cache-what-this-brings">What this brings</h4>
<ul>
<li><strong>Lower latency</strong>: The new proxy reduces per-request overhead through improved connection reuse.</li>
<li><strong>Reduced cache MISSes</strong>: Enhanced cache retention improves origin offload.</li>
<li><strong>Better RFC compliance</strong>: Caching behavior more closely follows HTTP caching standards.</li>
<li><strong>Foundation for future features</strong>: The new architecture enables upcoming improvements to cache functionality and efficiency.</li>
</ul>
<h4 id="2026-05-04-pingora-powers-cache-new-features">New features</h4>
<ul>
<li><strong>Asynchronous <code>stale-while-revalidate</code></strong>: Every request returns stale content immediately while revalidation happens in the background, instead of the first request after expiry blocking on the origin. Refer to the <a href="/changelog/post/2026-02-26-async-stale-while-revalidate/">asynchronous <code>stale-while-revalidate</code> changelog</a> for details.</li>
<li><strong>Unbuffered bypass by default</strong>: Responses that bypass cache are streamed directly to the client without buffering, reducing time-to-first-byte for uncacheable content.</li>
</ul>
<h4 id="2026-05-04-pingora-powers-cache-behavioral-changes">Behavioral changes</h4>
<p>The new architecture introduces the following behavioral changes to improve RFC compliance and correctness:</p>
<ul>
<li><strong><code>Vary: *</code> results in cache bypass</strong>: According to <a href="https://httpwg.org/specs/rfc9110.html#field.vary">RFC 9110 Section 12.5.5</a>, a <code>Vary</code> header value of <code>*</code> indicates the response varies on factors beyond request headers and must not be served from cache. Cloudflare now bypasses cache for these responses instead of storing them.</li>
<li><strong><code>Set-Cookie</code> stripped on MISS and EXPIRED</strong>: For cacheable assets, <code>Set-Cookie</code> is now stripped on MISS and EXPIRED responses, not only on HITs.</li>
<li><strong>Floating-point TTL values</strong>: Floating-point time-to-live values (for example, <code>max-age=1.5</code>) are rounded down to the nearest integer instead of being rejected as invalid.</li>
</ul>
<h4 id="2026-05-04-pingora-powers-cache-what-s-next">What's next</h4>
<p>A deeper look at the new cache proxy is coming soon to the <a href="https://blog.cloudflare.com/">Cloudflare blog</a>. For background on the underlying framework, read:</p>
<ul>
<li><a href="https://blog.cloudflare.com/pingora-open-source/">Open sourcing Pingora: our Rust framework for building programmable network services</a></li>
<li><a href="https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/">How we built Pingora, the proxy that connects Cloudflare to the Internet</a></li>
</ul>


<h2 id="2026-04-27">2026-04-27</h2>

<strong>Cache Response Rules now support zone versioning</strong>

<p>Cache Response Rules now work with <a href="/version-management/">Version Management</a>. You can version response-phase cache settings and promote them through environments, just like Cache Rules and other supported configurations.</p>
<h4 id="2026-04-27-cache-response-rules-zone-versioning-what-changed">What changed</h4>
<p>Previously, Cache Response Rules were excluded from zone versioning. Any response-phase rule you created applied globally across all environments with no way to test changes in staging first. Cache Rules already supported versioning, but the response phase, where you modify <code>Cache-Control</code> directives, manage cache tags, and strip headers, did not.</p>
<p>Cache Response Rules are now fully integrated with Version Management. You can create or modify response-phase rules within a version, and those changes stay scoped to that version until promoted.</p>
<h4 id="2026-04-27-cache-response-rules-zone-versioning-benefits">Benefits</h4>
<ul>
<li><strong>Safe rollout of cache behavior changes</strong>: Test response-phase rules in a staging environment before promoting to production. Catch unintended caching side effects early.</li>
<li><strong>Parity with Cache Rules</strong>: Cache Response Rules now follow the same versioning workflow as Cache Rules, so you can manage all cache configuration through a single promotion pipeline.</li>
<li><strong>Independent environment control</strong>: Run different response-phase cache settings per environment. For example, strip <code>Set-Cookie</code> headers in staging to validate cacheability without affecting production traffic.</li>
</ul>
<h4 id="2026-04-27-cache-response-rules-zone-versioning-get-started">Get started</h4>
<p>Configure Cache Response Rules in the <a href="https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules">Cloudflare dashboard</a> under <strong>Caching</strong> &gt; <strong>Cache Rules</strong>, or via the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a>. For more details, refer to the <a href="/cache/how-to/cache-response-rules/">Cache Response Rules documentation</a> and the <a href="/version-management/">Version Management documentation</a>.</p>


<h2 id="2026-04-17">2026-04-17</h2>

<strong>Smart Tiered Cache optimizes public cloud origins</strong>

<p>You can now achieve higher cache HIT rates and reduce origin load for origins hosted on public cloud providers with <a href="/cache/how-to/tiered-cache/#smart-tiered-cache">Smart Tiered Cache</a>. By setting a cloud region hint for your origin, Cloudflare selects the optimal upper-tier data center for that cloud region, funneling all cache MISSes through a single location close to your origin.</p>
<p>Previously, Smart Tiered Cache could not reliably select an optimal upper tier for origins behind anycast or regional unicast networks commonly used by cloud providers. Origins on AWS, GCP, Azure, and Oracle Cloud would fall back to a multi-upper-tier topology, resulting in lower cache HIT rates and more requests reaching your origin.</p>
<h4 id="2026-04-17-smart-tiered-cache-for-public-cloud-how-it-works">How it works</h4>
<p>Set a cloud region hint (for example, <code>aws/us-east-1</code> or <code>gcp/europe-west1</code>) for your origin IP or hostname. Smart Tiered Cache uses this hint along with real-time latency data to select a primary upper tier close to your cloud region, plus a fallback in a different location for resilience.</p>
<ul>
<li><strong>Supported providers</strong>: AWS, GCP, Azure, and Oracle Cloud.</li>
<li><strong>All plans</strong>: Available on Free, Pro, Business, and Enterprise plans at no additional cost.</li>
<li><strong>Dashboard and API</strong>: Configure from <strong>Caching</strong> &gt; <strong>Tiered Cache</strong> &gt; <strong>Origin Configuration</strong>, or use the API and Terraform.</li>
</ul>
<h4 id="2026-04-17-smart-tiered-cache-for-public-cloud-get-started">Get started</h4>
<p>To get started, enable <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> and set a cloud region hint for your origin in the <a href="/cache/how-to/tiered-cache/#public-cloud-origins">Tiered Cache settings</a>.</p>


<h2 id="2026-03-24">2026-03-24</h2>

<strong>Cache Response Rules</strong>

<p>You can now control how Cloudflare handles origin responses without changing your origin. Cache Response Rules let you modify <code>Cache-Control</code> directives, manage cache tags, and strip headers like <code>Set-Cookie</code> from origin responses <em>before</em> they reach Cloudflare's cache. Whether traffic is cached or passed through dynamically, these rules give you control over origin response behavior that was previously out of reach.</p>
<h4 id="2026-03-24-cache-response-rules-what-changed">What changed</h4>
<p>Cache Rules previously only operated on request attributes. Cache Response Rules introduce a new response phase that evaluates origin responses and lets you act on them before caching. You can now:</p>
<ul>
<li><strong>Modify <code>Cache-Control</code> directives</strong>: Set or remove individual directives like <code>no-store</code>, <code>no-cache</code>, <code>max-age</code>, <code>s-maxage</code>, <code>stale-while-revalidate</code>, <code>immutable</code>, and more. For example, remove a <code>no-cache</code> directive your origin sends so Cloudflare can cache the asset, or set an <code>s-maxage</code> to control how long Cloudflare stores it.</li>
<li><strong>Set a different browser <code>Cache-Control</code></strong>: Send a different <code>Cache-Control</code> header downstream to browsers and other clients than what Cloudflare uses internally, giving you independent control over edge and browser caching strategies.</li>
<li><strong>Manage cache tags</strong>: Add, set, or remove cache tags on responses, including converting tags from another CDN's header format into Cloudflare's <code>Cache-Tag</code> header. This is especially useful if you are migrating from a CDN that uses a different tag header or delimiter.</li>
<li><strong>Strip headers that block caching</strong>: Remove <code>Set-Cookie</code>, <code>ETag</code>, or <code>Last-Modified</code> headers from origin responses before caching, so responses that would otherwise be treated as uncacheable can be stored and served from cache.</li>
</ul>
<h4 id="2026-03-24-cache-response-rules-benefits">Benefits</h4>
<ul>
<li><strong>No origin changes required</strong>: Fix caching behavior entirely from Cloudflare, even when your origin configuration is locked down or managed by a different team.</li>
<li><strong>Simpler CDN migration</strong>: Match caching behavior from other CDN providers without rewriting your origin. Translate cache tag formats and override directives that do not align with Cloudflare's defaults.</li>
<li><strong>Native support, fewer workarounds</strong>: Functionality that previously required workarounds is now built into Cache Rules with full Tiered Cache compatibility.</li>
<li><strong>Fine-grained control</strong>: Use expressions to match on request and response attributes, then apply precise cache settings per rule. Rules are stackable and composable with existing Cache Rules.</li>
</ul>
<h4 id="2026-03-24-cache-response-rules-get-started">Get started</h4>
<p>Configure Cache Response Rules in the <a href="https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules">Cloudflare dashboard</a> under <strong>Caching</strong> &gt; <strong>Cache Rules</strong>, or via the <a href="https://developers.cloudflare.com/ruleset-engine/rulesets-api/">Rulesets API</a>. For more details, refer to the <a href="https://developers.cloudflare.com/cache/how-to/cache-response-rules/">Cache Rules documentation</a>.</p>


<h2 id="2026-02-26">2026-02-26</h2>

<strong>Asynchronous stale-while-revalidate</strong>

<p>Cloudflare's <a href="/cache/concepts/cache-control/#revalidation"><code>stale-while-revalidate</code></a> support is now fully asynchronous. Previously, the first request for a stale (expired) asset in cache had to wait for an origin response, after which that visitor received a REVALIDATED or EXPIRED status. Now, the first request after the asset expires triggers revalidation in the background and immediately receives stale content with an UPDATING status. All following requests also receive stale content with an <code>UPDATING</code> status until the origin responds, after which subsequent requests receive fresh content with a <code>HIT</code> status.</p>
<p><code>stale-while-revalidate</code> is a <code>Cache-Control</code> directive set by your origin server that allows Cloudflare to serve an expired cached asset while a fresh copy is fetched from the origin.</p>
<p>Asynchronous revalidation brings:</p>
<ul>
<li><strong>Lower latency</strong>: No visitor is waiting for the origin when the asset is already in cache. Every request is served from cache during revalidation.</li>
<li><strong>Consistent experience</strong>: All visitors receive the same cached response during revalidation.</li>
<li><strong>Reduced error exposure</strong>: The first request is no longer vulnerable to origin timeouts or errors. All visitors receive a cached response while revalidation happens in the background.</li>
</ul>
<h4 id="2026-02-26-async-stale-while-revalidate-availability">Availability</h4>
<p>This change is live for all Free, Pro, and Business zones. Approximately 75% of Enterprise zones have been migrated, with the remaining zones rolling out throughout the quarter.</p>
<h4 id="2026-02-26-async-stale-while-revalidate-get-started">Get started</h4>
<p>To use this feature, make sure your origin includes the <code>stale-while-revalidate</code> directive in the <code>Cache-Control</code> header. Refer to the <a href="/cache/concepts/cache-control/#revalidation">Cache-Control documentation</a> for details.</p>


<h2 id="2025-11-25">2025-11-25</h2>

<strong>Audit Logs for Cache Purge Events</strong>

<p>You can now review detailed audit logs for cache purge events, giving you visibility into what purge requests were sent, what they contained, and by whom. Audit your purge requests via the Dashboard or API for all purge methods:</p>
<ul>
<li>Purge everything</li>
<li>List of prefixes</li>
<li>List of tags</li>
<li>List of hosts</li>
<li>List of files</li>
</ul>
<h4 id="2025-11-25-audit-logs-for-cache-purge-events-example">Example</h4>
<p>The detailed audit payload is visible within the Cloudflare Dashboard (under <strong>Manage Account</strong> &gt; <strong>Audit Logs</strong>) and via the API. Below is an example of the Audit Logs v2 payload structure:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;action&quot;: {&#10;    &quot;result&quot;: &quot;success&quot;,&#10;    &quot;type&quot;: &quot;create&quot;&#10;  },&#10;  &quot;actor&quot;: {&#10;    &quot;id&quot;: &quot;1234567890abcdef&quot;,&#10;    &quot;email&quot;: &quot;user@example.com&quot;,&#10;    &quot;type&quot;: &quot;user&quot;&#10;  },&#10;  &quot;resource&quot;: {&#10;    &quot;product&quot;: &quot;purge_cache&quot;,&#10;    &quot;request&quot;: {&#10;      &quot;files&quot;: [&#10;        &quot;https://example.com/images/logo.png&quot;,&#10;        &quot;https://example.com/css/styles.css&quot;&#10;      ]&#10;    }&#10;  },&#10;  &quot;zone&quot;: {&#10;    &quot;id&quot;: &quot;023e105f4ecef8ad9ca31a8372d0c353&quot;,&#10;    &quot;name&quot;: &quot;example.com&quot;&#10;  }&#10;}&#10;</code></pre>
<h4 id="2025-11-25-audit-logs-for-cache-purge-events-get-started">Get started</h4>
<p>To get started, refer to the <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs documentation</a>.</p>


<h2 id="2025-11-07">2025-11-07</h2>

<strong>Inspect Cache Keys with Cloudflare Trace</strong>

<p>You can now see the exact cache key generated for any request directly in Cloudflare Trace. This visibility helps you troubleshoot cache hits and misses, and verify that your Custom Cache Keys — configured via Cache Rules or Page Rules — are working as intended.</p>
<p>Previously, diagnosing caching behavior required inferring the key from configuration settings. Now, you can confirm that your custom logic for headers, query strings, and device types is correctly applied.</p>
<p>Access Trace via the <a href="/rules/trace-request/how-to/#use-trace-in-the-dashboard">dashboard</a> or <a href="/api/resources/request_tracer/methods/trace/">API</a>, either manually for ad-hoc debugging or automated as part of your quality-of-service monitoring.</p>
<h4 id="2025-11-07-cache-keys-for-cloudflare-trace-example-scenario">Example scenario</h4>
<p>If you have a Cache Rule that segments content based on a specific cookie (for example, <code>user_region</code>), run a Trace with that cookie present to confirm the <code>user_region</code> value appears in the resulting cache key.</p>
<p>The Trace response includes the cache key in the <code>cache</code> object:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;step_name&quot;: &quot;request&quot;,&#10;  &quot;type&quot;: &quot;cache&quot;,&#10;  &quot;matched&quot;: true,&#10;  &quot;public_name&quot;: &quot;Cache Parameters&quot;,&#10;  &quot;cache&quot;: {&#10;    &quot;key&quot;: {&#10;      &quot;zone_id&quot;: &quot;023e105f4ecef8ad9ca31a8372d0c353&quot;,&#10;      &quot;scheme&quot;: &quot;https&quot;,&#10;      &quot;host&quot;: &quot;example.com&quot;,&#10;      &quot;uri&quot;: &quot;/images/hero.jpg&quot;&#10;    },&#10;    &quot;key_string&quot;: &quot;023e105f4ecef8ad9ca31a8372d0c353::::https://example.com/images/hero.jpg:::::&quot;&#10;  }&#10;}&#10;</code></pre>
<h4 id="2025-11-07-cache-keys-for-cloudflare-trace-get-started">Get started</h4>
<p>To learn more, refer to the <a href="/rules/trace-request/">Trace documentation</a> and our guide on <a href="/cache/how-to/cache-keys/">Custom Cache Keys</a>.</p>


<h2 id="2025-08-29">2025-08-29</h2>

<strong>Smart Tiered Cache Fallback to Generic</strong>

<p><a href="/cache/how-to/tiered-cache/#smart-tiered-cache">Smart Tiered Cache</a> now falls back to <a href="/cache/how-to/tiered-cache/#generic-global-tiered-cache">Generic Tiered Cache</a> when the origin location cannot be determined, improving cache precision for your content.</p>
<p>Previously, when Smart Tiered Cache was unable to select the optimal upper tier (such as when origins are masked by Anycast IPs), latency could be negatively impacted. This fallback now uses Generic Tiered Cache instead, providing better performance and cache efficiency.</p>
<h4 id="2025-08-29-smart-tiered-cache-fallback-to-generic-how-it-works">How it works</h4>
<p>When Smart Tiered Cache falls back to Generic Tiered Cache:</p>
<ol>
<li><strong>Multiple upper-tiers</strong>: Uses all of Cloudflare's global data centers as a network of upper-tiers instead of a single optimal location.</li>
<li><strong>Distributed cache requests</strong>: Lower-tier data centers can query any available upper-tier for cached content.</li>
<li><strong>Improved global coverage</strong>: Provides better cache hit ratios across geographically distributed visitors.</li>
<li><strong>Automatic fallback</strong>: Seamlessly transitions when origin location cannot be determined, such as with Anycast-masked origins.</li>
</ol>
<h4 id="2025-08-29-smart-tiered-cache-fallback-to-generic-benefits">Benefits</h4>
<ul>
<li><strong>Preserves high performance during fallback</strong>: Smart Tiered Cache now maintains strong cache efficiency even when optimal upper tier selection is not possible.</li>
<li><strong>Minimizes latency impact</strong>: Automatically uses Generic Tiered Cache topology to keep performance high when origin location cannot be determined.</li>
<li><strong>Seamless experience</strong>: No configuration changes or intervention required when fallback occurs.</li>
<li><strong>Improved resilience</strong>: Smart Tiered Cache remains effective across diverse origin infrastructure, including Anycast-masked origins.</li>
</ul>
<h4 id="2025-08-29-smart-tiered-cache-fallback-to-generic-get-started">Get started</h4>
<p>This improvement is automatically applied to all zones using <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a>. No action is required on your part.</p>


<h2 id="2025-04-04">2025-04-04</h2>

<strong>Workers Fetch API can override Cache Rules</strong>

<p>You can now programmatically override Cache Rules using the <code>cf</code> object in the <code>fetch()</code> command. This feature gives you fine-grained control over caching behavior on a per-request basis, allowing Workers to customize cache settings dynamically based on request properties, user context, or business logic.</p>
<h4 id="2025-04-04-workers-fetch-api-override-cache-rules-how-it-works">How it works</h4>
<p>Using the <code>cf</code> object in <code>fetch()</code>, you can override specific Cache Rules settings by:</p>
<ol>
<li><strong>Setting custom cache options</strong>: Pass cache properties in the <code>cf</code> object as the second argument to <code>fetch()</code> to override default Cache Rules.</li>
<li><strong>Dynamic cache control</strong>: Apply different caching strategies based on request headers, cookies, or other runtime conditions.</li>
<li><strong>Per-request customization</strong>: Bypass or modify Cache Rules for individual requests while maintaining default behavior for others.</li>
<li><strong>Programmatic cache management</strong>: Implement complex caching logic that adapts to your application's needs.</li>
</ol>
<h4 id="2025-04-04-workers-fetch-api-override-cache-rules-what-can-be-configured">What can be configured</h4>
<p>Workers can override the following Cache Rules settings through the <code>cf</code> object:</p>
<ul>
<li><strong><code>cacheEverything</code></strong>: Treat all content as static and cache all file types beyond the default cached content.</li>
<li><strong><code>cacheTtl</code></strong>: Set custom time-to-live values in seconds for cached content at the edge, regardless of origin headers.</li>
<li><strong><code>cacheTtlByStatus</code></strong>: Set different TTLs based on the response status code (for example, <code>{ &quot;200-299&quot;: 86400, 404: 1, &quot;500-599&quot;: 0 }</code>).</li>
<li><strong><code>cacheKey</code></strong>: Customize cache keys to control which requests are treated as the same for caching purposes (Enterprise only).</li>
<li><strong><code>cacheTags</code></strong>: Append additional cache tags for targeted cache purging operations.</li>
</ul>
<h4 id="2025-04-04-workers-fetch-api-override-cache-rules-benefits">Benefits</h4>
<ul>
<li><strong>Enhanced flexibility</strong>: Customize cache behavior without modifying zone-level Cache Rules.</li>
<li><strong>Dynamic optimization</strong>: Adjust caching strategies in real-time based on request context.</li>
<li><strong>Simplified configuration</strong>: Reduce the number of Cache Rules needed by handling edge cases programmatically.</li>
<li><strong>Improved performance</strong>: Fine-tune cache behavior for specific use cases to maximize hit rates.</li>
</ul>
<h4 id="2025-04-04-workers-fetch-api-override-cache-rules-get-started">Get started</h4>
<p>To get started, refer to the <a href="/workers/runtime-apis/fetch/">Workers Fetch API documentation</a> and the <a href="/workers/runtime-apis/request/#the-cf-property-requestinitcfproperties">cf object properties documentation</a>.</p>


<h2 id="2025-04-03">2025-04-03</h2>

<strong>All cache purge methods now available for all plans</strong>

<p>You can now access all Cloudflare cache purge methods — no matter which plan you’re on. Whether you need to update a single asset or instantly invalidate large portions of your site’s content, you now have the same powerful tools previously reserved for Enterprise customers.</p>
<p><strong>Anyone on Cloudflare can now:</strong></p>
<ol>
<li><a href="/cache/how-to/purge-cache/purge-everything/">Purge Everything</a>: Clears all cached content associated with a website.</li>
<li><a href="/cache/how-to/purge-cache/purge_by_prefix/">Purge by Prefix</a>: Targets URLs sharing a common prefix.</li>
<li><a href="/cache/how-to/purge-cache/purge-by-hostname/">Purge by Hostname</a>: Invalidates content by specific hostnames.</li>
<li><a href="/cache/how-to/purge-cache/purge-by-single-file/">Purge by URL (single-file purge)</a>: Precisely targets individual URLs.</li>
<li><a href="/cache/how-to/purge-cache/purge-by-tags/">Purge by Tag</a>: Uses Cache-Tag response headers to invalidate grouped assets, offering flexibility for complex cache management scenarios.</li>
</ol>
<p>Want to learn how each purge method works, when to use them, or what limits apply to your plan? Dive into our <a href="/cache/how-to/purge-cache/">purge cache documentation</a> and <a href="https://developers.cloudflare.com/api/resources/cache/methods/purge/">API reference</a> for all the details.</p>


<h2 id="2025-02-12">2025-02-12</h2>

<strong>Configurable multiplexing HTTP/2 to Origin</strong>

<p>You can now configure HTTP/2 multiplexing settings for origin connections on Enterprise plans. This feature allows you to optimize how Cloudflare manages concurrent requests over HTTP/2 connections to your origin servers, improving cache efficiency and reducing connection overhead.</p>
<h4 id="2025-02-12-configurable-multiplexing-http2-to-origin-how-it-works">How it works</h4>
<p>HTTP/2 multiplexing allows multiple requests to be sent over a single TCP connection. With this configuration option, you can:</p>
<ol>
<li><strong>Control concurrent streams</strong>: Adjust the maximum number of concurrent streams per connection.</li>
<li><strong>Optimize connection reuse</strong>: Fine-tune connection pooling behavior for your origin infrastructure.</li>
<li><strong>Reduce connection overhead</strong>: Minimize the number of TCP connections required between Cloudflare and your origin.</li>
<li><strong>Improve cache performance</strong>: Better connection management can enhance cache fetch efficiency.</li>
</ol>
<h4 id="2025-02-12-configurable-multiplexing-http2-to-origin-benefits">Benefits</h4>
<ul>
<li><strong>Customizable performance</strong>: Tailor multiplexing settings to your origin's capabilities.</li>
<li><strong>Reduced latency</strong>: Fewer connection handshakes improve response times.</li>
<li><strong>Lower origin load</strong>: More efficient connection usage reduces server resource consumption.</li>
<li><strong>Enhanced scalability</strong>: Better connection management supports higher traffic volumes.</li>
</ul>
<h4 id="2025-02-12-configurable-multiplexing-http2-to-origin-get-started">Get started</h4>
<p>Enterprise customers can configure HTTP/2 multiplexing settings in the <a href="https://dash.cloudflare.com/">Cloudflare Dashboard</a> or through our <a href="/api/">API</a>.</p>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2025-02-12-configurable-multiplexing-http2-to-origin-important-consideration">Important consideration</h4>
@markup("md", "content/.markup/bodies/17703.md")</aside>


<h2 id="2025-02-04">2025-02-04</h2>

<strong>Fight CSAM More Easily Than Ever</strong>

<p>You can now implement our <strong>child safety tooling</strong>, the <strong><a href="/cache/reference/csam-scanning/">CSAM Scanning Tool</a></strong>, more easily. Instead of requiring external reporting credentials, you only need a verified email address for notifications to onboard. This change makes the tool more accessible to a wider range of customers.</p>
<p><strong>How It Works</strong></p>
<p>When enabled, the tool automatically <a href="https://blog.cloudflare.com/the-csam-scanning-tool/">hashes images for enabled websites as they enter the Cloudflare cache</a>. These hashes are then checked against a database of <strong>known abusive images</strong>.</p>
<ul>
<li><strong>Potential match detected?</strong>
<ul>
<li>The <strong>content URL is blocked</strong>, and</li>
<li><strong>Cloudflare will notify you</strong> about the found matches via the provided email address.</li>
</ul>
</li>
</ul>
<p><strong>Updated Service-Specific Terms</strong></p>
<p>We have also made updates to our <strong><a href="https://www.cloudflare.com/service-specific-terms-application-services/#csam-scanning-tool-terms">Service-Specific Terms</a></strong> to reflect these changes.</p>


<h2 id="2025-01-08">2025-01-08</h2>

<strong>Smart Tiered Cache optimizes Load Balancing Pools</strong>

<p>You can now achieve higher cache hit rates and reduce origin load when using <a href="/load-balancing/">Load Balancing</a> with <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a>. Cloudflare automatically selects a single, optimal tiered data center for all origins in your Load Balancing Pool.</p>
<h4 id="2025-01-08-smart-tiered-cache-for-load-balancing-how-it-works">How it works</h4>
<p>When you use <a href="/load-balancing/">Load Balancing</a> with <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a>, Cloudflare analyzes performance metrics across your pool's origins and automatically selects the optimal Upper Tier data center for the entire pool. This means:</p>
<ul>
<li><strong>Consistent cache location</strong>: All origins in the pool share the same Upper Tier cache.</li>
<li><strong>Higher HIT rates</strong>: Requests for the same content hit the cache more frequently.</li>
<li><strong>Reduced origin requests</strong>: Fewer requests reach your origin servers.</li>
<li><strong>Improved performance</strong>: Faster response times for cache HITs.</li>
</ul>
<h4 id="2025-01-08-smart-tiered-cache-for-load-balancing-example-workflow">Example workflow</h4>
<pre tabindex="0"><code class="language-txt">Load Balancing Pool: api-pool&#10;├── Origin 1: api-1.example.com&#10;├── Origin 2: api-2.example.com&#10;└── Origin 3: api-3.example.com&#10;    ↓&#10;Selected Upper Tier: [Optimal data center based on pool performance]&#10;</code></pre>
<h4 id="2025-01-08-smart-tiered-cache-for-load-balancing-get-started">Get started</h4>
<p>To get started, enable <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> on your zone and configure your <a href="/load-balancing/">Load Balancing Pool</a>.</p>


<h2 id="2024-11-20">2024-11-20</h2>

<strong>Smart Tiered Cache automatically optimizes R2 caching</strong>

<p>You can now reduce latency and lower R2 egress costs automatically when using <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> with <a href="/r2/">R2</a>. Cloudflare intelligently selects a tiered data center close to your R2 bucket location, creating an efficient caching topology without additional configuration.</p>
<h4 id="2024-11-20-smart-tiered-cache-for-r2-how-it-works">How it works</h4>
<p>When you enable <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> for zones using <a href="/r2/">R2</a> as an origin, Cloudflare automatically:</p>
<ol>
<li><strong>Identifies your R2 bucket location</strong>: Determines the geographical region where your R2 bucket is stored.</li>
<li><strong>Selects an optimal Upper Tier</strong>: Chooses a data center close to your bucket as the common Upper Tier cache.</li>
<li><strong>Routes requests efficiently</strong>: All cache misses in edge locations route through this Upper Tier before reaching R2.</li>
</ol>
<h4 id="2024-11-20-smart-tiered-cache-for-r2-benefits">Benefits</h4>
<ul>
<li><strong>Automatic optimization</strong>: No manual configuration required.</li>
<li><strong>Lower egress costs</strong>: Fewer requests to R2 reduce egress charges.</li>
<li><strong>Improved hit ratio</strong>: Common Upper Tier increases cache efficiency.</li>
<li><strong>Reduced latency</strong>: Upper Tier proximity to R2 minimizes fetch times.</li>
</ul>
<h4 id="2024-11-20-smart-tiered-cache-for-r2-get-started">Get started</h4>
<p>To get started, enable <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> on your zone using R2 as an origin.</p>


<h2 id="2024-11-07">2024-11-07</h2>

<strong>Stage and test cache configurations safely</strong>

<p>You can now stage and test cache configurations before deploying them to production. Versioned environments let you safely validate cache rules, purge operations, and configuration changes without affecting live traffic.</p>
<h4 id="2024-11-07-cache-versioning-how-it-works">How it works</h4>
<p>With versioned environments, you can:</p>
<ol>
<li><strong>Create staging versions</strong> of your cache configuration.</li>
<li><strong>Test cache rules</strong> in a non-production environment.</li>
<li><strong>Purge staged content</strong> independently from production.</li>
<li><strong>Validate changes</strong> before promoting to production.</li>
</ol>
<p>This capability integrates with Cloudflare's broader <a href="/version-management/">versioning system</a>, allowing you to manage cache configurations alongside other zone settings.</p>
<h4 id="2024-11-07-cache-versioning-benefits">Benefits</h4>
<ul>
<li><strong>Risk-free testing</strong>: Validate configuration changes without impacting production.</li>
<li><strong>Independent purging</strong>: Clear staging cache without affecting live content.</li>
<li><strong>Deployment confidence</strong>: Catch issues before they reach end users.</li>
<li><strong>Team collaboration</strong>: Multiple team members can work on different versions.</li>
</ul>
<h4 id="2024-11-07-cache-versioning-get-started">Get started</h4>
<p>To get started, refer to the <a href="/version-management/">version management documentation</a>.</p>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2024-11-07-cache-versioning-important-limitation">Important limitation</h4>
@markup("md", "content/.markup/bodies/17701.md")</aside>


<h2 id="2024-11-07-1">2024-11-07</h2>

<strong>Shard cache using custom cache key values</strong>

<p>Enterprise customers can now optimize cache hit ratios for content that varies by device, language, or referrer by <strong>sharding cache</strong> using up to ten values from previously restricted headers with <a href="/cache/how-to/cache-keys/">custom cache keys</a>.</p>
<h4 id="2024-11-07-shard-cache-by-cache-key-how-it-works">How it works</h4>
<p>When configuring <a href="/cache/how-to/cache-keys/">custom cache keys</a>, you can now include values from these headers to create distinct cache entries:</p>
<ul>
<li><strong><code>accept*</code> headers</strong> (for example, <code>accept</code>, <code>accept-encoding</code>, <code>accept-language</code>): Serve different cached versions based on content negotiation.</li>
<li><strong><code>referer</code> header</strong>: Cache content differently based on the referring page or site.</li>
<li><strong><code>user-agent</code> header</strong>: Maintain separate caches for different browsers, devices, or bots.</li>
</ul>
<h4 id="2024-11-07-shard-cache-by-cache-key-when-to-use-cache-sharding">When to use cache sharding</h4>
<ul>
<li>Content varies significantly by device type (mobile vs desktop).</li>
<li>Different language or encoding preferences require distinct responses.</li>
<li>Referrer-specific content optimization is needed.</li>
</ul>
<h4 id="2024-11-07-shard-cache-by-cache-key-example-configuration">Example configuration</h4>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;cache_key&quot;: {&#10;    &quot;custom_key&quot;: {&#10;      &quot;header&quot;: {&#10;        &quot;include&quot;: [&quot;accept-language&quot;, &quot;user-agent&quot;],&#10;        &quot;check_presence&quot;: [&quot;referer&quot;]&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>This configuration creates separate cache entries based on the <code>accept-language</code> and <code>user-agent</code> headers, while also considering whether the <code>referer</code> header is present.</p>
<h4 id="2024-11-07-shard-cache-by-cache-key-get-started">Get started</h4>
<p>To get started, refer to the <a href="/cache/how-to/cache-keys/">custom cache keys documentation</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17702.md")</aside>


<h2 id="2024-09-05">2024-09-05</h2>

<strong>One-click Cache Rules templates now available</strong>

<p>You can now create optimized cache rules instantly with <strong>one-click templates</strong>, eliminating the complexity of manual rule configuration.</p>
<h4 id="2024-09-05-cache-rules-templates-how-it-works">How it works</h4>
<ol>
<li>Navigate to <strong>Rules</strong> &gt; <strong>Templates</strong> in your Cloudflare dashboard.</li>
<li>Select a template for your use case.</li>
<li>Click to apply the template with sensible defaults.</li>
<li>Customize as needed for your specific requirements.</li>
</ol>
<h4 id="2024-09-05-cache-rules-templates-available-cache-templates">Available cache templates</h4>
<ul>
<li><strong>Cache everything</strong>: Adjust the cache level for all requests.</li>
<li><strong>Bypass cache for everything</strong>: Bypass cache for all requests.</li>
<li><strong>Cache default file extensions</strong>: Replicate Page Rules caching behavior by making only default extensions eligible for cache.</li>
<li><strong>Bypass cache on cookie</strong>: Bypass cache for requests containing specific cookies.</li>
<li><strong>Set edge cache time</strong>: Cache responses with status code between 200 and 599 on the Cloudflare edge.</li>
<li><strong>Set browser cache time</strong>: Adjust how long a browser should cache a resource.</li>
</ul>
<h4 id="2024-09-05-cache-rules-templates-get-started">Get started</h4>
<p>To get started, go to <a href="https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules"><strong>Rules &gt; Templates</strong></a> in the dashboard. For more information, refer to the <a href="/cache/how-to/cache-rules/">Cache Rules documentation</a>.</p>


<h2 id="2024-07-19">2024-07-19</h2>

<strong>Regionalized Generic Tiered Cache for higher hit ratios</strong>

<p>You can now achieve higher cache hit ratios with <a href="/cache/how-to/tiered-cache/#generic-global-tiered-cache">Generic Global Tiered Cache</a>. Regional content hashing routes content consistently to the same upper-tier data centers, eliminating redundant caching and reducing origin load.</p>
<h4 id="2024-07-19-regionalized-generic-tiered-cache-how-it-works">How it works</h4>
<p>Regional content hashing groups data centers by region and uses consistent hashing to route content to designated upper-tier caches:</p>
<ul>
<li>Same content always routes to the same upper-tier data center within a region.</li>
<li>Eliminates redundant copies across multiple upper-tier caches.</li>
<li>Increases the likelihood of cache HITs for the same content.</li>
</ul>
<h4 id="2024-07-19-regionalized-generic-tiered-cache-example">Example</h4>
<p>A popular image requested from multiple edge locations in a region:</p>
<ul>
<li><strong>Before</strong>: Cached at 3-4 different upper-tier data centers</li>
<li><strong>After</strong>: Cached at 1 designated upper-tier data center</li>
<li><strong>Result</strong>: 3-4x fewer cache MISSes, reducing origin load and improving performance</li>
</ul>
<h4 id="2024-07-19-regionalized-generic-tiered-cache-get-started">Get started</h4>
<p>To get started, enable <a href="/cache/how-to/tiered-cache/#generic-global-tiered-cache">Generic Global Tiered Cache</a> on your zone.</p>


