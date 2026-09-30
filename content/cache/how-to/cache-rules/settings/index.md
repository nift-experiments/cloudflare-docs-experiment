---
cp9:
  canonical: https://developers.cloudflare.com/cache/how-to/cache-rules/settings/
  description: Available settings for Cache Rules.
  full_title: Cache Rules settings · Cloudflare Cache (CDN) docs
  head_html: <title>Cache Rules settings · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Available settings for Cache Rules."><link rel="canonical" href="https://developers.cloudflare.com/cache/how-to/cache-rules/settings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/how-to/cache-rules/settings/index.md"><meta property="og:title" content="Cache Rules settings · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Available settings for Cache Rules."><meta property="og:url" content="https://developers.cloudflare.com/cache/how-to/cache-rules/settings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/how-to/cache-rules/settings/#page","headline":"Cache Rules settings \u00b7 Cloudflare Cache (CDN) docs","description":"Available settings for Cache Rules.","url":"https://developers.cloudflare.com/cache/how-to/cache-rules/settings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/how-to/cache-rules/settings/
  schema: 1
---
<p>These are the settings that you can configure when creating a cache rule.</p>
<h2 id="fields">Fields</h2>
<p>The fields available for Cache Rule matching expressions in the <strong>Expression Builder</strong> are:</p>
<ul>
<li>URI Full - <code>http.request.full_uri</code></li>
<li>URI - <code>http.request.uri</code></li>
<li>URI Path - <code>http.request.uri.path</code></li>
<li>URI Query String - <code>http.request.uri.query</code></li>
<li>Cookie - <code>http.cookie</code></li>
<li>Hostname - <code>http.host</code></li>
<li>Referer - <code>http.referer</code></li>
<li>SSL/HTTPS - <code>ssl</code></li>
<li>User Agent - <code>http.user_agent</code></li>
<li>X-Forwarded-For - <code>http.x_forwarded_for</code></li>
<li>Request Headers - <code>http.request.headers</code></li>
<li>Cookie value of - <code>http.request.cookies</code></li>
<li>File extension - <code>http.request.uri.path.extension</code></li>
</ul>
<p>If you select the <a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-editor">Edit expression</a> option, you can enter additional fields supported by Cache Rules. These fields include:</p>
<ul>
<li><code>cf.bot_management.score</code></li>
<li><code>cf.bot_management.ja3_hash</code></li>
<li><code>cf.bot_management.ja4</code></li>
<li><code>cf.bot_management.verified_bot</code></li>
<li><code>cf.bot_management.static_resource</code></li>
<li><code>cf.bot_management.js_detection.passed</code></li>
<li><code>cf.bot_management.detection_ids</code></li>
<li><code>cf.bot_management.tags</code></li>
<li><code>cf.bot_management.signed_agent</code></li>
<li><code>cf.bot_management.corporate_proxy</code></li>
<li><code>ip.src.asnum</code></li>
</ul>
<p>Bot Management fields require a <a href="/bots/plans/bm-subscription/">Bot Management subscription</a>. For field types, descriptions, and expression syntax, refer to the <a href="/ruleset-engine/rules-language/fields/reference/">Fields reference</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3886.md")
</aside>
<h2 id="operators">Operators</h2>
<p>The operators available for Cache Rule expressions are:</p>
<ul>
<li>wildcard</li>
<li>strict wildcard</li>
<li>equals</li>
<li>does not equal</li>
<li>contains</li>
<li>does not contain</li>
<li>matches regex</li>
<li>does not match regex</li>
<li>starts with</li>
<li>ends with</li>
<li>does not start with</li>
<li>does not end with</li>
<li>is in</li>
<li>is not in</li>
<li>is in list</li>
<li>is not in list</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3885.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3884.md")
</aside>
<h2 id="cache-eligibility">Cache eligibility</h2>
<p>In <strong>Cache eligibility</strong>, you have the option to select <strong>Bypass cache</strong> if you want matching requests to not be cached, or <strong>Eligible for cache</strong> if you want Cloudflare to attempt to cache them.</p>
<h3 id="bypass-cache">Bypass cache</h3>
<p>When creating a cache rule, you have the option to select <strong>Bypass cache</strong> if you want matching incoming requests to not be cached. Alternatively, you can use <a href="/cache/reference/development-mode/">Development Mode</a>, if you want to bypass cache for shorter periods.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3883.md")
</aside>
<h3 id="eligible-for-cache-settings">Eligible for cache settings</h3>
<p>When you select <strong>Eligible for cache</strong>, you can change the configuration settings described below.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3882.md")
</aside>
<h4 id="edge-ttl">Edge TTL</h4>
<p>Edge Cache TTL refers to the maximum cache time-to-live (TTL), or how long an asset should be considered fresh or available to serve from Cloudflare’s cache in response to requests. This setting has three primary options:</p>
<ul>
<li><strong>Use cache control-header if present, bypass cache if not</strong>: If a cache-control header is present on the response, follow its directives. If not, skip caching entirely.</li>
<li><strong>Use cache-control header if present, use default Cloudflare caching behavior if not</strong>: If a cache-control header is present on the response, follow its directives. If not, cache in accordance with our <a href="/cache/how-to/configure-cache-status-code/#edge-ttl">default edge TTL settings</a>.</li>
<li><strong>Ignore cache-control header and use this TTL</strong>: Completely ignore any cache-control header on the response and instead cache the response for a duration specified in the timing dropdown.</li>
</ul>
<p>Additionally, you can select how long you would like a particular matching status code's content to be cached in Cloudflare's global network. In <strong>Status Code TTL</strong> section you can define the TTL duration for one or more status codes of responses from the origin server. This setting can be applied to a <em>Single code</em> status code, to a <em>Greater than or equal</em> or <em>Less than or equal</em> status code, or to a <em>Range</em> of status codes. Status code TTLs are similar to <strong>Ignore cache-control header and use this TTL</strong> in that the cache-control header on the response will be ignored in favor of the TTL specified by the cache rule. For more information, refer to <a href="/cache/how-to/configure-cache-status-code/">Status code TTL</a>.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3887.md")
</div></details>
<h4 id="browser-ttl">Browser TTL</h4>
<p>Browser TTL refers to the maximum cache time-to-live (TTL) that an asset should be considered available to serve from the browser’s cache.</p>
<p>Select if you want to <strong>Bypass cache</strong>, <strong>Respect origin</strong>, or <strong>Override origin</strong>. If you wish to override the browser TTL value, define how long resources cached by client browsers will remain valid from the dropdown menu. For more information, refer to <a href="/cache/how-to/edge-browser-cache-ttl/#browser-cache-ttl">Browser Cache TTL</a>.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3888.md")
</div></details>
<h4 id="cache-key">Cache Key</h4>
<p>Cache keys refer to the criteria that Cloudflare uses to determine how to store resources in our cache. Customizing the Cache Key allows you to determine how Cloudflare can reuse particular cache entries across requests or share the cache entries for more granularity for end users.</p>
<p>There is no explicit length limit for cache keys. However, the total request size (including headers used in the cache key) must not exceed Cloudflare's <a href="/fundamentals/reference/connection-limits/#request-limits">request limits</a>. Including large values (such as cookies) in the cache key may increase per-request latency. The maximum number of query string parameters in a custom cache key configuration is 100.</p>
<p>Define the request components used to define a <a href="/cache/how-to/cache-keys/">custom Cache Key</a>, customizing the following options:</p>
<ul>
<li>You can switch on or off <a href="/cache/cache-security/cache-deception-armor/">Cache deception armor</a>, <a href="/automatic-platform-optimization/reference/cache-device-type/">Cache by device type</a>, and <a href="/cache/how-to/cache-keys/#query-string">Sort query string</a>.</li>
</ul>
<p>Enterprise customers have these additional options for custom Cache Keys:</p>
<ul>
<li>
<p>In the <strong>Query string</strong> section, you can select <strong>All query string parameters</strong>, <strong>All query string parameters except</strong> and enter an exception, <strong>No query parameters except</strong> and enter the parameters, or <strong>Ignore query string</strong> (also available for Pay-as-you-go customers).</p>
</li>
<li>
<p>In the <strong>Headers</strong> section, you can specify header names along with their values. For custom headers, values are optional; however, for the following restricted headers, you must include one to three specific values:</p>
<ul>
<li><code>accept</code></li>
<li><code>accept-charset</code></li>
<li><code>accept-encoding</code></li>
<li><code>accept-datetime</code></li>
<li><code>accept-language</code></li>
<li><code>referer</code></li>
<li><code>user-agent</code></li>
</ul>
<p>To check for a header's presence without including its value, use the <strong>Check presence of</strong> option. You can also choose whether to <strong>Include origin header</strong>.</p>
</li>
<li>
<p>In the <strong>Cookie</strong> section, you can include cookie names and their values, and check for the presence of another cookie.</p>
</li>
<li>
<p>In the <strong>Host</strong> section, you can select <strong>Use original host</strong> and <strong>Resolved host</strong>. In the <strong>User</strong> section, you can select <strong>Device type</strong>, <strong>Country</strong>, and <strong>Language</strong>. Using <strong>Resolved host</strong> means the Cache Key will contain whatever hostname was used to resolve the origin IP which can be different depending on whether the <a href="/rules/origin-rules/features/#dns-record">resolve override</a> feature is on or not.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3881.md")
</aside>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3889.md")
</div></details>
<h4 id="cache-reserve-eligibility">Cache Reserve Eligibility</h4>
<p>Cache Reserve eligibility allows you to specify which website resources should be eligible for our persistent cache called <a href="/cache/advanced-configuration/cache-reserve/">Cache Reserve</a>. If the request matches and also meets <a href="/cache/advanced-configuration/cache-reserve/#cache-reserve-asset-eligibility">eligibility criteria</a>, Cloudflare will write the resource to cache reserve. This requires an add-on cache reserve plan.</p>
<p>This rule can also be used to specify Cache Reserve eligibility for website resources based on their size. For example, by specifying that all assets which are eligible be 100 MB and above, Cloudflare will look for eligible assets at or above 100 MB for Cache Reserve eligibility and only persistently store those assets.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3880.md")
</aside>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3890.md")
</div></details>
<h4 id="caching-on-port-enterprise-only">Caching on Port (Enterprise-only)</h4>
<p>Cloudflare supports several <a href="/fundamentals/reference/network-ports/#network-ports-compatible-with-cloudflares-proxy">network ports</a> by default, like 80 or 443. Some ports, traditionally admin ports, are supported but have caching disabled as they are used to manage sensitive information that should be ineligible for cache. Enterprise customers wanting to enable caching on these admin ports can cache on these ports by entering their desired port.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3878.md")
</aside>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3891.md")
</div></details>
<h4 id="proxy-read-timeout-enterprise-only">Proxy Read Timeout (Enterprise-only)</h4>
<p>Defines a timeout value between two successive read operations to your origin server. The default value can be found in the <a href="/fundamentals/reference/connection-limits/">Connection limits</a> table. If you are attempting to reduce <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/"><code>HTTP 524</code></a> errors because of timeouts from an origin server, try increasing this timeout value using the API endpoint below.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3892.md")
</div></details>
<h4 id="serve-stale-content-while-revalidating">Serve stale content while revalidating</h4>
<p>Defines if Cloudflare will serve stale content while updating the latest content from the origin server. If serving stale content is disabled, Cloudflare will not serve stale content while getting the latest content from the origin.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3893.md")
</div></details>
<h4 id="origin-range-requests">Origin range requests</h4>
<p>Origin Range Requests let Cloudflare fetch large files from your origin in cache-aligned byte ranges. Cloudflare may expand a client range and issue several single-range origin requests. Your origin may receive ranges that differ from the client's <code>Range</code> header.</p>
<p>This setting does not make a request or response cacheable. Cloudflare can use origin range fetching for an eligible <code>GET</code> even if the response is not stored. File-size limits apply to the complete object, not the requested range. <a href="/cache/advanced-configuration/cache-reserve/#limits">Cache Reserve</a> does not support Origin Range Requests.</p>
<p>Cloudflare asks the origin for unencoded content. Origins should return compatible range responses throughout the request. If an origin ignores <code>Range</code> and returns <code>200 OK</code>, Cloudflare can use the response but must download the complete file. For all origin and client response requirements, refer to <a href="/cache/reference/range-requests/">Range request behavior</a>.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3894.md")
</div></details>
<h4 id="respect-strong-etags">Respect Strong ETags</h4>
<p>Turn on or off byte-for-byte equivalency checks between the Cloudflare cache and the origin server. When enabled, Cloudflare will use <a href="/cache/reference/etag-headers/#strong-etags">strong ETag</a> header validation to ensure that resources in the Cloudflare cache and on the origin server are byte-for-byte identical. If disabled, Cloudflare converts ETag headers into <a href="/cache/reference/etag-headers/#weak-etags">weak ETag</a> headers.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3895.md")
</div></details>
<h4 id="origin-error-page-pass-through">Origin error page pass-through</h4>
<p>Turn on or off Cloudflare error pages generated from error HTTP status codes sent from the origin server. If enabled, this setting enables the use of error pages issued by the origin.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3896.md")
</div></details>
<h4 id="origin-cache-control-enterprise-only">Origin Cache Control (Enterprise-only)</h4>
<p>When this option is enabled, Cloudflare will aim to strictly adhere to <a href="https://datatracker.ietf.org/doc/html/rfc7234">RFC 7234</a>. Enterprise customers have the ability to select if Cloudflare will adhere to this behavior. Free, Pro, and Business customers have this option enabled by default and cannot disable it.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3897.md")
</div></details>
<h4 id="vary">Vary</h4>
<p>The <code>Vary</code> response header lets your origin cache multiple versions of the same URL based on request headers. Use the <code>vary</code> object to configure how Cloudflare handles each header your origin lists in its <code>Vary</code> response. For how Vary affects cache keys and how normalization works, refer to <a href="/cache/concepts/vary/">Vary</a>.</p>
<p>The <code>vary</code> object supports these keys:</p>
<table>
<thead>
<tr>
<th>Key</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>default</code></td>
<td>Yes</td>
<td>Configuration for any header name in the origin <code>Vary</code> response that is not included in <code>headers</code>.</td>
</tr>
<tr>
<td><code>headers</code></td>
<td>No</td>
<td>A map of lowercase request header names to configuration objects.</td>
</tr>
</tbody>
</table>
<p>If the <code>vary</code> object is omitted, this Cache Rules Vary setting is turned off. Other Vary behavior, such as <code>Vary: *</code>, <a href="/cache/advanced-configuration/vary-for-images/">Vary for images</a>, and compression handling, is unaffected. If the <code>vary</code> object is present, <code>default</code> is required. An empty <code>vary</code> object is invalid.</p>
<p>Each header configuration object, and the <code>default</code> object, must include an <code>action</code> key set to one of <code>normalize</code>, <code>passthrough</code>, or <code>bypass</code>. Refer to <a href="/cache/concepts/vary/#actions">Actions</a> for guidance on when to use each.</p>
<p>Additional parameters can be specified for certain header names:</p>
<table>
<thead>
<tr>
<th>Header</th>
<th>Additional key</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>accept</code></td>
<td><code>media_types</code></td>
<td>List of MIME types to include when normalizing the <code>Accept</code> header. Maximum 10 items.</td>
</tr>
<tr>
<td><code>accept-language</code></td>
<td><code>languages</code></td>
<td>List of languages to include when normalizing the <code>Accept-Language</code> header. Maximum 20 items.</td>
</tr>
</tbody>
</table>
<p>For most deployments, start with a restrictive <code>default</code> and explicit per-header configuration:</p>
<ul>
<li>Use <code>default</code> set to <code>bypass</code> to avoid caching variants for unexpected origin <code>Vary</code> headers.</li>
<li>Add explicit <code>headers</code> entries for the headers you expect your origin to vary on.</li>
<li>Use <code>normalize</code> for <code>accept</code>, <code>accept-language</code>, and <code>accept-encoding</code> unless your origin requires raw header values.</li>
<li>Use <code>media_types</code> and <code>languages</code> allowlists when you know the exact variants your origin can serve.</li>
<li>Use <code>passthrough</code> only when exact raw header values should select different cached versions.</li>
<li>Use <code>bypass</code> for high-cardinality headers such as <code>user-agent</code>, cookies, or request headers with per-user values.</li>
</ul>
<p>The following limits and validation rules apply:</p>
<ul>
<li>Header names in <code>headers</code> must be lowercase.</li>
<li>Header names can contain letters, numbers, underscores, and hyphens.</li>
<li>Header names cannot exceed 128 characters.</li>
<li>Header names beginning with <code>cf-</code> or <code>cf_</code> are not allowed.</li>
<li>Certain hop-by-hop or cache-control headers, such as <code>connection</code>, <code>host</code>, and <code>cache-control</code>, are not allowed.</li>
<li><code>headers</code> can contain up to 50 entries.</li>
<li><code>accept.media_types</code> can contain up to 10 entries.</li>
<li><code>accept-language.languages</code> can contain up to 20 entries.</li>
<li>Values in <code>media_types</code> and <code>languages</code> must be non-empty printable ASCII.</li>
</ul>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3898.md")
</div></details>
