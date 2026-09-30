---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/application-performance/2/
  description: '2026-04-30'
  full_title: Application performance changelog - page 2 | Cloudflare Docs
  head_html: <title>Application performance changelog - page 2 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-04-30"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/application-performance/2/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Application performance changelog - page 2"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-04-30"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/application-performance/2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/application-performance/2/#page","headline":"Application performance changelog - page 2 | Cloudflare Docs","description":"2026-04-30","url":"https://developers.cloudflare.com/changelog/product-group/application-performance/2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/application-performance/2/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="shared-dictionaries-passthrough-now-in-open-beta"><a href="/changelog/post/2026-04-30-shared-dictionaries-passthrough-beta/">Shared dictionaries passthrough now in open beta</a></h2>
<p><em>2026-04-30</em></p>
<p><a href="/speed/optimization/content/shared-dictionaries/">Shared dictionaries</a> (<a href="https://www.rfc-editor.org/rfc/rfc9842.html">RFC 9842</a>) let an origin compress a response against a previous version of the same resource that the browser already has cached, so only the difference between versions travels over the wire. Shared dictionaries passthrough is now in open beta on all plans.</p>
<h4 id="2026-04-30-shared-dictionaries-passthrough-beta-what-changed">What changed</h4>
<p>In passthrough mode, Cloudflare:</p>
<ul>
<li>Forwards the <code>Use-As-Dictionary</code> and <code>Available-Dictionary</code> headers between client and origin without modification.</li>
<li>Treats <code>dcb</code> (Dictionary-Compressed Brotli) and <code>dcz</code> (Dictionary-Compressed Zstandard) as valid <code>Content-Encoding</code> values end to end, without recompressing them.</li>
<li>Extends the cache key to vary on <code>Available-Dictionary</code> and <code>Accept-Encoding</code> so each delta-compressed variant is cached correctly.</li>
</ul>
<p>Your origin manages the dictionary lifecycle: deciding which assets are dictionaries, attaching <code>Use-As-Dictionary</code> headers, and producing deltas in response to <code>Available-Dictionary</code> requests. Cloudflare handles the transport and the cache.</p>
<p>In internal testing on a 272 KB JavaScript bundle, the asset shrinks from 92.1 KB with Gzip to 2.6 KB with delta Zstandard against the previous version — a 97% reduction over standard compression — with download times improving by 81–89% versus Gzip.</p>
<p>Shared dictionaries work with browsers that advertise <code>dcb</code> or <code>dcz</code> in <code>Accept-Encoding</code>. Today, this includes Chrome 130 or later and Edge 130 or later.</p>
<h4 id="2026-04-30-shared-dictionaries-passthrough-beta-get-started">Get started</h4>
<p>Turn on passthrough for your zone with a single API call:</p>
<pre tabindex="0"><code class="language-bash">curl --request PATCH --url https://api.cloudflare.com/client/v4/zones/$ZONE_ID/settings/shared_dictionary_mode</code></pre>
<p>You can also turn it on under <strong>Speed</strong> &gt; <strong>Settings</strong> &gt; <strong>Content Optimization</strong> in the <a href="https://dash.cloudflare.com/?to=/:account/:zone/speed/optimization">Cloudflare dashboard</a>. For full origin setup instructions and a working test recipe, refer to <a href="/speed/optimization/content/shared-dictionaries/">Shared dictionaries</a>, or try the live demo at <a href="https://canicompress.com/">canicompress.com</a>.</p>


<h2 id="web-analytics-adds-navigation-type-filtering-and-reporting"><a href="/changelog/post/2026-04-30-rum-navigation-types/">Web Analytics adds Navigation Type filtering and reporting</a></h2>
<p><em>2026-04-30</em></p>
<p>Cloudflare Web Analytics now supports <strong>Navigation Type</strong> reporting and filtering.</p>
<p>This update allows developers and performance analysts to see how users are navigating between pages — whether through a link click or form submission, a page reload, or using the browser's back/forward buttons — and whether a browser cache hit occurred for these behaviors.</p>
<p>Understanding navigation types is critical for optimizing user experience. For example, if a high volume of your traffic consists of &quot;Back-forward&quot; navigations versus &quot;Back-forward Cache&quot;, those visitors are not benefiting from the Back/Forward Cache (bfcache) and therefore are experiencing higher load times due to potentially unnecessary network requests.</p>
<p>The same applies for regular &quot;Navigate&quot; entries — where &quot;Navigate Cache&quot;, &quot;Navigate Prefetch Cache&quot; and &quot;Prerender&quot; would provide instant document retrieval — and &quot;Reload&quot;, where &quot;Reload cache&quot; would be more optimal.</p>
<p>A high volume of &quot;Reload&quot; entries can also indicate a potential stability problem with your website.</p>
<p>By identifying these patterns, you can tune your browser caching strategies to ensure HTML documents are served instantaneously from local caches rather than requiring a roundtrip to the network.</p>
<p>For more information, refer to <a href="/web-analytics/data-metrics/dimensions/#navigation-types">Navigation Types</a>.</p>
<h4 id="2026-04-30-rum-navigation-types-key-benefits">Key benefits</h4>
<ul>
<li><strong>Monitor Cache Effectiveness:</strong> See how often your site is served from the HTTP cache or bfcache.</li>
<li><strong>Identify Performance Bottlenecks:</strong> Filter by the different types to understand performance opportunity of improving browser cache hit ratio.</li>
</ul>
<h4 id="2026-04-30-rum-navigation-types-analyze-navigation-types-in-the-cloudflare-dashboard">Analyze navigation types in the Cloudflare dashboard</h4>
<p>You can now find the <strong>Navigation Type</strong> dimension in the Web Analytics dashboard. You can filter to include/exclude one or more specific types using &quot;equals&quot;, &quot;does not equal&quot;, &quot;in&quot;, or &quot;not in&quot; matchers.</p>
<p><img src="/assets/upstream/images/web-analytics/dash-web_analytics-navigation-type-filter.png" alt="Navigation Type filter" /></p>
<p>To check the list of popular navigation types, select <strong>Page views</strong> on the Web Analytics sidebar and scroll down to the bottom:</p>
<p><img src="/assets/upstream/images/web-analytics/dash-web_analytics-navigation-types-list.png" alt="Navigation Types list in Page Views tab" /></p>


