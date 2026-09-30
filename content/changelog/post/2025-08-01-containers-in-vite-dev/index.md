<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 1, 2025</time><h2 id="post-title">Develop locally with Containers and the Cloudflare Vite plugin</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now configure and run <a href="/containers">Containers</a> alongside your <a href="/workers">Worker</a> during local development when using the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>. Previously, you could only develop locally when using <a href="/workers/wrangler/">Wrangler</a> as your local development server.</p>
<h4 id="configuration">Configuration</h4>
<p>You can simply configure your Worker and your Container(s) in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17782.md")</div>
<h4 id="worker-code">Worker Code</h4>
<p>Once your Worker and Containers are configured, you can access the Container instances from your Worker code:</p>
<pre><code class="language-ts">import { Container, getContainer } from &quot;@cloudflare/containers&quot;;&#10;&#10;export class MyContainer extends Container {&#10;  defaultPort = 4000; // Port the container is listening on&#10;  sleepAfter = &quot;10m&quot;; // Stop the instance if requests not sent for 10 minutes&#10;}&#10;&#10;async fetch(request, env) {&#10;  const { &quot;session-id&quot;: sessionId } = await request.json();&#10;  // Get the container instance for the given session ID&#10;  const containerInstance = getContainer(env.MY_CONTAINER, sessionId)&#10;  // Pass the request to the container instance on its default port&#10;  return containerInstance.fetch(request);&#10;}&#10;</code></pre>
<h4 id="local-development">Local development</h4>
<p>To develop your Worker locally, start a local dev server by running</p>
<pre><code class="language-sh">vite dev&#10;</code></pre>
<p>in your terminal.</p>
<h4 id="resources">Resources</h4>
<p>Learn more about <a href="https://developers.cloudflare.com/containers/">Cloudflare Containers</a> or the <a href="https://developers.cloudflare.com/workers/vite-plugin/">Cloudflare Vite plugin</a> in our developer docs.</p>
</div></article></div>
