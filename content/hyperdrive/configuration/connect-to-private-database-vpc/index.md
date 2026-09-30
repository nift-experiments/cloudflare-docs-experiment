---
cp9:
  canonical: https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database-vpc/
  description: Workers VPC provides a way to connect Hyperdrive to a private database without configuring Cloudflare Access applications or service tokens. Instead, you create a TCP VPC Service that points to your database and pass its service ID to Hyperdrive.
  full_title: Connect to a private database using Workers VPC (Recommended) · Cloudflare Hyperdrive docs
  head_html: <title>Connect to a private database using Workers VPC (Recommended) · Cloudflare Hyperdrive docs</title><meta name="generator" content="Nift"><meta name="description" content="Workers VPC provides a way to connect Hyperdrive to a private database without configuring Cloudflare Access applications or service tokens. Instead, you create a TCP VPC Service that points to your database and pass its service ID to Hyperdrive."><link rel="canonical" href="https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database-vpc/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database-vpc/index.md"><meta property="og:title" content="Connect to a private database using Workers VPC (Recommended) · Cloudflare Hyperdrive docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Workers VPC provides a way to connect Hyperdrive to a private database without configuring Cloudflare Access applications or service tokens. Instead, you create a TCP VPC Service that points to your database and pass its service ID to Hyperdrive."><meta property="og:url" content="https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database-vpc/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Hyperdrive"><meta name="algolia_product_filter" content="Hyperdrive"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database-vpc/#page","headline":"Connect to a private database using Workers VPC (Recommended) \u00b7 Cloudflare Hyperdrive docs","description":"Workers VPC provides a way to connect Hyperdrive to a private database without configuring Cloudflare Access applications or service tokens. Instead, you create a TCP VPC Service that points to your database and pass its service ID to Hyperdrive.","url":"https://developers.cloudflare.com/hyperdrive/configuration/connect-to-private-database-vpc/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /hyperdrive/configuration/connect-to-private-database-vpc/
  schema: 1
