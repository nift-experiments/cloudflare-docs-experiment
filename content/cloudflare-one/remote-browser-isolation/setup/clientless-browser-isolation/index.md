---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/
  description: How Clientless Web Isolation works in Browser Isolation.
  full_title: Clientless Web Isolation · Cloudflare One docs
  head_html: <title>Clientless Web Isolation · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How Clientless Web Isolation works in Browser Isolation."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/index.md"><meta property="og:title" content="Clientless Web Isolation · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Clientless Web Isolation works in Browser Isolation."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/#page","headline":"Clientless Web Isolation \u00b7 Cloudflare One docs","description":"How Clientless Web Isolation works in Browser Isolation.","url":"https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/
  schema: 1
---
<p>Clientless Web Isolation allows users to securely browse high risk or sensitive websites in a remote browser without having to install the Cloudflare One Client on their device. Use Clientless Web Isolation when you need to provide isolated browsing to unmanaged devices (for example, contractor laptops or personal phones) where you cannot install software.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5891.md")
</aside>
<h2 id="set-up-clientless-web-isolation">Set up Clientless Web Isolation</h2>
<ol>
<li>
<p>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Browser isolation</strong> &gt; <strong>Browser isolation settings</strong>.</p>
</li>
<li>
<p>Turn on <strong>Allow users to open a remote browser without the device client</strong>.</p>
</li>
<li>
<p>To configure permissions, in <strong>Browser isolation</strong> &gt; <strong>Browser isolation settings</strong> &gt; select <strong>Manage</strong> next to <strong>Manage remote browser permissions</strong>. You can add authentication methods and <a href="/cloudflare-one/access-controls/policies/">rules</a> to control who can access the remote browser.</p>
</li>
<li>
<p>Under <strong>Policies</strong> &gt; Access Policies &gt; select <strong>Create new policy</strong>.</p>
</li>
<li>
<p>Name your policy and define who will have access to your isolated application. Refer to the <a href="/cloudflare-one/access-controls/policies/#actions">Access policy documentation</a> to construct your policy.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
<li>
<p>Under <strong>Policies</strong> &gt; Access Policies &gt; select <strong>Select existing policies</strong> and select the policy or policies you created in the previous step &gt; select <strong>Confirm</strong>.</p>
</li>
<li>
<p>At the bottom of the page, select <strong>Save</strong>.</p>
</li>
</ol>
<p>Your application will now be served in an isolated browser for users matching your policies.</p>
<h3 id="open-links-in-browser-isolation">Open links in Browser Isolation</h3>
<p>To open links using Browser Isolation:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Browser isolation</strong> &gt; <strong>Browser isolation settings</strong>.</li>
<li>Turn on <strong>Allow users to open a remote browser without the device client</strong>.</li>
<li>In <strong>Launch browser</strong>, enter the URL link, and then select <strong>Launch</strong>. Your URL will open in a secure isolated browser.</li>
</ol>
<h2 id="filter-dns-queries">Filter DNS queries</h2>
<p>When users browse through Clientless Web Isolation, their DNS queries (the lookups that translate domain names to IP addresses) are handled by Gateway. You can use <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policies</a> to control which domains the remote browser can resolve. Enterprise users can resolve domains available only through private DNS servers by creating <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policies</a>.</p>
<p>Gateway DNS and resolver policies will always apply to Clientless Web Isolation traffic, regardless of device configuration.</p>
<h2 id="use-the-remote-browser">Use the remote browser</h2>
<p>Clientless Web Isolation is implemented through a prefixed URL — the target website's address is appended to a Cloudflare-hosted base URL. <code>&lt;your-team-name&gt;</code> is your organization's <span class="nb-glossary-tooltip" title="team name">team name</span>.</p>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/browser/&lt;URL&gt;&#10;</code></pre>
<p>For example, to isolate <code>www.example.com</code>, users would visit <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/browser/https://www.example.com/</code> in their preferred browser.</p>
<p>If <code>&lt;url&gt;</code> is not provided, users are presented with a Cloudflare Zero Trust landing page where they can input a target URL or search for a website.</p>
<h2 id="optional-configurations">Optional configurations</h2>
<h3 id="allow-or-block-websites">Allow or block websites</h3>
<p>When users visit a website through the <a href="#use-the-remote-browser">Clientless Web Isolation URL</a>, the traffic passes through Cloudflare Gateway. This allows you to <a href="/cloudflare-one/traffic-policies/http-policies/">apply HTTP policies</a> to control what websites the remote browser can connect to, even if the user's device does not have the Cloudflare One Client installed.</p>
<p>For example, if you use a third-party Secure Web Gateway to block <code>example.com</code>, users can still access the page in the remote browser by visiting <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/browser/https://www.example.com/</code>. To block <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/browser/https://www.example.com/</code>, create a Cloudflare Gateway HTTP policy to block <code>example.com</code>:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Domain</td>
<td>in</td>
<td><code>example.com</code></td>
<td>Block</td>
</tr>
</tbody>
</table>
<h3 id="bypass-tls-decryption">Bypass TLS decryption</h3>
<p><a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a> allows Gateway to inspect the contents of HTTPS traffic by decrypting it, applying policies, and re-encrypting it. If TLS decryption is turned on, Gateway will decrypt all sites accessed through the Clientless Web Isolation URL. Some sites are incompatible with this process (for example, sites that use certificate pinning). To connect to those sites, add a Do Not Inspect HTTP policy for the application or domain.</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Domain</td>
<td>is</td>
<td><code>mysite.com</code></td>
<td>Do Not Inspect</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5890.md")
</aside>
<h3 id="connect-private-networks">Connect private networks</h3>
<p>With Clientless Web Isolation, users can reach any internal web server you have connected through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>. For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/">Connect private networks</a>.</p>
<p>For example, if you added <code>192.168.2.1</code> to your tunnel, users can connect to your application through the remote browser by going to <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/browser/http://192.168.2.1</code>. Clientless Web Isolation also supports connecting over private ports, for example <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/browser/http://192.168.2.1:7148</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5889.md")
</aside>
<h3 id="disable-remote-browser-controls">Disable remote browser controls</h3>
<p>You can configure <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/#policy-settings">remote browser controls</a> such as disabling copy/paste, printing, or keyboard input. These settings display in the Gateway <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policy builder</a> when you select the Isolate action.</p>
<h3 id="sync-cookies-between-local-and-remote-browser">Sync cookies between local and remote browser</h3>
<p>The Cloudflare One Chrome extension allows a user to seamlessly access isolated and non-isolated applications without needing to re-authenticate. The user can log in once to their identity provider (whether through a Clientless Web Isolation link or their local browser) and gain access to all applications behind the SSO login.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5888.md")
</aside>
<h2 id="address-bar">Address bar</h2>
<p>Clientless Web Isolation has an embedded address bar. This feature is designed to improve the user's experience while visiting isolated pages with prefixed URLs.</p>
<p>The clientless address bar has three views: hostname notch, full address bar and hidden. The user's selected view is remembered across domains and remote browsing sessions.</p>
<h3 id="hostname-notch-view">Hostname notch view</h3>
<p>By default the isolated domain name appears in the notch positioned at the top and center of an isolated page.</p>
<p><img src="/assets/upstream/images/cloudflare-one/policies/rbi-address-bar-notch.png" alt="Viewing hostname of an isolated page in the clientless remote browser" /></p>
<p>Selecting <strong>Expand</strong> or the hostname text will expand the notch to the full address bar view. If isolated page content is obscured by the notch, expanding to the full address bar view will make the content accessible.</p>
<h3 id="full-address-bar-view">Full address bar view</h3>
<p>The full address bar allows users to search and go to isolated websites. Users can jump to the address bar at any time by pressing <code>CTRL + L</code> on the keyboard.</p>
<p><img src="/assets/upstream/images/cloudflare-one/policies/rbi-address-bar-full.png" alt="Viewing full address of an isolated page in the clientless remote browser" /></p>
<h3 id="hidden-view">Hidden view</h3>
<p>To turn on or off the address bar, users can right-click on any isolated page and select <strong>Show / Hide address bar</strong>.</p>
<h2 id="logs">Logs</h2>
<ul>
<li><strong>Authentication events</strong>: User login events are available in <a href="/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/">Access authentication logs</a>.</li>
<li><strong>HTTP requests</strong>: Traffic from the remote browser to the Internet is logged in <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway activity logs</a>.</li>
<li><strong>DNS queries</strong>: DNS queries from the remote browser are shown in <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway activity logs</a>.</li>
<li><strong>Network sessions</strong>: Egress traffic from the remote browser generates <a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust Network Session Logs</a>, available via <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a> and <a href="/log-explorer/">Log Explorer</a>.</li>
<li><strong>User actions</strong>: Track copy/paste, download/upload, and print actions initiated by users in the remote browser (only available in <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a>).</li>
</ul>
<h2 id="redirect-traffic-to-the-remote-browser">Redirect traffic to the remote browser</h2>
<p>If you want to isolate a website without the Cloudflare One Client installed, you will need to redirect traffic to the Clientless Web Isolation <a href="#use-the-remote-browser">prefixed URL</a>. One way to do this is through a third-party Secure Web Gateway. To redirect users to the remote browser, you can implement a custom block page similar to the example shown below.</p>
<pre tabindex="0"><code class="language-html">&lt;!DOCTYPE html&gt;&#10;&lt;html&gt;&#10;	&lt;head&gt;&#10;		&lt;title&gt;Redirecting website to a remote browser&lt;/title&gt;&#10;		&lt;script&gt;&#10;			window.location.href =&#10;				&quot;https://&lt;your-team-name&gt;.cloudflareaccess.com/browser/&lt;URL&gt;}&quot;;&#10;		&lt;/script&gt;&#10;		&lt;noscript&gt;&#10;			&lt;meta&#10;				http-equiv=&quot;refresh&quot;&#10;				content=&quot;0; url=https://&lt;your-team-name&gt;.cloudflareaccess.com/browser/&lt;URL&gt;&quot;&#10;			/&gt;&#10;		&lt;/noscript&gt;&#10;	&lt;/head&gt;&#10;	&lt;body&gt;&#10;		&lt;p&gt;&#10;			This website is being redirected to a remote browser. Select&#10;			&lt;a href=&quot;https://&lt;your-team-name&gt;.cloudflareaccess.com/browser/&lt;URL&gt;&quot;&#10;				&gt;here&lt;/a&#10;			&gt;&#10;			if you are not automatically redirected.&#10;		&lt;/p&gt;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>Review troubleshooting guidance related to Clientless Web Isolation.</p>
<ul>
<li><a href="/cloudflare-one/remote-browser-isolation/troubleshooting/#blank-screen-on-windows">Clientless Web Isolation is loading a blank screen on a Windows device</a></li>
</ul>
