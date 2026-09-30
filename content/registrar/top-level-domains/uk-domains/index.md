---
cp9:
  canonical: https://developers.cloudflare.com/registrar/top-level-domains/uk-domains/
  description: Manage .UK domains with Cloudflare Registrar.
  full_title: Learn how to manage a .UK domain with Cloudflare. · Cloudflare Registrar docs
  head_html: <title>Learn how to manage a .UK domain with Cloudflare. · Cloudflare Registrar docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage .UK domains with Cloudflare Registrar."><link rel="canonical" href="https://developers.cloudflare.com/registrar/top-level-domains/uk-domains/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/registrar/top-level-domains/uk-domains/index.md"><meta property="og:title" content="Learn how to manage a .UK domain with Cloudflare. · Cloudflare Registrar docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage .UK domains with Cloudflare Registrar."><meta property="og:url" content="https://developers.cloudflare.com/registrar/top-level-domains/uk-domains/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Registrar"><meta name="algolia_product_filter" content="Registrar"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Registrar"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/registrar/top-level-domains/uk-domains/#page","headline":"Learn how to manage a .UK domain with Cloudflare. \u00b7 Cloudflare Registrar docs","description":"Manage .UK domains with Cloudflare Registrar.","url":"https://developers.cloudflare.com/registrar/top-level-domains/uk-domains/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /registrar/top-level-domains/uk-domains/
  schema: 1
---
<h2 id="how-to-transfer-a-uk-domain-to-cloudflare">How to transfer a .UK domain to Cloudflare</h2>
<p>Cloudflare currently supports the transfer of <code>.uk</code>, <code>co.uk</code>, <code>org.uk</code>, and <code>me.uk</code> domains. To transfer a <code>.uk</code> domain to Cloudflare from another registrar follow these steps:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Transfer domains</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<p>Cloudflare will show you a list of domains that are eligible for transfer (see below for restrictions). If you do not see your domain, <a href="/fundamentals/manage-domains/add-site/">add the domain you want to transfer</a> to your Cloudflare account before you try to transfer your <code>.uk</code> domain.
2. Select the domains you wish to transfer.
3. Proceed to checkout. Note that there is no fee to transfer a <code>.uk</code> domain and an additional year is NOT added during the transfer process.
4. After checkout, request your current registrar to update the <a href="https://en.wikipedia.org/wiki/Internet_Provider_Security">IPS tag</a> to <code>CLOUDFLARE</code>. If the transfer is not completed within 24 hours, ask your registrar again to update the IPS tag. The transfer will be automatically canceled if not completed within 30 days.
5. Cloudflare will receive a notice once your registrar updates the IPS tag. After that, we will finish transferring your domain.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/12735.md")
</aside>
<h2 id="transfer-a-uk-domain-to-another-registrar">Transfer a .UK domain to another registrar</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>Domain Registration</strong> &gt; <strong>Manage Domains</strong>.</li>
<li>Find the domain you want to transfer, and select <strong>Manage</strong>.</li>
<li>Select <strong>Configuration</strong> &gt; <strong>Unlock</strong>.</li>
<li>Enter the IPS tag of the registrar you wish to transfer to.</li>
</ol>
<p>Your new registrar is responsible for accepting the transfer. Cloudflare has no visibility into why a transfer might not be accepted by the new registrar.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12734.md")
</aside>
