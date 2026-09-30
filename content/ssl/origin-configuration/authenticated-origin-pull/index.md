---
cp9:
  canonical: https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/
  description: Authenticated Origin Pulls helps ensure requests to your origin server come from the Cloudflare network.
  full_title: Authenticated Origin Pulls (mTLS) · Cloudflare SSL/TLS docs
  head_html: <title>Authenticated Origin Pulls (mTLS) · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Authenticated Origin Pulls helps ensure requests to your origin server come from the Cloudflare network."><link rel="canonical" href="https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/index.md"><meta property="og:title" content="Authenticated Origin Pulls (mTLS) · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Authenticated Origin Pulls helps ensure requests to your origin server come from the Cloudflare network."><meta property="og:url" content="https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="mTLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/#page","headline":"Authenticated Origin Pulls (mTLS) \u00b7 Cloudflare SSL/TLS docs","description":"Authenticated Origin Pulls helps ensure requests to your origin server come from the Cloudflare network.","url":"https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["mTLS"]}</script>
  markdown: true
  noindex: false
  route: /ssl/origin-configuration/authenticated-origin-pull/
  schema: 1
---
<p>Authenticated Origin Pulls (AOP) helps ensure requests to your origin server come from the Cloudflare network, which provides an additional layer of security on top of <a href="/ssl/origin-configuration/ssl-modes/full/">Full</a> or <a href="/ssl/origin-configuration/ssl-modes/full-strict/">Full (strict)</a> encryption modes.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="check-your-encryption-mode">Check your encryption mode</h3>
@markup("md", "content/.markup/bodies/14283.md")
</aside>
<p>Without AOP, anyone who discovers your origin server's IP address can send requests directly, bypassing Cloudflare and all its protections. When you combine AOP with the <a href="/waf/">Cloudflare Web Application Firewall (WAF)</a>, your origin only accepts requests that have passed through Cloudflare, which means every request is evaluated by the WAF before reaching your server.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="not-compatible-with-cloudflare-tunnel">Not compatible with Cloudflare Tunnel</h3>
@markup("md", "content/.markup/bodies/14282.md")
</aside>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="configuration-levels">Configuration levels</h2>
<p>AOP has three independent configuration levels. Each uses its own certificate and enablement setting, and each requires configuration on your origin server. Refer to the specific setup guides for details.</p>
<ul>
<li>
<p><a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/global/">Global</a>: Uses a Cloudflare-provided certificate that is shared across all Cloudflare accounts. Applies to all proxied traffic on the zone. This is the simplest setup but only guarantees that a request is coming from the Cloudflare network.</p>
</li>
<li>
<p><a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/">Zone-level</a>: Uses a certificate that you upload. Applies to all proxied traffic on the zone. Provides stricter security because the certificate is exclusive to your account. Zone-level certificates take precedence over global certificates.</p>
</li>
<li>
<p><a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/">Per-hostname</a>: Uses a certificate that you upload, applied to specific hostnames. Per-hostname certificates take precedence over zone-level and global certificates for the specified hostname.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14281.md")
</aside>
<h2 id="when-to-use-your-own-certificate">When to use your own certificate</h2>
<p>Global AOP uses a Cloudflare-provided certificate shared across all accounts, so it only proves a request came from the Cloudflare network — not from your account specifically. If you need to guarantee requests come from your account, set up <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/">zone-level</a> or <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/">per-hostname</a> AOP with your own certificate.</p>
<p>Using your own certificate is also required for <a href="https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards">FIPS</a> compliance. For broader origin protection guidance, refer to <a href="/fundamentals/security/protect-your-origin-server/">Protect your origin server</a>.</p>
<h2 id="post-quantum-certificates">Post-quantum certificates</h2>
<p>Zone-level and per-hostname AOP support ML-DSA (FIPS 204) post-quantum client certificates. Refer to <a href="/ssl/post-quantum-cryptography/pqc-to-origin/#post-quantum-signatures">Post-quantum signatures</a> for certificate generation and upload guidance.</p>
<h2 id="related-topics">Related topics</h2>
<ul>
<li><a href="/ssl/origin-configuration/ssl-modes/">SSL/TLS Encryption Modes</a></li>
</ul>
