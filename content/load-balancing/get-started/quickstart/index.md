---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/get-started/quickstart/
  description: Create a load balancer with pools and monitors in a few steps.
  full_title: Quickstart · Cloudflare Load Balancing docs
  head_html: <title>Quickstart · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a load balancer with pools and monitors in a few steps."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/get-started/quickstart/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/get-started/quickstart/index.md"><meta property="og:title" content="Quickstart · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a load balancer with pools and monitors in a few steps."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/get-started/quickstart/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/get-started/quickstart/#page","headline":"Quickstart \u00b7 Cloudflare Load Balancing docs","description":"Create a load balancer with pools and monitors in a few steps.","url":"https://developers.cloudflare.com/load-balancing/get-started/quickstart/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/get-started/quickstart/
  schema: 1
---
<p>Get up and running quickly with Load Balancing. For more in-depth explanations, refer to the <a href="/learning-paths/load-balancing/concepts/">Learning path</a>.</p>
<p>This guide assumes you are familiar with the Cloudflare <a href="/load-balancing/understand-basics/load-balancing-components/">Load Balancing components</a>.</p>
<br />
<hr />
<h2 id="before-you-begin">Before you begin</h2>
<p>Make sure you:</p>
<ul>
<li>Have access to multiple <span class="nb-glossary-tooltip" title="endpoint">endpoints</span> (origin servers, private or public IP addresses, virtual IP addresses (VIPs), etc), either physical or cloud-based.</li>
<li>Have access to Load Balancing, available as an <a href="/load-balancing/get-started/enable-load-balancing/">add-on</a> for any type of account.</li>
<li>Have test and production hostnames that are covered by <a href="/load-balancing/load-balancers/dns-records/#ssltls-coverage">SSL/TLS certificates</a>.</li>
</ul>
<h2 id="create-a-monitor">Create a monitor</h2>
<div class="nb-glossary-definition"><p>A monitor issues health monitor requests at regular intervals to evaluate the health of each endpoint within a <a href="/load-balancing/pools/">pool</a>.</p>
<p>When a pool <a href="/load-balancing/understand-basics/health-details/">becomes unhealthy</a>, your load balancer takes that pool out of the endpoint rotation.</p></div>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10412.md")
</div></div>
<details class="nb-details"><summary>Example monitor configuration</summary><div class="nb-details-body">
@input("content/.markup/bodies/10413.md")
</div></details>
<h2 id="create-pools">Create pools</h2>
<div class="nb-glossary-definition"><p>Within Cloudflare, pools represent your endpoints and how they are organized. As such, a pool can be a group of several endpoints, or you could also have only one endpoint (an origin server, for example) per pool.</p>
<p>If you are familiar with DNS terminology, think of a pool as a “record set,” except Cloudflare only returns addresses that are considered healthy. You can attach health monitors to individual pools for customized monitoring. A pool can have either a single monitor or a monitor group attached — but not both.</p></div>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10416.md")
</div></div>
<h2 id="confirm-pool-health">Confirm pool health</h2>
<p>Before directing any traffic to your pools, make sure that your pools and monitors are set up correctly. The status of your health check will be <em>unknown</em> until the results of the first check are available.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10419.md")
</div></div>
<h3 id="unexpected-health-status">Unexpected health status</h3>
<p>If you notice that healthy pools are being marked unhealthy:</p>
<ul>
<li>Review <a href="/load-balancing/understand-basics/health-details/">how endpoints and pools become unhealthy</a>.</li>
<li>Refer to the <a href="/load-balancing/troubleshooting/">Troubleshooting section</a>.</li>
</ul>
<h2 id="create-a-load-balancer-on-a-test-subdomain">Create a load balancer on a test subdomain</h2>
<p>Instead of starting on your production domain, you likely should create a load balancer on a test or staging domain. This may involve temporary changes to your monitors and pools, depending on your infrastructure setup.</p>
<p>Starting with a test domain allows you to verify everything is working correctly before routing production traffic.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10422.md")
</div></div>
<h2 id="optional-review-load-balancing-analytics">Optional - Review load balancing analytics</h2>
<p>As you send sample requests to your test domain, review the <a href="/load-balancing/reference/load-balancing-analytics/">load balancing analytics</a> page to make sure your load balancer is distributing requests like you were expecting.</p>
<h2 id="route-production-traffic">Route production traffic</h2>
<p>Now that you have set up your load balancer and verified everything is working correctly, you can put the load balancer on a live domain or subdomain:</p>
<ol>
<li>If you update your pools and monitors, review the pool health again to make sure everything is working as expected.</li>
<li>Confirm that your production hostname has the correct <a href="/load-balancing/load-balancers/dns-records/#priority-order">priority order</a> of DNS records and is covered by an <a href="/load-balancing/load-balancers/dns-records/#ssltls-coverage">SSL/TLS certificate</a>.</li>
<li>Configure your load balancer to receive production traffic, which could involve either:
<ul>
<li>Editing the <strong>Hostname</strong> of your existing load balancer.</li>
<li>Updating the <code>CNAME</code> record sending traffic to your load balancer.</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10403.md")
</aside>
<h2 id="optional-next-steps">Optional - Next steps</h2>
<p>Your load balancer should be receiving production traffic (and you can confirm this by reviewing the <a href="/load-balancing/reference/load-balancing-analytics/">analytics</a>).</p>
<p>Though your product is officially set up, you may want to consider the following suggestions.</p>
<h3 id="usage-based-notifications">Usage-based notifications</h3>
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
@markup("md", "content/.markup/bodies/10402.md")
</aside>
<ol start="4">
<li>Select <strong>Save</strong>.</li>
</ol>
<h3 id="additional-configuration-options">Additional configuration options</h3>
<p>You may want to further customize how your load balancer routes traffic or integrate your load balancer with other Cloudflare products:</p>
<ul class="directory-listing"><li><a href="/load-balancing/additional-options/cloudflare-tunnel/">Cloudflare Tunnel (published applications)</a></li><li><a href="/load-balancing/additional-options/spectrum/">Spectrum</a></li><li><a href="/load-balancing/additional-options/planned-maintenance/">Perform planned maintenance</a></li><li><a href="/load-balancing/additional-options/load-shedding/">Load shedding</a></li><li><a href="/load-balancing/additional-options/dns-persistence/">DNS persistence</a></li><li><a href="/load-balancing/additional-options/load-balancing-china/">Load Balancing with the China Network</a></li><li><a href="/load-balancing/additional-options/override-http-host-headers/">Override HTTP Host headers</a></li><li><a href="/load-balancing/additional-options/cname-flattening/">CNAME flattening for endpoints</a></li><li><a href="/load-balancing/additional-options/load-balancing-rules/">Custom load balancing rules</a></li><li><a href="/load-balancing/additional-options/pagerduty-integration/">Integrate with PagerDuty</a></li><li><a href="/load-balancing/additional-options/additional-dns-records/">Additional DNS records</a></li></ul>
