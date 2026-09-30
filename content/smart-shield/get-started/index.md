---
cp9:
  canonical: https://developers.cloudflare.com/smart-shield/get-started/
  description: Enable Smart Shield and configure origin protection features for your domain.
  full_title: Get started · Cloudflare Smart Shield docs
  head_html: <title>Get started · Cloudflare Smart Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable Smart Shield and configure origin protection features for your domain."><link rel="canonical" href="https://developers.cloudflare.com/smart-shield/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/smart-shield/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare Smart Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable Smart Shield and configure origin protection features for your domain."><meta property="og:url" content="https://developers.cloudflare.com/smart-shield/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Smart Shield"><meta name="algolia_product_filter" content="Smart Shield"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Smart Shield"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/smart-shield/get-started/#page","headline":"Get started \u00b7 Cloudflare Smart Shield docs","description":"Enable Smart Shield and configure origin protection features for your domain.","url":"https://developers.cloudflare.com/smart-shield/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /smart-shield/get-started/
  schema: 1
---
<p>Smart Shield reduces the load on your origin server and improves content delivery by consolidating requests through Cloudflare's caching infrastructure. It is available to all customers as an opt-in configuration.</p>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>You must have a Cloudflare account and <a href="/fundamentals/manage-domains/add-site/">onboard your domain</a>.</li>
<li>Verify that DNS records for the domain you want to protect are set to <span class="nb-glossary-tooltip" title="proxy status">proxied</span>. Smart Shield operates within Cloudflare's reverse proxy, so traffic from DNS-only records is not routed through it.</li>
</ul>
<h2 id="steps">Steps</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select your account and domain.</li>
<li>Go to <strong>Speed</strong> &gt; <strong>Smart Shield</strong>.</li>
<li>(Optional) Explore the different <a href="#packages-and-availability">available packages</a>.</li>
<li>Select <strong>Get started for free</strong> or choose a different package and select <strong>Continue</strong> to proceed to the guided onboarding flow.</li>
</ol>
<p>After setup, you can monitor origin performance and cache effectiveness through the <a href="/speed/observatory/">Observatory</a> dashboard.</p>
<h2 id="packages-and-availability">Packages and availability</h2>
<p>Pro, Business, and Enterprise customers have access to <a href="/smart-shield/configuration/health-checks/">Health Checks</a> for monitoring origin availability across all packages.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/352.md")
</div></div>
<h2 id="further-reading">Further reading</h2>
<ul class="directory-listing"><li><a href="/smart-shield/concepts/network-diagram/">Network diagram</a></li><li><a href="/smart-shield/concepts/connection-reuse/">Connection reuse</a></li></ul>
