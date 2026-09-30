---
cp9:
  canonical: https://developers.cloudflare.com/network-flow/routers/netflow-ipfix-config/
  description: A step-by-step configuration guide for exporting NetFlow or IPFIX data to Cloudflare's network.
  full_title: Netflow/IPFIX configuration · Cloudflare Network Flow docs
  head_html: <title>Netflow/IPFIX configuration · Cloudflare Network Flow docs</title><meta name="generator" content="Nift"><meta name="description" content="A step-by-step configuration guide for exporting NetFlow or IPFIX data to Cloudflare&#x27;s network."><link rel="canonical" href="https://developers.cloudflare.com/network-flow/routers/netflow-ipfix-config/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network-flow/routers/netflow-ipfix-config/index.md"><meta property="og:title" content="Netflow/IPFIX configuration · Cloudflare Network Flow docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="A step-by-step configuration guide for exporting NetFlow or IPFIX data to Cloudflare&#x27;s network."><meta property="og:url" content="https://developers.cloudflare.com/network-flow/routers/netflow-ipfix-config/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network Flow"><meta name="algolia_product_filter" content="Network Flow"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Network Flow"><meta name="pcx_tags" content="NetFlow,UDP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network-flow/routers/netflow-ipfix-config/#page","headline":"Netflow/IPFIX configuration \u00b7 Cloudflare Network Flow docs","description":"A step-by-step configuration guide for exporting NetFlow or IPFIX data to Cloudflare's network.","url":"https://developers.cloudflare.com/network-flow/routers/netflow-ipfix-config/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["NetFlow","UDP"]}</script>
  markdown: true
  noindex: false
  route: /network-flow/routers/netflow-ipfix-config/
  schema: 1
---
<p>Configure your router to export <span class="nb-glossary-tooltip" title="flow data">flow data</span> to Cloudflare's network for analysis in Network Flow (formerly Magic Network Monitoring). Network Flow supports the NetFlow v5, NetFlow v9, and IPFIX formats.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Before configuring NetFlow or IPFIX, verify the following:</p>
<ul>
<li>Your router supports NetFlow or IPFIX export capabilities. Refer to <a href="/network-flow/routers/supported-routers/">Supported routers</a> for a list of compatible routers.</li>
<li>You have administrative access to your router's configuration interface.</li>
<li>You have <a href="/network-flow/get-started/#2-register-your-router-with-cloudflare">registered your router with Cloudflare</a>.</li>
</ul>
<h2 id="1-access-your-router-configuration"><ol>
<li>Access your router configuration</li>
</ol></h2>
<p>Log in to your router's configuration application or command-line interface. The exact method varies by router vendor and model.</p>
<h2 id="2-configure-flow-exporter"><ol start="2">
<li>Configure Flow Exporter</li>
</ol></h2>
<p>Open your router's NetFlow configuration menu and set up the <strong>Flow Exporter</strong> with the following values:</p>
<ul>
<li><strong>Destination IP address</strong>: <code>162.159.65.1</code></li>
<li><strong>Destination Port</strong>: <code>2055</code></li>
<li><strong>Transport Protocol</strong>: <code>UDP</code></li>
</ul>
<p>These settings direct your router to send flow data to Cloudflare's network for analysis.</p>
<h2 id="3-configure-flow-record"><ol start="3">
<li>Configure Flow Record</li>
</ol></h2>
<p>Set up your router's <strong>Flow Record</strong> configuration with the following fields. These fields define what traffic metadata your router collects and exports.</p>
<p>Match fields identify the traffic:</p>
<ul>
<li><code>match ipv4 protocol</code></li>
<li><code>match ipv4 source address</code></li>
<li><code>match ipv4 destination address</code></li>
<li><code>match transport source-port</code></li>
<li><code>match transport destination-port</code></li>
<li><code>match interface input</code></li>
</ul>
<p>Collect fields capture statistics about the traffic:</p>
<ul>
<li><code>collect transport tcp flag</code></li>
<li><code>collect counter packets long</code></li>
<li><code>collect counter bytes long</code></li>
<li><code>collect flow sampler</code></li>
<li><code>collect timestamp sys-uptime first</code></li>
<li><code>collect timestamp sys-uptime last</code></li>
</ul>
<h2 id="4-save-and-apply-configuration"><ol start="4">
<li>Save and apply configuration</li>
</ol></h2>
<p>Save your NetFlow or IPFIX configuration changes and apply them to your router. Verify that your router's NetFlow template does not contain duplicated fields, as duplicates can cause export errors.</p>
<h2 id="5-verify-your-configuration"><ol start="5">
<li>Verify your configuration</li>
</ol></h2>
<p>After configuring NetFlow or IPFIX, verify that data is being sent to Cloudflare:</p>
<ol>
<li>Wait five to ten minutes for flow data to be transmitted and processed.</li>
<li>Check your router status in the Cloudflare dashboard under <strong>Network flow</strong> &gt; <strong>Configure Network flow</strong> &gt; <strong>Check routers</strong> (visible during onboarding) or view analytics in the <strong>Network flow</strong> page.</li>
<li>If data is not appearing, verify your Flow Exporter settings and confirm your router's public IP address matches the IP registered with Cloudflare.</li>
</ol>
