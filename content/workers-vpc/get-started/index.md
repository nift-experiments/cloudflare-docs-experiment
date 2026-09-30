---
cp9:
  canonical: https://developers.cloudflare.com/workers-vpc/get-started/
  description: Create your first Workers VPC Service and connect a Worker to your private network.
  full_title: Get started · Cloudflare Workers VPC
  head_html: <title>Get started · Cloudflare Workers VPC</title><meta name="generator" content="Nift"><meta name="description" content="Create your first Workers VPC Service and connect a Worker to your private network."><link rel="canonical" href="https://developers.cloudflare.com/workers-vpc/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-vpc/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare Workers VPC"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create your first Workers VPC Service and connect a Worker to your private network."><meta property="og:url" content="https://developers.cloudflare.com/workers-vpc/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers VPC"><meta name="algolia_product_filter" content="Workers VPC"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Workers VPC"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-vpc/get-started/#page","headline":"Get started \u00b7 Cloudflare Workers VPC","description":"Create your first Workers VPC Service and connect a Worker to your private network.","url":"https://developers.cloudflare.com/workers-vpc/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-vpc/get-started/
  schema: 1
---
<p>This guide will walk you through creating your first Workers VPC Service, allowing your Worker to access resources in your private network.</p>
<p>You will create a Workers application, create a Tunnel in your private network to connect it to Cloudflare, and then configure VPC Services for the services on your private network you want to access from Workers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15866.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, ensure you have completed the following:</p>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15867.md")
</div></details>
<p>Additionally, you will need:</p>
<ul>
<li>Access to a private network (your local network, AWS VPC, Azure VNet, GCP VPC, or on-premise networks)</li>
<li>The <strong>Connectivity Directory Bind</strong> role to bind to existing VPC Services from Workers.</li>
<li>Or, the <strong>Connectivity Directory Admin</strong> role to create VPC Services, and bind to them from Workers.</li>
</ul>
<h2 id="1-create-a-new-worker-project"><ol>
<li>Create a new Worker project</li>
</ol></h2>
<p>Create a new Worker project using Wrangler:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- workers-vpc-app</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- workers-vpc-app" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare workers-vpc-app</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare workers-vpc-app" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest workers-vpc-app</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest workers-vpc-app" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Navigate to your project directory:</p>
<pre tabindex="0"><code class="language-sh">cd workers-vpc-app&#10;</code></pre>
<h2 id="2-set-up-cloudflare-tunnel"><ol start="2">
<li>Set up Cloudflare Tunnel</li>
</ol></h2>
<p>A Cloudflare Tunnel creates a secure connection from your private network to Cloudflare. This tunnel will allow Workers to securely access your private resources. You can create the tunnel on a virtual machine or container in your external cloud, or even on your local desktop for the sake of this tutorial.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15868.md")
</div>
<p>The dashboard will confirm when your tunnel is successfully connected.</p>
<h3 id="configuring-your-private-network-for-cloudflare-tunnel">Configuring your private network for Cloudflare Tunnel</h3>
<p>Once your tunnel is connected, you will need to ensure it can access the services that you want your Workers to have access to. The tunnel should be installed on a machine that can reach the internal resources you want to expose to Workers VPC. In external clouds, this may mean configuring Access-Control-Lists, Security Groups, or VPC Firewall Rules to ensure that the tunnel can access the desired services.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15865.md")
</aside>
<h2 id="3-create-a-vpc-service"><ol start="3">
<li>Create a VPC Service</li>
</ol></h2>
<p>Now that your tunnel is running, create a VPC Service that Workers can use to access your internal resources:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15872.md")
</div></div>
<p>If you encounter permission errors, refer to <a href="/workers-vpc/configuration/vpc-services/#required-roles">Required roles</a>.</p>
<h2 id="4-configure-your-worker"><ol start="4">
<li>Configure your Worker</li>
</ol></h2>
<p>Add the VPC Service binding to your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15873.md")
</div>
<p>Replace <code>&lt;YOUR_SERVICE_ID&gt;</code> with the service ID from step 3.</p>
<h2 id="5-write-your-worker-code"><ol start="5">
<li>Write your Worker code</li>
</ol></h2>
<p>Update your Worker to use the VPC Service binding. The following example:</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		const url = new URL(request.url);&#10;&#10;		// This is a simple proxy scenario.&#10;		// In this case, you will need to replace the URL with the proper protocol (http vs. https), hostname and port of the service.&#10;		// For example, this could be &quot;http://localhost:1111&quot;, &quot;http://192.0.0.1:3000&quot;, &quot;https://my-internal-api.example.com&quot;&#10;		const targetUrl = new URL(&#10;			`http://&lt;ENTER_SERVICE_HOST&gt;:&lt;ENTER_SERVICE_PORT&gt;${url.pathname}${url.search}`,&#10;		);&#10;&#10;		// Create new request with the target URL but preserve all other properties&#10;		const proxyRequest = new Request(targetUrl, {&#10;			method: request.method,&#10;			headers: request.headers,&#10;			body: request.body,&#10;		});&#10;&#10;		const response = await env.VPC_SERVICE.fetch(proxyRequest);&#10;&#10;		return response;&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<h2 id="6-test-locally"><ol start="6">
<li>Test locally</li>
</ol></h2>
<p>Test your Worker locally. You must use remote VPC Services, using either <a href="/workers/local-development/#remote-bindings">Workers remote bindings</a> as was configured in your <code>wrangler.jsonc</code> configuration file, or using <code>npx wrangler dev --remote</code>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev&#10;</code></pre>
<p>Visit <code>http://localhost:8787</code> to test your Worker's connection to your private network.</p>
<h2 id="7-deploy-your-worker"><ol start="7">
<li>Deploy your Worker</li>
</ol></h2>
<p>Once testing is complete, deploy your Worker:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Your Worker is now deployed and can access your private network resources securely through the Cloudflare Tunnel. If you encounter permission errors, refer to <a href="/workers-vpc/configuration/vpc-services/#required-roles">Required roles</a>.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Explore <a href="/workers-vpc/configuration/">configuration options</a> for advanced setups</li>
<li>Set up <a href="/workers-vpc/configuration/tunnel/hardware-requirements/">high availability tunnels</a> for production</li>
<li>View <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/">platform-specific guides</a> for AWS, Azure, GCP, and Kubernetes</li>
<li>Check out <a href="/workers-vpc/examples/">examples</a> for common use cases</li>
</ul>
