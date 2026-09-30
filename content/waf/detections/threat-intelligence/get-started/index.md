<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>Your account must have an active <a href="/security-center/cloudforce-one/">Cloudforce One subscription</a>. Contact your account team for access.</li>
<li>The <a href="/waf/">WAF</a> must be enabled on your zone.</li>
</ul>
<h2 id="1-create-a-rule-from-threat-events"><ol>
<li>Create a rule from Threat Events</li>
</ol></h2>
<p>The fastest way to create a threat intelligence rule is from a saved view in the <a href="/security-center/cloudforce-one/">Threat Events</a> dashboard. Filter the threats you care about, then export the filters directly to a WAF rule.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15481.md")
</div>
<h2 id="2-review-matches-in-security-analytics"><ol start="2">
<li>Review matches in Security Analytics</li>
</ol></h2>
<p>Once the rule is deployed, matches appear in <a href="/waf/analytics/security-analytics/">Security Analytics</a>. You can see the threat event details — including threat actors, target industries, and countries — directly in the analytics view.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15482.md")
</div>
<p>If no matches appear after deploying the rule, contact your account team to verify your Cloudforce One subscription is active.</p>
<h2 id="3-switch-to-block-or-managed-challenge"><ol start="3">
<li>Switch to Block or Managed Challenge</li>
</ol></h2>
<p>Once you are confident in the match patterns, update the rule action from <em>Log</em> to <em>Block</em> or <em>Managed Challenge</em>.</p>
<p>For more examples, refer to <a href="/waf/detections/threat-intelligence/example-rules/">Example rules</a>. For the full field list, refer to <a href="/waf/detections/threat-intelligence/fields/">Threat intelligence fields</a>.</p>
<h2 id="4-alternative-create-a-rule-manually"><ol start="4">
<li>(Alternative) Create a rule manually</li>
</ol></h2>
<p>If you prefer to write expressions directly, you can create a rule from the dashboard or the API.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15486.md")
</div></div>
