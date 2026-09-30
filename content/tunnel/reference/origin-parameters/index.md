---
cp9:
  canonical: https://developers.cloudflare.com/tunnel/reference/origin-parameters/
  description: Parameters for configuring the connection between cloudflared and your origin.
  full_title: Origin parameters · Cloudflare Docs
  head_html: <title>Origin parameters · Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="Parameters for configuring the connection between cloudflared and your origin."><link rel="canonical" href="https://developers.cloudflare.com/tunnel/reference/origin-parameters/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/tunnel/reference/origin-parameters/index.md"><meta property="og:title" content="Origin parameters · Cloudflare Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Parameters for configuring the connection between cloudflared and your origin."><meta property="og:url" content="https://developers.cloudflare.com/tunnel/reference/origin-parameters/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Tunnel"><meta name="algolia_product_filter" content="Cloudflare Tunnel"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Tunnel"><meta name="pcx_tags" content="TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/tunnel/reference/origin-parameters/#page","headline":"Origin parameters \u00b7 Cloudflare Docs","description":"Parameters for configuring the connection between cloudflared and your origin.","url":"https://developers.cloudflare.com/tunnel/reference/origin-parameters/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS"]}</script>
  markdown: true
  noindex: false
  route: /tunnel/reference/origin-parameters/
  schema: 1
