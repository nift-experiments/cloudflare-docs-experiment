---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-27-new-protocol-detection-protocols/
  description: New updates and improvements at Cloudflare.
  full_title: New protocols added for Gateway Protocol Detection (Beta) · Changelog
  head_html: <title>New protocols added for Gateway Protocol Detection (Beta) · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-27-new-protocol-detection-protocols/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New protocols added for Gateway Protocol Detection (Beta) · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-27-new-protocol-detection-protocols/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-27-new-protocol-detection-protocols/#page","headline":"New protocols added for Gateway Protocol Detection (Beta) \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-27-new-protocol-detection-protocols/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-27-new-protocol-detection-protocols/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 27, 2026</time><h2 id="post-title">New protocols added for Gateway Protocol Detection (Beta)</h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>Gateway <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">Protocol Detection</a> now supports seven additional protocols in beta:</p>
<table>
<thead>
<tr>
<th>Protocol</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>IMAP</td>
<td>Internet Message Access Protocol — email retrieval</td>
</tr>
<tr>
<td>POP3</td>
<td>Post Office Protocol v3 — email retrieval</td>
</tr>
<tr>
<td>SMTP</td>
<td>Simple Mail Transfer Protocol — email sending</td>
</tr>
<tr>
<td>MYSQL</td>
<td>MySQL database wire protocol</td>
</tr>
<tr>
<td>RSYNC-DAEMON</td>
<td>rsync daemon protocol</td>
</tr>
<tr>
<td>LDAP</td>
<td>Lightweight Directory Access Protocol</td>
</tr>
<tr>
<td>NTP</td>
<td>Network Time Protocol</td>
</tr>
</tbody>
</table>
<p>These protocols join the existing set of detected protocols (HTTP, HTTP2, SSH, TLS, DCERPC, MQTT, and TPKT) and can be used with the <em>Detected Protocol</em> selector in <a href="/cloudflare-one/traffic-policies/network-policies/">Network policies</a> to identify and filter traffic based on the application-layer protocol, without relying on port-based identification.</p>
<p>If protocol detection is enabled on your account, these protocols will automatically be logged when detected in your Gateway network traffic.</p>
<p>For more information on using Protocol Detection, refer to the <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">Protocol detection documentation</a>.</p>
</div></article></div>
