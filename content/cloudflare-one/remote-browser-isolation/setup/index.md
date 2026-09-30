---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/
  description: Set up Browser Isolation in Browser Isolation.
  full_title: Set up Browser Isolation · Cloudflare One docs
  head_html: <title>Set up Browser Isolation · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up Browser Isolation in Browser Isolation."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/index.md"><meta property="og:title" content="Set up Browser Isolation · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up Browser Isolation in Browser Isolation."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/#page","headline":"Set up Browser Isolation \u00b7 Cloudflare One docs","description":"Set up Browser Isolation in Browser Isolation.","url":"https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/setup/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/remote-browser-isolation/setup/
  schema: 1
---
<p>Browser Isolation is enabled through <a href="/cloudflare-one/traffic-policies/http-policies/">Secure Web Gateway HTTP policies</a>. By default, no traffic is isolated until you have added an Isolate policy to your HTTP policies.</p>
<h2 id="1-connect-devices-to-cloudflare"><ol>
<li>Connect devices to Cloudflare</li>
</ol></h2>
<p>Setup instructions vary depending on how you want to connect your devices to Cloudflare. Refer to the links below to view the setup guide for each deployment option.</p>
<table>
<thead>
<tr>
<th>Connection</th>
<th>Mode</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-one/traffic-policies/get-started/http/">Traffic and DNS mode</a></td>
<td>In-line</td>
<td>Apply identity-based HTTP policies to traffic proxied through the Cloudflare One Client.</td>
</tr>
<tr>
<td><a href="/cloudflare-one/access-controls/policies/isolate-application/">Access</a></td>
<td>In-line</td>
<td>Apply identity-based HTTP policies to Access applications that are rendered in a remote browser.</td>
</tr>
<tr>
<td><a href="/cloudflare-one/remote-browser-isolation/setup/non-identity/">Gateway proxy endpoint (source IP)</a></td>
<td>In-line</td>
<td>Apply non-identity HTTP policies to traffic forwarded to a <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint">source IP proxy endpoint</a>.</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">Gateway proxy endpoint (authorization)</a></td>
<td>In-line</td>
<td>Apply identity-based HTTP policies to traffic forwarded to an <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">authorization proxy endpoint</a>.</td>
</tr>
<tr>
<td><a href="/cloudflare-one/remote-browser-isolation/setup/non-identity/">Cloudflare WAN</a></td>
<td>In-line</td>
<td>Apply non-identity HTTP policies to traffic connected through a GRE or IPsec tunnel (site-to-site encrypted connections to Cloudflare's network).</td>
</tr>
<tr>
<td><a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">Clientless remote browser</a></td>
<td>Prefixed URL</td>
<td>Render web pages in a remote browser when users go to <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/browser/&lt;URL&gt;</code>.</td>
</tr>
</tbody>
</table>
<p><strong>In-line</strong> mode means traffic is inspected as it flows through Gateway — users browse to websites using normal URLs, not a special Cloudflare prefix. Some in-line methods require device or network configuration, such as installing the Cloudflare One Client or configuring a PAC file. <strong>Prefixed URL</strong> mode requires users to visit a Cloudflare-hosted URL that wraps the target website.</p>
<h2 id="2-build-an-isolation-policy"><ol start="2">
<li>Build an Isolation policy</li>
</ol></h2>
<p>To configure Browser Isolation policies:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong> &gt; <strong>HTTP</strong>.</li>
<li>Select <strong>Add a policy</strong> and enter a name for the policy.</li>
<li>Use the HTTP policy <a href="/cloudflare-one/traffic-policies/http-policies/#selectors">selectors</a> and <a href="/cloudflare-one/traffic-policies/http-policies/#comparison-operators">operators</a> to specify the websites or content you want to isolate.</li>
<li>For <strong>Action</strong>, choose either <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/#isolate"><em>Isolate</em></a> or <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/#do-not-isolate"><em>Do not Isolate</em></a>.</li>
<li>(Optional) Configure <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/#policy-settings">settings</a> for an Isolate policy.</li>
<li>Select <strong>Create policy</strong>.</li>
</ol>
<p>Next, <a href="#3-check-if-a-web-page-is-isolated">verify that your policy is working</a>.</p>
<h2 id="3-check-if-a-web-page-is-isolated"><ol start="3">
<li>Check if a web page is isolated</li>
</ol></h2>
<p>Users can see if a webpage is isolated by using one of the following methods:</p>
<ul>
<li>Select the padlock in the address bar and check for the presence of a Cloudflare Root CA.</li>
<li>Right-click the web page and view the context menu options.</li>
</ul>
<h3 id="normal-browsing">Normal browsing</h3>
<ul>
<li>A non-Cloudflare root certificate indicates that Cloudflare did not proxy this web page. The root certificate is the certificate authority (CA) that your browser trusts to verify the site's identity.</li>
</ul>
<p><img src="/assets/upstream/images/cloudflare-one/rbi/non-cloudflare-root-ca.png" alt="Website does not present a Cloudflare root certificate" /></p>
<ul>
<li>The right-click context menu will have all of the normal options.</li>
</ul>
<p><img src="/assets/upstream/images/cloudflare-one/rbi/non-isolated-browser.png" alt="Normal right-click menu in browser" /></p>
<h3 id="isolated-browsing">Isolated browsing</h3>
<ul>
<li>A Cloudflare root certificate indicates traffic was proxied through Cloudflare Gateway.</li>
</ul>
<p><img src="/assets/upstream/images/cloudflare-one/rbi/cloudflare-gateway-root-ca.png" alt="Website presents a Cloudflare root certificate" /></p>
<ul>
<li>The right-click context menu will be simplified.</li>
</ul>
<p><img src="/assets/upstream/images/cloudflare-one/rbi/isolated-browser.png" alt="Simplified right-click menu in browser" /></p>
<h4 id="disconnect-browser-isolation">Disconnect Browser Isolation</h4>
<p>Cloudflare One Client users can temporarily disable remote browsing by <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#lock-device-client-switch">disconnecting the Cloudflare One Client</a>.
Once the Cloudflare One Client is disconnected, a refresh will return the non-isolated page.</p>
