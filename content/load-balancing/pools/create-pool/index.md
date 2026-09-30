---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/pools/create-pool/
  description: Learn how to set up and maintain pools.
  full_title: Manage pools · Cloudflare Load Balancing docs
  head_html: <title>Manage pools · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to set up and maintain pools."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/pools/create-pool/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/pools/create-pool/index.md"><meta property="og:title" content="Manage pools · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to set up and maintain pools."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/pools/create-pool/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/pools/create-pool/#page","headline":"Manage pools \u00b7 Cloudflare Load Balancing docs","description":"Learn how to set up and maintain pools.","url":"https://developers.cloudflare.com/load-balancing/pools/create-pool/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/pools/create-pool/
  schema: 1
---
<div class="nb-glossary-definition"><p>Within Cloudflare, pools represent your endpoints and how they are organized. As such, a pool can be a group of several endpoints, or you could also have only one endpoint (an origin server, for example) per pool.</p>
<p>If you are familiar with DNS terminology, think of a pool as a “record set,” except Cloudflare only returns addresses that are considered healthy. You can attach health monitors to individual pools for customized monitoring. A pool can have either a single monitor or a monitor group attached — but not both.</p></div>
<p>For more background information on pools, refer to <a href="/load-balancing/pools/">Pools</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10357.md")
</aside>
<hr />
<h2 id="endpoint-address-uniqueness">Endpoint address uniqueness</h2>
<p>Within a single pool, each endpoint address must be unique. Endpoints cannot share the same IP address, even when they use different ports or virtual networks. To use overlapping IP addresses, assign the endpoints to different pools.</p>
<hr />
<h2 id="create-a-pool">Create a pool</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10360.md")
</div></div>
<hr />
<h2 id="edit-a-pool">Edit a pool</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10363.md")
</div></div>
<hr />
<h2 id="delete-a-pool">Delete a pool</h2>
<p>You cannot delete pools that are in use by load balancers. This includes <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/#region-steering">geo steering regions</a> pools, pools referenced by a <a href="/load-balancing/understand-basics/traffic-steering/pool-sets/">pool set</a>, as well as <a href="/load-balancing/understand-basics/health-details/#fallback-pools">fallback pools</a>.</p>
<p>If you get an error when trying to delete a pool, consider the hostnames listed in the error and <a href="/load-balancing/load-balancers/create-load-balancer/">edit the respective load balancers</a>, making sure to remove all references to the pool.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10355.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10366.md")
</div></div>
<hr />
<h2 id="set-up-alerts">Set up alerts</h2>
<p>You can configure alerts to receive notifications for changes in the status of your pools.</p>
<details><summary>Pool Enablement</summary><strong>Who is it for?</strong><p>Customers who want to be warned about status changes (enabled/disabled) in their pools.</p>
<strong>Other options / filters</strong><p>Available filters include:</p>
<ul>
<li>You can search for and add pools from your list of pools. If no pools are selected, the alert will apply to all pools in the account.</li>
<li>You can also choose the trigger that fires the notification when the Load Balancing pool is <strong>enabled</strong>, <strong>disabled</strong>, and <strong>either enabled or disabled</strong>.</li>
</ul>
<strong>Included with</strong><p>Purchase of <a href="/load-balancing/get-started/enable-load-balancing/">Load Balancing</a>.</p>
<strong>What should you do if you receive one?</strong><p>No action is needed.</p>
</details><details><summary>Load Balancing Health Alert</summary><strong>Who is it for?</strong><p>Customers who want to be warned about <a href="/load-balancing/understand-basics/health-details/">changes in health status</a> in their pools or origins.</p>
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
