---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/tutorials/regional-private-dns-resolver-policies/
  description: Configure Gateway resolver policies to route DNS queries to region-specific private DNS servers, enabling geo-steering for internal resources across multiple locations.
  full_title: Implement regional private DNS servers with Gateway resolver policies · Cloudflare One docs
  head_html: <title>Implement regional private DNS servers with Gateway resolver policies · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Gateway resolver policies to route DNS queries to region-specific private DNS servers, enabling geo-steering for internal resources across multiple locations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/tutorials/regional-private-dns-resolver-policies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/tutorials/regional-private-dns-resolver-policies/index.md"><meta property="og:title" content="Implement regional private DNS servers with Gateway resolver policies · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Gateway resolver policies to route DNS queries to region-specific private DNS servers, enabling geo-steering for internal resources across multiple locations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/tutorials/regional-private-dns-resolver-policies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="DNS,Geolocation,Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/tutorials/regional-private-dns-resolver-policies/#page","headline":"Implement regional private DNS servers with Gateway resolver policies \u00b7 Cloudflare One docs","description":"Configure Gateway resolver policies to route DNS queries to region-specific private DNS servers, enabling geo-steering for internal resources across multiple locations.","url":"https://developers.cloudflare.com/cloudflare-one/tutorials/regional-private-dns-resolver-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS","Geolocation","Private networks"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/tutorials/regional-private-dns-resolver-policies/
  schema: 1
