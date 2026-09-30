---
cp9:
  canonical: https://developers.cloudflare.com/changelog/16/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 16 | Cloudflare Docs
  head_html: <title>Changelog - page 16 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/16/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 16"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/16/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/16/#page","headline":"Changelog - page 16 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/16/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/16/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-05-07">May 7, 2026</time><div>
<h2 id="post-2026-05-07-virtual-appliance-self-serve-api"><a href="/changelog/post/2026-05-07-virtual-appliance-self-serve-api/">Self-serve provisioning of Cloudflare One Virtual Appliance via API</a></h2>
<div class="changelog-badges"><span>cloudflare-one-appliance</span><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>You can now create, rotate, and delete Cloudflare One Virtual Appliance instances and their license keys directly via the API and Terraform.</p>
<ul>
<li>Create a virtual appliance and receive a license key: <code>POST /accounts/{account_id}/magic/connectors</code> with <code>device.provision_license: true</code>.</li>
<li>Rotate the license key for an existing virtual appliance: <code>PATCH /accounts/{account_id}/magic/connectors/{connector_id}</code> with <code>provision_license: true</code>. The previous key is immediately and irrevocably revoked.</li>
<li>Delete a virtual appliance to release the associated licensed device.</li>
</ul>
<p>The license key is returned in the response only once, at create or rotate time. Copy and store it securely.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure a Cloudflare One Virtual Appliance</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-07">May 7, 2026</time><div>
<h2 id="post-2026-05-07-CSV-export-for-RFIs"><a href="/changelog/post/2026-05-07-CSV-export-for-RFIs/">CSV export and adjustable page density for RFIs</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>You can now export your Requests for Information (RFI) history to a <strong>CSV document</strong> and customize your dashboard view by choosing how many RFI records to load per page.</p>
<h4 id="2026-05-07-CSV-export-for-RFIs-why-this-matters">Why this matters</h4>
These quality-of-life updates focus on data portability and dashboard performance, allowing power users to manage high volumes of requests more efficiently:
<ul>
<li>The new <strong>CSV export</strong> allows you to move RFI data into external tools for custom reporting, internal auditing, or cross-referencing with other security projects without manual data entry</li>
<li>With <strong>adjustable page density</strong>, you can now choose to load more records at once (10, 25 or 50) to scan through history faster</li>
</ul>
<p>Cloudforce One subscribers can find these new options in <a href="https://dash.cloudflare.com/?to=/:account/application-security/threat-intelligence/requests">Cloudflare Dashboard &gt; Application Security &gt; Threat Intelligence &gt; Requests for Information</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-07">May 7, 2026</time><div>
<h2 id="post-2026-05-07-stream-workers-binding"><a href="/changelog/post/2026-05-07-stream-workers-binding/">Introducing Stream Bindings for Workers</a></h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>You can now interact with your Stream video library using new bindings for Workers! This allows customers to upload content to Stream, provision direct uploads, manage videos, and generate signed URLs from a Worker without making authenticated API calls. We're excited to bring Stream and Workers closer together to empower more programmatic pipelines, tighter integrations, and support generative AI and inference workloads.</p>
<p>Use the Stream binding when you want to:</p>
<ul>
<li>Upload videos from URLs or create basic direct upload links for end users</li>
<li>Generate signed playback tokens without managing signing keys</li>
<li>Manage video metadata, captions, downloads, and watermarks</li>
<li>Build video pipelines entirely within Workers</li>
</ul>
<p>To get started, add the Stream binding to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17756.md")</div>
<p><strong>Generate a video with AI and upload directly to Stream</strong> or send a URL of a file you already have:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17757.md")</div>
<p><strong>Generate a signed URL without using a signing key</strong> or an API call:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17758.md")</div>
<p><strong>Get and set video properties</strong> easily:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17759.md")</div>
<p>For setup instructions and the full API reference, refer to <a href="/stream/manage-video-library/bindings/">Bind to Workers API</a>.</p>
<h4 id="2026-05-07-stream-workers-binding-get-started-with-your-agent">Get started with your Agent</h4>
<blockquote>
<p>Add a binding for Cloudflare Stream (env.STREAM). On the watch page, use the
Stream binding to get info based on the ID, and leverage video.meta.name as
the page title.</p>
</blockquote>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-07">May 7, 2026</time><div>
<h2 id="post-2026-05-07-emergency-waf-release"><a href="/changelog/post/2026-05-07-emergency-waf-release/">WAF Release - 2026-05-07 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This emergency release introduces a new rule to detect Next.js App Router middleware and proxy bypass attempts via segment-prefetch routes (CVE-2026-44575).</p>
<p><strong>Key Findings</strong></p>
<p>CVE-2026-44575: Next.js Middleware / Proxy Bypass in App Router Applications via Segment-Prefetch Routes</p>
<p>Successful exploitation allows unauthenticated attackers to bypass middleware or proxy-based authorization checks in affected Next.js App Router applications. This leads to unauthorized access to protected content, potential exposure of sensitive application data, and compromise of application security boundaries.</p>
<p>We strongly recommend upgrading to Next.js 15.5.16 or 16.2.5 (or later) immediately to address the underlying vulnerability. If you cannot upgrade immediately, enforce authorization in the underlying route or page logic instead of relying solely on middleware.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1de95bf6d6374e1099854278e77e4a53">e77e4a53</code>
</td>
<td>N/A</td>
<td>Next.js - Middleware Bypass via Invalid RSC Header - CVE:CVE-2026-44575</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection.
</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-07">May 7, 2026</time><div>
<h2 id="post-2026-05-07-automatic-tracing-across-do-and-worker-subrequests"><a href="/changelog/post/2026-05-07-automatic-tracing-across-do-and-worker-subrequests/">Automatic tracing across Durable Object and Worker subrequests</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now get a single unified trace across Worker-to-Worker subrequests, with trace context propagating automatically. Previously, <a href="/workers/observability/traces/">automatic tracing</a> produced disconnected traces when a Worker called another Worker through a <a href="/workers/runtime-apis/bindings/service-bindings/">service binding</a> or <a href="/durable-objects/">Durable Object</a>.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-04-28-worker-to-worker-context-prop.png" alt="Unified trace showing nested spans across a Durable Object subrequest and a service binding call" /></p>
<p>This means you can:</p>
<ul>
<li>Follow a request through your entire Worker architecture in one trace view</li>
<li>See service binding and Durable Object calls as nested child spans instead of separate traces</li>
<li>Debug cross-Worker request flows in the Cloudflare dashboard or in an external observability platform via <a href="/workers/observability/exporting-opentelemetry-data/">OpenTelemetry</a></li>
</ul>
<p><a href="/workers/observability/traces/#how-to-enable-tracing">Tracing must be enabled</a> in your Wrangler configuration for traces to be recorded. Checkout <a href="/workers/observability/traces/">Workers tracing</a> to get started.</p>
<p>Up next, we are working on external trace context propagation using <a href="https://www.w3.org/TR/trace-context/">W3C Trace Context standards</a>, which will allow traces from your Workers to link with traces from services outside of Cloudflare.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-07">May 7, 2026</time><div>
<h2 id="post-2026-05-06-cloudy-summaries-in-phishnet_o365"><a href="/changelog/post/2026-05-06-cloudy-summaries-in-phishnet_o365/">Cloudy Summaries in PhishNet O365</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>PhishNet users can now access <strong>Cloudy summaries</strong> directly within the email investigation experience. When reviewing a message in PhishNet, users will see an AI-generated summary that provides additional context and key details about the email.</p>
<p>These summaries help users quickly understand the nature of a message without needing to manually parse through headers, body content, and detection signals. Cloudy surfaces the most relevant information so users can make faster, more informed decisions about suspicious emails.</p>
<p><strong>These summaries are not trained on customer data.</strong> They are generated using the outputs of our existing detection models and analysis systems.</p>
<p>This feature is available for PhishNet with Office 365. Support for Gmail will be available by the end of the quarter.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-06">May 6, 2026</time><div>
<h2 id="post-2026-05-06-mesh-ipv6-routes"><a href="/changelog/post/2026-05-06-mesh-ipv6-routes/">IPv6 CIDR routes for Cloudflare Mesh</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span></div><div class="changelog-body"><p><a href="/mesh/">Cloudflare Mesh</a> nodes now support IPv6 CIDR routes. You can advertise both IPv4 and IPv6 subnets through your Mesh nodes, making IPv6-only or dual-stack private networks reachable from any enrolled device.</p>
<p><img src="/assets/upstream/images/cloudflare-one/connections/mesh-ipv6-routes.png" alt="IPv6 CIDR routes on a Mesh node in the Cloudflare dashboard" /></p>
<p>To add an IPv6 route, follow the same steps as <a href="/mesh/features/routes/#add-a-route">adding an IPv4 route</a> — enter the IPv6 CIDR (for example, <code>fd00::/64</code>) when configuring the route in the <a href="https://dash.cloudflare.com/?to=/:account/mesh">dashboard</a> or via the API.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-06">May 6, 2026</time><div>
<h2 id="post-2026-05-06-radar-tld-nameserver-performance"><a href="/changelog/post/2026-05-06-radar-tld-nameserver-performance/">TLD Nameserver Performance in Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now provides TLD authoritative nameserver performance insights, measuring response time (latency) as observed from Cloudflare's <a href="/1.1.1.1/">1.1.1.1</a> resolver infrastructure when forwarding queries upstream to TLD nameservers.</p>
<p>New widgets on <a href="https://radar.cloudflare.com/tlds/com">TLD detail pages</a>:</p>
<ul>
<li><a href="https://radar.cloudflare.com/tlds/com#tld-ns-latency"><strong>Aggregate nameserver latency</strong></a>: Response time percentiles (p25/p50/p75) for all authoritative nameservers of the selected TLD.</li>
<li><a href="https://radar.cloudflare.com/tlds/com#tld-ns-latency-by-ns"><strong>Latency per nameserver</strong></a>: Median response time (p50) broken down by each authoritative nameserver over time.</li>
</ul>
<p><img src="/assets/upstream/images/radar/tld-nameserver-latency-by-ns.png" alt="Latency per nameserver chart" /></p>
<ul>
<li><a href="https://radar.cloudflare.com/tlds/com#geographical-distribution"><strong>Median latency geographic distribution</strong></a>: p50 response time by Cloudflare data center country, displayed on a choropleth map.</li>
<li><a href="https://radar.cloudflare.com/tlds/com#tld-ranking"><strong>TLD ranking over time</strong></a>: Daily DNS magnitude rank and magnitude value with a Rank/Magnitude toggle.</li>
<li><a href="https://radar.cloudflare.com/tlds"><strong>Rank change deltas</strong></a>: 1 week, 4 weeks, and 3 months rank changes added to the TLD magnitude table and the TLD detail info panel.</li>
</ul>
<p><img src="/assets/upstream/images/radar/tld-magnitude-rank-deltas.webp" alt="TLD Rankings by DNS Magnitude table with rank change deltas" /></p>
<p>The new <a href="/api/resources/radar/subresources/tlds/subresources/performance/"><code>TLD Performance</code></a> API provides the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/tlds/subresources/performance/methods/summary/"><code>/tlds/performance/summary/{dimension}</code></a> — TLD nameserver performance summarized by dimension.</li>
<li><a href="/api/resources/radar/subresources/tlds/subresources/performance/methods/timeseries_groups/"><code>/tlds/performance/timeseries_groups/{dimension}</code></a> — TLD nameserver performance over time grouped by dimension.</li>
</ul>
<p>Available dimensions: <code>LATENCY</code> (aggregate p25/p50/p75), <code>NAMESERVER_LATENCY</code> (per-nameserver p50), <code>LOCATION_LATENCY</code> (per-data-center-country p50).</p>
<p>TLD Performance is also available as a dataset in the <a href="https://radar.cloudflare.com/explorer?dataSet=tlds.performance">Data Explorer</a>.</p>
<p>Check out the updated <a href="https://radar.cloudflare.com/tlds/com">TLD detail page</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-06">May 6, 2026</time><div>
<h2 id="post-2026-05-06-TAXII-support-for-threat-events-api"><a href="/changelog/post/2026-05-06-TAXII-support-for-threat-events-api/">TAXII support added to Threat Events API</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>The Cloudforce One Threat Events API now supports <a href="https://www.cloudflare.com/en-gb/learning/security/what-is-stix-and-taxii/"><strong>TAXII</strong></a> as an output format, enabling standardized, automated sharing of cyber threat intelligence with your existing security stack.</p>
<h4 id="2026-05-06-TAXII-support-for-threat-events-api-why-this-matters">Why this matters</h4>
<ul>
<li>You can now ingest Cloudforce One threat data directly into your SIEM, TIP or SOAR tools that prefer TAXII-formatted streams without needing custom translation scripts.</li>
<li>By supporting the TAXII format parameter in our API, security teams can automate the synchronization of indicator data, reducing the manual overhead of updating blocklists and detection rules.</li>
<li>This alignment with industry standards ensures that your threat data remains consistent across different security ecosystems and partner integrations.</li>
</ul>
<h4 id="2026-05-06-TAXII-support-for-threat-events-api-how-to-use-it">How to use it</h4>
<p>When calling the Threat Events API, you can now specify <code>taxii</code> in the <code>format</code> query parameter:</p>
<p><code>GET /accounts/{account_id}/cloudforce_one/threat_events?format=taxii</code></p>
<p>You can find the updated documentation in the <a href="https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list#%28resource%29%20cloudforce_one.threat_events%20%3E%20%28method%29%20list%20%3E%20%28params%29%20default%20%3E%20%28param%29%20format%20%3E%20%28schema%29">Cloudflare API Reference</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-04">May 4, 2026</time><div>
<h2 id="post-2026-05-04-pingora-powers-cache"><a href="/changelog/post/2026-05-04-pingora-powers-cache/">Pingora now powers Cloudflare's cache</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>Cloudflare's cache now runs on a new proxy built on <a href="https://github.com/cloudflare/pingora">Pingora</a>, the Rust-based framework that already serves a significant portion of Cloudflare's network traffic. The new proxy is faster, more memory-safe, and designed to evolve our cache architecture. It delivers immediate performance improvements and enables new caching capabilities.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-04">May 4, 2026</time><div>
<h2 id="post-2026-05-04-keyboard-shortcuts"><a href="/changelog/post/2026-05-04-keyboard-shortcuts/">Keyboard shortcuts for the Cloudflare dashboard</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>You can now navigate, switch context, and take common actions in the Cloudflare dashboard without leaving your keyboard. Press <code>?</code> anywhere to see the full list. Keyboard shortcuts can be disabled by visiting your <a href="https://dash.cloudflare.com/profile/settings">profile settings</a>.</p>
<h4 id="2026-05-04-keyboard-shortcuts-navigate">Navigate</h4>
<table>
<thead>
<tr>
<th>Shortcut</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>g h</code></td>
<td>Go to Home</td>
</tr>
<tr>
<td><code>g a</code></td>
<td>Go to account overview</td>
</tr>
<tr>
<td><code>g z</code></td>
<td>Go to zone overview</td>
</tr>
<tr>
<td><code>g p</code></td>
<td>Go to your profile</td>
</tr>
<tr>
<td><code>g w</code></td>
<td>Go to Workers &amp; Pages</td>
</tr>
<tr>
<td><code>g o</code></td>
<td>Go to Zero Trust</td>
</tr>
<tr>
<td><code>g b</code></td>
<td>Go to billing</td>
</tr>
<tr>
<td><code>g 1</code> – <code>g 5</code></td>
<td>Go to a recent or pinned item (by position in sidebar)</td>
</tr>
<tr>
<td><code>t →</code></td>
<td>Move to the next tab</td>
</tr>
<tr>
<td><code>t ←</code></td>
<td>Move to the previous tab</td>
</tr>
<tr>
<td><code>p →</code></td>
<td>Move to the next page of a table</td>
</tr>
<tr>
<td><code>p ←</code></td>
<td>Move to the previous page of a table</td>
</tr>
</tbody>
</table>
<h4 id="2026-05-04-keyboard-shortcuts-take-action">Take action</h4>
<table>
<thead>
<tr>
<th>Shortcut</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/</code></td>
<td>Open quick search</td>
</tr>
<tr>
<td><code>?</code></td>
<td>Show keyboard shortcuts</td>
</tr>
<tr>
<td><code>s a</code></td>
<td>Switch account</td>
</tr>
<tr>
<td><code>s z</code></td>
<td>Switch zone</td>
</tr>
<tr>
<td><code>s .</code></td>
<td>Star or unstar the current zone</td>
</tr>
<tr>
<td><code>p .</code></td>
<td>Pin or unpin the current page</td>
</tr>
<tr>
<td><code>t s</code></td>
<td>Toggle the sidebar open or closed</td>
</tr>
<tr>
<td><code>t m</code></td>
<td>Expand or collapse all sidebar menus</td>
</tr>
<tr>
<td><code>t a</code></td>
<td>Toggle Ask AI sidebar</td>
</tr>
<tr>
<td><code>d .</code></td>
<td>Toggle dark mode</td>
</tr>
<tr>
<td><code>c u</code></td>
<td>Copy the current URL</td>
</tr>
<tr>
<td><code>c d</code></td>
<td>Copy a deep link URL</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-04">May 4, 2026</time><div>
<h2 id="post-2026-04-27-terraform-support"><a href="/changelog/post/2026-04-27-terraform-support/">Pipelines and R2 Data Catalog now supported in Terraform</a></h2>
<div class="changelog-badges"><span>pipelines</span></div><div class="changelog-body"><p><a href="/pipelines/">Cloudflare Pipelines</a> ingests streaming data via <a href="/workers/">Workers</a> or HTTP endpoints, transforms it with SQL, and writes it to <a href="/r2/">R2</a> as Apache Iceberg tables. <a href="/r2-data-catalog/">R2 Data Catalog</a> manages those Iceberg tables, compaction, and compatibility with query engines like <a href="/r2-sql/">R2 SQL</a>, <a href="/r2-data-catalog/config-examples/spark-scala/">Spark</a>, and <a href="/r2-data-catalog/config-examples/duckdb/">DuckDB</a>.</p>
<p>You can now create and manage both products using Terraform, supported in the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider v5.19.0</a>.</p>
<p>This adds four new resources that let you define your entire data pipeline as infrastructure-as-code: a data catalog, a stream for ingestion, a sink that writes to R2 Data Catalog or R2, and a pipeline that connects them with SQL.</p>
<p>The new Terraform resources are:</p>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/r2_data_catalog"><code>cloudflare_r2_data_catalog</code></a> — enable the data catalog on an R2 bucket</li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline_stream"><code>cloudflare_pipeline_stream</code></a> — create a stream that receives events via HTTP or Worker bindings</li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline_sink"><code>cloudflare_pipeline_sink</code></a> — create a sink that writes to R2 Data Catalog or R2</li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline"><code>cloudflare_pipeline</code></a> — create a pipeline with SQL connecting a stream to a sink</li>
</ul>
<p>Here is a minimal example that creates a stream, an R2 Data Catalog sink, and a pipeline:</p>
<pre tabindex="0"><code class="language-hcl">resource &quot;cloudflare_pipeline_stream&quot; &quot;my_stream&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;my_stream&quot;&#10;  format     = { type = &quot;json&quot; }&#10;  schema = {&#10;    fields = [{&#10;      name     = &quot;value&quot;&#10;      type     = &quot;json&quot;&#10;      required = true&#10;    }]&#10;  }&#10;  http           = { enabled = true, authentication = false, cors = {} }&#10;  worker_binding = { enabled = false }&#10;}&#10;&#10;resource &quot;cloudflare_pipeline_sink&quot; &quot;my_sink&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;my_sink&quot;&#10;  type       = &quot;r2_data_catalog&quot;&#10;  format     = { type = &quot;parquet&quot; }&#10;  schema     = { fields = [] }&#10;  config = {&#10;    account_id = var.cloudflare_account_id&#10;    bucket     = &quot;my-pipeline-bucket&quot;&#10;    table_name = &quot;my_table&quot;&#10;    token      = var.catalog_token&#10;  }&#10;}&#10;&#10;resource &quot;cloudflare_pipeline&quot; &quot;my_pipeline&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;my_pipeline&quot;&#10;  sql        = &quot;INSERT INTO ${cloudflare_pipeline_sink.my_sink.name} SELECT * FROM ${cloudflare_pipeline_stream.my_stream.name}&quot;&#10;}&#10;</code></pre>
<p>For a full end-to-end example that includes R2 bucket creation, data catalog setup, and scoped API token provisioning, refer to the <a href="/pipelines/reference/terraform/">Pipelines Terraform documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-04">May 4, 2026</time><div>
<h2 id="post-2026-05-04-radar-routing-widgets"><a href="/changelog/post/2026-05-04-radar-routing-widgets/">New routing widgets on Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> is expanding its <a href="https://radar.cloudflare.com/routing">Routing section</a> with two new widgets that give a deeper view into how networks announce address space and how RPKI ROA coverage evolves over time.</p>
<h4 id="2026-05-04-radar-routing-widgets-top-ases-by-announced-ip-space-on-country-pages">Top ASes by announced IP space on country pages</h4>
<p>Country routing pages now include a <strong>Top ASes by announced IP space</strong> chart, breaking down the IPv4 and IPv6 address space announced from a country across the autonomous systems that originate it. The chart stacks the IPv4 and IPv6 views vertically, with the top contributing ASes called out by color and the remaining networks aggregated as <strong>Other</strong>.</p>
<p><img src="/assets/upstream/images/radar/country-top-ases-ip-space.png" alt="Screenshot of the top ASes by announced IP space chart on a country routing page" /></p>
<h4 id="2026-05-04-radar-routing-widgets-rpki-roa-deployment-timeseries">RPKI ROA deployment timeseries</h4>
<p>The <a href="https://radar.cloudflare.com/routing/rpki">RPKI sub-page</a> adds an <strong>RPKI ROA deployment</strong> timeseries widget that tracks the share of announced BGP space covered by a valid Route Origin Authorization (ROA) over time, with separate IPv4 and IPv6 lines. A toggle switches the view between the share of covered <strong>prefixes</strong> and the share of covered <strong>IP address space</strong>. The widget is available on global, country, and AS views, so operators can monitor RPKI adoption progress and compare deployment trends across different scopes.</p>
<p><img src="/assets/upstream/images/radar/rpki-roa-deployment-timeseries.png" alt="Screenshot of the RPKI ROA deployment timeseries widget" /></p>
<h4 id="2026-05-04-radar-routing-widgets-api-endpoints">API endpoints</h4>
<p>The data behind these widgets is also available through two new endpoints on the <a href="/api/resources/radar/subresources/bgp/"><code>BGP</code></a> API:</p>
<ul>
<li><a href="/api/resources/radar/subresources/bgp/subresources/ips/subresources/top/methods/ases/"><code>/bgp/ips/top/ases</code></a> - Returns the top autonomous systems by announced IP space (IPv4 <code>/24</code>s or IPv6 <code>/48</code>s), globally or filtered by country, snapped to the nearest 8-hour RIB boundary.</li>
<li><a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/roas/methods/timeseries/"><code>/bgp/rpki/roas/timeseries</code></a> - Returns RPKI ROA validation coverage over time, by share of prefixes or share of IP address space, split by IP version, with optional ASN or location filters.</li>
</ul>
<p>Visit the <a href="https://radar.cloudflare.com/routing">Radar routing section</a> to explore both widgets.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-04">May 4, 2026</time><div>
<h2 id="post-2026-05-04-waf-release"><a href="/changelog/post/2026-05-04-waf-release/">WAF Release - 2026-05-04</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release focuses on new detections to expand coverage across command injection, SQL injection, PHP object injection, remote code execution, and XSS attack vectors.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.</li>
</ul>
<p><strong>Continuous Rule Improvements</strong></p>
<p>We are continuously refining our managed rules to provide more resilient protection and deeper insights into attack patterns. To ensure an optimal security posture, we recommend consistently monitoring the Security Events dashboard and adjusting rule actions as these enhancements are deployed.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="607ec27233b54beb8b89386ef0884a68">f0884a68</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Object Tag - Body (beta)</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"XSS, HTML Injection - Object Tag" (ID:{" "}
				<code class="nb-rule-id" title="e9e3ac45a6d842f1a132fbf70c14e284">0c14e284</code>).
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="0087c27420c54168a10bc05eff012303">ff012303</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Object Tag - Headers</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. The rule previously known as "XSS, HTML
				Injection - Object Tag - Headers (beta)" is now renamed to "XSS, HTML
				Injection - Object Tag - Headers".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="38dc97853ebf40ed9476ec7816f921d9">16f921d9</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Object Tag - URI</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. The rule previously known as "XSS, HTML
				Injection - Object Tag - URI (beta)" is now renamed to "XSS, HTML
				Injection - Object Tag - URI".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="963cb530f72d4c75b2ae7befdc90d21a">dc90d21a</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 9 - Body Vector - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"Command Injection - Generic 9 - Body Vector" (ID:{" "}
				<code class="nb-rule-id" title="155bb67d1061479e995a38510677175f">0677175f</code>)
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6ac1b6dfe22449a798cc7021f8960375">f8960375</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 9 - Header Vector - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"Command Injection - Generic 9 - Header Vector" (ID:{" "}
				<code class="nb-rule-id" title="b31c34a7b29b4aaf9be6883d1eb7a999">1eb7a999</code>)
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="47a9b66dd73a4a558590c4bdef47a800">ef47a800</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 9 - URI Vector - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"Command Injection - Generic 9 - URI Vector" (ID:{" "}
				<code class="nb-rule-id" title="54ad0465c30d4cd2ac7a707197321c6c">97321c6c</code>)
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d2ae4a8093f245a1b9de71bbbeebf804">beebf804</code>
</td>
<td>N/A</td>
<td>Command Injection - Sleep - Body</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection. The rule previously known as "Command Injection
				- Sleep" is now renamed to "Command Injection - Sleep - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="da91868c0d3d44afb846e7830d257566">0d257566</code>
