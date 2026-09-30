---
cp9:
  canonical: https://developers.cloudflare.com/workers-vpc/examples/private-api/
  description: Use Workers VPC to fetch data from a private REST API behind Cloudflare Tunnel.
  full_title: Access a private API or website · Cloudflare Workers VPC
  head_html: <title>Access a private API or website · Cloudflare Workers VPC</title><meta name="generator" content="Nift"><meta name="description" content="Use Workers VPC to fetch data from a private REST API behind Cloudflare Tunnel."><link rel="canonical" href="https://developers.cloudflare.com/workers-vpc/examples/private-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-vpc/examples/private-api/index.md"><meta property="og:title" content="Access a private API or website · Cloudflare Workers VPC"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Workers VPC to fetch data from a private REST API behind Cloudflare Tunnel."><meta property="og:url" content="https://developers.cloudflare.com/workers-vpc/examples/private-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers VPC"><meta name="algolia_product_filter" content="Workers VPC"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Workers VPC"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-vpc/examples/private-api/#page","headline":"Access a private API or website \u00b7 Cloudflare Workers VPC","description":"Use Workers VPC to fetch data from a private REST API behind Cloudflare Tunnel.","url":"https://developers.cloudflare.com/workers-vpc/examples/private-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-vpc/examples/private-api/
  schema: 1
---
<p>This example demonstrates how to access a private REST API that is not exposed to the public internet. In this guide, we will configure a VPC Service for an internal API, create a Worker that makes requests to that API, and deploy the Worker to validate our changes.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A virtual machine/EC2 instance running in your VPC/virtual network</li>
<li>A private API or website running in your VPC/virtual network with security rules allowing access to the virtual machine that will be running <code>cloudflared</code></li>
<li>Workers account with Workers VPC access</li>
</ul>
<h2 id="1-set-up-cloudflare-tunnel"><ol>
<li>Set up Cloudflare Tunnel</li>
</ol></h2>
<p>A Cloudflare Tunnel creates a secure connection from your private network to Cloudflare. This tunnel will allow Workers to securely access your private resources.</p>
<ol>
<li>
<p>Navigate to the <a href="https://dash.cloudflare.com/?to=/:account/workers/vpc/tunnels">Workers VPC dashboard</a> and select the <strong>Tunnels</strong> tab.</p>
</li>
<li>
<p>Select <strong>Create</strong> to create a new tunnel.</p>
</li>
<li>
<p>Enter a name for your tunnel (for example, <code>private-api-tunnel</code>) and select <strong>Save tunnel</strong>.</p>
</li>
<li>
<p>Choose your operating system and architecture. The dashboard will provide specific installation instructions for your environment.</p>
</li>
<li>
<p>Follow the provided commands to download and install <code>cloudflared</code> on your VM, and execute the service installation command with your unique token.</p>
</li>
</ol>
<p>The dashboard will confirm when your tunnel is successfully connected. Note the tunnel ID for the next step.</p>
<h2 id="2-create-the-workers-vpc-service"><ol start="2">
<li>Create the Workers VPC Service</li>
</ol></h2>
<p>First, create a Workers VPC Service for your internal API:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler vpc service create api-service \&#10;  &#45;-type http \&#10;  &#45;-tunnel-id &lt;YOUR_TUNNEL_ID&gt; \&#10;  &#45;-ipv4 10.0.1.50 \&#10;  &#45;-http-port 8080&#10;</code></pre>
<p>You can also create a VPC Service for a service using its hostname:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler vpc service create api-service \&#10;  &#45;-type http \&#10;  &#45;-tunnel-id &lt;YOUR_TUNNEL_ID&gt; \&#10;  &#45;-hostname internal-hostname.example.com&#10;</code></pre>
<p>Note the service ID returned for the next step.</p>
<h2 id="3-configure-your-worker"><ol start="3">
<li>Configure your Worker</li>
</ol></h2>
<p>Update your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15883.md")
</div>
<h2 id="4-implement-the-worker"><ol start="4">
<li>Implement the Worker</li>
</ol></h2>
<p>In your Workers code, use the VPC Service binding in order to send requests to the service:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		try {&#10;			// Fetch data from internal API and process it before returning&#10;			const response = await env.INTERNAL_API.fetch(&quot;http://10.0.1.50:8080/api/data&quot;);&#10;&#10;			// Use the response of the private API to perform more logic in Workers, before returning the final response&#10;			return response;&#10;		} catch (error) {&#10;			return new Response(&quot;Service unavailable&quot;, { status: 503 });&#10;		}&#10;	},&#10;};&#10;</code></pre>
<p>This guide demonstrates how you could create a simple proxy in your Workers. However, you could use VPC Services to fetch APIs directly and manipulate the responses to enable you to build more full-stack and backend functionality on Workers.</p>
<h2 id="5-deploy-and-test"><ol start="5">
<li>Deploy and test</li>
</ol></h2>
<p>Now, you can deploy and test your Worker that you have created:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler deploy&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">&#35; Test GET request&#10;curl https://private-api-gateway.workers.dev&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Add <a href="/workers/examples/auth-with-headers/">authentication and authorization</a></li>
<li>Implement <a href="/durable-objects/api/">rate limiting</a></li>
<li>Set up <a href="/analytics/analytics-engine/">monitoring and alerting</a></li>
<li>Explore <a href="/workers-vpc/examples/">other examples</a></li>
</ul>
