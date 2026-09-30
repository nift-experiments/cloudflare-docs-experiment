---
cp9:
  canonical: https://developers.cloudflare.com/byoip/service-bindings/
  description: In IP address management, service binding refers to the association of IPs to specific Cloudflare services. Review the available options and the API endpoints to set up service bindings.
  full_title: IP address service bindings · Cloudflare BYOIP docs
  head_html: <title>IP address service bindings · Cloudflare BYOIP docs</title><meta name="generator" content="Nift"><meta name="description" content="In IP address management, service binding refers to the association of IPs to specific Cloudflare services. Review the available options and the API endpoints to set up service bindings."><link rel="canonical" href="https://developers.cloudflare.com/byoip/service-bindings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/byoip/service-bindings/index.md"><meta property="og:title" content="IP address service bindings · Cloudflare BYOIP docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="In IP address management, service binding refers to the association of IPs to specific Cloudflare services. Review the available options and the API endpoints to set up service bindings."><meta property="og:url" content="https://developers.cloudflare.com/byoip/service-bindings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="BYOIP"><meta name="algolia_product_filter" content="BYOIP"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="BYOIP"><meta name="pcx_tags" content="Bindings"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/byoip/service-bindings/#page","headline":"IP address service bindings \u00b7 Cloudflare BYOIP docs","description":"In IP address management, service binding refers to the association of IPs to specific Cloudflare services. Review the available options and the API endpoints to set up service bindings.","url":"https://developers.cloudflare.com/byoip/service-bindings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Bindings"]}</script>
  markdown: true
  noindex: false
  route: /byoip/service-bindings/
  schema: 1
---
<p>In the context of BYOIP, service bindings map traffic destined for IP addresses to the Cloudflare service it should be routed through - such as Magic Transit, CDN, or Spectrum. A default binding covering the entire prefix is required when you first <a href="/byoip/get-started/#2-create-service-bindings">onboard</a>, and additional bindings can be created at any time to route specific IP addresses or CIDR ranges to a different service.</p>
<p>For example, you could set Magic Transit as the default service for Layer 3 DDoS protection across the entire prefix, while directing specific IPs to the CDN for Layer 7 processing. Refer to <a href="#scope">Scope</a> for the available combinations.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3748.md")
</aside>
<h2 id="scope">Scope</h2>
<p>Customers using BYOIP with Magic Transit, <a href="/cache/">CDN services</a>, or <a href="/spectrum/">Spectrum</a> can leverage the <a href="/api/resources/addressing/subresources/prefixes/subresources/service_bindings/">service binding API endpoints</a> to selectively route traffic through the CDN <sup><a href="#footnote-1">1</a></sup> or Spectrum <sup><a href="#footnote-2">2</a></sup> pipelines on a per-IP address basis. This means:</p>
<ul>
<li>You can upgrade individual IPs within a Magic Transit prefix to either a CDN IP or a Spectrum IP. For example, if you have a Magic Transit prefix <code>203.0.113.0/24</code>, you can upgrade <code>203.0.113.1</code> to CDN and <code>203.0.113.2</code> to Spectrum.</li>
<li>You can upgrade individual IPs within a CDN prefix to a Spectrum IP. For example, if you have a CDN prefix <code>203.0.113.0/24</code>, you can upgrade <code>203.0.113.1</code> to Spectrum.</li>
<li>You can upgrade individual IPs within a Spectrum prefix to a CDN IP. For example, if you have a Spectrum prefix <code>203.0.113.0/24</code>, you can upgrade <code>203.0.113.1</code> to CDN.</li>
</ul>
<p>Refer to <a href="/byoip/service-bindings/magic-transit-with-cdn/">Magic Transit with CDN</a> or <a href="/byoip/service-bindings/cdn-and-spectrum/">CDN and Spectrum</a> for detailed guidance.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3747.md")
</aside>
<h3 id="cdn-cache">CDN (Cache)</h3>
<p>When a service binding of type <code>CDN</code> is applied, once the change has propagated across Cloudflare's global network (four to six hours), any HTTP requests are directed into the CDN pipeline for Layer 7 processing.</p>
<h3 id="spectrum">Spectrum</h3>
<p>When a service binding of type <code>Spectrum</code> is applied, once the change has propagated across Cloudflare's global network (four to six hours), any TCP/HTTP requests are directed into the Spectrum pipeline for Layer 4 or Layer 7 processing.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="udp-applications">UDP applications</h3>
@markup("md", "content/.markup/bodies/3746.md")
</aside>
<h3 id="magic-transit">Magic Transit</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3745.md")
</aside>
<p>The entire BYOIP prefix is primarily announced for Magic Transit, providing layer 3 DDoS protection and acceleration. Traffic not explicitly bound to CDN will flow through Magic Transit.</p>
<p>Also, traffic egressing to an IP in the prefix will always go to Magic Transit, even if there is an overlapping binding for CDN or Spectrum. This allows customers who want to use the same IP as ingress IP and as origin IP to do so.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;        accTitle: Cloudflare as a reverse proxy&#10;        accDescr: Diagram showing Cloudflare&#x27;s network between clients and the origin server.&#10;        A[Client] --ingress--&gt; B((Cloudflare))--egress--&gt; C[(Origin server)]&#10;</code></pre>
<p>When adding a service binding for a given IP address, it must be either a CDN service binding or a Spectrum service binding. It is not possible (or necessary) to bind both services.</p>
<h3 id="cdn-egress">CDN egress</h3>
<p><a href="/smart-shield/configuration/dedicated-egress-ips/">Dedicated CDN Egress IPs</a> (formerly known as Aegis) is only available for Enterprise. If you are interested, reach out to your account team. Also note that a single BYOIP prefix can be used for either CDN ingress or CDN egress, but not both.</p>
<h2 id="tutorials">Tutorials</h2>
<ul class="directory-listing"><li><a href="/byoip/service-bindings/magic-transit-with-cdn/">Use BYOIP with Magic Transit and CDN</a></li><li><a href="/byoip/service-bindings/cdn-and-spectrum/">Use BYOIP with CDN and Spectrum</a></li></ul>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Layer 7 HTTP-based</li>
<li id="footnote-2">Layer 4 or Layer 7 HTTP with custom ports</li></ol></section>