---
<p>Origin parameters determine how <code>cloudflared</code> sends requests to the origin server of your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">published application</a>.</p>
<h2 id="update-origin-parameters">Update origin parameters</h2>
<p>This section describes how to update origin parameters for a <span class="nb-glossary-tooltip" title="remotely-managed tunnel">remotely-managed tunnel</span>. If you are using a <span class="nb-glossary-tooltip" title="locally-managed tunnel">locally-managed tunnel</span>, add these parameters to your <a href="/tunnel/features/locally-managed-tunnels/configuration-file/">configuration file</a>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14884.md")
</div></div>
<h2 id="tls-settings">TLS settings</h2>
<h3 id="originservername">originServerName</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;&quot;</code></td>
<td>Origin Server Name</td>
</tr>
</tbody>
</table>
<p>Hostname that <code>cloudflared</code> should expect from your origin server certificate. If empty, <code>cloudflared</code> uses the hostname from the service URL, for example <code>localhost</code> if the service is <code>https://localhost:443</code>.</p>
<h3 id="matchsnitohost">matchSNItoHost</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>false</code></td>
<td>Match SNI to host</td>
</tr>
</tbody>
</table>
<p>When <code>true</code>, <code>cloudflared</code> sets the Server Name Indication (SNI) during the TLS handshake to the request <code>Host</code> value sent to the origin. If you configure <a href="#httphostheader">HTTP Host Header</a>, <code>cloudflared</code> uses that value for SNI. This setting overrides <a href="#originservername">Origin Server Name</a> for each request.</p>
<p>This setting is useful when directing traffic to entry points that host multiple services and rely on SNI to route requests or present the correct certificate. It eliminates the need to explicitly configure <a href="#originservername"><code>originServerName</code></a> for individual services when using wildcard routing.</p>
<h3 id="capool">caPool</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;&quot;</code></td>
<td>CA Pool</td>
</tr>
</tbody>
</table>
<p>Local file path to the certificate authority (CA) for your origin server certificate (for example, <code>/root/certs/ca.pem</code>). The path should point to a certificate store file or a bundle file in <code>.pem</code> or <code>.crt</code> format that contains one or more trusted root CA certificates. <code>cloudflared</code> adds these certificates to its default trust pool. Configure this setting when a private CA signs the certificate and the CA is not in the default trust pool.</p>
<h3 id="notlsverify">noTLSVerify</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>false</code></td>
<td>Disable TLS certificate verification</td>
</tr>
</tbody>
</table>
<p>When <code>false</code>, TLS verification is performed on the certificate presented by your origin.</p>
<p>When <code>true</code>, TLS verification is disabled. This will allow any certificate from the origin to be accepted.</p>
<h3 id="tlstimeout">tlsTimeout</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>10s</code></td>
<td>TLS Timeout</td>
</tr>
</tbody>
</table>
<p>Timeout for completing a TLS handshake to your origin server, if you have chosen to connect Tunnel to an HTTPS server.</p>
<h3 id="http2origin">http2Origin</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>false</code></td>
<td>Use HTTP/2 to origin</td>
</tr>
</tbody>
</table>
<p>When <code>false</code>, <code>cloudflared</code> will connect to your origin with HTTP/1.1.</p>
<p>When <code>true</code>, <code>cloudflared</code> attempts to connect to your origin server using HTTP/2 instead of HTTP/1.1. HTTP/2 to the origin requires HTTPS. For a certificate signed by a private CA, configure <a href="#capool">CA Pool</a> and keep TLS verification enabled.</p>
<h2 id="http-settings">HTTP settings</h2>
<h3 id="httphostheader">httpHostHeader</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;&quot;</code></td>
<td>HTTP Host Header</td>
</tr>
</tbody>
</table>
<p>Sets the HTTP <code>Host</code> header on requests sent to the local service.</p>
<h3 id="disablechunkedencoding">disableChunkedEncoding</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>false</code></td>
<td>Disable Chunked Encoding</td>
</tr>
</tbody>
</table>
<p>When <code>false</code>, <code>cloudflared</code> performs chunked transfer encoding when transferring data over HTTP/1.1.</p>
<p>When <code>true</code>, chunked transfer encoding is disabled. This is useful if you are running a Web Server Gateway Interface (WSGI) server.</p>
<h2 id="connection-settings">Connection settings</h2>
<h3 id="connecttimeout">connectTimeout</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>30s</code></td>
<td>Connect Timeout</td>
</tr>
</tbody>
</table>
<p>Timeout for establishing a new TCP connection to your origin server. This excludes the time taken to
establish TLS, which is controlled by tlsTimeout.</p>
<h3 id="nohappyeyeballs">noHappyEyeballs</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>false</code></td>
<td>No Happy Eyeballs</td>
</tr>
</tbody>
</table>
<p>When <code>false</code>, <code>cloudflared</code> uses the Happy Eyeballs algorithm for IPv4/IPv6 fallback if your local network has misconfigured one of the protocols.</p>
<p>When <code>true</code>, Happy Eyeballs is disabled.</p>
<h3 id="proxytype">proxyType</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;&quot;</code></td>
<td>Proxy Type</td>
</tr>
</tbody>
</table>
<p><code>cloudflared</code> starts a proxy server to translate HTTP traffic into TCP when proxying, for example, SSH or RDP.
This configures what type of proxy will be started. Valid options are:</p>
<ul>
<li><code>&quot;&quot;</code> for the regular proxy</li>
<li><code>&quot;socks&quot;</code> for a SOCKS5 proxy. Refer to the <a href="/cloudflare-one/tutorials/kubectl/">tutorial on connecting through Cloudflare Access using kubectl</a> for more information.</li>
</ul>
<h3 id="proxyaddress">proxyAddress</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14880.md")
</aside>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>127.0.0.1</code></td>
<td>--</td>
</tr>
</tbody>
</table>
<p><code>cloudflared</code> starts a proxy server to translate HTTP traffic into TCP when proxying, for example, SSH or RDP.
This configures the listen address for that proxy.</p>
<h3 id="proxyport">proxyPort</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14879.md")
</aside>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>0</code></td>
<td>--</td>
</tr>
</tbody>
</table>
<p><code>cloudflared</code> starts a proxy server to translate HTTP traffic into TCP when proxying, for example, SSH or RDP.
This configures the listen port for that proxy. If set to zero, an unused port will randomly be chosen.</p>
<h3 id="keepalivetimeout">keepAliveTimeout</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1m30s</code></td>
<td>Idle Connection Expiration Time</td>
</tr>
</tbody>
</table>
<p>Timeout after which an idle keepalive connection can be discarded.</p>
<h3 id="keepaliveconnections">keepAliveConnections</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>100</code></td>
<td>Keep Alive Connections</td>
</tr>
</tbody>
</table>
<p>Default: <code>100</code></p>
<p>Maximum number of idle keepalive connections between <code>cloudflared</code> and your origin. This does not restrict the total number of concurrent connections.</p>
<h3 id="tcpkeepalive">tcpKeepAlive</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>30s</code></td>
<td>TCP Keep Alive Interval</td>
</tr>
</tbody>
</table>
<p>Default: <code>30s</code></p>
<p>The timeout after which <code>cloudflared</code> sends a TCP keepalive packet to the origin server.</p>
<h2 id="access-settings">Access settings</h2>
<h3 id="access">access</h3>
<table>
<thead>
<tr>
<th>Default</th>
<th>UI name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;&quot;</code></td>
<td>Protect with Access</td>
</tr>
</tbody>
</table>
<p>Requires <code>cloudflared</code> to validate the <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/">Cloudflare Access JWT</a> prior to proxying traffic to your origin. You can enforce this check on public hostname services that are protected by an Access application. For all L7 requests to these hostnames, Access will send the JWT to <code>cloudflared</code> as a <code>Cf-Access-Jwt-Assertion</code> request header.</p>
<p>To enable this security control in a <a href="/tunnel/features/locally-managed-tunnels/configuration-file/">configuration file</a>, <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/#get-your-aud-tag">get the AUD tag</a> for your Access application and add the following rule to <code>originRequest</code>:</p>
<pre tabindex="0"><code class="language-yml">access:&#10;  required: true&#10;  teamName: &lt;your-team-name&gt;&#10;  audTag:&#10;    &#45; &lt;Access-application-audience-tag&gt;&#10;    &#45; &lt;Optional-additional-tags&gt;&#10;</code></pre>
