---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/
  description: Troubleshoot HTTP 522 error responses.
  full_title: Error 522 · Cloudflare Support docs
  head_html: <title>Error 522 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot HTTP 522 error responses."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/index.md"><meta property="og:title" content="Error 522 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot HTTP 522 error responses."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/#page","headline":"Error 522 \u00b7 Cloudflare Support docs","description":"Troubleshoot HTTP 522 error responses.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/
  schema: 1
---
<h2 id="error-522-connection-timed-out">Error 522: connection timed out</h2>
<p>Error <code>522</code> occurs when Cloudflare times out contacting the origin web server.</p>
<h3 id="common-causes">Common causes</h3>
<p>Two different timeouts cause HTTP error <code>522</code> depending on when they occur between Cloudflare and the origin web server:</p>
<ul>
<li>Before a TCP connection is established, Cloudflare does not receive a SYN+ACK within 19 seconds after sending a SYN. The SYN retry backoff intervals are 1, 1, 1, 1, 1, 2, 4, and 8 seconds.</li>
<li>After the TCP connection is established, Cloudflare does not receive an acknowledgment (ACK) of its resource request within 90 seconds.</li>
</ul>
<h3 id="resolution">Resolution</h3>
<ul>
<li>
<p>Contact your hosting provider and share the <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/#required-error-details-for-hosting-provider">error details</a> to assist in troubleshooting these common causes:</p>
<ul>
<li><a href="https://www.cloudflare.com/ips/">Cloudflare IP addresses</a> are rate limited or blocked in .htaccess, iptables, or firewalls. Confirm your hosting provider allows <strong>all Cloudflare IP ranges</strong> (most common cause). You can use a <a href="/waf/custom-rules/use-cases/block-by-geographical-location/">Cloudflare WAF Custom Rule</a> if you need to restrict traffic from geographical locations.</li>
<li>An overloaded or offline origin web server drops incoming requests.</li>
<li><a href="http://tldp.org/HOWTO/TCP-Keepalive-HOWTO/overview.html">Keepalives</a> are disabled at the origin web server.</li>
<li>The origin IP address in your Cloudflare <strong>DNS</strong> app does not match the IP address currently provisioned to your origin web server by your hosting provider.</li>
<li>Packets were dropped at your origin web server.</li>
</ul>
</li>
<li>
<p>If you are using <a href="/pages/">Cloudflare Pages</a>, verify that you have a custom domain set up and that your CNAME record is pointed to your <a href="/pages/configuration/custom-domains/#add-a-custom-domain">custom Pages domain</a>.</p>
</li>
<li>
<p>If you are using <a href="/workers/configuration/routing/custom-domains/">Workers with a Custom Domain</a>, performing a <code>fetch</code> to its own hostname will cause a <code>522</code> error. Consider using a <a href="/workers/configuration/routing/">Route</a>, targeting another hostname, or enabling the <a href="/workers/configuration/compatibility-flags/#global-fetch-strictly-public"><code>global_fetch_strictly_public</code> compatibility flag</a> instead.</p>
</li>
<li>
<p>If you are using <a href="/rules/origin-rules/">Origin Rules</a>, make sure the resulting hostname can be resolved. For example, if your Origin Rule point to a Worker route, a <code>522</code> error will be returned if the hostname for this route is an A record pointing to a reserved address such as <code>100::</code> or <code>192.0.2.0</code>.</p>
</li>
<li>
<p>If none of the above leads to a resolution, request the following information from your hosting provider or site administrator before <a href="/support/contacting-cloudflare-support/">contacting Cloudflare support</a>:</p>
<ul>
<li>An <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#perform-a-traceroute">MTR or traceroute</a> from your origin web server to a <a href="http://www.cloudflare.com/ips">Cloudflare IP address</a> that most commonly connected to your origin web server before the issue occurred. Identify a connecting Cloudflare IP recorded in the origin web server logs.</li>
<li>Details from the hosting provider's investigation, such as pertinent logs or conversations with the hosting provider.</li>
</ul>
</li>
</ul>
<h3 id="diagnose-with-origin-analytics">Diagnose with Origin Analytics</h3>
<p>Use <a href="/speed/origin-analytics/">Origin Analytics</a> to check for TCP connection failures to your origin. If the <strong>Top endpoints</strong> table shows a high TCP failure rate for specific paths, the issue may be path-specific rather than a general origin problem. Origin Analytics can also help confirm whether your origin is reachable from Cloudflare's edge.</p>
