---
cp9:
  canonical: https://developers.cloudflare.com/argo-smart-routing/get-started/
  description: Learn how to enable Argo Smart Routing in the Cloudflare dashboard.
  full_title: Get started · Cloudflare Argo Smart Routing docs
  head_html: <title>Get started · Cloudflare Argo Smart Routing docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to enable Argo Smart Routing in the Cloudflare dashboard."><link rel="canonical" href="https://developers.cloudflare.com/argo-smart-routing/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/argo-smart-routing/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare Argo Smart Routing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to enable Argo Smart Routing in the Cloudflare dashboard."><meta property="og:url" content="https://developers.cloudflare.com/argo-smart-routing/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Argo Smart Routing"><meta name="algolia_product_filter" content="Argo Smart Routing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Argo Smart Routing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/argo-smart-routing/get-started/#page","headline":"Get started \u00b7 Cloudflare Argo Smart Routing docs","description":"Learn how to enable Argo Smart Routing in the Cloudflare dashboard.","url":"https://developers.cloudflare.com/argo-smart-routing/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /argo-smart-routing/get-started/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="smart-shield">Smart Shield</h3>
@markup("md", "content/.markup/bodies/1523.md")
</aside>
<p>Argo Smart Routing speeds up your global traffic by routing requests across the fastest network paths available.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1526.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1522.md")
</aside>
<h2 id="billing">Billing</h2>
<p>If Cloudflare mitigates attacks on your site - whether through DDoS protection, the WAF, or other mechanisms - that traffic will not be included in any charges for Argo Smart Routing.</p>
<p>Since this is a service with <a href="/billing/understand/usage-based-billing/">usage-based billing</a>, Cloudflare recommends that you set up usage-based billing notifications to avoid unexpected bills.</p>
<p>To set up those notifications:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>On <strong>Alert Type</strong> of <strong>Usage Based Billing</strong>, click <strong>Select</strong>.</p>
</li>
<li>
<p>Fill out the following information:</p>
<ul>
<li><strong>Name</strong></li>
<li><strong>Product</strong></li>
<li><strong>Notification limit</strong> (exact metric will vary based on product)</li>
<li><strong>Notification email</strong></li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1521.md")
</aside>
<ol start="4">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="enable-tiered-cache">Enable Tiered Cache</h2>
<p><a href="/cache/">Cache</a> works by storing a copy of website content at Cloudflare's data centers. <a href="/cache/how-to/tiered-cache/">Tiered Cache</a> organizes these data centers into a hierarchy based on location. This behavior allows Cloudflare to deliver content from data centers closest to your visitor.</p>
<p>When used together, Argo Smart Routing optimizes the network path between Cloudflare data centers and your origin, while Tiered Cache reduces the number of requests that reach your origin. For more information, refer to <a href="/cache/how-to/tiered-cache/">Tiered Cache</a>.</p>
