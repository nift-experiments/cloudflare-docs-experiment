<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15500.md")
</aside>
<h2 id="1-turn-on-the-detection"><ol>
<li>Turn on the detection</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashNewNav"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15505.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15499.md")
</aside>
<h2 id="2-validate-the-content-scanning-behavior"><ol start="2">
<li>Validate the content scanning behavior</li>
</ol></h2>
<p>Use <a href="/waf/analytics/security-analytics/">Security Analytics</a> and HTTP logs to validate that malicious content objects are being detected correctly.</p>
<p>You can use the <a href="https://www.eicar.org/download-anti-malware-testfile/">EICAR anti-malware test file</a> to test content scanning (select the ZIP format).</p>
<p>Alternatively, create a custom rule like described in the next step using a <em>Log</em> action instead of a mitigation action like <em>Block</em>. This rule will generate <a href="/waf/analytics/security-events/">security events</a> that will allow you to validate your configuration.</p>
<h2 id="3-create-a-custom-rule"><ol start="3">
<li>Create a custom rule</li>
</ol></h2>
<p><a href="/waf/custom-rules/create-dashboard/">Create a custom rule</a> that blocks detected malicious content objects uploaded to your application.</p>
<p>For example, create a custom rule with the <em>Block</em> action and the following expression:</p>
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
<td>Has malicious content object</td>
<td>equals</td>
<td>True</td>
</tr>
</tbody>
</table>
<p>If you use the Expression Editor, enter the following expression:</p>
<pre><code class="language-txt">(cf.waf.content_scan.has_malicious_obj)&#10;</code></pre>
<p>Rule action: <em>Block</em></p>
<p>This rule will match requests where Cloudflare detects a suspicious or malicious content object. For a list of fields provided by WAF content scanning, refer to <a href="/waf/detections/malicious-uploads/#content-scanning-fields">Content scanning fields</a>.</p>
<details class="nb-details"><summary>Optional: Combine with other Rules language fields</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15506.md")
</div></details>
<p>For additional examples, refer to <a href="/waf/detections/malicious-uploads/example-rules/">Example rules</a>.</p>
<h2 id="4-optional-configure-a-custom-scan-expression"><ol start="4">
<li>(Optional) Configure a custom scan expression</li>
</ol></h2>
<p>To check uploaded content in a way that is not covered by the default configuration, add a <a href="/waf/detections/malicious-uploads/#custom-scan-expressions">custom scan expression</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashNewNav"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15511.md")
</div></div>
<p>For more information, refer to <a href="/waf/detections/malicious-uploads/#custom-scan-expressions">Custom scan expressions</a>.</p>
