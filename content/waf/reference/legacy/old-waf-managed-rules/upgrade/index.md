<p>On 2022-05-04, Cloudflare started the upgrade from the <a href="/waf/reference/legacy/old-waf-managed-rules/">previous version of WAF managed rules</a> to the new <a href="/waf/managed-rules/">WAF Managed Rules</a>, allowing a first set of eligible zones to migrate. Currently, all zones can upgrade to WAF Managed Rules, including partner accounts.</p>
<p>Cloudflare is gradually upgrading all zones to the new version of WAF Managed Rules. You can also start the upgrade process manually for a zone in the Cloudflare dashboard or via API. <strong>The upgrade is irreversible</strong> — once you upgrade to the new WAF Managed Rules, you cannot go back to the previous version.</p>
<p>If you are using the old dashboard, once the upgrade finishes your rules will be shown using a different user interface in <strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Managed rules</strong> tab. If you are using the <a href="/security/">new security dashboard</a>, your upgraded rules will be shown in <strong>Security</strong> &gt; <strong>Security rules</strong>.</p>
<p>Additionally, the WAF managed rules APIs will stop working once you upgrade.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/15683.md")
</aside>
<h2 id="main-benefits">Main benefits</h2>
<p>The new version of WAF Managed Rules provides the following benefits over the previous version:</p>
<ul>
<li>
<p><strong>New matching engine</strong> – WAF Managed Rules are powered by the Ruleset Engine, which allows faster managed rule deployments and the ability to check even more traffic without scaling issues. The rules follow the same syntax used in other Cloudflare security products like WAF custom rules.</p>
</li>
<li>
<p><strong>Updated Managed Rulesets</strong> – The Cloudflare OWASP Core Ruleset, one of WAF's Managed Rulesets, is based on the latest version of the OWASP Core Ruleset (v3.x), which adds <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
</li>
</ul>
@markup("md", "content/.markup/bodies/15684.md")
</div> and improves false positives rates compared to the version used in WAF managed rules (2.x). You also have more control over the sensitivity score, with a clear indication of how much each rule contributes to the score and what was the total score of a triggered request.
<ul>
<li><strong>Better rule browsing and configuration</strong> – Deploy Managed Rulesets with a single click to get immediate protection. Override the behavior of entire rulesets, or customize a single rule. Apply overrides to all rules with a specific tag to adjust rules applicable to a given software or attack vector. You can deploy configurations like the following:
<ul>
<li>Deploy the Cloudflare Managed Ruleset across all my zones.</li>
<li>Deploy the Cloudflare OWASP Core Ruleset on all traffic that does not contain <code>/api/*</code> in the path.</li>
<li>Disable Managed Rulesets across my account for traffic coming from my IP.</li>
</ul>
</li>
</ul>
<p>For more information on the benefits of WAF Managed Rules, refer to our <a href="https://blog.cloudflare.com/new-cloudflare-waf/">blog post</a>.</p>
<hr />
<h2 id="upgrade-impact">Upgrade impact</h2>
<p>You will be able to upgrade all your zones that do not have URI-based WAF overrides. The same protection will apply to your zone once you move to the new WAF.</p>
<p>Most configuration settings from the previous version of WAF managed rules will be upgraded to the new version, but some specific configurations originally defined in the OWASP ModSecurity Core Rule Set will be lost — you will have to create these configurations in the new WAF Managed Rules, if needed.</p>
<p>For API users, the APIs for managing the previous version of WAF managed rules will stop working once you upgrade. You must use the Rulesets API to manage the new WAF Managed Rules.</p>
<h3 id="configurations-that-will-be-upgraded">Configurations that will be upgraded</h3>
<p>The upgrade process will create an equivalent configuration for the following settings of WAF managed rules:</p>
<ul>
<li>Firewall rules configured with <em>Bypass</em> &gt; <em>WAF Managed Rules</em>.</li>
<li>Page Rules configured with <em>Disable Security</em>.</li>
<li>Page Rules configured with <em>Web Application Firewall: Off</em> or <em>Web Application Firewall: On</em>.</li>
</ul>
<p>The OWASP ruleset configuration will be partially upgraded. Refer to the next section for details.</p>
<h3 id="configurations-that-will-be-lost-in-the-upgrade-process">Configurations that will be lost in the upgrade process</h3>
<p>The upgrade process will partially migrate the settings of the OWASP ModSecurity Core Rule Set available in the previous version of WAF managed rules.</p>
<p>The following OWASP settings will be migrated:</p>
<ul>
<li><strong>Sensitivity</strong>: The <a href="/waf/reference/legacy/old-waf-managed-rules/#owasp-modsecurity-core-rule-set">old sensitivity values</a> will be migrated to the following <a href="/waf/managed-rules/reference/owasp-core-ruleset/concepts/#paranoia-level">paranoia level</a> (PL) and <a href="/waf/managed-rules/reference/owasp-core-ruleset/concepts/#score-threshold">score threshold</a> combinations in the new OWASP ruleset:</li>
</ul>
<table>
<thead>
<tr>
<th>Old sensitivity</th>
<th>PL in new OWASP</th>
<th>Score threshold in new OWASP</th>
</tr>
</thead>
<tbody>
<tr>
<td>High</td>
<td>PL2</td>
<td>Medium – 40 or higher</td>
</tr>
<tr>
<td>Medium</td>
<td>PL1</td>
<td>High – 25 or higher</td>
</tr>
<tr>
<td>Low</td>
<td>PL1</td>
<td>Medium – 40 or higher</td>
</tr>
<tr>
<td>Default</td>
<td>PL2</td>
<td>Medium – 40 or higher</td>
</tr>
</tbody>
</table>
<ul>
<li><strong>Action</strong>: The action in the previous OWASP ruleset has an almost direct mapping in the new OWASP managed ruleset, except for the <em>Simulate</em> action which will be migrated to <em>Log</em>.</li>
</ul>
<p>The following OWASP settings will <strong>not</strong> be migrated, since there is no direct equivalence between rules in the two versions:</p>
<ul>
<li>OWASP group overrides</li>
<li>OWASP rule overrides</li>
</ul>
<p>To replace these settings you will need to configure the Cloudflare OWASP Core Ruleset in WAF Managed Rules again according to your needs, namely any tag/rule overrides. For more information on configuring the new OWASP Core Ruleset, refer to <a href="/waf/managed-rules/reference/owasp-core-ruleset/">Cloudflare OWASP Core Ruleset</a>.</p>
<h3 id="configurations-that-will-prevent-you-from-upgrading">Configurations that will prevent you from upgrading</h3>
<p>If a zone has <a href="/api/resources/firewall/subresources/waf/subresources/overrides/methods/list/">URI-based WAF overrides</a> (only available via API), you will not have the option to upgrade to WAF Managed Rules. To upgrade to WAF Managed Rules you must:</p>
<ol>
<li>Delete any existing URI-based WAF overrides using the <a href="/api/resources/firewall/subresources/waf/subresources/overrides/methods/delete/">Delete a WAF override</a> operation.</li>
<li>Follow the upgrade process described below.</li>
</ol>
<h3 id="cloudflare-dashboard-changes">Cloudflare dashboard changes</h3>
<p>After the upgrade process is complete, the Cloudflare dashboard will display your rules in:</p>
<ul>
<li>Old dashboard: <strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Managed rules</strong> tab (using a different user interface)</li>
<li>New dashboard: <strong>Security</strong> &gt; <strong>Security rules</strong></li>
</ul>
<p>Unlike the old WAF managed rules, there is no longer a global on/off setting to enable the WAF. Instead, you deploy each managed ruleset individually in your zone.</p>
<p>For more information about deploying WAF Managed Rules in the Cloudflare dashboard, refer to <a href="/waf/managed-rules/deploy-zone-dashboard/">Deploy a WAF managed ruleset in the dashboard</a>.</p>
<h3 id="api-changes">API changes</h3>
<p>Once the upgrade is complete, the APIs for interacting with WAF managed rules <strong>will stop working</strong>. These APIs are the following:</p>
<ul>
<li><a href="/api/resources/firewall/subresources/waf/subresources/packages/methods/list/">WAF packages</a></li>
<li><a href="/api/resources/firewall/subresources/waf/subresources/packages/subresources/groups/methods/list/">WAF rule groups</a></li>
<li><a href="/api/resources/firewall/subresources/waf/subresources/packages/subresources/rules/methods/list/">WAF rules</a></li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15682.md")
</aside>
<p>To work with WAF Managed Rules you must use the <a href="/ruleset-engine/managed-rulesets/">Rulesets API</a>. For more information on deploying WAF Managed Rules via API, refer to <a href="/waf/managed-rules/deploy-api/">Deploy a WAF managed ruleset via API (zone)</a>.</p>
<h3 id="terraform-changes">Terraform changes</h3>
<p>Once the upgrade is complete, the following Terraform resources for configuring WAF managed rules <strong>will stop working</strong>:</p>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/3.35.0/docs/resources/waf_package"><code>cloudflare_waf_package</code></a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/3.35.0/docs/resources/waf_group"><code>cloudflare_waf_group</code></a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/3.35.0/docs/resources/waf_rule"><code>cloudflare_waf_rule</code></a></li>
</ul>
<p>These resources were only supported in the Terraform Cloudflare provider up to version 3.35. Version 4.x <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-4-upgrade#resources-1">no longer supports these resources</a>.</p>
<p>To manage the configuration of the new WAF Managed Rules using Terraform, you must use <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/ruleset"><code>cloudflare_ruleset</code></a> resources.</p>
<hr />
<h2 id="eligible-zones">Eligible zones</h2>
<h3 id="phase-2-since-2022-09-19">Phase 2 (since 2022-09-19)</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="update-notice">Update notice</h3>
@markup("md", "content/.markup/bodies/15681.md")
</aside>
<p>In phase 2 all zones are eligible for upgrade. The exact upgrade procedure varies according to your Cloudflare plan.</p>
<ul>
<li>
<p><strong>Pro</strong> and <strong>Business</strong> customers can upgrade to the new WAF Managed Rules in the Cloudflare dashboard or via API. Once the new version is enabled, the previous version of WAF managed rules will be automatically disabled.</p>
</li>
<li>
<p><strong>Enterprise</strong> customers can enable the new WAF Managed Rules configuration while keeping the previous version of WAF managed rules enabled, allowing them to check the impact of the new WAF configuration. After reviewing the behavior of the new configuration and making any required adjustments to specific managed rules, Enterprise users can then finish the upgrade, which will disable the previous version of WAF managed rules.</p>
</li>
</ul>
<p><strong>Note:</strong> Zones that have <a href="/api/resources/firewall/subresources/waf/subresources/overrides/methods/list/">URI-based WAF overrides</a>, which you could only manage via API, will not be able to upgrade immediately to the new WAF Managed Rules. You must delete these overrides before migrating.</p>
<h3 id="phase-1-since-2022-05-04">Phase 1 (since 2022-05-04)</h3>
<p>In phase 1 the upgrade became available to a subset of eligible zones, which had to meet the following requirements:</p>
<ul>
<li>
<p>The zone has:</p>
<ul>
<li>WAF disabled, or</li>
<li>WAF enabled and only the Cloudflare Managed Ruleset is enabled (the OWASP ModSecurity Core Rule Set must be disabled).</li>
</ul>
</li>
<li>
<p>The zone has no <a href="/firewall/cf-dashboard/">firewall rules</a> or <a href="/rules/page-rules/">Page Rules</a> bypassing, enabling, or disabling WAF managed rules:</p>
<ul>
<li>Firewall rules configured with <em>Bypass</em> &gt; <em>WAF Managed Rules</em>.</li>
<li>Page Rules configured with <em>Disable Security</em>.</li>
<li>Page Rules configured with <em>Web Application Firewall: Off</em> or <em>Web Application Firewall: On.</em></li>
</ul>
</li>
<li>
<p>The zone has no <a href="/api/resources/firewall/subresources/waf/subresources/overrides/methods/list/">URI-based WAF overrides</a> (only available via API).</p>
</li>
</ul>
<hr />
<h2 id="start-the-upgrade">Start the upgrade</h2>
<p>You can start the WAF upgrade in the Cloudflare dashboard or via API.</p>
<h3 id="using-the-dashboard">Using the dashboard</h3>
<ol>
<li>
<p>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select your account and zone.</p>
</li>
<li>
<p>A) If you are using the old dashboard:</p>
<ul>
<li>Go to <strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Managed rules</strong> tab.</li>
</ul>
<p>B) If you are using the <a href="/security/">new security dashboard</a>:</p>
<ol>
<li>Go to the <strong>Security rules</strong> page.</li>
</ol>
</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Go to upgrade your Managed rules</strong>.</li>
</ol>
<p>If you are an Enterprise customer, the dashboard will show the following banner:</p>
<p><img src="/assets/upstream/images/waf/reference/waf-migration-ent-banner.png" alt="The upgrade banner displayed to Enterprise customers." /></p>
<p>If you are a Professional/Business customer, the dashboard will show the following banner:</p>
<p><img src="/assets/upstream/images/waf/reference/waf-migration-biz-banner.png" alt="The upgrade banner displayed to Pro/Business customers." /></p>
<ol start="3">
<li>
<p>In the upgrade banner, select <strong>Review configuration</strong>. This banner is only displayed in eligible zones.</p>
</li>
<li>
<p>Review the proposed WAF configuration. You can adjust configuration, like <a href="/waf/managed-rules/deploy-zone-dashboard/#configure-a-managed-ruleset">editing the WAF Managed Rules configuration</a> or creating <a href="/waf/managed-rules/waf-exceptions/">exceptions</a> to skip the execution of rulesets or specific rules.</p>
</li>
<li>
<p>When you are done reviewing, select <strong>Deploy</strong> to deploy the new WAF Managed Rules configuration.</p>
<p>If you are a Professional/Business customer, Cloudflare will deploy the new WAF configuration and then disable the previous WAF version. The upgrade process may take a couple of minutes.</p>
<p>If you are an Enterprise customer, both WAF implementations will be enabled simultaneously when you select <strong>Deploy</strong>, so that you can validate your new configuration. Refer to the steps in the next section for additional guidance.</p>
</li>
</ol>
<h4 id="validate-your-new-waf-configuration-and-finish-the-upgrade-enterprise-customers-only">Validate your new WAF configuration and finish the upgrade (Enterprise customers only)</h4>
<p>If you are an Enterprise customer, after deploying your new WAF configuration both WAF implementations will be enabled simultaneously. During this stage (called validation mode), you can access both implementations of WAF Managed Rules in the Cloudflare dashboard, which will keep showing the upgrade banner until you finish upgrading. The new WAF Managed Rules will run before the previous version.</p>
<ol>
<li>
<p>Use the current validation mode to check the behavior of the new WAF configuration in <a href="/waf/analytics/security-events/">Security Events</a>. For more information, refer to <a href="#analyzing-the-new-waf-behavior-in-security-events">Analyzing the new WAF behavior in Security Events</a>.</p>
</li>
<li>
<p>When you are done reviewing your configuration with both WAFs enabled, select <strong>Ready to update</strong> in the upgrade banner, and then select <strong>Turn off previous version</strong>. This operation will complete the upgrade and disable the previous WAF version.</p>
</li>
</ol>
<p>When the upgrade finishes, the dashboard will show all of your upgraded rules in:</p>
<ul>
<li>Old dashboard: <strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Managed rules</strong> tab</li>
<li>New dashboard: <strong>Security</strong> &gt; <strong>Security rules</strong></li>
</ul>
<p>To check if the upgrade has finished, refresh the dashboard.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15680.md")
</aside>
<h3 id="using-the-api">Using the API</h3>
<ol>
<li>Use the <a href="#api-operations">Check WAF update compatibility</a> operation to determine if the zone can update to the new WAF, given its current configuration:</li>
</ol>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/waf_migration/check?phase_two=1&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Example response:</p>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;compatible&quot;: true,&#10;		&quot;migration_state&quot;: &quot;start&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>If the response includes <code>&quot;compatible&quot;: true</code>, this means that the zone can update to the new WAF and you can proceed with the upgrade process. If the response includes <code>&quot;compatible&quot;: false</code>, this means that your zone is not eligible for the upgrade, given its current configuration. Refer to <a href="#eligible-zones">Eligible zones</a> for details.</p>
<ol start="2">
<li>To get the new WAF configuration corresponding to your current configuration, use the <a href="#api-operations">Get new WAF configuration</a> operation:</li>
</ol>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/waf_migration/config?phase_two=1&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Example response:</p>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;name&quot;: &quot;default&quot;,&#10;		&quot;rules&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;&quot;,&#10;				&quot;version&quot;: &quot;&quot;,&#10;				&quot;action&quot;: &quot;execute&quot;,&#10;				&quot;expression&quot;: &quot;true&quot;,&#10;				&quot;description&quot;: &quot;&quot;,&#10;				&quot;ref&quot;: &quot;&quot;,&#10;				&quot;enabled&quot;: true,&#10;				&quot;action_parameters&quot;: {&#10;					&quot;id&quot;: &quot;efb7b8c949ac4650a09736fc376e9aee&quot;,&#10;					&quot;overrides&quot;: {&#10;						&quot;rules&quot;: [&#10;							{&#10;								&quot;id&quot;: &quot;23ee7cebe6e8443e99ecf932ab579455&quot;,&#10;								&quot;action&quot;: &quot;log&quot;,&#10;								&quot;enabled&quot;: false&#10;							}&#10;						]&#10;					}&#10;				}&#10;			}&#10;		]&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>The returned configuration in the example above, which would match the existing configuration for the previous WAF version, contains:</p>
<ul>
<li>A rule that executes the Cloudflare Managed Ruleset (ruleset ID efb7b8c949ac4650a09736fc376e9aee).</li>
<li>A single override for the rule <code>Apache Struts - Open Redirect - CVE:CVE-2013-2248</code> (rule ID <code>23ee7cebe6e8443e99ecf932ab579455</code>) in the same ruleset, setting the action to <code>log</code> and disabling the rule.</li>
</ul>
<ol start="3">
<li>(Optional, for Enterprise customers only) If you are upgrading an Enterprise zone to WAF Managed Rules, you can enter validation mode before finishing the upgrade. In this mode, both WAF implementations will be enabled. Use the <a href="/api/resources/rulesets/subresources/phases/methods/update/">Update a zone entry point ruleset</a> operation, making sure you include the <code>waf_migration=validation&amp;phase_two=1</code> query string parameters:</li>
</ol>
<pre><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/http_request_firewall_managed/entrypoint?waf_migration=validation&amp;phase_two=1&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;default&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;expression&quot;: &quot;true&quot;,&#10;      &quot;description&quot;: &quot;&quot;,&#10;      &quot;enabled&quot;: true,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;efb7b8c949ac4650a09736fc376e9aee&quot;,&#10;        &quot;overrides&quot;: {&#10;          &quot;rules&quot;: [&#10;            {&#10;              &quot;id&quot;: &quot;23ee7cebe6e8443e99ecf932ab579455&quot;,&#10;              &quot;action&quot;: &quot;log&quot;,&#10;              &quot;enabled&quot;: false&#10;            }&#10;          ]&#10;        }&#10;      }&#10;    }&#10;  ]&#10;}&#x27;&#10;</code></pre>
<p>After invoking this API endpoint, both WAF managed rules and WAF Managed Rules will be enabled. Check <a href="/waf/analytics/security-events/#sampled-logs">sampled logs</a> in Security Events for any legitimate traffic getting blocked, and perform any required adjustments to the WAF Managed Rules configuration. For example, you can <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">add an override</a> for a single rule that disables it or changes its action.</p>
<ol start="4">
<li>To finish the upgrade and disable WAF managed rules, set the configuration for the new WAF using the settings you obtained in step 2 and possibly adjusted in step 3. Make sure you include the <code>waf_migration=pending&amp;phase_two=1</code> query string parameters.</li>
</ol>
<pre><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/http_request_firewall_managed/entrypoint?waf_migration=pending&amp;phase_two=1&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;default&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;id&quot;: &quot;&quot;,&#10;      &quot;version&quot;: &quot;&quot;,&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;expression&quot;: &quot;true&quot;,&#10;      &quot;description&quot;: &quot;&quot;,&#10;      &quot;ref&quot;: &quot;&quot;,&#10;      &quot;enabled&quot;: true,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;efb7b8c949ac4650a09736fc376e9aee&quot;,&#10;        &quot;overrides&quot;: {&#10;          &quot;rules&quot;: [&#10;            {&#10;              &quot;id&quot;: &quot;23ee7cebe6e8443e99ecf932ab579455&quot;,&#10;              &quot;action&quot;: &quot;log&quot;,&#10;              &quot;enabled&quot;: false&#10;            }&#10;          ]&#10;        }&#10;      }&#10;    }&#10;  ]&#10;}&#x27;&#10;</code></pre>
<p>Once the provided configuration is saved and the new WAF Managed Rules are enabled, the previous version of the WAF managed rules will be automatically disabled, due to the presence of the <code>waf_migration=pending&amp;phase_two=1</code> parameters. This will make sure that your zone stays protected by one of the WAF versions during the update process.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15679.md")
</aside>
<hr />
<h2 id="analyzing-the-new-waf-behavior-in-security-events">Analyzing the new WAF behavior in Security Events</h2>
<h3 id="for-enterprise-customers">For Enterprise customers</h3>
<p>If you are an Enterprise customer, use the <strong>validation mode</strong> of the WAF upgrade process to check the behavior of the new WAF Managed Rules configuration. Cloudflare enables validation mode after you deploy the new WAF configuration. In this mode, the previous WAF version is still enabled, so that you can validate the behavior of your new configuration during the upgrade process. The new WAF Managed Rules will run before the previous version.</p>
<p>Go to <a href="/waf/analytics/security-events/#sampled-logs">sampled logs</a> in Security Events during validation mode and check the following:</p>
<ul>
<li>
<p>Look for any requests allowed by the new WAF that are being handled by the previous WAF version (for example, by a challenge or block action). If this happens, consider writing a <a href="/firewall/cf-dashboard/create-edit-delete-rules/#create-a-firewall-rule">firewall rule</a> or a <a href="/waf/custom-rules/create-dashboard/">WAF custom rule</a> to handle the requests you previously identified.</p>
</li>
<li>
<p>Look for legitimate requests being blocked by the new WAF. In this situation, edit the WAF managed rule that is blocking these requests, changing the performed action or disabling the rule. For more information, refer to <a href="/waf/managed-rules/deploy-zone-dashboard/#configure-a-managed-ruleset">Configure a managed ruleset</a>.</p>
</li>
</ul>
<h3 id="for-business-professional-customers">For Business/Professional customers</h3>
<p>Business and Professional customers do not have access to validation mode, which means that they will be able to check the new WAF behavior after they upgrade to the new WAF Managed Rules.</p>
<p>In the days following the upgrade, check <a href="/waf/analytics/security-events/#sampled-logs">sampled logs</a> in Security Events looking for any legitimate requests being blocked by WAF Managed Rules. If you identify any incorrectly blocked requests, adjust the corresponding WAF rule action to Log. For more information on changing the action of a managed ruleset rule, refer to <a href="/waf/managed-rules/deploy-zone-dashboard/#configure-individual-rules-of-a-managed-ruleset">Configure individual rules of a managed ruleset</a>.</p>
<p>Additionally, check for requests that should have been blocked. In this situation, consider creating a <a href="/firewall/cf-dashboard/create-edit-delete-rules/#create-a-firewall-rule">firewall rule</a> or a <a href="/waf/custom-rules/create-dashboard/">WAF custom rule</a> to block these requests.</p>
<hr />
<h2 id="api-operations">API operations</h2>
<p>Upgrading to the new WAF Managed Rules via API requires invoking the following API operations:</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Method + Endpoint</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Check WAF<br/>update compatibility</td>
<td><code>GET</code> <code>/zones/&lt;ZONE_ID&gt;/waf_migration/check?phase_two=1</code></td>
<td>Checks if the current zone can be updated to the new WAF, given its current configuration.</td>
</tr>
<tr>
<td>Get new WAF<br/>configuration</td>
<td><code>GET</code> <code>/zones/&lt;ZONE_ID&gt;/waf_migration/config?phase_two=1</code></td>
<td>Obtains the new WAF Managed Rules configuration that is equivalent to the current configuration (previous version of WAF managed rules).</td>
</tr>
<tr>
<td><a href="/ruleset-engine/rulesets-api/update/">Update zone<br/>entry point ruleset</a></td>
<td><code>PUT</code> <code>/zones/&lt;ZONE_ID&gt;/rulesets/</code> <code>phases/http_request_firewall_managed/entrypoint?waf_migration=&lt;VALUE&gt;&amp;phase_two=1</code></td>
<td>Updates the configuration of the zone entry point ruleset for the <code>http_request_firewall_managed</code> phase.<br/>Available values for the <code>waf_migration</code> query string parameter:<br/>– <code>pending</code> / <code>1</code>: Defines the new WAF Managed Rules configuration and disables the previous version of WAF managed rules as soon as the provided configuration is saved and the new WAF is enabled.<br/>– <code>validation</code> / <code>2</code>: (Enterprise zones only) Defines the new WAF Managed Rules configuration and enables the new WAF Managed Rules side by side with the previous version, entering validation mode. To exit validation mode and finish the upgrade, invoke the same API endpoint with <code>waf_migration=pending</code>.</td>
</tr>
<tr>
<td>Get WAF status</td>
<td><code>GET</code> <code>/zones/&lt;ZONE_ID&gt;/waf_migration/status</code></td>
<td>Obtains the status of old and new WAF managed rules for a zone (enabled/disabled). The response also includes the current upgrade state (or mode).</td>
</tr>
</tbody>
</table>
<p>You must prepend the Cloudflare API base URL to the endpoints listed above to obtain the full endpoint:</p>
<p><code>https://api.cloudflare.com/client/v4</code></p>
<hr />
<h2 id="possible-upgrade-errors">Possible upgrade errors</h2>
<p>Contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> to get help with the following errors:</p>
<ul>
<li>The number of firewall rules to migrate exceeds 200.</li>
<li>The length of a firewall rule expression is longer than 4 KB.</li>
</ul>
<hr />
<h2 id="additional-resources">Additional resources</h2>
<h3 id="configuring-the-new-waf-managed-rules-using-the-cloudflare-api">Configuring the new WAF Managed Rules using the Cloudflare API</h3>
<p>Instead of using the previous APIs for managing WAF packages, rule groups, and rules, you must now use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to programmatically configure WAF Managed Rules.</p>
<p>You can also create <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">overrides</a> to specify changes to be executed on top of the default WAF Managed Rules configuration. These changes will take precedence over the managed ruleset’s default behavior.</p>
<p>For more information, refer to the following resources:</p>
<ul>
<li><a href="/ruleset-engine/managed-rulesets/deploy-managed-ruleset/#deploy-a-managed-ruleset-to-a-phase-at-the-zone-level">Deploy a managed ruleset to a phase at the zone level</a></li>
<li><a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">Override a managed ruleset</a></li>
</ul>
<h3 id="configuring-the-new-waf-managed-rules-using-terraform">Configuring the new WAF Managed Rules using Terraform</h3>
<p>Instead of using the previous resources for managing WAF packages, rule groups, and rules, you must now use the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/ruleset"><code>cloudflare_ruleset</code></a> Terraform resource to configure WAF Managed Rules. For configuration examples, refer to <a href="/terraform/additional-configurations/waf-managed-rulesets/">WAF Managed Rules configuration using Terraform</a>.</p>
<h4 id="replace-your-configuration-using-cf-terraforming">Replace your configuration using <code>cf-terraforming</code></h4>
<p>You can use the <a href="https://github.com/cloudflare/cf-terraforming"><code>cf-terraforming</code></a> tool to generate the Terraform configuration for your new WAF Managed Rules configuration after you upgrade. Then, import the new resources to Terraform state.</p>
<p>The recommended steps for replacing your old WAF managed rules configuration in Terraform with a new ruleset-based configuration for the new WAF Managed Rules are the following:</p>
<ol>
<li>Run the following command to generate all ruleset configurations for a zone:</li>
</ol>
<pre><code class="language-sh">cf-terraforming generate --zone &lt;ZONE_ID&gt; --resource-type &quot;cloudflare_ruleset&quot;&#10;</code></pre>
<pre><code class="language-txt">resource &quot;cloudflare_ruleset&quot; &quot;terraform_managed_resource_3c0b456bc2aa443089c5f40f45f51b31&quot; {&#10;  kind    = &quot;zone&quot;&#10;  name    = &quot;default&quot;&#10;  phase   = &quot;http_request_firewall_managed&quot;&#10;  zone_id = &quot;&lt;ZONE_ID&gt;&quot;&#10;  rules {&#10;    [...]&#10;  }&#10;  [...]&#10;}&#10;[...]&#10;</code></pre>
<ol start="2">
<li>
<p>The previous command may return additional ruleset configurations for other Cloudflare products also based on the <a href="/ruleset-engine/">Ruleset Engine</a>. Since you are looking for the WAF Managed Rules configuration, keep only the Terraform resource for the <code>http_request_firewall_managed</code> phase and save it to a <code>.tf</code> configuration file. You will need the full resource name in the next step.</p>
</li>
<li>
<p>Import the <code>cloudflare_ruleset</code> resource you previously identified into Terraform state using the <code>terraform import</code> command. For example:</p>
</li>
</ol>
<pre><code class="language-sh">terraform import cloudflare_ruleset.terraform_managed_resource_3c0b456bc2aa443089c5f40f45f51b31 zone/&lt;ZONE_ID&gt;/3c0b456bc2aa443089c5f40f45f51b31&#10;</code></pre>
<pre><code class="language-txt"> cloudflare_ruleset.terraform_managed_resource_3c0b456bc2aa443089c5f40f45f51b31: Importing from ID &quot;zone/&lt;ZONE_ID&gt;/3c0b456bc2aa443089c5f40f45f51b31&quot;...&#10; cloudflare_ruleset.terraform_managed_resource_3c0b456bc2aa443089c5f40f45f51b31: Import prepared!&#10;   Prepared cloudflare_ruleset for import&#10; cloudflare_ruleset.terraform_managed_resource_3c0b456bc2aa443089c5f40f45f51b31: Refreshing state... [id=3c0b456bc2aa443089c5f40f45f51b31]&#10;&#10; Import successful!&#10;&#10; The resources that were imported are shown above. These resources are now in&#10; your Terraform state and will henceforth be managed by Terraform.&#10;</code></pre>
<ol start="4">
<li>Run <code>terraform plan</code> to validate that Terraform now checks the state of the new <code>cloudflare_ruleset</code> resource, in addition to other existing resources already managed by Terraform. For example:</li>
</ol>
<pre><code class="language-sh">terraform plan&#10;</code></pre>
<pre><code class="language-txt">&#10;cloudflare_ruleset.terraform_managed_resource_3c0b456bc2aa443089c5f40f45f51b31: Refreshing state... [id=3c0b456bc2aa443089c5f40f45f51b31]&#10;[...]&#10;cloudflare_waf_package.my_package: Refreshing state... [id=14a2524fd75c419f8d273116815b6349]&#10;cloudflare_waf_group.my_group: Refreshing state... [id=0580eb5d92e344ddb2374979f74c3ddf]&#10;[...]&#10;</code></pre>
<ol start="5">
<li>Remove any state related to the previous version of WAF managed rules from your Terraform state:</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15678.md")
</aside>
   1. Run the following command to find all resources related to the previous version of WAF managed rules:
<pre><code class="language-sh">terraform state list | grep -E &#x27;^cloudflare_waf_(package|group|rule)\.&#x27;&#10;</code></pre>
<pre><code class="language-txt">cloudflare_waf_package.my_package&#10;cloudflare_waf_group.my_group&#10;</code></pre>
<ol start="2">
<li>Run the <code>terraform state rm ...</code> command in dry-run mode to understand the impact of removing those resources without performing any changes:</li>
</ol>
<pre><code class="language-sh">terraform state rm -dry-run cloudflare_waf_package.my_package cloudflare_waf_group.my_group&#10;</code></pre>
<pre><code class="language-txt">Would remove cloudflare_waf_package.my_package&#10;Would remove cloudflare_waf_group.my_group&#10;</code></pre>
<ol start="3">
<li>If the impact looks correct, run the same command without the <code>-dry-run</code> parameter to actually remove the resources from Terraform state:</li>
</ol>
<pre><code class="language-sh">terraform state rm cloudflare_waf_package.my_package cloudflare_waf_group.my_group&#10;</code></pre>
<pre><code class="language-txt">Removed cloudflare_waf_package.my_package&#10;Removed cloudflare_waf_group.my_group&#10;Successfully removed 2 resource instance(s).&#10;</code></pre>
<ol start="6">
<li>
<p>After removing WAF package, group, and rule resources from Terraform state, delete <code>cloudflare_waf_package</code>, <code>cloudflare_waf_group</code>, and <code>cloudflare_waf_rule</code> resources from <code>.tf</code> configuration files.</p>
</li>
<li>
<p>Run <code>terraform plan</code> to verify that the resources you deleted from configuration files no longer appear. You should not have any pending changes.</p>
</li>
</ol>
<pre><code class="language-sh">terraform plan&#10;</code></pre>
<pre><code class="language-txt">cloudflare_ruleset.terraform_managed_resource_3c0b456bc2aa443089c5f40f45f51b31: Refreshing state... [id=3c0b456bc2aa443089c5f40f45f51b31]&#10;[...]&#10;&#10;No changes. Your infrastructure matches the configuration.&#10;&#10;Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are needed.&#10;</code></pre>
<p>For details on importing Cloudflare resources to Terraform and using the <code>cf-terraforming</code> tool, refer to the following resources:</p>
<ul>
<li><a href="/terraform/advanced-topics/import-cloudflare-resources/">Import Cloudflare resources</a></li>
<li><a href="https://github.com/cloudflare/cf-terraforming"><code>cf-terraforming</code> GitHub repository</a></li>
</ul>
<hr />
<h2 id="final-remarks">Final remarks</h2>
<p>The concept of <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/15685.md")
</div> did not exist in the OWASP version (2.x) used in WAF managed rules. Based on the OWASP guide recommendations, the WAF migration process will set the paranoia level of the Cloudflare OWASP Core Ruleset to _PL2_.
<p>You cannot disable the new version of WAF Managed Rules using <a href="/rules/page-rules/">Page Rules</a>, since the <em>Web Application Firewall: Off</em> setting in Page Rules only applies to the previous version of WAF managed rules. To disable the new WAF Managed Rules you must configure <a href="/waf/managed-rules/waf-exceptions/">exceptions</a> (also known as skip rules).</p>
