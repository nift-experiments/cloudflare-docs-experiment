---
cp9:
  canonical: https://developers.cloudflare.com/kv/reference/data-location/
  description: Learn how the location of data stored in Workers KV is determined, including how you can restrict a namespace to a specific jurisdiction.
  full_title: Data location · Cloudflare Workers KV docs
  head_html: <title>Data location · Cloudflare Workers KV docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how the location of data stored in Workers KV is determined, including how you can restrict a namespace to a specific jurisdiction."><link rel="canonical" href="https://developers.cloudflare.com/kv/reference/data-location/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/kv/reference/data-location/index.md"><meta property="og:title" content="Data location · Cloudflare Workers KV docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how the location of data stored in Workers KV is determined, including how you can restrict a namespace to a specific jurisdiction."><meta property="og:url" content="https://developers.cloudflare.com/kv/reference/data-location/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="KV"><meta name="algolia_product_filter" content="KV"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/kv/reference/data-location/#page","headline":"Data location \u00b7 Cloudflare Workers KV docs","description":"Learn how the location of data stored in Workers KV is determined, including how you can restrict a namespace to a specific jurisdiction.","url":"https://developers.cloudflare.com/kv/reference/data-location/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /kv/reference/data-location/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9496.md")
</aside>
<p>Learn how the location of data stored in Workers KV is determined, including how you can restrict a namespace to a specific jurisdiction.</p>
<h2 id="automatic-default">Automatic (default)</h2>
<p>By default, data written to a Workers KV namespace is replicated globally across Cloudflare's network with no jurisdictional restriction, allowing your data to be read with low latency from anywhere in the world.</p>
<h2 id="restrict-a-namespace-to-a-jurisdiction">Restrict a namespace to a jurisdiction</h2>
<p>Jurisdictions are used to create Workers KV namespaces that only durably store data within a region, to help comply with data locality regulations such as the <a href="https://gdpr-info.eu/">GDPR</a> or <a href="https://blog.cloudflare.com/cloudflare-achieves-fedramp-authorization/">FedRAMP</a>.</p>
<p>Workers may still access a namespace constrained to a jurisdiction from anywhere in the world, and KV data can be cached outside the jurisdiction location on Cloudflare's network. The jurisdiction constraint only controls where the namespace's data is durably stored. Consider using <a href="/data-localization/regional-services/">Regional Services</a> to control the regions from which Cloudflare responds to requests.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9495.md")
</aside>
<h3 id="supported-jurisdictions">Supported jurisdictions</h3>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Location</th>
</tr>
</thead>
<tbody>
<tr>
<td>eu</td>
<td>The European Union</td>
</tr>
<tr>
<td>fedramp</td>
<td>FedRAMP-compliant data centers</td>
</tr>
<tr>
<td>us</td>
<td>The United States of America</td>
</tr>
</tbody>
</table>
<h3 id="get-access">Get access</h3>
<p>Workers KV jurisdictions are in private beta. If you are interested in restricting your namespaces to a supported jurisdiction, contact your Cloudflare account team or <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> to request access.</p>
