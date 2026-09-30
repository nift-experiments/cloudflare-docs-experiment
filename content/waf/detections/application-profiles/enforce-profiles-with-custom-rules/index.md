<p>Application Profiles separate detection from mitigation. Cloudflare runs an <strong>always-on detection</strong> after a profile becomes available.</p>
<p>A violation does not block a request automatically. Use a <a href="/waf/custom-rules/">Custom Rule</a> when you are ready to mitigate traffic.</p>
<h2 id="select-a-detection-field">Select a detection field</h2>
<p>Use this expression for learned Schema Profiles:</p>
<pre><code class="language-txt">cf.schema_validation.learned.violated&#10;</code></pre>
<p>Use this expression for uploaded Schema Profiles:</p>
<pre><code class="language-txt">cf.schema_validation.uploaded.violated&#10;</code></pre>
<p>Monitor the selected field in <a href="/waf/analytics/security-analytics/">Security Analytics</a> before creating a blocking rule.</p>
<h2 id="scope-by-application">Scope by application</h2>
<p>Limit mitigation to the intended hostname and path:</p>
<pre><code class="language-txt">cf.schema_validation.learned.violated and http.host eq &quot;api.example.com&quot; and starts_with(http.request.uri.path, &quot;/v1/orders/&quot;)&#10;</code></pre>
<p>Scope mitigation to an operation using its complete identity. Include the HTTP method, hostname, and path:</p>
<pre><code class="language-txt">cf.schema_validation.learned.violated and http.request.method eq &quot;POST&quot; and http.host eq &quot;api.example.com&quot; and http.request.uri.path eq &quot;/v1/orders&quot;&#10;</code></pre>
<h2 id="combine-security-signals">Combine security signals</h2>
<p>Combine a profile violation with <a href="/waf/detections/attack-score/">Attack Score</a>:</p>
<pre><code class="language-txt">cf.schema_validation.learned.violated and cf.waf.score lt 20&#10;</code></pre>
<p>Combine an uploaded profile violation with <a href="/bots/concepts/bot-score/">Bot Score</a>:</p>
<pre><code class="language-txt">cf.schema_validation.uploaded.violated and cf.bot_management.score lt 10&#10;</code></pre>
<h2 id="roll-out-mitigation">Roll out mitigation</h2>
<p>Review production traffic and sampled violation reasons first. Then <a href="/waf/custom-rules/create-dashboard/">create a Custom Rule</a> with a suitable action.</p>
<p>Follow these rollout practices:</p>
<ul>
<li>Start with monitoring in Security Analytics.</li>
<li>Limit the first rule to one operation.</li>
<li>Review the effect before expanding scope.</li>
<li>Recheck profiles after application releases.</li>
<li>Recheck violations after client changes.</li>
</ul>
<p>For field details, refer to <a href="/waf/detections/application-profiles/fields/">Application Profile fields</a>.</p>
