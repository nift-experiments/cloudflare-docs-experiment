---
cp9:
  canonical: https://developers.cloudflare.com/byoip/service-bindings/magic-transit-with-cdn/
  description: Service bindings allow BYOIP customers to selectively route traffic on a per-IP address basis to the CDN pipeline. It is important to note that traffic routed to the CDN pipeline is protected at Layers 3 and 4 by the inherent DDoS protection capabilities.
  full_title: Use BYOIP with Magic Transit and CDN · Cloudflare BYOIP docs
  head_html: <title>Use BYOIP with Magic Transit and CDN · Cloudflare BYOIP docs</title><meta name="generator" content="Nift"><meta name="description" content="Service bindings allow BYOIP customers to selectively route traffic on a per-IP address basis to the CDN pipeline. It is important to note that traffic routed to the CDN pipeline is protected at Layers 3 and 4 by the inherent DDoS protection capabilities."><link rel="canonical" href="https://developers.cloudflare.com/byoip/service-bindings/magic-transit-with-cdn/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/byoip/service-bindings/magic-transit-with-cdn/index.md"><meta property="og:title" content="Use BYOIP with Magic Transit and CDN · Cloudflare BYOIP docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Service bindings allow BYOIP customers to selectively route traffic on a per-IP address basis to the CDN pipeline. It is important to note that traffic routed to the CDN pipeline is protected at Layers 3 and 4 by the inherent DDoS protection capabilities."><meta property="og:url" content="https://developers.cloudflare.com/byoip/service-bindings/magic-transit-with-cdn/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="BYOIP"><meta name="algolia_product_filter" content="BYOIP"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="BYOIP"><meta name="pcx_tags" content="DNS,Integration"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/byoip/service-bindings/magic-transit-with-cdn/#page","headline":"Use BYOIP with Magic Transit and CDN \u00b7 Cloudflare BYOIP docs","description":"Service bindings allow BYOIP customers to selectively route traffic on a per-IP address basis to the CDN pipeline. It is important to note that traffic routed to the CDN pipeline is protected at Layers 3 and 4 by the inherent DDoS protection capabilities.","url":"https://developers.cloudflare.com/byoip/service-bindings/magic-transit-with-cdn/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS","Integration"]}</script>
  markdown: true
  noindex: false
  route: /byoip/service-bindings/magic-transit-with-cdn/
  schema: 1
---
<p><a href="/magic-transit/">Magic Transit</a> customers using BYOIP can also benefit from the performance, reliability, and security that Cloudflare offers for HTTP-based applications. <a href="/byoip/service-bindings/">Service bindings</a> allow BYOIP customers to selectively route traffic on a per-IP address basis to the CDN pipeline (which includes <a href="/cache/">Cache</a>, <a href="/waf/">Web Application Firewall (WAF)</a>, and more).</p>
<p>This guide covers using the Cloudflare API to configure Magic Transit with CDN. It is also possible to define service bindings to route traffic to the Spectrum pipeline selectively. Refer to <a href="/byoip/service-bindings/#scope">scope</a> for the full list of possible configurations and other available guides.</p>
<p>It is important to note that traffic routed to the CDN pipeline is protected at Layers 3 and 4 by the inherent DDoS protection capabilities native to the CDN pipeline.</p>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>
<p>Make sure your contract includes CDN according to your needs. If you find any issues related to subscription when following the steps below, reach out to your account team.</p>
</li>
<li>
<p>Plan for what IPs will be used:</p>
</li>
</ul>
<p>Cloudflare <strong>strongly</strong> recommends implementing service bindings through an <strong>aggregated</strong> CIDR block, as it is more efficient than adding discrete bindings for non-contiguous CIDR blocks.</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3731.md")
</div></details>
<p>Once a service binding is created (or deleted), it will take <strong>four to six hours</strong> to propagate across Cloudflare's global network. Services for the IP addresses in scope will likely be disrupted during this window.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3730.md")
</aside>
<h2 id="1-get-account-information"><ol>
<li>Get account information</li>
</ol></h2>
<ol>
<li>Log in to your Cloudflare account and get your <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> and <a href="/fundamentals/api/get-started/">authentication key or token</a>. If using an <a href="/fundamentals/api/get-started/create-token/">API token</a>, the permissions should include <code>Account</code> - <code>IP Prefixes</code> - <code>Edit</code>.</li>
<li>Make a <code>GET</code> request to the <a href="/api/resources/addressing/subresources/services/methods/list/">List Services</a> endpoint and take note of the <code>id</code> associated with the CDN service.</li>
<li>Use the <a href="/api/resources/addressing/subresources/prefixes/methods/list/">List Prefixes</a> endpoint and take note of the <code>id</code> associated with the prefix (<code>cidr</code>) you will configure.</li>
</ol>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/3732.md")
</div>
<ol start="4">
<li>To confirm you currently have a Magic Transit service binding and that it spans across your entire prefix, make a <code>GET</code> request to the <a href="/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/list/">List Service Bindings</a> endpoint. Replace the <code>{prefix_id}</code> in the URI path by the actual prefix ID you got from the previous step.</li>
</ol>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/3733.md")
</div>
<h2 id="2-create-service-bindings"><ol start="2">
<li>Create service bindings</li>
</ol></h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="caution">Caution</h3>
@markup("md", "content/.markup/bodies/3729.md")
</aside>
<ol>
<li>Make a <code>POST</code> request to the <a href="/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/create/">Create service binding</a> endpoint, indicating the IP address you want to bind to CDN. Specify the <strong>corresponding network mask</strong> as needed.</li>
</ol>
<div class="nb-example"><h3 class="nb-component-title" id="example-2">Example</h3>
@markup("md", "content/.markup/bodies/3734.md")
</div>
<p>You can periodically check the service binding status using the <a href="/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/list/">List Service Bindings</a> endpoint.</p>
<h2 id="3-create-address-maps"><ol start="3">
<li>Create address maps</li>
</ol></h2>
<p>Once you have configured your IPs to have CDN service, you can use <span class="nb-glossary-tooltip" title="address map">address maps</span> to specify which IPs should be used by Cloudflare in DNS responses when a record is <span class="nb-glossary-tooltip" title="proxy status">proxied</span>.</p>
<p>You can choose between two different scopes:</p>
<ul>
<li>Account-level: uses the address map for all proxied DNS records across all of the zones within an account.</li>
<li>Zone-level: uses the address map for all proxied DNS records within a zone.</li>
</ul>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/3728.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3739.md")
</div></div>
<h2 id="4-create-dns-records"><ol start="4">
<li>Create DNS records</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3742.md")
</div></div>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/3727.md")
</aside>
<p>While the DNS record proxy status and address map will determine how Cloudflare's authoritative DNS responds to requests for your hostnames, the IP addresses specified in <code>A</code>/<code>AAAA</code> records will determine <a href="/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-reverse-proxy">how Cloudflare reaches the configured origin</a>.</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3743.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3726.md")
</aside>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3744.md")
</div></details>
<h2 id="5-optional-add-layer-7-functionality"><ol start="5">
<li>(Optional) Add layer 7 functionality</li>
</ol></h2>
<p>Leverage other features according to your needs. For example:</p>
<ul>
<li><a href="/cache/">Cache</a></li>
<li><a href="/waf/custom-rules/">WAF custom rules</a></li>
<li><a href="/waf/analytics/security-analytics/">Security analytics</a></li>
</ul>