---
<p><a href="/workers-vpc/">Workers VPC</a> provides a way to connect Hyperdrive to a private database without configuring Cloudflare Access applications or service tokens. Instead, you create a TCP <a href="/workers-vpc/configuration/vpc-services/">VPC Service</a> that points to your database and pass its service ID to Hyperdrive.</p>
<p>For the Tunnel and Access approach, refer to <a href="/hyperdrive/configuration/connect-to-private-database/">Connect to a private database using Tunnel</a>.</p>
<h2 id="how-it-works">How it works</h2>
<p>When your database is isolated within a private network (such as a <a href="https://www.cloudflare.com/learning/cloud/what-is-a-virtual-private-cloud">virtual private cloud</a> or an on-premise network), you must enable a secure connection from your network to Cloudflare.</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> is used to establish a secure outbound connection from your private network to Cloudflare.</li>
<li>A <a href="/workers-vpc/configuration/vpc-services/">VPC Service</a> is used to route traffic from your Worker through the tunnel to your database, without requiring Cloudflare Access applications or service tokens.</li>
</ul>
<p>A request from the Cloudflare Worker to the origin database goes through Hyperdrive, the VPC Service, and the Cloudflare Tunnel established by <code>cloudflared</code>. <code>cloudflared</code> must be running in the private network in which your database is accessible.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;    A[Cloudflare Worker] --&gt; B[Hyperdrive] --&gt; C[VPC Service] --&gt; D[Cloudflare Tunnel] --&gt; E[Private Database]&#10;</code></pre>
<h2 id="before-you-start">Before you start</h2>
<p>All of the tutorials assume you have already completed the <a href="/workers/get-started/guide/">Get started guide</a>, which gets you set up with a Cloudflare Workers account, <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a>, and <a href="/workers/wrangler/install-and-update/">Wrangler</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A database in your private network, <a href="/hyperdrive/examples/connect-to-postgres/#supported-tls-ssl-modes">configured to use TLS/SSL</a>.</li>
<li>A <a href="/workers-vpc/configuration/tunnel/">Cloudflare Tunnel</a> running in a network that can reach your database.</li>
<li>The <strong>Connectivity Directory Admin</strong> role on your Cloudflare account to create VPC Services.</li>
</ul>
<h2 id="1-set-up-a-cloudflare-tunnel"><ol>
<li>Set up a Cloudflare Tunnel</li>
</ol></h2>
<p>If you do not already have a tunnel running in the same network as your database, create one.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/9081.md")
</div>
<p>The tunnel must be able to reach your database host and port from within the private network.</p>
<p>For full tunnel documentation, refer to <a href="/workers-vpc/configuration/tunnel/">Cloudflare Tunnel for Workers VPC</a>.</p>
<h2 id="2-create-a-tcp-vpc-service"><ol start="2">
<li>Create a TCP VPC Service</li>
</ol></h2>
<p>Create a VPC Service of type <code>tcp</code> that points to your database. Set the <code>--app-protocol</code> flag to <code>postgresql</code> or <code>mysql</code> so that Hyperdrive can optimize connections.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9084.md")
</div></div>
<p>Replace:</p>
<ul>
<li><code>&lt;YOUR_TUNNEL_ID&gt;</code> with the tunnel ID from step 1.</li>
<li><code>&lt;YOUR_DATABASE_IP&gt;</code> with the private IP address of your database (for example, <code>10.0.0.5</code>). You can also use <code>--hostname</code> with a DNS name instead of <code>--ipv4</code>.</li>
</ul>
<p>The command will return a service ID. Save this value for the next step.</p>
<p>You can also create a TCP VPC Service from the <a href="https://dash.cloudflare.com/?to=/:account/workers/vpc">Workers VPC dashboard</a>. Refer to <a href="/workers-vpc/configuration/vpc-services/">VPC Services</a> for all configuration options.</p>
<h3 id="tls-certificate-verification">TLS certificate verification</h3>
<p>Unlike Hyperdrive, which does not verify the origin server certificate by default, Workers VPC defaults to <code>verify_full</code> — it verifies both the certificate chain and the hostname. If your database uses a self-signed certificate or a certificate from a private certificate authority (CA), the TLS handshake will fail unless you adjust the verification mode.</p>
<p>For databases with self-signed certificates, add <code>--cert-verification-mode</code> when creating the VPC Service:</p>
<ul>
<li><code>verify_ca</code> — Verifies the certificate chain but skips hostname verification. Use this when your database has a certificate signed by a CA you control but the hostname does not match the certificate.</li>
<li><code>disabled</code> — Skips certificate verification entirely. Use this only for development or testing.</li>
</ul>
<p>For example, to create a VPC Service for a PostgreSQL database with a self-signed certificate:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler vpc service create my-postgres-db \&#10;  &#45;-type tcp \&#10;  &#45;-tcp-port 5432 \&#10;  &#45;-app-protocol postgresql \&#10;  &#45;-tunnel-id &lt;YOUR_TUNNEL_ID&gt; \&#10;  &#45;-ipv4 &lt;YOUR_DATABASE_IP&gt; \&#10;  &#45;-cert-verification-mode verify_ca&#10;</code></pre>
<p>To update an existing VPC Service, use <code>wrangler vpc service update</code> with the same flag.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9080.md")
</aside>
<p>For the full list of verification modes, refer to <a href="/workers-vpc/configuration/vpc-services/#tls-certificate-verification-mode">TLS certificate verification mode</a>.</p>
<h2 id="3-create-a-hyperdrive-configuration"><ol start="3">
<li>Create a Hyperdrive configuration</li>
</ol></h2>
<p>Use the <code>--service-id</code> flag to point Hyperdrive at the VPC Service you created. When you use <code>--service-id</code>, you do not provide <code>--origin-host</code>, <code>--origin-port</code>, or <code>--connection-string</code>. Hyperdrive routes traffic through the VPC Service instead.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9087.md")
</div></div>
<p>Replace:</p>
<ul>
<li><code>&lt;YOUR_VPC_SERVICE_ID&gt;</code> with the service ID from step 2.</li>
<li><code>&lt;DATABASE_NAME&gt;</code> with the name of your database.</li>
<li><code>&lt;DATABASE_USER&gt;</code> and <code>&lt;DATABASE_PASSWORD&gt;</code> with your database credentials.</li>
</ul>
<p>If successful, the command will output a Hyperdrive configuration with an <code>id</code> field. Copy this ID for the next step.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9079.md")
</aside>
<h2 id="4-bind-hyperdrive-to-a-worker"><ol start="4">
<li>Bind Hyperdrive to a Worker</li>
</ol></h2>
<p>You must create a binding in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> for your Worker to connect to your Hyperdrive configuration. <a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Workers to access resources, like Hyperdrive, on the Cloudflare developer platform.</p>
<p>To bind your Hyperdrive configuration to your Worker, add the following to the end of your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9088.md")
</div>
<p>Specifically:</p>
<ul>
<li>The value (string) you set for the <code>binding</code> (binding name) will be used to reference this database in your Worker. In this tutorial, name your binding <code>HYPERDRIVE</code>.</li>
<li>The binding must be <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variables">a valid JavaScript variable name</a>. For example, <code>binding = &quot;hyperdrive&quot;</code> or <code>binding = &quot;productionDB&quot;</code> would both be valid names for the binding.</li>
<li>Your binding is available in your Worker at <code>env.&lt;BINDING_NAME&gt;</code>.</li>
</ul>
<p>If you wish to use a local database during development, you can add a <code>localConnectionString</code> to your  Hyperdrive configuration with the connection string of your database:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9089.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9078.md")
</aside>
<h2 id="5-query-the-database"><ol start="5">
<li>Query the database</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9094.md")
</div></div>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">how Hyperdrive works</a>.</li>
<li>Configure <a href="/hyperdrive/concepts/query-caching/">query caching</a> for Hyperdrive.</li>
<li>Review <a href="/workers-vpc/configuration/vpc-services/">VPC Service configuration options</a> including TLS certificate verification.</li>
<li>Set up <a href="/workers-vpc/configuration/tunnel/hardware-requirements/">high availability tunnels</a> for production workloads.</li>
<li><a href="/hyperdrive/observability/troubleshooting/">Troubleshoot common issues</a> when connecting a database to Hyperdrive.</li>
</ul>
