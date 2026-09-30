---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/test-policy/
  description: Test Gateway DNS policy enforcement.
  full_title: Test a policy · Cloudflare Learning Paths
  head_html: <title>Test a policy · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Test Gateway DNS policy enforcement."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/test-policy/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/test-policy/index.md"><meta property="og:title" content="Test a policy · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Test Gateway DNS policy enforcement."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/test-policy/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Gateway,Cloudflare One,Data Loss Prevention,CASB,Browser Isolation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/test-policy/#page","headline":"Test a policy \u00b7 Cloudflare Learning Paths","description":"Test Gateway DNS policy enforcement.","url":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-dns-policies/test-policy/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/secure-internet-traffic/build-dns-policies/test-policy/
  schema: 1
---
<p>It is common for a misconfigured Gateway policy to accidentally block traffic to benign sites. To ensure a smooth deployment, we recommend testing a simple policy before deploying DNS filtering to your organization.</p>
<h2 id="test-a-policy-in-the-browser">Test a policy in the browser</h2>
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>Turn off all existing DNS policies.</li>
<li>Turn on any existing security policies or create a policy to block all security categories:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Security Categories</td>
<td>in</td>
<td><em>All security risks</em></td>
<td>Block</td>
</tr>
</tbody>
</table>
<ol start="4">
<li>Ensure that your browser is not configured to use an alternate DNS resolver. For example, Chrome has a <strong>Use secure DNS</strong> setting that will cause the browser to send requests to 1.1.1.1 and bypass your DNS policies.</li>
<li>In the browser, go to <code>malware.testcategory.com</code>. Your browser will display:
<ul>
<li>The Gateway block page, if your device is connected through the Cloudflare One Client in Traffic and DNS mode.</li>
<li>A generic error page, if your device is connected through another method, such as DNS only mode.</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10215.md")
</aside>
<ol start="6">
<li>In <strong>Logs</strong> &gt; <strong>Gateway</strong> &gt; <strong>DNS</strong>, verify that you see the blocked domain.</li>
<li>Slowly turn on or add other policies to your configuration.</li>
<li>When testing against frequently-visited sites, you may need to <a href="/cloudflare-one/traffic-policies/dns-policies/test-dns-filtering/#clear-dns-cache">clear the DNS cache</a> in your browser or OS. Otherwise, the DNS lookup will return the locally-cached IP address and bypass your DNS policies.</li>
</ol>
<p>You have now validated DNS filtering on a test device.</p>
