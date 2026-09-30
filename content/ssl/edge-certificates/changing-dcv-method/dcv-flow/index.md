---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/dcv-flow/
  description: Consider the steps that have to take place before the DCV process is completed and certificate authorities can issue SSL/TLS certificates.
  full_title: Domain control validation flow · Cloudflare SSL/TLS docs
  head_html: <title>Domain control validation flow · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Consider the steps that have to take place before the DCV process is completed and certificate authorities can issue SSL/TLS certificates."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/dcv-flow/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/dcv-flow/index.md"><meta property="og:title" content="Domain control validation flow · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Consider the steps that have to take place before the DCV process is completed and certificate authorities can issue SSL/TLS certificates."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/dcv-flow/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/dcv-flow/#page","headline":"Domain control validation flow \u00b7 Cloudflare SSL/TLS docs","description":"Consider the steps that have to take place before the DCV process is completed and certificate authorities can issue SSL/TLS certificates.","url":"https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/dcv-flow/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/changing-dcv-method/dcv-flow/
  schema: 1
---
<p>To obtain <a href="/ssl/edge-certificates/universal-ssl/">Universal</a>, <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced</a>, and <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/">Custom hostname</a> certificates, Cloudflare partners with different publicly trusted <a href="/ssl/reference/certificate-authorities/">certificate authorities (CAs)</a>.</p>
<p>However, every time a CA is requested to issue or renew a certificate, the requester must prove that they have control over the domain. That is when the DCV process takes place, with the proof usually consisting of placing an HTTP token at a standard URL path (<code>/.well-known/pki-validation</code>), or placing a TXT record at the authoritative DNS provider.</p>
<h2 id="where-cloudflare-sits-in-the-dcv-process">Where Cloudflare sits in the DCV process</h2>
<p>For the use cases mentioned above, there are three different parties involved in the process:</p>
<ul>
<li>The website or application for which the certificate is issued.</li>
<li>The requester (Cloudflare).</li>
<li>The CA that processes the request.</li>
</ul>
<h2 id="steps-in-the-process">Steps in the process</h2>
<p>In summary, five steps have to succeed after Cloudflare requests a CA to issue or renew a certificate:</p>
<ol>
<li>Cloudflare receives the DCV tokens from the CA.</li>
<li>Cloudflare either places the tokens on your behalf (<a href="/dns/zone-setups/full-setup/">Full DNS setup</a>, <a href="/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/">Delegated DCV</a>), or makes the tokens available for you to place them.</li>
<li>Cloudflare polls the validation URLs to check for the tokens.</li>
<li>After Cloudflare can confirm that the tokens are placed via multiple DNS resolvers, the CA is asked to check as well.</li>
<li>If the CA can confirm the tokens are placed, the certificate gets issued. If the CA cannot confirm the tokens are placed, the certificate is not issued and the tokens are no longer valid.</li>
</ol>
<h2 id="aspects-to-consider">Aspects to consider</h2>
<ul>
<li>Settings that interfere with the validation URLs - firewall blocks or misconfigured DNSSEC, for example - can cause issues with your certificate issuance or renewal. Refer to the <a href="/ssl/edge-certificates/changing-dcv-method/troubleshooting/">troubleshooting guide</a>.</li>
<li></li>
</ul>
<p>When your certificate is in <code>pending_validation</code> and valid tokens are in place, some security features targeting your zone's path for <code>/.well-known/*</code> can be automatically bypassed.</p>
<ul>
<li>Certificate authority authorization (CAA) records may block certificate issuance. Refer to <a href="/ssl/edge-certificates/caa-records/">CAA records</a>.</li>
</ul>
<h3 id="dcv-tokens">DCV tokens</h3>
<p>DCV tokens are generated and controlled by the CA and not by Cloudflare. You can find further technical specification of how they work in <a href="https://www.rfc-editor.org/rfc/rfc8555#section-7.1.5">RFC 8555</a>.</p>
<ul>
<li>
<p>As mentioned in <a href="#steps-in-the-process">Step 5</a>, DCV tokens will change upon verification failures. For example, if a DCV check fails because of a DNSSEC issue, the certificate order is no longer valid and Cloudflare must start a new certificate request. Since tokens cannot be reused, a new token is required.</p>
</li>
<li>
<p>DCV tokens also have <a href="/ssl/edge-certificates/changing-dcv-method/validation-backoff-schedule/">validity periods</a>. If you are handling the DCV process manually, it is recommended that you place the tokens as soon as the certificate is up for renewal. Otherwise, the tokens may expire and new tokens will be required.</p>
</li>
</ul>
