<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 1, 2025</time><h2 id="post-title">Enhanced support for static assets with the Cloudflare Vite plugin</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now use any of Vite's <a href="https://vite.dev/guide/assets">static asset handling</a> features in your Worker as well as in your frontend.
These include importing assets as URLs, importing as strings and importing from the <code>public</code> directory as well as inlining assets.</p>
<p>Additionally, assets imported as URLs in your Worker are now automatically moved to the client build output.</p>
<p>Here is an example that fetches an imported asset using the <a href="/workers/static-assets/binding/#binding">assets binding</a> and modifies the response.</p>
<pre><code class="language-ts">// Import the asset URL&#10;// This returns the resolved path in development and production&#10;import myImage from &quot;./my-image.png&quot;;&#10;&#10;export default {&#10;	async fetch(request, env) {&#10;		// Fetch the asset using the binding&#10;		const response = await env.ASSETS.fetch(new URL(myImage, request.url));&#10;		// Create a new `Response` object that can be modified&#10;		const modifiedResponse = new Response(response.body, response);&#10;		// Add an additional header&#10;		modifiedResponse.headers.append(&quot;my-header&quot;, &quot;imported-asset&quot;);&#10;&#10;		// Return the modified response&#10;		return modifiedResponse;&#10;	},&#10;};&#10;</code></pre>
<p>Refer to <a href="/workers/vite-plugin/reference/static-assets/">Static Assets</a> in the Cloudflare Vite plugin docs for more info.</p>
</div></article></div>
