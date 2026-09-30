---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/update-tunnel-health-checks-frequency/
  description: Update tunnel health checks frequency in Zero Trust networking.
  full_title: Update tunnel health checks frequency · Cloudflare One docs
  head_html: <title>Update tunnel health checks frequency · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Update tunnel health checks frequency in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/update-tunnel-health-checks-frequency/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/update-tunnel-health-checks-frequency/index.md"><meta property="og:title" content="Update tunnel health checks frequency · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Update tunnel health checks frequency in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/update-tunnel-health-checks-frequency/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/update-tunnel-health-checks-frequency/#page","headline":"Update tunnel health checks frequency \u00b7 Cloudflare One docs","description":"Update tunnel health checks frequency in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/update-tunnel-health-checks-frequency/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/update-tunnel-health-checks-frequency/
  schema: 1
---
<p>By default, Cloudflare servers send <span class="nb-glossary-tooltip" title="tunnel health-check">health checks</span> to each <span class="nb-glossary-tooltip" title="GRE tunnel">GRE</span>, Cloudflare Network Interconnect (CNI), or <span class="nb-glossary-tooltip" title="IPsec tunnel">IPsec</span> tunnel endpoint you configure to receive traffic from Cloudflare WAN.</p>
<p>For Cloudflare One Appliance (formerly Magic WAN Connector), Cloudflare sends health checks to IPsec tunnel endpoints.</p>
<p>You can configure the health check frequency through the dashboard or <a href="/api/resources/magic_transit/subresources/gre_tunnels/methods/update/">the API</a> to suit your use case. For example, if you are connecting a lower-traffic site that does not need immediate failover and you prefer a lower volume of health check traffic, set the frequency to <code>low</code>. On the other hand, if you are connecting a site that is extremely sensitive to any issues and you want proactive failover at the earliest sign of a potential problem, set this to <code>high</code>.</p>
<p>Available options are <code>low</code>, <code>mid</code>, and <code>high</code>.</p>
<p>To configure health checks frequency in Cloudflare One Appliance, refer to <a href="#configure-connector">Configure Connector</a></p>
<h2 id="manual-configuration">Manual configuration</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5699.md")
</div></div>
<h2 id="configure-connector">Configure Connector</h2>
<ol>
<li>
<p>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> &gt; <strong>Networks</strong>.</p>
</li>
<li>
<p>Go to <strong>Connectors</strong> &gt; <strong>Appliances</strong>.</p>
</li>
<li>
<p>In <strong>Profiles</strong>, find the Connector profile you want to edit &gt; select the three dots &gt; <strong>Edit</strong>.</p>
</li>
<li>
<p>In <strong>Network Configuration</strong> &gt; <strong>WAN configuration</strong> &gt; select your WAN &gt; <strong>Edit</strong>.</p>
</li>
<li>
<p>Change the <strong>Health check rate</strong> to your desired rate.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5693.md")
</aside>
