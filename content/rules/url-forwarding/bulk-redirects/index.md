---
cp9:
  canonical: https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/
  description: Redirect large numbers of URLs with Bulk Redirects at the account level.
  full_title: Bulk Redirects · Cloudflare Rules docs
  head_html: <title>Bulk Redirects · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Redirect large numbers of URLs with Bulk Redirects at the account level."><link rel="canonical" href="https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/index.md"><meta property="og:title" content="Bulk Redirects · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Redirect large numbers of URLs with Bulk Redirects at the account level."><meta property="og:url" content="https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Rules"><meta name="pcx_tags" content="Redirects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/#page","headline":"Bulk Redirects \u00b7 Cloudflare Rules docs","description":"Redirect large numbers of URLs with Bulk Redirects at the account level.","url":"https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Redirects"]}</script>
  markdown: true
  noindex: false
  route: /rules/url-forwarding/bulk-redirects/
  schema: 1
---
<p>Bulk Redirects allow you to define a large number of URL redirects at the account level, which can apply across domains in your account. These redirects navigate the user from a source URL to a target URL using a given HTTP status code. URL redirection is also known as URL forwarding.</p>
<p>Unlike dynamic URL redirects created in <a href="/rules/url-forwarding/single-redirects/">Single Redirects</a>, Bulk Redirects are essentially static. They do not support string replacement operations or regular expressions. However, you can configure URL redirect parameters that affect how source URLs are matched and how the redirect is performed.</p>
<p>For more complex and customized redirect logic, consider using <a href="/rules/snippets/">Snippets</a>.</p>
<hr />
<h2 id="bulk-redirects-and-the-waf">Bulk Redirects and the WAF</h2>
<p>Bulk Redirects run after the WAF in the request processing pipeline. This means that:</p>
<ul>
<li>If a <a href="/waf/custom-rules/">WAF custom rule</a> or <a href="/waf/rate-limiting-rules/">rate limiting rule</a> blocks a request, the Bulk Redirect will not execute.</li>
<li>If a WAF rule logs or challenges a request that subsequently passes, the firewall event will still appear in <a href="/waf/analytics/security-events/">Security Events</a> and <a href="/logs/">Logpush</a> — even though the request is later redirected. This is expected behavior.</li>
</ul>
<p>For the complete request processing order, refer to <a href="/rules/url-forwarding/#execution-order">Rules execution order</a>.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/rules/url-forwarding/#availability">Availability</a>: Information on the Bulk Redirects quotas and features per Cloudflare plan.</li>
<li><a href="/rules/url-forwarding/#execution-order">Execution order</a>: Execution order of the different Rules products.</li>
<li><a href="/rules/trace-request/">Trace a request</a>: Use Cloudflare Trace to determine if a bulk redirect rule is triggering for a specific URL.</li>
</ul>
