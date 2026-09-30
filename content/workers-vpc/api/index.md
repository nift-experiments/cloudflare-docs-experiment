---
cp9:
  canonical: https://developers.cloudflare.com/workers-vpc/api/
  description: API reference for VPC Service and VPC Network bindings in Workers.
  full_title: Workers Binding API · Cloudflare Workers VPC
  head_html: <title>Workers Binding API · Cloudflare Workers VPC</title><meta name="generator" content="Nift"><meta name="description" content="API reference for VPC Service and VPC Network bindings in Workers."><link rel="canonical" href="https://developers.cloudflare.com/workers-vpc/api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-vpc/api/index.md"><meta property="og:title" content="Workers Binding API · Cloudflare Workers VPC"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for VPC Service and VPC Network bindings in Workers."><meta property="og:url" content="https://developers.cloudflare.com/workers-vpc/api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers VPC"><meta name="algolia_product_filter" content="Workers VPC"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers VPC"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-vpc/api/#page","headline":"Workers Binding API \u00b7 Cloudflare Workers VPC","description":"API reference for VPC Service and VPC Network bindings in Workers.","url":"https://developers.cloudflare.com/workers-vpc/api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-vpc/api/
  schema: 1
---
<p>VPC bindings provide APIs for accessing private services from your Worker. Both <a href="/workers-vpc/configuration/vpc-services/">VPC Services</a> and <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a> expose a <code>fetch()</code> method for HTTP traffic. VPC Networks also expose a <code>connect()</code> method for raw TCP connections. The difference between binding types is in routing scope, not in API surface.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15887.md")
</aside>
<h2 id="binding-types">Binding types</h2>
<h3 id="vpc-service">VPC Service</h3>
<p>A VPC Service binding routes requests to a specific pre-registered host and port. The <a href="/workers-vpc/configuration/vpc-services/#vpc-service-configuration">VPC Service configuration</a> always determines the connection target, even if a different URL or host is present in the <code>fetch()</code> call.</p>
<ul>
<li>The <strong>host</strong> provided in <code>fetch()</code> does not control routing. It only populates the <code>Host</code> header and, when using <code>https</code>, the Server Name Indication (SNI) value.</li>
<li>The <strong>port</strong> provided in <code>fetch()</code> is ignored — the port specified in the VPC Service configuration is always used.</li>
</ul>
<h3 id="vpc-network">VPC Network</h3>
<p>A VPC Network binding grants access to any service reachable through the bound Cloudflare Tunnel or through Cloudflare Mesh — including subnet and hostname routes announced through Cloudflare Tunnel or Mesh, and destinations connected through Cloudflare WAN on-ramps (GRE, IPsec, or CNI). The URL passed to <code>fetch()</code> or the address passed to <code>connect()</code> determines the actual destination — hostname or IP address and port.</p>
<h2 id="fetch">fetch()</h2>
<p>Makes an HTTP request to the private service through the bound Cloudflare Tunnel or Cloudflare Mesh. Available on both VPC Service and VPC Network bindings.</p>
<pre tabindex="0"><code class="language-js">const response = await env.MY_BINDING.fetch(resource, options);&#10;</code></pre>
<h3 id="parameters">Parameters</h3>
<ul>
<li><code>resource</code> (string | URL | Request) — The URL to fetch. Must be an absolute URL including protocol, host, and path (for example, <code>http://internal-api/api/users</code>).</li>
<li><code>options</code> (optional RequestInit) — Standard fetch options including:
<ul>
<li><code>method</code> — HTTP method (GET, POST, PUT, DELETE, etc.)</li>
<li><code>headers</code> — Request headers</li>
<li><code>body</code> — Request body</li>
<li><code>signal</code> — AbortSignal for request cancellation</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="absolute-urls-required">Absolute URLs required</h3>
@markup("md", "content/.markup/bodies/15886.md")
</aside>
<h3 id="return-value">Return value</h3>
<p>Returns a <code>Promise&lt;Response&gt;</code> that resolves to a <a href="https://developer.mozilla.org/en-US/docs/Web/API/Response">standard Fetch API Response object</a>.</p>
<h3 id="examples">Examples</h3>
<p>The following examples apply to both VPC Service and VPC Network bindings.</p>
<h4 id="basic-get-request">Basic GET request</h4>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		const privateRequest = new Request(&#10;			&quot;http://internal-api.company.local/users&quot;,&#10;		);&#10;		const response = await env.MY_BINDING.fetch(privateRequest);&#10;		const users = await response.json();&#10;&#10;		return new Response(JSON.stringify(users), {&#10;			headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;		});&#10;	},&#10;};&#10;</code></pre>
<h4 id="post-request-with-body">POST request with body</h4>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		const privateRequest = new Request(&#10;			&quot;http://internal-api.company.local/users&quot;,&#10;			{&#10;				method: &quot;POST&quot;,&#10;				headers: {&#10;					&quot;Content-Type&quot;: &quot;application/json&quot;,&#10;					Authorization: `Bearer ${env.API_TOKEN}`,&#10;				},&#10;				body: JSON.stringify({&#10;					name: &quot;John Doe&quot;,&#10;					email: &quot;john@example.com&quot;,&#10;				}),&#10;			},&#10;		);&#10;&#10;		const response = await env.MY_BINDING.fetch(privateRequest);&#10;&#10;		if (!response.ok) {&#10;			return new Response(&quot;Failed to create user&quot;, { status: response.status });&#10;		}&#10;&#10;		const user = await response.json();&#10;		return new Response(JSON.stringify(user), {&#10;			headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;		});&#10;	},&#10;};&#10;</code></pre>
<h4 id="request-with-https-and-ip-address">Request with HTTPS and IP address</h4>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		const privateRequest = new Request(&quot;https://10.0.1.50/api/data&quot;);&#10;		const response = await env.MY_BINDING.fetch(privateRequest);&#10;&#10;		return response;&#10;	},&#10;};&#10;</code></pre>
<h2 id="connect">connect()</h2>
<p>Opens a raw TCP connection to a private destination through the bound Cloudflare Tunnel or Cloudflare Mesh. Available on VPC Network bindings only.</p>
<pre tabindex="0"><code class="language-js">const socket = await env.MY_BINDING.connect(address);&#10;</code></pre>
<h3 id="parameters-1">Parameters</h3>
<ul>
<li><code>address</code> (string | SocketAddress) — The destination to connect to. Pass a string in <code>&quot;host:port&quot;</code> format (for example, <code>&quot;10.0.1.50:6379&quot;</code>) or a <a href="/workers/runtime-apis/tcp-sockets/#socketaddress/"><code>SocketAddress</code></a> object with <code>hostname</code> and <code>port</code>.</li>
</ul>
<h3 id="return-value-1">Return value</h3>
<p>Returns a <code>Promise&lt;Socket&gt;</code> that resolves to a <a href="/workers/runtime-apis/tcp-sockets/#socket/"><code>Socket</code></a> with <code>readable</code> and <code>writable</code> streams. If <code>connect()</code> cannot establish the connection, it throws an exception.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15885.md")
</aside>
<h3 id="examples-1">Examples</h3>
<h4 id="connect-to-a-private-redis-instance">Connect to a private Redis instance</h4>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		const socket = await env.MY_BINDING.connect(&quot;10.0.1.50:6379&quot;);&#10;&#10;		const writer = socket.writable.getWriter();&#10;		await writer.write(new TextEncoder().encode(&quot;PING\r\n&quot;));&#10;		await writer.close();&#10;&#10;		return new Response(socket.readable);&#10;	},&#10;};&#10;</code></pre>
<h4 id="connect-using-a-socketaddress-object">Connect using a SocketAddress object</h4>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		const socket = await env.MY_BINDING.connect({&#10;			hostname: &quot;10.0.1.50&quot;,&#10;			port: 6379,&#10;		});&#10;&#10;		const writer = socket.writable.getWriter();&#10;		await writer.write(new TextEncoder().encode(&quot;PING\r\n&quot;));&#10;		await writer.close();&#10;&#10;		return new Response(socket.readable);&#10;	},&#10;};&#10;</code></pre>
<h2 id="required-roles">Required roles</h2>
<p>To bind a VPC Service or VPC Network in a Worker, your user needs <code>Connectivity Directory Bind</code> (or <code>Connectivity Directory Admin</code>). Binding directly to a Cloudflare Tunnel through a VPC Network binding requires <code>Connectivity Directory Admin</code>. For role definitions, refer to <a href="/fundamentals/manage-members/roles/#account-scoped-roles">Roles</a>.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Configure <a href="/workers-vpc/configuration/vpc-services/">VPC Services</a></li>
<li>Configure <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a></li>
<li>Refer to <a href="/workers-vpc/examples/">usage examples</a></li>
</ul>
