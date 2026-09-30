---
cp9:
  canonical: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/
  description: Understand the Pay Per Crawl monetization model.
  full_title: What is Pay Per Crawl? · Cloudflare AI Crawl Control docs
  head_html: <title>What is Pay Per Crawl? · Cloudflare AI Crawl Control docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand the Pay Per Crawl monetization model."><link rel="canonical" href="https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/index.md"><meta property="og:title" content="What is Pay Per Crawl? · Cloudflare AI Crawl Control docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand the Pay Per Crawl monetization model."><meta property="og:url" content="https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Crawl Control"><meta name="algolia_product_filter" content="AI Crawl Control"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="AI Crawl Control"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/#page","headline":"What is Pay Per Crawl? \u00b7 Cloudflare AI Crawl Control docs","description":"Understand the Pay Per Crawl monetization model.","url":"https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="pay-per-crawl-beta">Pay per crawl beta</h3>
@markup("md", "content/.markup/bodies/2753.md")
</aside>
<p>AI crawlers often consume vast amounts of web content. Some provide mutual benefit to content owners by indexing content for search engines, but others engage in activities such as content scraping without permission.</p>
<p>The resulting landscape leaves content owners with limited options for managing AI crawlers or receiving compensation for automated access to their intellectual property.</p>
<h2 id="what-is-pay-per-crawl">What is Pay Per Crawl?</h2>
<p>Pay per crawl is a feature of AI Crawl Control that enables site owners to control and monetize AI crawler access to content by setting a price per zone.</p>
<p>Each time an AI crawler requests content, they either present payment intent via request headers for successful <code>HTTP 200</code> access, or receive an <code>HTTP 402 Payment Required</code> response with pricing. Cloudflare acts as the <span class="nb-glossary-tooltip" title="Merchant of Record">Merchant of Record</span> for pay per crawl and also provides the underlying technical infrastructure.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2752.md")
</aside>
<p>Ultimately, pay per crawl enables:</p>
<ul>
<li>Site owners to take control of their content, and charge a fee every time an AI crawler accesses a page in their <a href="/fundamentals/concepts/accounts-and-zones/#zones">Cloudflare zone</a>. For more details, refer to <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/">use pay per crawl as a site owner</a>.</li>
<li>AI crawler owners to pay to access content on sites protected by pay per crawl. For more details, refer to <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/">use pay per crawl as an AI owner</a>.</li>
</ul>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-pay-per-crawl-diagram.png" alt="Pay per crawl components" /></p>
<h2 id="additional-resources">Additional resources</h2>
<p>Refer to the following resources.</p>
<ul>
<li><a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/enable-in-account-settings/">Use pay per crawl as a site owner</a>.</li>
<li><a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/set-up-cloudflare-account/">Use pay per crawl as an AI owner</a>.</li>
<li><a href="/ai-crawl-control/configuration/ai-crawl-control-with-waf/">AI Crawl Control with Cloudflare WAF</a>.</li>
<li><a href="/ai-crawl-control/configuration/ai-crawl-control-with-bots/">AI Crawl Control with Cloudflare Bots</a>.</li>
</ul>
