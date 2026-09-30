---
cp9:
  canonical: https://developers.cloudflare.com/network-flow/tutorials/ddos-testing-guide/
  description: Cloudflare's Network Flow can be used to test a simulated DDoS attack.
  full_title: Network Flow DDoS testing guide · Cloudflare Network Flow docs
  head_html: <title>Network Flow DDoS testing guide · Cloudflare Network Flow docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare&#x27;s Network Flow can be used to test a simulated DDoS attack."><link rel="canonical" href="https://developers.cloudflare.com/network-flow/tutorials/ddos-testing-guide/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network-flow/tutorials/ddos-testing-guide/index.md"><meta property="og:title" content="Network Flow DDoS testing guide · Cloudflare Network Flow docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare&#x27;s Network Flow can be used to test a simulated DDoS attack."><meta property="og:url" content="https://developers.cloudflare.com/network-flow/tutorials/ddos-testing-guide/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network Flow"><meta name="algolia_product_filter" content="Network Flow"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Network Flow"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network-flow/tutorials/ddos-testing-guide/#page","headline":"Network Flow DDoS testing guide \u00b7 Cloudflare Network Flow docs","description":"Cloudflare's Network Flow can be used to test a simulated DDoS attack.","url":"https://developers.cloudflare.com/network-flow/tutorials/ddos-testing-guide/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /network-flow/tutorials/ddos-testing-guide/
  schema: 1
---
<p>To test Network Flow (formerly Magic Network Monitoring) in a repeatable manner, simulate a DDoS attack. At a high level, you need to:</p>
<ol>
<li>Select and install a trusted, open source DDoS simulation tool.</li>
<li>Conduct a small DDoS test attack in a safe test environment.</li>
</ol>
<h2 id="permission-requirements">Permission requirements</h2>
<p>You need to contact Cloudflare to obtain permission before conducting a DDoS test if:</p>
<ul>
<li>Your property is hosted in Cloudflare.</li>
<li>Internet traffic goes through Cloudflare before reaching your property.</li>
</ul>
<p>If you are an Enterprise customer with Network Flow enabled, contact your Cloudflare Account Manager before starting DDoS testing, even if the property is not hosted in Cloudflare.</p>
<p>Refer to <a href="/ddos-protection/reference/simulate-ddos-attack/">Simulating test DDoS attacks</a> for more information.</p>
<p>If you need help conducting a simulated DDoS attack, <a href="https://forms.gle/6tBZNu7shoaCmP9h6">fill out this form</a>.</p>
