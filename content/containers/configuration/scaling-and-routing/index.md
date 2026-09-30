---
cp9:
  canonical: https://developers.cloudflare.com/containers/configuration/scaling-and-routing/
  description: Scale Container instances using explicit IDs or the getRandom helper for stateless load balancing.
  full_title: Scaling and Routing · Cloudflare Containers docs
  head_html: <title>Scaling and Routing · Cloudflare Containers docs</title><meta name="generator" content="Nift"><meta name="description" content="Scale Container instances using explicit IDs or the getRandom helper for stateless load balancing."><link rel="canonical" href="https://developers.cloudflare.com/containers/configuration/scaling-and-routing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/containers/configuration/scaling-and-routing/index.md"><meta property="og:title" content="Scaling and Routing · Cloudflare Containers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Scale Container instances using explicit IDs or the getRandom helper for stateless load balancing."><meta property="og:url" content="https://developers.cloudflare.com/containers/configuration/scaling-and-routing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Containers"><meta name="algolia_product_filter" content="Containers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Containers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/containers/configuration/scaling-and-routing/#page","headline":"Scaling and Routing \u00b7 Cloudflare Containers docs","description":"Scale Container instances using explicit IDs or the getRandom helper for stateless load balancing.","url":"https://developers.cloudflare.com/containers/configuration/scaling-and-routing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /containers/configuration/scaling-and-routing/
  schema: 1
---
<h2 id="scale-container-instances-with-explicit-ids">Scale container instances with explicit IDs</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7150.md")
</aside>
<p>Today, Containers are scaled manually by getting containers with a unique ID, then
starting the container. Note that getting a container does not automatically start it.</p>
<pre tabindex="0"><code class="language-typescript">// get and start two container instances&#10;const containerOne = getContainer(&#10;	env.MY_CONTAINER,&#10;	idOne,&#10;).startAndWaitForPorts();&#10;&#10;const containerTwo = getContainer(&#10;	env.MY_CONTAINER,&#10;	idTwo,&#10;).startAndWaitForPorts();&#10;</code></pre>
<p>Each instance will run until its <code>sleepAfter</code> time has elapsed, or until it is manually stopped.</p>
<p>This behavior is very useful when you want explicit control over the lifecycle of container instances.
For instance, you may want to spin up a container backend instance for a specific user, or you may briefly
run a code sandbox to isolate AI-generated code, or you may want to run a short-lived batch job.</p>
<h3 id="use-the-getrandom-helper-function">Use the <code>getRandom</code> helper function</h3>
<p>If you want to run multiple instances of a container and route requests between them, use the
<code>getRandom</code> helper function:</p>
<pre tabindex="0"><code class="language-javascript">import { Container, getRandom } from &quot;@cloudflare/containers&quot;;&#10;&#10;const INSTANCE_COUNT = 3;&#10;&#10;class Backend extends Container {&#10;	defaultPort = 8080;&#10;	sleepAfter = &quot;2h&quot;;&#10;}&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env): Promise&lt;Response&gt; {&#10;		const containerInstance = await getRandom(env.BACKEND, INSTANCE_COUNT);&#10;		return containerInstance.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<p>Use <code>getRandom</code> to route to multiple stateless container instances. It randomly selects one of N
instances for each request, which means:</p>
<ul>
<li>It requires that the user set a fixed number of instances to route to.</li>
<li>It will randomly select each instance, regardless of location.</li>
</ul>
<p>We plan to fix these issues with built-in autoscaling and routing features in the near future.</p>
