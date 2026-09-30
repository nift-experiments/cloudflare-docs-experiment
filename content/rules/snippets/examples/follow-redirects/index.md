<p class="article-summary">Modify the fetch request to follow redirects from the origin, ensuring the client receives the final response.</p>
<pre><code class="language-js">export default {&#10;	async fetch(request) {&#10;		// Define fetch options to follow redirects&#10;		const fetchOptions = {&#10;			redirect: &quot;follow&quot;, // Ensure fetch follows redirects automatically. Each subrequest in a redirect chain counts against the subrequest limit.&#10;		};&#10;&#10;		// Make the fetch request to the origin&#10;		const response = await fetch(request, fetchOptions);&#10;&#10;		// Log the final URL after redirects (optional, for debugging)&#10;		console.log(`Final URL after redirects: ${response.url}`);&#10;&#10;		// Return the final response to the client&#10;		return response;&#10;	},&#10;};&#10;</code></pre>
<p>This template is ready for use and should fit most redirect-following scenarios.</p>
<p>It ensures the Snippet transparently follows redirects issued by the origin server. The <code>redirect: &quot;follow&quot;</code> option of the <a href="/workers/runtime-apis/fetch/">Fetch API</a> ensures automatic handling of <code>3xx</code> redirects, returning the final response. If the origin response is not a redirect, the original content is returned.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13124.md")
</aside>
