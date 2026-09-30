---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/load-balancing/setup/next-steps/
  description: Explore advanced load balancing configurations.
  full_title: Next steps · Cloudflare Learning Paths
  head_html: <title>Next steps · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Explore advanced load balancing configurations."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/load-balancing/setup/next-steps/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/load-balancing/setup/next-steps/index.md"><meta property="og:title" content="Next steps · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Explore advanced load balancing configurations."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/load-balancing/setup/next-steps/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/load-balancing/setup/next-steps/#page","headline":"Next steps \u00b7 Cloudflare Learning Paths","description":"Explore advanced load balancing configurations.","url":"https://developers.cloudflare.com/learning-paths/load-balancing/setup/next-steps/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/load-balancing/setup/next-steps/
  schema: 1
---
<p>Your load balancer should be receiving production traffic (and you can confirm this by reviewing the <a href="/load-balancing/reference/load-balancing-analytics/">analytics</a>).</p>
<p>Though your product is officially set up, you may want to consider the following suggestions.</p>
<h2 id="usage-based-notifications">Usage-based notifications</h2>
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
@markup("md", "content/.markup/bodies/9799.md")
</aside>
<ol start="4">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="additional-configuration-options">Additional configuration options</h2>
<p>You may want to further customize how your load balancer routes traffic or integrate your load balancer with other Cloudflare products:</p>
<ul class="directory-listing"><li><a href="/load-balancing/additional-options/cloudflare-tunnel/">Cloudflare Tunnel (published applications)</a></li><li><a href="/load-balancing/additional-options/spectrum/">Spectrum</a></li><li><a href="/load-balancing/additional-options/planned-maintenance/">Perform planned maintenance</a></li><li><a href="/load-balancing/additional-options/load-shedding/">Load shedding</a></li><li><a href="/load-balancing/additional-options/dns-persistence/">DNS persistence</a></li><li><a href="/load-balancing/additional-options/load-balancing-china/">Load Balancing with the China Network</a></li><li><a href="/load-balancing/additional-options/override-http-host-headers/">Override HTTP Host headers</a></li><li><a href="/load-balancing/additional-options/cname-flattening/">CNAME flattening for endpoints</a></li><li><a href="/load-balancing/additional-options/load-balancing-rules/">Custom load balancing rules</a></li><li><a href="/load-balancing/additional-options/pagerduty-integration/">Integrate with PagerDuty</a></li><li><a href="/load-balancing/additional-options/additional-dns-records/">Additional DNS records</a></li></ul>