<h2 id="account-level-enforce-dns-only"><a href="/changelog/post/2026-04-28-enforce-dns-only/">Account-level enforce DNS-only</a></h2>
<p><em>2026-04-28</em></p>
<p>You can now disable Cloudflare's reverse proxy across all zones in your account simultaneously using the new <code>enforce_dns_only</code> setting. When enabled, Cloudflare responds to DNS queries for all proxied records with your origin IP addresses instead of Cloudflare's anycast IPs.
This account-level kill switch is designed for incident response scenarios where you need to quickly route traffic directly to your origin servers.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17717.md")</aside>
<h4 id="2026-04-28-enforce-dns-only-key-characteristics">Key characteristics</h4>
<ul>
<li><strong>Account-level</strong> — Affects all zones in the account simultaneously with a single API call.</li>
<li><strong>Non-destructive</strong> — Does not modify your DNS records. Disabling the setting restores normal proxy behavior.</li>
<li><strong>API-only</strong> — Available through the API only, not in the Cloudflare dashboard.</li>
</ul>
<h4 id="2026-04-28-enforce-dns-only-what-s-affected">What's affected</h4>
<p><strong>Included:</strong> Standard proxied A, AAAA, and CNAME records, Load Balancing records, and records matching Worker routes.</p>
<p><strong>Excluded:</strong> Spectrum applications, Cloudflare Tunnel CNAMEs, R2 custom domains, Web3 gateways, and Workers custom domains continue to operate normally.</p>
<h4 id="2026-04-28-enforce-dns-only-before-you-enable">Before you enable</h4>
<ul>
<li>Verify your origin servers can handle direct traffic without Cloudflare's caching and filtering.</li>
<li>Review which origin IPs will become publicly visible through DNS queries.</li>
<li>Test the API in a staging account before relying on it for incident response.</li>
</ul>
<h4 id="2026-04-28-enforce-dns-only-availability">Availability</h4>
<p>Available via API to all Cloudflare customers.</p>
<p>For information on how to use it, refer to <a href="/dns/proxy-status/enforce-dns-only/">Enforce DNS-only developer documentation</a> .</p>


<h2 id="cache-response-rules-now-support-zone-versioning"><a href="/changelog/post/2026-04-27-cache-response-rules-zone-versioning/">Cache Response Rules now support zone versioning</a></h2>
<p><em>2026-04-27</em></p>
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


<h2 id="smart-tiered-cache-optimizes-public-cloud-origins"><a href="/changelog/post/2026-04-17-smart-tiered-cache-for-public-cloud/">Smart Tiered Cache optimizes public cloud origins</a></h2>
<p><em>2026-04-17</em></p>
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


<h2 id="manage-mtls-and-byo-ca-certificates-from-the-cloudflare-dashboard"><a href="/changelog/post/2026-04-07-mtls-byoca-dashboard/">Manage mTLS and BYO CA certificates from the Cloudflare dashboard</a></h2>
<p><em>2026-04-07</em></p>
<p>You can now manage mutual TLS (mTLS) and Bring Your Own Certificate Authority
(BYO CA) configurations directly from the Cloudflare dashboard — no API required.</p>
<p>Previously, these advanced workflows required the Cloudflare API. The following
are now available in the dashboard:</p>
<ul>
<li><strong>AOP certificate management</strong> — Upload and manage your own
certificate authorities for <a href="/ssl/origin-configuration/authenticated-origin-pull/">Authenticated Origin Pulls (AOP)</a>
directly from the dashboard.</li>
<li><strong>BYO Client mTLS certificate management</strong> — Upload and manage your own CA
certificates for <a href="/ssl/client-certificates/byo-ca/">client mTLS enforcement</a>
without needing API access.</li>
<li><strong>CDN hostname to client mTLS certificate mapping</strong> — Associate client mTLS
certificates with specific hostnames directly from the dashboard.</li>
</ul>