---
<p>Gateway resolver policies allow you to route DNS queries to custom DNS resolvers based on various criteria. This tutorial demonstrates how to configure region-specific private DNS servers to ensure your users are directed to the closest internal resources based on their geographic location.</p>
<p>This approach is particularly useful for organizations with internal networks spanning multiple locations where DNS routes and manages access to private network resources.</p>
<p>By the end of this tutorial, you will have configured Gateway resolver policies to automatically route DNS queries to region-specific private DNS servers based on user location, providing optimal performance and access to internal resources.</p>
<p>This tutorial uses US and EU region servers as example private DNS servers.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, make sure you have:</p>
<ul>
<li>An Enterprise Zero Trust account</li>
<li>Private DNS servers deployed in multiple regions (for example, US, EU, and APAC)</li>
<li>A <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> connecting your private DNS servers to Cloudflare</li>
<li>Internal domains that need to be resolved (for example, <code>internal.example.com</code>)</li>
</ul>
<h2 id="1-connect-private-dns-servers-with-cloudflare-tunnel"><ol>
<li>Connect private DNS servers with Cloudflare Tunnel</li>
</ol></h2>
<p>First, connect your regional private DNS servers to Cloudflare using Cloudflare Tunnel.</p>
<p>For each region where you have a private DNS server, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/#1-create-a-tunnel">create a tunnel</a>. For each tunnel, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/#2-add-private-network-routes">add the private IP addresses</a> of your DNS servers. For example, <code>10.0.1.53/32</code> for the US region and <code>10.1.1.53/32</code> for the EU region.</p>
<p>Repeat this process for all regional DNS servers.</p>
<h2 id="2-create-gateway-resolver-policies-for-each-region"><ol start="2">
<li>Create Gateway resolver policies for each region</li>
</ol></h2>
<p>Once your private DNS servers are connected to Cloudflare, configure Gateway resolver policies to route DNS queries to the appropriate regional DNS server based on user location.</p>
<h3 id="create-resolver-policies-for-each-region">Create resolver policies for each region</h3>
<p>For each region where you have a private DNS server:</p>
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>Resolver policies</strong>.</li>
<li>Select <strong>Add a policy</strong>.</li>
<li>Name your policy based on the region (for example, <code>US Internal DNS</code>).</li>
<li>Create an expression to match internal domains and users in that region. For example, to match users in the United States:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
</tr>
</thead>
<tbody>
<tr>
<td>Domain</td>
<td>in</td>
<td><code>internal.example.com</code></td>
<td>And</td>
</tr>
<tr>
<td>Source Country IP Geolocation</td>
<td>in</td>
<td><em>United States</em></td>
<td></td>
</tr>
</tbody>
</table>
<ol start="5">
<li>In <strong>Select DNS resolver</strong>, select <em>Configure custom DNS resolvers</em>.</li>
<li>Enter the private IP address of your regional DNS server (for example, <code>10.0.1.53</code> for US or <code>10.1.1.53</code> for EU).</li>
<li>In the dropdown menu, choose <em><code>&lt;IP-address&gt; - Private</code></em>.</li>
<li>(Optional) Select <strong>Add DNS resolver</strong> and enter a secondary IP address to add a backup DNS resolver.</li>
<li>Select <strong>Create policy</strong>.</li>
<li>Repeat steps 1-9 for each region where you have a private DNS server. For example, to create a policy to match users in the EU region:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
</tr>
</thead>
<tbody>
<tr>
<td>Domain</td>
<td>in</td>
<td><code>internal.example.com</code></td>
<td>And</td>
</tr>
<tr>
<td>Source Country IP Geolocation</td>
<td>in</td>
<td><em>Austria</em>, <em>Belgium</em>, <em>France</em>, <em>Germany</em>, <em>Netherlands</em></td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="create-a-fallback-resolver-policy">Create a fallback resolver policy</h3>
<p>Create a catch-all policy for users in regions without a dedicated DNS server, or if no policies match your traffic:</p>
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>Resolver policies</strong>.</li>
<li>Select <strong>Add a policy</strong>.</li>
<li>Name your policy (for example, <code>Internal DNS Fallback</code>).</li>
<li>Create an expression to match internal domains:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Domain</td>
<td>in</td>
<td><code>internal.example.com</code></td>
</tr>
</tbody>
</table>
<ol start="5">
<li>In <strong>Select DNS resolver</strong>, select <em>Configure custom DNS resolvers</em>.</li>
<li>Enter the private IP address of your primary DNS server.</li>
<li>Select <strong>Create policy</strong>.</li>
</ol>
<h2 id="3-configure-policy-order"><ol start="3">
<li>Configure policy order</li>
</ol></h2>
<p>Gateway will apply resolver policies based on <a href="/cloudflare-one/traffic-policies/order-of-enforcement/#order-of-precedence">order of precedence</a>. Ensure your policies are ordered from most specific to least specific:</p>
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>Resolver policies</strong>.</li>
<li>Use the drag handle to reorder policies:
<ul>
<li>Resolver policies with regional coverage first</li>
<li>Your fallback resolver policy last</li>
</ul>
</li>
</ol>
<p>Gateway will apply the first matching policy. If no policies match your traffic, Gateway will apply the fallback resolver policy. The order between resolver policies with regional coverage does not matter.</p>
<h2 id="4-test-your-configuration"><ol start="4">
<li>Test your configuration</li>
</ol></h2>
<h3 id="test-from-different-regions">Test from different regions</h3>
<p>To test your configuration, deploy the Cloudflare One Client on a device in each region where you have a private DNS server and run a DNS query to an internal domain. For example, to test the US region:</p>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">Deploy the Cloudflare One Client</a> on a device in the US region.</li>
<li>From the device, open a terminal and run:</li>
</ol>
<pre tabindex="0"><code class="language-sh">nslookup internal.example.com&#10;</code></pre>
<ol start="3">
<li>Verify that the DNS query returns the expected IP address for your internal resource. The response should show the IP address that your US DNS server is configured to return for <code>internal.example.com</code>.</li>
<li>Repeat the test from devices in other regions to confirm they receive responses from their respective regional DNS servers. Each region may return different IP addresses based on your DNS server configuration.</li>
</ol>
<h3 id="verify-in-gateway-logs">Verify in Gateway logs</h3>
<ol>
<li>Go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>DNS query logs</strong>.</li>
<li>Filter for queries to <code>internal.example.com</code>.</li>
<li>Check the <strong>Resolver IP</strong> field to confirm queries are being routed to the correct regional DNS servers based on user location.</li>
</ol>
<h2 id="best-practices">Best practices</h2>
<ul>
<li><strong>Use backup resolvers</strong>: Configure secondary DNS resolvers for each region to ensure high availability.</li>
<li><strong>Monitor DNS performance</strong>: Use <a href="/cloudflare-one/insights/analytics/gateway/">Gateway Analytics</a> to track DNS query performance and identify any issues with regional routing.</li>
<li><strong>Implement network policies</strong>: Combine resolver policies with <a href="/cloudflare-one/traffic-policies/network-policies/">network policies</a> to control access to internal resources based on user identity and device posture.</li>
<li><strong>Consider virtual networks</strong>: If you have overlapping IP address spaces across regions, use <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">virtual networks</a> to isolate traffic.</li>
<li><strong>Test failover scenarios</strong>: Regularly test what happens when a regional DNS server becomes unavailable to ensure your backup resolvers work as expected.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/traffic-policies/resolver-policies/">Resolver policies</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Connect private networks</a></li>
<li><a href="/cloudflare-one/insights/analytics/gateway/">Gateway Analytics</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">Virtual networks</a></li>
</ul>
