<p>Cloudflare Snippets are executed based on rules defined within your zone. Here is how the process works:</p>
<p><img src="/assets/upstream/images/rules/snippets/snippets-execution.png" alt="Diagram of the snippets execution workflow" /></p>
<h2 id="1-evaluate-snippet-rules"><ol>
<li>Evaluate snippet rules</li>
</ol></h2>
<p>For each incoming request, Cloudflare evaluates the expression of every snippet rule defined in the zone. The evaluation checks for a match based on various request properties (such as bot score, WAF attack score, country of origin, and cookies).</p>
<h2 id="2-build-snippets-table"><ol start="2">
<li>Build Snippets table</li>
</ol></h2>
<p>For every snippet rule in a zone that matches an incoming request, Cloudflare adds the corresponding unique snippet ID to a Snippets table.</p>
<h2 id="3-execute-snippets-code"><ol start="3">
<li>Execute snippets code</li>
</ol></h2>
<p>Once all the rules have been evaluated and the full table has been compiled, Cloudflare starts processing all the snippet IDs in the table.</p>
<p>The snippets are executed sequentially. Each snippet receives the modified request from the previous snippet and applies new modifications to it.</p>
<h2 id="4-continue-with-the-request-execution-workflow"><ol start="4">
<li>Continue with the request execution workflow</li>
</ol></h2>
<p>After executing the final snippet IDs, the resulting modified request is passed back to the request execution workflow. Refer to <a href="/rules/snippets/#execution-order">Execution order</a> for more information on the Rules features evaluated before and after Cloudflare Snippets.</p>
