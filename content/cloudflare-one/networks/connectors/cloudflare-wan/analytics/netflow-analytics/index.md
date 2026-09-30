---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/analytics/netflow-analytics/
  description: NetFlow statistics in Zero Trust networking.
  full_title: Cloudflare One Appliance NetFlow Analytics · Cloudflare One docs
  head_html: <title>Cloudflare One Appliance NetFlow Analytics · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="NetFlow statistics in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/analytics/netflow-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/analytics/netflow-analytics/index.md"><meta property="og:title" content="Cloudflare One Appliance NetFlow Analytics · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="NetFlow statistics in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/analytics/netflow-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="NetFlow"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/analytics/netflow-analytics/#page","headline":"Cloudflare One Appliance NetFlow Analytics \u00b7 Cloudflare One docs","description":"NetFlow statistics in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/analytics/netflow-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["NetFlow"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-wan/analytics/netflow-analytics/
  schema: 1
---
<h2 id="netflow-exports-from-cloudflare-one-appliance-to-network-flow">NetFlow exports from Cloudflare One Appliance to Network Flow</h2>
<p>You can configure your Cloudflare One Appliance (formerly Magic WAN Connector) to export Netflow statistics for <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/">local breakout traffic</a> to <a href="/network-flow">Network Flow</a> (formerly Magic Network Monitoring). This provides insights into traffic that leaves your site directly, bypassing the Cloudflare network.</p>
<p>The Cloudflare One Appliance uses NetFlow v9 to export flow data for breakout traffic only. You can enable and configure this export by setting the Netflow configuration for the associated site via the Cloudflare API.</p>
<h3 id="enable-netflow-exports">Enable NetFlow exports</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5591.md")
</aside>
<ol>
<li>Send a <code>PUT</code> request to the Netflow configuration endpoint for your site.</li>
<li>In the JSON body request, you must include the <code>collector_ip</code> parameter. To export traffic statistics to Network Flow, use the IP address <code>162.159.65.1</code>. This is the only field required to enable the feature.</li>
</ol>
<p>Minimal configuration example:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT --url https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/sites/$SITE_ID/netflow_config</code></pre>
<ol start="3">
<li>You can customize the configuration by adding optional fields to the JSON payload. These fields include:</li>
</ol>
<ul>
<li><code>collector_port</code>: The UDP port for the collector. The default is <code>2055</code>.</li>
<li><code>sampling_rate</code>: The rate at which packets are sampled.</li>
<li><code>active_timeout</code>: The timeout for active flows in seconds.</li>
<li><code>inactive_timeout</code>: The timeout for inactive flows in seconds.</li>
</ul>
<p>Full configuration example:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT --url https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/sites/$SITE_ID/netflow_config</code></pre>
<p>Your Cloudflare One Appliance will now begin exporting Netflow data for its breakout traffic, which will be ingested and displayed within your Network Flow dashboard. You can retrieve the current settings by sending a <code>GET</code> request, or disable the export by sending a <code>DELETE</code> request to the same endpoint.</p>