<h2 id="new-quic-rtt-and-delivery-rate-fields"><a href="/changelog/post/2026-04-01-quic-rtt-delivery-rate-fields/">New QUIC RTT and delivery rate fields</a></h2>
<p><em>2026-04-01</em></p>
<p>Two new fields are now available in rule expressions that surface Layer 4 transport telemetry from the client connection. Together with the existing <a href="/ruleset-engine/rules-language/fields/reference/"><code>cf.timings.client_tcp_rtt_msec</code></a> field, these fields give you a complete picture of connection quality for both TCP and QUIC traffic — enabling transport-aware rules without requiring any client-side changes.</p>
<p>Previously, QUIC RTT and delivery rate data was only available via the <code>Server-Timing: cfL4</code> response header. These new fields make the same data available directly in rule expressions, so you can use them in Transform Rules, WAF Custom Rules, and other phases that support dynamic fields.</p>
<h4 id="2026-04-01-quic-rtt-delivery-rate-fields-new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.timings.client_quic_rtt_msec</code></td>
<td>Integer</td>
<td>The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds. Only populated for QUIC (HTTP/3) connections. Returns <code>0</code> for TCP connections.</td>
</tr>
<tr>
<td><code>cf.edge.l4.delivery_rate</code></td>
<td>Integer</td>
<td>The most recent data delivery rate estimate for the client connection, in bytes per second. Returns <code>0</code> when L4 statistics are not available for the request.</td>
</tr>
</tbody>
</table>
<h4 id="2026-04-01-quic-rtt-delivery-rate-fields-example-route-slow-connections-to-a-lightweight-origin">Example: Route slow connections to a lightweight origin</h4>
<p>Use a request header transform rule to tag requests from high-latency connections, so your origin can serve a lighter page variant:</p>
<p><strong>Rule expression:</strong></p>
<pre tabindex="0"><code class="language-txt">cf.timings.client_tcp_rtt_msec &gt; 200 or cf.timings.client_quic_rtt_msec &gt; 200&#10;</code></pre>
<p><strong>Header modifications:</strong></p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Header name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Set</td>
<td><code>X-High-Latency</code></td>
<td><code>true</code></td>
</tr>
</tbody>
</table>
<h4 id="2026-04-01-quic-rtt-delivery-rate-fields-example-match-low-bandwidth-connections">Example: Match low-bandwidth connections</h4>
<pre tabindex="0"><code class="language-txt">cf.edge.l4.delivery_rate &gt; 0 and cf.edge.l4.delivery_rate &lt; 100000&#10;</code></pre>
<p>For more information, refer to <a href="/rules/transform/request-header-modification/">Request Header Transform Rules</a> and the <a href="/ruleset-engine/rules-language/fields/reference/">fields reference</a>.</p>


<h2 id="internal-dns-now-in-open-beta"><a href="/changelog/post/2026-03-31-internal-dns-open-beta/">Internal DNS - now in open beta</a></h2>
<p><em>2026-03-31</em></p>
<p>Internal DNS is now in open beta.</p>
<h4 id="2026-03-31-internal-dns-open-beta-who-can-use-it">Who can use it?</h4>
Internal DNS is bundled as a part of Cloudflare Gateway and is now available to every Enterprise customer with one of the following subscriptions:
<ul>
<li>Cloudflare Zero Trust Enterprise</li>
<li>Cloudflare Gateway Enterprise</li>
</ul>
<p>To learn more and get started, refer to the <a href="/dns/internal-dns/">Internal DNS documentation</a>.</p>


<h2 id="new-mtls-certificate-fields-for-transform-rules"><a href="/changelog/post/2026-03-25-rfc9440-mtls-fields/">New mTLS certificate fields for Transform Rules</a></h2>
<p><em>2026-03-25</em></p>
<p>Cloudflare now exposes four new fields in the Transform Rules phase that encode client certificate data in <a href="https://www.rfc-editor.org/rfc/rfc9440">RFC 9440</a> format. Previously, forwarding client certificate information to your origin required custom parsing of PEM-encoded fields or non-standard HTTP header formats. These new fields produce output in the standardized <code>Client-Cert</code> and <code>Client-Cert-Chain</code> header format defined by RFC 9440, so your origin can consume them directly without any additional decoding logic.</p>
<p>Each certificate is DER-encoded, Base64-encoded, and wrapped in colons. For example, <code>:MIIDsT...Vw==:</code>. A chain of intermediates is expressed as a comma-separated list of such values.</p>
<h4 id="2026-03-25-rfc9440-mtls-fields-new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.tls_client_auth.cert_rfc9440</code></td>
<td>String</td>
<td>The client leaf certificate in RFC 9440 format. Empty if no client certificate was presented.</td>
</tr>
<tr>
<td><code>cf.tls_client_auth.cert_rfc9440_too_large</code></td>
<td>Boolean</td>
<td><code>true</code> if the leaf certificate exceeded 10 KB and was omitted. In practice this will almost always be <code>false</code>.</td>
</tr>
<tr>
<td><code>cf.tls_client_auth.cert_chain_rfc9440</code></td>
<td>String</td>
<td>The intermediate certificate chain in RFC 9440 format as a comma-separated list. Empty if no intermediate certificates were sent or if the chain exceeded 16 KB.</td>
</tr>
<tr>
<td><code>cf.tls_client_auth.cert_chain_rfc9440_too_large</code></td>
<td>Boolean</td>
<td><code>true</code> if the intermediate chain exceeded 16 KB and was omitted.</td>
</tr>
</tbody>
</table>
<p>The chain encoding follows the same ordering as the TLS handshake: the certificate closest to the leaf appears first, working up toward the trust anchor. The root certificate is not included.</p>
<h4 id="2026-03-25-rfc9440-mtls-fields-example-forwarding-client-certificate-headers-to-your-origin-server">Example: Forwarding client certificate headers to your origin server</h4>
<p>Add a request header transform rule to set the <code>Client-Cert</code> and <code>Client-Cert-Chain</code> headers on requests forwarded to your origin server. For example, to forward headers for verified, non-revoked certificates:</p>
<p><strong>Rule expression:</strong></p>
<pre tabindex="0"><code class="language-txt">cf.tls_client_auth.cert_verified and not cf.tls_client_auth.cert_revoked&#10;</code></pre>
<p><strong>Header modifications:</strong></p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Header name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Set</td>
<td><code>Client-Cert</code></td>
<td><code>cf.tls_client_auth.cert_rfc9440</code></td>
</tr>
<tr>
<td>Set</td>
<td><code>Client-Cert-Chain</code></td>
<td><code>cf.tls_client_auth.cert_chain_rfc9440</code></td>
</tr>
</tbody>
</table>
<p>To get the most out of these fields, upload your client CA certificate to Cloudflare so that Cloudflare validates the client certificate at the edge and populates <code>cf.tls_client_auth.cert_verified</code> and <code>cf.tls_client_auth.cert_revoked</code>.</p>
<aside class="nb-aside caution">
<h4 class="nb-aside-title" id="2026-03-25-rfc9440-mtls-fields-prevent-header-injection">Prevent header injection</h4>
@markup("md", "content/.markup/bodies/17749.md")</aside>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">Mutual TLS authentication</a>, <a href="/rules/transform/request-header-modification/">Request Header Transform Rules</a>, and the <a href="/ruleset-engine/rules-language/fields/reference/">fields reference</a>.</p>


