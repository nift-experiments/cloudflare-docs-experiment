---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-china/
  description: Use Load Balancing with the China Network.
  full_title: Load Balancing with the China Network · Cloudflare Load Balancing docs
  head_html: <title>Load Balancing with the China Network · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Load Balancing with the China Network."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-china/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-china/index.md"><meta property="og:title" content="Load Balancing with the China Network · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Load Balancing with the China Network."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-china/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-china/#page","headline":"Load Balancing with the China Network \u00b7 Cloudflare Load Balancing docs","description":"Use Load Balancing with the China Network.","url":"https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-china/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/additional-options/load-balancing-china/
  schema: 1
---
<h2 id="prerequisites">Prerequisites</h2>
<p>To enable load balancers to be deployed to the <a href="/china-network/">China Network</a>, your zone will need to meet the following two criteria:</p>
<ol>
<li>A valid <a href="/china-network/concepts/icp/">ICP license</a> for the zone in question.</li>
<li>The zone must be provisioned with access to the China Network.</li>
</ol>
<p>Once these two criteria are met, any newly created load balancer will be automatically deployed to the China Network. When choosing a region for a pool's health checks, <code>China</code> is now available to be selected in both the dashboard and API.</p>
<p>You can also create a load balancer by sending a <code>POST</code> request to the following endpoint. To deploy to the China Network with the API, the <code>networks</code> array in the API call must contain <code>jdcloud</code> as a value in addition to <code>cloudflare</code>. Refer to the <a href="/api/resources/load_balancers/methods/create/">Cloudflare API documentation</a> for details on the required fields and their formats.</p>
<pre tabindex="0"><code class="language-bash">https://api.cloudflare.com/client/v4/zones/{zone_id}/load_balancers&#10;</code></pre>
<h2 id="limitations">Limitations</h2>
<p>Load balancers deployed to the China Network currently have the following limitations:</p>
<ul>
<li>Only cookie-based session affinity is supported.</li>
<li>Private network off-ramps (Tunnel, GRE, IPsec) are not supported.</li>
<li>Private Network Load Balancing is not available on the China Network.</li>
</ul>
