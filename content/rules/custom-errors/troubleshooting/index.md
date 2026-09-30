---
cp9:
  canonical: https://developers.cloudflare.com/rules/custom-errors/troubleshooting/
  description: Resolve common issues with custom error rules and error pages.
  full_title: Troubleshoot Error Pages issues · Cloudflare Rules docs
  head_html: <title>Troubleshoot Error Pages issues · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Resolve common issues with custom error rules and error pages."><link rel="canonical" href="https://developers.cloudflare.com/rules/custom-errors/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/custom-errors/troubleshooting/index.md"><meta property="og:title" content="Troubleshoot Error Pages issues · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Resolve common issues with custom error rules and error pages."><meta property="og:url" content="https://developers.cloudflare.com/rules/custom-errors/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/custom-errors/troubleshooting/#page","headline":"Troubleshoot Error Pages issues \u00b7 Cloudflare Rules docs","description":"Resolve common issues with custom error rules and error pages.","url":"https://developers.cloudflare.com/rules/custom-errors/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/custom-errors/troubleshooting/
  schema: 1
---
<h2 id="cannot-preview-error-page">Cannot preview error page</h2>
<p>If Cloudflare cannot load your site or you have blocked the United States (US) via <a href="/waf/tools/ip-access-rules/">IP Access rules</a> or <a href="/waf/custom-rules/">WAF custom rules</a>, publishing and previewing a custom error page might not work.</p>
<p>A common error might look like the following: <code>Error fetching page: Fetch failed, https://example.com/ipcountryblock.html returned 403 (Code: 1202)</code>.</p>
<p>Make sure that no WAF rule is blocking or challenging Custom Errors product when it is fetching the content of your custom error page.</p>
<h2 id="error-pages-for-blocked-requests">Error pages for blocked requests</h2>
<p>If you block countries or IP addresses with an <a href="/waf/tools/ip-access-rules/">IP Access rule</a>, affected visitors will get a <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1005/">1005 error</a> and your <strong>IP/Country Block</strong> custom page.</p>
<p>If you block countries or IP addresses with a <a href="/waf/custom-rules/">WAF custom rule</a> and you do not configure a <a href="/rules/custom-errors/create-rules/#create-a-custom-error-rule-dashboard">custom error rule</a> or a <a href="/waf/custom-rules/create-dashboard/#configure-a-custom-response-for-blocked-requests">WAF custom response</a> for blocked requests, affected visitors will get your <strong>WAF Block</strong> page.</p>
<p>If you block requests due to a <a href="/waf/rate-limiting-rules/">rate limiting rule</a> and you do not configure a <a href="/rules/custom-errors/create-rules/#create-a-custom-error-rule-dashboard">custom error rule</a> or a <a href="/waf/rate-limiting-rules/create-zone-dashboard/#configure-a-custom-response-for-blocked-requests">WAF custom response</a> for blocked requests, affected visitors will get your <strong>429 Errors</strong> page displaying a Cloudflare <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1015/">1015 error</a>.</p>
<p>If you block countries or IP addresses with a firewall rule (now deprecated), affected visitors will get your <strong>1000 Class Errors</strong> page.</p>
<h2 id="1xxx-errors">1XXX errors</h2>
<p>You cannot customize the following 1XXX errors via Error Pages:</p>
<ul>
<li><code>1001</code> - Unable to resolve</li>
<li><code>1003</code> - Bad Host header</li>
<li><code>1018</code> - Unable to resolve because of ownership lookup failure</li>
<li><code>1023</code> - Unable to resolve because of feature lookup failure</li>
</ul>
<h2 id="custom-error-page-size">Custom error page size</h2>
<p>Your custom error page cannot be blank and the combined size of all page assets cannot exceed 1.5 MB (1,500,000 characters). To avoid exceeding the custom error page limit, preview your page to check its size before publishing.</p>
<h2 id="general-troubleshooting-advice">General troubleshooting advice</h2>
<p>If you encounter errors while attempting to preview or publish your custom error page, use an <a href="https://validator.w3.org/">HTML validator</a> to ensure that your code resolves properly.</p>
<h2 id="more-resources">More resources</h2>
<ul>
<li><a href="/support/troubleshooting/http-status-codes/">HTTP Status Codes</a></li>
<li><a href="/cloudflare-challenges/">Challenges</a></li>
</ul>
