---
cp9:
  canonical: https://developers.cloudflare.com/cache/how-to/cache-rules/order/
  description: How Cache Rules are ordered and which rule takes priority.
  full_title: Order and priority · Cloudflare Cache (CDN) docs
  head_html: <title>Order and priority · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="How Cache Rules are ordered and which rule takes priority."><link rel="canonical" href="https://developers.cloudflare.com/cache/how-to/cache-rules/order/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/how-to/cache-rules/order/index.md"><meta property="og:title" content="Order and priority · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Cache Rules are ordered and which rule takes priority."><meta property="og:url" content="https://developers.cloudflare.com/cache/how-to/cache-rules/order/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/how-to/cache-rules/order/#page","headline":"Order and priority \u00b7 Cloudflare Cache (CDN) docs","description":"How Cache Rules are ordered and which rule takes priority.","url":"https://developers.cloudflare.com/cache/how-to/cache-rules/order/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/how-to/cache-rules/order/
  schema: 1
---
<p>Cache rules affect requests differently from Page Rules. This is how they are applied:</p>
<ol>
<li>
<p>Cache Rules are stackable. This means that multiple matching rules can be combined and applied to the same request. For example, if multiple cache rules match the same URL, then the features set in those cache rules will all be applied in order. If several matching rules set a value for the same setting, the value in the last matching rule wins. For an example of a similar scenario where multiple rules match, refer to the <a href="/rules/origin-rules/faq/#what-happens-if-more-than-one-origin-rule-matches-the-current-request">Origin Rules FAQ</a>.</p>
</li>
<li>
<p>For conflicting settings (for example, bypass cache versus eligible for cache), the last matching rule wins. For example, if cache rule #1 is set to cache everything on <code>example.com/images</code> and cache rule #2 is set to bypass cache on <code>example.com</code>, then cache will be bypassed for all URLs that match <code>example.com</code>, since rule #2 is the last matching rule.</p>
</li>
<li>
<p>If you have Page Rules implemented for caching on the same path, Cache Rules will take precedence by design.</p>
</li>
<li>
<p>Cache rules can be more specific than website-wide settings in the cache configuration tab, so they take precedence over website-wide settings on requests they match against. For example, if browser cache TTL is set to 4 hours for the entire website <code>example.com</code> and there is a cache rule matching requests with a path of <code>/feed</code> setting browser cache TTL to 10 seconds, the cache rule will override the website-wide setting for requests to <code>https://example.com/feed</code>.</p>
</li>
</ol>
<h2 id="execution-order-of-rules-products">Execution order of Rules products</h2>
<p>The execution order of Rules features is the following:</p>
<ul>
<li><a href="/rules/url-forwarding/single-redirects/">Single Redirects</a></li>
<li><a href="/rules/transform/url-rewrite/">URL Rewrite Rules</a></li>
<li><a href="/rules/configuration-rules/">Configuration Rules</a></li>
<li><a href="/rules/origin-rules/">Origin Rules</a></li>
<li><a href="/rules/url-forwarding/bulk-redirects/">Bulk Redirects</a></li>
<li><a href="/rules/transform/managed-transforms/">Managed Transforms</a></li>
<li><a href="/rules/transform/request-header-modification/">Request Header Transform Rules</a></li>
<li><a href="/cache/how-to/cache-rules/">Cache Rules</a></li>
<li><a href="/rules/snippets/">Snippets</a></li>
<li><a href="/rules/cloud-connector/">Cloud Connector</a></li>
</ul>
<p>The different types of rules listed above will take precedence over <a href="/rules/page-rules/">Page Rules</a>. This means that Page Rules will be overridden if there is a match for both Page Rules and the Rules products listed above.</p>
<p>Generally speaking, for <a href="/ruleset-engine/rules-language/actions/">non-terminating actions</a> the last change made by rules in the same <a href="/ruleset-engine/about/phases/">phase</a> will win (later rules can overwrite changes done by previous rules). However, for terminating actions (<em>Block</em>, <em>Redirect</em>, or one of the challenge actions), rule evaluation will stop and the action will be executed immediately.</p>
<p>For example, if multiple rules with the <em>Redirect</em> action match, Cloudflare will always use the URL redirect of the first rule that matches. Also, if you configure URL redirects using different Cloudflare products (Single Redirects and Bulk Redirects), the product executed first will apply, if there is a rule match (in this case, Single Redirects).</p>
<p>Refer to the <a href="/ruleset-engine/reference/phases-list/">Phases list</a> for the product execution order.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3906.md")
</aside>
