---
cp9:
  canonical: https://developers.cloudflare.com/network-interconnect/maintenance/
  description: Understand how Cloudflare coordinates maintenance across resilient CNI deployments.
  full_title: Maintenance · Cloudflare Network Interconnect docs
  head_html: <title>Maintenance · Cloudflare Network Interconnect docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand how Cloudflare coordinates maintenance across resilient CNI deployments."><link rel="canonical" href="https://developers.cloudflare.com/network-interconnect/maintenance/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network-interconnect/maintenance/index.md"><meta property="og:title" content="Maintenance · Cloudflare Network Interconnect docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand how Cloudflare coordinates maintenance across resilient CNI deployments."><meta property="og:url" content="https://developers.cloudflare.com/network-interconnect/maintenance/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network Interconnect"><meta name="algolia_product_filter" content="Network Interconnect"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Network Interconnect"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network-interconnect/maintenance/#page","headline":"Maintenance \u00b7 Cloudflare Network Interconnect docs","description":"Understand how Cloudflare coordinates maintenance across resilient CNI deployments.","url":"https://developers.cloudflare.com/network-interconnect/maintenance/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /network-interconnect/maintenance/
  schema: 1
---
<h2 id="planned-maintenance">Planned maintenance</h2>
<p>Routine CNI-disruptive maintenance is planned work that can interrupt traffic on an affected CNI connection. Cloudflare coordinates this work across resilient Cloudflare Network Interconnect (CNI) deployments, including across CNI locations.</p>
<h3 id="timing-and-scheduling">Timing and scheduling</h3>
<p>For Dataplane v2 connectivity in multi-homed PoPs only:</p>
<ul>
<li><strong>Routine maintenance</strong>: Minimum one week notice.</li>
<li><strong>Emergency maintenance</strong>: Best-effort notice, which may be less than one week.</li>
<li>Routine maintenance on redundant devices at the same location will occur on different days.</li>
<li>Routine maintenance is not rescheduled to accommodate customer schedule preferences.</li>
</ul>
<table>
<thead>
<tr>
<th>CNI deployment</th>
<th>During routine CNI-disruptive maintenance</th>
</tr>
</thead>
<tbody>
<tr>
<td>One CNI connection at one location</td>
<td>The connection can be interrupted.</td>
</tr>
<tr>
<td>Two CNI connections on separate devices at one location</td>
<td>One connection remains in service.</td>
</tr>
<tr>
<td>Four CNI connections across two coordinated locations, with two connections on separate devices at each location</td>
<td>Three connections remain in service.</td>
</tr>
</tbody>
</table>
<h2 id="emergency-and-non-routine-maintenance">Emergency and non-routine maintenance</h2>
<p>Non-routine maintenance, such as maintenance that affects an entire PoP, can affect all CNI connections at the affected location. For the four-connection deployment with two connections at each of two locations, a full-PoP non-routine event at one location can interrupt two connections, leaving two in service. Cloudflare avoids performing non-routine maintenance at multiple coordinated locations at the same time.</p>
<p>Cloudflare coordinates emergency maintenance across locations where feasible.</p>
<h2 id="receive-maintenance-notifications">Receive maintenance notifications</h2>
<p>To configure circuit-specific or point-of-presence (PoP) maintenance notifications, refer to <a href="/network-interconnect/monitoring-and-alerts/">Monitoring and alerts</a>.</p>
