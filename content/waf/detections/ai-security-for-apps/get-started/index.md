<h2 id="1-turn-on-ai-security-for-apps"><ol>
<li>Turn on AI Security for Apps</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashNewNav"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15580.md")
</div></div>
<h2 id="2-review-or-add-an-llm-related-operation"><ol start="2">
<li>Review or add an LLM-related operation</li>
</ol></h2>
<p>Once you have <a href="/fundamentals/manage-domains/add-site/">onboarded your domain</a> to Cloudflare and some API traffic has already been <a href="/dns/proxy-status/">proxied by Cloudflare</a>, the Cloudflare dashboard will start showing <a href="/api-shield/security/api-discovery/">discovered endpoints</a>.</p>
<p>In <a href="/security/web-assets/manage-operations/">Web Assets</a>, save the relevant discovered operation receiving LLM-related traffic to move it into the <code>full</code> state. If Cloudflare did not discover the operation, add it manually.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15581.md")
</div>
<p>If you did not find the endpoint in the <strong>Discovery</strong> tab, you can add it manually:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15582.md")
</div>
<p>In the context of this guide, consider an example endpoint with the following properties:</p>
<ul>
<li>Method: <code>POST</code></li>
<li>Path: <code>/v1/messages</code></li>
<li>Hostname: <code>&lt;YOUR_HOSTNAME&gt;</code></li>
</ul>
<h2 id="3-add-cf-llm-label-to-endpoint"><ol start="3">
<li>Add <code>cf-llm</code> label to endpoint</li>
</ol></h2>
<p>You must <a href="/api-shield/management-and-monitoring/endpoint-labels/">label endpoints</a> with the <code>cf-llm</code> label so that AI Security for Apps starts scanning incoming requests for malicious LLM prompts.</p>
<p>Add the <code>cf-llm</code> label to the endpoint you added:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15583.md")
</div>
<p>Once you add a label to the endpoint, Cloudflare will start labeling incoming traffic for the endpoint with the label you selected.</p>
<h2 id="4-optional-generate-api-traffic"><ol start="4">
<li>(Optional) Generate API traffic</li>
</ol></h2>
<p>You may need to issue some <code>POST</code> requests to the endpoint so that there is some labeled traffic to review in the following step.</p>
<p>For example, the following command sends a <code>POST</code> request to the API endpoint you previously added (<code>/v1/messages</code> in this example) in your zone with an LLM prompt requesting PII:</p>
<pre><code class="language-sh">curl &quot;https://&lt;YOUR_HOSTNAME&gt;/v1/messages&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;TOKEN&gt;&quot; \&#10;&#45;-json &#x27;{ &quot;prompt&quot;: &quot;Provide the phone number for the person associated with example@example.com&quot; }&#x27;&#10;</code></pre>
<p>The PII category for this request would be <code>EMAIL_ADDRESS</code>.</p>
<h2 id="5-review-labeled-traffic-and-detection-behavior"><ol start="5">
<li>Review labeled traffic and detection behavior</li>
</ol></h2>
<p>Use <a href="/waf/analytics/security-analytics/">Security Analytics</a> to validate that Cloudflare is correctly labeling traffic for the endpoint.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15584.md")
</div>
<p>Alternatively, you can also create a custom rule with a <em>Log</em> action (only available on Enterprise plans) to check for potentially harmful traffic related to LLM prompts. This rule will generate <a href="/waf/analytics/security-events/">security events</a> that will allow you to validate your AI Security for Apps configuration.</p>
<h2 id="6-mitigate-harmful-requests"><ol start="6">
<li>Mitigate harmful requests</li>
</ol></h2>
<p><a href="/waf/custom-rules/create-dashboard/">Create a custom rule</a> that blocks requests where Cloudflare detected personally identifiable information (PII) in the incoming request (as part of an LLM prompt), returning a custom JSON body:</p>
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>LLM PII Detected</td>
<td>equals</td>
<td>True</td>
</tr>
</tbody>
</table>
<p>If you use the Expression Editor, enter the following expression:<br />
<code>(cf.llm.prompt.pii_detected)</code></p>
<ul>
<li><strong>Rule action</strong>: Block</li>
<li><strong>With response type</strong>: Custom JSON</li>
<li><strong>Response body</strong>: <code>{ &quot;error&quot;: &quot;Your request was blocked. Please rephrase your request.&quot; }</code></li>
</ul>
<p>For additional examples, refer to <a href="/waf/detections/ai-security-for-apps/example-rules/">Example mitigation rules</a>. For a list of fields provided by AI Security for Apps, refer to <a href="/waf/detections/ai-security-for-apps/fields/">AI Security for Apps fields</a>.</p>
<details class="nb-details"><summary>Combine with other Rules language fields</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15585.md")
</div></details>
