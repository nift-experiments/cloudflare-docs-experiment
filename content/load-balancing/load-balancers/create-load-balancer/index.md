---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/load-balancers/create-load-balancer/
  description: Learn how to set up and maintain load balancers.
  full_title: Manage load balancers · Cloudflare Load Balancing docs
  head_html: <title>Manage load balancers · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to set up and maintain load balancers."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/load-balancers/create-load-balancer/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/load-balancers/create-load-balancer/index.md"><meta property="og:title" content="Manage load balancers · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to set up and maintain load balancers."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/load-balancers/create-load-balancer/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/load-balancers/create-load-balancer/#page","headline":"Manage load balancers \u00b7 Cloudflare Load Balancing docs","description":"Learn how to set up and maintain load balancers.","url":"https://developers.cloudflare.com/load-balancing/load-balancers/create-load-balancer/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/load-balancers/create-load-balancer/
  schema: 1
---
<p>A load balancer distributes traffic among pools according to <a href="/load-balancing/understand-basics/health-details/">pool health</a> and <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">traffic steering policies</a>. Each load balancer is identified by its DNS hostname (<code>lb.example.com</code>, <code>dev.example.com</code>, etc.) or IP address.
<br /></p>
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/ce39fdf599aed3661f60e8f780761808/iframe?preload=true&amp;letterboxColor=transparent&amp;poster=https%3A%2F%2Fimagedelivery.net%2FxDOJvHcv1KwTQn6S-BGFIw%2F51022c1e-c6d4-424e-f439-002ffb4b8400%2Fpublic" title="Set up Load Balancer" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<p>For more details about load balancers, refer to <a href="/load-balancing/load-balancers/">Load balancers</a>.</p>
<h2 id="create-a-load-balancer">Create a load balancer</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10394.md")
</div></div>
<h3 id="sharing-your-load-balancer-with-other-sites">Sharing your load balancer with other sites</h3>
<p>You can share your load balancer with other sites in your account by <a href="/dns/manage-dns-records/how-to/create-dns-records/">creating a canonical name (<code>CNAME</code>) record</a>. This is useful for sharing configurations with multiple other domains so you do not have to create new load balancers for each site.</p>
<p>You can also configure separate load balancers for each domain and reuse monitors and pools. This is especially useful for changing the failover order for different domains, such as when your <code>example.co.uk</code> server has a different failover priority from <code>example.com</code> or <code>example.com.au</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10390.md")
</aside>
<hr />
<h2 id="edit-a-load-balancer">Edit a load balancer</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10397.md")
</div></div>
<hr />
<h2 id="delete-a-load-balancer">Delete a load balancer</h2>
<p>If you delete or disable a load balancer, your endpoint's response to requests will depend on your <a href="/load-balancing/load-balancers/dns-records/#disabling-a-load-balancer">existing DNS records</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10400.md")
</div></div>
<hr />
<h2 id="set-up-alerts">Set up alerts</h2>
<p>You can configure alerts to receive notifications for changes in the health status of your pools or endpoints.</p>
<details><summary>Load Balancing Health Alert</summary><strong>Who is it for?</strong><p>Customers who want to be warned about <a href="/load-balancing/understand-basics/health-details/">changes in health status</a> in their pools or origins.</p>
<strong>Other options / filters</strong><p>Available filters include:</p>
<ul>
<li>You can search for and add pools from your list of pools, as well as <strong>Include future pools</strong> (if all pools are selected).</li>
<li>You can choose the trigger that fires the notification when the health status becomes <strong>unhealthy</strong>, <strong>healthy</strong>, or <strong>either unhealthy or healthy</strong></li>
<li>You can choose the trigger that fires the notification when the event source health status changes in <strong>pool</strong>, <strong>origin</strong>, or <strong>either pool or origin</strong>.</li>
</ul>
<strong>Included with</strong><p>Purchase of <a href="/load-balancing/get-started/enable-load-balancing/">Load Balancing</a>.</p>
<strong>What should you do if you receive one?</strong><p>Evaluate <a href="/load-balancing/reference/load-balancing-analytics/">load balancing analytics</a> to review changes in health status over time.</p>
</details>
<p>Refer to <a href="/notifications/get-started/">Cloudflare Notifications</a> for more information on how to set up an alert.</p>
