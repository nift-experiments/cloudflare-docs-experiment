---
cp9:
  canonical: https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/how-it-works/
  description: How Bulk Redirects evaluate and match incoming requests.
  full_title: How Bulk Redirects work · Cloudflare Rules docs
  head_html: <title>How Bulk Redirects work · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="How Bulk Redirects evaluate and match incoming requests."><link rel="canonical" href="https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/how-it-works/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/how-it-works/index.md"><meta property="og:title" content="How Bulk Redirects work · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Bulk Redirects evaluate and match incoming requests."><meta property="og:url" content="https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/how-it-works/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Rules"><meta name="pcx_tags" content="Redirects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/how-it-works/#page","headline":"How Bulk Redirects work \u00b7 Cloudflare Rules docs","description":"How Bulk Redirects evaluate and match incoming requests.","url":"https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/how-it-works/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Redirects"]}</script>
  markdown: true
  noindex: false
  route: /rules/url-forwarding/bulk-redirects/how-it-works/
  schema: 1
---
<p>When a request reaches Cloudflare, Bulk Redirects are evaluated before the request is sent to your origin server. Cloudflare checks all URL redirects of each Bulk Redirect List that is enabled by a Bulk Redirect Rule.</p>
<p>If there is a match for a URL redirect according to the <a href="#url-matching-algorithm">URL matching algorithm</a>, the redirect action is performed immediately according to the URL redirect configuration parameters. Cloudflare performs no further processing once a redirect action has been executed.</p>
<h2 id="matching-the-source-url-of-redirects">Matching the source URL of redirects</h2>
<p>The following URL redirect parameters control the matching behavior between the request URL and source URLs of the configured (and enabled) URL redirects:</p>
<ul>
<li><strong>Subpath matching</strong> <span class="nb-metainfo">(default: false)</span>
<ul>
<li>
<p>When <code>true</code>, the URL redirect applies not only to the exact source path, but also to all paths under it. For example, consider the following source and target URLs of a URL redirect:</p>
<ul>
<li>Source URL: <code>https://example.com/foo/</code></li>
<li>Target URL: <code>https://example.com/qux/</code></li>
</ul>
</li>
<li>
<p>With this configuration and <strong>Subpath matching</strong> enabled, an incoming request to <code>example.com/foo/bar</code> will be redirected to <code>https://example.com/qux/bar</code>.</p>
</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13212.md")
</aside>
<ul>
<li><strong>Include subdomains</strong> <span class="nb-metainfo">(default: false)</span>
<ul>
<li>
<p>When <code>true</code>, the URL redirect matches not only the exact hostname in the source URL, but also any of its subdomains. For example, consider the following source and target URLs of a URL redirect:</p>
<ul>
<li>Source URL: <code>https://example.com/about</code></li>
<li>Target URL: <code>https://example.com/newpage</code></li>
</ul>
</li>
<li>
<p>With this configuration and <strong>Includes subdomains</strong> enabled, incoming requests to <code>http://a.example.com/about</code> and <code>http://a.b.example.com/about</code> would also match, in addition to the specified domain with no subdomain (<code>https://example.com/about</code>).</p>
</li>
</ul>
</li>
</ul>
<p>For detailed information on these parameters, refer to <a href="/rules/url-forwarding/bulk-redirects/reference/parameters/">URL redirect parameters</a>.</p>
<h2 id="configuring-the-path-and-query-string-behavior">Configuring the path and query string behavior</h2>
<p>The following parameters configure how Cloudflare determines the path and query string of the final target URL:</p>
<ul>
<li>
<p><strong>Preserve query string</strong> <span class="nb-metainfo">(default: false)</span></p>
<ul>
<li>
<p>When <code>true</code>, the final target URL keeps the query string of the original request. For example, consider the following source and target URLs of a URL redirect:</p>
<ul>
<li>Source URL: <code>https://example.com/about</code></li>
<li>Target URL: <code>https://example.com/newpage</code></li>
</ul>
</li>
<li>
<p>With this configuration and <strong>Preserve query string</strong> enabled, an incoming request to <code>http://example.com/about?q=term</code> would be redirected to <code>https://example.com/newpage?q=term</code>. If <strong>Preserve query string</strong> is disabled, the same incoming request would be redirected to <code>https://example.com/newpage</code>.</p>
</li>
</ul>
</li>
<li>
<p><strong>Preserve path suffix</strong> <span class="nb-metainfo">(default: true)</span></p>
<ul>
<li>
<p>When <code>true</code>, the final target URL includes the remaining path segments (the parts of the request path that did not match the URL redirect's source URL).</p>
</li>
<li>
<p>When <strong>Subpath matching</strong> is enabled, the path that was not matched is copied over to the final target URL. For example, consider the following source and target URLs of a URL redirect:</p>
<ul>
<li>Source URL: <code>https://example.com/a/</code></li>
<li>Target URL: <code>https://example.com/b/</code></li>
</ul>
</li>
<li>
<p>An incoming request to <code>https://example.com/a/foo</code> will be redirected to <code>https://example.com/b/foo</code>.</p>
</li>
<li>
<p>If you set <strong>Preserve path suffix</strong> to <code>false</code>, the same request will still match the redirect, but it will be redirected to <code>https://example.com/b/</code>.</p>
</li>
</ul>
</li>
</ul>
<p>For detailed information on these parameters, refer to <a href="/rules/url-forwarding/bulk-redirects/reference/parameters/">URL redirect parameters</a>.</p>
<h2 id="url-matching-algorithm">URL matching algorithm</h2>
<p>The URL of an incoming request matches a URL redirect in a list if:</p>
<ol>
<li>
<p>The scheme (<code>http</code> or <code>https</code>) is the same as the source URL of the URL redirect definition. Source URLs with no scheme will match both <code>http</code> and <code>https</code>.</p>
</li>
<li>
<p>The hostname is the same as the hostname in the source URL of the URL redirect definition. If <strong>Include subdomains</strong> is enabled, the subdomains of the hostname in the redirect definition will also match.</p>
</li>
<li>
<p>The path is the same as the source URL. If <strong>Subpath matching</strong> is enabled, Cloudflare also considers the subpaths of the path in the URL redirect's source URL when determining if there is a match. For example, a URL redirect with its source URL defined as <code>example.com/blog</code> will also match requests to <code>example.com/blog/foo</code> and <code>example.com/blog/bar</code>.</p>
</li>
</ol>
<h3 id="determining-the-url-redirect-to-apply">Determining the URL redirect to apply</h3>
<p>If multiple URL redirects can apply, then the redirect that wins is determined by the following rules:</p>
<ol>
<li>
<p>Given two URL redirects with <strong>Subpath matching</strong> enabled, the URL redirect with the most specific path wins over the other URL redirect.<br/>
If there are two URL redirects with source URL paths <code>/folder</code> and <code>/folder/subfolder</code>, an incoming request for the <code>/folder/subfolder/item</code> URL path will match the second redirect (<code>/folder/subfolder</code>) because it is more specific.</p>
</li>
<li>
<p>URL redirects with the exact hostname win over URL redirects with the <strong>Include subdomains</strong> option enabled.</p>
</li>
<li>
<p>Given two URL redirects with <strong>Include subdomains</strong> enabled, the URL with the most specific domain wins over the other URL redirect.<br/>
If there are two URL redirects with source URL hostnames <code>bar.com</code> and <code>foo.bar.com</code>, an incoming request to <code>qux.foo.bar.com</code> will match the second redirect (<code>foo.bar.com</code>) because it is more specific.</p>
</li>
<li>
<p>URL redirects with a specific scheme (either <code>http</code> or <code>https</code>) win over URL redirects that match both schemes.</p>
</li>
</ol>
