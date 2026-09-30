---
cp9:
  canonical: https://developers.cloudflare.com/rules/url-forwarding/single-redirects/settings/
  description: Available settings for Single Redirect rules.
  full_title: Single Redirects settings · Cloudflare Rules docs
  head_html: <title>Single Redirects settings · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Available settings for Single Redirect rules."><link rel="canonical" href="https://developers.cloudflare.com/rules/url-forwarding/single-redirects/settings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/url-forwarding/single-redirects/settings/index.md"><meta property="og:title" content="Single Redirects settings · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Available settings for Single Redirect rules."><meta property="og:url" content="https://developers.cloudflare.com/rules/url-forwarding/single-redirects/settings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Rules"><meta name="pcx_tags" content="Redirects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/url-forwarding/single-redirects/settings/#page","headline":"Single Redirects settings \u00b7 Cloudflare Rules docs","description":"Available settings for Single Redirect rules.","url":"https://developers.cloudflare.com/rules/url-forwarding/single-redirects/settings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Redirects"]}</script>
  markdown: true
  noindex: false
  route: /rules/url-forwarding/single-redirects/settings/
  schema: 1
---
<p>The following sections describe the settings of redirect rules to configure static and dynamic URL redirects.</p>
<h2 id="wildcard-url-redirect">Wildcard URL Redirect</h2>
<p>Performs a URL redirect using <a href="/ruleset-engine/rules-language/operators/#wildcard-matching">wildcard patterns</a> to match multiple requests. This method simplifies defining source and target URL patterns without needing complex expressions.</p>
<p>A wildcard URL redirect has the following configuration parameters:</p>
<ul>
<li>
<p><strong>Request URL</strong>: Enter the <a href="/ruleset-engine/rules-language/operators/#wildcard-matching">wildcard pattern</a> using the asterisk (<code>*</code>) character to match multiple requests. For example, <code>https://*.example.com/files/*</code>.</p>
</li>
<li>
<p><strong>Target URL</strong>: Enter the target URL, which can be static (for example, <code>https://example.com</code>) or dynamic (for example, <code>https://example.com/${1}/files/${2}</code>). Use <a href="/ruleset-engine/rules-language/functions/#wildcard_replace">wildcard replacement</a> like <code>${1}</code>, <code>${2}</code>, etc., to define dynamic targets.</p>
</li>
<li>
<p><strong>Status code</strong>: The HTTP status code of the redirect response (<em>301 - Permanent Redirect</em> by default). Must be one of the following:</p>
</li>
<li>
<p><strong>301 - Permanent Redirect</strong>: The page has permanently moved to a new address. For <code>POST</code> requests, the client or browser might switch the HTTP method to <code>GET</code> when following the redirect.</p>
</li>
<li>
<p><strong>302 - Temporary Redirect</strong>: The page has temporarily moved to a new address. For <code>POST</code> requests, the client or browser might switch the HTTP method to <code>GET</code> when following the redirect.</p>
</li>
<li>
<p><strong>307 - Advanced: Temporary, HTTP method preserved</strong>: The page has temporarily moved to a new address. The client or browser must preserve the original HTTP method (for example, <code>POST</code>) when following the redirect.</p>
</li>
<li>
<p><strong>308 - Advanced: Permanent, HTTP method preserved</strong>: The page has permanently moved to a new address. The client or browser must preserve the original HTTP method (for example, <code>POST</code>) when following the redirect.</p>
</li>
<li>
<p><strong>Preserve query string</strong>: Whether to preserve the query string when redirecting (disabled by default).</p>
</li>
</ul>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13187.md")
</div></details>
<h2 id="static-url-redirect">Static URL redirect</h2>
<p>Performs a static URL redirect with a given HTTP status code and optionally preserves the query string.</p>
<p>A static URL redirect has the following configuration parameters:</p>
<ul>
<li>
<p><strong>URL</strong>: A literal string that will be used in the <code>Location</code> HTTP header returned in the redirect response.</p>
</li>
<li>
<p><strong>Status code</strong>: The HTTP status code of the redirect response (<em>301 - Permanent Redirect</em> by default). Must be one of the following:</p>
</li>
<li>
<p><strong>301 - Permanent Redirect</strong>: The page has permanently moved to a new address. For <code>POST</code> requests, the client or browser might switch the HTTP method to <code>GET</code> when following the redirect.</p>
</li>
<li>
<p><strong>302 - Temporary Redirect</strong>: The page has temporarily moved to a new address. For <code>POST</code> requests, the client or browser might switch the HTTP method to <code>GET</code> when following the redirect.</p>
</li>
<li>
<p><strong>307 - Advanced: Temporary, HTTP method preserved</strong>: The page has temporarily moved to a new address. The client or browser must preserve the original HTTP method (for example, <code>POST</code>) when following the redirect.</p>
</li>
<li>
<p><strong>308 - Advanced: Permanent, HTTP method preserved</strong>: The page has permanently moved to a new address. The client or browser must preserve the original HTTP method (for example, <code>POST</code>) when following the redirect.</p>
</li>
<li>
<p><strong>Preserve query string</strong>: Whether to preserve the query string when redirecting (disabled by default).</p>
</li>
</ul>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13188.md")
</div></details>
<h2 id="dynamic-url-redirect">Dynamic URL redirect</h2>
<p>Performs a dynamic URL redirect, where the target URL is determined by an expression. You can configure the redirect HTTP status code and whether to preserve the query string when redirecting.</p>
<p>A dynamic URL redirect has the following configuration parameters:</p>
<ul>
<li>
<p><strong>Expression</strong>: An <a href="/ruleset-engine/rules-language/expressions/">expression</a> that defines the target URL of the redirect. The result of evaluating this expression will be used in the <code>Location</code> HTTP header returned in the redirect response. Refer to the <a href="/ruleset-engine/rules-language/fields/reference/">fields</a> and <a href="/ruleset-engine/rules-language/functions/">functions</a> you can use in expressions.</p>
</li>
<li>
<p><strong>Status code</strong>: The HTTP status code of the redirect response (<em>301 - Permanent Redirect</em> by default). Must be one of the following:</p>
</li>
<li>
<p><strong>301 - Permanent Redirect</strong>: The page has permanently moved to a new address. For <code>POST</code> requests, the client or browser might switch the HTTP method to <code>GET</code> when following the redirect.</p>
</li>
<li>
<p><strong>302 - Temporary Redirect</strong>: The page has temporarily moved to a new address. For <code>POST</code> requests, the client or browser might switch the HTTP method to <code>GET</code> when following the redirect.</p>
</li>
<li>
<p><strong>307 - Advanced: Temporary, HTTP method preserved</strong>: The page has temporarily moved to a new address. The client or browser must preserve the original HTTP method (for example, <code>POST</code>) when following the redirect.</p>
</li>
<li>
<p><strong>308 - Advanced: Permanent, HTTP method preserved</strong>: The page has permanently moved to a new address. The client or browser must preserve the original HTTP method (for example, <code>POST</code>) when following the redirect.</p>
</li>
<li>
<p><strong>Preserve query string</strong>: Whether to preserve the query string when redirecting (disabled by default).</p>
</li>
</ul>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13189.md")
</div></details>
