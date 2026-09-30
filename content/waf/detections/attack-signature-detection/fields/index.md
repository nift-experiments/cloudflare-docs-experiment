<p>Attack Signature Detection populates these request fields when signatures match:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.waf.signature.request.categories</code></td>
<td><span class="nb-type">Array&lt;String&gt;</span></td>
<td>Categories associated with all matching signatures. A signature can have more than one category.</td>
</tr>
<tr>
<td><code>cf.waf.signature.request.confidence</code></td>
<td><span class="nb-type">Array&lt;String&gt;</span></td>
<td>Confidence values associated with matching signatures. Supported values are <code>high</code> and <code>low</code>.</td>
</tr>
<tr>
<td><code>cf.waf.signature.request.refs</code></td>
<td><span class="nb-type">Array&lt;String&gt;</span></td>
<td>Refs for matching signatures, up to 10 per request. Each Ref matches the corresponding Managed Rule public Rule ID.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15541.md")
</aside>
<p>All three fields are available in Security Analytics and Security Rules. You can reference them in rules created in the dashboard or through the API.</p>
<h2 id="example-values">Example values</h2>
<p>The fields can contain values like these:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Example value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.waf.signature.request.categories</code></td>
<td><code>[&quot;sqli&quot;, &quot;cve-2025-55182&quot;]</code></td>
</tr>
<tr>
<td><code>cf.waf.signature.request.confidence</code></td>
<td><code>[&quot;high&quot;]</code></td>
</tr>
<tr>
<td><code>cf.waf.signature.request.refs</code></td>
<td><code>[&quot;d68f8101f6e14e25aefcaea69c530a29&quot;]</code></td>
</tr>
</tbody>
</table>
<h2 id="rules-language-examples">Rules language examples</h2>
<p>Use <code>any()</code> to test array elements:</p>
<pre><code class="language-txt">any(cf.waf.signature.request.categories[*] eq &quot;sqli&quot;)&#10;</code></pre>
<pre><code class="language-txt">any(cf.waf.signature.request.confidence[*] eq &quot;high&quot;)&#10;</code></pre>
<pre><code class="language-txt">any(cf.waf.signature.request.refs[*] eq &quot;d68f8101f6e14e25aefcaea69c530a29&quot;)&#10;</code></pre>
<p>For rollout guidance, refer to <a href="/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/">Use attack signatures in Security Rules</a>.</p>
<h2 id="logpush-fields">Logpush fields</h2>
<p>Signature Refs and categories are available in Logpush:</p>
<table>
<thead>
<tr>
<th>Rules field</th>
<th>Logpush field</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.waf.signature.request.refs</code></td>
<td><a href="/logs/logpush/logpush-job/datasets/zone/http_requests/#wafrequestsignaturerefs"><code>wafRequestSignatureRefs</code></a></td>
</tr>
<tr>
<td><code>cf.waf.signature.request.categories</code></td>
<td><a href="/logs/logpush/logpush-job/datasets/zone/http_requests/#wafrequestsignaturecategories"><code>wafRequestSignatureCategories</code></a></td>
</tr>
</tbody>
</table>
<p>Only signature Ref and category mappings are available in Logpush.</p>
