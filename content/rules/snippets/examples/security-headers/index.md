<p class="article-summary">Set common security headers such as X-XSS-Protection, X-Frame-Options, and X-Content-Type-Options.</p>
<pre><code class="language-js">export default {&#10;	async fetch(request) {&#10;		// Define an object with the security headers you want to set.&#10;		// Refer to https://developers.cloudflare.com/rules/snippets/examples/security-headers/#other-common-security-headers for more options.&#10;		const DEFAULT_SECURITY_HEADERS = {&#10;			&quot;X-Content-Type-Options&quot;: &quot;nosniff&quot;,&#10;			&quot;Referrer-Policy&quot;: &quot;strict-origin-when-cross-origin&quot;,&#10;			&quot;Cross-Origin-Embedder-Policy&quot;: &#x27;require-corp; report-to=&quot;default&quot;;&#x27;,&#10;			&quot;Cross-Origin-Opener-Policy&quot;: &#x27;same-site; report-to=&quot;default&quot;;&#x27;,&#10;			&quot;Cross-Origin-Resource-Policy&quot;: &quot;same-site&quot;,&#10;		};&#10;&#10;		// You can also define headers to be deleted.&#10;		const BLOCKED_HEADERS = [&#10;			&quot;Public-Key-Pins&quot;,&#10;			&quot;X-Powered-By&quot;,&#10;			&quot;X-AspNet-Version&quot;,&#10;		];&#10;&#10;		// Receive response from the origin.&#10;		let response = await fetch(request);&#10;&#10;		// Create a new Headers object to modify response headers&#10;		let newHeaders = new Headers(response.headers);&#10;&#10;		// This sets the headers for HTML responses:&#10;		if (&#10;			newHeaders.has(&quot;Content-Type&quot;) &amp;&amp;&#10;			!newHeaders.get(&quot;Content-Type&quot;).includes(&quot;text/html&quot;)&#10;		) {&#10;			return new Response(response.body, {&#10;				status: response.status,&#10;				statusText: response.statusText,&#10;				headers: newHeaders,&#10;			});&#10;		}&#10;&#10;		// Use DEFAULT_SECURITY_HEADERS object defined above to set the new security headers.&#10;		Object.keys(DEFAULT_SECURITY_HEADERS).map((name) =&gt; {&#10;			newHeaders.set(name, DEFAULT_SECURITY_HEADERS[name]);&#10;		});&#10;&#10;		// Use the BLOCKED_HEADERS object defined above to delete headers you wish to block.&#10;		BLOCKED_HEADERS.forEach((name) =&gt; {&#10;			newHeaders.delete(name);&#10;		});&#10;&#10;		return new Response(response.body, {&#10;			status: response.status,&#10;			statusText: response.statusText,&#10;			headers: newHeaders,&#10;		});&#10;	},&#10;};&#10;</code></pre>
<h2 id="other-common-security-headers">Other common security headers</h2>
<ul>
<li>Content-Security-Policy headers: Enabling these headers will permit content from a trusted domain and all its subdomains.
Refer to <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy">Content-Security-Policy</a> for details.</li>
</ul>
<pre><code class="language-js">&quot;Content-Security-Policy&quot;: &quot;default-src &#x27;self&#x27; example.com *.example.com&quot;,&#10;</code></pre>
<ul>
<li>Strict-Transport-Security headers: These are not automatically set because your website might get added to Chrome's HSTS preload list.</li>
</ul>
<pre><code class="language-js">&quot;Strict-Transport-Security&quot; : &quot;max-age=63072000; includeSubDomains; preload&quot;,&#10;</code></pre>
<ul>
<li>Permissions-Policy header: Allow or deny the use of browser features, such as opting out of FLoC.</li>
</ul>
<pre><code class="language-js">&quot;Permissions-Policy&quot;: &quot;interest-cohort=()&quot;,&#10;</code></pre>
<ul>
<li>X-XSS-Protection header: Prevents a page from loading if an XSS attack is detected. Refer to <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-XSS-Protection">X-XSS-Protection</a> for details.</li>
</ul>
<pre><code class="language-js">&quot;X-XSS-Protection&quot;: &quot;0&quot;,&#10;</code></pre>
<ul>
<li>X-Frame-Options header: Prevents click-jacking attacks. Refer to <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options">X-Frame-Options</a>.</li>
</ul>
<pre><code class="language-js">&quot;X-Frame-Options&quot;: &quot;DENY&quot;,&#10;</code></pre>
