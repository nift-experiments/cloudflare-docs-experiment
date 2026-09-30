---
cp9:
  canonical: https://developers.cloudflare.com/rules/transform/url-rewrite/
  description: Rewrite request URL paths and query strings with Transform Rules.
  full_title: URL Rewrite Rules · Cloudflare Rules docs
  head_html: <title>URL Rewrite Rules · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Rewrite request URL paths and query strings with Transform Rules."><link rel="canonical" href="https://developers.cloudflare.com/rules/transform/url-rewrite/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/transform/url-rewrite/index.md"><meta property="og:title" content="URL Rewrite Rules · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Rewrite request URL paths and query strings with Transform Rules."><meta property="og:url" content="https://developers.cloudflare.com/rules/transform/url-rewrite/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Rules"><meta name="pcx_tags" content="URL rewrite"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/transform/url-rewrite/#page","headline":"URL Rewrite Rules \u00b7 Cloudflare Rules docs","description":"Rewrite request URL paths and query strings with Transform Rules.","url":"https://developers.cloudflare.com/rules/transform/url-rewrite/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["URL rewrite"]}</script>
  markdown: true
  noindex: false
  route: /rules/transform/url-rewrite/
  schema: 1
---
<p>You can manipulate the URL of a request through different operations, namely rewrites and redirects:</p>
<ul>
<li>
<p><strong>URL rewrite</strong>: A server-side operation that converts a source URL into a target URL. It occurs before a web server has fully processed a request. A rewrite is not visible to website visitors, since the URL displayed in the browser does not change. Configure URL Rewrite Rules to perform rewrites on the Cloudflare global network without reaching your web server.</p>
</li>
<li>
<p><strong>URL redirect</strong>: A client-side operation that converts a source URL into a target URL. It occurs after the web server has loaded the initial URL. In this case, a website visitor can notice the URL changing when the redirect occurs. Refer to <a href="/rules/url-forwarding/">Redirects</a> to learn more about configuring redirects.</p>
</li>
</ul>
<p>Use a URL rewrite rule to return the content of a URL while displaying a different URL in the browser. You can rewrite the URI path, the query string, or both.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13126.md")
</aside>
<h2 id="static-and-dynamic-rewrites">Static and dynamic rewrites</h2>
<p>URL Rewrite Rules can perform static or dynamic rewrites:</p>
<ul>
<li><strong>Static rewrite</strong>: Replaces a given part of a request URL (path or query string) with a static string.</li>
<li><strong>Dynamic rewrite</strong>: Supports more advanced scenarios where you use a <a href="/ruleset-engine/rules-language/">rewrite expression</a> (a formula based on request properties) to define the resulting path or query string.</li>
</ul>
<p>Create URL Rewrite Rules <a href="/rules/transform/url-rewrite/create-dashboard/">in the dashboard</a>, <a href="/rules/transform/url-rewrite/create-api/">via Cloudflare API</a>, or <a href="/terraform/additional-configurations/transform-rules/#create-a-url-rewrite-rule">using Terraform</a>.</p>
<h2 id="serve-images-from-custom-paths">Serve images from custom paths</h2>
<p>When using Cloudflare Images, you can use URL Rewrite Rules to serve images from a custom path. For more information, refer to <a href="/images/optimization/hosted-images/serve-from-custom-domains/">Serve images from custom domains</a>.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>When troubleshooting URL Rewrite Rules, use <a href="/rules/trace-request/">Cloudflare Trace</a> to determine if a rule is triggering for a specific URL.</p>
<h2 id="important-remarks">Important remarks</h2>
<ul>
<li>
<p>URL rewrite rules run in order, and later rules can overwrite changes done by previous rules.</p>
</li>
<li>
<p>The values of request and response fields are immutable within each <a href="/ruleset-engine/about/phases/">phase</a>, such as the <code>http_request_transform</code> phase where URL rewrite rules are defined. This means that later URL rewrite rules will still use the original field values when evaluating their filter expressions, not the values changed by previous rules. Refer to <a href="/ruleset-engine/about/rules/#field-values-during-rule-evaluation">Field values during rule evaluation</a> for more information.</p>
</li>
</ul>
