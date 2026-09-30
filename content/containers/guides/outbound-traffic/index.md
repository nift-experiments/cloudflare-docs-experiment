---
cp9:
  canonical: https://developers.cloudflare.com/containers/guides/outbound-traffic/
  description: Intercept and handle outbound HTTP from containers using Workers.
  full_title: Handle outbound traffic · Cloudflare Containers docs
  head_html: <title>Handle outbound traffic · Cloudflare Containers docs</title><meta name="generator" content="Nift"><meta name="description" content="Intercept and handle outbound HTTP from containers using Workers."><link rel="canonical" href="https://developers.cloudflare.com/containers/guides/outbound-traffic/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/containers/guides/outbound-traffic/index.md"><meta property="og:title" content="Handle outbound traffic · Cloudflare Containers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Intercept and handle outbound HTTP from containers using Workers."><meta property="og:url" content="https://developers.cloudflare.com/containers/guides/outbound-traffic/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Containers"><meta name="algolia_product_filter" content="Containers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Containers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/containers/guides/outbound-traffic/#page","headline":"Handle outbound traffic \u00b7 Cloudflare Containers docs","description":"Intercept and handle outbound HTTP from containers using Workers.","url":"https://developers.cloudflare.com/containers/guides/outbound-traffic/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /containers/guides/outbound-traffic/
  schema: 1
