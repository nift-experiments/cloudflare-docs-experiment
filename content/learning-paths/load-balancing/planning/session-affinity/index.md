<p>When you enable session affinity, your load balancer directs all requests from a particular end user to a specific endpoint. This continuity preserves information about the user session — such as items in their shopping cart — that might otherwise be lost if requests were spread out among multiple servers.</p>
<p>Session affinity can also help reduce network requests, leading to savings for customers with usage-based billing.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9817.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>Session affinity automatically directs requests from the same client to the same endpoint:</p>
<ol>
<li>When a client makes its first request, Cloudflare sets a <code>__cflb</code> cookie on the client (to track the associated endpoint).</li>
<li>Subsequent requests by the same client are forwarded to that endpoint for the duration of the cookie and as long as the endpoint remains healthy.</li>
<li>If the cookie expires or the endpoint becomes unhealthy, Cloudflare sets a new cookie tracking the new failover endpoint.</li>
</ol>
<pre><code class="language-mermaid">    flowchart LR&#10;      accTitle: Session affinity process&#10;      accDescr: Session affinity directs requests from the same client to the same server.&#10;     A[Client] --Request--&gt; B{&lt;code&gt;__cflb&lt;/code&gt; cookie set?}&#10;     B --&gt;|Yes| C[Route to previous endpoint]&#10;     C --&gt; O2&#10;     B ----&gt;|No| E[Follow normal routing]&#10;     E --&gt; O2&#10;     E --Set &lt;code&gt;__cflb&lt;/code&gt; cookie--&gt; A&#10;     subgraph P1 [Pool 1]&#10;        O1[Endpoint 1]&#10;        O2[Endpoint 2]&#10;     end&#10;</code></pre>
<br/>
<p>All cookie-based sessions default to 23 hours unless you set a custom session <em>Time to live</em> (TTL).</p>
<p>The session cookie is secure when <a href="/ssl/edge-certificates/additional-options/always-use-https/">Always Use HTTPS</a> is enabled. Additionally, HttpOnly is always enabled for the cookie to prevent cross-site scripting attacks.</p>
