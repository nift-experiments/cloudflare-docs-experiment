---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-egress-policies/egress-policies/
  description: Create egress policies for IP consistency.
  full_title: Use egress policies to deliver consistent egress IPs · Cloudflare Learning Paths
  head_html: <title>Use egress policies to deliver consistent egress IPs · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Create egress policies for IP consistency."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-egress-policies/egress-policies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-egress-policies/egress-policies/index.md"><meta property="og:title" content="Use egress policies to deliver consistent egress IPs · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create egress policies for IP consistency."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-egress-policies/egress-policies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Gateway,Cloudflare One,Data Loss Prevention,CASB,Browser Isolation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-egress-policies/egress-policies/#page","headline":"Use egress policies to deliver consistent egress IPs \u00b7 Cloudflare Learning Paths","description":"Create egress policies for IP consistency.","url":"https://developers.cloudflare.com/learning-paths/secure-internet-traffic/build-egress-policies/egress-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/secure-internet-traffic/build-egress-policies/egress-policies/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10211.md")
</aside>
<p>Egress policies allow you to determine whether your organization's traffic egresses via the default Cloudflare IP or via a <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">dedicated egress IP</a> assigned to your account.</p>
<p>To create a new egress policy:</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Egress policies</strong>.</p>
</li>
<li>
<p>Select <strong>Add a policy</strong>.</p>
</li>
<li>
<p>Name the policy.</p>
</li>
<li>
<p>Build a logical expression that defines the traffic you want to control egress for. For example, you can add a policy to configure all traffic destined for a third-party network to use a static source IP:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Policy name</th>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Egress method</th>
</tr>
</thead>
<tbody>
<tr>
<td>Access third-party provider</td>
<td>Destination IP</td>
<td>is</td>
<td><code>198.51.100.158</code></td>
<td>Dedicated Cloudflare egress IPs</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>Primary IPv4 address</th>
<th>IPv6 address</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>203.0.113.88</code></td>
<td><code>2001:db8::/32</code></td>
</tr>
</tbody>
</table>
<ol start="5">
<li>Select <strong>Create policy</strong>.</li>
</ol>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/egress-policies/">Egress policies</a>.</p>
