---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/
  description: Overview of Tiered policies in Gateway.
  full_title: Tiered policies · Cloudflare One docs
  head_html: <title>Tiered policies · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Overview of Tiered policies in Gateway."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/index.md"><meta property="og:title" content="Tiered policies · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Overview of Tiered policies in Gateway."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/#page","headline":"Tiered policies \u00b7 Cloudflare One docs","description":"Overview of Tiered policies in Gateway.","url":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/traffic-policies/tiered-policies/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6407.md")
</aside>
<p>Gateway tiered policies allow you to share and enforce Gateway policies across multiple Zero Trust accounts. This enables centralized policy management for organizations that manage multiple accounts.</p>
<p>There are two approaches for setting up tiered policies, depending on your deployment model and policy requirements:</p>
<ul>
<li><strong><a href="/cloudflare-one/traffic-policies/tiered-policies/organizations/">Cloudflare Organizations</a></strong> — Share DNS, network, HTTP, and resolver policies across accounts in a Cloudflare Organization using the dashboard.</li>
<li><strong><a href="/cloudflare-one/traffic-policies/tiered-policies/tenant-api/">Tenant API</a></strong> — Manage DNS policies across parent and child accounts for Managed Service Provider (MSP) deployments.</li>
</ul>
<h2 id="organizations-vs-tenant-api">Organizations vs. Tenant API</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th><a href="/cloudflare-one/traffic-policies/tiered-policies/organizations/">Cloudflare Organizations</a></th>
<th><a href="/cloudflare-one/traffic-policies/tiered-policies/tenant-api/">Tenant API</a></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Supported policy types</strong></td>
<td>DNS, Network, HTTP, Resolver</td>
<td>DNS only</td>
</tr>
<tr>
<td><strong>Account model</strong></td>
<td>Source / Recipient accounts</td>
<td>Parent / Child accounts</td>
</tr>
<tr>
<td><strong>Shareable settings</strong></td>
<td>Block pages, extended email matching</td>
<td>Block pages</td>
</tr>
<tr>
<td><strong>Setup</strong></td>
<td>Dashboard (self-serve)</td>
<td>API-only</td>
</tr>
<tr>
<td><strong>Availability</strong></td>
<td>Enterprise (beta)</td>
<td>Enterprise (GA)</td>
</tr>
</tbody>
</table>