<h2 id="cache-response-rules"><a href="/changelog/post/2026-03-24-cache-response-rules/">Cache Response Rules</a></h2>
<p><em>2026-03-24</em></p>
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


<h2 id="dns-analytics-for-customer-metadata-boundary-set-to-eu-region"><a href="/changelog/post/2026-03-20-dns-analytics-cmb-eu/">DNS Analytics for Customer Metadata Boundary set to EU region</a></h2>
<p><em>2026-03-20</em></p>
<p>DNS Analytics is now available for customers with <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary</a> (CMB) set to EU. Query your DNS analytics data while keeping metadata stored in the EU region.</p>
<p>This update includes:</p>
<ul>
<li><strong>DNS Analytics</strong> — Access the same DNS analytics experience for zones in CMB=EU accounts.</li>
<li><strong>EU data residency</strong> — Analytics data is stored and queried from the EU region, meeting data localization requirements.</li>
<li><strong>DNS Firewall Analytics</strong> — DNS Firewall analytics is now supported for CMB=EU customers.</li>
</ul>
<h4 id="2026-03-20-dns-analytics-cmb-eu-availability">Availability</h4>
<p>Available to customers with the <a href="/data-localization/">Data Localization Suite</a> who have Customer Metadata Boundary configured for the EU region.</p>
<h4 id="2026-03-20-dns-analytics-cmb-eu-where-to-find-it">Where to find it</h4>
<ul>
<li><strong>Authoritative DNS:</strong> In the Cloudflare dashboard, select your zone and go to the <strong>Analytics</strong> page.</li>
</ul>
<div class="nb-dash-button"></div>
<ul>
<li><strong>DNS Firewall:</strong> In the Cloudflare dashboard, go to the <strong>DNS Firewall Analytics</strong> page.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For more information, refer to <a href="/dns/additional-options/analytics/">DNS Analytics</a> and <a href="/dns/dns-firewall/analytics/">DNS Firewall Analytics</a>.</p>


<h2 id="worker-execution-timing-field-now-available-in-rules"><a href="/changelog/post/2026-03-18-worker-timing-field/">Worker execution timing field now available in Rules</a></h2>
<p><em>2026-03-18</em></p>
<p>The <code>cf.timings.worker_msec</code> field is now available in the Ruleset Engine. This field reports the wall-clock time that a Cloudflare Worker spent handling a request, measured in milliseconds.</p>
<p>You can use this field to identify slow Worker executions, detect performance regressions, or build rules that respond differently based on Worker processing time, such as logging requests that exceed a latency threshold.</p>
<h4 id="2026-03-18-worker-timing-field-field-details">Field details</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.timings.worker_msec</code></td>
<td>Integer</td>
<td>The time spent executing a Cloudflare Worker in milliseconds. Returns <code>0</code> if no Worker was invoked.</td>
</tr>
</tbody>
</table>
<p>Example filter expression:</p>
<pre tabindex="0"><code>cf.timings.worker_msec &gt; 500&#10;</code></pre>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/fields/reference/cf.timings.worker_msec/">Fields reference</a>.</p>


<h2 id="asynchronous-stale-while-revalidate"><a href="/changelog/post/2026-02-26-async-stale-while-revalidate/">Asynchronous stale-while-revalidate</a></h2>
<p><em>2026-02-26</em></p>
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


