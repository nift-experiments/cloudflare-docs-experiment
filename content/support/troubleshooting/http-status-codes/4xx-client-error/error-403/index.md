---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-403/
  description: Troubleshoot HTTP 403 error responses.
  full_title: Error 403 · Cloudflare Support docs
  head_html: <title>Error 403 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot HTTP 403 error responses."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-403/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-403/index.md"><meta property="og:title" content="Error 403 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot HTTP 403 error responses."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-403/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-403/#page","headline":"Error 403 \u00b7 Cloudflare Support docs","description":"Troubleshoot HTTP 403 error responses.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-403/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/4xx-client-error/error-403/
  schema: 1
---
<h2 id="403-forbidden">403 Forbidden</h2>
<p>The <code>403 Forbidden</code> status code indicates that the client's request was understood by the server but cannot be fulfilled due to insufficient permissions to access the requested resource.
For more details, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>If you encounter a <code>403</code> error without the Cloudflare branding, this means that the error is being returned directly by the origin web server, not Cloudflare. This is typically related to permission rules set on your server. Common reasons for this error are:</p>
<ul>
<li>Permission rules configured on the origin web server (for example, in an Apache <code>.htaccess</code> file).</li>
<li>Mod_security rules.</li>
<li>IP deny rules, such as blocking traffic from certain IP ranges. Make sure that <a href="https://www.cloudflare.com/ips">Cloudflare's IP ranges</a> are not being blocked.</li>
</ul>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>Cloudflare may serve <code>403</code> responses in the following scenarios:</p>
<ul>
<li>
<p><strong>WAF rules</strong>: The request violated a default WAF managed rule (enabled for all orange-clouded Cloudflare domains) or a custom WAF managed rule specific to your zone. For more information, refer to <a href="/waf/managed-rules/">WAF Managed Rules</a>.</p>
</li>
<li>
<p><strong>Security features</strong>: A <code>403</code> response with Cloudflare branding in the response body may be triggered by:</p>
<ul>
<li><a href="/waf/">WAF Custom or Managed Rules</a> with the challenge or block action.</li>
<li><a href="/waf/tools/security-level/">Security Level</a> settings, which default to Medium.</li>
<li><a href="/ddos-protection/">DDoS Protection</a>, which is enabled by default on zones onboarded to Cloudflare, IP applications onboarded to Spectrum, and IP Prefixes onboarded to Magic Transit.</li>
<li>Most <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">1xxx Cloudflare error codes</a>.</li>
<li>The <a href="/waf/tools/browser-integrity-check/">Browser Integrity Check</a>.</li>
<li><a href="/waf/tools/validation-checks/">Validation Checks</a>.</li>
</ul>
</li>
</ul>
<p>Cloudflare may also serve an unstyled <code>403</code> error page in specific cases. These errors are not logged because they occur early in Cloudflare's infrastructure, before domain configuration is loaded. An example is:</p>
<ul>
<li><a href="https://www.cloudflare.com/learning/ssl/what-is-sni/">SNI</a>: A <code>403</code> error is returned when the client sends a host that does not match the SNI (Server Name Indication).</li>
</ul>
