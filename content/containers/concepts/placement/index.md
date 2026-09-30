---
cp9:
  canonical: https://developers.cloudflare.com/containers/concepts/placement/
  description: Control where your containers run with regional and jurisdictional constraints.
  full_title: Placement · Cloudflare Containers docs
  head_html: <title>Placement · Cloudflare Containers docs</title><meta name="generator" content="Nift"><meta name="description" content="Control where your containers run with regional and jurisdictional constraints."><link rel="canonical" href="https://developers.cloudflare.com/containers/concepts/placement/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/containers/concepts/placement/index.md"><meta property="og:title" content="Placement · Cloudflare Containers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Control where your containers run with regional and jurisdictional constraints."><meta property="og:url" content="https://developers.cloudflare.com/containers/concepts/placement/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Containers"><meta name="algolia_product_filter" content="Containers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Containers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/containers/concepts/placement/#page","headline":"Placement \u00b7 Cloudflare Containers docs","description":"Control where your containers run with regional and jurisdictional constraints.","url":"https://developers.cloudflare.com/containers/concepts/placement/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /containers/concepts/placement/
  schema: 1
---
<p>By default, containers run in the location nearest to the incoming request with a pre-fetched image. Use placement constraints to restrict where your containers run for data residency, compliance, or latency requirements.</p>
<h2 id="regional-constraints">Regional constraints</h2>
<p>Use the <code>regions</code> constraint to limit container placement to specific geographic areas:</p>
<table>
<thead>
<tr>
<th>Region</th>
<th>Description</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ENAM</code></td>
<td>Eastern North America</td>
<td></td>
</tr>
<tr>
<td><code>WNAM</code></td>
<td>Western North America</td>
<td></td>
</tr>
<tr>
<td><code>EEUR</code></td>
<td>Eastern Europe</td>
<td></td>
</tr>
<tr>
<td><code>WEUR</code></td>
<td>Western Europe</td>
<td></td>
</tr>
<tr>
<td><code>APAC</code></td>
<td>Asia Pacific</td>
<td></td>
</tr>
<tr>
<td><code>SAM</code></td>
<td>South America</td>
<td></td>
</tr>
<tr>
<td><code>ME</code></td>
<td>Middle East</td>
<td>Limited capacity</td>
</tr>
<tr>
<td><code>OC</code></td>
<td>Oceania</td>
<td>Limited capacity</td>
</tr>
<tr>
<td><code>AFR</code></td>
<td>Africa</td>
<td>Limited capacity</td>
</tr>
</tbody>
</table>
<p>Limited capacity regions (ME, OC, AFR) cannot be used exclusively. Include at least one other region, or contact support for dedicated access.</p>
<h2 id="jurisdictional-constraints">Jurisdictional constraints</h2>
<p>Use the <code>jurisdiction</code> constraint to restrict containers to compliance boundaries:</p>
<table>
<thead>
<tr>
<th>Jurisdiction</th>
<th>Regions</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>eu</code></td>
<td>EEUR, WEUR</td>
<td>EU data residency</td>
</tr>
<tr>
<td><code>fedramp</code></td>
<td>ENAM, WNAM</td>
<td>FedRAMP regions</td>
</tr>
</tbody>
</table>
<p>When you specify both <code>jurisdiction</code> and <code>regions</code>, the regions must be valid for that jurisdiction. For example, specifying <code>jurisdiction: &quot;eu&quot;</code> with <code>regions: [&quot;ENAM&quot;]</code> is invalid.</p>
<h2 id="configure-placement">Configure placement</h2>
<p>Set placement constraints in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7152.md")
</div>
<p>Refer to <a href="/containers/concepts/architecture/">Lifecycle of a Container</a> for more details on how placement affects container startup and routing.</p>
