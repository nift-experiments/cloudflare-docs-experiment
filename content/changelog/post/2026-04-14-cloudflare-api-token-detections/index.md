---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-api-token-detections/
  description: New updates and improvements at Cloudflare.
  full_title: Detect Cloudflare API tokens with DLP · Changelog
  head_html: <title>Detect Cloudflare API tokens with DLP · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-api-token-detections/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Detect Cloudflare API tokens with DLP · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-api-token-detections/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-api-token-detections/#page","headline":"Detect Cloudflare API tokens with DLP \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-14-cloudflare-api-token-detections/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-14-cloudflare-api-token-detections/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 14, 2026</time><h2 id="post-title">Detect Cloudflare API tokens with DLP</h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>The <strong>Credentials and Secrets</strong> DLP profile now includes three new predefined entries for detecting Cloudflare API credentials:</p>
<table>
<thead>
<tr>
<th>Entry name</th>
<th>Token prefix</th>
<th>Detects</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare User API Key</td>
<td><code>cfk_</code></td>
<td>User-scoped API keys</td>
</tr>
<tr>
<td>Cloudflare User API Token</td>
<td><code>cfut_</code></td>
<td>User-scoped API tokens</td>
</tr>
<tr>
<td>Cloudflare Account Owned API Token</td>
<td><code>cfat_</code></td>
<td>Account-scoped API tokens</td>
</tr>
</tbody>
</table>
<p>These detections target the new <a href="/fundamentals/api/get-started/token-formats/">Cloudflare API credential format</a>, which uses a structured prefix and a CRC32 checksum suffix. The identifiable prefix makes it possible to detect leaked credentials with high confidence and low false positive rates — no surrounding context such as <code>Authorization: Bearer</code> headers is required.</p>
<p>Credentials generated before this format change will not be matched by these entries.</p>
<h4 id="how-to-enable-cloudflare-api-token-detections">How to enable Cloudflare API token detections</h4>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>DLP</strong> &gt; <strong>DLP Profiles</strong>.</li>
<li>Select the <strong>Credentials and Secrets</strong> profile.</li>
<li>Turn on one or more of the new Cloudflare API token entries.</li>
<li>Use the profile in a Gateway HTTP policy to log or block traffic containing these credentials.</li>
</ol>
<p>Example policy:</p>
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
<td>DLP Profile</td>
<td>in</td>
<td><em>Credentials and Secrets</em></td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>You can also enable individual entries to scope detection to specific credential types — for example, enabling <strong>Account Owned API Token</strong> detection without enabling <strong>User API Key</strong> detection.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">predefined DLP profiles</a>.</p>
</div></article></div>
