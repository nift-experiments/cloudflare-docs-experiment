---
cp9:
  canonical: https://developers.cloudflare.com/stream/stream-live/custom-domains/
  description: Configure custom RTMPS ingest domains for Cloudflare Stream live inputs instead of using the default URL.
  full_title: Add custom ingest domains · Cloudflare Stream docs
  head_html: <title>Add custom ingest domains · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure custom RTMPS ingest domains for Cloudflare Stream live inputs instead of using the default URL."><link rel="canonical" href="https://developers.cloudflare.com/stream/stream-live/custom-domains/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/stream-live/custom-domains/index.md"><meta property="og:title" content="Add custom ingest domains · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure custom RTMPS ingest domains for Cloudflare Stream live inputs instead of using the default URL."><meta property="og:url" content="https://developers.cloudflare.com/stream/stream-live/custom-domains/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/stream-live/custom-domains/#page","headline":"Add custom ingest domains \u00b7 Cloudflare Stream docs","description":"Configure custom RTMPS ingest domains for Cloudflare Stream live inputs instead of using the default URL.","url":"https://developers.cloudflare.com/stream/stream-live/custom-domains/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/stream-live/custom-domains/
  schema: 1
---
<p>With custom ingest domains, you can configure your RTMPS feeds to use an ingest URL that you specify instead of using <code>live.cloudflare.com.</code></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14404.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Live inputs</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Settings</strong>, above the list. The <strong>Custom Input Domains</strong> page displays.</li>
<li>Under <strong>Domain</strong>, add your domain and select <strong>Add domain</strong>.</li>
<li>At your DNS provider, add a CNAME record that points to <code>live.cloudflare.com</code>. If your DNS provider is Cloudflare, this step is done automatically.</li>
</ol>
<p>If you are using Cloudflare for DNS, ensure the <a href="/dns/proxy-status/"><strong>Proxy status</strong></a> of your ingest domain is <strong>DNS only</strong> (grey-clouded).</p>
<h2 id="delete-a-custom-domain">Delete a custom domain</h2>
<ol>
<li>From the <strong>Custom Input Domains</strong> page under <strong>Hostnames</strong>, locate the domain.</li>
<li>Select the menu icon under <strong>Action</strong>. Select <strong>Delete</strong>.</li>
</ol>
