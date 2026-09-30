<h2 id="use-trace-in-the-dashboard">Use Trace in the dashboard</h2>
<h3 id="1-configure-one-or-more-cloudflare-products"><ol>
<li>Configure one or more Cloudflare products</li>
</ol></h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/12774.md")
</div>
<h3 id="2-build-a-trace"><ol start="2">
<li>Build a trace</li>
</ol></h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/12775.md")
</div>
<h3 id="3-assess-results"><ol start="3">
<li>Assess results</li>
</ol></h3>
<p>The <strong>Trace results</strong> page shows all evaluated and executed configurations from different Cloudflare products, in evaluation order. Any inactive rules are not evaluated.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/12776.md")
</div>
<h3 id="4-optional-save-the-trace-configuration"><ol start="4">
<li>(Optional) Save the trace configuration</li>
</ol></h3>
<p>To run a trace later with the same configuration:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/12777.md")
</div>
<h2 id="use-trace-via-api">Use Trace via API</h2>
<p>Use the <a href="/api/resources/request_tracers/subresources/traces/methods/create/">Request Trace</a> operation to perform a trace using the Cloudflare API.</p>
<hr />
<h2 id="steps-in-trace-results">Steps in trace results</h2>
<ul>
<li>Execution of one or more rules of Cloudflare products built on the <a href="/ruleset-engine/">Ruleset Engine</a>. Refer to the Ruleset Engine's <a href="/ruleset-engine/reference/phases-list/">Phases list</a> for a list of such products.</li>
<li><a href="/rules/page-rules/">Page Rules</a>: Execution of one or more rules.</li>
<li><a href="/workers/">Workers</a>: Execution of one or more scripts.</li>
</ul>
