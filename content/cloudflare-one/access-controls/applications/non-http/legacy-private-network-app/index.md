---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/legacy-private-network-app/
  description: Private network applications (legacy) in Access.
  full_title: Private network applications (legacy) · Cloudflare One docs
  head_html: <title>Private network applications (legacy) · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Private network applications (legacy) in Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/legacy-private-network-app/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/legacy-private-network-app/index.md"><meta property="og:title" content="Private network applications (legacy) · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Private network applications (legacy) in Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/legacy-private-network-app/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/legacy-private-network-app/#page","headline":"Private network applications (legacy) \u00b7 Cloudflare One docs","description":"Private network applications (legacy) in Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/legacy-private-network-app/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/non-http/legacy-private-network-app/
  schema: 1
---
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4793.md")
</aside>
<p>Existing <strong>Private Network</strong> applications continue to function and can still be managed. These applications were originally configured with the following steps:</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong> &gt; <strong>Add an application</strong>.</p>
</li>
<li>
<p>Select <strong>Private Network</strong>.</p>
</li>
<li>
<p>Name your application.</p>
</li>
<li>
<p>For <strong>Application type</strong>, select <em>Destination IP</em>.</p>
</li>
<li>
<p>For <strong>Value</strong>, enter the IP address for your application (for example, <code>10.128.0.7</code>).</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4792.md")
</aside>
<ol start="6">
<li>
<p>Configure your <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a> visibility and logo.</p>
</li>
<li>
<p>Select <strong>Next</strong>. You will see two auto-generated Gateway Network policies: one that allows access to the destination IP and another that blocks access.</p>
</li>
<li>
<p>Modify the policies to include additional identity-based conditions. For example:</p>
<ul>
<li><strong>Policy 1</strong></li>
</ul>
</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Destination IP</td>
<td>in</td>
<td><code>10.128.0.7</code></td>
<td>And</td>
<td>Allow</td>
</tr>
<tr>
<td>User Email</td>
<td>matches regex</td>
<td><code>.*@example.com</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<ul>
<li><strong>Policy 2</strong></li>
</ul>
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
<td>Destination IP</td>
<td>in</td>
<td><code>10.128.0.7</code></td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>Policies are evaluated in <a href="/cloudflare-one/traffic-policies/order-of-enforcement/#order-of-precedence">numerical order</a>, so a user with an email ending in @example.com will be able to access <code>10.128.0.7</code> while all others will be blocked. For more information on building network policies, refer to our <a href="/cloudflare-one/traffic-policies/network-policies/">dedicated documentation</a>.</p>
<ol start="9">
<li>Select <strong>Add application</strong>.</li>
</ol>
<p>Your application will appear on the <strong>Applications</strong> page.</p>
