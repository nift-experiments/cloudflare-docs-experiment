---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-500/
  description: Troubleshoot HTTP 500 error responses.
  full_title: Error 500 · Cloudflare Support docs
  head_html: <title>Error 500 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot HTTP 500 error responses."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-500/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-500/index.md"><meta property="og:title" content="Error 500 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot HTTP 500 error responses."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-500/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-500/#page","headline":"Error 500 \u00b7 Cloudflare Support docs","description":"Troubleshoot HTTP 500 error responses.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-500/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-500/
  schema: 1
---
<h2 id="error-500-internal-server-error">Error 500: internal server error</h2>
<p>This error indicates a problem with your origin web server, preventing it from fulfilling the request.</p>
<h3 id="common-causes">Common causes</h3>
<p>The <code>Error establishing database connection message</code> is a common HTTP <code>500</code> error, typically indicating an origin web server issue. If you encounter this error, contact your hosting provider for assistance.</p>
<h3 id="resolution">Resolution</h3>
<p>When dealing with most <code>5XX</code> errors, the first step is to reach out to your hosting provider or site administrator to help troubleshoot the issue. Share the necessary <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/#required-error-details-for-hosting-provider">error details</a> to your hosting provider to assist troubleshooting the issue.</p>
<p>However, if the <code>500</code> error contains <code>cloudflare</code> or <code>cloudflare-nginx</code> in the HTML response body, contact <a href="/support/contacting-cloudflare-support/">Cloudflare support</a> and provide the following details:</p>
<ul>
<li>Your domain name</li>
<li>The time and timezone of the <code>500</code> error occurrence</li>
<li>The output of <code>www.example.com/cdn-cgi/trace</code> from the browser where the <code>500</code> error was observed (replace <code>www.example.com</code> with your actual domain and hostname)</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14731.md")
</aside>
<h3 id="workers-specific-causes">Workers-specific causes</h3>
<p>Error 500 can also occur when using Cloudflare Workers:</p>
<ul>
<li>A Cloudflare Worker throws a runtime JavaScript exception (see <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1101/">Error 1101</a>)</li>
</ul>
<p>If you are using Workers, check the Workers dashboard for error logs and exceptions.</p>
<h3 id="troubleshooting-steps">Troubleshooting steps</h3>
<ol>
<li><strong>Check recent configuration changes</strong>: Review any recent changes to Page Rules, Transform Rules, or Workers that might affect request processing.</li>
<li><strong>Verify origin connectivity</strong>: Ensure your origin server is responding correctly and within acceptable timeframes.</li>
<li><strong>Review Workers logs</strong>: If using Workers, check for JavaScript exceptions or CPU time limit errors in the Workers dashboard.</li>
<li><strong>Test with Cloudflare paused</strong>: Temporarily pause Cloudflare to determine if the issue is origin-related.</li>
</ol>
<h3 id="known-cloudflare-issue-leading-to-http-error-500">Known Cloudflare issue leading to HTTP Error 500</h3>
<ul>
<li>A configuration issue on Page Rules can generate HTTP Error <code>500</code>. Refer to <a href="/rules/page-rules/troubleshooting/general/#error-500-internal-server-error">Page Rules troubleshooting</a> for more details and resolution.</li>
</ul>
