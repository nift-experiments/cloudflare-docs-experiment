---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/
  description: Proxy endpoints in Zero Trust networking.
  full_title: Proxy endpoints · Cloudflare One docs
  head_html: <title>Proxy endpoints · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Proxy endpoints in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/index.md"><meta property="og:title" content="Proxy endpoints · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Proxy endpoints in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="JavaScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#page","headline":"Proxy endpoints \u00b7 Cloudflare One docs","description":"Proxy endpoints in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5829.md")
</aside>
<p>Proxy endpoints allow you to apply Gateway policies without installing a client on your devices. By configuring a <a href="#what-is-a-pac-file">Proxy Auto-Configuration (PAC) file</a> at the browser level, you can route traffic through Gateway for filtering and policy enforcement. Cloudflare supports configuring two types of proxy endpoints: identity-based <a href="#authorization-endpoint">authorization endpoints</a> and <a href="#source-ip-endpoint">source IP proxy endpoints</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5828.md")
</aside>
<h3 id="when-to-use-proxy-endpoints">When to use proxy endpoints</h3>
<p>Proxy endpoints are designed for environments where deploying the Cloudflare One Client is not an option. Common use cases include:</p>
<ul>
<li><strong>Virtual desktops (VDI)</strong>: Users log into a virtual machine and use a browser to reach the Internet.</li>
<li><strong>Compliance-restricted endpoints</strong>: Environments where you are legally or technically prohibited from installing software on the endpoint.</li>
<li><strong>Legacy SWG migration</strong>: Organizations transitioning from legacy Secure Web Gateways that use PAC files.</li>
</ul>
<h3 id="logging">Logging</h3>
<p>Traffic sent through proxy endpoints generates <a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust Network Session Logs</a>, which are available via <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a> and <a href="/log-explorer/">Log Explorer</a>.</p>
<h3 id="what-is-a-pac-file">What is a PAC file</h3>
<div class="nb-glossary-definition"><p>A PAC file is a file containing a JavaScript function which can instruct a browser to forward traffic to a proxy server instead of directly to the destination server.</p></div>
<p>When end users visit a website, their browser sends the request to a Cloudflare proxy server associated with your account to be filtered by Gateway. PAC files are evaluated by the browser for every request, determining whether traffic should go through the proxy or connect directly. Note that Gateway <a href="#traffic-limitations">cannot filter every type of HTTP traffic</a> proxied using PAC files.</p>
<p>PAC files offer several advantages:</p>
<ul>
<li><strong>Centralized management</strong>: Update routing rules in one location without reconfiguring individual devices</li>
<li><strong>Flexible routing</strong>: Route different traffic types to different proxies or direct connections based on domain, IP range, or protocol</li>
<li><strong>Load balancing</strong>: Distribute traffic across multiple proxy servers with automatic failover</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5827.md")
</aside>
<h3 id="types-of-proxy-endpoints">Types of proxy endpoints</h3>
<p>Cloudflare One offers two types of proxy endpoints, each with different authorization methods.</p>
<p>Once you create a proxy endpoint, you cannot change its type. If you need a different authorization method, you must create a new proxy endpoint.</p>
<h4 id="authorization-endpoint">Authorization endpoint</h4>
<p>Authorization endpoints use <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> to provide Zero Trust authorization. Users must authenticate through an identity provider and pass Access policies before they can use the proxy endpoint.</p>
<p>Use authorization endpoints when:</p>
<ul>
<li>You need user-level authentication and identity-based policies</li>
<li>You want to associate specific users with their proxy traffic</li>
<li>Your organization requires login through identity providers (such as Okta, Microsoft Entra ID, or Google Workspace)</li>
<li>You need granular control over who can access the proxy</li>
</ul>
<h4 id="source-ip-endpoint">Source IP endpoint</h4>
<p>Source IP endpoints authorize traffic based on the originating IP address. Only traffic from pre-configured IP addresses can use the proxy endpoint.</p>
<p>Use source IP endpoints when:</p>
<ul>
<li>You have a fixed set of office or network locations</li>
<li>You want simpler setup without user authentication</li>
<li>Your devices share a common egress IP address</li>
<li>You do not need to identify individual users</li>
</ul>
<h2 id="1-create-a-proxy-endpoint"><ol>
<li>Create a proxy endpoint</li>
</ol></h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5826.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5836.md")
</div></div>
<h2 id="2-create-a-pac-file"><ol start="2">
<li>Create a PAC file</li>
</ol></h2>
<p>A PAC file is a text file written in JavaScript that specifies which traffic should redirect to the proxy server. You can create a PAC file in the Cloudflare dashboard or write your own custom PAC file.</p>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/5824.md")
</aside>
<h3 id="create-a-hosted-pac-file">Create a hosted PAC file</h3>
<p>When you create a PAC file in Cloudflare One, Cloudflare will host it in a publicly accessible Worker. Hosted PAC files are automatically distributed through Cloudflare's global network.</p>
<p>To create a hosted PAC file:</p>
<ol>
<li>
<p>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Networks</strong> &gt; <strong>Resolvers &amp; Proxies</strong>.</p>
</li>
<li>
<p>Select <strong>Proxy endpoints</strong>.</p>
</li>
<li>
<p><a href="#1-create-a-proxy-endpoint">Create a proxy endpoint</a> or select an existing one, then select <strong>Edit</strong>.</p>
</li>
<li>
<p>Select <strong>Add PAC files</strong>.</p>
</li>
<li>
<p>Configure your PAC file:</p>
<p>In <strong>PAC file details</strong>:</p>
<ol>
<li>Enter the <strong>Basic Information</strong>, including a name and optional description.</li>
<li>(Optional) Customize the <strong>URL slug</strong> to create a memorable URL path. The slug cannot be changed after creation.</li>
<li>In <strong>PAC file configuration</strong>, select <strong>Browse PAC file configuration templates</strong> and choose a pre-configured template to customize. The available templates are Okta and Azure. After you select a template, <strong>PAC file JavaScript</strong> will populate with the selected template.</li>
<li>Modify the JavaScript as needed to match your network requirements.</li>
</ol>
<p>In <strong>Setup instructions</strong>:</p>
<ol>
<li>Choose a browser.</li>
<li>Follow the instructions in Cloudflare One to configure devices.</li>
</ol>
</li>
<li>
<p>Select <strong>Create</strong>.</p>
</li>
</ol>
<p>Your hosted PAC file URL will be:</p>
<pre tabindex="0"><code class="language-txt">https://pac.cloudflare-gateway.com/&lt;account-id&gt;/&lt;slug&gt;&#10;</code></pre>
<p>Where:</p>
<ul>
<li><code>&lt;account-id&gt;</code> is your <a href="/fundamentals/account/find-account-and-zone-ids/">Cloudflare account ID</a></li>
<li><code>&lt;slug&gt;</code> is the customizable path you specified (or an auto-generated value if not customized)</li>
</ul>
<h4 id="hosted-pac-file-limits">Hosted PAC file limits</h4>
<p>Cloudflare-hosted PAC files have the following limits:</p>
<ul>
<li><strong>Maximum file size</strong>: 256 KB per PAC file</li>
<li><strong>Maximum PAC files per account</strong>: 50 (non-Enterprise plans) or 1,000 (Enterprise plans)</li>
<li><strong>Update propagation</strong>: Changes to PAC files propagate within seconds to minutes across the global network</li>
</ul>
<h4 id="caching-behavior">Caching behavior</h4>
<p>Hosted PAC files are cached globally for performance and reliability:</p>
<ul>
<li>Browsers and operating systems may cache PAC files locally based on their own policies</li>
<li>Updates to hosted PAC files automatically invalidate the cache</li>
<li>If you need to force clients to fetch a new version, you may need to clear browser caches or restart browsers depending on the client configuration</li>
</ul>
<h3 id="self-hosting-pac-files">Self-hosting PAC files</h3>
<p>You can also host PAC files on your own infrastructure, such as an internal web server or <a href="/workers/">Cloudflare Workers</a>. Self-hosting gives you complete control over the hosting environment but requires you to manage availability and distribution.</p>
<h3 id="proxy-endpoint-limits">Proxy endpoint limits</h3>
<p>Each account has a maximum number of proxy endpoints:</p>
<ul>
<li><strong>Non-Enterprise plans</strong>: 50 proxy endpoints</li>
<li><strong>Enterprise plans</strong>: 500 proxy endpoints</li>
</ul>
<h2 id="3-configure-your-devices"><ol start="3">
<li>Configure your devices</li>
</ol></h2>
<h3 id="3a-install-cloudflare-certificate">3a. Install Cloudflare certificate</h3>
<p>You must <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">install a Cloudflare certificate</a> on your devices. Authorization endpoints use the certificate to inspect TLS traffic and read the authorization cookie. Source IP endpoints use the certificate to apply Gateway HTTP policies such as blocking specific domains or displaying the Gateway block page.</p>
<h3 id="3b-configure-browser-to-use-pac-file">3b. Configure browser to use PAC file</h3>
<p>All major browsers support PAC files. You can configure individual browsers, or you can configure system-level proxy settings that apply to all browsers on the device. Multiple devices can call the same PAC file as long as their source IP addresses were included in the proxy endpoint configuration.</p>
<p>For detailed, OS-specific instructions (including Windows, macOS, Linux, iOS, Android, ChromeOS, and enterprise deployment), refer to <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/configure-pac-file-on-device/">Configure a PAC file on your device</a>.</p>
<details class="nb-details"><summary>Chromium-based browsers</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5837.md")
</div></details>
<details class="nb-details"><summary>Mozilla Firefox</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5838.md")
</div></details>
<details class="nb-details"><summary>Safari</summary><div class="nb-details-body">
@input("content/.markup/bodies/5839.md")
</div></details>
<h2 id="4-test-your-http-policy"><ol start="4">
<li>Test your HTTP policy</li>
</ol></h2>
<p>To test your configuration, create an <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policy</a> to block a test domain. When you visit the blocked domain in your browser, you should see the Gateway block page.</p>
<p>You can now use the Proxy Endpoint selector in <a href="/cloudflare-one/traffic-policies/network-policies/#proxy-endpoint">network</a> and <a href="/cloudflare-one/traffic-policies/http-policies/#proxy-endpoint">HTTP</a> policies to filter traffic proxied via PAC files.</p>
<h2 id="5-optional-configure-firewall"><ol start="5">
<li>(Optional) Configure firewall</li>
</ol></h2>
<p>You may need to configure your organization's firewall to allow your users to connect to a proxy endpoint. Depending on your firewall, you will need to create a rule using either your proxy endpoint's domain or IP addresses.</p>
<p>To get the domain of a proxy endpoint:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5842.md")
</div></div>
<p>Using your proxy endpoint's domain, you can get the IP addresses assigned to the proxy endpoint:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5845.md")
</div></div>
<p>To ensure responses are allowed through your firewall, add an inbound rule to allow the static IPv4 address for Cloudflare proxy endpoints, <code>162.159.193.21</code>.</p>
<h2 id="edit-proxy-endpoints">Edit proxy endpoints</h2>
<p>You can modify proxy endpoint settings after creation.</p>
<h3 id="edit-authorization-endpoint">Edit authorization endpoint</h3>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Networks</strong> &gt; <strong>Resolvers &amp; Proxies</strong> &gt; <strong>Proxy endpoints</strong>.</li>
<li>Locate your authorization endpoint (indicated by <strong>Authorization</strong> under <strong>Type</strong>).</li>
<li>Select the three dots, then select <strong>Configure</strong>.</li>
<li>Choose what to edit:
<ul>
<li><strong>Basic info</strong>: Update the endpoint name and description.</li>
<li><strong>Access policies</strong>: Add, remove, or modify Access policies that control who can use the endpoint.</li>
<li><strong>Login methods</strong>: Select which <a href="/cloudflare-one/integrations/identity-providers/">identity providers</a> users can authenticate with.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h3 id="edit-source-ip-endpoint">Edit source IP endpoint</h3>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Networks</strong> &gt; <strong>Resolvers &amp; Proxies</strong> &gt; <strong>Proxy endpoints</strong>.</li>
<li>Locate your source IP endpoint (indicated by <strong>Source IP</strong> under <strong>Type</strong>).</li>
<li>Select the three dots, then select <strong>Configure</strong>.</li>
<li>Update the endpoint name or modify the allowed source IP addresses.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="logs">Logs</h2>
<p>Proxy endpoint traffic is logged in the following locations:</p>
<ul>
<li><strong>Authentication logs</strong>: When users authenticate through an authorization endpoint, login events appear in your <a href="/cloudflare-one/insights/logs/">Access logs</a>.</li>
<li><strong>Traffic logs</strong>: HTTP and network traffic proxied through the endpoint appears in <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway logs</a>, with the specific proxy endpoint indicated.</li>
</ul>
<h2 id="billing">Billing</h2>
<p>Each user who authenticates through an authorization proxy endpoint occupies a <a href="/cloudflare-one/team-and-resources/users/seat-management/">Gateway seat</a>, the same as a user connected through the Cloudflare One Client.</p>
<h2 id="limitations">Limitations</h2>
<h3 id="authorization-endpoint-limitations">Authorization endpoint limitations</h3>
<p>When using <a href="#authorization-endpoint">authorization endpoints</a>, be aware of the following limitations. For configuration guidance on apps with certificate pinning, refer to <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/best-practices/#apps-with-certificate-pinning">PAC file best practices</a>.</p>
<h4 id="tls-inspection-required">TLS inspection required</h4>
<p>Authorization endpoints require <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS inspection</a> on all proxied traffic. Gateway must decrypt HTTPS requests to read the authorization cookie that identifies each user session. Gateway always performs TLS decryption for traffic routed through an authorization endpoint, even if you turn off TLS decryption at the account level. You cannot selectively bypass TLS inspection for specific destinations when using an authorization endpoint.</p>
<h4 id="plaintext-http-traffic">Plaintext HTTP traffic</h4>
<p>Authorization endpoints do not support plaintext HTTP traffic unless the traffic is configured through an <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">Access application</a> or bypassed with the PAC file.</p>
<h4 id="referer-header-traffic">Referer header traffic</h4>
<p>Traffic with a referer HTTP header matching the domain of a recently logged in user from the same source IP will be allowed through and logged with the following non-identity email address:</p>
<pre tabindex="0"><code class="language-txt">auth-proxy-non-identity@&lt;your-team-name&gt;.cloudflareaccess.com&#10;</code></pre>
<p>Where <code>&lt;your-team-name&gt;</code> is your <a href="/cloudflare-one/faq/getting-started-faq/#what-is-a-team-domainteam-name">team name</a>.</p>
<p>This occurs because browsers do not tag HTTP sub-requests with the identity cookie used to verify user authentication. This is an industry-standard behavior for proxy-based Secure Web Gateways.</p>
<p>To filter this traffic, you have two options:</p>
<ul>
<li>Set up an <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policy</a> to block or allow all traffic matching the <code>auth-proxy-non-identity@&lt;your-team-name&gt;.cloudflareaccess.com</code> email address.</li>
<li>To restrict non-identity traffic to specific source IPs, create a <a href="/cloudflare-one/traffic-policies/network-policies/">network policy</a> that matches both the source IP and the proxy endpoint.</li>
</ul>
<h3 id="safari-and-ios-not-supported">Safari and iOS not supported</h3>
<p>Safari (on macOS) and all browsers on iOS/iPadOS do not support the HTTPS proxy type that Cloudflare proxy endpoints require. This is a platform-level limitation confirmed by Apple. On macOS, use a Chromium-based browser or Firefox instead. On iOS/iPadOS, proxy endpoints cannot be used.</p>
<h3 id="traffic-limitations">Traffic limitations</h3>
<p>Each type of proxy endpoint supports the following features:</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Source IP endpoint</th>
<th>Authorization endpoint</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>HTTP/HTTPS traffic</strong></td>
<td>✅<sup><a href="#footnote-1">1</a></sup></td>
<td>✅<sup><a href="#footnote-2">2</a></sup></td>
</tr>
<tr>
<td><strong>Non-HTTP TCP traffic</strong></td>
<td>✅</td>
<td>—</td>
</tr>
<tr>
<td><strong>UDP traffic</strong></td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td><strong><a href="/cloudflare-one/traffic-policies/http-policies/http3/">HTTP3</a></strong></td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td><strong><a href="/cloudflare-one/traffic-policies/identity-selectors/">Identity-based policies</a></strong></td>
<td>—</td>
<td>✅</td>
</tr>
<tr>
<td><strong>mTLS authentication</strong></td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td><strong><a href="https://datatracker.ietf.org/doc/html/rfc6555">Happy Eyeballs</a></strong></td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td><strong>Browser HTTPS auto-upgrade</strong></td>
<td>—<sup><a href="#footnote-3">3</a></sup></td>
<td>—<sup><a href="#footnote-3">3</a></sup></td>
</tr>
</tbody>
</table>
<h3 id="session-duration">Session duration</h3>
<p>All connections proxied through Cloudflare Gateway have a maximum guaranteed duration of 10 hours. For more information, refer to <a href="/cloudflare-one/access-controls/troubleshooting/#long-lived-ssh-sessions-disconnect">Troubleshooting</a>.</p>
<h3 id="gateway-dns-and-resolver-policies">Gateway DNS and resolver policies</h3>
<p>Gateway <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS</a> and <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver</a> policies will always apply to traffic proxied with PAC files, regardless of device configuration.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">For [source IP endpoints](#source-ip-endpoint), to access plaintext HTTP (non-HTTPS) origins, configure them as [self-hosted Access applications](/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/). This allows users to access HTTP resources while maintaining security through Access policies.</li>
<li id="footnote-2">To access plaintext HTTP (non-HTTPS) origins with [authorization endpoints](#authorization-endpoint), refer to [Plaintext HTTP traffic](#plaintext-http-traffic).</li>
<li id="footnote-3">Proxy endpoints do not support HTTPS when browsers automatically upgrade HTTP requests to HTTPS (such as Chrome's automatic HTTPS upgrades). If you encounter connection issues with sites that are being auto-upgraded, you may need to disable automatic HTTPS upgrades in your browser settings or configure the site as an exception.</li></ol></section>
