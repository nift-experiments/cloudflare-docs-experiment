---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/
  description: Secure a private IP or hostname in Access.
  full_title: Secure a private IP or hostname · Cloudflare One docs
  head_html: <title>Secure a private IP or hostname · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Secure a private IP or hostname in Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/index.md"><meta property="og:title" content="Secure a private IP or hostname · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Secure a private IP or hostname in Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/#page","headline":"Secure a private IP or hostname \u00b7 Cloudflare One docs","description":"Secure a private IP or hostname in Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/
  schema: 1
---
<p>You can configure a self-hosted Access application to manage access to specific IPs or hostnames on your private network.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4791.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Private IPs and hostnames are reachable over the Cloudflare One Client, Cloudflare WAN (formerly Magic WAN) or Browser Isolation. For more details, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">Connect a private network</a>.</li>
<li>Private hostnames route to your custom DNS resolver through <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> or <a href="/cloudflare-one/traffic-policies/resolver-policies/">Gateway resolver policies</a>.</li>
<li>Public IPs and hostnames can be used to define a private application, however the IP or hostname must route through Cloudflare via <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/">Cloudflare Tunnel</a>, <a href="/mesh/">Cloudflare Mesh</a>, or <a href="/cloudflare-wan/configuration/how-to/configure-routes/">Cloudflare WAN</a>.</li>
<li>(Optional) Turn on <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">Gateway TLS decryption</a> if you want to use Access JWTs to manage <a href="#https-applications">HTTPS application sessions</a>.</li>
</ul>
<h2 id="add-your-application-to-access">Add your application to Access</h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Select <strong>Create new application</strong>.</p>
</li>
<li>
<p>Select <strong>Self-hosted and private</strong>.</p>
</li>
<li>
<p>To add an application using its private IP:
1. Select <strong>Add private IP</strong>.
2. In <strong>IP address</strong>, enter the private IP or CIDR range that represents the application (for example, <code>10.0.0.1</code> or <code>172.16.0.0/12</code>).
3. In <strong>Port</strong>, enter a single port or a port range used by your application (for example, <code>22</code> or <code>8000-8099</code>).</p>
<pre tabindex="0"><code>	Comma-separated lists of ports (such as `80, 443`) are not supported. To add multiple ports for a specific IP, you can select **Add private IP** and repeat the IP address with the other port. Alternatively, create a new Access application for the other port.&#10;</code></pre>
</li>
<li>
<p>To add an application using its private hostname:</p>
<ol>
<li>Select <strong>Add private hostname</strong>.</li>
<li>In <strong>Hostname</strong>, enter the private hostname of the application (for example, <code>wiki.internal.local</code>). You can use <a href="/cloudflare-one/access-controls/policies/app-paths/">wildcards</a> with private hostnames to protect multiple parts of an application that share a root path.</li>
<li>In <strong>Port</strong>, enter a single port or a port range used by your application (for example, <code>22</code> or <code>8000-8099</code>).</li>
</ol>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4790.md")
</aside>
