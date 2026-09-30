---
cp9:
  canonical: https://developers.cloudflare.com/cache/how-to/cache-keys/
  description: Customize cache keys to control how Cloudflare stores cached resources.
  full_title: Cache Keys · Cloudflare Cache (CDN) docs
  head_html: <title>Cache Keys · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Customize cache keys to control how Cloudflare stores cached resources."><link rel="canonical" href="https://developers.cloudflare.com/cache/how-to/cache-keys/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/how-to/cache-keys/index.md"><meta property="og:title" content="Cache Keys · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Customize cache keys to control how Cloudflare stores cached resources."><meta property="og:url" content="https://developers.cloudflare.com/cache/how-to/cache-keys/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cache / CDN"><meta name="pcx_tags" content="CORS,Geolocation,Headers,Cookies"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/how-to/cache-keys/#page","headline":"Cache Keys \u00b7 Cloudflare Cache (CDN) docs","description":"Customize cache keys to control how Cloudflare stores cached resources.","url":"https://developers.cloudflare.com/cache/how-to/cache-keys/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["CORS","Geolocation","Headers","Cookies"]}</script>
  markdown: true
  noindex: false
  route: /cache/how-to/cache-keys/
  schema: 1
---
<p>A Cache Key is an identifier that Cloudflare uses for a file in our cache, and the Cache Key Template defines the identifier for a given HTTP request.</p>
<p>A default cache key includes:</p>
<ol>
<li>Full URL:
<ul>
<li>scheme - could be HTTP or HTTPS.</li>
<li>host - for example, <code>www.cloudflare.com</code></li>
<li>URI with query string - for example, <code>/logo.jpg?utm_source=newsletter</code></li>
</ul>
</li>
<li>Origin header sent by client (for CORS support).</li>
<li><code>x-http-method-override</code>, <code>x-http-method</code>, and <code>x-method-override</code> headers.</li>
<li><code>x-forwarded-host</code>, <code>x-host</code>, <code>x-forwarded-scheme</code> (unless http or https), <code>x-original-url</code>, <code>x-rewrite-url</code>, and <code>forwarded</code> headers.</li>
</ol>
<h2 id="create-custom-cache-keys">Create custom cache keys</h2>
<p>Custom cache keys let you precisely set the cacheability setting for any resource. They provide the benefit of more control, though they may reduce your cache hit rate and result in cache sharding:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Cache Rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create rule</strong>.</li>
<li>Under <strong>When incoming requests match</strong>, define the <a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-builder">rule expression</a>.</li>
<li>Under <strong>Then</strong>, in the <strong>Cache eligibility</strong> section, select <strong>Eligible for cache</strong>.</li>
<li>Add the <strong>Cache Key</strong> setting to the rule and select the appropriate <strong>Query String</strong> setting.</li>
<li>You can also select settings for <strong>Headers</strong>, <strong>Cookie</strong>, <strong>Host</strong>, and <strong>User</strong>.</li>
<li>To save and deploy your rule, select <strong>Deploy</strong>. If you are not ready to deploy your rule, select <strong>Save as Draft</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3812.md")
</aside>
<h2 id="cache-key-template">Cache Key Template</h2>
<p>There are a couple of common reasons to change the Cache Key Template. You might change the Cache Key Template to:</p>
<ul>
<li>Fragment the cache so one URL is stored in multiple files. For example, to store different files based on a specific query string in the URL.</li>
<li>Consolidate the cache so different HTTP requests are stored in the same file. For example, to remove the Origin header added to Cloudflare Cache Keys by default.</li>
</ul>
<h3 id="impact-of-ssl-settings-on-cache-behavior">Impact of SSL settings on Cache behavior</h3>
<p>Cloudflare's <code>$scheme</code> variable plays a key role in caching behavior, but its meaning varies depending on the cache key type:</p>
<ul>
<li>
<p><strong>Default Cache Key</strong>: <code>$scheme</code> refers to the <strong>origin scheme</strong> — the protocol Cloudflare uses to connect to your origin server (HTTP or HTTPS). In this configuration, changes to your SSL settings (for example, switching from Flexible to Full) alter the origin scheme. Because the cache key includes the origin scheme, such changes trigger a cache bust, requiring Cloudflare to fetch content again from the origin.</p>
</li>
<li>
<p><strong>Custom Cache Key</strong>: <code>$scheme</code> refers to the <strong>visitor's scheme</strong> — the protocol used by the client making the request to Cloudflare. In this case, SSL setting changes do not impact the cache key unless the origin scheme is explicitly included in your custom configuration.</p>
</li>
</ul>
<p>For example, with Flexible SSL, Cloudflare always connects to the origin over HTTP, regardless of whether the visitor uses HTTP or HTTPS. This results in the same cache key for both protocols under the default configuration.</p>
<p>Be aware that changes in the SSL setting can lead to cache invalidation when using the default cache key:</p>
<ul>
<li>
<p>Switching from <strong>Off</strong> to <strong>Full</strong>, <strong>Full (strict)</strong>, or <strong>Strict</strong> updates the origin scheme from HTTP to HTTPS, resulting in a cache bust.</p>
</li>
<li>
<p>Moving from <strong>Flexible</strong> to <strong>Full</strong>, <strong>Full (strict)</strong>, or <strong>Strict</strong> similarly changes the origin scheme to HTTPS and causes a cache bust.</p>
</li>
</ul>
<p>Understanding how <code>$scheme</code> interacts with your caching configuration is essential when modifying SSL modes to avoid unexpected cache behavior.</p>
<h3 id="cache-level-ignore-query-string">Cache Level: Ignore Query String</h3>
<p>A <a href="/cache/how-to/set-caching-levels/">Cache Level</a> of Ignore Query String creates a Cache Key that includes all the elements in the default cache key, except for the query string in the URI that is no longer included. For instance, a request for <code>http://example.com/file.jpg?something=123</code> and a request for <code>http://example.com/file.jpg?something=789</code> will have the same cache key, in this case.</p>
<h2 id="cache-key-settings">Cache Key Settings</h2>
<p>The following fields control the Cache Key Template.</p>
<h3 id="query-string">Query String</h3>
<p>The query string controls which URL query string parameters go into the Cache Key. You can <code>include</code> specific query string parameters or <code>exclude</code> them using the respective fields. When you include a query string parameter, the <code>value</code> of the query string parameter is used in the Cache Key.</p>
<h4 id="example">Example</h4>
<p>If you include the query string foo in a URL like <code>https://www.example.com/?foo=bar</code>, then bar appears in the Cache Key. Exactly one of <code>include</code> or <code>exclude</code> is expected.</p>
<h4 id="usage-notes">Usage notes</h4>
<ul>
<li>To include all query string parameters (the default behavior), use include: <code>&quot;\*&quot;</code></li>
<li>To ignore query strings, use exclude: <code>&quot;\*&quot;</code></li>
<li>To include most query string parameters but exclude a few, use the exclude field which assumes the other query string parameters are included.</li>
</ul>
<h3 id="headers">Headers</h3>
<p>Headers control which headers go into the Cache Key. Similar to Query String, you can include specific headers or exclude default headers.</p>
<p>When you include a header, the header value is included in the Cache Key. For example, if an HTTP request contains an HTTP header like <code>X-Auth-API-key: 12345</code>, and you include the <code>X-Auth-API-Key header</code> in your Cache Key Template, then <code>12345</code> appears in the Cache Key.</p>
<p>In the <strong>Include headers and selected values</strong> section, you can add header names and their values to the cache key. For custom headers, values are optional, but for the following restricted headers, you must include one to 10 specific values:</p>
<ul>
<li><code>accept</code></li>
<li><code>accept-charset</code></li>
<li><code>accept-encoding</code></li>
<li><code>accept-datetime</code></li>
<li><code>accept-language</code></li>
<li><code>referer</code></li>
<li><code>user-agent</code></li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3811.md")
</aside>
<p>To check for the presence of a header without including its actual value, use the <strong>Check presence of</strong> option.</p>
<p>Currently, you can only exclude the <code>Origin</code> header. The <code>Origin</code> header is always included unless explicitly excluded. Including the <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Origin">Origin header</a> in the Cache Key is important to enforce <a href="https://developer.mozilla.org/en-US/docs/Glossary/CORS">CORS</a>.</p>
<p>Additionally, you cannot include the following headers:</p>
<ul>
<li>Headers that re-implement cache or proxy features
<ul>
<li><code>connection</code></li>
<li><code>content-length</code></li>
<li><code>cache-control</code></li>
<li><code>if-match</code></li>
<li><code>if-modified-since</code></li>
<li><code>if-none-match</code></li>
<li><code>if-unmodified-since</code></li>
<li><code>range</code></li>
<li><code>upgrade</code></li>
</ul>
</li>
<li>Headers that are covered by other Cache Key features
<ul>
<li><code>cookie</code></li>
<li><code>host</code></li>
</ul>
</li>
<li>Headers that are specific to Cloudflare and prefixed with <code>cf-</code>, for example, <code>cf-ray</code></li>
<li>Headers that are already included in the custom Cache Key template, for example, <code>origin</code></li>
</ul>
<h3 id="host">Host</h3>
<p>Host determines which host header to include in the Cache Key.</p>
<ul>
<li>If <code>Use original host</code> (<code>resolved: false</code> in the API), Cloudflare includes the <code>Host</code> header in the HTTP request sent to the origin.</li>
<li>If <code>Resolved host</code> (<code>resolved: true</code> in the API), Cloudflare includes the <code>Host</code> header that was resolved to get the <code>origin IP</code> for the request. The <code>Host</code> header may be different from the header actually sent if it has been changed with an <a href="/rules/origin-rules/features/#dns-record">Origin Rule</a>.</li>
</ul>
<h3 id="cookie">Cookie</h3>
<p>Like <code>query_string</code> or <code>header</code>, <code>cookie</code> controls which cookies appear in the Cache Key. You can either include the cookie value or check for the presence of a particular cookie.</p>
<h4 id="usage-notes-1">Usage notes</h4>
<p>You cannot include cookies specific to Cloudflare. Cloudflare cookies are prefixed with <code>__cf</code>, for example, <code>__cflb</code></p>
<h3 id="user-features">User features</h3>
<p>User feature fields add features about the end-user (client) into the Cache Key.</p>
<ul>
<li><code>device_type</code> classifies a request as <code>mobile</code>, <code>desktop</code>, or <code>tablet</code> based on the User Agent</li>
<li><code>geo</code> includes the client’s country, derived from the IP address</li>
<li><code>lang</code> includes the first language code contained in the <code>Accept-Language</code> header sent by the client</li>
</ul>
<h2 id="availability">Availability</h2>
<p>Cache keys options availability varies according to your plan.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cache deception armor</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Cache by device type</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Ignore query string</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Sort query string</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Query string</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Headers</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Cookie</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Host</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>User features</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>You can use <a href="/rules/trace-request/">Cloudflare Trace</a> to find which Cache Key settings were applied to your request. When you send a request through the Trace tool, if the request was served from cache, it will show a cache hit in the <strong>Cache Parameters</strong> section. Then select <strong>View parameter detail</strong> to see exactly which Cache Key properties were used.</p>
<h2 id="limitations">Limitations</h2>
<p>The <a href="/speed/optimization/content/prefetch-urls/">Prefetch</a> feature is not compatible with the <a href="/cache/how-to/cache-rules/examples/custom-cache-key/">Custom Cache Keys</a>. With <a href="/cache/how-to/cache-rules/">Cache Rules</a>, the custom cache key is used to cache all assets. However, Prefetch always uses the default cache key. This results in a key mismatch.</p>
