---
cp9:
  canonical: https://developers.cloudflare.com/workers-vpc/configuration/vpc-services/
  description: Register private network resources as VPC Services that Workers can access through Cloudflare Tunnel.
  full_title: VPC Services · Cloudflare Workers VPC
  head_html: <title>VPC Services · Cloudflare Workers VPC</title><meta name="generator" content="Nift"><meta name="description" content="Register private network resources as VPC Services that Workers can access through Cloudflare Tunnel."><link rel="canonical" href="https://developers.cloudflare.com/workers-vpc/configuration/vpc-services/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-vpc/configuration/vpc-services/index.md"><meta property="og:title" content="VPC Services · Cloudflare Workers VPC"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Register private network resources as VPC Services that Workers can access through Cloudflare Tunnel."><meta property="og:url" content="https://developers.cloudflare.com/workers-vpc/configuration/vpc-services/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers VPC"><meta name="algolia_product_filter" content="Workers VPC"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers VPC"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-vpc/configuration/vpc-services/#page","headline":"VPC Services \u00b7 Cloudflare Workers VPC","description":"Register private network resources as VPC Services that Workers can access through Cloudflare Tunnel.","url":"https://developers.cloudflare.com/workers-vpc/configuration/vpc-services/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-vpc/configuration/vpc-services/
  schema: 1
