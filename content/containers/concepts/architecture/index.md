---
cp9:
  canonical: https://developers.cloudflare.com/containers/concepts/architecture/
  description: Understand how a Container is deployed, started, routed, and shut down across Cloudflare's network.
  full_title: Lifecycle of a Container · Cloudflare Containers docs
  head_html: <title>Lifecycle of a Container · Cloudflare Containers docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand how a Container is deployed, started, routed, and shut down across Cloudflare&#x27;s network."><link rel="canonical" href="https://developers.cloudflare.com/containers/concepts/architecture/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/containers/concepts/architecture/index.md"><meta property="og:title" content="Lifecycle of a Container · Cloudflare Containers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand how a Container is deployed, started, routed, and shut down across Cloudflare&#x27;s network."><meta property="og:url" content="https://developers.cloudflare.com/containers/concepts/architecture/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Containers"><meta name="algolia_product_filter" content="Containers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Containers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/containers/concepts/architecture/#page","headline":"Lifecycle of a Container \u00b7 Cloudflare Containers docs","description":"Understand how a Container is deployed, started, routed, and shut down across Cloudflare's network.","url":"https://developers.cloudflare.com/containers/concepts/architecture/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /containers/concepts/architecture/
  schema: 1
---
<h2 id="deployment">Deployment</h2>
<p>After you deploy an application with a Container, your image is uploaded to
<a href="/containers/guides/image-management/">Cloudflare's Registry</a> and distributed globally to Cloudflare's Network.
Cloudflare will pre-schedule instances and pre-fetch images across the globe to ensure quick start
times when scaling up the number of concurrent container instances.</p>
<p>Worker code goes live on deploy. Container instances update with a <a href="/containers/configuration/rollouts/">rollout</a>. Refer to <a href="/containers/guides/deploy/">Deploy Containers</a>.</p>
<h2 id="lifecycle-of-a-request">Lifecycle of a Request</h2>
<h3 id="client-to-worker">Client to Worker</h3>
<p>Recall that Containers are backed by <a href="/durable-objects/">Durable Objects</a> and <a href="/workers/">Workers</a>.
Requests are first routed through a Worker, which is generally handled
by a datacenter in a location with the best latency between itself and the requesting user.
A different datacenter may be selected to optimize overall latency, if <a href="/workers/configuration/placement/">Smart Placement</a>
is on, or if the nearest location is under heavy load.</p>
<p>Because all Container requests are passed through a Worker, end-users cannot make non-HTTP TCP or
UDP requests to a Container instance. If you have a use case that requires inbound TCP
or UDP from an end-user, please <a href="https://forms.gle/AGSq54VvUje6kmKu8">let us know</a>.</p>
<h3 id="worker-to-durable-object">Worker to Durable Object</h3>
<p>From the Worker, a request passes through a Durable Object instance (the <a href="/containers/reference/container-class/">Container class</a> extends a Durable Object class).
Each Durable Object instance is a globally routable isolate that can execute code and store state. This allows
developers to easily address and route to specific container instances (no matter where they are placed),
define and run hooks on container status changes, execute recurring checks on the instance, and store persistent
state associated with each instance.</p>
<h3 id="starting-a-container">Starting a Container</h3>
<p>When a Durable Object instance requests to start a new container instance, the <strong>nearest location
with a pre-fetched image</strong> is selected.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7159.md")
</aside>
<p>Starting additional container instances will use other locations with pre-fetched images,
and Cloudflare will automatically begin prepping additional machines behind the scenes
for additional scaling and quick cold starts. Because there are a finite number of pre-warmed
locations, some container instances may be started in locations that are farther away from
the end-user. This is done to ensure that the container instance starts quickly. You are
only charged for actively running instances and not for any unused pre-warmed images.</p>
<h4 id="cold-starts">Cold starts</h4>
<p>A cold start is when a container instance is started from a completely stopped state.
If you call <code>env.MY_CONTAINER.get(id)</code> with a completely novel ID and launch
this instance for the first time, it will result in a cold start.
This will start the container image from its entrypoint for the first time. Depending
on what this entrypoint does, it will take a variable amount of time to start.</p>
<p>Container cold starts can often be in the 1-3 second range, but this is dependent
on image size and code execution time, among other factors.</p>
<h3 id="requests-to-running-containers">Requests to running Containers</h3>
<p>When a request <em>starts</em> a new container instance, the nearest location with a pre-fetched image is selected.
Subsequent requests to a particular instance, regardless of where they originate, will be routed to this location as long as
the instance stays alive.</p>
<p>However, once that container instance stops and restarts, future requests could be routed to a <em>different</em> location.
This location will again be the nearest location to the originating request with a pre-fetched image.</p>
<h3 id="container-runtime">Container runtime</h3>
<p>Each container instance runs inside its own VM, which provides strong
isolation from other workloads running on Cloudflare's network. Containers
should be built for the <code>linux/amd64</code> architecture, and should stay within
<a href="/containers/platform/limits/">size limits</a>.</p>
<p><a href="/containers/faq/#how-do-container-logs-work">Logging</a>, metrics collection, and
<a href="/containers/faq/#how-do-i-allow-or-disallow-egress-from-my-container">networking</a> are automatically set up on each container, as configured by the developer.</p>
<h3 id="container-shutdown">Container shutdown</h3>
<p>The Container class sets <a href="/containers/reference/container-class/#sleepafter"><code>sleepAfter</code></a> to 10 minutes by default. Its default <a href="/containers/reference/container-class/#onactivityexpired"><code>onActivityExpired()</code></a> implementation signals the container to stop after that period without activity. You can change the duration or override the hook.</p>
<p>You can stop a container instance yourself with <a href="/containers/reference/container-class/#stop"><code>stop()</code></a> or <a href="/containers/reference/container-class/#destroy"><code>destroy()</code></a>.</p>
<p>When the platform is about to stop a container instance, it:</p>
<ol>
<li>Sends <code>SIGTERM</code> to the main process in the container.</li>
<li>Waits up to 15 minutes for that process to exit.</li>
<li>Sends <code>SIGKILL</code> if the process is still running.</li>
</ol>
<p>Handle <code>SIGTERM</code> in your image if you need cleanup before exit. The same sequence runs when a <a href="/containers/configuration/rollouts/">rollout</a> replaces a container instance with a new image.</p>
<h3 id="lifecycle-hooks">Lifecycle hooks</h3>
<p>The <a href="/containers/reference/container-class/"><code>Container</code> class</a> provides hooks that run Worker code when the container changes state:</p>
<ul>
<li><a href="/containers/reference/container-class/#onstart"><code>onStart()</code></a> — Runs after the container has started.</li>
<li><a href="/containers/reference/container-class/#onstop"><code>onStop()</code></a> — Runs after the container process exits. Receives the exit code and reason for the stop.</li>
<li><a href="/containers/reference/container-class/#onactivityexpired"><code>onActivityExpired()</code></a> — Runs when the <a href="/containers/reference/container-class/#sleepafter"><code>sleepAfter</code></a> timer expires with no incoming requests. The default implementation calls <code>stop()</code> to shut down the container. You can use this to only stop the container on certain conditions.</li>
<li><a href="/containers/reference/container-class/#onerror"><code>onError()</code></a> — Runs when the container exits with an error.</li>
</ul>
<p>Refer to the <a href="/containers/examples/status-hooks/">status hooks example</a> for a full implementation.</p>
<h4 id="persistent-disk">Persistent disk</h4>
<p>All disk is ephemeral. When a Container instance goes to sleep, the next time
it is started, it will have a fresh disk as defined by its container image.</p>
<p>Snapshots are coming soon, which allow the user to quickly persist and restore the disk
from an entire container or a directory.</p>
<p>You can also use <a href="/containers/examples/r2-fuse-mount/">FUSE</a> to persist disk
to R2 or other object storage backends. Though you should not expect native
SSD-like performance while using FUSE.</p>
<h2 id="an-example-request">An example request</h2>
<ul>
<li>A developer deploys a Container. Cloudflare automatically readies instances across its Network.</li>
<li>A request is made from a client in Bariloche, Argentina. It reaches the Worker in a nearby
Cloudflare location in Neuquen, Argentina.</li>
<li>This Worker request calls <code>getContainer(env.MY_CONTAINER, &quot;session-1337&quot;)</code>. Under the hood, this brings up a Durable
Object, which then calls <code>this.ctx.container.start</code>.</li>
<li>This requests the nearest free Container instance. Cloudflare recognizes that an instance is free in Buenos Aires, Argentina, and
starts it there.</li>
<li>A different user needs to route to the same container. This user's request reaches
the Worker running in Cloudflare's location in San Diego, US.</li>
<li>The Worker again calls <code>getContainer(env.MY_CONTAINER, &quot;session-1337&quot;)</code>.</li>
<li>If the initial container instance is still running, the request is routed to the original location
in Buenos Aires. If the initial container has gone to sleep, Cloudflare will once
again try to find the nearest &quot;free&quot; instance of the Container, likely
one in North America, and start an instance there.</li>
</ul>
