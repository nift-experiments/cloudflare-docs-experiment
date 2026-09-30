<p>D1 supports remote development using the <a href="/workers/playground/#use-the-playground">dashboard playground</a>. The dashboard playground uses a browser version of Visual Studio Code, allowing you to rapidly iterate on your Worker entirely in your browser.</p>
<h2 id="1-bind-a-d1-database-to-a-worker"><ol>
<li>Bind a D1 database to a Worker</li>
</ol></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7378.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select an existing Worker.
3. Go to the **Bindings** tab.
4. Select **Add binding**.
5. Select **D1 database** > **Add binding**.
6. Enter a variable name, such as `DB`, and select the D1 database you wish to access from this Worker.
7. Select **Add binding**.
<h2 id="2-start-a-remote-development-session"><ol start="2">
<li>Start a remote development session</li>
</ol></h2>
<ol>
<li>On the Worker's page on the Cloudflare dashboard, select <strong>Edit Code</strong> at the top of the page.</li>
<li>Your Worker now has access to D1.</li>
</ol>
<p>Use the following Worker script to verify that the Worker has access to the bound D1 database:</p>
<pre><code class="language-js">export default {&#10;  async fetch(request, env, ctx) {&#10;    const res = await env.DB.prepare(&quot;SELECT 1;&quot;).run();&#10;    return new Response(JSON.stringify(res, null, 2));&#10;  },&#10;};&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>Learn <a href="/d1/observability/debug-d1/">how to debug D1</a>.</li>
<li>Understand how to <a href="/workers/observability/logs/">access logs</a> generated from your Worker and D1.</li>
</ul>
