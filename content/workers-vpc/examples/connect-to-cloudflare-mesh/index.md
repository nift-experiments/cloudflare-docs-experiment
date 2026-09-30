---
cp9:
  canonical: https://developers.cloudflare.com/workers-vpc/examples/connect-to-cloudflare-mesh/
  description: Use a VPC Network binding with Cloudflare Mesh to reach private services from a Worker.
  full_title: Connect Workers to Cloudflare Mesh · Cloudflare Workers VPC
  head_html: <title>Connect Workers to Cloudflare Mesh · Cloudflare Workers VPC</title><meta name="generator" content="Nift"><meta name="description" content="Use a VPC Network binding with Cloudflare Mesh to reach private services from a Worker."><link rel="canonical" href="https://developers.cloudflare.com/workers-vpc/examples/connect-to-cloudflare-mesh/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-vpc/examples/connect-to-cloudflare-mesh/index.md"><meta property="og:title" content="Connect Workers to Cloudflare Mesh · Cloudflare Workers VPC"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use a VPC Network binding with Cloudflare Mesh to reach private services from a Worker."><meta property="og:url" content="https://developers.cloudflare.com/workers-vpc/examples/connect-to-cloudflare-mesh/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers VPC"><meta name="algolia_product_filter" content="Workers VPC"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Workers VPC"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-vpc/examples/connect-to-cloudflare-mesh/#page","headline":"Connect Workers to Cloudflare Mesh \u00b7 Cloudflare Workers VPC","description":"Use a VPC Network binding with Cloudflare Mesh to reach private services from a Worker.","url":"https://developers.cloudflare.com/workers-vpc/examples/connect-to-cloudflare-mesh/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-vpc/examples/connect-to-cloudflare-mesh/
  schema: 1
---
<p>This example demonstrates how to use a VPC Network binding with <a href="/mesh/">Cloudflare Mesh</a> (formerly WARP Connector) to connect to any private service in your account from a Worker — without pre-registering individual hosts or specifying a Cloudflare Tunnel UUID.</p>
<p>When you bind to <a href="/mesh/">Cloudflare Mesh</a> using <code>network_id: &quot;cf1:network&quot;</code>, your Worker can reach any Mesh node, client device, subnet or hostname route announced through Cloudflare Tunnel or Cloudflare Mesh, or destination connected through a <a href="/cloudflare-wan/">Cloudflare WAN</a> on-ramp (GRE, IPsec, or CNI).</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="/mesh/">Cloudflare Mesh</a> node connected to your private network</li>
<li>Private services running behind your Mesh node (for example, an internal API, database, or web application)</li>
</ul>
<h2 id="1-configure-your-worker"><ol>
<li>Configure your Worker</li>
</ol></h2>
<p>Bind your Worker to Cloudflare Mesh using <code>network_id: &quot;cf1:network&quot;</code> in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15884.md")
</div>
<p>With this single binding, your Worker can reach any service across all Cloudflare Tunnels, Mesh nodes, and Cloudflare WAN on-ramps in your account.</p>
<h2 id="2-implement-the-worker"><ol start="2">
<li>Implement the Worker</li>
</ol></h2>
<p>Use the VPC Network binding to access services by private IP address. Cloudflare Mesh currently supports IP-based routing only.</p>
<pre tabindex="0"><code class="language-js">// You can target a Mesh node directly by its Mesh IP or any private IP&#10;// on a subnet route behind the node&#10;const SERVICE_IP = &quot;10.0.1.50&quot;;&#10;const SERVICE_PORT = 8080;&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		try {&#10;			const response = await env.MESH.fetch(&#10;				`http://${SERVICE_IP}:${SERVICE_PORT}/api/data`,&#10;			);&#10;			return response;&#10;		} catch (error) {&#10;			// fetch() throws if the VPC Network cannot connect to the target&#10;			return new Response(&quot;Service unavailable&quot;, { status: 503 });&#10;		}&#10;	},&#10;};&#10;</code></pre>
<p>Unlike <a href="/workers-vpc/configuration/vpc-services/">VPC Services</a>, the URL you pass to <code>fetch()</code> or the address you pass to <code>connect()</code> determines the actual destination. You can reach any IP and port accessible through your Mesh network without creating separate bindings for each service.</p>
<h3 id="tcp-connections">TCP connections</h3>
<p>You can also use <code>connect()</code> to open raw TCP sockets to non-HTTP services through the same binding:</p>
<pre tabindex="0"><code class="language-js">// You can target a Mesh node directly by its Mesh IP or any private IP&#10;// on a subnet route behind the node&#10;const REDIS_IP = &quot;10.0.1.50&quot;;&#10;const REDIS_PORT = 6379;&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		try {&#10;			const socket = await env.MESH.connect(`${REDIS_IP}:${REDIS_PORT}`);&#10;&#10;			const writer = socket.writable.getWriter();&#10;			await writer.write(new TextEncoder().encode(&quot;PING\r\n&quot;));&#10;			await writer.close();&#10;&#10;			return new Response(socket.readable);&#10;		} catch (error) {&#10;			// connect() throws if the VPC Network cannot connect to the target&#10;			return new Response(&quot;Service unavailable&quot;, { status: 503 });&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h2 id="3-deploy-and-test"><ol start="3">
<li>Deploy and test</li>
</ol></h2>
<p>Deploy your Worker and verify it can reach your private services:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler deploy&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">&#35; Test accessing the internal user API&#10;curl https://mesh-gateway.workers.dev/api/users&#10;&#10;&#35; Test accessing metrics by private IP&#10;curl https://mesh-gateway.workers.dev/api/metrics&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn more about <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a> configuration options</li>
<li>Refer to the <a href="/workers-vpc/api/">Workers Binding API</a> reference</li>
<li><a href="/mesh/get-started/">Set up Cloudflare Mesh</a> for your account</li>
<li>Explore <a href="/workers-vpc/examples/">other examples</a></li>
</ul>
