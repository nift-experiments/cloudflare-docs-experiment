<p>This tutorial explains how to conditionally enforce Turnstile based on the incoming request, such as a pre-shared secret in a header or a specific IP address.</p>
<h2 id="overview">Overview</h2>
<p>You may have setups such as automation that cannot load or run the Turnstile challenge. Using <a href="/workers/runtime-apis/html-rewriter/"><code>HTMLRewriter</code></a>, this tutorial will demonstrate how to conditionally handle the <a href="/turnstile/get-started/client-side-rendering/">client-side widget</a> and <a href="/turnstile/get-started/server-side-validation/">Siteverify API</a> when specific criteria are met.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14991.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14990.md")
</aside>
<h2 id="implementation">Implementation</h2>
<p>This tutorial will modify the existing <a href="https://github.com/cloudflare/turnstile-demo-workers/blob/main/src/">Turnstile demo</a> to conditionally remove the existing <code>script</code> and widget container elements.</p>
<pre><code class="language-diff">export default {&#10;  async fetch(request) {&#10;    // ...&#10;&#10;&#43;    if (request.headers.get(&quot;x-bypass-turnstile&quot;) === &quot;VerySecretValue&quot;) {&#10;&#43;      class RemoveHandler {&#10;&#43;        element(element) {&#10;&#43;          element.remove();&#10;&#43;        }&#10;&#43;      }&#10;&#43;&#10;&#43;      return new HTMLRewriter()&#10;&#43;        // Remove the script tag&#10;&#43;        .on(&#10;&#43;          &#x27;script[src=&quot;https://challenges.cloudflare.com/turnstile/v0/api.js&quot;]&#x27;,&#10;&#43;          new RemoveHandler(),&#10;&#43;        )&#10;&#43;       // Remove the container used in implicit rendering&#10;&#43;				.on(&#10;&#43;					&#x27;.cf-turnstile&#x27;,&#10;&#43;					new RemoveHandler(),&#10;&#43;				)&#10;&#43;       // Remove the container used in explicit rendering&#10;&#43;				.on(&#10;&#43;					&#x27;#myWidget&#x27;,&#10;&#43;					new RemoveHandler(),&#10;&#43;				)&#10;&#43;        .transform(body);&#10;&#43;    }&#10;&#10;    return new Response(body, {&#10;      headers: {&#10;        &quot;Content-Type&quot;: &quot;text/html&quot;,&#10;      },&#10;    });&#10;  },&#10;};&#10;</code></pre>
<h2 id="server-side-integration">Server-side integration</h2>
<p>We will exit early in our validation if the same logic we used to remove the client-side elements is present.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14989.md")
</aside>
<pre><code class="language-diff">async function handlePost(request) {&#10;&#43;  if (request.headers.get(&quot;x-bypass-turnstile&quot;) === &quot;VerySecretValue&quot;) {&#10;&#43;    return new Response(&#x27;Turnstile not enforced on this request&#x27;)&#10;&#43;  }&#10;	// Proceed with validation as normal!&#10;	const body = await request.formData();&#10;  // Turnstile injects a token in &quot;cf-turnstile-response&quot;.&#10;  const token = body.get(&#x27;cf-turnstile-response&#x27;);&#10;  const ip = request.headers.get(&#x27;CF-Connecting-IP&#x27;);&#10;  // ...&#10;}&#10;</code></pre>
<p>With these changes, Turnstile will not be enforced on requests with the header <code>x-bypass-turnstile: VerySecretValue</code> present.</p>
<h2 id="demonstration">Demonstration</h2>
<p>After running <code>npm run dev</code> in the project folder, you can test the changes by running the following command:</p>
<pre><code class="language-sh">curl -X POST http://localhost:8787/handler -H &quot;x-bypass-turnstile: VerySecretValue&quot;&#10;</code></pre>
<pre><code class="language-txt">Turnstile not enforced on this request&#10;</code></pre>
