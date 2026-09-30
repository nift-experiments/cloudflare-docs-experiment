<p>Cloudflare performs a validation check for every request. The Validation component executes prior to all other security features like custom rules or Managed Rules. The validation check blocks malformed requests like Shellshock attacks and requests with certain attack patterns in their HTTP headers before any <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/15329.md")
</div> logic occurs.
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15328.md")
</aside>
<h2 id="event-logs-for-validation-checks">Event logs for validation checks</h2>
<p>Actions performed by the Validation component appear in <a href="/waf/analytics/security-events/#sampled-logs">Sampled logs</a> in Security Events, associated with the <code>Validation</code> service and without a rule ID. Event logs downloaded from the API show source as <code>Validation</code> and action as <code>drop</code> when this behavior occurs.</p>
<p>The following example shows a request blocked by the Validation component due to a malformed <code>User-Agent</code> HTTP request header:</p>
<p><img src="/assets/upstream/images/waf/validation-service.png" alt="Sampled logs displaying an example of a validation check event" /></p>
<p>In the downloaded JSON file for the event, the <code>ruleId</code> value indicates the detected issue — in this case, it was a Shellshock attack.</p>
<pre><code class="language-json">{&#10;	&quot;action&quot;: &quot;drop&quot;,&#10;	&quot;ruleId&quot;: &quot;sanity-shellshock&quot;,&#10;	&quot;source&quot;: &quot;sanitycheck&quot;,&#10;	&quot;userAgent&quot;: &quot;() { :;}; printf \\\\\&quot;detection[%s]string\\\\\&quot; \\\\\&quot;TjcLLwVzBtLzvbN\\\\&quot;&#10;	//...&#10;}&#10;</code></pre>