<h2 id="control-request-and-response-body-buffering-in-configuration-rules"><a href="/changelog/post/2026-01-27-body-buffering-settings/">Control request and response body buffering in Configuration Rules</a></h2>
<p><em>2026-01-27</em></p>
<p>You can now control how Cloudflare buffers HTTP request and response bodies using two new settings in <a href="/rules/configuration-rules/">Configuration Rules</a>.</p>
<h4 id="2026-01-27-body-buffering-settings-request-body-buffering">Request body buffering</h4>
<p>Controls how Cloudflare buffers HTTP request bodies before forwarding them to your origin server:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Standard</strong> (default)</td>
<td>Cloudflare can inspect a prefix of the request body for enabled functionality such as WAF and Bot Management.</td>
</tr>
<tr>
<td><strong>Full</strong></td>
<td>Buffers the entire request body before sending to origin.</td>
</tr>
<tr>
<td><strong>None</strong></td>
<td>No buffering — the request body streams directly to origin without inspection.</td>
</tr>
</tbody>
</table>
<h4 id="2026-01-27-body-buffering-settings-response-body-buffering">Response body buffering</h4>
<p>Controls how Cloudflare buffers HTTP response bodies before forwarding them to the client:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Standard</strong> (default)</td>
<td>Cloudflare can inspect a prefix of the response body for enabled functionality.</td>
</tr>
<tr>
<td><strong>None</strong></td>
<td>No buffering — the response body streams directly to the client without inspection.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17748.md")</aside>
<h4 id="2026-01-27-body-buffering-settings-api-example">API example</h4>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;action&quot;: &quot;set_config&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;request_body_buffering&quot;: &quot;standard&quot;,&#10;    &quot;response_body_buffering&quot;: &quot;none&quot;&#10;  }&#10;}&#10;</code></pre>
<p>For more information, refer to <a href="/rules/configuration-rules/">Configuration Rules</a>.</p>


<h2 id="new-cryptographic-functions-encode-base64-and-sha256"><a href="/changelog/post/2026-01-22-sha256-base64-encode-functions/">New cryptographic functions — encode_base64() and sha256()</a></h2>
<p><em>2026-01-22</em></p>
<p>Cloudflare Rulesets now includes <code>encode_base64()</code> and <code>sha256()</code> functions, enabling you to generate signed request headers directly in rule expressions. These functions support common patterns like constructing a canonical string from request attributes, computing a SHA256 digest, and Base64-encoding the result.</p>
<hr />
<h4 id="2026-01-22-sha256-base64-encode-functions-new-functions">New functions</h4>
<table>
<thead>
<tr>
<th>Function</th>
<th>Description</th>
<th>Availability</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>encode_base64(input, flags)</code></td>
<td>Encodes a string to Base64 format. Optional <code>flags</code> parameter: <code>u</code> for URL-safe encoding, <code>p</code> for padding (adds <code>=</code> characters to make the output length a multiple of 4, as required by some systems). By default, output is standard Base64 without padding.</td>
<td>All plans (in header transform rules)</td>
</tr>
<tr>
<td><code>sha256(input)</code></td>
<td>Computes a SHA256 hash of the input string.</td>
<td>Requires enablement</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17747.md")</aside>
<hr />
<h4 id="2026-01-22-sha256-base64-encode-functions-examples">Examples</h4>
<p><strong>Encode a string to Base64 format:</strong></p>
<pre tabindex="0"><code class="language-txt">encode_base64(&quot;hello world&quot;)&#10;</code></pre>
<p>Returns: <code>aGVsbG8gd29ybGQ</code></p>
<p><strong>Encode a string to Base64 format with padding:</strong></p>
<pre tabindex="0"><code class="language-txt">encode_base64(&quot;hello world&quot;, &quot;p&quot;)&#10;</code></pre>
<p>Returns: <code>aGVsbG8gd29ybGQ=</code></p>
<p><strong>Perform a URL-safe Base64 encoding of a string:</strong></p>
<pre tabindex="0"><code class="language-txt">encode_base64(&quot;hello world&quot;, &quot;u&quot;)&#10;</code></pre>
<p>Returns: <code>aGVsbG8gd29ybGQ</code></p>
<p><strong>Compute the SHA256 hash of a secret token:</strong></p>
<pre tabindex="0"><code class="language-txt">sha256(&quot;my-token&quot;)&#10;</code></pre>
<p>Returns a hash that your origin can validate to authenticate requests.</p>
<p><strong>Compute the SHA256 hash of a string and encode the result to Base64 format:</strong></p>
<pre tabindex="0"><code class="language-txt">encode_base64(sha256(&quot;my-token&quot;))&#10;</code></pre>
<p>Combines hashing and encoding for systems that expect Base64-encoded signatures.</p>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/functions/">Functions reference</a>.</p>


