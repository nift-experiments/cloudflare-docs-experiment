---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/monitors/create-monitor/
  description: Learn how to set up and maintain monitors for your load balancer.
  full_title: Manage monitors · Cloudflare Load Balancing docs
  head_html: <title>Manage monitors · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to set up and maintain monitors for your load balancer."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/monitors/create-monitor/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/monitors/create-monitor/index.md"><meta property="og:title" content="Manage monitors · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to set up and maintain monitors for your load balancer."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/monitors/create-monitor/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/monitors/create-monitor/#page","headline":"Manage monitors \u00b7 Cloudflare Load Balancing docs","description":"Learn how to set up and maintain monitors for your load balancer.","url":"https://developers.cloudflare.com/load-balancing/monitors/create-monitor/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/monitors/create-monitor/
  schema: 1
---
<div class="nb-glossary-definition"><p>A monitor issues health monitor requests at regular intervals to evaluate the health of each endpoint within a <a href="/load-balancing/pools/">pool</a>.</p>
<p>When a pool <a href="/load-balancing/understand-basics/health-details/">becomes unhealthy</a>, your load balancer takes that pool out of the endpoint rotation.</p></div>
<p>For more details about monitors, refer to <a href="/load-balancing/monitors/">Monitors</a>.</p>
<hr />
<h2 id="retry-timing">Retry timing</h2>
<p>When a health check times out, Cloudflare sends retries immediately — they do not wait for the next interval. The <code>retries</code> setting defines the number of additional attempts after the initial check. For example, with five retries:</p>
<ul>
<li>Total attempts: 1 (initial) + 5 (retries) = <strong>6</strong></li>
<li>With a 20 s timeout: Cloudflare marks the endpoint unhealthy after approximately 120 s (6 × 20 s)</li>
<li>The configured interval (for example, 60 s) only applies between <strong>successful</strong> probe cycles, not between retries</li>
</ul>
<hr />
<h2 id="create-a-monitor">Create a monitor</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10381.md")
</div></div>
<hr />
<h2 id="edit-a-monitor">Edit a monitor</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10384.md")
</div></div>
<hr />
<h2 id="delete-a-monitor">Delete a monitor</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10387.md")
</div></div>
