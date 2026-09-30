<h2 id="workers">Workers</h2>
<p><a href="/workers/">Workers</a> provides a serverless execution environment that allows you to create new applications or augment existing ones.</p>
<p>To use Workers AI with Workers, you must create a Workers AI <a href="/workers/runtime-apis/bindings/">binding</a>. Bindings allow your Workers to interact with resources, like Workers AI, on the Cloudflare Developer Platform. You create bindings on the Cloudflare dashboard or by updating your <a href="/workers/wrangler/configuration/">Wrangler file</a>.</p>
<p>To bind Workers AI to your Worker, add the following to the end of your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15817.md")
</div>
<h2 id="pages-functions">Pages Functions</h2>
<p><a href="/pages/functions/">Pages Functions</a> allow you to build full-stack applications with Cloudflare Pages by executing code on the Cloudflare network. Functions are Workers under the hood.</p>
<p>To configure a Workers AI binding in your Pages Function, you must use the Cloudflare dashboard. Refer to <a href="/pages/functions/bindings/#workers-ai">Workers AI bindings</a> for instructions.</p>
<h2 id="methods">Methods</h2>
<h3 id="async-env-ai-run">async env.AI.run()</h3>
<p><code>async env.AI.run()</code> runs a model. Takes a model as the first parameter, and an object as the second parameter.</p>
<pre><code class="language-javascript">const answer = await env.AI.run(&#x27;@cf/meta/llama-3.1-8b-instruct&#x27;, {&#10;    prompt: &quot;What is the origin of the phrase &#x27;Hello, World&#x27;&quot;&#10;});&#10;</code></pre>
<p><strong>Parameters</strong></p>
<ul>
<li>
<p><code>model</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
<ul>
<li>The model to run.</li>
</ul>
<p><strong>Supported options</strong></p>
<ul>
<li><code>stream</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Returns a stream of results as they are available.</li>
</ul>
</li>
</ul>
</li>
</ul>
<pre><code class="language-javascript">const answer = await env.AI.run(&#x27;@cf/meta/llama-3.1-8b-instruct&#x27;, {&#10;    prompt: &quot;What is the origin of the phrase &#x27;Hello, World&#x27;&quot;,&#10;    stream: true&#10;});&#10;&#10;return new Response(answer, {&#10;    headers: { &quot;content-type&quot;: &quot;text/event-stream&quot; }&#10;});&#10;</code></pre>