---
<p>Outbound handlers let you intercept and modify HTTP traffic from a container with trusted code.</p>
<p>Use them to:</p>
<ul>
<li>Allow or deny specific origin destinations</li>
<li>Safely inject authorization headers or tokens</li>
<li>Transparently reroute traffic</li>
<li>Add custom policy on outbound traffic (such as denying specific HTTP requests)</li>
<li><a href="/containers/configuration/workers-connections/">Connect to Workers bindings</a> like KV, R2, and Durable Objects</li>
</ul>
<h2 id="block-outbound-traffic">Block outbound traffic</h2>
<p>Use <code>enableInternet = false</code> to block public internet access by default:</p>
<pre tabindex="0"><code class="language-js">import { Container } from &quot;@cloudflare/containers&quot;;&#10;&#10;export class MyContainer extends Container {&#10;	enableInternet = false;&#10;}&#10;</code></pre>
<p>When <code>enableInternet</code> is <code>false</code>, only traffic you explicitly allow later on this page through <code>allowedHosts</code> or outbound handlers can leave the container. Only ports <code>80</code>, <code>443</code>, and DNS are available, and DNS queries use Cloudflare's DNS servers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7095.md")
</aside>
<h2 id="block-or-allow-traffic-by-host">Block or allow traffic by host</h2>
<p>You can filter outbound traffic with the <code>allowedHosts</code> and <code>deniedHosts</code> properties on the Container class.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7094.md")
</aside>
<p>When <code>allowedHosts</code> is set, it becomes a deny-by-default allowlist. Any host or IP not in the list is denied, and only matching destinations can reach <code>outbound</code> or <code>outboundByHost</code> handlers.</p>
<p><code>allowedHosts</code> and <code>deniedHosts</code> also support simple glob patterns where <code>*</code> matches any sequence of characters.</p>
<p>By default, a Container will allow internet access, and you can set <code>deniedHosts</code> to
disallow specific hosts or IPs:</p>
<pre tabindex="0"><code class="language-js">import { Container, ContainerProxy } from &quot;@cloudflare/containers&quot;;&#10;export { ContainerProxy };&#10;&#10;export class MyContainer extends Container {&#10;	// Make sure the container trusts /etc/cloudflare/certs/cloudflare-containers-ca.crt&#10;	interceptHttps = true;&#10;	deniedHosts = [&quot;some-nefarious-website.com&quot;, &quot;141.101.64.0/18&quot;];&#10;}&#10;</code></pre>
<p>You can also disable internet access by default, but allow specific hosts and IPs:</p>
<pre tabindex="0"><code class="language-js">import { Container, ContainerProxy } from &quot;@cloudflare/containers&quot;;&#10;export { ContainerProxy };&#10;&#10;export class MyContainer extends Container {&#10;	// Make sure the container trusts /etc/cloudflare/certs/cloudflare-containers-ca.crt&#10;	interceptHttps = true;&#10;&#10;	// default internet access to off unless overridden by &#x27;allowedHosts&#x27; or outbound proxy&#10;	enableInternet = false;&#10;&#10;	// overrides enableInternet = false&#10;	allowedHosts = [&quot;allowed.com&quot;];&#10;}&#10;</code></pre>
<h2 id="define-outbound-handlers">Define outbound handlers</h2>
<p>Outbound handlers are programmable egress proxies that run on the same machine as the container. They have access to all Workers bindings.</p>
<p>Use <code>outbound</code> to intercept all HTTP and HTTPS traffic:</p>
<pre tabindex="0"><code class="language-js">import { Container, ContainerProxy } from &quot;@cloudflare/containers&quot;;&#10;export { ContainerProxy };&#10;&#10;export class MyContainer extends Container {&#10;	interceptHttps = true;&#10;}&#10;&#10;MyContainer.outbound = async (request, env, ctx) =&gt; {&#10;	if (request.method !== &quot;GET&quot;) {&#10;		console.log(`Blocked ${request.method} to ${request.url}`);&#10;		return new Response(&quot;Method Not Allowed&quot;, { status: 405 });&#10;	}&#10;	return fetch(request);&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7093.md")
</aside>
<p>Use <code>outboundByHost</code> to map specific domain names or IP addresses to proxy functions:</p>
<pre tabindex="0"><code class="language-js">import { Container, ContainerProxy } from &quot;@cloudflare/containers&quot;;&#10;export { ContainerProxy };&#10;&#10;export class MyContainer extends Container {&#10;	interceptHttps = true;&#10;}&#10;&#10;MyContainer.outboundByHost = {&#10;	&quot;my.worker&quot;: async (request, env, ctx) =&gt; {&#10;		// Run arbitrary Workers logic from this hostname&#10;		return await someWorkersFunction(request.body);&#10;	},&#10;};&#10;</code></pre>
<p>Calls to <code>http://my.worker</code> from the container invoke the handler, which runs inside the Workers runtime, outside the container sandbox.</p>
<p><code>deniedHosts</code> and <code>allowedHosts</code> are evaluated before any outbound handler. If you use <code>allowedHosts</code>, include the hostname there for either <code>outbound</code> or <code>outboundByHost</code> to run. <code>outboundByHost</code> handlers take precedence over catch-all <code>outbound</code> handlers.</p>
<h2 id="securely-inject-credentials">Securely inject credentials</h2>
<p>Because outbound handlers run in the Workers runtime — outside the container sandbox — they can hold secrets that the container itself never sees. The container makes a plain HTTP request, and the handler attaches the credential before forwarding it to the upstream service.</p>
<pre tabindex="0"><code class="language-js">export class MyContainer extends Container {&#10;	// Make sure the container trusts /etc/cloudflare/certs/cloudflare-containers-ca.crt&#10;	interceptHttps = true;&#10;}&#10;&#10;MyContainer.outboundByHost = {&#10;	&quot;github.com&quot;: (request, env, ctx) =&gt; {&#10;		const requestWithAuth = new Request(request);&#10;		requestWithAuth.headers.set(&quot;x-auth-token&quot;, env.SECRET);&#10;		return fetch(requestWithAuth);&#10;	},&#10;};&#10;</code></pre>
<p>This is especially useful for agentic workloads where you cannot fully trust the code running inside the container. With this pattern:</p>
<ul>
<li><strong>No token is exposed to the container.</strong> The secret lives in the Worker's environment and is never passed into the sandbox.</li>
<li><strong>No token rotation inside the container.</strong> Rotate the secret in your Worker's environment and every request picks it up immediately.</li>
<li><strong>Per-host and per-instance rules.</strong> Combine <code>outboundByHost</code> with <code>ctx.containerId</code> to scope credentials or permissions to a specific container instance.</li>
</ul>
<p>Here, <code>ctx.containerId</code> looks up a per-instance key from KV:</p>
<pre tabindex="0"><code class="language-js">export class MyContainer extends Container {&#10;	// Make sure the container trusts /etc/cloudflare/certs/cloudflare-containers-ca.crt&#10;	interceptHttps = true;&#10;}&#10;&#10;MyContainer.outboundByHost = {&#10;	&quot;my-internal-vcs.dev&quot;: async (request, env, ctx) =&gt; {&#10;		const authKey = await env.KEYS.get(ctx.containerId);&#10;&#10;		const requestWithAuth = new Request(request);&#10;		requestWithAuth.headers.set(&quot;x-auth-token&quot;, authKey);&#10;		return fetch(requestWithAuth);&#10;	},&#10;};&#10;</code></pre>
<h2 id="https-traffic">HTTPS traffic</h2>
<p>By default, HTTPS traffic is not intercepted by outbound handlers. To opt in
you must set the <code>interceptHttps</code> attribute.</p>
<pre tabindex="0"><code class="language-js">export class MyContainer extends Container {&#10;	// Make sure the container trusts /etc/cloudflare/certs/cloudflare-containers-ca.crt&#10;	interceptHttps = true;&#10;}&#10;&#10;MyContainer.outbound = (req, env, ctx) =&gt; {&#10;	// All HTTP(S) requests will trigger this hook.&#10;	return fetch(req);&#10;};&#10;</code></pre>
<p>This is useful for Sandbox-like services that redirect untrusted traffic from a container instance to Workers for filtering and modification.</p>
<p>When HTTPS interception is active, an ephemeral CA file will be created at <code>/etc/cloudflare/certs/cloudflare-containers-ca.crt</code> once your container starts. The CA is only injected when you both set <code>interceptHttps = true</code> and define an <code>outbound</code> or <code>outboundByHost</code> handler.</p>
<h3 id="trust-the-ca-certificate">Trust the CA certificate</h3>
<p>For HTTPS interception to work, you must trust the CA file. The CA is ephemeral and only exists at runtime, so do not try to bake it into your image during <code>docker build</code>. Instead, copy it into your distro's trust store and refresh the trust store from the container <code>entrypoint</code> before your application starts.</p>
<p>If your base image does not already include the trust-store tooling, install the distro's <code>ca-certificates</code> package in your image first.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7100.md")
</div></div>
<p>Replace <code>node server.js</code> with the command that starts your application.</p>
<p>Most runtimes will then trust the CA through the system root store automatically. If your runtime uses its own CA bundle, point it at <code>/etc/cloudflare/certs/cloudflare-containers-ca.crt</code> directly, for example with <code>NODE_EXTRA_CA_CERTS</code> or <code>REQUESTS_CA_BUNDLE</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7092.md")
</aside>
<h2 id="non-http-traffic">Non-HTTP traffic</h2>
<p>Outbound handlers only intercept HTTP and HTTPS traffic. Traffic on ports other than <code>80</code> and <code>443</code> is never routed through <code>outbound</code> or <code>outboundByHost</code>.</p>
<p>If you set <code>enableInternet = false</code>, that traffic is denied. DNS queries are the one exception, but they only go to Cloudflare's DNS servers. That prevents using arbitrary DNS destinations for data exfiltration.</p>
<h2 id="change-policies-at-runtime">Change policies at runtime</h2>
<p>Use <code>outboundHandlers</code> to define named handlers, then assign them to specific hosts at runtime using <code>setOutboundByHost()</code>. You can also apply a handler globally with <code>setOutboundHandler()</code>.</p>
<p>You can also manage runtime policy with <code>setOutboundByHosts()</code>, <code>setAllowedHosts()</code>, <code>setDeniedHosts()</code>, <code>allowHost()</code>, <code>denyHost()</code>, <code>removeAllowedHost()</code>, and <code>removeDeniedHost()</code>.</p>
<p>This lets a trusted Worker hold credentials without exposing them to an untrusted container:</p>
<pre tabindex="0"><code class="language-js">export class MyContainer extends Container {&#10;	// Make sure the container trusts /etc/cloudflare/certs/cloudflare-containers-ca.crt&#10;	interceptHttps = true;&#10;}&#10;&#10;MyContainer.outboundHandlers = {&#10;	authenticatedGithub: async (request, env, ctx) =&gt; {&#10;		const githubToken = env.GITHUB_TOKEN;&#10;		return authenticateGitHttpsRequest(request, githubToken, ctx.containerId);&#10;	},&#10;};&#10;</code></pre>
<p>Apply handlers to hosts programmatically from your Worker:</p>
<pre tabindex="0"><code class="language-js">async setUpContainer(req, env) {&#10;  const container = await env.MY_CONTAINER.getByName(&quot;my-instance&quot;);&#10;&#10;  // Give the container access to github.com on a specific host during setup&#10;  await container.setOutboundByHost(&quot;github.com&quot;, &quot;authenticatedGithub&quot;);&#10;&#10;	// do something with github.com on your container...&#10;}&#10;&#10;async removeAccessToGithub(req, env) {&#10;  const container = await env.MY_CONTAINER.getByName(&quot;my-instance&quot;);&#10;&#10;  // Remove access to Github&#10;  await container.removeOutboundByHost(&quot;github.com&quot;);&#10;}&#10;</code></pre>
<h2 id="handler-precedence">Handler precedence</h2>
<p>Requests are evaluated in this order:</p>
<ol>
<li><code>deniedHosts</code> is checked first. Matching hosts or IPs are denied immediately.</li>
<li><code>allowedHosts</code> is checked next. When it is set, any host or IP not in the list is denied. Matching hosts continue to outbound handlers, or egress to the public internet if no handler is set.</li>
<li>Instance-level rules set with <code>setOutboundByHost()</code> are checked before class-level <code>outboundByHost</code> rules.</li>
<li>Per-host handlers always take precedence over catch-all handlers, so <code>outboundByHost</code> runs before <code>outbound</code>.</li>
<li>Instance-level handlers set with <code>setOutboundHandler()</code> are checked before the class-level <code>outbound</code> handler.</li>
<li>If no handler matches, the request can still egress to the public internet when it matched <code>allowedHosts</code> or <code>enableInternet = true</code>. Otherwise, it is denied.</li>
</ol>
<h2 id="low-level-api">Low-level API</h2>
<p>To configure outbound interception directly on <code>ctx.container</code>, use <code>interceptOutboundHttp</code> for a specific hostname glob, IP, or CIDR range,
or <code>interceptAllOutboundHttp</code> for all traffic. Both accept a <code>WorkerEntrypoint</code>.</p>
<pre tabindex="0"><code class="language-js">import { WorkerEntrypoint } from &quot;cloudflare:workers&quot;;&#10;&#10;export class MyOutboundWorker extends WorkerEntrypoint {&#10;	fetch(request) {&#10;		// Inspect, modify, or deny the request before passing it on&#10;		return fetch(request);&#10;	}&#10;}&#10;&#10;// Inside your Container DurableObject&#10;this.ctx.container.start({ enableInternet: false });&#10;const worker = this.ctx.exports.MyOutboundWorker({ props: {} });&#10;await this.ctx.container.interceptAllOutboundHttp(worker);&#10;</code></pre>
<p>You can call these methods before or after starting the container, and even while connections are open. In-flight TCP connections pick up the new handler automatically — no connections are dropped.</p>
<pre tabindex="0"><code class="language-js">// Intercept a specific CIDR range&#10;await this.ctx.container.interceptOutboundHttp(&quot;203.0.113.0/24&quot;, worker);&#10;// Intercept by hostname&#10;this.ctx.container.interceptOutboundHttp(&quot;foo.com&quot;, worker);&#10;&#10;// Update the handler while the container is running&#10;const updated = this.ctx.exports.MyOutboundWorker({&#10;	props: { phase: &quot;post-install&quot; },&#10;});&#10;await this.ctx.container.interceptOutboundHttp(&quot;203.0.113.0/24&quot;, updated);&#10;</code></pre>
<p>For HTTPS, <code>interceptOutboundHttps</code> works the same way as <code>interceptOutboundHttp</code>.</p>
<pre tabindex="0"><code class="language-js">// Intercept a specific hostname&#10;this.ctx.container.interceptOutboundHttps(&quot;foo.com&quot;, worker);&#10;&#10;// Intercept all traffic&#10;this.ctx.container.interceptOutboundHttps(&quot;*&quot;, worker);&#10;</code></pre>
<p>The <code>Container</code> class calls these methods automatically when you use the functions shown above. You can also call them directly for cases the class does not cover.</p>
<h2 id="local-development">Local development</h2>
<p><code>wrangler dev</code> supports outbound interception. A sidecar process is spawned inside the container's network namespace. It applies <code>TPROXY</code> rules to route matching traffic to the local Workerd instance, mirroring production behavior.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/containers/configuration/workers-connections/">Connect to Workers bindings</a> — Access KV, R2, Durable Objects, and other bindings from a container</li>
<li><a href="/sandbox/guides/outbound-traffic/">Control outbound traffic (Sandboxes)</a> — Sandbox SDK API for outbound handlers</li>
<li><a href="/containers/configuration/environment-variables/">Environment variables and secrets</a> — Configure secrets and environment variables</li>
<li><a href="/durable-objects/api/container/">Durable Object interface</a> — Full <code>ctx.container</code> API reference</li>
</ul>