</td>
<td>N/A</td>
<td>Command Injection - Sleep - Headers</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="04863c61e982464b91778f051856fe86">1856fe86</code>
</td>
<td>N/A</td>
<td>Command Injection - Sleep - URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="9dc1a0b8dbb7425db619309be6e43c37">e6e43c37</code>
</td>
<td>N/A</td>
<td>Fortinet FortiSandbox - Command Injection - CVE:CVE-2026-39808</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b84c10f5a8f84800905932dc88118795">88118795</code>
</td>
<td>N/A</td>
<td>Remote Code Execution - Common Bash Bypass - Headers</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="f496c40011f14bfdb5f55ec79299d53b">9299d53b</code>
</td>
<td>N/A</td>
<td>Remote Code Execution - Common Bash Bypass - URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a5f75abac2664554a984d061b0bf33f9">b0bf33f9</code>
</td>
<td>N/A</td>
<td>Remote Code Execution - Common Bash Bypass - Body - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"Remote Code Execution - Common Bash Bypass Body" (ID:{" "}
				<code class="nb-rule-id" title="6e2f7a696ea74c979e7d069cefb7e5b9">efb7e5b9</code>). The rule previously
				known as "Remote Code Execution - Common Bash Bypass Beta" is now
				renamed to "Remote Code Execution - Common Bash Bypass Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bbb31a886ab54f6c8cdd220d33bfe8b9">33bfe8b9</code>
