---
cp9:
  canonical: https://developers.cloudflare.com/artifacts/api/errors/
  description: Error codes returned by the Artifacts REST API and Workers binding.
  full_title: Errors · Artifacts · Cloudflare Artifacts docs
  head_html: <title>Errors · Artifacts · Cloudflare Artifacts docs</title><meta name="generator" content="Nift"><meta name="description" content="Error codes returned by the Artifacts REST API and Workers binding."><link rel="canonical" href="https://developers.cloudflare.com/artifacts/api/errors/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/artifacts/api/errors/index.md"><meta property="og:title" content="Errors · Artifacts · Cloudflare Artifacts docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Error codes returned by the Artifacts REST API and Workers binding."><meta property="og:url" content="https://developers.cloudflare.com/artifacts/api/errors/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Artifacts"><meta name="algolia_product_filter" content="Artifacts"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Artifacts"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/artifacts/api/errors/#page","headline":"Errors \u00b7 Artifacts \u00b7 Cloudflare Artifacts docs","description":"Error codes returned by the Artifacts REST API and Workers binding.","url":"https://developers.cloudflare.com/artifacts/api/errors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /artifacts/api/errors/
  schema: 1
---
<p>This is a list of Artifacts errors.</p>
<h2 id="error-codes">Error codes</h2>
<table>
<thead>
<tr>
<th>Name</th>
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ALREADY_EXISTS</code></td>
<td>10201</td>
<td>The target repository already exists in the namespace.</td>
</tr>
<tr>
<td><code>NOT_FOUND</code></td>
<td>10200</td>
<td>The repository or remote resource does not exist.</td>
</tr>
<tr>
<td><code>IMPORT_IN_PROGRESS</code></td>
<td>10302</td>
<td>The repository is still being imported and is not yet available.</td>
</tr>
<tr>
<td><code>FORK_IN_PROGRESS</code></td>
<td>10303</td>
<td>The repository is still being forked and is not yet available.</td>
</tr>
<tr>
<td><code>INVALID_INPUT</code></td>
<td>10100</td>
<td>A request parameter is missing, malformed, or outside the accepted range.</td>
</tr>
<tr>
<td><code>INVALID_REPO_NAME</code></td>
<td>10101</td>
<td>The repository name does not meet naming requirements.</td>
</tr>
<tr>
<td><code>INVALID_TTL</code></td>
<td>10103</td>
<td>The token TTL is outside the allowed range (60–31,536,000 seconds).</td>
</tr>
<tr>
<td><code>INVALID_URL</code></td>
<td>10104</td>
<td>The source URL does not point to a valid git repository.</td>
</tr>
<tr>
<td><code>REMOTE_AUTH_REQUIRED</code></td>
<td>10106</td>
<td>The remote repository requires authentication.</td>
</tr>
<tr>
<td><code>UPSTREAM_UNAVAILABLE</code></td>
<td>10401</td>
<td>The remote git server could not be reached.</td>
</tr>
<tr>
<td><code>MEMORY_LIMIT</code></td>
<td>10402</td>
<td>The operation exceeds service memory limits.</td>
</tr>
<tr>
<td><code>INTERNAL_ERROR</code></td>
<td>10400</td>
<td>An unexpected internal error occurred.</td>
</tr>
</tbody>
</table>
