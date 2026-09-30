---
cp9:
  canonical: https://developers.cloudflare.com/data-localization/how-to/workers/
  description: Configure Workers with Regional Services and Customer Metadata Boundary.
  full_title: Workers · Cloudflare Data Localization Suite docs
  head_html: <title>Workers · Cloudflare Data Localization Suite docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Workers with Regional Services and Customer Metadata Boundary."><link rel="canonical" href="https://developers.cloudflare.com/data-localization/how-to/workers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/data-localization/how-to/workers/index.md"><meta property="og:title" content="Workers · Cloudflare Data Localization Suite docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Workers with Regional Services and Customer Metadata Boundary."><meta property="og:url" content="https://developers.cloudflare.com/data-localization/how-to/workers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Data Localization Suite"><meta name="algolia_product_filter" content="Data Localization Suite"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Data Localization Suite,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/data-localization/how-to/workers/#page","headline":"Workers \u00b7 Cloudflare Data Localization Suite docs","description":"Configure Workers with Regional Services and Customer Metadata Boundary.","url":"https://developers.cloudflare.com/data-localization/how-to/workers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /data-localization/how-to/workers/
  schema: 1
---
<p>To ensure that your Cloudflare Workers code runs only within a specific geographic region, configure Regional Services on the Workers custom domain. This restricts where TLS termination (traffic decryption) and code execution occur.</p>
<h2 id="regional-services">Regional Services</h2>
<p>To configure Regional Services for hostnames <a href="/dns/proxy-status/">proxied</a> (meaning traffic routes through Cloudflare rather than directly to your origin server) through Cloudflare and ensure that processing of a Workers project occurs only in-region, follow these steps:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your Workers project.</li>
<li>Follow the steps to <a href="/workers/configuration/routing/custom-domains/">create a custom domain</a>.</li>
<li>Run the <a href="/data-localization/regional-services/regional-hostnames/#configure-regional-services-via-api">API POST</a> command on the configured Workers Custom Domain to create a <code>regional_hostnames</code> with a specific region.</li>
</ol>
<h3 id="caveats">Caveats</h3>
<p>Regional Services only applies to the custom domain configured for a Workers project. Therefore, it will run only in-region Cloudflare locations.</p>
<p>Regional Services restricts where Workers are executed (where requests are processed). However, Workers code and secrets are deployed globally to all Cloudflare data centers. Regional Services does not prevent the code itself from being present outside the configured region — only its execution is regionalized.</p>
<p>Requests reaching your regionalized hostname from another zone or domain are regionalized according to your hostname's Regional Services configuration, regardless of the originating zone. Regional Services does not extend to outgoing <a href="/workers/platform/limits/#subrequests">subrequests</a> from Workers to other services — refer to <a href="/data-localization/limitations/#regional-services">Limitations</a> for details.</p>
<p>Regional Services does not apply to other Worker triggers, like <a href="/queues/">Queues</a> or <a href="/workers/configuration/cron-triggers/">Cron Triggers</a>.</p>
<h2 id="customer-metadata-boundary">Customer Metadata Boundary</h2>
<p>Customer Metadata Boundary applies to the custom domain configured, as well as the <a href="/workers/configuration/routing/workers-dev/"><code>*.workers.dev</code></a> subdomain.</p>
<p>Workers <a href="/workers/observability/metrics-and-analytics/">Metrics and Analytics</a> are not available outside the US region when using Customer Metadata Boundary.</p>
<p>With Customer Metadata Boundary set to <code>EU</code>, <strong>Workers &amp; Pages</strong> &gt; <strong>Workers</strong> &gt; <strong>Metrics</strong> tab the zone dashboard will not be populated.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7433.md")
</aside>
<p>Refer to the <a href="/workers/">Workers documentation</a> for more information.</p>
