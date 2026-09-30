---
cp9:
  canonical: https://developers.cloudflare.com/byoip/troubleshooting/
  description: Review common troubleshooting scenarios for BYOIP.
  full_title: Troubleshooting · Cloudflare BYOIP docs
  head_html: <title>Troubleshooting · Cloudflare BYOIP docs</title><meta name="generator" content="Nift"><meta name="description" content="Review common troubleshooting scenarios for BYOIP."><link rel="canonical" href="https://developers.cloudflare.com/byoip/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/byoip/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting · Cloudflare BYOIP docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review common troubleshooting scenarios for BYOIP."><meta property="og:url" content="https://developers.cloudflare.com/byoip/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="BYOIP"><meta name="algolia_product_filter" content="BYOIP"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="BYOIP"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/byoip/troubleshooting/#page","headline":"Troubleshooting \u00b7 Cloudflare BYOIP docs","description":"Review common troubleshooting scenarios for BYOIP.","url":"https://developers.cloudflare.com/byoip/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /byoip/troubleshooting/
  schema: 1
---
<p>The following topics are useful for troubleshooting BYOIP issues.</p>
<h2 id="urpf-filtering-and-packet-loss">uRPF filtering and packet loss</h2>
<p>Routers receive IP packets and forward the packets to the destination IP address. Unicast Reverse Path Forwarding (uRPF) is a security feature that can prevent spoofing attacks. uRPF operates under two modes: strict and loose mode.</p>
<p>Under <strong>strict mode</strong>, the router performs two checks on incoming packets to look for a matching entry in the source routing table and to determine whether the interface that received the packet can be used to reach the source. If the incoming IP packets pass both checks, the packets are forwarded; if the checks do not pass, the packets are dropped.</p>
<p>When uRPF is set to loose mode, the router performs a single check when it receives an IP packet to look for a source's matching entry in the routing table.</p>
<p>If you are experiencing packet loss as a result of an upstream ISP implementing uRPF filtering, contact your ISP and request the link be set to <strong>loose mode</strong>.</p>
<h2 id="non-sni-support">Non-SNI support</h2>
<p>Currently, BYOIP cannot be used with <a href="/ssl/edge-certificates/custom-certificates/uploading/">legacy custom certificates</a> to support <span class="nb-glossary-tooltip" title="Server Name Indication (SNI)">non-SNI</span> requests.</p>
<p>Instead, you can use Address Maps to set a default SNI for IPs on your account or zone. Refer to <a href="/byoip/address-maps/setup/#non-sni-support">Setup</a> for further guidance.</p>
<h2 id="self-serve-onboarding-api-errors">Self-serve onboarding API errors</h2>
<p>When onboarding BYOIP prefixes via the API, you may encounter the following errors:</p>
<table>
<thead>
<tr>
<th>Error code</th>
<th>Meaning</th>
<th>Resolution</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>prefix_not_valid_and_approved</code></td>
<td>The prefix has not passed IRR validation, RPKI validation, and ownership verification (or manual approval).</td>
<td>Verify all three validation steps have completed. If one or more are failing, check prefix registration with your Regional Internet Registry (RIR) and your RPKI ROA configuration. If validation is passing but you are still seeing this error, contact support for manual approval.</td>
</tr>
<tr>
<td><code>incomplete_bgp_deployment</code></td>
<td>Cannot create a BGP prefix without a default edge service binding configured.</td>
<td>Configure a default edge service binding before creating BGP prefixes.</td>
</tr>
<tr>
<td><code>advertise_state_locked</code></td>
<td>Cannot create a BGP prefix — the default edge service binding is still deploying.</td>
<td>Wait for the edge service binding deployment to complete, then retry.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3724.md")
</aside>
