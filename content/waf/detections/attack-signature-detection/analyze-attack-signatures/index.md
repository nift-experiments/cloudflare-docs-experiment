<p>Use <strong>Security Analytics</strong> &gt; <strong>Attack Analysis</strong> to investigate attack signature matches before applying mitigation.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15542.md")
</aside>
<h2 id="review-signature-matches">Review signature matches</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15543.md")
</div>
<p>Use this analysis to identify common signatures and attack categories. You can also investigate a specific Common Vulnerabilities and Exposures (CVE) identifier or attack technique. Correlate the matches with <a href="/waf/detections/attack-score/">WAF Attack Score</a> to add another signal.</p>
<p>The request outcome shows whether existing protections mitigated matching traffic. It also helps identify requests served by Cloudflare or your origin. A detection does not apply an action by itself.</p>
<h2 id="interpret-confidence">Interpret confidence</h2>
<p>Confidence describes the expected false-positive characteristics of a signature. It does not prove that a request is malicious.</p>
<table>
<thead>
<tr>
<th>Confidence</th>
<th>Meaning</th>
<th>Comparison with Managed Rules</th>
<th>Recommended analysis</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>high</code></td>
<td>The signature targets a high true-positive and low false-positive rate.</td>
<td>Includes the same signatures that the default Managed Rules deployment enables.</td>
<td>Confirm affected traffic and current mitigation before applying a broad action.</td>
</tr>
<tr>
<td><code>low</code></td>
<td>The signature has a greater risk of matching legitimate application traffic.</td>
<td>Includes the Managed Rules signatures that are disabled by default.</td>
<td>Review requests and scope mitigation to the affected application surface.</td>
</tr>
</tbody>
</table>
<h2 id="investigate-possible-false-positives">Investigate possible false positives</h2>
<p>Legitimate rich-text input can match a generic cross-site scripting signature. For example, a content management or support application may accept HTML.</p>
<p>Filter the analysis to that hostname, path, and method. Review representative requests to distinguish expected content from attacks. Then create a scoped rule or exception instead of changing protection for the entire application.</p>
<h2 id="compare-results-with-managed-rules">Compare results with Managed Rules</h2>
<p>Each signature Ref matches the corresponding Managed Rule public Rule ID. Use this identifier to find the Managed Rule and compare the detection with your deployment.</p>
<p>Check the request outcome and <a href="/waf/analytics/security-events/">Security Events</a> before assuming Managed Rules blocked a match. Managed Rules actions and overrides determine their behavior.</p>
<h2 id="sampling">Sampling</h2>
<p>Attack Analysis uses <a href="/waf/analytics/security-analytics/#sampling">Security Analytics adaptive sampling</a>. Use <a href="/log-explorer/">Log Explorer</a> when you need 100% retention rather than sampled data.</p>
<p>After reviewing historical traffic, refer to <a href="/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/">Use attack signatures in Security Rules</a>.</p>