---
<p>VPC Services are the core building block of Workers VPC. They represent specific resources in your private network that Workers can access through Cloudflare Tunnel.</p>
<p>You can use bindings to connect to VPC Services from Workers. Every request made to a VPC Service using its <code>fetch</code> function will be securely routed to the configured service in the private network.</p>
<p>VPC Services enforce that requests are routed to their intended service without exposing the entire network, securing your workloads and preventing server-side request forgery (SSRF).</p>
<p>Members with the <strong>Connectivity Directory Bind</strong> role can bind to existing VPC Services from Workers. Creating VPC Services requires the <strong>Connectivity Directory Admin</strong> role.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15890.md")
</aside>
<h2 id="vpc-service-configuration">VPC Service configuration</h2>
<p>A VPC Service consists of:</p>
<ul>
<li><strong>Type</strong>: <code>http</code> for HTTP/HTTPS services, or <code>tcp</code> for TCP services (for example, PostgreSQL, MySQL)</li>
<li><strong>Tunnel ID</strong>: The Cloudflare Tunnel that provides network connectivity</li>
<li><strong>Hostname or IPv4/IPv6 addresses</strong>: The hostname, or IPv4 and/or IPv6 addresses to use to route to your service from the tunnel in your private network</li>
<li><strong>Ports</strong>: For <code>http</code> type, HTTP and/or HTTPS port configuration (optional, defaults to 80/443). For <code>tcp</code> type, a TCP port (required).</li>
<li><strong>Application protocol</strong> (TCP only): Optionally, specify <code>postgresql</code> or <code>mysql</code> to indicate the application-layer protocol for the TCP service</li>
<li><strong>TLS certificate verification mode</strong>: Optionally, configure how the connection to the origin verifies TLS certificates</li>
<li><strong>Resolver IPs</strong>: Optionally, a specific resolver IP can be provided — when not provided, <code>cloudflared</code> will direct DNS traffic to the currently configured default system resolver.</li>
</ul>
<h3 id="http-services">HTTP services</h3>
<p>HTTP VPC Services allow Workers to make <code>fetch()</code> requests to private HTTP/HTTPS endpoints.</p>
<p>Requests are encrypted in flight until they reach your network via a tunnel, regardless of the scheme used in the URL provided to <code>fetch</code>. If the <code>http</code> scheme is used, a plaintext connection is established to the service from the tunnel.</p>
<p>The <code>https</code> scheme can be used for an encrypted connection within your network, between the tunnel and your service. When the <code>https</code> scheme is specified, a hostname provided to the <code>fetch()</code> operation is utilized as the Server Name Indication (SNI) value.</p>
<p>VPC Services default to allowing both <code>http</code> and <code>https</code> schemes to be used. You can provide values for only one of <code>http_port</code> or <code>https_port</code> to enforce the use of a particular scheme.</p>
<p>When Workers VPC is unable to establish a connection to your service, <code>fetch()</code> will throw an exception.</p>
<h3 id="tcp-services">TCP services</h3>
<p>TCP VPC Services allow connections to TCP-based services such as PostgreSQL and MySQL databases. Use the <code>tcp</code> service type with a <code>--tcp-port</code> to expose a TCP service.</p>
<p>You can optionally specify an <code>--app-protocol</code> of <code>postgresql</code> or <code>mysql</code> to indicate the application-layer protocol. This metadata is used by other Cloudflare products, such as <a href="/hyperdrive/">Hyperdrive</a>, to locate TCP services using a supported wire protocol.</p>
<p>TCP VPC Services are used with <a href="/hyperdrive/">Hyperdrive</a> to connect Workers to private databases. Refer to <a href="/hyperdrive/configuration/connect-to-private-database-vpc/">Connect to a private database using Workers VPC</a> for a complete guide.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15889.md")
</aside>
<h3 id="supported-tls-certificates">Supported TLS certificates</h3>
<p>When using the <code>https</code> scheme, the tunnel verifies the TLS certificate presented by your origin service. Workers VPC trusts the following certificate types:</p>
<ul>
<li><strong>Publicly trusted certificates</strong> — Certificates issued by well-known public certificate authorities (for example, Let's Encrypt, DigiCert).</li>
<li><strong><a href="/ssl/origin-configuration/origin-ca/">Cloudflare Origin CA certificates</a></strong> — Free certificates issued by Cloudflare that encrypt traffic between Cloudflare and your origin. Origin CA certificates are not trusted by browsers, but are trusted by Workers VPC when connecting to your private services.</li>
</ul>
<p>If your origin service presents a certificate that is not issued by a publicly trusted CA or by Cloudflare Origin CA, the TLS handshake will fail and <code>fetch()</code> will throw an exception.</p>
<h3 id="tls-certificate-verification-mode">TLS certificate verification mode</h3>
<p>You can configure how the connection to your origin service verifies TLS certificates by setting the <code>--cert-verification-mode</code> option when creating or updating a VPC Service. This applies to both HTTP and TCP service types.</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>verify_full</code></td>
<td>Verify the full certificate chain and hostname (default)</td>
</tr>
<tr>
<td><code>verify_ca</code></td>
<td>Verify the certificate chain only, skip hostname verification</td>
</tr>
<tr>
<td><code>disabled</code></td>
<td>Do not verify the server certificate</td>
</tr>
</tbody>
</table>
<h2 id="configuration-examples">Configuration examples</h2>
<p>These configurations represent the expected contract of the <a href="/api/resources/connectivity/subresources/directory/subresources/services/">REST API for creating a VPC Service</a>, a type of service within the broader connectivity directory.</p>
<h3 id="http-service-with-ip-addresses">HTTP service with IP addresses</h3>
<p>The following is an example of an HTTP VPC Service using custom HTTP and HTTPS ports, and both IPv4 and IPv6 addresses.</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;type&quot;: &quot;http&quot;,&#10;	&quot;name&quot;: &quot;human-readable-name&quot;,&#10;&#10;	// Port configuration (optional - defaults to 80/443)&#10;	&quot;http_port&quot;: 80,&#10;	&quot;https_port&quot;: 443,&#10;&#10;	// Host configuration&#10;	&quot;host&quot;: {&#10;		&quot;ipv4&quot;: &quot;10.0.0.1&quot;,&#10;		&quot;ipv6&quot;: &quot;fe80::&quot;,&#10;		&quot;network&quot;: {&#10;			&quot;tunnel_id&quot;: &quot;0191dce4-9ab4-7fce-b660-8e5dec5172da&quot;,&#10;		},&#10;	},&#10;}&#10;</code></pre>
<h3 id="http-service-with-hostname">HTTP service with hostname</h3>
<p>The following is an example of an HTTP VPC Service using a hostname. When using a hostname, provide a <code>resolver_network</code> that optionally includes <code>resolver_ips</code>.</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;type&quot;: &quot;http&quot;,&#10;	&quot;name&quot;: &quot;human-readable-name&quot;,&#10;&#10;	// Port configuration (optional - defaults to 80/443)&#10;	&quot;http_port&quot;: 80,&#10;	&quot;https_port&quot;: 443,&#10;&#10;	// Hostname Host (with DNS resolver)&#10;	&quot;host&quot;: {&#10;		&quot;hostname&quot;: &quot;example.com&quot;,&#10;		&quot;resolver_network&quot;: {&#10;			&quot;tunnel_id&quot;: &quot;0191dce4-9ab4-7fce-b660-8e5dec5172da&quot;,&#10;			&quot;resolver_ips&quot;: [&quot;10.0.0.1&quot;], // Optional&#10;		},&#10;	},&#10;}&#10;</code></pre>
<h3 id="tcp-service-for-example-postgresql">TCP service (for example, PostgreSQL)</h3>
<p>The following is an example of a TCP VPC Service for a PostgreSQL database.</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;type&quot;: &quot;tcp&quot;,&#10;	&quot;name&quot;: &quot;my-postgres-db&quot;,&#10;	&quot;tcp_port&quot;: 5432,&#10;	&quot;app_protocol&quot;: &quot;postgresql&quot;, // Optional: &quot;postgresql&quot; or &quot;mysql&quot;&#10;&#10;	&quot;host&quot;: {&#10;		&quot;ipv4&quot;: &quot;10.0.0.5&quot;,&#10;		&quot;network&quot;: {&#10;			&quot;tunnel_id&quot;: &quot;0191dce4-9ab4-7fce-b660-8e5dec5172da&quot;,&#10;		},&#10;	},&#10;}&#10;</code></pre>
<h3 id="service-with-tls-certificate-verification">Service with TLS certificate verification</h3>
<p>The following example creates a TCP service with <code>verify_ca</code> certificate verification mode.</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;type&quot;: &quot;tcp&quot;,&#10;	&quot;name&quot;: &quot;my-postgres-db&quot;,&#10;	&quot;tcp_port&quot;: 5432,&#10;	&quot;app_protocol&quot;: &quot;postgresql&quot;,&#10;&#10;	&quot;host&quot;: {&#10;		&quot;ipv4&quot;: &quot;10.0.0.5&quot;,&#10;		&quot;network&quot;: {&#10;			&quot;tunnel_id&quot;: &quot;0191dce4-9ab4-7fce-b660-8e5dec5172da&quot;,&#10;		},&#10;	},&#10;&#10;	&quot;tls_settings&quot;: {&#10;		&quot;cert_verification_mode&quot;: &quot;verify_ca&quot;,&#10;	},&#10;}&#10;</code></pre>
<h2 id="workers-binding-configuration">Workers binding configuration</h2>
<p>Once you have created a VPC Service, you can bind it to your Worker:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15891.md")
</div>
<p>You can have multiple VPC service bindings:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15892.md")
</div>
<h2 id="required-roles">Required roles</h2>
<p>Workers VPC uses the following account roles:</p>
<ul>
<li><code>Connectivity Directory Read</code> to view Workers VPC Services and Tunnels.</li>
<li><code>Connectivity Directory Bind</code> to list, read, and bind VPC Services in Workers.</li>
<li><code>Connectivity Directory Admin</code> to create, update, and delete VPC Services, and bind directly to tunnels through a VPC Network binding.</li>
</ul>
<p>For role definitions, refer to <a href="/fundamentals/manage-members/roles/#account-scoped-roles">Roles</a>.</p>
<p>If your roles were recently updated and commands are still failing, refresh Wrangler authentication:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler logout&#10;npx wrangler login&#10;</code></pre>
<p>If you authenticate with an API token (<code>CLOUDFLARE_API_TOKEN</code>), ensure the token belongs to a user with the required roles.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/workers-vpc/configuration/vpc-services/terraform/">Configure VPC Services with Terraform</a> for managing VPC Services as infrastructure</li>
<li>Set up <a href="/workers-vpc/configuration/tunnel/">Cloudflare Tunnel</a> for your environment</li>
<li>Learn about the <a href="/workers-vpc/api/">Service Binding API</a></li>
<li>Refer to <a href="/workers-vpc/examples/">examples</a> of common use cases</li>
</ul>