<h2 id="new-functions-for-array-and-map-operations"><a href="/changelog/post/2026-01-20-array-map-functions/">New functions for array and map operations</a></h2>
<p><em>2026-01-20</em></p>
<h4 id="2026-01-20-array-map-functions-new-functions-for-array-and-map-operations">New functions for array and map operations</h4>
<p>Cloudflare Rulesets now include new functions that enable advanced expression logic for evaluating arrays and maps. These functions allow you to build rules that match against lists of values in request or response headers, enabling use cases like country-based blocking using custom headers.</p>
<hr />
<h4 id="2026-01-20-array-map-functions-new-functions">New functions</h4>
<table>
<thead>
<tr>
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>split(source, delimiter)</code></td>
<td>Splits a string into an array of strings using the specified delimiter.</td>
</tr>
<tr>
<td><code>join(array, delimiter)</code></td>
<td>Joins an array of strings into a single string using the specified delimiter.</td>
</tr>
<tr>
<td><code>has_key(map, key)</code></td>
<td>Returns <code>true</code> if the specified key exists in the map.</td>
</tr>
<tr>
<td><code>has_value(map, value)</code></td>
<td>Returns <code>true</code> if the specified value exists in the map.</td>
</tr>
</tbody>
</table>
<hr />
<h4 id="2026-01-20-array-map-functions-example-use-cases">Example use cases</h4>
<p><strong>Check if a country code exists in a header list:</strong></p>
<pre tabindex="0"><code class="language-txt">has_value(split(http.response.headers[&quot;x-allow-country&quot;][0], &quot;,&quot;), ip.src.country)&#10;</code></pre>
<p><strong>Check if a specific header key exists:</strong></p>
<pre tabindex="0"><code class="language-txt">has_key(http.request.headers, &quot;x-custom-header&quot;)&#10;</code></pre>
<p><strong>Join array values for logging or comparison:</strong></p>
<pre tabindex="0"><code class="language-txt">join(http.request.headers.names, &quot;, &quot;)&#10;</code></pre>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/functions/">Functions reference</a>.</p>


<h2 id="metro-code-field-now-available-in-rules"><a href="/changelog/post/2026-01-12-dma-metro-code-field/">Metro code field now available in Rules</a></h2>
<p><em>2026-01-12</em></p>
<p>The <code>ip.src.metro_code</code> field in the Ruleset Engine is now populated with DMA (Designated Market Area) data.</p>
<p>You can use this field to build rules that target traffic based on geographic market areas, enabling more granular location-based policies for your applications.</p>
<h4 id="2026-01-12-dma-metro-code-field-field-details">Field details</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ip.src.metro_code</code></td>
<td>String | null</td>
<td>The metro code (DMA) of the incoming request's IP address. Returns the designated market area code for the client's location.</td>
</tr>
</tbody>
</table>
<p>Example filter expression:</p>
<pre tabindex="0"><code>ip.src.metro_code eq &quot;501&quot;&#10;</code></pre>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/fields/reference/ip.src.metro_code/">Fields reference</a>.</p>


<h2 id="audit-logs-for-cache-purge-events"><a href="/changelog/post/2025-11-25-audit-logs-for-cache-purge-events/">Audit Logs for Cache Purge Events</a></h2>
<p><em>2025-11-25</em></p>
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


<h2 id="inspect-cache-keys-with-cloudflare-trace"><a href="/changelog/post/2025-11-07-cache-keys-for-cloudflare-trace/">Inspect Cache Keys with Cloudflare Trace</a></h2>
<p><em>2025-11-07</em></p>
<p>You can now see the exact cache key generated for any request directly in Cloudflare Trace. This visibility helps you troubleshoot cache hits and misses, and verify that your Custom Cache Keys — configured via Cache Rules or Page Rules — are working as intended.</p>
<p>Previously, diagnosing caching behavior required inferring the key from configuration settings. Now, you can confirm that your custom logic for headers, query strings, and device types is correctly applied.</p>
<p>Access Trace via the <a href="/rules/trace-request/how-to/#use-trace-in-the-dashboard">dashboard</a> or <a href="/api/resources/request_tracer/methods/trace/">API</a>, either manually for ad-hoc debugging or automated as part of your quality-of-service monitoring.</p>
<h4 id="2025-11-07-cache-keys-for-cloudflare-trace-example-scenario">Example scenario</h4>
<p>If you have a Cache Rule that segments content based on a specific cookie (for example, <code>user_region</code>), run a Trace with that cookie present to confirm the <code>user_region</code> value appears in the resulting cache key.</p>
<p>The Trace response includes the cache key in the <code>cache</code> object:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;step_name&quot;: &quot;request&quot;,&#10;  &quot;type&quot;: &quot;cache&quot;,&#10;  &quot;matched&quot;: true,&#10;  &quot;public_name&quot;: &quot;Cache Parameters&quot;,&#10;  &quot;cache&quot;: {&#10;    &quot;key&quot;: {&#10;      &quot;zone_id&quot;: &quot;023e105f4ecef8ad9ca31a8372d0c353&quot;,&#10;      &quot;scheme&quot;: &quot;https&quot;,&#10;      &quot;host&quot;: &quot;example.com&quot;,&#10;      &quot;uri&quot;: &quot;/images/hero.jpg&quot;&#10;    },&#10;    &quot;key_string&quot;: &quot;023e105f4ecef8ad9ca31a8372d0c353::::https://example.com/images/hero.jpg:::::&quot;&#10;  }&#10;}&#10;</code></pre>
<h4 id="2025-11-07-cache-keys-for-cloudflare-trace-get-started">Get started</h4>
<p>To learn more, refer to the <a href="/rules/trace-request/">Trace documentation</a> and our guide on <a href="/cache/how-to/cache-keys/">Custom Cache Keys</a>.</p>


