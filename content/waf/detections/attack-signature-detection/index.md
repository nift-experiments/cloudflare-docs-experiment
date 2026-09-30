<p>Attack Signature Detection evaluates requests against Cloudflare attack signatures. It records match metadata without applying an action by itself.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15540.md")
</aside>
<p>Traditional WAF deployments combine detection and mitigation through managed rules. You may need to review matches before blocking traffic to reduce false positives.</p>
<p>Attack Signature Detection separates these steps. It records confidence, category, and signature Ref metadata for matching requests. Review this data in <strong>Security Analytics</strong> &gt; <strong>Attack Analysis</strong> before creating a <a href="/security/rules/">Security Rule</a>. Security Rules provide the mitigation layer. You can match confidence, category, or signature Ref values. You can also combine these values with properties such as hostname, path, and HTTP method.</p>
<p>A signature match does not mean Cloudflare blocked the request. Inspect the request outcome and your deployed rules to determine the applied action.</p>
<p>Attack Signature Detection uses the same signature definitions as <a href="/waf/managed-rules/">Cloudflare Managed Rules</a>.</p>
<h2 id="how-request-evaluation-works">How request evaluation works</h2>
<p>Attack Signature Detection uses the following request lifecycle:</p>
<ol>
<li>Cloudflare evaluates a request against attack signatures.</li>
<li>Matching signatures populate confidence, category, and Ref fields.</li>
<li>The match data becomes available in Security Analytics.</li>
<li>A Security Rule can evaluate these fields and apply its action.</li>
</ol>
<p>Attack Signature Detection does not inherit your Managed Rules deployment configuration. Managed Rules actions and overrides do not create Security Rules based on detection fields.</p>
<p>When no rule references an Attack Signature Detection field, detection does not add request latency. When a rule references a detection field, detection runs inline. Inline detection should have latency similar to Cloudflare Managed Rules evaluation.</p>
<h2 id="compare-attack-signature-detection-and-managed-rules">Compare Attack Signature Detection and Managed Rules</h2>
<p>Attack Signature Detection and Managed Rules use one signature catalog. Cloudflare releases each new signature to both products at the same time.</p>
<table>
<thead>
<tr>
<th>Area</th>
<th>Attack Signature Detection</th>
<th>Cloudflare Managed Rules</th>
</tr>
</thead>
<tbody>
<tr>
<td>Signatures</td>
<td>Uses the same signatures as Cloudflare Managed Rules.</td>
<td>Uses the same signatures as Attack Signature Detection.</td>
</tr>
<tr>
<td>Primary result</td>
<td>Populates confidence, category, and Ref metadata.</td>
<td>Applies the configured managed ruleset actions.</td>
</tr>
<tr>
<td>Mitigation</td>
<td>Requires a Security Rule that references a detection field.</td>
<td>Uses Managed Rules actions, overrides, and deployment configuration.</td>
</tr>
<tr>
<td>Analysis</td>
<td>Shows signature-oriented data in <strong>Security Analytics</strong> &gt; <strong>Attack Analysis</strong>.</td>
<td>Shows events produced by the deployed managed ruleset configuration.</td>
</tr>
<tr>
<td>Identifier</td>
<td>A signature Ref matches the corresponding Managed Rule public Rule ID.</td>
<td>A public Rule ID matches the corresponding signature Ref.</td>
</tr>
<tr>
<td>Rule ordering</td>
<td>A Custom Rule follows normal Custom Rules ordering. A terminating action stops later evaluation.</td>
<td>Managed Rules evaluate unless an earlier terminating action stops request processing.</td>
</tr>
</tbody>
</table>
<p>The shared Ref and Rule ID help you compare detection results with your Managed Rules deployment. Equivalent signatures do not produce equivalent behavior. Attack Signature Detection produces metadata, while Managed Rules apply configured actions.</p>
<p>Attack Signature Detection and Managed Rules have no special interaction. Normal phase and terminating-action behavior applies. Attack Signature Detection does not replace Managed Rules during Early Access.</p>
<h2 id="explore-attack-signature-detection">Explore Attack Signature Detection</h2>
<ul class="directory-listing"><li><a href="/waf/detections/attack-signature-detection/analyze-attack-signatures/">Analyze attack signatures</a></li><li><a href="/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/">Use attack signatures in Security Rules</a></li><li><a href="/waf/detections/attack-signature-detection/fields/">Fields</a></li></ul>
