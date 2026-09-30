---
cp9:
  canonical: https://developers.cloudflare.com/artifacts/guides/data-localization/
  description: Ensure Artifacts stores and processes repo data only within a selected jurisdiction.
  full_title: Data localization · Cloudflare Artifacts docs
  head_html: <title>Data localization · Cloudflare Artifacts docs</title><meta name="generator" content="Nift"><meta name="description" content="Ensure Artifacts stores and processes repo data only within a selected jurisdiction."><link rel="canonical" href="https://developers.cloudflare.com/artifacts/guides/data-localization/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/artifacts/guides/data-localization/index.md"><meta property="og:title" content="Data localization · Cloudflare Artifacts docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Ensure Artifacts stores and processes repo data only within a selected jurisdiction."><meta property="og:url" content="https://developers.cloudflare.com/artifacts/guides/data-localization/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Artifacts"><meta name="algolia_product_filter" content="Artifacts"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Artifacts"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/artifacts/guides/data-localization/#page","headline":"Data localization \u00b7 Cloudflare Artifacts docs","description":"Ensure Artifacts stores and processes repo data only within a selected jurisdiction.","url":"https://developers.cloudflare.com/artifacts/guides/data-localization/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /artifacts/guides/data-localization/
  schema: 1
---
<p>Artifacts jurisdictions ensure repo data is stored and processed only within a selected location. Set a jurisdiction when you create a namespace to apply the restriction to every repo in that namespace.</p>
<h2 id="supported-jurisdictions">Supported jurisdictions</h2>
<p>Artifacts supports the following jurisdictions:</p>
<table>
<thead>
<tr>
<th>Jurisdiction</th>
<th>Location</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>eu</code></td>
<td>European Union</td>
</tr>
<tr>
<td><code>us</code></td>
<td>United States</td>
</tr>
</tbody>
</table>
<h2 id="create-a-namespace-with-a-jurisdiction">Create a namespace with a jurisdiction</h2>
<p>To restrict a namespace to the European Union, set <code>jurisdiction</code> to <code>eu</code> when you create the namespace:</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;  &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;namespace&quot;: &quot;my-eu-namespace&quot;,&#10;    &quot;jurisdiction&quot;: &quot;eu&quot;&#10;  }&#x27;&#10;</code></pre>
<p>The selected jurisdiction applies to every repo in the namespace. You cannot change the jurisdiction after creating the namespace. The <code>jurisdiction</code> parameter is optional. If you omit it, the namespace remains unrestricted.</p>
<p>For endpoint details, refer to the <a href="/artifacts/api/rest-api/#create-a-namespace">Artifacts REST API reference</a>.</p>
