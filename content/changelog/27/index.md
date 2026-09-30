---
cp9:
  canonical: https://developers.cloudflare.com/changelog/27/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 27 | Cloudflare Docs
  head_html: <title>Changelog - page 27 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/27/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 27"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/27/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/27/#page","headline":"Changelog - page 27 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/27/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/27/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-01-27">Jan 27, 2026</time><div>
<h2 id="post-2026-01-27-configure-cloudflare-source-ips"><a href="/changelog/post/2026-01-27-configure-cloudflare-source-ips/">Configure Cloudflare source IPs (beta)</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>Cloudflare source IPs are the IP addresses used by Cloudflare services (such as Load Balancing, Gateway, and Browser Isolation) when sending traffic to your private networks.</p>
<p>For customers using legacy mode routing, traffic to private networks is sourced from public Cloudflare IPs, which may cause IP conflicts. For customers using Unified Routing mode (beta), traffic to private networks is sourced from dedicated, non-Internet-routable private IPv4 range to ensure:</p>
<ul>
<li>Symmetric routing over private network connections</li>
<li>Proper firewall state preservation</li>
<li>Private traffic stays on secure paths</li>
</ul>
<p>Key details:</p>
<ul>
<li><strong>IPv4</strong>: Sourced from <code>100.64.0.0/12</code> by default, configurable to any <code>/12</code> CIDR</li>
<li><strong>IPv6</strong>: Sourced from <code>2606:4700:cf1:5000::/64</code> (not configurable)</li>
<li><strong>Affected connectors</strong>: GRE, IPsec, CNI, WARP Connector, and WARP Client (Cloudflare Tunnel is not affected)</li>
</ul>
<p>Configuring Cloudflare source IPs requires Unified Routing (beta) and the <code>Cloudflare One Networks Write</code> permission.</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/">Configure Cloudflare source IPs</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-27">Jan 27, 2026</time><div>
<h2 id="post-2026-01-27-timezone-preferences"><a href="/changelog/post/2026-01-27-timezone-preferences/">Added Timezone preferences settings</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>You can now set the timezone in the Cloudflare dashboard as Coordinated Universal Time (UTC) or your browser or system's timezone.</p>
<h4 id="2026-01-27-timezone-preferences-what-s-new">What's New</h4>
<p>Unless otherwise specified in the user interface, all dates and times in the Cloudflare dashboard are now displayed in the selected timezone.</p>
<p>You can change the timezone setting from the user profile dropdown.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-01-27-set-timezone.png" alt="Timezone preference dropdown" /></p>
<p>The page will reload to apply the new timezone setting.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-27">Jan 27, 2026</time><div>
<h2 id="post-2026-01-27-body-buffering-settings"><a href="/changelog/post/2026-01-27-body-buffering-settings/">Control request and response body buffering in Configuration Rules</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>You can now control how Cloudflare buffers HTTP request and response bodies using two new settings in <a href="/rules/configuration-rules/">Configuration Rules</a>.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-26">Jan 26, 2026</time><div>
<h2 id="post-2026-01-26-waf-release"><a href="/changelog/post/2026-01-26-waf-release/">WAF Release - 2026-01-26</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s release introduces new detections for denial-of-service attempts targeting React CVE-2026-23864 (<a href="https://www.cve.org/CVERecord?id=CVE-2026-23864">https://www.cve.org/CVERecord?id=CVE-2026-23864</a>).</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-23864 (<a href="https://www.cve.org/CVERecord?id=CVE-2026-23864">https://www.cve.org/CVERecord?id=CVE-2026-23864</a>) affects <code>react-server-dom-parcel</code>, <code>react-server-dom-turbopack</code>, and <code>react-server-dom-webpack</code> packages.</li>
<li>Attackers can send crafted HTTP requests to Server Function endpoints, causing server crashes, out-of-memory exceptions, or excessive CPU usage.</li>
</ul>
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
        <code class="nb-rule-id" title="aaede80b4d414dc89c443cea61680354">61680354</code>
</td>
<td>N/A</td>
<td>React Server - DOS - CVE:CVE-2026-23864 - 1</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="3e93c9faaafa447c83a525f2dcdffcf8">dcdffcf8</code>
</td>
<td>N/A</td>
<td>React Server - DOS - CVE:CVE-2026-23864 - 2</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="930020d567684f19b05fb35b349edbc6">349edbc6</code>
</td>
<td>N/A</td>
<td>React Server - DOS - CVE:CVE-2026-23864 - 3</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-23">Jan 23, 2026</time><div>
<h2 id="post-2026-01-23-New-2FA-Experience"><a href="/changelog/post/2026-01-23-New-2FA-Experience/">New 2FA Experience for Login</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/changelog/fundamentals/2026-01-23-2fa-interstitial.png" alt="Screenshot of new 2FA enrollment experience" /></p>
<p>In an effort to improve overall user security, users without 2FA will be prompted upon login to enroll in email 2FA. This will improve user security posture while minimizing friction. Users without email 2FA enabled will see a prompt to secure their account with additional factors upon logging in. Enrolling in 2FA remains optional, but strongly encouraged as it is the best way to prevent account takeovers.</p>
<p>We also made changes to existing 2FA screens to improve the user experience. Now we have distinct experiences for each 2FA factor type, reflective of the way that factor works.</p>
<h4 id="2026-01-23-New-2FA-Experience-for-more-information">For more information</h4>
* [Configure Email Two Factor Authentication](/fundamentals/user-profiles/2fa/#configure-email-two-factor-authentication)
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-23">Jan 23, 2026</time><div>
<h2 id="post-2026-01-23-pages-file-limit-increase"><a href="/changelog/post/2026-01-23-pages-file-limit-increase/">Increased Pages file limit to 100,000 for paid plans</a></h2>
<div class="changelog-badges"><span>pages</span></div><div class="changelog-body"><p>Paid plans can now have up to 100,000 files per Pages site, increased from the previous limit of 20,000 files.</p>
<p>To enable this increased limit, set the environment variable <code>PAGES_WRANGLER_MAJOR_VERSION=4</code> in your Pages project settings.</p>
<p>The Free plan remains at 20,000 files per site.</p>
<p>For more details, refer to the <a href="/pages/platform/limits/#files">Pages limits documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-23">Jan 23, 2026</time><div>
<h2 id="post-2026-01-23-increased-index-capacity"><a href="/changelog/post/2026-01-23-increased-index-capacity/">Vectorize indexes now support up to 10 million vectors</a></h2>
<div class="changelog-badges"><span>vectorize</span></div><div class="changelog-body"><p>You can now store up to 10 million vectors in a single Vectorize index, doubling the previous limit of 5 million vectors. This enables larger-scale semantic search, recommendation systems, and retrieval-augmented generation (RAG) applications without splitting data across multiple indexes.</p>
<p>Vectorize continues to support indexes with up to 1,536 dimensions per vector at 32-bit precision. Refer to the <a href="/vectorize/platform/limits/">Vectorize limits documentation</a> for complete details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-22">Jan 22, 2026</time><div>
<h2 id="post-2026-01-22-deny-by-default-for-zones"><a href="/changelog/post/2026-01-22-deny-by-default-for-zones/">Require Access protection for zones</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>access</span></div><div class="changelog-body"><p>You can now require Cloudflare Access protection for all hostnames in your account. When enabled, traffic to any hostname that does not have a matching Access application is automatically blocked.</p>
<p>This deny-by-default approach prevents accidental exposure of internal resources to the public Internet. If a developer deploys a new application or creates a DNS record without configuring an Access application, the traffic is blocked rather than exposed.</p>
<p><img src="/assets/upstream/images/changelog/access/require-cloudflare-access-protection.png" alt="Require Cloudflare Access protection in the dashboard" /></p>
<h4 id="2026-01-22-deny-by-default-for-zones-how-it-works">How it works</h4>
<ul>
<li><strong>Blocked by default</strong>: Traffic to all hostnames in the account is blocked unless an Access application exists for that hostname.</li>
<li><strong>Explicit access required</strong>: To allow traffic, create an Access application with an Allow or Bypass policy.</li>
<li><strong>Hostname exemptions</strong>: You can exempt specific hostnames from this requirement.</li>
</ul>
<p>To turn on this feature, refer to <a href="/cloudflare-one/access-controls/access-settings/require-access-protection/">Require Access protection</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-22">Jan 22, 2026</time><div>
<h2 id="post-2026-01-22-granular-api-token-permissions"><a href="/changelog/post/2026-01-22-granular-api-token-permissions/">New granular API token permissions for Cloudflare Access</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Three new API token permissions are available for Cloudflare Access, giving you finer-grained control when building automations and integrations:</p>
<ul>
<li><strong>Access: Organizations Revoke</strong> — Grants the ability to <a href="/cloudflare-one/access-controls/access-settings/session-management/#revoke-user-sessions">revoke user sessions</a> in a Zero Trust organization. Use this permission when you need a token that can terminate active sessions without broader write access to organization settings.</li>
<li><strong>Access: Population Read</strong> — Grants read access to the <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM users and groups</a> synced from an identity provider to Cloudflare Access. Use this permission for tokens that only need to read synced user and group data.</li>
<li><strong>Access: Population Write</strong> — Grants write access to the <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM users and groups</a> synced from an identity provider to Cloudflare Access. Use this permission for tokens that need to create or modify synced user and group data.</li>
</ul>
<p>These permissions are scoped at the account level and can be combined with existing Access permissions.</p>
<p>For a full list of available permissions, refer to <a href="/fundamentals/api/reference/permissions/">API token permissions</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-22">Jan 22, 2026</time><div>
<h2 id="post-2026-01-22-sha256-base64-encode-functions"><a href="/changelog/post/2026-01-22-sha256-base64-encode-functions/">New cryptographic functions — encode_base64() and sha256()</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>Cloudflare Rulesets now includes <code>encode_base64()</code> and <code>sha256()</code> functions, enabling you to generate signed request headers directly in rule expressions. These functions support common patterns like constructing a canonical string from request attributes, computing a SHA256 digest, and Base64-encoding the result.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-22">Jan 22, 2026</time><div>
<h2 id="post-2026-01-22-explicit-placement-hints"><a href="/changelog/post/2026-01-22-explicit-placement-hints/">New Placement Hints for Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now configure Workers to run close to infrastructure in legacy cloud regions to minimize latency to existing services and databases. This is most useful when your Worker makes multiple round trips.</p>
<p>To <a href="/workers/configuration/placement/#configure-explicit-placement-hints">set a placement hint</a>, set the <code>placement.region</code> property in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17793.md")</div>
<p>Placement hints support Amazon Web Services (AWS), Google Cloud Platform (GCP), and Microsoft Azure region identifiers. Workers run in the <a href="https://www.cloudflare.com/network/">Cloudflare data center</a> with the lowest latency to the specified cloud region.</p>
<p>If your existing infrastructure is not in these cloud providers, expose it to placement probes with <code>placement.host</code> for layer 4 checks or <code>placement.hostname</code> for layer 7 checks. These probes are designed to locate single-homed infrastructure and are not suitable for anycasted or multicasted resources.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17794.md")</div>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17795.md")</div>
<p>This is an extension of <a href="/workers/configuration/placement/#enable-smart-placement">Smart Placement</a>, which automatically places your Workers closer to back-end APIs based on measured latency. When you do not know the location of your back-end APIs or have multiple back-end APIs, set <code>mode: &quot;smart&quot;</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17796.md")</div>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-20">Jan 20, 2026</time><div>
<h2 id="post-2026-01-20-ai-search-path-filtering"><a href="/changelog/post/2026-01-20-ai-search-path-filtering/">AI Search path filtering for website and R2 data sources</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now includes <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a> for both <a href="/ai-search/configuration/data-source/website/#path-filtering">website</a> and <a href="/ai-search/configuration/data-source/r2/#path-filtering">R2</a> data sources. You can now control which content gets indexed by defining include and exclude rules for paths.</p>
<p>By controlling what gets indexed, you can improve the relevance and quality of your search results. You can also use path filtering to split a single data source across multiple AI Search instances for specialized search experiences.</p>
<p><img src="/assets/upstream/images/ai-search/path-filtering.png" alt="Path filtering configuration in AI Search" /></p>
<p>Path filtering uses <a href="https://github.com/micromatch/micromatch">micromatch</a> patterns, so you can use <code>*</code> to match within a directory and <code>**</code> to match across directories.</p>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Include</th>
<th>Exclude</th>
</tr>
</thead>
<tbody>
<tr>
<td>Index docs but skip drafts</td>
<td><code>**/docs/**</code></td>
<td><code>**/docs/drafts/**</code></td>
</tr>
<tr>
<td>Keep admin pages out of results</td>
<td>—</td>
<td><code>**/admin/**</code></td>
</tr>
<tr>
<td>Index only English content</td>
<td><code>**/en/**</code></td>
<td>—</td>
</tr>
</tbody>
</table>
<p>Configure path filters when creating a new instance or update them anytime from <strong>Settings</strong>. Check out <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a> to learn more.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-20">Jan 20, 2026</time><div>
<h2 id="post-2026-01-20-ai-search-simplified-api"><a href="/changelog/post/2026-01-20-ai-search-simplified-api/">Create AI Search instances programmatically via REST API</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>You can now create <a href="/ai-search/">AI Search</a> instances programmatically using the <a href="/ai-search/get-started/api/">API</a>. For example, use the API to create instances for each customer in a multi-tenant application or manage AI Search alongside your other infrastructure.</p>
<p>If you have created an AI Search instance via the <a href="/ai-search/get-started/dashboard/">dashboard</a> before, you already have a <a href="/ai-search/configuration/indexing/service-api-token/">service API token</a> registered and can start creating instances programmatically right away. If not, follow the <a href="/ai-search/get-started/api/">API guide</a> to set up your first instance.</p>
<p>For example, you can now create separate search instances for each language on your website:</p>
<pre tabindex="0"><code class="language-bash">for lang in en fr es de; do&#10;  curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/instances&quot; \&#10;    &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;    &#45;H &quot;Content-Type: application/json&quot; \&#10;    &#45;-data &#x27;{&#10;      &quot;id&quot;: &quot;docs-&#x27;&quot;$lang&quot;&#x27;&quot;,&#10;      &quot;type&quot;: &quot;web-crawler&quot;,&#10;      &quot;source&quot;: &quot;example.com&quot;,&#10;      &quot;source_params&quot;: {&#10;        &quot;path_include&quot;: [&quot;**/&#x27;&quot;$lang&quot;&#x27;/**&quot;]&#10;      }&#10;    }&#x27;&#10;done&#10;</code></pre>
<p>Refer to the <a href="/api/resources/ai_search/subresources/instances/methods/create/">REST API reference</a> for additional configuration options.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-20">Jan 20, 2026</time><div>
<h2 id="post-2026-01-20-kv-dash-ui-homepage"><a href="/changelog/post/2026-01-20-kv-dash-ui-homepage/">New Workers KV Dashboard UI</a></h2>
<div class="changelog-badges"><span>kv</span></div><div class="changelog-body"><p><a href="/kv/">Workers KV</a> has an updated dashboard UI with new dashboard styling that makes it easier to navigate and see analytics and settings for a KV namespace.</p>
<p>The new dashboard features a <strong>streamlined homepage</strong> for easy access to your namespaces and key operations, with consistent design with the rest of the dashboard UI updates. It also provides an <strong>improved analytics view</strong>.</p>
<p><img src="/assets/upstream/images/changelog/kv/kv-dash-ui-homepage.png" alt="New KV Dashboard Homepage" /></p>
<p>The updated dashboard is now available for all Workers KV users. Log in to the <a href="https://dash.cloudflare.com/">Cloudflare Dashboard</a> to start exploring the new interface.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-20">Jan 20, 2026</time><div>
<h2 id="post-2026-01-20-array-map-functions"><a href="/changelog/post/2026-01-20-array-map-functions/">New functions for array and map operations</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><h4 id="2026-01-20-array-map-functions-new-functions-for-array-and-map-operations">New functions for array and map operations</h4>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-20">Jan 20, 2026</time><div>
<h2 id="post-2026-01-20-cloudflare-typescript-v6.0.0-beta.1"><a href="/changelog/post/2026-01-20-cloudflare-typescript-v6.0.0-beta.1/">Cloudflare Typescript SDK v6.0.0-beta.1 now available</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>sdk</span></div><div class="changelog-body"><blockquote>
<p><strong>Disclaimer:</strong> Please note that v6.0.0-beta.1 is in Beta and we are still testing it for stability.</p>
</blockquote>
<p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-typescript/compare/v5.2.0...v6.0.0-beta.1">v5.2.0...v6.0.0-beta.1</a></p>
<p>In this release, you'll see a large number of breaking changes. This is primarily due to a change in OpenAPI definitions, which our libraries are based off of, and codegen updates that we rely on to read those OpenAPI definitions and produce our SDK libraries. As the codegen is always evolving and improving, so are our code bases.</p>
<p>Some breaking changes were introduced due to bug fixes, also listed below.</p>
<p>Please ensure you read through the list of changes below before moving to this version - this will help you understand any down or upstream issues it may cause to your environments.</p>
<hr />
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-breaking-changes">Breaking Changes</h4>
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-addressing-parameter-requirements-changed">Addressing - Parameter Requirements Changed</h4>
- `BGPPrefixCreateParams.cidr`: optional → **required**
- `PrefixCreateParams.asn`: `number | null` → `number`
- `PrefixCreateParams.loa_document_id`: required → **optional**
- `ServiceBindingCreateParams.cidr`: optional → **required**
- `ServiceBindingCreateParams.service_id`: optional → **required**
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-api-gateway">API Gateway</h4>
- `ConfigurationUpdateResponse` removed
- `PublicSchema` → `OldPublicSchema`
- `SchemaUpload` → `UserSchemaCreateResponse`
- `ConfigurationUpdateParams.properties` removed; use `normalize`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-cloudforceone-response-type-changes">CloudforceOne - Response Type Changes</h4>
- `ThreatEventBulkCreateResponse`: `number` → complex object with counts and errors
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-d1-database-query-parameters">D1 Database - Query Parameters</h4>
- `DatabaseQueryParams`: simple interface → union type (`D1SingleQuery | MultipleQueries`)
- `DatabaseRawParams`: same change
- Supports batch queries via `batch` array
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-dns-records-type-renames-21-types">DNS Records - Type Renames (21 types)</h4>
All record type interfaces renamed from `*Record` to short names:
- `RecordResponse.ARecord` → `RecordResponse.A`
- `RecordResponse.AAAARecord` → `RecordResponse.AAAA`
- `RecordResponse.CNAMERecord` → `RecordResponse.CNAME`
- `RecordResponse.MXRecord` → `RecordResponse.MX`
- `RecordResponse.NSRecord` → `RecordResponse.NS`
- `RecordResponse.PTRRecord` → `RecordResponse.PTR`
- `RecordResponse.TXTRecord` → `RecordResponse.TXT`
- `RecordResponse.CAARecord` → `RecordResponse.CAA`
- `RecordResponse.CERTRecord` → `RecordResponse.CERT`
- `RecordResponse.DNSKEYRecord` → `RecordResponse.DNSKEY`
- `RecordResponse.DSRecord` → `RecordResponse.DS`
- `RecordResponse.HTTPSRecord` → `RecordResponse.HTTPS`
- `RecordResponse.LOCRecord` → `RecordResponse.LOC`
- `RecordResponse.NAPTRRecord` → `RecordResponse.NAPTR`
- `RecordResponse.SMIMEARecord` → `RecordResponse.SMIMEA`
- `RecordResponse.SRVRecord` → `RecordResponse.SRV`
- `RecordResponse.SSHFPRecord` → `RecordResponse.SSHFP`
- `RecordResponse.SVCBRecord` → `RecordResponse.SVCB`
- `RecordResponse.TLSARecord` → `RecordResponse.TLSA`
- `RecordResponse.URIRecord` → `RecordResponse.URI`
- `RecordResponse.OpenpgpkeyRecord` → `RecordResponse.Openpgpkey`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-iam-resource-groups">IAM Resource Groups</h4>
- `ResourceGroupCreateResponse.scope`: optional single → **required array**
- `ResourceGroupCreateResponse.id`: optional → **required**
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-origin-ca-certificates-parameter-requirements-changed">Origin CA Certificates - Parameter Requirements Changed</h4>
- `OriginCACertificateCreateParams.csr`: optional → **required**
- `OriginCACertificateCreateParams.hostnames`: optional → **required**
- `OriginCACertificateCreateParams.request_type`: optional → **required**
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-pages">Pages</h4>
- Renamed: `DeploymentsSinglePage` → `DeploymentListResponsesV4PagePaginationArray`
- Domain response fields: many optional → **required**
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-pipelines-v0-to-v1-migration">Pipelines - v0 to v1 Migration</h4>
- Entire v0 API deprecated; use v1 methods (`createV1`, `listV1`, etc.)
- New sub-resources: `Sinks`, `Streams`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-r2">R2</h4>
- `EventNotificationUpdateParams.rules`: optional → **required**
- Super Slurper: `bucket`, `secret` now required in source params
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-radar">Radar</h4>
- `dataSource`: `string` → typed enum (23 values)
- `eventType`: `string` → typed enum (6 values)
- V2 methods require `dimension` parameter (breaking signature change)
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-resource-sharing">Resource Sharing</h4>
- Removed: `status_message` field from all recipient response types
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-schema-validation">Schema Validation</h4>
- Consolidated `SchemaCreateResponse`, `SchemaListResponse`, `SchemaEditResponse`, `SchemaGetResponse` → `PublicSchema`
- Renamed: `SchemaListResponsesV4PagePaginationArray` → `PublicSchemasV4PagePaginationArray`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-spectrum">Spectrum</h4>
- Renamed union members: `AppListResponse.UnionMember0` → `SpectrumConfigAppConfig`
- Renamed union members: `AppListResponse.UnionMember1` → `SpectrumConfigPaygoAppConfig`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-workers">Workers</h4>
- Removed: `WorkersBindingKindTailConsumer` type (all occurrences)
- Renamed: `ScriptsSinglePage` → `ScriptListResponsesSinglePage`
- Removed: `DeploymentsSinglePage`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-dlp">Zero-Trust DLP</h4>
- `datasets.create()`, `update()`, `get()` return types changed
- `PredefinedGetResponse` union members renamed to `UnionMember0-5`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-tunnels">Zero-Trust Tunnels</h4>
- Removed: `CloudflaredCreateResponse`, `CloudflaredListResponse`, `CloudflaredDeleteResponse`, `CloudflaredEditResponse`, `CloudflaredGetResponse`
- Removed: `CloudflaredListResponsesV4PagePaginationArray`
<hr />
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-features">Features</h4>
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-abuse-reports-client-abusereports">Abuse Reports (<code>client.abuseReports</code>)</h4>
- **Reports**: `create`, `list`, `get`
- **Mitigations**: sub-resource for abuse mitigations
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-ai-search-client-aisearch">AI Search (<code>client.aisearch</code>)</h4>
- **Instances**: `create`, `update`, `list`, `delete`, `read`, `stats`
- **Items**: `list`, `get`
- **Jobs**: `create`, `list`, `get`, `logs`
- **Tokens**: `create`, `update`, `list`, `delete`, `read`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-connectivity-client-connectivity">Connectivity (<code>client.connectivity</code>)</h4>
- **Directory Services**: `create`, `update`, `list`, `delete`, `get`
- Supports IPv4, IPv6, dual-stack, and hostname configurations
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-organizations-client-organizations">Organizations (<code>client.organizations</code>)</h4>
- **Organizations**: `create`, `update`, `list`, `delete`, `get`
- **OrganizationProfile**: `update`, `get`
- Hierarchical organization support with parent/child relationships
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-r2-data-catalog-client-r2datacatalog">R2 Data Catalog (<code>client.r2DataCatalog</code>)</h4>
- **Catalog**: `list`, `enable`, `disable`, `get`
- **Credentials**: `create`
- **MaintenanceConfigs**: `update`, `get`
- **Namespaces**: `list`
- **Tables**: `list`, maintenance config management
- Apache Iceberg integration
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-realtime-kit-client-realtimekit">Realtime Kit (<code>client.realtimeKit</code>)</h4>
- **Apps**: `get`, `post`
- **Meetings**: `create`, `get`, participant management
- **Livestreams**: 10+ methods for streaming
- **Recordings**: start, pause, stop, get
- **Sessions**: transcripts, summaries, chat
- **Webhooks**: full CRUD
- **ActiveSession**: polls, kick participants
- **Analytics**: organization analytics
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-token-validation-client-tokenvalidation">Token Validation (<code>client.tokenValidation</code>)</h4>
- **Configuration**: `create`, `list`, `delete`, `edit`, `get`
- **Credentials**: `update`
- **Rules**: `create`, `list`, `delete`, `bulkCreate`, `bulkEdit`, `edit`, `get`
- JWT validation with RS256/384/512, PS256/384/512, ES256, ES384
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-alerting-silences-client-alerting-silences">Alerting Silences (<code>client.alerting.silences</code>)</h4>
- `create`, `update`, `list`, `delete`, `get`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-iam-sso-client-iam-sso">IAM SSO (<code>client.iam.sso</code>)</h4>
- `create`, `update`, `list`, `delete`, `get`, `beginVerification`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-pipelines-v1-client-pipelines">Pipelines v1 (<code>client.pipelines</code>)</h4>
- **Sinks**: `create`, `list`, `delete`, `get`
- **Streams**: `create`, `update`, `list`, `delete`, `get`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-ai-controls-mcp-client-zerotrust-access-aicontrols-mcp">Zero-Trust AI Controls / MCP (<code>client.zeroTrust.access.aiControls.mcp</code>)</h4>
- **Portals**: `create`, `update`, `list`, `delete`, `read`
- **Servers**: `create`, `update`, `list`, `delete`, `read`, `sync`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-accounts">Accounts</h4>
- `managed_by` field with `parent_org_id`, `parent_org_name`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-addressing-loa-documents">Addressing LOA Documents</h4>
- `auto_generated` field on `LOADocumentCreateResponse`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-addressing-prefixes">Addressing Prefixes</h4>
- `delegate_loa_creation`, `irr_validation_state`, `ownership_validation_state`, `ownership_validation_token`, `rpki_validation_state`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-ai">AI</h4>
- Added `toMarkdown.supported()` method to get all supported conversion formats
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-ai-gateway">AI Gateway</h4>
- `zdr` field added to all responses and params
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-alerting">Alerting</h4>
- New alert type: `abuse_report_alert`
- `type` field added to PolicyFilter
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-browser-rendering">Browser Rendering</h4>
- `ContentCreateParams`: refined to discriminated union (`Variant0 | Variant1`)
- Split into URL-based and HTML-based parameter variants for better type safety
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-client-certificates">Client Certificates</h4>
- `reactivate` parameter in edit
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-cloudforceone">CloudforceOne</h4>
- `ThreatEventCreateParams.indicatorType`: required → optional
- `hasChildren` field added to all threat event response types
- `datasetIds` query parameter on `AttackerListParams`, `CategoryListParams`, `TargetIndustryListParams`
- `categoryUuid` field on `TagCreateResponse`
- `indicators` array for multi-indicator support per event
- `uuid` and `preserveUuid` fields for UUID preservation in bulk create
- `format` query parameter (`'json' | 'stix2'`) on `ThreatEventListParams`
- `createdAt`, `datasetId` fields on `ThreatEventEditParams`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-content-scanning">Content Scanning</h4>
- Added `create()`, `update()`, `get()` methods
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-custom-pages">Custom Pages</h4>
- New page types: `basic_challenge`, `under_attack`, `waf_challenge`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-d1">D1</h4>
- `served_by_colo` - colo that handled query
- `jurisdiction` - `'eu' | 'fedramp'`
- **Time Travel** (`client.d1.database.timeTravel`): `getBookmark()`, `restore()` - point-in-time recovery
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-email-security">Email Security</h4>
- New fields on `InvestigateListResponse`/`InvestigateGetResponse`: `envelope_from`, `envelope_to`, `postfix_id_outbound`, `replyto`
- New detection classification: `'outbound_ndr'`
- Enhanced `Finding` interface with `attachment`, `detection`, `field`, `portion`, `reason`, `score`
- Added `cursor` query parameter to `InvestigateListParams`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-gateway-lists">Gateway Lists</h4>
- New list types: `CATEGORY`, `LOCATION`, `DEVICE`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-intel">Intel</h4>
- New issue type: `'configuration_suggestion'`
- `payload` field: `unknown` → typed `Payload` interface with `detection_method`, `zone_tag`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-leaked-credential-checks">Leaked Credential Checks</h4>
- Added `detections.get()` method
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-logpush">Logpush</h4>
- New datasets: `dex_application_tests`, `dex_device_state_events`, `ipsec_logs`, `warp_config_changes`, `warp_toggle_changes`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-load-balancers">Load Balancers</h4>
- `Monitor.port`: `number` → `number | null`
- `Pool.load_shedding`: `LoadShedding` → `LoadShedding | null`
- `Pool.origin_steering`: `OriginSteering` → `OriginSteering | null`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-magic-transit">Magic Transit</h4>
- `license_key` field on connectors
- `provision_license` parameter for auto-provisioning
- IPSec: `custom_remote_identities` with FQDN support
- Snapshots: Bond interface, `probed_mtu` field
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-pages-1">Pages</h4>
- New response types: `ProjectCreateResponse`, `ProjectListResponse`, `ProjectEditResponse`, `ProjectGetResponse`
- Deployment methods return specific response types instead of generic `Deployment`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-queues">Queues</h4>
- Added `subscriptions.get()` method
- Enhanced `SubscriptionGetResponse` with typed event source interfaces
- New event source types: Images, KV, R2, Vectorize, Workers AI, Workers Builds, Workflows
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-r2-1">R2</h4>
- Sippy: new provider `s3` (S3-compatible endpoints)
- Sippy: `bucketUrl` field for S3-compatible sources
- Super Slurper: `keys` field on source response schemas (specify specific keys to migrate)
- Super Slurper: `pathPrefix` field on source schemas
- Super Slurper: `region` field on S3 source params
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-radar-1">Radar</h4>
- Added `geolocations.list()`, `geolocations.get()` methods
- Added V2 dimension-based methods (`summaryV2`, `timeseriesGroupsV2`) to radar sub-resources
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-resource-sharing-1">Resource Sharing</h4>
- Added `terminal` boolean field to Resource Error interfaces
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-rules">Rules</h4>
- Added `id` field to `ItemDeleteParams.Item`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-rulesets">Rulesets</h4>
- New buffering fields on `SetConfigRule`: `request_body_buffering`, `response_body_buffering`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-secrets-store">Secrets Store</h4>
- New scopes: `'dex'`, `'access'` (in addition to `'workers'`, `'ai_gateway'`)
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-ssl-certificate-packs">SSL Certificate Packs</h4>
- Response types now proper interfaces (was `unknown`)
- Fields now required: `id`, `certificates`, `hosts`, `status`, `type`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-security-center">Security Center</h4>
- `payload` field: `unknown` → typed `Payload` interface with `detection_method`, `zone_tag`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-shared-types">Shared Types</h4>
- Added: `CloudflareTunnelsV4PagePaginationArray` pagination class
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-workers-1">Workers</h4>
- Added `subdomains.delete()` method
- `Worker.references` - track external dependencies (domains, Durable Objects, queues)
- `Worker.startup_time_ms` - startup timing
- `Script.observability` - observability settings with logging
- `Script.tag`, `Script.tags` - immutable ID and tags
- Placement: support for region, hostname, host-based placement
- `tags`, `tail_consumers` now accept `| null`
- Telemetry: `traces` field, `$containers` event info, `durableObjectId`, `transactionName`, `abr_level` fields
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-workers-for-platforms">Workers for Platforms</h4>
- `ScriptUpdateResponse`: new fields `entry_point`, `observability`, `tag`, `tags`
- `placement` field now union of 4 variants (smart mode, region, hostname, host)
- `tags`, `tail_consumers` now nullable
- `TagUpdateParams.body` now accepts `null`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-workflows">Workflows</h4>
- `instance_retention`: `unknown` → typed `InstanceRetention` interface with `error_retention`, `success_retention`
- New status option: `'restart'` added to `StatusEditParams.status`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-devices">Zero-Trust Devices</h4>
- External emergency disconnect settings (4 new fields)
- `antivirus` device posture check type
- `os_version_extra` documentation improvements
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zones">Zones</h4>
- New response types: `SubscriptionCreateResponse`, `SubscriptionUpdateResponse`, `SubscriptionGetResponse`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-access-applications">Zero-Trust Access Applications</h4>
- New `ApplicationType` values: `'mcp'`, `'mcp_portal'`, `'proxy_endpoint'`
- New destination type: `ViaMcpServerPortalDestination` for MCP server access
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-gateway">Zero-Trust Gateway</h4>
- Added `rules.listTenant()` method
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-gateway-proxy-endpoints">Zero-Trust Gateway - Proxy Endpoints</h4>
- `ProxyEndpoint`: interface → discriminated union (`ZeroTrustGatewayProxyEndpointIP | ZeroTrustGatewayProxyEndpointIdentity`)
- `ProxyEndpointCreateParams`: interface → union type
- Added `kind` field: `'ip' | 'identity'`
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-zero-trust-tunnels-1">Zero-Trust Tunnels</h4>
- `WARPConnector*Response`: union type → interface
<hr />
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-deprecations">Deprecations</h4>
<ul>
<li><strong>API Gateway</strong>: <code>UserSchemas</code>, <code>Settings</code>, <code>SchemaValidation</code> resources</li>
<li><strong>Audit Logs</strong>: <code>auditLogId.not</code> (use <code>id.not</code>)</li>
<li><strong>CloudforceOne</strong>: <code>ThreatEvents.get()</code>, <code>IndicatorTypes.list()</code></li>
<li><strong>Devices</strong>: <code>public_ip</code> field (use DEX API)</li>
<li><strong>Email Security</strong>: <code>item_count</code> field in Move responses</li>
<li><strong>Pipelines</strong>: v0 methods (use v1)</li>
<li><strong>Radar</strong>: old <code>summary()</code> and <code>timeseriesGroups()</code> methods (use V2)</li>
<li><strong>Rulesets</strong>: <code>disable_apps</code>, <code>mirage</code> fields</li>
<li><strong>WARP Connector</strong>: <code>connections</code> field</li>
<li><strong>Workers</strong>: <code>environment</code> parameter in Domains</li>
<li><strong>Zones</strong>: <code>ResponseBuffering</code> page rule</li>
</ul>
<hr />
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>mcp:</strong> correct code tool API endpoint (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/599703c45672dc899455d74b124018efd4b75095">599703c</a>)</li>
<li><strong>mcp:</strong> return correct lines on typescript errors (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/5d6f9998ed9999aaa95e1bda8cf50929f3555cf1">5d6f999</a>)</li>
<li><strong>organization_profile:</strong> fix bad reference (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/d84ea77094400055c06554812b84c2f0c8d00cc4">d84ea77</a>)</li>
<li><strong>schema_validation:</strong> correctly reflect model to openapi mapping (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/bb861516774b159d80e0f46a5f3abc5a4c9f9d49">bb86151</a>)</li>
<li><strong>workers:</strong> fix tests (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/2ee37f7adf5a4637d65f61fc225e135eec2579fc">2ee37f7</a>)</li>
</ul>
<hr />
<h4 id="2026-01-20-cloudflare-typescript-v6.0.0-beta.1-documentation">Documentation</h4>
<ul>
<li>Added deprecation notices with migration paths</li>
<li><strong>api_gateway:</strong> deprecate API Shield Schema Validation resources (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/8a4b20f7a572422f74179fbdb4f1c4fb555e3e40">8a4b20f</a>)</li>
<li>Improved JSDoc examples across all resources</li>
<li><strong>workers:</strong> expose subdomain delete documentation (<a href="https://github.com/cloudflare/cloudflare-typescript/commit/4f7cc1f2b8861a5b8abc193d287f78264a425062">4f7cc1f</a>)</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-20">Jan 20, 2026</time><div>
<h2 id="post-2026-01-20-terraform-v5.16.0-provider"><a href="/changelog/post/2026-01-20-terraform-v5.16.0-provider/">Terraform v5.16.0 now available</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>In January 2025, we announced the launch of the new Terraform v5 Provider. We greatly appreciate the proactive engagement and valuable feedback from the Cloudflare community following the v5 release. In response, we've established a consistent and rapid <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 week cadence</a> for releasing targeted improvements, demonstrating our commitment to stability and reliability.</p>
<p>With the help of the community, we have a growing number of resources that we have marked as <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">stable</a>, with that list continuing to grow with every release. The most used <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">resources</a> are on track to be stable by the end of March 2026, when we will also be releasing a new migration tool to you migrate from v4 to v5 with ease.</p>
<p>Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.</p>
<p>This release includes bug fixes, the stabilization of even more popular resources, and more.</p>
<h4 id="2026-01-20-terraform-v5.16.0-provider-features">Features</h4>
<ul>
<li><strong>custom_pages:</strong> add &quot;waf_challenge&quot; as new supported error page type identifier in both resource and data source schemas</li>
<li><strong>list:</strong> enhance CIDR validator to check for normalized CIDR notation requiring network address for IPv4 and IPv6</li>
<li><strong>magic_wan_gre_tunnel:</strong> add automatic_return_routing attribute for automatic routing control</li>
<li><strong>magic_wan_gre_tunnel:</strong> add BGP configuration support with new BGP model attribute</li>
<li><strong>magic_wan_gre_tunnel:</strong> add bgp_status computed attribute for BGP connection status information</li>
<li><strong>magic_wan_gre_tunnel:</strong> enhance schema with BGP-related attributes and validators</li>
<li><strong>magic_wan_ipsec_tunnel:</strong> add automatic_return_routing attribute for automatic routing control</li>
<li><strong>magic_wan_ipsec_tunnel:</strong> add BGP configuration support with new BGP model attribute</li>
<li><strong>magic_wan_ipsec_tunnel:</strong> add bgp_status computed attribute for BGP connection status information</li>
<li><strong>magic_wan_ipsec_tunnel:</strong> add custom_remote_identities attribute for custom identity configuration</li>
<li><strong>magic_wan_ipsec_tunnel:</strong> enhance schema with BGP and identity-related attributes</li>
<li><strong>ruleset:</strong> add request body buffering support</li>
<li><strong>ruleset:</strong> enhance ruleset data source with additional configuration options</li>
<li><strong>workers_script:</strong> add observability logs attributes to list data source model</li>
<li><strong>workers_script:</strong> enhance list data source schema with additional configuration options</li>
</ul>
<h4 id="2026-01-20-terraform-v5.16.0-provider-bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>account_member</strong>: fix resource importability issues</li>
<li><strong>dns_record:</strong> remove unnecessary fmt.Sprintf wrapper around LoadTestCase call in test configuration helper function</li>
<li><strong>load_balancer:</strong> fix session_affinity_ttl type expectations to match Float64 in initial creation and Int64 after migration</li>
<li><strong>workers_kv:</strong> handle special characters correctly in URL encoding</li>
</ul>
<h4 id="2026-01-20-terraform-v5.16.0-provider-documentation">Documentation</h4>
<ul>
<li><strong>account_subscription:</strong> update schema description for rate_plan.sets attribute to clarify it returns an array of strings</li>
<li><strong>api_shield:</strong> add resource-level description for API Shield management of auth ID characteristics</li>
<li><strong>api_shield:</strong> enhance auth_id_characteristics.name attribute description to include JWT token configuration format requirements</li>
<li><strong>api_shield:</strong> specify JSONPath expression format for JWT claim locations</li>
<li><strong>hyperdrive_config:</strong> add description attribute to name attribute explaining its purpose in dashboard and API identification</li>
<li><strong>hyperdrive_config:</strong> apply description improvements across resource, data source, and list data source schemas</li>
<li><strong>hyperdrive_config:</strong> improve schema descriptions for cache settings to clarify default values</li>
<li><strong>hyperdrive_config:</strong> update port description to clarify defaults for different database types</li>
</ul>
<h4 id="2026-01-20-terraform-v5.16.0-provider-for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](/terraform/)
- [List of stabilized resources](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-20">Jan 20, 2026</time><div>
<h2 id="post-2026-01-20-waf-release"><a href="/changelog/post/2026-01-20-waf-release/">WAF Release - 2026-01-20</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release focuses on improvements to existing detections to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against SQL injection.</li>
</ul>
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
        <code class="nb-rule-id" title="a291bd530fa346d18cc1ce5a68d90c8f">68d90c8f</code>
</td>
<td>N/A</td>
<td>SQLi - Comment - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - Comment" (ID: <code class="nb-rule-id" title="42c424998d2a42c9808ab49c6d8d8fe4">6d8d8fe4</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="da289f9e692e4f5397d915fbfaa045cf">faa045cf</code>
</td>
<td>N/A</td>
<td>SQLi - Comparison - Beta</td>
<td>Log</td>
<td>Block</td>      
<td>This rule is merged into the original rule "SQLi - Comparison" (ID: <code class="nb-rule-id" title="8166da327a614849bfa29317e7907480">e7907480</code>)</td>
</tr>
</tbody>    
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-20">Jan 20, 2026</time><div>
<h2 id="post-2026-01-20-auxiliary-workers"><a href="/changelog/post/2026-01-20-auxiliary-workers/">Use auxiliary Workers alongside full-stack frameworks</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Auxiliary Workers are now fully supported when using full-stack frameworks, such as <a href="/workers/framework-guides/web-apps/react-router/">React Router</a> and <a href="/workers/framework-guides/web-apps/tanstack-start/">TanStack Start</a>, that integrate with the <a href="/workers/vite-plugin/reference/api/">Cloudflare Vite plugin</a>.
They are included alongside the framework's build output in the build output directory.
Note that this feature requires Vite 7 or above.</p>
<p>Auxiliary Workers are additional Workers that can be called via <a href="/workers/runtime-apis/bindings/service-bindings/">service bindings</a> from your main (entry) Worker.
They are defined in the plugin config, as in the example below:</p>
<pre tabindex="0"><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { tanstackStart } from &quot;@tanstack/react-start/plugin/vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		tanstackStart(),&#10;		cloudflare({&#10;			viteEnvironment: { name: &quot;ssr&quot; },&#10;			auxiliaryWorkers: [{ configPath: &quot;./wrangler.aux.jsonc&quot; }],&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p>See the Vite plugin <a href="/workers/vite-plugin/reference/api/">API docs</a> for more info.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-20">Jan 20, 2026</time><div>
<h2 id="post-2026-01-20-sql-module-rule"><a href="/changelog/post/2026-01-20-sql-module-rule/">Import SQL files as additional modules by default</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The <code>.sql</code> file extension is now automatically configured to be importable in your Worker code when using <a href="/workers/wrangler/bundling/#including-non-javascript-modules">Wrangler</a> or the <a href="/workers/vite-plugin/reference/non-javascript-modules/">Cloudflare Vite plugin</a>.
This is particular useful for importing migrations in Durable Objects and means you no longer need to configure custom rules when using <a href="https://orm.drizzle.team/docs/connect-cloudflare-do">Drizzle</a>.</p>
<p>SQL files are imported as JavaScript strings:</p>
<pre tabindex="0"><code class="language-ts">// `example` will be a JavaScript string&#10;import example from &quot;./example.sql&quot;;&#10;</code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-19">Jan 19, 2026</time><div>
<h2 id="post-2026-01-19-http3-499-reporting-improvement"><a href="/changelog/post/2026-01-19-http3-499-reporting-improvement/">Enhanced HTTP/3 request cancellation visibility</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><h4 id="2026-01-19-http3-499-reporting-improvement-enhanced-http-3-request-cancellation-visibility">Enhanced HTTP/3 request cancellation visibility</h4>
<p>Cloudflare now provides more accurate visibility into HTTP/3 client request cancellations, giving you better insight into real client behavior and reducing unnecessary load on your origins.</p>
<p>Previously, when an HTTP/3 client cancelled a request, the cancellation was not always actioned immediately. This meant requests could continue through the CDN — potentially all the way to your origin — even after the client had abandoned them. In these cases, logs would show the upstream response status (such as <code>200</code> or a timeout-related code) rather than reflecting the client cancellation.</p>
<p>Now, Cloudflare terminates cancelled HTTP/3 requests immediately and accurately logs them with a <code>499</code> status code.</p>
<hr />
<h4 id="2026-01-19-http3-499-reporting-improvement-better-observability-for-client-behavior">Better observability for client behavior</h4>
<p>When HTTP/3 clients cancel requests, Cloudflare now immediately reflects this in your logs with a <code>499</code> status code. This gives you:</p>
<ul>
<li><strong>More accurate traffic analysis</strong>: Understand exactly when and how often clients cancel requests.</li>
<li><strong>Clearer debugging</strong>: Distinguish between true errors and intentional client cancellations.</li>
<li><strong>Better availability metrics</strong>: Separate client-initiated cancellations from server-side issues.</li>
</ul>
<hr />
<h4 id="2026-01-19-http3-499-reporting-improvement-reduced-origin-load">Reduced origin load</h4>
<p>Cloudflare now terminates cancelled requests faster, which means:</p>
<ul>
<li><strong>Less wasted compute</strong>: Your origin no longer processes requests that clients have already abandoned.</li>
<li><strong>Lower bandwidth usage</strong>: Responses are no longer generated and transmitted for cancelled requests.</li>
<li><strong>Improved efficiency</strong>: Resources are freed up to handle active requests.</li>
</ul>
<hr />
<h4 id="2026-01-19-http3-499-reporting-improvement-what-to-expect-in-your-logs">What to expect in your logs</h4>
<p>You may notice an increase in <code>499</code> status codes for HTTP/3 traffic. For HTTP/3, a <code>499</code> indicates the client <a href="https://datatracker.ietf.org/doc/html/rfc9114#section-4.1.1">cancelled the request stream</a> before receiving a complete response — the underlying connection may remain open. This is a normal part of web traffic.</p>
<p><strong>Tip</strong>: If you use <code>499</code> codes in availability calculations, consider whether client-initiated cancellations should be excluded from error rates. These typically represent normal user behavior — such as closing a browser, navigating away from a page, mobile network drops, or cancelling a download — rather than service issues.</p>
<hr />
<p>For more information, refer to <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-499/">Error 499</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-15">Jan 15, 2026</time><div>
<h2 id="post-2026-01-15-networking-navigation-update"><a href="/changelog/post/2026-01-15-networking-navigation-update/">Network Services navigation update</a></h2>
<div class="changelog-badges"><span>magic-transit</span><span>cloudflare-network-firewall</span><span>cloudflare-wan</span><span>network-flow</span></div><div class="changelog-body"><p>The Network Services menu structure in Cloudflare's dashboard has been updated to reflect solutions and capabilities instead of product names. This will make it easier for you to find what you need and better reflects how our services work together.</p>
<p>Your existing configurations will remain the same, and you will have access to all of the same features and functionality.</p>
<p>The changes visible in your dashboard may vary based on the products you use. Overall, changes relate to <a href="https://developers.cloudflare.com/magic-transit/">Magic Transit</a>, <a href="https://developers.cloudflare.com/magic-wan/">Magic WAN</a>, and <a href="https://developers.cloudflare.com/cloudflare-network-firewall/">Magic Firewall</a>.</p>
<p><strong>Summary of changes:</strong></p>
<ul>
<li>A new <strong>Overview</strong> page provides access to the most common tasks across Magic Transit and Magic WAN.</li>
<li>Product names have been removed from top-level navigation.</li>
<li>Magic Transit and Magic WAN configuration is now organized under <strong>Routes</strong> and <strong>Connectors</strong>. For example, you will find IP Prefixes under <strong>Routes</strong>, and your GRE/IPsec Tunnels under <strong>Connectors.</strong></li>
<li>Magic Firewall policies are now called <strong>Firewall Policies.</strong></li>
<li>Magic WAN Connectors and Connector On-Ramps are now referenced in the dashboard as <strong>Appliances</strong> and <strong>Appliance profiles.</strong> They can be found under <strong>Connectors &gt; Appliances.</strong></li>
<li>Network analytics, network health, and real-time analytics are now available under <strong>Insights.</strong></li>
<li>Packet Captures are found under <strong>Insights &gt; Diagnostics.</strong></li>
<li>You can manage your Sites from <strong>Insights &gt; Network health.</strong></li>
<li>You can find Magic Network Monitoring under <strong>Insights &gt; Network flow</strong>.</li>
</ul>
<p>If you would like to provide feedback, complete <a href="https://forms.gle/htWyjRsTjw1usdis5">this form</a>. You can also find these details in the January 7, 2026 email titled <strong>[FYI] Upcoming Network Services Dashboard Navigation Update</strong>.</p>
<p>Preview:
<img src="/assets/upstream/images/changelog/cloudflare-network-firewall/networking-overview-and-navigation.png" alt="Networking Navigation" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-15">Jan 15, 2026</time><div>
<h2 id="post-2026-1-15-crowdstrike-score"><a href="/changelog/post/2026-1-15-crowdstrike-score/">Support for CrowdStrike device scores in User Risk Scoring</a></h2>
<div class="changelog-badges"><span>risk-score</span></div><div class="changelog-body"><p>Cloudflare One has expanded its [User Risk Scoring] (/cloudflare-one/insights/risk-score/) capabilities by introducing two new behaviors for organizations using the [CrowdStrike integration] (/cloudflare-one/integrations/service-providers/crowdstrike/).</p>
<p>Administrators can now automatically escalate the risk score of a user if their device matches specific CrowdStrike Zero Trust Assessment (ZTA) score ranges. This allows for more granular security policies that respond dynamically to the health of the endpoint.</p>
<p>New risk behaviors
The following risk scoring behaviors are now available:</p>
<ul>
<li>CrowdStrike low device score: Automatically increases a user's risk score when the connected device reports a &quot;Low&quot; score from CrowdStrike.</li>
<li>CrowdStrike medium device score: Automatically increases a user's risk score when the connected device reports a &quot;Medium&quot; score from CrowdStrike.</li>
</ul>
<p>These scores are derived from [CrowdStrike device posture attributes] (/cloudflare-one/integrations/service-providers/crowdstrike/#device-posture-attributes), including OS signals and sensor configurations.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-15">Jan 15, 2026</time><div>
<h2 id="post-2026-01-15-warp-connector-ping-support"><a href="/changelog/post/2026-01-15-warp-connector-ping-support/">Verify WARP Connector connectivity with a simple ping</a></h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-tunnel-sase</span></div><div class="changelog-body"><p>We have made it easier to validate connectivity when deploying <a href="/mesh/">WARP Connector</a> as part of your <a href="/reference-architecture/architectures/sase/#connecting-networks">software-defined private network</a>.</p>
<p>You can now <code>ping</code> the WARP Connector host directly on its LAN IP address immediately after installation. This provides a fast, familiar way to confirm that the Connector is online and reachable within your network before testing access to downstream services.</p>
<p>Starting with <a href="/changelog/2026-01-13-warp-linux-ga/">version 2025.10.186.0</a>, WARP Connector responds to traffic addressed to its own LAN IP, giving you immediate visibility into Connector reachability.</p>
<p>Learn more about deploying <a href="/mesh/">WARP Connector</a> and building private network connectivity with <a href="/cloudflare-one/">Cloudflare One</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-15">Jan 15, 2026</time><div>
<h2 id="post-2026-01-15-waf-release"><a href="/changelog/post/2026-01-15-waf-release/">WAF Release - 2026-01-15</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release focuses on improvements to existing detections to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against SQL Injection.</li>
</ul>
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
        <code class="nb-rule-id" title="eb3f44c07266448b9fa54ee7ad7dad3e">ad7dad3e</code>
</td>
<td>N/A</td>
<td>SQLi - String Function - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - String Function" (ID: <code class="nb-rule-id" title="63e03eecddfc4b3fb0cad587d32b798c">d32b798c</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="adf076af09b2484ca9e7881f9e553ad3">9e553ad3</code>
</td>
<td>N/A</td>
<td>SQLi - Sub Query - Beta</td>
<td>Log</td>
<td>Block</td>      
<td>This rule is merged into the original rule "SQLi - Sub Query" (ID: <code class="nb-rule-id" title="6ec5ecf52c094330aff99a38743e66b1">743e66b1</code>)</td>
</tr>
</tbody>    
</table>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/26/">Previous</a><span>Page 27 of 50</span><a class="pagination-next" rel="next" href="/changelog/28/">Next</a></nav>
</div>
