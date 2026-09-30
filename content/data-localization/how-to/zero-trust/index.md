---
cp9:
  canonical: https://developers.cloudflare.com/data-localization/how-to/zero-trust/
  description: Use Zero Trust products with the Data Localization Suite, including Gateway and CASB.
  full_title: Zero Trust · Cloudflare Data Localization Suite docs
  head_html: <title>Zero Trust · Cloudflare Data Localization Suite docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Zero Trust products with the Data Localization Suite, including Gateway and CASB."><link rel="canonical" href="https://developers.cloudflare.com/data-localization/how-to/zero-trust/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/data-localization/how-to/zero-trust/index.md"><meta property="og:title" content="Zero Trust · Cloudflare Data Localization Suite docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Zero Trust products with the Data Localization Suite, including Gateway and CASB."><meta property="og:url" content="https://developers.cloudflare.com/data-localization/how-to/zero-trust/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Data Localization Suite"><meta name="algolia_product_filter" content="Data Localization Suite"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Data Localization Suite,Cloudflare One"><meta name="pcx_tags" content="Logging,SSH"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/data-localization/how-to/zero-trust/#page","headline":"Zero Trust \u00b7 Cloudflare Data Localization Suite docs","description":"Use Zero Trust products with the Data Localization Suite, including Gateway and CASB.","url":"https://developers.cloudflare.com/data-localization/how-to/zero-trust/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Logging","SSH"]}</script>
  markdown: true
  noindex: false
  route: /data-localization/how-to/zero-trust/
  schema: 1
---
<p>The following sections describe how to configure Zero Trust products with the Data Localization Suite, including which features support Regional Services and Customer Metadata Boundary.</p>
<h2 id="gateway">Gateway</h2>
<p>Regional Services can be used with Gateway in all <a href="/data-localization/region-support/">supported regions</a>. Be aware that Regional Services only apply when using the Cloudflare One Client in Traffic and DNS mode.</p>
<h3 id="egress-policies">Egress policies</h3>
<p>Enterprise customers can purchase a <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">dedicated egress IP</a> (IPv4 and IPv6) or range of IPs geolocated to one or more Cloudflare network locations.
This allows your egress traffic to geolocate to the city selected in your <a href="/cloudflare-one/traffic-policies/egress-policies/">egress policies</a>.</p>
<p>Zero Trust <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">dedicated egress IPs</a> control the IPs used by WARP and Gateway traffic when it leaves Cloudflare toward the Internet. They are different from <a href="/smart-shield/configuration/dedicated-egress-ips/">Dedicated CDN Egress IPs</a>, which control the IPs used by the Cloudflare CDN when connecting to your origin server. For guaranteed egress IP geolocation from the Cloudflare CDN to your origin, refer to the <a href="/data-localization/how-to/cache/#egress-to-origin">Cache</a> guide.</p>
<h3 id="http-policies">HTTP policies</h3>
<p>As part of Regional Services, Cloudflare Gateway will only perform <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a> when using the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> (in default <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/">Traffic and DNS mode</a>).</p>
<h4 id="data-loss-prevention-dlp">Data Loss Prevention (DLP)</h4>
<p>You are able to <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-the-payload-of-matched-rules">log the payload of matched DLP rules</a> and encrypt them with your public key so that only you can examine them later.</p>
<p><a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#data-privacy">Cloudflare cannot decrypt encrypted payloads</a>.</p>
<h3 id="dns-policies">DNS policies</h3>
<p>Regional Services controls where Cloudflare decrypts traffic. Because most DNS traffic is not encrypted, Gateway DNS (domain name filtering) cannot be regionalized using Regional Services.</p>
<p>Refer to the <a href="/data-localization/how-to/zero-trust/#cloudflare-one-client-settings">Cloudflare One Client settings</a> section below for more information.</p>
<h3 id="custom-certificates">Custom certificates</h3>
<p>You can <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/custom-certificate/">bring your own certificate</a> to Gateway but these cannot yet be restricted to a specific region.</p>
<h3 id="logs-and-analytics">Logs and Analytics</h3>
<p>By default, Cloudflare will store and deliver logs from data centers across our global network. To maintain regional control over your data, you can use <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary</a> and restrict data storage to a specific geographic region. For more information refer to the section about <a href="/data-localization/metadata-boundary/logpush-datasets/">Logpush datasets supported</a>.</p>
<p>Customers also have the option to reduce the logs that Cloudflare stores:</p>
<ul>
<li>You can <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/manage-pii/">exclude PII from logs</a></li>
<li>You can <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#selective-logging">disable logging, or only log blocked requests</a>.</li>
</ul>
<h4 id="verify-regional-map-application">Verify regional map application</h4>
<p>To verify that your regional map is being applied correctly, check the <code>IngressColoName</code> field in your <a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/#ingresscoloname">Zero Trust Network Session logs</a>. This field shows the name of the Cloudflare data center where traffic ingressed. Since regionalization is applied upstream from Gateway, the ingress data center will be located within your configured regional map, confirming that traffic is being processed in the correct region.</p>
<h2 id="access">Access</h2>
<p>To ensure that all reverse proxy requests for applications protected by Cloudflare Access will only occur in FedRAMP-compliant data centers, you should use <a href="/data-localization/regional-services/regional-hostnames/">Regional Services</a> with the region set to FedRAMP.</p>
<h2 id="cloudflare-tunnel">Cloudflare Tunnel</h2>
<p>The <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#region"><code>--region</code> parameter</a> in <code>cloudflared</code> controls where the tunnel connector establishes its connection to Cloudflare. This setting is separate from Regional Services, which controls where user traffic is decrypted and processed.</p>
<p>For public hostnames served through a tunnel, Regional Services is configured at the DNS record level. The tunnel connector region and the Regional Services region operate independently.</p>
<h2 id="cloudflare-one-client-settings">Cloudflare One Client settings</h2>
<h3 id="local-domain-fallback">Local Domain Fallback</h3>
<p>You can use the WARP setting <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> in order to use a private DNS resolver, which you can manage yourself.</p>
<h3 id="split-tunnels">Split Tunnels</h3>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a> allow you to decide which IP addresses/ranges and/or domains are routed through or excluded from Cloudflare.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7432.md")
</aside>
