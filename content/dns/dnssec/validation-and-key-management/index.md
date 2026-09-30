---
cp9:
  canonical: https://developers.cloudflare.com/dns/dnssec/validation-and-key-management/
  description: DNSSEC key types, rotation, and validation behavior.
  full_title: Validation and keys · Cloudflare DNS docs
  head_html: <title>Validation and keys · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="DNSSEC key types, rotation, and validation behavior."><link rel="canonical" href="https://developers.cloudflare.com/dns/dnssec/validation-and-key-management/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/dnssec/validation-and-key-management/index.md"><meta property="og:title" content="Validation and keys · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="DNSSEC key types, rotation, and validation behavior."><meta property="og:url" content="https://developers.cloudflare.com/dns/dnssec/validation-and-key-management/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/dnssec/validation-and-key-management/#page","headline":"Validation and keys \u00b7 Cloudflare DNS docs","description":"DNSSEC key types, rotation, and validation behavior.","url":"https://developers.cloudflare.com/dns/dnssec/validation-and-key-management/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/dnssec/validation-and-key-management/
  schema: 1
---
<p>Refer to the sections below for an overview of some technical concepts and how they apply to Cloudflare DNSSEC. For broader content on DNSSEC, refer to <a href="https://www.cloudflare.com/dns/dnssec/how-dnssec-works/">How DNSSEC works</a>.</p>
<h2 id="chain-of-trust">Chain of trust</h2>
<p>DNSSEC validation follows a chain of trust from the root DNS servers to your zone:</p>
<ol>
<li>A resolver queries your parent registry (for example, <code>.com</code>) for your DS record.</li>
<li>The DS record contains a hash of your Key Signing Key (KSK).</li>
<li>The resolver expects all Zone Signing Keys (ZSK) to be signed by that specific KSK.</li>
<li>If Cloudflare uses a different KSK, validation fails when resolvers query Cloudflare nameservers.</li>
</ol>
<p>This is why you cannot simply keep your existing DS record when migrating to Cloudflare. The cryptographic chain of trust requires either:</p>
<ul>
<li><a href="/dns/dnssec/">Disabling DNSSEC</a> before migration and re-enabling it on Cloudflare</li>
<li>Using the <a href="/dns/dnssec/multi-signer-dnssec/about/">multi-signer DNSSEC</a> approach to coordinate keys between providers.</li>
</ul>
<hr />
<h2 id="automatic-ds-record-updates">Automatic DS record updates</h2>
<p>When you enable DNSSEC, Cloudflare automatically publishes <strong>CDS</strong> (Child Delegation Signer) and <strong>CDNSKEY</strong> (Child DNSKEY) records in your zone. These records automate the chain of trust management between your domain and the Top-Level Domain registry.</p>
<table>
<thead>
<tr>
<th>Record</th>
<th>Purpose</th>
<th>Contents</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>CDS</strong></td>
<td>High-level instruction</td>
<td>A hashed version of the public key (same data as a DS record)</td>
</tr>
<tr>
<td><strong>CDNSKEY</strong></td>
<td>Public key instruction</td>
<td>The full public Key Signing Key (KSK) for the parent to generate its own DS record</td>
</tr>
</tbody>
</table>
<p>Registrars that support <a href="https://www.rfc-editor.org/rfc/rfc8078.html">RFC 8078</a> periodically scan your domain for these records and automatically update the DS record at the registry level. This eliminates manual DS record management and ensures seamless key rollovers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7676.md")
</aside>
<hr />
<h2 id="dnskey-flags">DNSKEY flags</h2>
<ul>
<li><strong>ZSKs (Zone Signing Keys)</strong>: flag <code>256</code></li>
<li><strong>KSKs (Key Signing Keys)</strong>: flag <code>257</code></li>
</ul>
