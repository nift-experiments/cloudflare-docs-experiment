---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/
  description: Scannable API credential formats and leaked token detection.
  full_title: Token formats · Cloudflare Fundamentals docs
  head_html: <title>Token formats · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Scannable API credential formats and leaked token detection."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/index.md"><meta property="og:title" content="Token formats · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Scannable API credential formats and leaked token detection."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare Fundamentals,API documentation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/#page","headline":"Token formats \u00b7 Cloudflare Fundamentals docs","description":"Scannable API credential formats and leaked token detection.","url":"https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/api/get-started/token-formats/
  schema: 1
---
<p>Cloudflare API credentials use a prefixed, scannable format that makes them identifiable by credential scanning tools. Each credential type has a distinct prefix followed by 40 characters and a checksum.</p>
<table>
<thead>
<tr>
<th>Credential type</th>
<th>Description</th>
<th>Format</th>
</tr>
</thead>
<tbody>
<tr>
<td>Global API Key</td>
<td>Global key tied to your user account (full access)</td>
<td><code>cfk_[40 characters][checksum]</code></td>
</tr>
<tr>
<td>User API Token</td>
<td>Scoped token you create for specific permissions</td>
<td><code>cfut_[40 characters][checksum]</code></td>
</tr>
<tr>
<td>Account API Token</td>
<td>Token owned by the account, not tied to a specific user</td>
<td><code>cfat_[40 characters][checksum]</code></td>
</tr>
</tbody>
</table>
<p>Existing tokens continue to work. Every new token you create or <a href="/fundamentals/api/how-to/roll-token/">roll</a> uses the scannable format automatically.</p>
<h2 id="leaked-token-detection">Leaked token detection</h2>
<p>The prefixed format and checksum allow credential scanning tools to detect leaked Cloudflare tokens with high confidence. Cloudflare partners with credential scanning providers to proactively find your leaked tokens and revoke them before they can be used maliciously.</p>
<h3 id="github-secret-scanning">GitHub Secret Scanning</h3>
<p>Cloudflare participates in <a href="https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning">GitHub's Secret Scanning program</a>. GitHub scans every commit for Cloudflare API credentials in both public and private repositories.</p>
<ul>
<li><strong>Public repositories</strong> — When GitHub detects a leaked Cloudflare token, it verifies the token using the checksum and sends Cloudflare a webhook. Cloudflare automatically revokes the token and notifies you by email so you can generate a replacement.</li>
<li><strong>Private repositories</strong> — GitHub notifies you about any leaked Cloudflare tokens so you can rotate them.</li>
</ul>
<h2 id="pre-2026-formats">Pre-2026 formats</h2>
<p>Tokens created before the scannable format was introduced use unprefixed strings. These tokens continue to work. Cloudflare scans for and revokes leaked tokens in both the old and new formats.</p>
<table>
<thead>
<tr>
<th>Credential type</th>
<th>Old format</th>
</tr>
</thead>
<tbody>
<tr>
<td>Global API Key</td>
<td>37–45 character lowercase hex string</td>
</tr>
<tr>
<td>User API Token</td>
<td>40-character alphanumeric string</td>
</tr>
<tr>
<td>Account API Token</td>
<td>40-character alphanumeric string</td>
</tr>
</tbody>
</table>
