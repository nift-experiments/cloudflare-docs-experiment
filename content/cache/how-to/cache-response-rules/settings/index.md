---
cp9:
  canonical: https://developers.cloudflare.com/cache/how-to/cache-response-rules/settings/
  description: Available settings for cache response rules.
  full_title: Cache Response Rules settings · Cloudflare Cache (CDN) docs
  head_html: <title>Cache Response Rules settings · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Available settings for cache response rules."><link rel="canonical" href="https://developers.cloudflare.com/cache/how-to/cache-response-rules/settings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/how-to/cache-response-rules/settings/index.md"><meta property="og:title" content="Cache Response Rules settings · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Available settings for cache response rules."><meta property="og:url" content="https://developers.cloudflare.com/cache/how-to/cache-response-rules/settings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/how-to/cache-response-rules/settings/#page","headline":"Cache Response Rules settings \u00b7 Cloudflare Cache (CDN) docs","description":"Available settings for cache response rules.","url":"https://developers.cloudflare.com/cache/how-to/cache-response-rules/settings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/how-to/cache-response-rules/settings/
  schema: 1
---
<p>These are the settings that you can configure when creating a Cache Response Rule. Because Cache Response Rules execute after Cloudflare receives the origin response, both request and response fields are available for rule matching.</p>
<h2 id="expression-fields">Expression fields</h2>
<h3 id="request-fields">Request fields</h3>
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
<td><code>http.cookie</code></td>
<td>String</td>
<td>Full cookie header value</td>
</tr>
<tr>
<td><code>http.host</code></td>
<td>String</td>
<td>The HTTP Host header</td>
</tr>
<tr>
<td><code>http.referer</code></td>
<td>String</td>
<td>The HTTP Referer header</td>
</tr>
<tr>
<td><code>http.user_agent</code></td>
<td>String</td>
<td>The HTTP User-Agent header</td>
</tr>
<tr>
<td><code>http.request.method</code></td>
<td>String</td>
<td>The HTTP request method</td>
</tr>
<tr>
<td><code>http.request.uri</code></td>
<td>String</td>
<td>The request URI</td>
</tr>
<tr>
<td><code>http.request.uri.path</code></td>
<td>String</td>
<td>The URI path</td>
</tr>
<tr>
<td><code>http.request.uri.path.basename</code></td>
<td>String</td>
<td>The basename of the URI path</td>
</tr>
<tr>
<td><code>http.request.uri.path.extension</code></td>
<td>String</td>
<td>The file extension from the URI path</td>
</tr>
<tr>
<td><code>http.request.uri.query</code></td>
<td>String</td>
<td>The query string</td>
</tr>
<tr>
<td><code>http.request.uri.args</code></td>
<td>Map</td>
<td>Query string arguments as key-value pairs</td>
</tr>
<tr>
<td><code>http.request.uri.args.names</code></td>
<td>Array</td>
<td>Query string argument names</td>
</tr>
<tr>
<td><code>http.request.uri.args.values</code></td>
<td>Array</td>
<td>Query string argument values</td>
</tr>
<tr>
<td><code>http.request.full_uri</code></td>
<td>String</td>
<td>The full request URI including scheme and host</td>
</tr>
<tr>
<td><code>http.request.headers</code></td>
<td>Map</td>
<td>Request headers as key-value pairs</td>
</tr>
<tr>
<td><code>http.request.headers.names</code></td>
<td>Array</td>
<td>Request header names</td>
</tr>
<tr>
<td><code>http.request.headers.values</code></td>
<td>Array</td>
<td>Request header values</td>
</tr>
<tr>
<td><code>http.request.cookies</code></td>
<td>Map</td>
<td>Parsed cookies as key-value pairs</td>
</tr>
<tr>
<td><code>http.request.accepted_languages</code></td>
<td>Array</td>
<td>Parsed Accept-Language header values</td>
</tr>
</tbody>
</table>
<h3 id="response-fields">Response fields</h3>
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
<td><code>http.response.code</code></td>
<td>Integer</td>
<td>The HTTP response status code from the origin</td>
</tr>
<tr>
<td><code>http.response.headers</code></td>
<td>Map</td>
<td>Response headers as key-value pairs</td>
</tr>
<tr>
<td><code>http.response.headers.names</code></td>
<td>Array</td>
<td>Response header names</td>
</tr>
<tr>
<td><code>http.response.headers.values</code></td>
<td>Array</td>
<td>Response header values</td>
</tr>
</tbody>
</table>
<p>If you select the <a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-editor">Edit expression</a> option, you can enter any of the above response fields.</p>
<h2 id="functions">Functions</h2>
<p>The following functions are available in this phase:</p>
<ul>
<li>all</li>
<li>any</li>
<li>concat</li>
<li>decode_base64</li>
<li>ends_with</li>
<li>len</li>
<li>lookup_json_integer</li>
<li>lookup_json_string</li>
<li>lower</li>
<li>regex_replace</li>
<li>remove_bytes</li>
<li>remove_query_args</li>
<li>split</li>
<li>starts_with</li>
<li>substring</li>
<li>to_string</li>
<li>upper</li>
<li>url_decode</li>
<li>wildcard_replace</li>
</ul>
<p>For descriptions of each function, refer to <a href="/ruleset-engine/rules-language/functions/">Functions</a>.</p>
<h2 id="operators">Operators</h2>
<p>For the full list of operators, refer to <a href="/ruleset-engine/rules-language/operators/">Operators</a>.</p>
<h2 id="available-actions">Available actions</h2>
<p>Cache Response Rules support three actions:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>set_cache_settings</code></td>
<td>Strip headers (ETags, Set-Cookie, Last-Modified) from the origin response before caching.</td>
</tr>
<tr>
<td><code>set_cache_tags</code></td>
<td>Add, remove, or set cache tags on the response for targeted purging.</td>
</tr>
<tr>
<td><code>set_cache_control</code></td>
<td>Modify Cache-Control header directives in the origin response.</td>
</tr>
</tbody>
</table>
<hr />
<h3 id="action-set-cache-settings">Action: set_cache_settings</h3>
<p>Configures settings related to caching on the origin response. The following parameters are available:</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>strip_etags</code></td>
<td>Boolean</td>
<td>Strip ETag headers from the origin response before caching.</td>
</tr>
<tr>
<td><code>strip_set_cookie</code></td>
<td>Boolean</td>
<td>Strip Set-Cookie headers from the origin response before caching.</td>
</tr>
<tr>
<td><code>strip_last_modified</code></td>
<td>Boolean</td>
<td>Strip Last-Modified headers from the origin response before caching.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3918.md")
</aside>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3919.md")
</div></details>
<hr />
<h3 id="action-set-cache-tags">Action: set_cache_tags</h3>
<p>Modifies the cache tags associated with the response. Cache tags can be used for targeted <a href="/cache/how-to/purge-cache/purge-by-tags/">cache purging</a>.</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>operation</code></td>
<td>String</td>
<td><strong>Required.</strong> One of: <code>add</code>, <code>remove</code>, <code>set</code>.</td>
</tr>
<tr>
<td><code>values</code></td>
<td>Array</td>
<td>A list of cache tag strings. Mutually exclusive with <code>expression</code>.</td>
</tr>
<tr>
<td><code>expression</code></td>
<td>String</td>
<td>An expression that evaluates to an array of cache tags. Mutually exclusive with <code>values</code>.</td>
</tr>
</tbody>
</table>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3920.md")
</div></details>
<hr />
<h3 id="action-set-cache-control">Action: set_cache_control</h3>
<p>Modifies Cache-Control header directives in the origin response.</p>
<h4 id="supported-directives">Supported directives</h4>
<p><strong>Directives with duration value (seconds):</strong></p>
<ul>
<li><code>max-age</code></li>
<li><code>s-maxage</code></li>
<li><code>stale-if-error</code></li>
<li><code>stale-while-revalidate</code></li>
</ul>
<p><strong>Directives with optional qualifiers (header names):</strong></p>
<ul>
<li><code>private</code></li>
<li><code>no-cache</code></li>
</ul>
<p><strong>Boolean directives:</strong></p>
<ul>
<li><code>no-store</code></li>
<li><code>no-transform</code></li>
<li><code>must-revalidate</code></li>
<li><code>proxy-revalidate</code></li>
<li><code>must-understand</code></li>
<li><code>public</code></li>
<li><code>immutable</code></li>
</ul>
<h4 id="directive-configuration">Directive configuration</h4>
<p>The available parameters depend on the directive type.</p>
<h5 id="directives-with-duration-value">Directives with duration value</h5>
<p>Applies to <code>max-age</code>, <code>s-maxage</code>, <code>stale-if-error</code>, and <code>stale-while-revalidate</code>.</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>operation</code></td>
<td>String</td>
<td><strong>Required.</strong> <code>set</code> or <code>remove</code>.</td>
</tr>
<tr>
<td><code>cloudflare_only</code></td>
<td>Boolean</td>
<td>When enabled, this setting only affects how Cloudflare caches your content. Your visitors still receive the original directive.</td>
</tr>
<tr>
<td><code>value</code></td>
<td>Integer</td>
<td>Duration in seconds. <strong>Required when operation is <code>set</code>.</strong></td>
</tr>
</tbody>
</table>
<h5 id="directives-with-optional-qualifiers">Directives with optional qualifiers</h5>
<p>Applies to <code>private</code> and <code>no-cache</code>.</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>operation</code></td>
<td>String</td>
<td><strong>Required.</strong> <code>set</code> or <code>remove</code>.</td>
</tr>
<tr>
<td><code>cloudflare_only</code></td>
<td>Boolean</td>
<td>When enabled, this setting only affects how Cloudflare caches your content. Your visitors still receive the original directive.</td>
</tr>
<tr>
<td><code>qualifiers</code></td>
<td>Array</td>
<td>Optional list of header names to qualify the directive.</td>
</tr>
</tbody>
</table>
<h5 id="boolean-directives">Boolean directives</h5>
<p>Applies to <code>no-store</code>, <code>no-transform</code>, <code>must-revalidate</code>, <code>proxy-revalidate</code>, <code>must-understand</code>, <code>public</code>, and <code>immutable</code>.</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>operation</code></td>
<td>String</td>
<td><strong>Required.</strong> <code>set</code> or <code>remove</code>.</td>
</tr>
<tr>
<td><code>cloudflare_only</code></td>
<td>Boolean</td>
<td>When enabled, this setting only affects how Cloudflare caches your content. Your visitors still receive the original directive.</td>
</tr>
</tbody>
</table>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3921.md")
</div></details>
