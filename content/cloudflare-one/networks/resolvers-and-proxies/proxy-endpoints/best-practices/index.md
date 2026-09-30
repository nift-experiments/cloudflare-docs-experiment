---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/best-practices/
  description: PAC file best practices in Zero Trust networking.
  full_title: PAC file best practices · Cloudflare One docs
  head_html: <title>PAC file best practices · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="PAC file best practices in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/best-practices/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/best-practices/index.md"><meta property="og:title" content="PAC file best practices · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="PAC file best practices in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/best-practices/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="JavaScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/best-practices/#page","headline":"PAC file best practices \u00b7 Cloudflare One docs","description":"PAC file best practices in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/best-practices/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/best-practices/
  schema: 1
---
<p>A PAC file is a text file that specifies which traffic should redirect to the proxy server. When a browser makes a web request, it consults the PAC file's <code>FindProxyForURL()</code> function, which evaluates the request and returns routing instructions, such as a direct connection, proxy server, or failover sequence.</p>
<h2 id="pac-file-format">PAC file format</h2>
<p>The default Cloudflare PAC file follows a standard format:</p>
<pre tabindex="0"><code class="language-js">function FindProxyForURL(url, host) {&#10;	// No proxy for private (RFC 1918) IP addresses (intranet sites)&#10;	if (&#10;		isInNet(dnsResolve(host), &quot;10.0.0.0&quot;, &quot;255.0.0.0&quot;) ||&#10;		isInNet(dnsResolve(host), &quot;172.16.0.0&quot;, &quot;255.240.0.0&quot;) ||&#10;		isInNet(dnsResolve(host), &quot;192.168.0.0&quot;, &quot;255.255.0.0&quot;)&#10;	) {&#10;		return &quot;DIRECT&quot;;&#10;	}&#10;&#10;	// No proxy for localhost&#10;	if (isInNet(dnsResolve(host), &quot;127.0.0.0&quot;, &quot;255.0.0.0&quot;)) {&#10;		return &quot;DIRECT&quot;;&#10;	}&#10;&#10;	// Proxy all&#10;	return &quot;HTTPS 3ele0ss56t.proxy.cloudflare-gateway.com:443&quot;;&#10;}&#10;</code></pre>
<p>You can <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Proxy_servers_and_tunneling/Proxy_Auto-Configuration_PAC_file">customize the PAC file</a> and host it somewhere your browser can access.</p>
<h3 id="formatting-considerations">Formatting considerations</h3>
<ul>
<li>Make sure the directive used for the endpoint is <code>HTTPS</code> and not <code>PROXY</code>. For example:
<ul>
<li>Correct: <code>return &quot;HTTPS your-subdomain.proxy.cloudflare-gateway.com:443&quot;;</code></li>
<li>Incorrect: <code>return &quot;PROXY your-subdomain.proxy.cloudflare-gateway.com:443&quot;;</code></li>
</ul>
</li>
<li>You must use a PAC file instead of configuring the endpoint directly in the proxy configuration of the browser. Modern browsers do not support HTTPS proxies without PAC files.</li>
<li>Use a plain text editor such as VS Code to avoid extra characters.</li>
<li>If you are using PAC files for public Internet browsing (instead of only internal services), refer to <a href="#common-bypass-rules">Common bypass rules</a> for domains you may need to exclude from the proxy to prevent website functionality issues.</li>
</ul>
<h2 id="pac-file-template-with-identity-provider-bypass">PAC file template with identity provider bypass</h2>
<p>When using <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">authorization endpoints</a>, you must bypass your identity provider (IdP) domains in the PAC file. This prevents authentication loops where the browser tries to authenticate with the proxy before it can reach the IdP to authenticate.</p>
<p>The following example PAC file is a comprehensive template that includes common IdP bypass rules. Replace the placeholder values with your configuration:</p>
<pre tabindex="0"><code class="language-js">function FindProxyForURL(url, host) {&#10;	// *** Identity Provider Bypass ***&#10;	// CRITICAL: Bypass your IdP to prevent authentication loops&#10;	// Uncomment and configure the section for your IdP:&#10;&#10;	// Okta&#10;	// if (host === &quot;your-domain.okta.com&quot; || shExpMatch(host, &quot;*.oktacdn.com&quot;)) {&#10;	// 	return &quot;DIRECT&quot;;&#10;	// }&#10;&#10;	// Microsoft Entra ID (Azure AD)&#10;	// if (&#10;	// 	host === &quot;login.microsoftonline.com&quot; ||&#10;	// 	host === &quot;aadcdn.msauth.net&quot; ||&#10;	// 	host === &quot;aadcdn.msftauth.net&quot;&#10;	// ) {&#10;	// 	return &quot;DIRECT&quot;;&#10;	// }&#10;&#10;	// Google Workspace&#10;	// if (&#10;	// 	host === &quot;accounts.google.com&quot; ||&#10;	// 	shExpMatch(host, &quot;*.gstatic.com&quot;)&#10;	// ) {&#10;	// 	return &quot;DIRECT&quot;;&#10;	// }&#10;&#10;	// GitHub&#10;	// if (shExpMatch(host, &quot;*.github.com&quot;)) {&#10;	// 	return &quot;DIRECT&quot;;&#10;	// }&#10;&#10;	// *** Private Networks ***&#10;	// Bypass private RFC 1918 IP addresses&#10;	if (&#10;		isInNet(dnsResolve(host), &quot;10.0.0.0&quot;, &quot;255.0.0.0&quot;) ||&#10;		isInNet(dnsResolve(host), &quot;172.16.0.0&quot;, &quot;255.240.0.0&quot;) ||&#10;		isInNet(dnsResolve(host), &quot;192.168.0.0&quot;, &quot;255.255.0.0&quot;)&#10;	) {&#10;		return &quot;DIRECT&quot;;&#10;	}&#10;&#10;	// Bypass localhost&#10;	if (isInNet(dnsResolve(host), &quot;127.0.0.0&quot;, &quot;255.0.0.0&quot;)) {&#10;		return &quot;DIRECT&quot;;&#10;	}&#10;&#10;	// Bypass plain hostnames (no dots)&#10;	if (isPlainHostName(host)) {&#10;		return &quot;DIRECT&quot;;&#10;	}&#10;&#10;	// Bypass .local domains&#10;	if (shExpMatch(host, &quot;*.local&quot;)) {&#10;		return &quot;DIRECT&quot;;&#10;	}&#10;&#10;	// *** Cloudflare Access Logout ***&#10;	// Optional: Redirect logout requests to your Access logout page&#10;	// if (shExpMatch(url, &quot;*logout*&quot;)) {&#10;	// 	return &quot;HTTPS your-team-name.cloudflareaccess.com/cdn-cgi/access/logout&quot;;&#10;	// }&#10;&#10;	// *** Proxy all other traffic ***&#10;	return &quot;HTTPS your-subdomain.proxy.cloudflare-gateway.com:443&quot;;&#10;}&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="idp-bypass-requirement">IdP bypass requirement</h3>
@markup("md", "content/.markup/bodies/5863.md")
</aside>
<h2 id="performance-optimization">Performance optimization</h2>
<p>Browsers evaluate PAC files for every request. Optimizing PAC file performance is critical to avoid delays and issues in web browsing for your users.</p>
<h3 id="cache-dns-results-in-variables">Cache DNS results in variables</h3>
<p>When performing DNS resolution with <code>dnsResolve()</code>, store the result in a variable to reuse it across multiple checks. This avoids redundant DNS lookups:</p>
<pre tabindex="0"><code class="language-js">function FindProxyForURL(url, host) {&#10;	// Resolve once and reuse&#10;	var hostIP = dnsResolve(host);&#10;&#10;	if (isInNet(hostIP, &quot;10.0.0.0&quot;, &quot;255.0.0.0&quot;)) {&#10;		return &quot;DIRECT&quot;;&#10;	}&#10;&#10;	// Reuse hostIP for additional checks&#10;	if (isInNet(hostIP, &quot;172.16.0.0&quot;, &quot;255.240.0.0&quot;)) {&#10;		return &quot;DIRECT&quot;;&#10;	}&#10;&#10;	return &quot;HTTPS proxy.example.com:443&quot;;&#10;}&#10;</code></pre>
<h3 id="check-for-plain-hostnames-first">Check for plain hostnames first</h3>
<p>NetBIOS names (hostnames without periods) are typically internal and should bypass the proxy. Check for these first:</p>
<pre tabindex="0"><code class="language-js">if (isPlainHostName(host)) return &quot;DIRECT&quot;;&#10;</code></pre>
<h2 id="advanced-techniques">Advanced techniques</h2>
<h3 id="case-sensitivity-handling">Case sensitivity handling</h3>
<p>JavaScript is case-sensitive. Convert hostnames to lowercase for consistent matching:</p>
<pre tabindex="0"><code class="language-js">function FindProxyForURL(url, host) {&#10;	// Normalize to lowercase&#10;	host = host.toLowerCase();&#10;	url = url.toLowerCase();&#10;&#10;	if (shExpMatch(host, &quot;*.example.com&quot;)) {&#10;		return &quot;DIRECT&quot;;&#10;	}&#10;&#10;	return &quot;HTTPS proxy.cloudflare-gateway.com:443&quot;;&#10;}&#10;</code></pre>
<h2 id="common-bypass-rules">Common bypass rules</h2>
<p>When using PAC files for public Internet browsing (not just internal services), you may need to bypass the proxy for certain domains to prevent website functionality issues. The following are common scenarios where your proxy may interfere with traffic.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="optional-rules">Optional rules</h3>
@markup("md", "content/.markup/bodies/5862.md")
</aside>
<h3 id="font-and-static-asset-providers">Font and static asset providers</h3>
<p>Font APIs and static asset providers should typically bypass the proxy to prevent rendering issues:</p>
<pre tabindex="0"><code class="language-js">// Bypass font providers&#10;if (&#10;	shExpMatch(host, &quot;*.googleapis.com&quot;) ||&#10;	shExpMatch(host, &quot;*.gstatic.com&quot;) ||&#10;	shExpMatch(host, &quot;fonts.adobe.com&quot;)&#10;) {&#10;	return &quot;DIRECT&quot;;&#10;}&#10;</code></pre>
<h3 id="streaming-and-media-services">Streaming and media services</h3>
<p>Video streaming and large media downloads may perform better with direct connections:</p>
<pre tabindex="0"><code class="language-js">// Bypass streaming services&#10;if (&#10;	shExpMatch(host, &quot;*.netflix.com&quot;) ||&#10;	shExpMatch(host, &quot;*.youtube.com&quot;) ||&#10;	shExpMatch(host, &quot;*.googlevideo.com&quot;)&#10;) {&#10;	return &quot;DIRECT&quot;;&#10;}&#10;</code></pre>
<h3 id="apps-with-certificate-pinning">Apps with certificate pinning</h3>
<p>When HTTPS inspection is enabled, applications and services that use certificate pinning reject the Cloudflare-injected certificate and fail to load when routed through the proxy. Bypass these domains in your PAC file:</p>
<pre tabindex="0"><code class="language-js">// Bypass certificate-pinned apps&#10;if (&#10;	shExpMatch(host, &quot;*.example-bank.com&quot;) ||&#10;	shExpMatch(host, &quot;*.example-pinned-app.com&quot;)&#10;) {&#10;	return &quot;DIRECT&quot;;&#10;}&#10;</code></pre>
<p><a href="/cloudflare-one/traffic-policies/http-policies/#do-not-inspect">Do Not Inspect (DNI) policies</a> will not prevent certificate pinning errors on these connections — bypassing certificate-pinned apps in the PAC file is required.</p>
<h2 id="test-pac-files">Test PAC files</h2>
<h3 id="test-with-expected-websites">Test with expected websites</h3>
<p>Before deploying your PAC file to all users in your organization, test it with the websites and applications your users commonly access. This helps ensure:</p>
<ul>
<li>Internal resources are accessible and not incorrectly routed through the proxy</li>
<li>External websites are properly filtered through Gateway</li>
<li>Performance is acceptable for typical usage patterns</li>
</ul>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/5861.md")
</aside>
<h3 id="validate-syntax">Validate syntax</h3>
<p>PAC files use JavaScript syntax. A single syntax error (such as a missing closing parenthesis <code>)</code> or bracket <code>]</code>) will cause the entire PAC file to fail. Use a JavaScript-aware text editor to find and fix syntax errors before deployment.</p>
<h2 id="troubleshoot-configurations">Troubleshoot configurations</h2>
<h3 id="debug-pac-file-routing-decisions">Debug PAC file routing decisions</h3>
<p>If you have an issue with proxy routing, most browsers provide debugging tools to verify PAC file behavior:</p>
<details class="nb-details"><summary>Chromium-based browsers (Chrome, Edge, Brave)</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5864.md")
</div></details>
<details class="nb-details"><summary>Firefox</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5865.md")
</div></details>
<details class="nb-details"><summary>Safari</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5866.md")
</div></details>
<h3 id="browsing-on-a-device-using-a-pac-file-is-slow">Browsing on a device using a PAC file is slow</h3>
<p>Excessive DNS lookups in the PAC file can cause delays. Review your PAC file and minimize the use of <code>dnsResolve()</code>, <code>isInNet()</code>, and <code>isResolvable()</code> functions.</p>
<h3 id="browser-caches-pac-files-incorrectly">Browser caches PAC files incorrectly</h3>
<p>When you update a PAC file, browsers may continue to use a cached version, causing unexpected behavior. Clear your browser cache and restart the browser after updating the PAC file to ensure the browser uses the latest version.</p>
