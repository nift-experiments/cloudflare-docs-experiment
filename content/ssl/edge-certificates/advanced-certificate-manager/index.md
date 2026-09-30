---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/
  description: Order advanced certificates with custom SANs, validity periods, and CAs.
  full_title: Advanced certificates · Cloudflare SSL/TLS docs
  head_html: <title>Advanced certificates · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Order advanced certificates with custom SANs, validity periods, and CAs."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/index.md"><meta property="og:title" content="Advanced certificates · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Order advanced certificates with custom SANs, validity periods, and CAs."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/#page","headline":"Advanced certificates \u00b7 Cloudflare SSL/TLS docs","description":"Order advanced certificates with custom SANs, validity periods, and CAs.","url":"https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/advanced-certificate-manager/
  schema: 1
---
<p>Use advanced certificates when you want something more customizable than <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL</a> but still want the convenience of SSL certificate issuance and renewal.</p>
<br />
<p>To order advanced certificates, you must purchase the Advanced Certificate Manager add-on. This add-on also unlocks the features listed below.</p>
<h2 id="what-the-add-on-includes">What the add-on includes</h2>
<p>Advanced Certificate Manager allows you to:</p>
<ul>
<li>Order advanced certificates that can:
<ul>
<li>Include up to 50 hosts as covered hostnames (the zone apex must be one of these 50).</li>
<li>Cover more than one level of subdomain.</li>
<li>Be issued by the certificate authority (CA) you choose.</li>
<li>Use your preferred validation method.</li>
<li>Have the validity period you choose.</li>
</ul>
</li>
<li>Automate <span class="nb-glossary-tooltip" title="domain control validation (DCV)">domain control validation (DCV)</span> for zones on a <span class="nb-glossary-tooltip" title="CNAME setup">CNAME setup</span> using <a href="/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/">delegated DCV</a>.</li>
<li>Enable <a href="/ssl/edge-certificates/additional-options/total-tls/">Total TLS</a> to automatically protect proxied hostnames.</li>
<li>Select a <a href="/ssl/origin-configuration/custom-origin-trust-store/">custom trust store</a> for origin authentication.</li>
<li>Control <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/">cipher suites</a> and <a href="/ssl/edge-certificates/additional-options/minimum-tls/#per-hostname">per-hostname minimum TLS version</a>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14120.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14118.md")
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
<td>Paid add-on</td>
<td>Paid add-on</td>
<td>Paid add-on</td>
<td>Paid add-on</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14117.md")
</aside>
<h2 id="limitations">Limitations</h2>
<p>Advanced certificates do not apply to <a href="/pages/">Cloudflare Pages</a> or <a href="/r2/">R2</a> custom domains. Due to <a href="/ssl/reference/certificate-and-hostname-priority/">certificate prioritization</a>, these products use Cloudflare for SaaS certificates instead.</p>
<p>Advanced certificates are <a href="/ssl/concepts/#validation-level">Domain Validated (DV)</a>. If your organization needs Organization Validated (OV) or Extended Validation (EV) certificates, refer to <a href="/ssl/edge-certificates/custom-certificates/">Custom certificates</a>. <br/></p>
<p>Advanced certificates cover hostnames within a single domain. If you need a certificate that spans multiple domains (a multi-domain certificate), use <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a>. For architecture guidance, refer to <a href="/reference-architecture/design-guides/leveraging-cloudflare-for-your-saas-applications/">Leveraging Cloudflare for your SaaS applications</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14116.md")
</aside>
<h2 id="multi-level-subdomain-support">Multi-level subdomain support</h2>
<p>Advanced Certificate Manager supports deep, multi-level subdomains (for example, <code>api.staging.example.com</code>). There is no arbitrary limit on the number of subdomain levels, but you must consider the following constraints.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14115.md")
</aside>
<h3 id="domain-name-length-limits">Domain name length limits</h3>
<p>These limits are defined by internet standards (<a href="https://www.rfc-editor.org/rfc/rfc1035">RFC 1035</a> and <a href="https://www.rfc-editor.org/rfc/rfc5280">RFC 5280</a>) and apply to all certificates, regardless of the certificate authority:</p>
<ul>
<li><strong>Total domain length</strong>: The entire domain name cannot exceed 253 characters.</li>
<li><strong>Label length</strong>: Each individual level (the text between dots) cannot exceed 63 characters.</li>
<li><strong>Common Name (CN) length</strong>: The Common Name field of a certificate cannot exceed 64 characters. If a hostname on your certificate exceeds 64 characters, you must order the certificate via the <a href="/api/resources/ssl/subresources/certificate_packs/methods/create/">API</a> and set the <code>cloudflare_branding</code> option to <code>true</code>. This places <code>sni.cloudflaressl.com</code> in the CN field and your long hostname in the SAN field. The dashboard does not support ordering certificates with hostnames longer than 64 characters.</li>
</ul>
<h3 id="wildcard-coverage">Wildcard coverage</h3>
<p>Wildcard certificates only cover <strong>one subdomain level</strong>:</p>
<ul>
<li>A certificate for <code>*.example.com</code> covers <code>www.example.com</code> and <code>api.example.com</code> but <strong>not</strong> <code>api.staging.example.com</code>.</li>
<li>To cover multiple levels, you must explicitly add a wildcard for each level to your certificate (for example, <code>*.example.com</code>, <code>*.staging.example.com</code>).</li>
</ul>
<h3 id="hostnames-per-certificate">Hostnames per certificate</h3>
<p>A single advanced certificate can include up to <strong>50 hosts</strong> (SANs) total. The zone apex must be one of these 50, leaving room for up to 49 additional hostnames or wildcards.</p>
<h3 id="consistency-across-certificate-authorities">Consistency across certificate authorities</h3>
<p>The character-length limits above (253-character total, 63-character label, 64-character CN) are defined by IETF standards (<a href="https://www.rfc-editor.org/rfc/rfc1035">RFC 1035</a>, <a href="https://www.rfc-editor.org/rfc/rfc5280">RFC 5280</a>) and apply uniformly across all CAs. Other constraints, such as the per-certificate SAN count and supported validity periods, are Cloudflare advanced certificates limits or vary by CA. Refer to <a href="/ssl/reference/certificate-authorities/">Certificate authorities</a> for CA-specific details.</p>
<h2 id="related-resources">Related resources</h2>
<ul class="directory-listing"><li><a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/">Manage advanced certificates</a></li><li><a href="/ssl/edge-certificates/advanced-certificate-manager/api-commands/">API commands</a></li></ul>
