---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/
  description: How DNS resolver IPs and hostnames works in Zero Trust networking.
  full_title: DNS resolver IPs and hostnames · Cloudflare One docs
  head_html: <title>DNS resolver IPs and hostnames · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How DNS resolver IPs and hostnames works in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/index.md"><meta property="og:title" content="DNS resolver IPs and hostnames · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How DNS resolver IPs and hostnames works in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/#page","headline":"DNS resolver IPs and hostnames \u00b7 Cloudflare One docs","description":"How DNS resolver IPs and hostnames works in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/
  schema: 1
---
<p>When you create a DNS location, Gateway assigns IPv4/IPv6 addresses and DoT/DoH hostnames to that location. These are the IP addresses and hostnames you send your DNS queries to for Gateway to resolve.</p>
<p>To view the resolver endpoint IP addresses and hostnames for a DNS location:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Networks</strong> &gt; <strong>Resolvers &amp; Proxies</strong>.</li>
<li>Select the DNS location, then select <strong>Edit</strong>.</li>
<li>Go to <strong>Setup instructions</strong>. The addresses and hostnames will appear in <strong>Your configuration</strong>.</li>
</ol>
<h2 id="dns-query-location-matching">DNS query location matching</h2>
<p>Gateway uses different methods to match a DNS query to DNS locations depending on the type of request and network:</p>
<pre tabindex="0"><code class="language-mermaid">flowchart TB&#10;    %% Accessibility&#10;    accTitle: How Gateway matches queries to DNS locations&#10;    accDescr: Flowchart describing the order of checks Cloudflare Gateway performs to determine the DNS location of a DNS query.&#10;&#10;    %% Flowchart&#10;    router([&quot;Router&quot;])--&gt;gateway[&quot;Cloudflare Gateway&quot;]&#10;&#10;    gateway--&gt;query{{&quot;Is the DNS query sent over HTTPS?&quot;}}&#10;&#10;    query--&quot;Yes&quot;--&gt;hostname[&quot;Look up location by&lt;br /&gt;unique hostname&quot;]&#10;    query--&quot;No&quot;--&gt;ipv4{{&quot;Is it over IPv4?&quot;}}&#10;&#10;    ipv4--&quot;Yes&quot;--&gt;source[&quot;Look up location by&lt;br /&gt;source IPv4 address&quot;]&#10;    ipv4--&quot;No&quot;--&gt;destination[&quot;Look up location by&lt;br /&gt;destination IPv6 address&quot;]&#10;</code></pre>
<ol>
<li>First, Gateway checks whether the query was sent using DNS over HTTPS. If yes, Gateway looks up the DNS location by its unique hostname.</li>
<li>Next, if the query was not sent with DNS over HTTPS, Gateway checks whether it was sent over IPv4. If yes, it looks up the DNS location by the source IPv4 address.</li>
<li>Last, if the query was not sent over IPv4, it means it was sent over IPv6. Gateway will look up the DNS location associated with the query based on the unique DNS resolver IPv6 address.</li>
</ol>
<h2 id="ipv4-ipv6-address">IPv4/IPv6 address</h2>
<h3 id="source-ip">Source IP</h3>
<p>Gateway uses the public source IPv4 address of your network to identify your DNS location, apply policies, and log DNS requests. Unless you have purchased a <a href="#dedicated-dns-resolver-ip">dedicated IPv4 resolver IP</a>, you must provide source IP addresses for the IPv4 traffic you want to filter with DNS policies. Otherwise, Gateway will not be able to attribute the traffic to your account.</p>
<p>If you are on an Enterprise plan, you have the option of manually entering one or more source IP addresses of your choice. This enables you to create Gateway DNS locations even if you are not connecting from any of those networks' IP addresses.</p>
<h3 id="dns-resolver-ip">DNS resolver IP</h3>
<p>When you create a DNS location, Gateway will resolve queries over IPv4 with the default DNS resolver IP addresses. These addresses are anycast IP addresses shared across every Cloudflare Zero Trust account. To resolve queries over IPv6, your location will receive and use a unique DNS resolver IPv6 address. These IP addresses are how Gateway will match DNS queries to locations and apply the appropriate filtering rules.</p>
<h4 id="dedicated-dns-resolver-ip">Dedicated DNS resolver IP</h4>
<p>Enterprise users can request a dedicated DNS resolver IPv4 address to be provisioned for a DNS location instead of the default anycast addresses. Queries forwarded to that address will be identified using the dedicated DNS resolver IPv4 address.</p>
<p>Cloudflare will only assign resolver IP addresses to the Zero Trust account you request. For more information on requesting dedicated DNS resolver IPv4 addresses, contact your account team.</p>
<h4 id="bring-your-own-dns-resolver-ip">Bring your own DNS resolver IP</h4>
<p>Enterprise users can use their own authority-provided IPv4 and IPv6 addresses as DNS endpoints for a location. Gateway can resolve UDP, TCP, DoT, and DoH queries through the IPv4 addresses provided, as well as UDP and TCP queries through the IPv6 addresses provided.</p>
<p>After you onboard your IP addresses, the IP addresses will appear under the associated endpoint when you create a new DNS location. If you did not provide IP addresses for a specific endpoint type, you can use the default Cloudflare resolver IPs or dedicated resolver IPs alongside your own resolver IPs. For example, if you want to use the IPv6 endpoint but only provided IPv4 addresses, you can use your own resolver IPs for IPv4 and the default Cloudflare IPs for IPv6.</p>
<p>For more information, refer to <a href="/byoip/">Cloudflare BYOIP</a> or contact your account team.</p>
<h2 id="dns-over-tls-dot">DNS over TLS (DoT)</h2>
<p>Each DNS location is assigned a unique hostname for DNS over TLS (DoT). Gateway will identify your location based on its DoT hostname.</p>
<h2 id="dns-over-https-doh">DNS over HTTPS (DoH)</h2>
<p>Each DNS location is assigned a unique hostname for DNS over HTTPS (DoH). Gateway will identify your location based on its DoH hostname.</p>
<h3 id="doh-subdomain">DoH subdomain</h3>
<p>Each DNS location in Cloudflare Zero Trust has a unique DoH subdomain (previously known as unique ID). If your organization uses DNS policies, you can enter your location's DoH subdomain as part of the Cloudflare One Client settings.</p>
<p>For example, for the DoH hostname <code>https://65y9p2vm1u.cloudflare-gateway.com/dns-query</code>, the DoH subdomain is <code>65y9p2vm1u</code>.</p>
<h2 id="send-specific-queries-to-gateway">Send specific queries to Gateway</h2>
<p>By default, all queries from a configured DNS location will be sent to its DNS resolver IP address to be inspected by Gateway. You can configure Gateway to only filter queries originating from specific networks within a location:</p>
<ol>
<li><a href="/cloudflare-one/reusable-components/lists/">Create an IP list</a> with the IPv4 and/or IPv6 addresses that your organization will source queries from.</li>
<li>Add a <a href="/cloudflare-one/traffic-policies/dns-policies/#source-ip">Source IP</a> condition to your DNS policies.</li>
</ol>
<p>For example, to block security threats for specific networks, you could create the following policy:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Security Categories</td>
<td>in</td>
<td>Select all categories that apply</td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>Source IP</td>
<td>in list</td>
<td>The name of the IP list containing your organization's networks</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>DNS queries made from IP addresses that are not in your IP list will not be filtered or populate your organization's <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway activity logs</a>.</p>
