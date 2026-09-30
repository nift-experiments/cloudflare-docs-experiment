---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/link-aggregation/
  description: Bundle physical LAN ports into a single logical interface for redundancy and bandwidth.
  full_title: Configure link aggregation groups · Cloudflare One docs
  head_html: <title>Configure link aggregation groups · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Bundle physical LAN ports into a single logical interface for redundancy and bandwidth."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/link-aggregation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/link-aggregation/index.md"><meta property="og:title" content="Configure link aggregation groups · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Bundle physical LAN ports into a single logical interface for redundancy and bandwidth."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/link-aggregation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/link-aggregation/#page","headline":"Configure link aggregation groups \u00b7 Cloudflare One docs","description":"Bundle physical LAN ports into a single logical interface for redundancy and bandwidth.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/link-aggregation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/link-aggregation/
  schema: 1
---
<p>You can bundle multiple physical LAN ports on a Cloudflare One Appliance into a single logical port called a Link Aggregation Group (LAG). This increases LAN bandwidth and provides redundancy. If a member port fails, traffic automatically shifts to the remaining ports in under one second.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5756.md")
</aside>
<p>The following guide assumes you have already created a site and configured your Cloudflare One Appliance. For instructions, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/configure-hardware-appliance/">Configure hardware Appliance</a> or <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure virtual Appliance</a>.</p>
<h2 id="create-a-lag">Create a LAG</h2>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Appliances</strong> tab &gt; <strong>Profiles</strong>.</li>
<li>Select the Cloudflare One Appliance you want to configure &gt; <strong>Edit</strong>.</li>
<li>Go to the <strong>Appliances</strong> tab.</li>
<li>In <strong>Link aggregation groups (LAGs)</strong>, select <strong>Create A LAG</strong>.</li>
<li>Select the LAN ports you want to bundle. You can add up to six ports per LAG. All ports must be the same type and speed.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="assign-a-lan-to-a-lag">Assign a LAN to a LAG</h2>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Appliances</strong> tab &gt; <strong>Profiles</strong>.</li>
<li>Select the Cloudflare One Appliance you want to edit &gt; <strong>Edit</strong>.</li>
<li>Go to <strong>Network Configuration</strong> &gt; <strong>LAN configuration</strong>.</li>
<li>Select or create a LAN &gt; <strong>Edit</strong>.</li>
<li>In <strong>Interface</strong> &gt; <strong>Interface type</strong>, select <strong>Aggregate</strong> as your LAG instead of a single port.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="monitor-lag-status">Monitor LAG status</h2>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Appliances</strong> tab &gt; <strong>Profiles</strong>.</li>
<li>Select the Cloudflare One Appliance &gt; <strong>Edit</strong>.</li>
<li>Go to the <strong>Appliances</strong> tab.</li>
</ol>
<p>The page displays each configured LAG and the status of its member ports.</p>
<h2 id="delete-a-lag">Delete a LAG</h2>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Appliances</strong> tab &gt; <strong>Profiles</strong>.</li>
<li>Select the Cloudflare One Appliance &gt; <strong>Edit</strong>.</li>
<li>Go to the <strong>Appliances</strong> tab.</li>
<li>Next to the LAG you want to delete, select the three-dot menu &gt; <strong>Delete</strong>.</li>
<li>Select <strong>Delete</strong>.</li>
</ol>
