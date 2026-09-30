---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-03-27-rfc9440-mtls-fields/
  description: New updates and improvements at Cloudflare.
  full_title: New RFC 9440 mTLS certificate fields in Workers · Changelog
  head_html: <title>New RFC 9440 mTLS certificate fields in Workers · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-03-27-rfc9440-mtls-fields/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New RFC 9440 mTLS certificate fields in Workers · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-03-27-rfc9440-mtls-fields/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-27-rfc9440-mtls-fields/#page","headline":"New RFC 9440 mTLS certificate fields in Workers \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-03-27-rfc9440-mtls-fields/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-03-27-rfc9440-mtls-fields/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 27, 2026</time><h2 id="post-title">New RFC 9440 mTLS certificate fields in Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Four new fields are now available on <code>request.cf.tlsClientAuth</code> in Workers for requests that include a mutual TLS (mTLS) client certificate. These fields encode the client certificate and its intermediate chain in <a href="https://www.rfc-editor.org/rfc/rfc9440">RFC 9440</a> format — the same standard format used by the <code>Client-Cert</code> and <code>Client-Cert-Chain</code> HTTP headers — so your Worker can forward them directly to your origin without any custom parsing or encoding logic.</p>
<h4 id="new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>certRFC9440</code></td>
<td>String</td>
<td>The client leaf certificate in RFC 9440 format (<code>:base64-DER:</code>). Empty if no client certificate was presented.</td>
</tr>
<tr>
<td><code>certRFC9440TooLarge</code></td>
<td>Boolean</td>
<td><code>true</code> if the leaf certificate exceeded 10 KB and was omitted from <code>certRFC9440</code>.</td>
</tr>
<tr>
<td><code>certChainRFC9440</code></td>
<td>String</td>
<td>The intermediate certificate chain in RFC 9440 format as a comma-separated list. Empty if no intermediates were sent or if the chain exceeded 16 KB.</td>
</tr>
<tr>
<td><code>certChainRFC9440TooLarge</code></td>
<td>Boolean</td>
<td><code>true</code> if the intermediate chain exceeded 16 KB and was omitted from <code>certChainRFC9440</code>.</td>
</tr>
</tbody>
</table>
<h4 id="example-forwarding-client-certificate-headers-to-your-origin">Example: forwarding client certificate headers to your origin</h4>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request) {&#10;    const tls = request.cf.tlsClientAuth;&#10;&#10;    // Only forward if cert was verified and chain is complete&#10;    if (!tls || !tls.certVerified || tls.certRevoked || tls.certChainRFC9440TooLarge) {&#10;      return new Response(&quot;Unauthorized&quot;, { status: 401 });&#10;    }&#10;&#10;    const headers = new Headers(request.headers);&#10;    headers.set(&quot;Client-Cert&quot;, tls.certRFC9440);&#10;    headers.set(&quot;Client-Cert-Chain&quot;, tls.certChainRFC9440);&#10;&#10;    return fetch(new Request(request, { headers }));&#10;  },&#10;};&#10;</code></pre>
<p>For more information, refer to <a href="/ssl/client-certificates/client-certificate-variables/#workers-variables">Client certificate variables</a> and <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">Mutual TLS authentication</a>.</p>
</div></article></div>
