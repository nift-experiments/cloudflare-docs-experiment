<h2 id="run-apo-on-a-subdomain">Run APO on a subdomain</h2>
<p>After you enable APO, you configure it to run on the subdomain that uses WordPress. For example, if you have a website called <code>www.mysite.com</code> which includes a subdomain running WordPress called <code>shop.mysite.com</code>, you would configure APO to run on the <code>shop.mysite.com</code> subdomain.</p>
<ol>
<li>Install version 4.4.0 or later of the Cloudflare WordPress plugin.</li>
<li>Log in using Cloudflare <strong>API token</strong> or <strong>Global key</strong>.</li>
<li>Enable APO. The subdomain displays in the list of hostnames in the card.</li>
<li>Repeat the process for each subdomain to enable APO.</li>
</ol>
<p>By default, APO runs on the apex domain (also known as &quot;root domain&quot; or &quot;naked domain&quot;). If you choose to run APO on a subdomain, the apex domain is automatically disabled. To run APO on a subdomain and the apex domain, upgrade the WordPress plugin to version 4.4.0 or later on the apex domain and re-enable APO.</p>
<h2 id="run-apo-on-a-subdirectory">Run APO on a subdirectory</h2>
<p>After you enable APO, you configure it to run on the subdirectory that uses WordPress. For example, if you have a website called <code>www.mysite.com</code> which includes a subdirectory running WordPress called <code>mysite.com/shop</code>, you would configure APO to run on the <code>mysite.com</code> domain.</p>
<ol>
<li>Install the Cloudflare WordPress plugin.</li>
<li>Add your Cloudflare API Token.</li>
<li>Activate APO.</li>
</ol>
<p>Repeat steps 1 and 2 for each subdirectory to activate the WordPress plugin for automatic cache purging.</p>
<h2 id="run-apo-only-on-a-subdirectory">Run APO only on a subdirectory</h2>
<p>If you choose to run APO only on a subdirectory, the rest of the domain should be configured to bypass APO. You can bypass APO in one of two ways.</p>
<h3 id="use-the-cf-edge-cache-response-header">Use the <code>cf-edge-cache</code> response header</h3>
<p>The <code>cf-edge-cache: no-cache</code> instructs the APO service to bypass caching for non-WordPress parts of the site. You can implement this option with Cloudflare Workers using the example below.</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		const originalResponse = await fetch(request);&#10;&#10;		// Response properties are immutable. To change them, construct a new Response object.&#10;    const response = new Response(originalResponse.body, originalResponse);&#10;&#10;    // Response headers can be modified through the headers `set` method.&#10;    response.headers.set(&quot;cf-edge-cache&quot;, &quot;no-cache&quot;);&#10;&#10;		return response;&#10;	},&#10;};&#10;</code></pre>
<h3 id="use-cache-rules">Use Cache Rules</h3>
<p>Create a <a href="/cache/how-to/cache-rules/">cache rule</a> to exclude non-WordPress portions of the site from caching using <strong>Cache eligibility: Bypass cache</strong>. This option disables all caching, including static assets for those paths. As a result, we recommend disabling APO via the response header.</p>
