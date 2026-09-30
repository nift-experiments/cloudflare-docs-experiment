<p class="article-summary">Reroute a request to a different origin and modify the URL path.</p>
<p>This example demonstrates how to use Cloudflare Snippets to:</p>
<ul>
<li>Reroute incoming requests to a different origin.</li>
<li>Prepend a directory to the URL path.</li>
<li>Remove specific segments from the URL path.</li>
</ul>
<pre><code class="language-js">export default {&#10;	async fetch(request) {&#10;		// Clone the original request to create a new request object&#10;		const newRequest = new Request(request);&#10;&#10;		// Add a header to identify a rerouted request at the new origin&#10;		newRequest.headers.set(&quot;X-Rerouted&quot;, &quot;1&quot;);&#10;&#10;		// Clone and parse the original URL&#10;		const url = new URL(request.url);&#10;&#10;		// Step 1: Reroute to a different origin&#10;		url.hostname = &quot;example.com&quot;; // Change the hostname to the new origin&#10;&#10;		// Step 2: Append a directory to the path&#10;		url.pathname = `/new-path${url.pathname}`; // Prepend &quot;/new-path&quot; to the current path&#10;&#10;		// Step 3: Remove a specific segment from the path&#10;		url.pathname = url.pathname.replace(&quot;/remove-me&quot;, &quot;&quot;); // Rewrite `/remove-me/something` to `/something`&#10;&#10;		// Fetch the modified request from the updated URL&#10;		return await fetch(url, newRequest);&#10;	},&#10;};&#10;</code></pre>
<p>This configuration will perform the following rewrites:</p>
<table>
<thead>
<tr>
<th>Request URL</th>
<th>URL after rewrite</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>https://subdomain.example.com/foo</code></td>
<td><code>https://example.com/new-path/foo</code></td>
</tr>
<tr>
<td><code>https://example.com/remove-me/bar</code></td>
<td><code>https://example.com/new-path/bar</code></td>
</tr>
<tr>
<td><code>https://example.net/remove-me</code></td>
<td><code>https://example.com/new-path</code></td>
</tr>
</tbody>
</table>