</td>
<td>N/A</td>
<td>PHP Object Injection - 2 - Body - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"PHP Object Injection - 2" (ID:{" "}
				<code class="nb-rule-id" title="8ef3c3f91eef46919cc9cb6d161aafdc">161aafdc</code>)
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e199688ab69746c88c33457f29552387">29552387</code>
</td>
<td>N/A</td>
<td>PHP Object Injection - 2 - Headers</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="eb33d40e96c54e929af6ed9c8104f4c5">8104f4c5</code>
</td>
<td>N/A</td>
<td>PHP Object Injection - 2 - URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="76b15b7b122a4be6a40d8aa96a46201e">6a46201e</code>
</td>
<td>N/A</td>
<td>SQLi - DROP - 2 - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - DROP - 2" (ID:{" "}
				<code class="nb-rule-id" title="a967a167874b42b6898be46e48ac2221">48ac2221</code>)
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e24b2ef4a5c54f97a62db7a68b7f85ee">8b7f85ee</code>
</td>
<td>N/A</td>
<td>SQLi - DROP - 2 - Headers</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="51123f35f1d249358aea8fb11546b5f0">1546b5f0</code>
</td>
<td>N/A</td>
<td>SQLi - DROP - 2 - URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d86d8873310d41f2877458a91e053dce">1e053dce</code>
</td>
<td>N/A</td>
<td>SmarterMail - Remote Code Execution - CVE:CVE-2026-24423</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="00da180570d34b5bae2121acd0023a36">d0023a36</code>
</td>
<td>N/A</td>
<td>SQLi - SELECT Expression - Body</td>
<td>Block</td>
<td>Disabled</td>
<td>Action changed</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="c46d9097c9ef419aa4d9f10626cc211f">26cc211f</code>
</td>
<td>N/A</td>
<td>SQLi - String Concatenation - URI</td>
<td>Block</td>
<td>Disabled</td>
<td>Action changed</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-01">May 1, 2026</time><div>
<h2 id="post-2026-05-01-dynamic-workflows"><a href="/changelog/post/2026-05-01-dynamic-workflows/">Run Workflows inside Dynamic Workers with the @cloudflare/dynamic-workflows library</a></h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p>You can now use <a href="https://github.com/cloudflare/dynamic-workflows"><code>@cloudflare/dynamic-workflows</code></a> to run a <a href="/workflows/">Workflow</a> inside a <a href="/dynamic-workers/">Dynamic Worker</a>, ensuring durable execution for code that is loaded at runtime.</p>
<p>The Worker Loader loads Dynamic Workers on demand, which previously made durability challenging. Even within a Dynamic Worker, a Workflow might sleep for hours or days between steps, and by the time it resumes, the original Dynamic Worker code would no longer be in memory.</p>
<p>The library solves this by tagging each Workflow instance with metadata that identifies which Dynamic Worker to load — for example, a tenant ID — then reloading the matching Dynamic Worker through the Worker Loader whenever a Workflow awakens.</p>
<p>Because Dynamic Workers are created on-demand, you do not have to register each Workflow up front or manage them individually. Load the Workflow code in the Dynamic Worker when it is needed, and the Workflows engine handles persistence and retries behind the scenes. Your Workflow code itself is unaffected by the routing and behaves as normal.</p>
<p>This unlocks patterns where the Workflow code itself is dynamic. For example, this is useful with:</p>
<ul>
<li><strong>SaaS platforms</strong> where each tenant defines their own automation, such as onboarding sequences, approval chains, or billing retry logic.</li>
<li><strong>AI agent frameworks</strong> where agents generate and execute multi-step plans at runtime, surviving restarts and waiting for human approval between tool calls.</li>
<li><strong>Multi-tenant job systems</strong> where each customer submits their own processing logic and every step persists progress and retries on failure.</li>
</ul>
<pre tabindex="0"><code class="language-ts">import {&#10;	createDynamicWorkflowEntrypoint,&#10;	DynamicWorkflowBinding,&#10;	wrapWorkflowBinding,&#10;	type WorkflowRunner,&#10;} from &quot;@cloudflare/dynamic-workflows&quot;;&#10;&#10;export { DynamicWorkflowBinding };&#10;&#10;interface Env {&#10;	WORKFLOWS: Workflow;&#10;	LOADER: WorkerLoader;&#10;}&#10;&#10;function loadTenant(env: Env, tenantId: string) {&#10;	return env.LOADER.get(tenantId, async () =&gt; ({&#10;		compatibilityDate: &quot;2026-01-01&quot;,&#10;		mainModule: &quot;index.js&quot;,&#10;		modules: { &quot;index.js&quot;: await fetchTenantCode(tenantId) },&#10;		// The Dynamic Worker uses this exactly like a real Workflow binding;&#10;		// every create() is tagged with { tenantId } automatically.&#10;		env: { WORKFLOWS: wrapWorkflowBinding({ tenantId }) },&#10;	}));&#10;}&#10;&#10;// The entrypoint name must match `class_name` in the workflows binding of your Wrangler config file.&#10;export const DynamicWorkflow = createDynamicWorkflowEntrypoint&lt;Env&gt;(&#10;	async ({ env, metadata }) =&gt; {&#10;		const stub = loadTenant(env, metadata.tenantId as string);&#10;		return stub.getEntrypoint(&quot;TenantWorkflow&quot;) as unknown as WorkflowRunner;&#10;	},&#10;);&#10;&#10;export default {&#10;	fetch(request: Request, env: Env) {&#10;		const tenantId = request.headers.get(&quot;x-tenant-id&quot;)!;&#10;		return loadTenant(env, tenantId).getEntrypoint().fetch(request);&#10;	},&#10;};&#10;</code></pre>
<p>For a full walkthrough, refer to the <a href="/dynamic-workers/usage/dynamic-workflows/">Dynamic Workflows guide</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-30">Apr 30, 2026</time><div>
<h2 id="post-2026-04-30-ipsec-post-quantum-third-party"><a href="/changelog/post/2026-04-30-ipsec-post-quantum-third-party/">Post-quantum IPsec interoperability with third-party devices</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>Cloudflare IPsec now supports post-quantum key agreement with compatible third-party devices. <a href="https://www.cisco.com/">Cisco</a> and <a href="https://www.fortinet.com/">Fortinet</a> are the first third-party vendors validated to interoperate with Cloudflare IPsec using ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).</p>
<p>Post-quantum IPsec uses <a href="https://datatracker.ietf.org/doc/rfc9370/">RFC 9370</a> and <a href="https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/">draft-ietf-ipsecme-ikev2-mlkem</a> to negotiate hybrid key agreement during the IKEv2 <code>IKE_INTERMEDIATE</code> phase. This combines classical Diffie-Hellman (Group 20) with ML-KEM-768 or ML-KEM-1024 to protect against <a href="https://en.wikipedia.org/wiki/Harvest_now,_decrypt_later">harvest-now, decrypt-later</a> attacks.</p>
<p>Key details:</p>
<ul>
<li>Compatible with Cisco 8000 Series Secure Routers with IOS XR Release 26.1.1 and Fortinet FortiOS 7.6.6 and later.</li>
<li>Uses ML-KEM-768 or ML-KEM-1024 as an additional Key Exchange to DH Group 20.</li>
<li>Follows RFC 9370 and draft-ietf-ipsecme-ikev2-mlkem standards.</li>
<li>No additional licensing required.</li>
</ul>
<p>Post-quantum IPsec with third-party devices is now generally available with confirmed interoperability for the platforms listed above. Cloudflare intends to support interoperability with more vendors as they build out support for draft-ietf-ipsecme-ikev2-mlkem. Contact your account team to discuss support for additional vendors.</p>
<p>For supported key exchange methods and the list of validated platforms, refer to <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/#tested-third-party-vendor-interoperability">GRE and IPsec tunnels</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-30">Apr 30, 2026</time><div>
<h2 id="post-2026-04-30-data-classification"><a href="/changelog/post/2026-04-30-data-classification/">Classify sensitive content with Data Classification</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>Cloudflare DLP now includes <strong>Data Classification</strong>, which lets administrators organize and label sensitive content using labels, templates, and reusable data classes.</p>
<p>With Data Classification, administrators can define labels such as sensitivity schemas and levels, and data tag groups and tags. Administrators can also build from Cloudflare-managed templates and create reusable data classes that combine detection entries, other data classes, sensitivity levels, and data tags.</p>
<p>You can then use those classifications in custom DLP profiles to identify the severity of sensitive content, understand where it exists, and apply that logic consistently across DLP profiles.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/data-classification/">Data Classification</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-30">Apr 30, 2026</time><div>
<h2 id="post-2026-04-30-standalone-predefined-detection-entries"><a href="/changelog/post/2026-04-30-standalone-predefined-detection-entries/">New predefined detection entries are available</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>Cloudflare DLP now includes new predefined detection entries.</p>
<p>The expanded catalog includes detections for specific credential types, webhooks, addresses, tax identifiers, national IDs, financial data, and crypto wallets.</p>
<p>Examples include <code>GitHub PAT</code>, <code>OpenAI API Key</code>, <code>Slack Webhook</code>, <code>Discord Webhook</code>, <code>US Physical Address</code>, and <code>Bitcoin Wallet</code>.</p>
<p>For the full list, refer to <a href="/cloudflare-one/data-loss-prevention/detection-entries/predefined-detection-entries/">Predefined detection entries</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-30">Apr 30, 2026</time><div>
<h2 id="post-2026-04-30-go-sdk-v7.0.0"><a href="/changelog/post/2026-04-30-go-sdk-v7.0.0/">Go SDK v7.0.0 Released</a></h2>
<div class="changelog-badges"><span>sdk</span><span>go-sdk</span></div><div class="changelog-body"><p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-go/compare/v6.10.0...v7.0.0">v6.10.0...v7.0.0</a></p>
<p>This is a major version release that includes breaking changes to three packages: <code>ai_search</code>, <code>email_security</code>, and <code>workers</code>. These changes reflect upstream API specification updates that improve type correctness and consistency.</p>
<p><strong>Please ensure you read through the list of changes below before moving to this version</strong> - this will help you understand any down or upstream issues it may cause to your environments.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-breaking-changes">Breaking Changes</h4>
<p>See the <a href="https://github.com/cloudflare/cloudflare-go/blob/main/docs/migration-guides/v7.0.0-migration-guide.md">v7.0.0 Migration Guide</a> for before/after code examples and actions needed for each change.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-ai-search-searchforagents-metadata-removed">AI Search - SearchForAgents Metadata Removed</h4>
<p>The <code>SearchForAgents</code> nested type has been removed from all instance metadata structs. This field is no longer part of the API specification.</p>
<p><strong>Removed Types:</strong></p>
<ul>
<li><code>InstanceNewResponseMetadataSearchForAgents</code></li>
<li><code>InstanceUpdateResponseMetadataSearchForAgents</code></li>
<li><code>InstanceListResponseMetadataSearchForAgents</code></li>
<li><code>InstanceDeleteResponseMetadataSearchForAgents</code></li>
<li><code>InstanceReadResponseMetadataSearchForAgents</code></li>
<li><code>InstanceNewParamsMetadataSearchForAgents</code></li>
<li><code>InstanceUpdateParamsMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceNewResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceUpdateResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceListResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceDeleteResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceReadResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceNewParamsMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceUpdateParamsMetadataSearchForAgents</code></li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-path-parameter-type-changes">Email Security - Path Parameter Type Changes</h4>
<p>Multiple Email Security settings sub-resources have changed their path parameter types from <code>int64</code> to <code>string</code>:</p>
<ul>
<li><code>AllowPolicies</code> (<code>policyID int64</code> -&gt; <code>policyID string</code>)</li>
<li><code>BlockSenders</code> (<code>patternID int64</code> -&gt; <code>patternID string</code>)</li>
<li><code>Domains</code> (<code>domainID int64</code> -&gt; <code>domainID string</code>)</li>
<li><code>ImpersonationRegistry</code> (<code>displayNameID int64</code> -&gt; <code>impersonationRegistryID string</code>)</li>
<li><code>TrustedDomains</code> (<code>trustedDomainID int64</code> -&gt; <code>trustedDomainID string</code>)</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-investigate-parameter-rename">Email Security - Investigate Parameter Rename</h4>
<p>The <code>Investigate.Get</code>, <code>Investigate.Move.New</code>, and <code>Investigate.Reclassify.New</code> methods now use <code>investigateID</code> instead of <code>postfixID</code> as the path parameter name.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-domains-bulkdelete-method-removed">Email Security - Domains BulkDelete Method Removed</h4>
<p>The <code>SettingDomainService.BulkDelete</code> method and its associated types have been removed:</p>
<ul>
<li><code>SettingDomainBulkDeleteResponse</code></li>
<li><code>SettingDomainBulkDeleteParams</code></li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-trusteddomains-return-type-change">Email Security - TrustedDomains Return Type Change</h4>
<p><code>SettingTrustedDomainService.New</code> now returns <code>*SettingTrustedDomainNewResponse</code> instead of <code>*SettingTrustedDomainNewResponseUnion</code>.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-investigate-move-return-type-change">Email Security - Investigate.Move Return Type Change</h4>
<p><code>InvestigateMoveService.New</code> now returns <code>*pagination.SinglePage[InvestigateMoveNewResponse]</code> instead of <code>*[]InvestigateMoveNewResponse</code>.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-workers-observability-telemetry-filter-restructuring">Workers - Observability Telemetry Filter Restructuring</h4>
<p>The observability telemetry filter parameter types have been restructured to support nested filter groups. New discriminated union types replace the previous flat filter arrays:</p>
<ul>
<li><code>ObservabilityTelemetryKeysParams.Filters</code> now accepts <code>FiltersObjectFilterUnion</code> (was <code>[]interface\{\}</code>)</li>
<li><code>ObservabilityTelemetryQueryParams.Parameters.Filters</code> now accepts <code>FiltersObjectFilterUnion</code></li>
<li><code>ObservabilityTelemetryValuesParams.Filters</code> now accepts <code>FiltersObjectFilterUnion</code></li>
</ul>
<p>New types include <code>FiltersObjectFiltersObject</code> (for group filters with <code>FilterCombination</code>) and <code>FiltersWorkersObservabilityFilterLeaf</code> (for leaf filters with typed <code>Operation</code>, <code>Type</code>, and <code>Value</code> fields).</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-features">Features</h4>
<h4 id="2026-04-30-go-sdk-v7.0.0-organizations-audit-logs-client-organizations-logs-audit">Organizations - Audit Logs (<code>client.Organizations.Logs.Audit</code>)</h4>
<p><strong>NEW SERVICE:</strong> Query organization audit logs with cursor-based pagination.</p>
<ul>
<li><code>List()</code> - Retrieve audit logs</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-browser-rendering-client-browserrendering">Browser Rendering (<code>client.BrowserRendering</code>)</h4>
<ul>
<li><code>client.BrowserRendering.Devtools.Browser.Targets.Close()</code> - Close a specific browser target (tab, page) by ID</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-queues-client-queues">Queues (<code>client.Queues</code>)</h4>
<ul>
<li><code>client.Queues.GetMetrics()</code> - Retrieve queue metrics for a specific queue</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-ai-search-client-aisearch">AI Search (<code>client.AISearch</code>)</h4>
<ul>
<li>Added <code>WaitForCompletion</code> parameter to <code>NamespaceInstanceItemNewOrUpdateParams</code> and <code>NamespaceInstanceItemSyncParams</code> for synchronous indexing confirmation</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>Magic Transit</strong>: <code>ConnectorService.List</code> parameter name corrected from <code>query</code> to <code>params</code> (non-functional, affects generated documentation only)</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-deprecations">Deprecations</h4>
<p>None in this release.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-go/releases/tag/v7.0.0">Download Go SDK v7.0.0</a></li>
<li><a href="https://developers.cloudflare.com/api/sdks/go/">Go SDK documentation</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-go/blob/main/docs/migration-guides/v7.0.0-migration-guide.md">Migration Guide</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-30">Apr 30, 2026</time><div>
<h2 id="post-2026-04-30-r2-empty-bucket-folder-delete"><a href="/changelog/post/2026-04-30-r2-empty-bucket-folder-delete/">Empty buckets and delete folders from the R2 dashboard</a></h2>
<div class="changelog-badges"><span>r2</span></div><div class="changelog-body"><p>You can now empty an entire <a href="/r2/">R2</a> bucket or delete folders directly from the dashboard. Emptying a bucket is required before you can delete it. Previously, this required scripting or configuring <a href="/r2/buckets/object-lifecycles/">lifecycle rules</a>. Now, the dashboard can handle it in a single action.</p>
<h4 id="2026-04-30-r2-empty-bucket-folder-delete-empty-a-bucket">Empty a bucket</h4>
<p>Go to your bucket's <strong>Settings</strong> tab and select <strong>Empty</strong> under the <strong>Empty Bucket</strong> section. This deletes all objects in the bucket while preserving the bucket and its configuration. For large buckets, the operation runs in the background and the dashboard displays progress.</p>
<p>Emptying a bucket is also a prerequisite for deleting it. The dashboard now guides you through both steps in one place.</p>
<p><img src="/assets/upstream/images/r2/empty-bucket-changelog.png" alt="Empty Bucket and Delete Bucket sections in the R2 dashboard Settings tab" /></p>
<h4 id="2026-04-30-r2-empty-bucket-folder-delete-delete-folders">Delete folders</h4>
<p>R2 uses a flat object structure. The dashboard groups objects that share a common prefix into folders when the <strong>View prefixes as directories</strong> checkbox is selected. Deleting a folder removes every object under that prefix.</p>
<p>From the <strong>Objects</strong> tab, you can select one or more folders and delete them alongside individual objects.</p>
<p>For step-by-step instructions, refer to <a href="/r2/buckets/delete-buckets/">Delete buckets</a> and <a href="/r2/objects/delete-objects/">Delete objects</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-30">Apr 30, 2026</time><div>
<h2 id="post-2026-04-30-radar-cloud-observatory-connection-metrics"><a href="/changelog/post/2026-04-30-radar-cloud-observatory-connection-metrics/">Cloud Observatory connection metrics improvements</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p>The <a href="https://radar.cloudflare.com/cloud-observatory">Cloud Observatory</a> on <a href="/radar/"><strong>Radar</strong></a> now provides improved connection metric insights, offering new ways to explore TCP round-trip time, TCP handshake duration, TLS handshake duration, and response header receive duration across cloud provider origin servers.</p>
<p>The <a href="https://radar.cloudflare.com/cloud-observatory#connection-metrics">Cloud Observatory overview</a> now shows connection metrics broken down by cloud provider, making it easy to compare connection performance across Amazon Web Services, Google Cloud, Microsoft Azure, and Oracle Cloud.</p>
<p><img src="/assets/upstream/images/radar/cloud-observatory-connection-metrics-by-provider.png" alt="Screenshot of Cloud Observatory connection metrics broken down by cloud provider" /></p>
<p>Each <a href="https://radar.cloudflare.com/cloud-observatory/amazon#connection-metrics">provider page</a> now shows connection metrics for the top five regions, with a selector to rank by lowest or highest values.</p>
<p><img src="/assets/upstream/images/radar/cloud-observatory-connection-metrics-by-region.png" alt="Screenshot of Cloud Observatory connection metrics broken down by region for a provider" /></p>
<p>Each <a href="https://radar.cloudflare.com/cloud-observatory/amazon/us-east-1#connection-metrics">region page</a> now displays connection metrics as percentile distributions (25th percentile, median, and 75th percentile), providing insight into the range and variability of connection times.</p>
<p><img src="/assets/upstream/images/radar/cloud-observatory-connection-metrics-percentiles.png" alt="Screenshot of Cloud Observatory connection metrics with percentile distribution for a region" /></p>
<p>These views are also available through the <a href="/api/resources/radar/subresources/origins/"><code>Origins</code> API</a>, using the <code>timeseries_groups</code> endpoint with the <code>ORIGIN</code>, <code>REGION</code>, or <code>PERCENTILE</code> dimension.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-30">Apr 30, 2026</time><div>
<h2 id="post-2026-04-30-radar-dark-mode"><a href="/changelog/post/2026-04-30-radar-dark-mode/">Dark mode support on Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now supports <strong>dark mode</strong>. A theme selector in the upper right corner of the page lets users explicitly choose between three display options:</p>
<ul>
<li><strong>Light</strong> — standard light theme</li>
<li><strong>Dark</strong> — full dark theme</li>
<li><strong>System</strong> — follows the operating system preference</li>
</ul>
<p><img src="/assets/upstream/images/radar/dark-mode-theme-selector.png" alt="Screenshot of the theme selector showing Light, Dark, and System options" /></p>
<p>The selected theme applies consistently across all Radar pages and widgets.</p>
<p><img src="/assets/upstream/images/radar/dark-mode-overview.png" alt="Screenshot of the Cloudflare Radar overview page in dark mode" /></p>
<p>The theme choice also applies to shared and embedded graphs.</p>
<p>Try it out at <a href="https://radar.cloudflare.com">Cloudflare Radar</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-30">Apr 30, 2026</time><div>
<h2 id="post-2026-04-30-cloudflare-python-v5.0.0"><a href="/changelog/post/2026-04-30-cloudflare-python-v5.0.0/">Cloudflare Python SDK v5.0.0 Released</a></h2>
<div class="changelog-badges"><span>sdk</span></div><div class="changelog-body"><p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-python/compare/v4.3.1...v5.0.0">v4.3.1...v5.0.0</a></p>
<p>This is a major release of the Cloudflare Python SDK. It drops support for Python 3.8, adds 11 new API services, introduces optional aiohttp backend support for improved async concurrency, and includes hundreds of type and method updates across the entire API surface.</p>
<p><strong>Please review the breaking changes below before upgrading.</strong> A migration guide is available at <a href="https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md">v5.0.0 Migration Guide</a>.</p>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-breaking-changes">Breaking Changes</h4>
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
<h4 id="2026-04-30-cloudflare-python-v5.0.0-features">Features</h4>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-aiohttp-backend-support">aiohttp Backend Support</h4>
<p>The async client now supports an optional <code>aiohttp</code> HTTP backend for improved concurrency performance. Install with <code>pip install cloudflare[aiohttp]</code> and use <code>DefaultAioHttpClient()</code> as the <code>http_client</code> parameter.</p>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-python-3-13-and-3-14-support">Python 3.13 and 3.14 Support</h4>
<p>Python 3.13 and 3.14 are now tested and supported.</p>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-new-services">New Services</h4>
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
<h4 id="2026-04-30-cloudflare-python-v5.0.0-new-endpoints-on-existing-services">New Endpoints on Existing Services</h4>
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
<h4 id="2026-04-30-cloudflare-python-v5.0.0-bug-fixes">Bug Fixes</h4>
<ul>
<li>Fixed <code>polymorphic_serialization</code> parameter in <code>model_dump</code> overrides</li>
<li>Added <code>BaseModel</code> base to response <code>SchemaFieldStruct</code>/<code>SchemaFieldList</code> stubs in Pipelines</li>
<li>Added missing <code>model_rebuild</code>/<code>update_forward_refs</code> for <code>SharedEntryCustomEntry</code> classes in DLP</li>
<li>Made <code>RunQueryParametersNeedleValue</code> a <code>BaseModel</code> with <code>arbitrary_types_allowed</code> in Workers</li>
<li>Removed duplicate <code>notification_url</code> field in webhook response types for Stream</li>
<li>Resolved pre-existing codegen type errors</li>
<li>Fixed <code>type: ignore[call-arg]</code> placement for mypy compatibility in Radar</li>
</ul>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-deprecations">Deprecations</h4>
<p>Resources with <code>@deprecated</code> annotations on some methods include: <code>accounts</code>, <code>addressing</code>, <code>ai-gateway</code>, <code>aisearch</code>, <code>api-gateway</code>, <code>billing</code>, <code>cloudforce-one</code>, <code>dns</code>, <code>email-routing</code>, <code>email-security</code>, <code>filters</code>, <code>firewall</code>, <code>images</code>, <code>intel</code>, <code>kv</code>, <code>logpush</code>, <code>origin-tls-client-auth</code>, <code>pages</code>, <code>pipelines</code>, <code>radar</code>, <code>rate-limits</code>, <code>registrar</code>, <code>rulesets</code>, <code>ssl</code>, <code>user</code>, <code>workers</code>, <code>workers-for-platforms</code>, <code>zero-trust</code>, <code>zones</code></p>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-python/releases/tag/v5.0.0">Download Python SDK v5.0.0</a></li>
<li><a href="https://developers.cloudflare.com/api/sdks/python/">Python SDK documentation</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md">Migration Guide</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-30">Apr 30, 2026</time><div>
<h2 id="post-2026-04-30-cloudflare-typescript-v6.0.0"><a href="/changelog/post/2026-04-30-cloudflare-typescript-v6.0.0/">Cloudflare TypeScript SDK v6.0.0 Released</a></h2>
<div class="changelog-badges"><span>sdk</span></div><div class="changelog-body"><p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-typescript/compare/v6.0.0-beta.2...v6.0.0">v6.0.0-beta.2...v6.0.0</a></p>
<p>This is a major version release of the Cloudflare TypeScript SDK. It includes 11 entirely new top-level API resources, new sub-resources and methods across 50+ existing resources, SDK infrastructure improvements, and breaking changes to the generated API surface from the v5.x line.</p>
<p><strong>Please ensure you read through the list of changes below before moving to this version</strong> - this will help you understand any down or upstream issues it may cause to your environments.</p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-breaking-changes">Breaking Changes</h4>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-sdk-infrastructure">SDK Infrastructure</h4>
<ul>
<li><strong>Retry-After handling changed</strong>: The SDK now respects any server-specified <code>Retry-After</code> value for rate-limited requests. Previously, values over 60 seconds were ignored and a default backoff was used instead.</li>
<li><strong>Empty response handling</strong>: Responses with <code>content-length: 0</code> now return <code>undefined</code> instead of attempting to parse the body.</li>
<li><strong>Environment variable reading</strong>: Empty string env vars (for example, <code>CLOUDFLARE_API_TOKEN=&quot;&quot;</code>) are now treated as unset.</li>
<li><strong>Path query parameter merging</strong>: URL search params embedded in endpoint paths are now extracted and merged into the query object.</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-removed-endpoints-17">Removed Endpoints (17)</h4>
<p>17 HTTP endpoints were removed from the SDK, affecting <code>abuse-reports</code>, <code>cloudforce-one</code>, <code>dlp/profiles/predefined</code>, <code>email-security/investigate</code>, <code>email-security/settings</code>, and <code>intel/ip-list</code>.</p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-method-signature-changes">Method Signature Changes</h4>
<ul>
<li><code>client.ai.toMarkdown.transform(file, \{ ...params \})</code> -&gt; <code>client.ai.toMarkdown.transform(\{ ...params \})</code> -- <code>file</code> moved from positional arg into params body</li>
<li><code>client.radar.ai.toMarkdown.create(body, \{ ...params \})</code> -&gt; <code>client.radar.ai.toMarkdown.create(\{ ...params \})</code> -- <code>body</code> moved from positional arg into params</li>
<li><code>client.abuseReports.create(reportType, \{ ...params \})</code> -&gt; <code>client.abuseReports.create(reportParam, \{ ...params \})</code> -- positional arg renamed</li>
<li><code>client.iam.userGroups.members.create(userGroupId, [ ...body ])</code> -&gt; <code>client.iam.userGroups.members.create(userGroupId, [ ...members ])</code> -- body array param renamed</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-renamed-client-paths">Renamed Client Paths</h4>
<ul>
<li><code>client.originTLSClientAuth.hostnames.certificates</code> -&gt; <code>client.originTLSClientAuth.zoneCertificates</code></li>
<li><code>client.radar.netflows</code> -&gt; <code>client.radar.netFlows</code> (casing change)</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-return-type-changes-179">Return Type Changes (179)</h4>
<ul>
<li><strong>133 methods now return <code>null</code></strong> instead of a typed response object. This primarily affects delete operations across <code>accounts</code>, <code>cache</code>, <code>d1</code>, <code>filters</code>, <code>firewall</code>, <code>hyperdrive</code>, <code>iam</code>, <code>kv</code>, <code>logpush</code>, <code>logs</code>, <code>r2</code>, <code>stream</code>, <code>workers</code>, <code>zero-trust</code>, <code>zones</code>, and others.</li>
<li><strong>17 methods changed pagination type</strong> (for example, <code>KeysCursorPaginationAfter</code> -&gt; <code>KeysCursorLimitPagination</code>).</li>
<li><strong>29 methods changed to a different named type</strong> (for example, <code>CloudflaredCreateResponse</code> -&gt; <code>CloudflareTunnel</code>).</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-removed-types-43">Removed Types (43)</h4>
<p>24 shared types removed from root namespace (<code>ASN</code>, <code>AuditLog</code>, <code>Member</code>, <code>Permission</code>, <code>Role</code>, <code>Subscription</code>, <code>Token</code>, etc.). 19 response types consolidated or renamed.</p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-resource-restructuring">Resource Restructuring</h4>
<p>19 resources were restructured from single files to directories. Public API client paths are unchanged, but deep imports may break.</p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-new-top-level-resources">New Top-Level Resources</h4>
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
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-new-sub-resources-on-existing-resources">New Sub-Resources on Existing Resources</h4>
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
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-bug-fixes">Bug Fixes</h4>
<ul>
<li>Resolved type errors from codegen overwriting manual fixes</li>
<li>Fixed <code>post()</code> usage for to-markdown endpoints to resolve async type error</li>
<li>Added least-privilege permissions to all workflow jobs</li>
<li>Reverted erroneous removal of rulesets resource methods and types</li>
<li>Resolved prettier formatting errors in codegen output</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-deprecations">Deprecations</h4>
<p>The following resources now include <code>@deprecated</code> annotations on some methods:</p>
<p><code>accounts</code>, <code>addressing</code>, <code>ai-gateway</code>, <code>aisearch</code>, <code>api-gateway</code>, <code>billing</code>, <code>cloudforce-one</code>, <code>custom-nameservers</code>, <code>dns</code>, <code>email-routing</code>, <code>email-security</code>, <code>filters</code>, <code>firewall</code>, <code>images</code>, <code>intel</code>, <code>keyless-certificates</code>, <code>kv</code>, <code>logpush</code>, <code>origin-tls-client-auth</code>, <code>page-shield</code>, <code>pages</code>, <code>pipelines</code>, <code>radar</code>, <code>rate-limits</code>, <code>registrar</code>, <code>rulesets</code>, <code>ssl</code>, <code>user</code>, <code>workers</code>, <code>workers-for-platforms</code>, <code>zero-trust</code>, <code>zones</code></p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-typescript/releases/tag/v6.0.0">Download TypeScript SDK v6.0.0</a></li>
<li><a href="https://developers.cloudflare.com/api/sdks/typescript/">TypeScript SDK documentation</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-typescript/blob/main/CHANGELOG.md">Full Changelog</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-30">Apr 30, 2026</time><div>
<h2 id="post-2026-04-30-shared-dictionaries-passthrough-beta"><a href="/changelog/post/2026-04-30-shared-dictionaries-passthrough-beta/">Shared dictionaries passthrough now in open beta</a></h2>
<div class="changelog-badges"><span>speed</span></div><div class="changelog-body"><p><a href="/speed/optimization/content/shared-dictionaries/">Shared dictionaries</a> (<a href="https://www.rfc-editor.org/rfc/rfc9842.html">RFC 9842</a>) let an origin compress a response against a previous version of the same resource that the browser already has cached, so only the difference between versions travels over the wire. Shared dictionaries passthrough is now in open beta on all plans.</p>
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
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/15/">Previous</a><span>Page 16 of 50</span><a class="pagination-next" rel="next" href="/changelog/17/">Next</a></nav>
</div>
