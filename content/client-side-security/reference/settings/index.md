---
cp9:
  canonical: https://developers.cloudflare.com/client-side-security/reference/settings/
  description: Configure client-side security monitoring, logging, and connection tracking settings.
  full_title: Configuration settings · Client-side security docs
  head_html: <title>Configuration settings · Client-side security docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure client-side security monitoring, logging, and connection tracking settings."><link rel="canonical" href="https://developers.cloudflare.com/client-side-security/reference/settings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/client-side-security/reference/settings/index.md"><meta property="og:title" content="Configuration settings · Client-side security docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure client-side security monitoring, logging, and connection tracking settings."><meta property="og:url" content="https://developers.cloudflare.com/client-side-security/reference/settings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Client-side security"><meta name="algolia_product_filter" content="Client-side security"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Client-side security"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/client-side-security/reference/settings/#page","headline":"Configuration settings \u00b7 Client-side security docs","description":"Configure client-side security monitoring, logging, and connection tracking settings.","url":"https://developers.cloudflare.com/client-side-security/reference/settings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /client-side-security/reference/settings/
  schema: 1
---
<h2 id="reporting-endpoint">Reporting endpoint</h2>
<p>When enabled, client-side security's resource monitoring uses a <span class="nb-glossary-tooltip" title="content security policy (CSP)">Content Security Policy (CSP)</span> <a href="/client-side-security/reference/csp-header/">report-only HTTP header</a> to gather information about all the scripts running on your application.</p>
<p>By default, reports are sent to a Cloudflare-owned endpoint:</p>
<pre tabindex="0"><code class="language-txt">https://csp-reporting.cloudflare.com/cdn-cgi/script_monitor/report?&lt;QUERY_STRING&gt;&#10;</code></pre>
<p>Customers with Client-Side Security Advanced can change the reporting endpoint so that the CSP reports are sent to the same hostname:</p>
<pre tabindex="0"><code class="language-txt">&lt;YOUR-HOSTNAME&gt;/cdn-cgi/script-monitor/report?&lt;QUERY_STRING&gt;&#10;</code></pre>
<h3 id="prerequisites-for-using-the-same-hostname-for-csp-reports">Prerequisites for using the same hostname for CSP reports</h3>
<p>Using the same hostname for CSP reporting may interfere with other Cloudflare products. Before selecting this option, ensure that your Cloudflare configuration complies with the following:</p>
<ul>
<li>No rate limiting rules match the <code>cdn-cgi/*</code> URL path</li>
<li>No custom rules match the <code>cdn-cgi/*</code> URL path</li>
</ul>
<h3 id="configure-the-reporting-endpoint">Configure the reporting endpoint</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3971.md")
</aside>
<p>To configure the CSP reporting endpoint:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3973.md")
</div>
<h2 id="connection-target-details">Connection target details</h2>
<p>When connection targets are reported to Cloudflare, their URIs can sometimes include sensitive data such as session ID.</p>
<p>By default, client-side security only checks the domain against malicious threat intelligence feeds. You can choose to let Cloudflare use the full URI when analyzing the connections made from your domain's pages. Any sensitive data present in the URI will be logged in clear text, and any user with access to the connection monitor dashboard will be able to view it.</p>
<h3 id="configure-the-connection-target-details-to-use">Configure the connection target details to use</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3974.md")
</div>
<h2 id="turn-off-client-side-resource-monitoring">Turn off client-side resource monitoring</h2>
<p>When you turn off client-side security's resource monitoring, you lose visibility on the scripts running on your zone, the outbound connections made from pages in your domain, and cookies detected in HTTP traffic.</p>
<p>To turn off client-side resource monitoring:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3975.md")
</div>
<p>Turning off client-side security's resource monitoring does not turn off <a href="/client-side-security/rules/">content security rules</a> (previously known as policies). To turn off content security rules:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>(Optional) Filter by <strong>Content security rules</strong>.</li>
<li>For each rule, select the three dots next to it &gt; <strong>Disable</strong>.</li>
</ol>
