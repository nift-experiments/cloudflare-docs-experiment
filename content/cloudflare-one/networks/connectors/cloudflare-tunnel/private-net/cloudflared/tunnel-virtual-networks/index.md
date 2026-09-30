---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/
  description: Virtual networks in Zero Trust networking.
  full_title: Virtual networks · Cloudflare One docs
  head_html: <title>Virtual networks · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Virtual networks in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/index.md"><meta property="og:title" content="Virtual networks · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Virtual networks in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/#page","headline":"Virtual networks \u00b7 Cloudflare One docs","description":"Virtual networks in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/
  schema: 1
---
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/5392.md")
</div></details>
<p>Virtual networks provide routing isolation within your Cloudflare account. Each virtual network maintains its own routing table, allowing you to separate traffic between different environments, partners, or applications.</p>
<p>For example, an organization may have separate &quot;production&quot; and &quot;staging&quot; VPC networks that both use the same private IP range (such as <code>10.128.0.0/24</code>). Without virtual networks, Cloudflare cannot distinguish between <code>10.128.0.1</code> in production and <code>10.128.0.1</code> in staging. By creating two virtual networks, you can deterministically route traffic to the correct environment. Users select which virtual network they want to connect to in the Cloudflare One Client.</p>
<p>For a conceptual overview of virtual networks, including how they work across Cloudflare products, refer to <a href="/cloudflare-one/networks/virtual-networks/">Virtual networks</a>.</p>
<h2 id="use-cases">Use cases</h2>
<p>Here are a few scenarios where virtual networks may prove useful:</p>
<ul>
<li>Manage production and staging environments that use the same address space.</li>
<li>Manage acquisitions or mergers between organizations that use the same address space.</li>
<li>Allow IT professional services to access their customer's network for various administration and management purposes.</li>
<li>Allow developers or homelab users to deterministically route traffic through their home network to enforce additional security controls.</li>
<li>Guarantee additional segmentation (beyond just policy enforcement) between networks and resources for security reasons, while keeping all configuration within a single Cloudflare account.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">Install <code>cloudflared</code></a> on each private network.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">Deploy the Cloudflare One Client</a> on user devices.</li>
</ul>
<h2 id="create-a-virtual-network">Create a virtual network</h2>
<p>In this example, &quot;private network&quot; refers to a distinct environment (such as staging or production) that has its own overlapping IP address space (<code>10.128.0.1/32</code> staging and <code>10.128.0.1/32</code> production). If your environments use non-overlapping IPs, you do not need a separate tunnel for each. Instead, you can add multiple routes to a single tunnel.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5396.md")
</div></div>
<h2 id="delete-a-virtual-network">Delete a virtual network</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5399.md")
</div></div>
<h2 id="connect-to-a-virtual-network">Connect to a virtual network</h2>
<h3 id="windows-macos-and-linux">Windows, macOS, and Linux</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5402.md")
</div></div>
<p>When you visit <code>10.128.0.3/32</code>, the Cloudflare One Client will route your request to the staging environment.</p>
<h3 id="ios-android-and-chromeos">iOS, Android, and ChromeOS</h3>
<ol>
<li>Launch the Cloudflare One Agent app.</li>
<li>Go to <strong>Advanced</strong> &gt; <strong>Connection options</strong> &gt; <strong>Virtual networks</strong>.</li>
<li>Choose the virtual network you want to connect to, for example <code>staging-vnet</code>.</li>
</ol>
<p>When you visit <code>10.128.0.3/32</code>, the Cloudflare One Client will route your request to the staging environment.</p>
