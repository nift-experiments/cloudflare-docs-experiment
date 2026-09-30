---
cp9:
  canonical: https://developers.cloudflare.com/workers-vpc/examples/route-across-private-services/
  description: Build a Worker gateway that routes and load balances across multiple private VPC Services.
  full_title: Route to private services from Workers · Cloudflare Workers VPC
  head_html: <title>Route to private services from Workers · Cloudflare Workers VPC</title><meta name="generator" content="Nift"><meta name="description" content="Build a Worker gateway that routes and load balances across multiple private VPC Services."><link rel="canonical" href="https://developers.cloudflare.com/workers-vpc/examples/route-across-private-services/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-vpc/examples/route-across-private-services/index.md"><meta property="og:title" content="Route to private services from Workers · Cloudflare Workers VPC"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build a Worker gateway that routes and load balances across multiple private VPC Services."><meta property="og:url" content="https://developers.cloudflare.com/workers-vpc/examples/route-across-private-services/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers VPC"><meta name="algolia_product_filter" content="Workers VPC"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Workers VPC"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-vpc/examples/route-across-private-services/#page","headline":"Route to private services from Workers \u00b7 Cloudflare Workers VPC","description":"Build a Worker gateway that routes and load balances across multiple private VPC Services.","url":"https://developers.cloudflare.com/workers-vpc/examples/route-across-private-services/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-vpc/examples/route-across-private-services/
  schema: 1
---
<p>This example shows how to use Workers VPC to create a centralized gateway that routes requests based on URL paths, provides authentication and rate limiting, and load balances across internal services.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Multiple private APIs or services running in your VPC/virtual network (we'll use a user service and orders service)</li>
<li>Cloudflare Tunnel configured and running (follow the <a href="/workers-vpc/get-started/#2-set-up-cloudflare-tunnel">Get Started guide</a> to set up or <a href="https://dash.cloudflare.com/?to=/:account/workers/vpc/tunnels">create a tunnel from the dashboard</a>)</li>
<li>Workers account with Workers VPC access</li>
</ul>
<h2 id="1-create-the-vpc-services"><ol>
<li>Create the VPC Services</li>
</ol></h2>
<p>First, create services for your internal APIs using hostnames:</p>
<pre tabindex="0"><code class="language-bash">&#35; Create user service&#10;npx wrangler vpc service create user-service \&#10;  &#45;-type http \&#10;  &#45;-tunnel-id &lt;YOUR_TUNNEL_ID&gt; \&#10;  &#45;-hostname user-api.internal.example.com&#10;&#10;&#35; Create orders service&#10;npx wrangler vpc service create order-service \&#10;  &#45;-type http \&#10;  &#45;-tunnel-id &lt;YOUR_TUNNEL_ID&gt; \&#10;  &#45;-hostname orders-api.internal.example.com&#10;</code></pre>
<p>Note the service IDs returned for the next step.</p>
<h2 id="2-configure-your-worker"><ol start="2">
<li>Configure your Worker</li>
</ol></h2>
<p>Update your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15874.md")
</div>
<h2 id="3-implement-the-worker"><ol start="3">
<li>Implement the Worker</li>
</ol></h2>
<p>In your Workers code, use the VPC Service bindings to route requests to the appropriate services:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		const url = new URL(request.url);&#10;&#10;		// Route to internal services&#10;		if (url.pathname.startsWith(&#x27;/api/users&#x27;)) {&#10;			const response = await env.USER_SERVICE.fetch(&quot;https://user-api.internal.example.com&quot; + url.pathname);&#10;			return response;&#10;		} else if (url.pathname.startsWith(&#x27;/api/orders&#x27;)) {&#10;			const response = await env.ORDER_SERVICE.fetch(&quot;https://orders-api.internal.example.com&quot; + url.pathname);&#10;			return response;&#10;		}&#10;&#10;		return new Response(&#x27;Not Found&#x27;, { status: 404 });&#10;	},&#10;};&#10;</code></pre>
<h2 id="4-deploy-and-test"><ol start="4">
<li>Deploy and test</li>
</ol></h2>
<p>Now, you can deploy and test your Worker:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler deploy&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">&#35; Test user service requests&#10;curl https://api-gateway.workers.dev/api/users&#10;&#10;&#35; Test orders service requests&#10;curl https://api-gateway.workers.dev/api/orders&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Add <a href="/workers/examples/auth-with-headers/">authentication and authorization</a></li>
<li>Implement <a href="/durable-objects/api/">rate limiting</a></li>
<li>Set up <a href="/analytics/analytics-engine/">monitoring and alerting</a></li>
<li>Explore <a href="/workers-vpc/examples/">other examples</a></li>
</ul>
