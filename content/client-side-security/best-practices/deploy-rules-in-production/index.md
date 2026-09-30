<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4013.md")
</aside>
<p>Follow the practices on this page when deploying or updating <a href="/client-side-security/rules/">content security rules</a> in a production environment. Applying rule changes without a validation period can block legitimate resources and disrupt your application for end users.</p>
<h2 id="update-rules-safely">Update rules safely</h2>
<p>When updating content security rules in production, avoid the following:</p>
<ul>
<li>Do not edit an existing rule directly in production without testing first.</li>
<li>Do not change a rule action from <em>Log</em> to <em>Allow</em> without a validation period.</li>
<li>Do not delete all rules at once.</li>
</ul>
<p>Instead, follow these practices:</p>
<ul>
<li>Test changes in a staging environment before applying them in production.</li>
<li>Use the <em>Log</em> <a href="/client-side-security/rules/#rule-actions">rule action</a> for at least seven days before switching to <em>Allow</em>.</li>
<li>Update one rule at a time.</li>
<li>Monitor <a href="/client-side-security/rules/violations/">rule violations</a> for 24 hours after each change.</li>
<li>Document a rollback procedure before making changes.</li>
</ul>
<h2 id="pre-enforcement-checklist">Pre-enforcement checklist</h2>
<p>Complete the following checklist before switching a content security rule from <em>Log</em> to <em>Allow</em>:</p>
<ul>
<li>The rule was tested in <em>Log</em> mode for a minimum of seven days.</li>
<li>Reviewed all <a href="/client-side-security/rules/violations/">rule violations</a> and confirmed there are no unexpected blocks.</li>
<li>Added all legitimate third-party resources to the rule allowlist.</li>
<li>Tested the application on all major browsers (Chrome, Firefox, Safari, Edge).</li>
<li>Configured <a href="/client-side-security/alerts/">alerts</a> for rule violations.</li>
<li>There is a documented rollback procedure that is ready to execute.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4012.md")
</aside>
<h2 id="rollback-a-rule-change">Rollback a rule change</h2>
<p>If a rule change causes unexpected violations or blocks legitimate resources:</p>
<ol>
<li>Switch the rule action back to <em>Log</em> to stop blocking resources immediately.</li>
<li>Review the <a href="/client-side-security/rules/violations/">rule violations</a> to identify which resources were blocked.</li>
<li>Update the rule to include any missing resources.</li>
<li>Repeat the validation process before switching back to <em>Allow</em> (blocks resources not present in the allowlist).</li>
</ol>
