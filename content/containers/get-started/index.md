---
cp9:
  canonical: https://developers.cloudflare.com/containers/get-started/
  description: Deploy your first Container on Cloudflare by building an image, configuring a Worker, and routing requests to container instances.
  full_title: Get started · Cloudflare Containers docs
  head_html: <title>Get started · Cloudflare Containers docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy your first Container on Cloudflare by building an image, configuring a Worker, and routing requests to container instances."><link rel="canonical" href="https://developers.cloudflare.com/containers/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/containers/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare Containers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy your first Container on Cloudflare by building an image, configuring a Worker, and routing requests to container instances."><meta property="og:url" content="https://developers.cloudflare.com/containers/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Containers"><meta name="algolia_product_filter" content="Containers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Containers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/containers/get-started/#page","headline":"Get started \u00b7 Cloudflare Containers docs","description":"Deploy your first Container on Cloudflare by building an image, configuring a Worker, and routing requests to container instances.","url":"https://developers.cloudflare.com/containers/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /containers/get-started/
  schema: 1
---
<p>In this guide, you will deploy a Worker that can make requests to one or more Containers in response to end-user requests.
In this example, each container runs a small webserver written in Go.</p>
<p>This example Worker should give you a sense for simple Container use, and provide a starting point for more complex use cases.</p>
<h2 id="prerequisites">Prerequisites</h2>
<h3 id="ensure-docker-is-running-locally">Ensure Docker is running locally</h3>
<p>In this guide, we will build and push a container image alongside your Worker code. By default, this process uses
<a href="https://www.docker.com/">Docker</a> to do so.</p>
<p>You must have Docker running locally when you run <code>wrangler deploy</code>. For most people, the best way to install Docker is to follow the <a href="https://docs.docker.com/desktop/">docs for installing Docker Desktop</a>. Other tools like <a href="https://github.com/abiosoft/colima">Colima</a> may also work.</p>
<p>You can check that Docker is running properly by running the <code>docker info</code> command in your terminal. If Docker is running, the command will succeed. If Docker is not running,
the <code>docker info</code> command will hang or return an error including the message &quot;Cannot connect to the Docker daemon&quot;.</p>
<h2 id="deploy-your-first-container">Deploy your first Container</h2>
<p>Run the following command to create and deploy a new Worker with a container, from the starter template:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- --template=cloudflare/templates/containers-template</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- --template=cloudflare/templates/containers-template" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare --template=cloudflare/templates/containers-template</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare --template=cloudflare/templates/containers-template" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest --template=cloudflare/templates/containers-template</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest --template=cloudflare/templates/containers-template" aria-label="Copy to clipboard">Copy</button></div></div>
<p>When you want to deploy a code change to either the Worker or Container code, you can run the following command using <a href="/workers/wrangler/">Wrangler CLI</a>:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler deploy" aria-label="Copy to clipboard">Copy</button></div></div>
<p>On deploy, Wrangler uploads your Worker, builds and pushes the container image with Docker, and updates container instances on Cloudflare's network. The first build and push usually take the longest. Later deploys <a href="https://docs.docker.com/build/cache/">reuse cached image layers</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7136.md")
</aside>
<h3 id="check-deployment-status">Check deployment status</h3>
<p>After deploying, list containers in your account and their status:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler containers list</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler containers list" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler containers list</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler containers list" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler containers list</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler containers list" aria-label="Copy to clipboard">Copy</button></div></div>
<p>List images in the Cloudflare Registry:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx wrangler containers images list</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler containers images list" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn wrangler containers images list</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler containers images list" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm wrangler containers images list</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler containers images list" aria-label="Copy to clipboard">Copy</button></div></div>
<h3 id="make-requests-to-containers">Make requests to Containers</h3>
<p>Open the URL for your Worker. It should look like <code>https://hello-containers.&lt;YOUR_WORKERS_SUBDOMAIN&gt;.workers.dev</code>.</p>
<ul>
<li>Requests to <code>/container/1</code> or <code>/container/2</code> route to specific containers. Each path after <code>/container/</code> maps to a unique container.</li>
<li>Requests to <code>/lb</code> load-balance across three containers chosen at random.</li>
</ul>
<p>Read the response body to confirm which instance handled the request. If the Worker responds but container routes still error, wait for provisioning, then check <a href="https://dash.cloudflare.com/?to=/:account/workers/containers">Containers</a> logs in the dashboard.</p>
<h2 id="understanding-the-code">Understanding the Code</h2>
<p>Now that you've deployed your first container, let's explain what is happening in your Worker's code, in your configuration file, in your container's code, and how requests are routed.</p>
<h3 id="configuration">Configuration</h3>
<p>Your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> defines the configuration for both your Worker and your container:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7137.md")
</div>
<p>Important points about this config:</p>
<ul>
<li><code>image</code> points to a Dockerfile, to a directory containing a Dockerfile, or to a fully qualified image reference such as <code>registry.cloudflare.com/&lt;YOUR_ACCOUNT_ID&gt;/&lt;IMAGE&gt;:&lt;TAG&gt;</code>.</li>
<li><code>class_name</code> must be a <a href="/durable-objects/api/base/">Durable Object class name</a>.</li>
<li><code>max_instances</code> declares the maximum number of simultaneously running container instances
that will run.</li>
<li>The Durable Object must use <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class"><code>new_sqlite_classes</code></a> not <code>new_classes</code>.</li>
</ul>
<h3 id="the-container-image">The Container Image</h3>
<p>Your container image must be able to run on the <code>linux/amd64</code> architecture, but aside from that, has few limitations.</p>
<p>In the example you just deployed, it is a simple Golang server that responds to requests on port 8080 using
the <code>MESSAGE</code> environment variable that will be set in the Worker and an <a href="/containers/configuration/environment-variables/">auto-generated
environment variable</a> <code>CLOUDFLARE_DEPLOYMENT_ID.</code></p>
<pre tabindex="0"><code class="language-go">func handler(w http.ResponseWriter, r *http.Request) {&#10;	message := os.Getenv(&quot;MESSAGE&quot;)&#10;	instanceId := os.Getenv(&quot;CLOUDFLARE_DEPLOYMENT_ID&quot;)&#10;&#10;	fmt.Fprintf(w, &quot;Hi, I&#x27;m a container and this is my message: %s, and my instance ID is: %s&quot;, message, instanceId)&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7135.md")
</aside>
<h3 id="worker-code">Worker code</h3>
<h4 id="container-configuration">Container Configuration</h4>
<p>First note <code>MyContainer</code> which extends the <a href="https://github.com/cloudflare/containers"><code>Container</code></a> class:</p>
<pre tabindex="0"><code class="language-js">export class MyContainer extends Container {&#10;  defaultPort = 8080;&#10;  sleepAfter = &#x27;10s&#x27;;&#10;  envVars = {&#10;    MESSAGE: &#x27;I was passed in via the container class!&#x27;,&#10;  };&#10;&#10;  override onStart() {&#10;    console.log(&#x27;Container successfully started&#x27;);&#10;  }&#10;&#10;  override onStop() {&#10;    console.log(&#x27;Container successfully shut down&#x27;);&#10;  }&#10;&#10;  override onError(error: unknown) {&#10;    console.log(&#x27;Container error:&#x27;, error);&#10;  }&#10;}&#10;</code></pre>
<p>This defines basic configuration for the container:</p>
<ul>
<li><code>defaultPort</code> sets the port that the <code>fetch</code> and <code>containerFetch</code> methods will use to communicate with the container. It also blocks
requests until the container is listening on this port.</li>
<li><code>sleepAfter</code> sets the timeout for the container to sleep after it has been idle for a certain amount of time.</li>
<li><code>envVars</code> sets environment variables that will be passed to the container when it starts.</li>
<li><code>onStart</code>, <code>onStop</code>, and <code>onError</code> are hooks that run when the container starts, stops, or errors, respectively.</li>
</ul>
<p>The <code>Container</code> class itself extends <a href="/durable-objects/"><code>DurableObject</code></a>, so your subclass has access to the full Durable Object API. The Durable Object handles routing, lifecycle, and persistent state, while the container process runs your image inside a Linux VM. This means you can use <a href="/durable-objects/api/sqlite-storage-api/"><code>this.ctx.storage</code></a> to persist data that survives container restarts and resides close to the container itself.</p>
<p>Refer to the <a href="/containers/reference/container-class/">Container class reference</a> and the <a href="/durable-objects/api/container/">low-level Durable Object container API</a> for more details.</p>
<h4 id="routing-to-containers">Routing to Containers</h4>
<p>When a request enters Cloudflare, your Worker's <a href="/workers/runtime-apis/handlers/fetch/"><code>fetch</code> handler</a> is invoked. This is the code that handles the incoming request. The fetch handler in the example code, launches containers in two ways, on different routes:</p>
<ul>
<li>Making requests to <code>/container/</code> passes requests to a new container for
each path. This is done by spinning up a new Container instance. You may note
that the first request to a new path takes longer than subsequent requests, this is
because a new container is booting.</li>
</ul>
<pre tabindex="0"><code class="language-js">if (pathname.startsWith(&quot;/container&quot;)) {&#10;	const container = env.MY_CONTAINER.getByName(pathname);&#10;	return await container.fetch(request);&#10;}&#10;</code></pre>
<ul>
<li>Making requests to <code>/lb</code> will load balance requests across several containers.
This uses a simple <code>getRandom</code> helper method, which picks an ID at random
from a set number (in this case 3), then routes to that Container instance. You can replace this with any routing or load balancing logic you choose to implement:</li>
</ul>
<pre tabindex="0"><code class="language-js">if (pathname.startsWith(&quot;/lb&quot;)) {&#10;	const container = await getRandom(env.MY_CONTAINER, 3);&#10;	return await container.fetch(request);&#10;}&#10;</code></pre>
<p>This allows for multiple ways of using Containers:</p>
<ul>
<li>If you simply want to send requests to many stateless and interchangeable containers,
you should load balance.</li>
<li>If you have stateful services or need individually addressable
containers, you should request specific Container instances.</li>
<li>If you are running short-lived jobs, want fine-grained control over the container
lifecycle, want to parameterize container entrypoint or env vars, or
want to chain together multiple container calls, you should request specific
Container instances.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7134.md")
</aside>
<h2 id="view-containers-in-your-dashboard">View Containers in your Dashboard</h2>
<p>The <a href="https://dash.cloudflare.com/?to=/:account/workers/containers">Containers Dashboard</a> shows you helpful
information about your Containers, including:</p>
<ul>
<li>Status and Health</li>
<li>Metrics</li>
<li>Logs</li>
</ul>
<p>After launching your Worker, go to the Containers Dashboard by selecting
<strong>Workers &amp; Pages</strong> &gt; <strong>Containers</strong> in the dashboard sidebar.</p>
<h2 id="next-steps">Next Steps</h2>
<p>To do more:</p>
<ul>
<li>Modify the image by changing the Dockerfile and running <code>wrangler deploy</code></li>
<li>Refer to <a href="/containers/guides/deploy/">Deploy Containers</a> for Workers Builds and rollout behavior</li>
<li>Browse <a href="/containers/examples/">examples</a> for more patterns</li>
<li>Check the <a href="/containers/faq/">Frequently Asked Questions</a> for platform behavior and limitations</li>
</ul>
