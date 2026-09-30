---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/manage-domains/manage-subdomains/
  description: Create subdomains, set up redirects between subdomains and apex domains, and configure SSL/TLS for subdomains on Cloudflare.
  full_title: Manage subdomains · Cloudflare Fundamentals docs
  head_html: <title>Manage subdomains · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Create subdomains, set up redirects between subdomains and apex domains, and configure SSL/TLS for subdomains on Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/manage-domains/manage-subdomains/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/manage-domains/manage-subdomains/index.md"><meta property="og:title" content="Manage subdomains · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create subdomains, set up redirects between subdomains and apex domains, and configure SSL/TLS for subdomains on Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/manage-domains/manage-subdomains/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/manage-domains/manage-subdomains/#page","headline":"Manage subdomains \u00b7 Cloudflare Fundamentals docs","description":"Create subdomains, set up redirects between subdomains and apex domains, and configure SSL/TLS for subdomains on Cloudflare.","url":"https://developers.cloudflare.com/fundamentals/manage-domains/manage-subdomains/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/manage-domains/manage-subdomains/
  schema: 1
---
<p>Once you have <a href="/fundamentals/manage-domains/add-site/">added your domain to Cloudflare</a> and <a href="/dns/zone-setups/full-setup/">updated your nameservers</a>, you also might want to set up a subdomain.</p>
<p>Most subdomains serve a specific purpose within the overall context of your website. For example, <code>blog.example.com</code> might be your blog, <code>support.example.com</code> could be your customer help portal, and <code>store.example.com</code> would be your e-commerce site.</p>
<h2 id="create-a-subdomain">Create a subdomain</h2>
<p>If you have already added a subdomain at your host, create a corresponding <a href="/dns/manage-dns-records/how-to/create-dns-records/">DNS A or CNAME record</a> for that subdomain (<code>blog</code>, <code>store</code>).</p>
<h2 id="set-up-redirects">Set up redirects</h2>
<h3 id="redirect-a-subdomain-to-the-apex-domain">Redirect a subdomain to the apex domain</h3>
<p>Sometimes, you might want all traffic to a subdomain (<code>www.example.com</code>)  to actually go to your apex domain (<code>example.com</code>).</p>
<ol>
<li>Create a <a href="/dns/manage-dns-records/how-to/create-dns-records/">proxied DNS A record</a> for your subdomain. This record can point to any IP address since all traffic will be redirected prior to reaching the address.</li>
</ol>
<table>
<thead>
<tr>
<th><strong>Type</strong></th>
<th><strong>Name</strong></th>
<th><strong>IPv4 address</strong></th>
<th><strong>Proxy status</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td><code>www</code></td>
<td><code>192.0.2.1</code></td>
<td>Proxied</td>
</tr>
</tbody>
</table>
<ol start="2">
<li>Create a <a href="/rules/url-forwarding/single-redirects/create-dashboard/">Single Redirect</a> to forward traffic from your subdomain to your apex domain.</li>
</ol>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/8906.md")
</div>
<h3 id="redirect-the-apex-domain-to-a-subdomain">Redirect the apex domain to a subdomain</h3>
<p>Sometimes, you might want all traffic to your apex domain (<code>example.com</code>) to actually go to a subdomain (<code>www.example.com</code>).</p>
<ol>
<li>
<p>If you have already added that subdomain at your host, create a corresponding <a href="/dns/manage-dns-records/how-to/create-dns-records/">DNS A or CNAME record</a> for that subdomain.</p>
</li>
<li>
<p>Create a proxied DNS A record for your apex domain. This record can point to any IP address since all traffic will be redirected prior to reaching the address.</p>
</li>
</ol>
<table>
<thead>
<tr>
<th><strong>Type</strong></th>
<th><strong>Name</strong></th>
<th><strong>IPv4 address</strong></th>
<th><strong>Proxy status</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td><code>@</code></td>
<td><code>192.0.2.1</code></td>
<td>Proxied</td>
</tr>
</tbody>
</table>
<ol start="3">
<li>Create a <a href="/rules/url-forwarding/single-redirects/create-dashboard/">Single Redirect</a> to forward traffic from your apex domain to your subdomain.</li>
</ol>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/8907.md")
</div>
<h2 id="ssl-tls-for-subdomains">SSL/TLS for subdomains</h2>
<p>If your main domain is using Cloudflare's <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL certificate</a>, that certificate also covers all first-level subdomains (<code>blog.example.com</code>).</p>
<p>For deeper subdomains (<code>dev.blog.example.com</code>), use a <a href="/ssl/edge-certificates/universal-ssl/limitations/#full-setup">different type of certificate</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="proxy-status">Proxy status</h3>
@markup("md", "content/.markup/bodies/8905.md")
</aside>
<h2 id="customize-subdomain-behavior">Customize subdomain behavior</h2>
<p>If you want to customize Cloudflare settings for individual subdomains, your approach will vary depending on your plan.</p>
<p>Enterprise customers can set up custom settings and access for a specific subdomain within Cloudflare with <a href="/dns/zone-setups/subdomain-setup/">Subdomain support</a>.</p>
<p>All other customers can set up subdomain-specific <a href="/rules/configuration-rules/">Configuration Rules</a> or <a href="/rules/page-rules/">Page Rules</a> to alter Cloudflare settings.</p>
<p>If you want a subdomain's DNS settings managed totally outside of Cloudflare — meaning this subdomain can be managed by individuals without access to your Cloudflare account — refer to <a href="/dns/manage-dns-records/how-to/subdomains-outside-cloudflare/">Delegating subdomains outside of Cloudflare</a>.</p>
