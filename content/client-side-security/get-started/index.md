<h2 id="1-activate-client-side-resource-monitoring"><ol>
<li>Activate client-side resource monitoring</li>
</ol></h2>
<p>To enable client-side resource monitoring:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/1348.md")
</div>
<p>If you do not have access to client-side security settings in the Cloudflare dashboard, check if your user has one of the <a href="/client-side-security/reference/roles-and-permissions/">necessary roles</a>.</p>
<h2 id="2-review-detected-resources"><ol start="2">
<li>Review detected resources</li>
</ol></h2>
<p>When you enable client-side resource monitoring, it may take a while to get the list of detected scripts in your domain.</p>
<p>To review the scripts detected by Cloudflare:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/1349.md")
</div>
<p>Depending on your Cloudflare plan, you may be able to also review the connections made by scripts in your domain's pages and check them for malicious activity.</p>
<h2 id="3-optional-configure-alerts"><ol start="3">
<li>(Optional) Configure alerts</li>
</ol></h2>
<p>Once you have activated client-side security's resource monitoring, you can set up one or more alerts informing you of relevant client-side changes on your zones. The <a href="/client-side-security/alerts/alert-types/">available alert types</a> depend on your Cloudflare plan and subscriptions.</p>
<p>To configure an alert:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/1350.md")
</div>
<p>To learn how you can handle an alert, refer to <a href="/client-side-security/best-practices/handle-an-alert/">Handle a client-side resource alert</a>.</p>
<h2 id="4-optional-define-content-security-rules"><ol start="4">
<li>(Optional) Define content security rules</li>
</ol></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1347.md")
</aside>
<p><a href="/client-side-security/rules/">Content security rules</a> (previously called policies) define allowed resources on your websites. Create content security rules to implement a positive security model<sup><a href="#footnote-1">1</a></sup>.</p>
<h3 id="4-1-create-a-content-security-rule-with-the-log-action">4.1. Create a content security rule with the Log action</h3>
<p>When you create a content security rule with the <a href="/client-side-security/rules/#rule-actions"><em>Log</em> action</a>, Cloudflare logs any resources not covered by the rule, without blocking any resources. Use this action to validate a new rule before deploying it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1346.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/1351.md")
</div>
<h3 id="4-2-review-rule-violations">4.2. Review rule violations</h3>
<p>Resources not covered by the content security rule you created will be reported as <a href="/client-side-security/rules/violations/">rule violations</a>. After some time, review the list of rule violations to make sure the rule is correct.</p>
<p>To view rule violation information:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>(Optional) Filter by <strong>Content security rules</strong>.</li>
</ol>
<p>The displayed information includes the following:</p>
<ul>
<li>A sparkline next to the rule name, showing violations in the past seven days.</li>
<li>For content security rules with associated violations, an expandable details section for each rule, with the top resources present in violation events and a sparkline per top resource.</li>
</ul>
<p>Update the rule if needed.</p>
<h3 id="4-3-change-rule-action-to-allow">4.3. Change rule action to Allow</h3>
<p>Once you have verified that your content security rule is correct, change the rule action from <em>Log</em> to <em>Allow</em>.</p>
<p>When you use the <a href="/client-side-security/rules/#rule-actions"><em>Allow</em> action</a>, Cloudflare starts blocking any resources not explicitly allowed by the rule.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">A positive security model is one that defines what is allowed and rejects everything else. In contrast, a negative security model defines what will be rejected and accepts the rest.</li></ol></section>
