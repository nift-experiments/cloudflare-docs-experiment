---
cp9:
  canonical: https://developers.cloudflare.com/registrar/account-options/domain-ownership-certificate/
  description: Generate a domain ownership certificate (WHOIS ownership letter) for a domain registered with Cloudflare Registrar.
  full_title: Domain ownership certificate · Cloudflare Registrar docs
  head_html: <title>Domain ownership certificate · Cloudflare Registrar docs</title><meta name="generator" content="Nift"><meta name="description" content="Generate a domain ownership certificate (WHOIS ownership letter) for a domain registered with Cloudflare Registrar."><link rel="canonical" href="https://developers.cloudflare.com/registrar/account-options/domain-ownership-certificate/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/registrar/account-options/domain-ownership-certificate/index.md"><meta property="og:title" content="Domain ownership certificate · Cloudflare Registrar docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Generate a domain ownership certificate (WHOIS ownership letter) for a domain registered with Cloudflare Registrar."><meta property="og:url" content="https://developers.cloudflare.com/registrar/account-options/domain-ownership-certificate/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Registrar"><meta name="algolia_product_filter" content="Registrar"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Registrar"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/registrar/account-options/domain-ownership-certificate/#page","headline":"Domain ownership certificate \u00b7 Cloudflare Registrar docs","description":"Generate a domain ownership certificate (WHOIS ownership letter) for a domain registered with Cloudflare Registrar.","url":"https://developers.cloudflare.com/registrar/account-options/domain-ownership-certificate/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /registrar/account-options/domain-ownership-certificate/
  schema: 1
---
<p>A domain ownership certificate is a PDF letter that certifies Cloudflare is the registrar of record for your domain and lists the domain's current registration data. You can use it as proof of ownership when a third party (such as a bank, marketplace, or legal entity) requires written confirmation that you control the domain.</p>
<p>The certificate is generated on demand and is automatically populated with your domain's current WHOIS information and the date it was generated. It includes:</p>
<ul>
<li>A certification statement confirming that Cloudflare, an ICANN-accredited registrar, is the registrar for the domain.</li>
<li><strong>Exhibit A</strong>, containing the domain's registration data:
<ul>
<li>Creation date and registry expiry date.</li>
<li>Registrant, administrative, technical, and billing contacts.</li>
<li>Name servers.</li>
</ul>
</li>
</ul>
<p>The contact details shown on the certificate reflect the authoritative contact information Cloudflare has on file, not the redacted values published in public WHOIS. To review or update this information, refer to <a href="/registrar/account-options/domain-contact-updates/">Registrant contact updates</a>.</p>
<h2 id="generate-a-certificate">Generate a certificate</h2>
<p>To download a domain ownership certificate:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/12763.md")
</div>
<p>Your browser downloads a PDF named <code>&lt;domain&gt;_ownership_letter.pdf</code>.</p>
<h2 id="prerequisites-and-restrictions">Prerequisites and restrictions</h2>
<p>You can only generate a certificate when:</p>
<ul>
<li>The domain is registered with (sponsored by) Cloudflare Registrar.</li>
<li>You have permission to view the domain's contact information.</li>
<li>The domain has registrant contact information on file.</li>
</ul>
<p>If any of these conditions are not met, the certificate cannot be generated.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12762.md")
</aside>