<h2 id="new-tcp-based-fields-available-in-rulesets"><a href="/changelog/post/2025-10-30-tcp-rtt-and-tcp-fields/">New TCP-based fields available in Rulesets</a></h2>
<p><em>2025-10-30</em></p>
<h4 id="2025-10-30-tcp-rtt-and-tcp-fields-build-rules-based-on-tcp-transport-and-latency">Build rules based on TCP transport and latency</h4>
<p>Cloudflare now provides two new request fields in the Ruleset engine that let you make decisions based on whether a request used TCP and the measured TCP round-trip time between the client and Cloudflare. These fields help you understand protocol usage across your traffic and build policies that respond to network performance. For example, you can distinguish TCP from QUIC traffic or route high latency requests to alternative origins when needed.</p>
<hr />
<h4 id="2025-10-30-tcp-rtt-and-tcp-fields-new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.edge.client_tcp</code></td>
<td>Boolean</td>
<td>Indicates whether the request used TCP. A value of true means the client connected using TCP instead of QUIC.</td>
</tr>
<tr>
<td><code>cf.timings.client_tcp_rtt_msec</code></td>
<td>Number</td>
<td>Reports the smoothed TCP round-trip time between the client and Cloudflare in milliseconds. For example, a value of 20 indicates roughly twenty milliseconds of RTT.</td>
</tr>
</tbody>
</table>
<p>Example filter expression:</p>
<pre tabindex="0"><code>cf.edge.client_tcp &amp;&amp; cf.timings.client_tcp_rtt_msec &lt; 100&#10;</code></pre>
<p>More information can be found in the Rules language <a href="/ruleset-engine/rules-language/fields/reference/">fields reference</a>.</p>


<h2 id="monitor-groups-for-advanced-health-checking-with-load-balancing"><a href="/changelog/post/2025-08-15-monitor-groups-for-load-balancing/">Monitor Groups for Advanced Health Checking With Load Balancing</a></h2>
<p><em>2025-10-16</em></p>
<p>Cloudflare Load Balancing now supports Monitor Groups, a powerful new way to combine multiple health monitors into a single, logical group. This allows you to create sophisticated health checks that more accurately reflect the true availability of your applications by assessing multiple services at once.</p>
<p>With Monitor Groups, you can ensure that all critical components of an application are healthy before sending traffic to an origin pool, enabling smarter failover decisions and greater resilience. This feature is now available via the API for customers with an Enterprise Load Balancing subscription.</p>
<h4 id="2025-08-15-monitor-groups-for-load-balancing-what-you-can-do">What you can do:</h4>
<ul>
<li><strong>Combine Multiple Monitors</strong>: Group different health monitors (for example, HTTP, TCP) that check various application components, like a primary API gateway and a specific <code>/login</code> service.</li>
<li><strong>Isolate Monitors for Observation</strong>: Mark a monitor as &quot;monitoring only&quot; to receive alerts and data without it affecting a pool's health status or traffic steering. This is perfect for testing new checks or observing non-critical dependencies.</li>
<li><strong>Improve Steering Intelligence</strong>: Latency for Dynamic Steering is automatically averaged across all active monitors in a group, providing a more holistic view of an origin's performance.</li>
</ul>
<p>This enhancement is ideal for complex, multi-service applications where the health of one component depends on another. By aggregating health signals, Monitor Groups provide a more accurate and comprehensive assessment of your application's true status.</p>
<p>For detailed information and API configuration guides, please visit our <a href="/load-balancing/monitors/monitor-groups">developer documentation</a> for Monitor Groups.</p>


<h2 id="dns-firewall-analytics-now-in-the-cloudflare-dashboard"><a href="/changelog/post/2025-09-16-DNSFW-Analytics-UI/">DNS Firewall Analytics — now in the Cloudflare dashboard</a></h2>
<p><em>2025-09-16</em></p>
<h4 id="2025-09-16-DNSFW-Analytics-UI-what-s-new">What's New</h4>
<p>Access <a href="/dns/dns-firewall/analytics/">GraphQL-powered DNS Firewall analytics</a> directly in the Cloudflare dashboard.</p>
<p><img src="/assets/upstream/images/changelog/dns/DNSFW_Analytics_UI.png" alt="DNS Firewall Analytics UI" /></p>
<h4 id="2025-09-16-DNSFW-Analytics-UI-explore-four-interactive-panels">Explore Four Interactive Panels</h4>
<ul>
<li><strong>Query summary</strong>: Describes trends over time, segmented by dimensions.</li>
<li><strong>Query statistics</strong>: Describes totals, cached/uncached queries, and processing/response times.</li>
<li><strong>DNS queries by data center</strong>: Describes global view and the top 10 data centers.</li>
<li><strong>Top query statistics</strong>: Shows a breakdown by key dimensions, with search and expand options (up to top 100 items).</li>
</ul>
<p>Additional features:</p>
<ul>
<li>Apply filters and time ranges once. Changes reflect across all panels.</li>
<li>Filter by dimensions like query name, query type, cluster, data center, protocol (UDP/TCP), IP version, response code/reason, and more.</li>
<li>Access up to 62 days of historical data with flexible intervals.</li>
</ul>
<h4 id="2025-09-16-DNSFW-Analytics-UI-availability">Availability</h4>
<p>Available to all DNS Firewall customers as part of their existing subscription.</p>
<h4 id="2025-09-16-DNSFW-Analytics-UI-where-to-find-it">Where to Find It</h4>
<ul>
<li>In the Cloudflare dashboard, go to the <strong>DNS Firewall</strong> page.</li>
</ul>
<div class="nb-dash-button"></div>
<ul>
<li>Refer to the <a href="/dns/dns-firewall/analytics/">DNS Firewall Analytics</a> to learn more.</li>
</ul>


