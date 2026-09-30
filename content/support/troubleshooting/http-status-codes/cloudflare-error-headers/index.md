---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-error-headers/
  description: Reference for the cf-error-type and cf-error-origin response headers present on Cloudflare-generated error pages.
  full_title: Cloudflare error diagnostic headers · Cloudflare Support docs
  head_html: <title>Cloudflare error diagnostic headers · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference for the cf-error-type and cf-error-origin response headers present on Cloudflare-generated error pages."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-error-headers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-error-headers/index.md"><meta property="og:title" content="Cloudflare error diagnostic headers · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference for the cf-error-type and cf-error-origin response headers present on Cloudflare-generated error pages."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-error-headers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-error-headers/#page","headline":"Cloudflare error diagnostic headers \u00b7 Cloudflare Support docs","description":"Reference for the cf-error-type and cf-error-origin response headers present on Cloudflare-generated error pages.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-error-headers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-error-headers/
  schema: 1
---
<p>When Cloudflare generates an error page (as opposed to forwarding an error from your origin server), the response includes two diagnostic headers:</p>
<ul>
<li><strong><code>cf-error-type</code></strong>: Identifies the error category. Common values:
<ul>
<li><code>1000</code> — DNS resolution failure (A record points to a Cloudflare IP)</li>
<li><code>1016</code> — Origin DNS error (CNAME target does not resolve)</li>
<li><code>1101</code> — Worker threw an unhandled exception</li>
<li><code>1102</code> — Worker exceeded resource limits (CPU or memory)</li>
<li><code>52x</code> — Origin connectivity error (521, 522, 523, 524, 525, 526)</li>
</ul>
</li>
<li><strong><code>cf-error-origin</code></strong>: Identifies which Cloudflare system generated the error.</li>
</ul>
<p>These headers are present <strong>only on Cloudflare-generated error pages</strong>, not on errors forwarded from your origin server.</p>
<h2 id="how-to-capture-these-headers">How to capture these headers</h2>
<p>Reproduce the error and inspect response headers using one of:</p>
<ul>
<li><code>curl -v https://example.com</code> — look for <code>cf-error-type</code> in the response headers</li>
<li>Browser DevTools: select <strong>Network</strong> &gt; select the failing request &gt; <strong>Headers</strong></li>
<li>Export a HAR file and inspect the response headers</li>
</ul>
<h2 id="using-cf-error-type-for-diagnosis">Using cf-error-type for diagnosis</h2>
<table>
<thead>
<tr>
<th><code>cf-error-type</code> prefix</th>
<th>Origin</th>
<th>Next step</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1xxx</code></td>
<td>DNS / routing layer</td>
<td>Check DNS records; verify no Cloudflare IP in A record</td>
</tr>
<tr>
<td><code>1101</code> / <code>1102</code></td>
<td>Workers runtime</td>
<td>Check <code>wrangler tail</code> for the exception</td>
</tr>
<tr>
<td><code>52x</code></td>
<td>Origin connectivity</td>
<td>Check origin server is up and reachable</td>
</tr>
</tbody>
</table>
