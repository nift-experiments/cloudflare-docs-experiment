---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/additional-options/spectrum/
  description: Use Load Balancing with Spectrum for TCP and UDP traffic.
  full_title: Add load balancing to Spectrum applications · Cloudflare Load Balancing docs
  head_html: <title>Add load balancing to Spectrum applications · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Load Balancing with Spectrum for TCP and UDP traffic."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/additional-options/spectrum/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/additional-options/spectrum/index.md"><meta property="og:title" content="Add load balancing to Spectrum applications · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Load Balancing with Spectrum for TCP and UDP traffic."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/additional-options/spectrum/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/load-balancing/additional-options/spectrum/#page","headline":"Add load balancing to Spectrum applications \u00b7 Cloudflare Load Balancing docs","description":"Use Load Balancing with Spectrum for TCP and UDP traffic.","url":"https://developers.cloudflare.com/load-balancing/additional-options/spectrum/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/additional-options/spectrum/
  schema: 1
---
<p>You can configure <a href="/spectrum/">Spectrum</a> with Load Balancing to bring resiliency to your TCP or UDP based applications.</p>
<p>Leverage health monitors, failover, and traffic steering by selecting a load balancer as <strong>Origin</strong> when creating your Spectrum application.</p>
<p>The exact settings will vary depending on your use case. Refer to the following steps to understand the workflow.</p>
<hr />
<h2 id="set-up">Set up</h2>
<h3 id="1-configure-your-load-balancer"><ol>
<li>Configure your load balancer</li>
</ol></h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Load Balancing</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select an account where the Load Balancing add-on is <a href="/load-balancing/get-started/enable-load-balancing/">enabled</a>.</p>
</li>
<li>
<p>Go to <strong>Load Balancing</strong> and select <strong>Create load balancer</strong>.</p>
</li>
<li>
<p>On the <strong>Load Balancer Setup</strong>, select <strong>Public load balancer</strong></p>
</li>
<li>
<p>Choose the website to which you want to add this load balancer.</p>
</li>
<li>
<p>On the <strong>Hostname</strong> page, define the settings presented and select <strong>Next</strong>.</p>
<ul>
<li>Enter a <strong>Hostname</strong>, which is the DNS name at which the load balancer is available. For more details on record priority, refer to <a href="/load-balancing/load-balancers/dns-records/">DNS records for load balancing</a>.</li>
</ul>
</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10424.md")
</aside>
<ul>
<li>Keep the orange cloud icon enabled, meaning the load balancer is proxied. This refers to the <a href="/load-balancing/understand-basics/proxy-modes/">proxy mode</a> and, with Spectrum, traffic is always proxied.</li>
<li>Keep <strong>Session Affinity</strong> and <strong>Failover across pools</strong> disabled as these features are not supported with Spectrum.</li>
</ul>
<ol start="7">
<li>
<p>On the <strong>Add a Pool</strong> page, define the settings presented and select <strong>Next</strong>.</p>
<ul>
<li>Select one or more existing pools or <a href="/load-balancing/pools/create-pool/#create-a-pool">create a new pool</a> <sup><a href="#footnote-1">1</a></sup>.</li>
<li>If needed, update the <a href="/load-balancing/understand-basics/health-details/#fallback-pools">fallback pool</a> <sup><a href="#footnote-2">2</a></sup>.</li>
</ul>
</li>
<li>
<p>On the <strong>Monitors</strong> page, define the settings presented and select <strong>Next</strong>.</p>
<ul>
<li>Review the monitors attached to your pools.</li>
<li>If needed, you can attach an existing monitor or <a href="/load-balancing/monitors/create-monitor/#create-a-monitor">create a new monitor</a>.</li>
</ul>
</li>
<li>
<p>On the <strong>Traffic Steering</strong> page, choose an option for <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">Traffic steering</a> and select <strong>Next</strong>.</p>
</li>
<li>
<p>Keep <strong>Custom Rules</strong> page empty as this feature is not supported with Spectrum.</p>
</li>
<li>
<p>On the <strong>Review</strong> page:</p>
</li>
</ol>
<ul>
<li>Review your configuration and make any changes.
<ul>
<li>If you set traffic steering to <strong>Off</strong>, re-order the pools in your load balancer to adjust the fallback order.</li>
<li>If you chose to set traffic steering to Random, you can <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/standard-options/#random-steering">set weights to your pools</a> (via the <a href="/api/resources/load_balancers/methods/create/">API</a>) to determine the percentage of traffic sent to each pool.</li>
</ul>
</li>
<li>Choose whether to <strong>Save as Draft</strong> or <strong>Save and Deploy</strong>.</li>
</ul>
<h3 id="2-configure-your-spectrum-application"><ol start="2">
<li>Configure your Spectrum application</li>
</ol></h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Spectrum</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create an Application</strong>. If this is your first time using Spectrum, the <strong>Create an Application</strong> modal appears.</li>
<li>Select your <strong><a href="/spectrum/reference/configuration-options/#application-type">Application Type</a></strong>.</li>
<li>Under <strong>Domain</strong>, enter the domain that will use Spectrum.</li>
<li>Under <strong>Edge Port</strong>, enter the port Cloudflare should use for your application.</li>
<li>Under <strong>Origin</strong>, select <strong>Load Balancer</strong>.</li>
<li>Select the load balancer you want to use from the dropdown. Disabled load balancers will not show on the <strong>Load Balancer</strong> menu.</li>
<li>Select <strong>Add</strong>.</li>
</ol>
<hr />
<h2 id="limitations">Limitations</h2>
<ul>
<li>
<p>Load Balancing <a href="/load-balancing/understand-basics/session-affinity/">session affinity</a>, <a href="/load-balancing/understand-basics/adaptive-routing/#failover-across-pools">failover across pools</a>, and <a href="/load-balancing/additional-options/load-balancing-rules/">custom rules</a> are not supported by Spectrum.</p>
</li>
<li>
<p>UDP health checks are only available with public monitoring. TCP can be used with both public and private monitoring.</p>
</li>
</ul>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Within Cloudflare, pools represent your endpoints and how they are organized. As such, a pool can be a group of several endpoints, or you could also have only one endpoint (an origin server, for example) per pool.</li>
<li id="footnote-2">A fallback pool is the pool of last resort. When all pools are disabled or unhealthy, this is where the load balancer will send traffic.</li></ol></section>