<h2 id="smart-tiered-cache-fallback-to-generic"><a href="/changelog/post/2025-08-29-smart-tiered-cache-fallback-to-generic/">Smart Tiered Cache Fallback to Generic</a></h2>
<p><em>2025-08-29</em></p>
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


<h2 id="manage-and-deploy-your-ai-provider-keys-through-bring-your-own-key-byok-with-ai-gateway-now-powered-by-cloudflare-secrets-store"><a href="/changelog/post/2025-08-25-secrets-store-ai-gateway/">Manage and deploy your AI provider keys through Bring Your Own Key (BYOK) with AI Gateway, now powered by Cloudflare Secrets Store</a></h2>
<p><em>2025-08-25T11:00:00+00:00</em></p>
<p>Cloudflare Secrets Store is now integrated with AI Gateway, allowing you to store, manage, and deploy your AI provider keys in a secure and seamless configuration through <a href="https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/">Bring Your Own Key</a>. Instead of passing your AI provider keys directly in every request header, you can centrally manage each key with Secrets Store and deploy in your gateway configuration using only a reference, rather than passing the value in plain text.</p>
<p>You can now create a secret directly from your AI Gateway <a href="http://dash.cloudflare.com/?to=/:account/ai-gateway">in the dashboard</a> by navigating into your gateway -&gt; <strong>Provider Keys</strong> -&gt; <strong>Add</strong>.</p>
<p><img src="/assets/upstream/images/ssl/add-secret-ai-gateway.png" alt="Import repo or choose template" /></p>
<p>You can also create your secret with the newly available <strong>ai_gateway</strong> scope via <a href="https://developers.cloudflare.com/workers/wrangler/commands/">wrangler</a>, the <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">Secrets Store dashboard</a>, or the <a href="https://developers.cloudflare.com/api/resources/secrets_store/">API</a>.</p>
<p>Then, pass the key in the request header using its Secrets Store reference:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/&lt;ACCOUNT_ID&gt;/my-gateway/anthropic/v1/messages \&#10; &#45;-header &#x27;cf-aig-authorization: ANTHROPIC_KEY_1 \&#10; &#45;-header &#x27;anthropic-version: 2023-06-01&#x27; \&#10; &#45;-header &#x27;Content-Type: application/json&#x27; \&#10; &#45;-data  &#x27;{&quot;model&quot;: &quot;claude-3-opus-20240229&quot;, &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;What is Cloudflare?&quot;}]}&#x27;&#10;</code></pre>
<p>Or, using Javascript:</p>
<pre tabindex="0"><code>import Anthropic from &#x27;@anthropic-ai/sdk&#x27;;&#10;&#10;&#10;const anthropic = new Anthropic({&#10; apiKey: &quot;ANTHROPIC_KEY_1&quot;,&#10; baseURL: &quot;https://gateway.ai.cloudflare.com/v1/&lt;ACCOUNT_ID&gt;/my-gateway/anthropic&quot;,&#10;});&#10;&#10;&#10;const message = await anthropic.messages.create({&#10; model: &#x27;claude-3-opus-20240229&#x27;,&#10; messages: [{role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot;}],&#10; max_tokens: 1024&#10;});&#10;</code></pre>
<p>For more information, check out the <a href="https://blog.cloudflare.com/ai-gateway-aug-2025-refresh">blog</a>!</p>


<h2 id="steer-traffic-by-as-number-in-load-balancing-custom-rules"><a href="/changelog/post/2025-08-15-asnum-support-in-custom-rules/">Steer Traffic by AS Number in Load Balancing Custom Rules</a></h2>
<p><em>2025-08-15</em></p>
<p>You can now create more granular, network-aware Custom Rules in Cloudflare Load Balancing using the Autonomous System Number (ASN) of an incoming request.</p>
<p>This allows you to steer traffic with greater precision based on the network source of a request. For example, you can route traffic from specific Internet Service Providers (ISPs) or enterprise customers to dedicated infrastructure, optimize performance, or enforce compliance by directing certain networks to preferred data centers.</p>
<p><img src="/assets/upstream/images/changelog/load-balancing/asnum-custom-rule.png" alt="Create a Load Balancing Custom Rule using AS Num" /></p>
<p>To get started, create a <a href="https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/">Custom Rule</a> in your Load Balancer and select <strong>AS Num</strong> from the <strong>Field</strong> dropdown.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/application-performance/">Previous</a><span>Page 2 of 4</span><a class="pagination-next" rel="next" href="/changelog/product-group/application-performance/3/">Next</a></nav>
