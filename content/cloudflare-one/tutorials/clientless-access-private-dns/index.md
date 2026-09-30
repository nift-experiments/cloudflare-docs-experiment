---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/tutorials/clientless-access-private-dns/
  description: With Cloudflare Browser Isolation and resolver policies, users can connect to private web-based applications via their private hostnames.
  full_title: Access a web application via its private hostname without the Cloudflare One Client · Cloudflare One docs
  head_html: <title>Access a web application via its private hostname without the Cloudflare One Client · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="With Cloudflare Browser Isolation and resolver policies, users can connect to private web-based applications via their private hostnames."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/tutorials/clientless-access-private-dns/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/tutorials/clientless-access-private-dns/index.md"><meta property="og:title" content="Access a web application via its private hostname without the Cloudflare One Client · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="With Cloudflare Browser Isolation and resolver policies, users can connect to private web-based applications via their private hostnames."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/tutorials/clientless-access-private-dns/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="DNS,Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/tutorials/clientless-access-private-dns/#page","headline":"Access a web application via its private hostname without the Cloudflare One Client \u00b7 Cloudflare One docs","description":"With Cloudflare Browser Isolation and resolver policies, users can connect to private web-based applications via their private hostnames.","url":"https://developers.cloudflare.com/cloudflare-one/tutorials/clientless-access-private-dns/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS","Private networks"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/tutorials/clientless-access-private-dns/
  schema: 1
---
<p>With Cloudflare Browser Isolation and resolver policies, users can connect to private web-based applications via their private hostnames without needing to install the Cloudflare One Client. By the end of this tutorial, users who pass your Gateway DNS and network policies will be able to access your private application at <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/browser/https://internalrecord.com</code>.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Make sure you have:</p>
<ul>
<li><a href="/cloudflare-one/remote-browser-isolation/">Cloudflare Browser Isolation</a> enabled on your account</li>
<li><a href="/cloudflare-one/traffic-policies/resolver-policies/">Resolver policies</a> enabled on your account</li>
<li>An HTTP or HTTPS application that users access through a browser</li>
</ul>
<h2 id="create-a-cloudflare-tunnel">Create a Cloudflare Tunnel</h2>
<p>First, install <code>cloudflared</code> on a server in your private network:</p>
<ol>
<li>Log in to the Cloudflare dashboard and go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Create a tunnel</strong>.</p>
</li>
<li>
<p>Enter a name for your tunnel. We suggest choosing a name that reflects the type of resources you want to connect through this tunnel (for example, <code>enterprise-VPC-01</code>).</p>
</li>
<li>
<p>Select <strong>Create Tunnel</strong>.</p>
</li>
<li>
<p>Choose your operating system, then copy the installation command and run it in a terminal on your origin server.</p>
</li>
<li>
<p>Wait for the tunnel to connect. Once the connection is established, select <strong>Continue</strong>.</p>
</li>
</ol>
<h2 id="add-private-network-routes">Add private network routes</h2>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Routes</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Create route</strong> &gt; <strong>Tunnel CIDR</strong>. Select the tunnel you just created, enter the private IP/CIDR of your application server (for example, <code>10.128.0.175/32</code>), and select <strong>Create route</strong>.</p>
</li>
<li>
<p>Repeat to create a second route for the private IP/CIDR of your DNS server.</p>
</li>
</ol>
<p>The application and DNS server are now connected to Cloudflare.</p>
<h2 id="enable-clientless-web-isolation">Enable Clientless Web Isolation</h2>
<ol>
<li>
<p>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Browser isolation</strong> &gt; <strong>Browser isolation settings</strong>.</p>
</li>
<li>
<p>Turn on <strong>Allow users to open a remote browser without the device client</strong>.</p>
</li>
<li>
<p>For <strong>Permissions</strong>, select <strong>Manage</strong>.</p>
</li>
<li>
<p>Select <strong>Add a rule</strong>.</p>
</li>
<li>
<p>Create an expression that defines who can open the Clientless Web Isolation browser. For example,</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Rule action</th>
<th>Rule type</th>
<th>Selector</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Allow</td>
<td>Include</td>
<td>Emails ending in</td>
<td><code>@example.com</code></td>
<td>Select <strong>Save</strong>.</td>
</tr>
</tbody>
</table>
<p>To test, open a browser and go to <code>https://&lt;team-name&gt;.cloudflareaccess.com/browser/https://&lt;private-IP-of-application&gt;</code>.</p>
<h2 id="create-a-gateway-resolver-policy">Create a Gateway resolver policy</h2>
<ol>
<li>
<p>Go to <strong>Traffic policies</strong> &gt; <strong>Resolver policies</strong>.</p>
</li>
<li>
<p>Select <strong>Add a policy</strong>.</p>
</li>
<li>
<p>Create an expression to match against the private <a href="/cloudflare-one/traffic-policies/resolver-policies/#domain">domain</a> or <a href="/cloudflare-one/traffic-policies/resolver-policies/#host">hostname</a> of the application:</p>
</li>
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
<td><code>internalrecord.com</code></td>
</tr>
</tbody>
</table>
<ol start="4">
<li>
<p>In <strong>Select DNS resolver</strong>, select <em>Configure custom DNS resolvers</em>.</p>
</li>
<li>
<p>Enter the private IP address of your DNS server.</p>
</li>
<li>
<p>In the dropdown menu, select <em><code>&lt;IP-address&gt; - Private</code></em>.</p>
</li>
<li>
<p>(Optional) Enter a custom port.</p>
</li>
<li>
<p>Select <strong>Create policy</strong>.</p>
</li>
</ol>
<p>To test, open a browser and go to <code>https://&lt;team-name&gt;.cloudflareaccess.com/browser/https://internalrecord.com</code>.</p>
<h2 id="create-a-gateway-network-policy-recommended">Create a Gateway network policy (recommended)</h2>
<ol>
<li>
<p>Go to <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong> &gt; <strong>Network</strong>.</p>
</li>
<li>
<p>Add a <a href="/cloudflare-one/traffic-policies/network-policies/">network policy</a> that targets the private IP address of your application. You can optionally include any ports or protocols relevant for application access. For example,</p>
</li>
</ol>
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
<td>Destination IP</td>
<td>in</td>
<td><code>10.128.0.175</code></td>
<td>And</td>
<td>Allow</td>
</tr>
<tr>
<td>Destination Port</td>
<td>in</td>
<td><code>80</code></td>
<td>Or</td>
<td></td>
</tr>
<tr>
<td>User Email</td>
<td>matches regex</td>
<td><code>.*example.com</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4325.md")
</aside>
<p>For best practices on securing private applications, refer to <a href="/learning-paths/replace-vpn/build-policies/">Build secure access policies</a>.</p>
<h2 id="connect-as-a-user">Connect as a user</h2>
<p>Users can now access the application at the following URL:</p>
<p><code>https://&lt;team-name&gt;.cloudflareaccess.com/browser/https://internalrecord.com</code></p>
<p>The application will load in an isolated browser. You can optionally <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/#policy-settings">configure remote browser controls</a> such as disabling copy/paste, printing, or keyboard input.</p>
