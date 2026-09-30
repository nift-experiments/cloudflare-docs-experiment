---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/request/
  description: Interface that represents an HTTP request.
  full_title: Request · Cloudflare Workers docs
  head_html: <title>Request · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Interface that represents an HTTP request."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/request/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/request/index.md"><meta property="og:title" content="Request · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Interface that represents an HTTP request."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/request/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/request/#page","headline":"Request \u00b7 Cloudflare Workers docs","description":"Interface that represents an HTTP request.","url":"https://developers.cloudflare.com/workers/runtime-apis/request/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/request/
  schema: 1
---
<p>The <a href="https://developer.mozilla.org/en-US/docs/Web/API/Request/Request"><code>Request</code></a> interface represents an HTTP request and is part of the <a href="/workers/runtime-apis/fetch/">Fetch API</a>.</p>
<h2 id="background">Background</h2>
<p>The most common way you will encounter a <code>Request</code> object is as a property of an incoming request:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		return new Response(&#x27;Hello World!&#x27;);&#10;	},&#10;};&#10;</code></pre>
<p>You may also want to construct a <code>Request</code> yourself when you need to modify a request object, because the incoming <code>request</code> parameter that you receive from the <a href="/workers/runtime-apis/handlers/fetch/"><code>fetch()</code> handler</a> is immutable.</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;        const url = &quot;https://example.com&quot;;&#10;        const modifiedRequest = new Request(url, request);&#10;		// ...&#10;	},&#10;};&#10;</code></pre>
<p>The <a href="/workers/runtime-apis/handlers/fetch/"><code>fetch() handler</code></a> invokes the <code>Request</code> constructor. The <a href="#options"><code>RequestInit</code></a> and <a href="#the-cf-property-requestinitcfproperties"><code>RequestInitCfProperties</code></a> types defined below also describe the valid parameters that can be passed to the <a href="/workers/runtime-apis/handlers/fetch/"><code>fetch() handler</code></a>.</p>
<hr />
<h2 id="constructor">Constructor</h2>
<pre tabindex="0"><code class="language-js">let request = new Request(input, options)&#10;</code></pre>
<h3 id="parameters">Parameters</h3>
<ul>
<li>
<p><code>input</code> string | Request</p>
<ul>
<li>Either a string that contains a URL, or an existing <code>Request</code> object.</li>
</ul>
</li>
<li>
<p><code>options</code> options optional</p>
<ul>
<li>Optional options object that contains settings to apply to the <code>Request</code>.</li>
</ul>
</li>
</ul>
<h4 id="options"><code>options</code></h4>
<p>An object containing properties that you want to apply to the request.</p>
<ul>
<li>
<p><code>cache</code> <code>undefined | 'no-store' | 'no-cache'</code> optional</p>
<ul>
<li>Standard HTTP <code>cache</code> header. Only <code>cache: 'no-store'</code> and <code>cache: 'no-cache'</code> are supported.
Any other cache header will result in a <code>TypeError</code> with the message <code>Unsupported cache mode: &lt;attempted-cache-mode&gt;</code>.</li>
</ul>
</li>
<li>
<p><code>cf</code> RequestInitCfProperties optional</p>
<ul>
<li>Cloudflare-specific properties that can be set on the <code>Request</code> that control how Cloudflare’s global network handles the request.</li>
</ul>
</li>
<li>
<p><code>method</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The HTTP request method. The default is <code>GET</code>. In Workers, all <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods">HTTP request methods</a> are supported, except for <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/CONNECT"><code>CONNECT</code></a>.</li>
</ul>
</li>
<li>
<p><code>headers</code> Headers optional</p>
<ul>
<li>A <a href="https://developer.mozilla.org/en-US/docs/Web/API/Headers"><code>Headers</code> object</a>.</li>
</ul>
</li>
<li>
<p><code>body</code> string | ReadableStream | FormData | URLSearchParams optional</p>
<ul>
<li>The request body, if any.</li>
<li>Note that a request using the GET or HEAD method cannot have a body.</li>
</ul>
</li>
<li>
<p><code>redirect</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The redirect mode to use: <code>follow</code>, <code>error</code>, or <code>manual</code>. The default  for a new <code>Request</code> object is <code>follow</code>. Note, however, that the incoming <code>Request</code> property of a <code>FetchEvent</code> will have redirect mode <code>manual</code>.</li>
</ul>
</li>
<li>
<p><code>signal</code> AbortSignal optional</p>
<ul>
<li>If provided, the request can be canceled by triggering an abort on the corresponding <code>AbortController</code>.</li>
</ul>
</li>
</ul>
<h4 id="the-cf-property-requestinitcfproperties">The <code>cf</code> property (<code>RequestInitCfProperties</code>)</h4>
<p>An object containing Cloudflare-specific properties that can be set on the <code>Request</code> object. For example:</p>
<pre tabindex="0"><code class="language-js">// Disable ScrapeShield for this request.&#10;fetch(event.request, { cf: { scrapeShield: false } })&#10;</code></pre>
<p>Invalid or incorrectly-named keys in the <code>cf</code> object will be silently ignored. Consider using TypeScript and generating types by running <a href="/workers/languages/typescript/#generate-types"><code>wrangler types</code></a> to ensure proper use of the <code>cf</code> object.</p>
<ul>
<li>
<p><code>apps</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Whether <a href="https://www.cloudflare.com/apps/">Cloudflare Apps</a> should be enabled for this request. Defaults to <code>true</code>.</li>
</ul>
</li>
<li>
<p><code>cacheEverything</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Treats all content as static and caches all <a href="/cache/concepts/default-cache-behavior#default-cached-file-extensions">file types</a> beyond the Cloudflare default cached content. Respects cache headers from the origin web server. This is equivalent to setting the Page Rule <a href="/rules/page-rules/reference/settings/"><strong>Cache Level</strong> (to <strong>Cache Everything</strong>)</a>. Defaults to <code>false</code>.
This option applies to <code>GET</code> and <code>HEAD</code> request methods only.</li>
</ul>
</li>
<li>
<p><code>cacheKey</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A request’s cache key is what determines if two requests are the same for caching purposes. If a request has the same cache key as some previous request, then Cloudflare can serve the same cached response for both.</li>
</ul>
</li>
<li>
<p><code>cacheTags</code> Array&lt;string&gt; optional</p>
<ul>
<li>This option appends additional <a href="/cache/how-to/purge-cache/purge-by-tags/"><strong>Cache-Tag</strong></a> headers to the response from the origin server. This allows for purges of cached content based on tags provided by the Worker, without modifications to the origin server. This is performed using the <a href="/cache/how-to/purge-cache/purge-by-tags/#purge-using-cache-tags"><strong>Purge by Tag</strong></a> feature.</li>
</ul>
</li>
<li>
<p><code>cacheTtl</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>This option forces Cloudflare to cache the response for this request, regardless of what headers are seen on the response. This is equivalent to setting two Page Rules: <a href="/cache/how-to/edge-browser-cache-ttl/"><strong>Edge Cache TTL</strong></a> and <a href="/rules/page-rules/reference/settings/"><strong>Cache Level</strong> (to <strong>Cache Everything</strong>)</a>. The value must be zero or a positive number. A value of <code>0</code> indicates that the cache asset expires immediately. This option applies to <code>GET</code> and <code>HEAD</code> request methods only.</li>
</ul>
</li>
<li>
<p><code>cacheTtlByStatus</code> <code>{ [key: string]: number }</code> optional</p>
<ul>
<li>This option is a version of the <code>cacheTtl</code> feature which chooses a TTL based on the response’s status code. If the response to this request has a status code that matches, Cloudflare will cache for the instructed time and override cache instructives sent by the origin. For example: <code>{ &quot;200-299&quot;: 86400, &quot;404&quot;: 1, &quot;500-599&quot;: 0 }</code>. The value can be any integer, including zero and negative integers. A value of <code>0</code> indicates that the cache asset expires immediately. Any negative value instructs Cloudflare not to cache at all. This option applies to <code>GET</code> and <code>HEAD</code> request methods only.</li>
</ul>
</li>
<li>
<p><code>vary</code> <span class="nb-type">RequestInitCfPropertiesVary</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Controls how Cloudflare caches origin responses with a <code>Vary</code> header for a single <code>fetch()</code> request. If both <code>cf.vary</code> and <a href="/cache/how-to/cache-rules/settings/#vary">Cache Rules Vary</a> apply, <code>cf.vary</code> takes precedence for this subrequest.</li>
</ul>
</li>
<li>
<p><code>image</code> Object | null optional</p>
<ul>
<li>Enables <a href="/images/optimization/transformations/overview/">Image Resizing</a> for this request. The possible values are described in <a href="/images/optimization/transformations/transform-via-workers/">Transform images via Workers</a> documentation.</li>
</ul>
</li>
<li>
<p><code>polish</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Sets <a href="https://blog.cloudflare.com/introducing-polish-automatic-image-optimizati/">Polish</a> mode. The possible values are <code>lossy</code>, <code>lossless</code> or <code>off</code>.</li>
</ul>
</li>
<li>
<p><code>resolveOverride</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Directs the request to an alternate origin server by overriding the DNS lookup. The value of <code>resolveOverride</code> specifies an alternate hostname which will be used when determining the origin IP address, instead of using the hostname specified in the URL. The <code>Host</code> header of the request will still match what is in the URL. Thus, <code>resolveOverride</code> allows a request to be sent to a different server than the URL / <code>Host</code> header specifies. However, <code>resolveOverride</code> will only take effect if both the URL host and the host specified by <code>resolveOverride</code> are within your zone. If either specifies a host from a different zone / domain, then the option will be ignored for security reasons. If you need to direct a request to a host outside your zone (while keeping the <code>Host</code> header pointing within your zone), first create a CNAME record within your zone pointing to the outside host, and then set <code>resolveOverride</code> to point at the CNAME record. Note that, for security reasons, it is not possible to set the <code>Host</code> header to specify a host outside of your zone unless the request is actually being sent to that host.</li>
</ul>
</li>
<li>
<p><code>scrapeShield</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Whether <a href="https://blog.cloudflare.com/introducing-scrapeshield-discover-defend-dete/">ScrapeShield</a> should be enabled for this request, if otherwise configured for this zone. Defaults to <code>true</code>.</li>
</ul>
</li>
<li>
<p><code>webp</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Enables or disables <a href="https://blog.cloudflare.com/a-very-webp-new-year-from-cloudflare/">WebP</a> image format in <a href="/images/polish/">Polish</a>.</li>
</ul>
</li>
</ul>
<h4 id="the-cf-vary-property">The <code>cf.vary</code> property</h4>
<p>The <code>cf.vary</code> object controls how Cloudflare handles request headers named by the origin <code>Vary</code> response header for a single <code>fetch()</code> request. It uses the same <code>default</code> and <code>headers</code> shape as <a href="/cache/how-to/cache-rules/settings/#vary">Cache Rules Vary</a>, and the same actions and normalization behavior as <a href="/cache/concepts/vary/">Vary</a>.</p>
<p>If you omit <code>cf.vary</code>, Cloudflare uses other Vary behavior for the zone, including Cache Rules Vary if configured.</p>
<p>The origin response must include a <code>Vary</code> header for this setting to affect the cache key. A response containing <code>Vary: *</code> always bypasses cache.</p>
<p>The <code>cf.vary</code> object supports these keys:</p>
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
<p>If the <code>vary</code> object is present, <code>default</code> is required. An empty <code>vary</code> object is invalid. Invalid <code>cf.vary</code> configurations are ignored for that request.</p>
<p>Each header configuration object, and the <code>default</code> object, must include an <code>action</code> key set to one of <code>normalize</code>, <code>passthrough</code>, or <code>bypass</code>. For guidance, refer to <a href="/cache/concepts/vary/#actions">Actions</a>.</p>
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
<td>MIME types to keep when normalizing the <code>Accept</code> header. Maximum 10 items and 255 characters per item.</td>
</tr>
<tr>
<td><code>accept-language</code></td>
<td><code>languages</code></td>
<td>Languages to keep when normalizing the <code>Accept-Language</code> header. Maximum 20 items and 64 characters per item.</td>
</tr>
</tbody>
</table>
<p>The <code>default</code> object and <code>headers</code> entries other than <code>accept</code> and <code>accept-language</code> support only <code>action</code>.</p>
<p>For most deployments, set <code>default.action</code> to <code>bypass</code>, add <code>headers</code> entries for expected origin <code>Vary</code> headers, and use <code>normalize</code> for <code>accept</code> and <code>accept-language</code> unless your origin requires raw header values.</p>
<p>The following limits and validation rules apply:</p>
<ul>
<li>Header names in <code>headers</code> must be lowercase.</li>
<li>Header names can contain lowercase letters, numbers, underscores, and hyphens.</li>
<li>Header names cannot exceed 128 characters.</li>
<li>Header names beginning with <code>cf-</code> or <code>cf_</code> are not allowed.</li>
<li>Certain hop-by-hop, cache-control, or proxy-control headers are not allowed. Examples include <code>connection</code>, <code>content-length</code>, <code>cache-control</code>, <code>host</code>, <code>range</code>, <code>origin</code>, and <code>x-forwarded-for</code>.</li>
<li><code>headers</code> can contain up to 50 entries.</li>
<li><code>accept.media_types</code> can contain up to 10 entries.</li>
<li><code>accept-language.languages</code> can contain up to 20 entries.</li>
<li>Values in <code>media_types</code> and <code>languages</code> must be non-empty printable ASCII strings.</li>
</ul>
<p>The following request init fragment normalizes <code>Accept</code> and <code>Accept-Language</code>, and bypasses cache for any other header in the origin <code>Vary</code> response:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;cf&quot;: {&#10;		&quot;vary&quot;: {&#10;			&quot;default&quot;: {&#10;				&quot;action&quot;: &quot;bypass&quot;&#10;			},&#10;			&quot;headers&quot;: {&#10;				&quot;accept&quot;: {&#10;					&quot;action&quot;: &quot;normalize&quot;,&#10;					&quot;media_types&quot;: [&quot;text/html&quot;, &quot;application/json&quot;]&#10;				},&#10;				&quot;accept-language&quot;: {&#10;					&quot;action&quot;: &quot;normalize&quot;,&#10;					&quot;languages&quot;: [&quot;en&quot;, &quot;fr&quot;, &quot;de&quot;]&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<hr />
<h2 id="properties">Properties</h2>
<p>All properties of an incoming <code>Request</code> object (the request you receive from the <a href="/workers/runtime-apis/handlers/fetch/"><code>fetch()</code> handler</a>) are read-only. To modify the properties of an incoming request, create a new <code>Request</code> object and pass the options to modify to its <a href="#constructor">constructor</a>.</p>
<ul>
<li>
<p><code>body</code> ReadableStream read-only</p>
<ul>
<li>Stream of the body contents.</li>
</ul>
</li>
<li>
<p><code>bodyUsed</code> Boolean read-only</p>
<ul>
<li>Declares whether the body has been used in a response yet.</li>
</ul>
</li>
<li>
<p><code>cf</code> IncomingRequestCfProperties read-only</p>
<ul>
<li>An object containing properties about the incoming request provided by Cloudflare’s global network.</li>
<li>This property is read-only (unless created from an existing <code>Request</code>). To modify its values, pass in the new values on the <a href="/workers/runtime-apis/request/#the-cf-property-requestinitcfproperties"><code>cf</code> key of the <code>init</code> options argument</a> when creating a new <code>Request</code> object.</li>
</ul>
</li>
<li>
<p><code>headers</code> Headers read-only</p>
<ul>
<li>
<p>A <a href="https://developer.mozilla.org/en-US/docs/Web/API/Headers"><code>Headers</code> object</a>.</p>
</li>
<li>
<p>Compared to browsers, Cloudflare Workers imposes very few restrictions on what headers you are allowed to send. For example, a browser will not allow you to set the <code>Cookie</code> header, since the browser is responsible for handling cookies itself. Workers, however, has no special understanding of cookies, and treats the <code>Cookie</code> header like any other header.</p>
</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16136.md")
</aside>
<ul>
<li>
<p><code>method</code> string read-only</p>
<ul>
<li>Contains the request’s method, for example, <code>GET</code>, <code>POST</code>, etc.</li>
</ul>
</li>
<li>
<p><code>redirect</code> string read-only</p>
<ul>
<li>The redirect mode to use: <code>follow</code>, <code>error</code>, or <code>manual</code>. The <code>fetch</code> method will automatically follow redirects if the redirect mode is set to <code>follow</code>. If set to <code>manual</code>, the <code>3xx</code> redirect response will be returned to the caller as-is. The default for a new <code>Request</code> object is <code>follow</code>. Note, however, that the incoming <code>Request</code> property of a <code>FetchEvent</code> will have redirect mode <code>manual</code>.</li>
</ul>
</li>
<li>
<p><code>signal</code> AbortSignal read-only</p>
<ul>
<li>The <code>AbortSignal</code> corresponding to this request. If you use the <a href="/workers/configuration/compatibility-flags/#enable-requestsignal-for-incoming-requests"><code>enable_request_signal</code></a> compatibility flag, you can attach an event listener to the signal. This allows you to perform cleanup tasks or write to logs before your Worker's invocation ends.
For example, if you run the Worker below, and then abort the request from the client, a log will be written:</li>
</ul>
</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16137.md")
</div>
<ul>
<li>
<p><code>url</code> string read-only</p>
<ul>
<li>Contains the URL of the request.</li>
</ul>
</li>
</ul>
<h3 id="incomingrequestcfproperties"><code>IncomingRequestCfProperties</code></h3>
<p>In addition to the properties on the standard <a href="https://developer.mozilla.org/en-US/docs/Web/API/Request"><code>Request</code></a> object, the <code>request.cf</code> object on an inbound <code>Request</code> contains information about the request provided by Cloudflare’s global network.</p>
<p>All plans have access to:</p>
<ul>
<li>
<p><code>asn</code> Number</p>
<ul>
<li>ASN of the incoming request, for example, <code>395747</code>.</li>
</ul>
</li>
<li>
<p><code>asOrganization</code> string</p>
<ul>
<li>The organization which owns the ASN of the incoming request, for example, <code>Google Cloud</code>.</li>
</ul>
</li>
<li>
<p><code>botManagement</code> Object | null</p>
<ul>
<li>Only set when using Cloudflare Bot Management. Object with the following properties: <code>score</code>, <code>verifiedBot</code>, <code>signedAgent</code>, <code>staticResource</code>, <code>ja3Hash</code>, <code>ja4</code>, and <code>detectionIds</code>. Refer to <a href="/bots/reference/bot-management-variables/">Bot Management Variables</a> for more details.</li>
</ul>
</li>
<li>
<p><code>clientAcceptEncoding</code> string | null</p>
<ul>
<li>If Cloudflare replaces the value of the <code>Accept-Encoding</code> header, the original value is stored in the <code>clientAcceptEncoding</code> property, for example, <code>&quot;gzip, deflate, br&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>clientQuicRtt</code> number | undefined</p>
<ul>
<li>The smoothed round-trip time (RTT) between Cloudflare and the client for QUIC connections, in milliseconds. Only present when the client connected over QUIC (HTTP/3). For example, <code>42</code>.</li>
</ul>
</li>
<li>
<p><code>clientTcpRtt</code> number | undefined</p>
<ul>
<li>The smoothed round-trip time (RTT) between the client and Cloudflare for TCP connections, in milliseconds. Only present when the client connected over TCP (HTTP/1 and HTTP/2). For example, <code>22</code>.</li>
</ul>
</li>
<li>
<p><code>colo</code> string</p>
<ul>
<li>The three-letter <a href="https://en.wikipedia.org/wiki/IATA_airport_code"><code>IATA</code></a> airport code of the data center that the request hit, for example, <code>&quot;DFW&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>country</code> string | null</p>
<ul>
<li>Country of the incoming request. The two-letter country code in the request. This is the same value as that provided in the <code>CF-IPCountry</code> header, for example, <code>&quot;US&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>edgeL4</code> Object | undefined</p>
<ul>
<li>Layer 4 transport statistics for the connection between the client and Cloudflare. Contains the following property:
<ul>
<li><code>deliveryRate</code> number - The most recent data delivery rate estimate for the connection, in bytes per second. For example, <code>123456</code>.</li>
</ul>
</li>
</ul>
</li>
<li>
<p><code>isEUCountry</code> string | null</p>
<ul>
<li>If the country of the incoming request is in the EU, this will return <code>&quot;1&quot;</code>. Otherwise, this property is either omitted or <code>false</code>.</li>
</ul>
</li>
<li>
<p><code>httpProtocol</code> string</p>
<ul>
<li>HTTP Protocol, for example, <code>&quot;HTTP/2&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>hostMetadata</code> Object | undefined</p>
<ul>
<li>Only populated when the incoming request is from a zone with custom hostname metadata. Refer to the Cloudflare for Platforms documentation for more about what you can add as <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/">custom hostname metadata</a>, and how it is exposed on the <code>hostMetadata</code> field.</li>
</ul>
</li>
<li>
<p><code>requestPriority</code> string | null</p>
<ul>
<li>The browser-requested prioritization information in the request object, for example, <code>&quot;weight=192;exclusive=0;group=3;group-weight=127&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>tlsCipher</code> string</p>
<ul>
<li>The cipher for the connection to Cloudflare, for example, <code>&quot;AEAD-AES128-GCM-SHA256&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>tlsClientAuth</code> Object | null</p>
<ul>
<li>Various details about the client certificate (for mTLS connections). Refer to <a href="/ssl/client-certificates/client-certificate-variables/">Client certificate variables</a> for more details.</li>
</ul>
</li>
<li>
<p><code>tlsClientCiphersSha1</code> string</p>
<ul>
<li>The SHA-1 hash (Base64-encoded) of the cipher suite sent by the client during the TLS handshake, encoded in big-endian format. For example, <code>&quot;GXSPDLP4G3X+prK73a4wBuOaHRc=&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>tlsClientExtensionsSha1</code> string</p>
<ul>
<li>The SHA-1 hash (Base64-encoded) of the TLS client extensions sent during the handshake, encoded in big-endian format. For example, <code>&quot;OWFiM2I5ZDc0YWI0YWYzZmFkMGU0ZjhlYjhiYmVkMjgxNTU5YTU2Mg==&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>tlsClientExtensionsSha1Le</code> string</p>
<ul>
<li>The SHA-1 hash (Base64-encoded) of the TLS client extensions sent during the handshake, encoded in little-endian format. For example, <code>&quot;7zIpdDU5pvFPPBI2/PCzqbaXnRA=&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>tlsClientHelloLength</code> string</p>
<ul>
<li>The length of the client hello message sent in a <a href="https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/">TLS handshake</a>. For example, <code>&quot;508&quot;</code>. Specifically, the length of the bytestring of the client hello.</li>
</ul>
</li>
<li>
<p><code>tlsClientRandom</code> string</p>
<ul>
<li>The value of the 32-byte random value provided by the client in a <a href="https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/">TLS handshake</a>. Refer to <a href="https://datatracker.ietf.org/doc/html/rfc8446#section-4.1.2">RFC 8446</a> for more details.</li>
</ul>
</li>
<li>
<p><code>tlsVersion</code> string</p>
<ul>
<li>The TLS version of the connection to Cloudflare, for example, <code>TLSv1.3</code>.</li>
</ul>
</li>
<li>
<p><code>city</code> string | null</p>
<ul>
<li>City of the incoming request, for example, <code>&quot;Austin&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>continent</code> string | null</p>
<ul>
<li>Continent of the incoming request, for example, <code>&quot;NA&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>latitude</code> string | null</p>
<ul>
<li>Latitude of the incoming request, for example, <code>&quot;30.27130&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>longitude</code> string | null</p>
<ul>
<li>Longitude of the incoming request, for example, <code>&quot;-97.74260&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>postalCode</code> string | null</p>
<ul>
<li>Postal code of the incoming request, for example, <code>&quot;78701&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>metroCode</code> string | null</p>
<ul>
<li>Metro code (DMA) of the incoming request, for example, <code>&quot;635&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>region</code> string | null</p>
<ul>
<li>If known, the <a href="https://en.wikipedia.org/wiki/ISO_3166-2">ISO 3166-2</a> name for the first level region associated with the IP address of the incoming request, for example, <code>&quot;Texas&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>regionCode</code> string | null</p>
<ul>
<li>If known, the <a href="https://en.wikipedia.org/wiki/ISO_3166-2">ISO 3166-2</a> code for the first-level region associated with the IP address of the incoming request, for example, <code>&quot;TX&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>timezone</code> string</p>
<ul>
<li>Timezone of the incoming request, for example, <code>&quot;America/Chicago&quot;</code>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16135.md")
</aside>
<hr />
<h2 id="methods">Methods</h2>
<h3 id="instance-methods">Instance methods</h3>
<p>These methods are only available on an instance of a <code>Request</code> object or through its prototype.</p>
<ul>
<li>
<p><code>clone()</code> : Request</p>
<ul>
<li>Creates a copy of the <code>Request</code> object.</li>
</ul>
</li>
<li>
<p><code>arrayBuffer()</code> : Promise&lt;ArrayBuffer&gt;</p>
<ul>
<li>Returns a promise that resolves with an <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer"><code>ArrayBuffer</code></a> representation of the request body.</li>
</ul>
</li>
<li>
<p><code>formData()</code> : Promise&lt;FormData&gt;</p>
<ul>
<li>Returns a promise that resolves with a <a href="https://developer.mozilla.org/en-US/docs/Web/API/FormData"><code>FormData</code></a> representation of the request body.</li>
</ul>
</li>
<li>
<p><code>json()</code> : Promise&lt;Object&gt;</p>
<ul>
<li>Returns a promise that resolves with a JSON representation of the request body.</li>
</ul>
</li>
<li>
<p><code>text()</code> : Promise&lt;string&gt;</p>
<ul>
<li>Returns a promise that resolves with a string (text) representation of the request body.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="the-request-context">The <code>Request</code> context</h2>
<p>Each time a Worker is invoked by an incoming HTTP request, the <a href="/workers/runtime-apis/handlers/fetch"><code>fetch()</code> handler</a> is called on your Worker. The <code>Request</code> context starts when the <code>fetch()</code> handler is called, and asynchronous tasks (such as making a subrequest using the <a href="/workers/runtime-apis/fetch/"><code>fetch() API</code></a>) can only be run inside the <code>Request</code> context:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;        // Request context starts here&#10;		return new Response(&#x27;Hello World!&#x27;);&#10;	},&#10;};&#10;</code></pre>
<h3 id="when-passing-a-promise-to-fetch-event-respondwith">When passing a promise to fetch event <code>.respondWith()</code></h3>
<p>If you pass a Response promise to the fetch event <code>.respondWith()</code> method, the request context is active during any asynchronous tasks which run before the Response promise has settled. You can pass the event to an async handler, for example:</p>
<pre tabindex="0"><code class="language-js">addEventListener(&quot;fetch&quot;, event =&gt; {&#10;  event.respondWith(eventHandler(event))&#10;})&#10;&#10;// No request context available here&#10;&#10;async function eventHandler(event){&#10;  // Request context available here&#10;  return new Response(&quot;Hello, Workers!&quot;)&#10;}&#10;</code></pre>
<h3 id="errors-when-attempting-to-access-an-inactive-request-context">Errors when attempting to access an inactive <code>Request</code> context</h3>
<p>Any attempt to use APIs such as <code>fetch()</code> or access the <code>Request</code> context during script startup will throw an exception:</p>
<pre tabindex="0"><code class="language-js">const promise = fetch(&quot;https://example.com/&quot;) // Error&#10;async function eventHandler(event){..}&#10;</code></pre>
<p>This code snippet will throw during script startup, and the <code>&quot;fetch&quot;</code> event listener will never be registered.</p>
<hr />
<h3 id="set-the-content-length-header">Set the <code>Content-Length</code> header</h3>
<p>The <code>Content-Length</code> header will be automatically set by the runtime based on whatever the data source for the <code>Request</code> is. Any value manually set by user code in the <code>Headers</code> will be ignored. To have a <code>Content-Length</code> header with a specific value specified, the <code>body</code> of the <code>Request</code> must be either a <code>FixedLengthStream</code> or a fixed-length value just as a string or <code>TypedArray</code>.</p>
<p>A <code>FixedLengthStream</code> is an identity <code>TransformStream</code> that permits only a fixed number of bytes to be written to it.</p>
<pre tabindex="0"><code class="language-js">  const { writable, readable } = new FixedLengthStream(11);&#10;&#10;  const enc = new TextEncoder();&#10;  const writer = writable.getWriter();&#10;  writer.write(enc.encode(&quot;hello world&quot;));&#10;  writer.end();&#10;&#10;  const req = new Request(&#x27;https://example.org&#x27;, { method: &#x27;POST&#x27;, body: readable });&#10;</code></pre>
<p>Using any other type of <code>ReadableStream</code> as the body of a request will result in Chunked-Encoding being used.</p>
<hr />
<h2 id="differences">Differences</h2>
<p>The Workers implementation of the <code>Request</code> interface includes several extensions to the web standard <code>Request</code> API. These differences are intentional and provide additional functionality specific to the Workers runtime.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="typescript-users">TypeScript users</h3>
@markup("md", "content/.markup/bodies/16134.md")
</aside>
<h3 id="the-cf-property">The <code>cf</code> property</h3>
<p>Workers adds a <code>cf</code> property to the <code>Request</code> object that contains Cloudflare-specific metadata about the incoming request. This property is not part of the web standard, and is only available in the Workers runtime. Refer to <a href="#incomingrequestcfproperties"><code>IncomingRequestCfProperties</code></a> for details.</p>
<h3 id="the-headers-property">The <code>headers</code> property</h3>
<p>The <code>headers</code> property returns a Workers-specific <a href="/workers/runtime-apis/headers/"><code>Headers</code></a> object that includes additional methods like <code>getAll()</code> for <code>Set-Cookie</code> headers. Refer to the <a href="/workers/runtime-apis/headers/#differences">Headers documentation</a> for details on how the Workers <code>Headers</code> implementation differs from the web standard.</p>
<h3 id="immutability">Immutability</h3>
<p>Incoming <code>Request</code> objects passed to the <a href="/workers/runtime-apis/handlers/fetch/"><code>fetch()</code> handler</a> are immutable. To modify properties of an incoming request, you must create a new <code>Request</code> object.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/examples/modify-request-property/">Examples: Modify request property</a></li>
<li><a href="/workers/examples/accessing-the-cloudflare-object/">Examples: Accessing the <code>cf</code> object</a></li>
<li><a href="/workers/runtime-apis/response/">Reference: <code>Response</code></a></li>
<li>Write your Worker code in <a href="/workers/reference/migrate-to-module-workers/">ES modules syntax</a> for an optimized experience.</li>
</ul>
