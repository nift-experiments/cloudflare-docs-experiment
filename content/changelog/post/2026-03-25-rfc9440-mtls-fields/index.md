---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-03-25-rfc9440-mtls-fields/
  description: New updates and improvements at Cloudflare.
  full_title: New mTLS certificate fields for Transform Rules · Changelog
  head_html: <title>New mTLS certificate fields for Transform Rules · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-03-25-rfc9440-mtls-fields/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New mTLS certificate fields for Transform Rules · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-03-25-rfc9440-mtls-fields/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-25-rfc9440-mtls-fields/#page","headline":"New mTLS certificate fields for Transform Rules \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-03-25-rfc9440-mtls-fields/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-03-25-rfc9440-mtls-fields/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 25, 2026</time><h2 id="post-title">New mTLS certificate fields for Transform Rules</h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>Cloudflare now exposes four new fields in the Transform Rules phase that encode client certificate data in <a href="https://www.rfc-editor.org/rfc/rfc9440">RFC 9440</a> format. Previously, forwarding client certificate information to your origin required custom parsing of PEM-encoded fields or non-standard HTTP header formats. These new fields produce output in the standardized <code>Client-Cert</code> and <code>Client-Cert-Chain</code> header format defined by RFC 9440, so your origin can consume them directly without any additional decoding logic.</p>
<p>Each certificate is DER-encoded, Base64-encoded, and wrapped in colons. For example, <code>:MIIDsT...Vw==:</code>. A chain of intermediates is expressed as a comma-separated list of such values.</p>
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
<td><code>cf.tls_client_auth.cert_rfc9440</code></td>
<td>String</td>
<td>The client leaf certificate in RFC 9440 format. Empty if no client certificate was presented.</td>
</tr>
<tr>
<td><code>cf.tls_client_auth.cert_rfc9440_too_large</code></td>
<td>Boolean</td>
<td><code>true</code> if the leaf certificate exceeded 10 KB and was omitted. In practice this will almost always be <code>false</code>.</td>
</tr>
<tr>
<td><code>cf.tls_client_auth.cert_chain_rfc9440</code></td>
<td>String</td>
<td>The intermediate certificate chain in RFC 9440 format as a comma-separated list. Empty if no intermediate certificates were sent or if the chain exceeded 16 KB.</td>
</tr>
<tr>
<td><code>cf.tls_client_auth.cert_chain_rfc9440_too_large</code></td>
<td>Boolean</td>
<td><code>true</code> if the intermediate chain exceeded 16 KB and was omitted.</td>
</tr>
</tbody>
</table>
<p>The chain encoding follows the same ordering as the TLS handshake: the certificate closest to the leaf appears first, working up toward the trust anchor. The root certificate is not included.</p>
<h4 id="example-forwarding-client-certificate-headers-to-your-origin-server">Example: Forwarding client certificate headers to your origin server</h4>
<p>Add a request header transform rule to set the <code>Client-Cert</code> and <code>Client-Cert-Chain</code> headers on requests forwarded to your origin server. For example, to forward headers for verified, non-revoked certificates:</p>
<p><strong>Rule expression:</strong></p>
<pre tabindex="0"><code class="language-txt">cf.tls_client_auth.cert_verified and not cf.tls_client_auth.cert_revoked&#10;</code></pre>
<p><strong>Header modifications:</strong></p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Header name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Set</td>
<td><code>Client-Cert</code></td>
<td><code>cf.tls_client_auth.cert_rfc9440</code></td>
</tr>
<tr>
<td>Set</td>
<td><code>Client-Cert-Chain</code></td>
<td><code>cf.tls_client_auth.cert_chain_rfc9440</code></td>
</tr>
</tbody>
</table>
<p>To get the most out of these fields, upload your client CA certificate to Cloudflare so that Cloudflare validates the client certificate at the edge and populates <code>cf.tls_client_auth.cert_verified</code> and <code>cf.tls_client_auth.cert_revoked</code>.</p>
<aside class="nb-aside caution">
<h4 class="nb-aside-title" id="prevent-header-injection">Prevent header injection</h4>
@markup("md", "content/.markup/bodies/17749.md")</aside>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">Mutual TLS authentication</a>, <a href="/rules/transform/request-header-modification/">Request Header Transform Rules</a>, and the <a href="/ruleset-engine/rules-language/fields/reference/">fields reference</a>.</p>
</div></article></div>
