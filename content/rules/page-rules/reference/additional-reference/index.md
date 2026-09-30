---
cp9:
  canonical: https://developers.cloudflare.com/rules/page-rules/reference/additional-reference/
  description: Additional reference information for Page Rules settings.
  full_title: Additional reference for Page Rules · Cloudflare Rules docs
  head_html: <title>Additional reference for Page Rules · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Additional reference information for Page Rules settings."><link rel="canonical" href="https://developers.cloudflare.com/rules/page-rules/reference/additional-reference/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/page-rules/reference/additional-reference/index.md"><meta property="og:title" content="Additional reference for Page Rules · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Additional reference information for Page Rules settings."><meta property="og:url" content="https://developers.cloudflare.com/rules/page-rules/reference/additional-reference/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Rules"><meta name="pcx_tags" content="Cookies,Caching"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/page-rules/reference/additional-reference/#page","headline":"Additional reference for Page Rules \u00b7 Cloudflare Rules docs","description":"Additional reference information for Page Rules settings.","url":"https://developers.cloudflare.com/rules/page-rules/reference/additional-reference/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Cookies","Caching"]}</script>
  markdown: true
  noindex: false
  route: /rules/page-rules/reference/additional-reference/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13118.md")
</aside>
<h2 id="bypass-cache-on-cookie-setting">Bypass Cache on Cookie setting</h2>
<p>This setting is available to Business and Enterprise customers.</p>
<p>The <strong>Bypass Cache on Cookie</strong> setting supports basic regular expressions (regex) as follows:</p>
<ul>
<li>A pipe operator (represented by <code>|</code>) to match multiple cookies using <em>OR</em> boolean logic. For example, <code>bypass=.*|PHPSESSID=.*</code> would bypass the cache if either a cookie called <code>bypass</code> or <code>PHPSESSID</code> were set, regardless of the cookie's value.</li>
<li>The wildcard operator (represented by <code>.*</code>), such that a rule value of <code>t.*st=</code> would match both a cookie called <code>test</code> and one called <code>teeest</code>.</li>
</ul>
<p>Limitations include:</p>
<ul>
<li>150 characters per cookie regex</li>
<li>12 wildcards per cookie regex</li>
<li>1 wildcard in between each <code>|</code> in the cookie regex</li>
</ul>
<p>To learn how to configure <strong>Bypass Cache on Cookie</strong> with a cache rule, refer to <a href="/cache/how-to/cache-rules/examples/bypass-cache-on-cookie/">Bypass Cache on Cookie</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13117.md")
</aside>
<h2 id="zone-name-occurrences-must-end-with-a-slash">Zone name occurrences must end with a slash</h2>
<p>When saving a page rule, Cloudflare will ensure that there is a slash after each occurrence of the current zone name in the <strong>If the URL matches</strong> field. For example, if the current zone name is <code>example.com</code>, then:</p>
<ul>
<li><code>example.com</code> will be saved as <code>example.com/</code></li>
<li><code>example.com/path/example.com</code> will be saved as <code>example.com/path/example.com/</code></li>
</ul>
<p>Note that <code>example.com/some-path/cloudflare.com</code> will be saved <em>without</em> a final slash, since the zone name is not <code>cloudflare.com</code>.</p>
<h2 id="network-ports-supported-by-page-rules">Network ports supported by Page Rules</h2>
<p>If you specify a port in the <strong>If the URL matches</strong> field of a page rule, it must be one of the following:</p>
<ul>
<li>One of the HTTP/HTTPS ports <a href="/fundamentals/reference/network-ports/#network-ports-compatible-with-cloudflares-proxy">compatible with Cloudflare’s proxy</a>.</li>
<li>A custom port of a <a href="/spectrum/">Cloudflare Spectrum</a> HTTPS application.</li>
</ul>
<h2 id="using-page-rules-with-workers">Using Page Rules with Workers</h2>
<p>If the URL of the current request matches both a page rule and a <a href="/workers/configuration/routing/routes/">Workers custom route</a>, some Pages Rules settings will not be applied. For more details, refer to <a href="/workers/configuration/workers-with-page-rules/">Page Rules</a>.</p>
<h2 id="page-rules-are-case-insensitive">Page Rules are case-insensitive</h2>
<p>The pattern entered under <strong>If the URL matches</strong> will not consider upper and lower case differences — <code>example.com/path</code>, <code>example.com/Path</code>, and <code>example.com/PATH</code> will be triggered the same way.</p>
<p>If you need your rules to consider case sensitivity, you might want to use alternative <a href="/rules/">Rules</a> options instead.</p>
