<p>Cloudflare's Bot Management feature scores the likelihood that a request originates from a bot.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15472.md")
</aside>
<h2 id="bot-settings">Bot settings</h2>
<p>Before creating custom rules for bot protection, review the settings on your <a href="/security/">Security Settings</a> page under <strong>Bot traffic</strong>. Built-in features auto-update with new bot signatures, do not count toward your custom rule limits, and are simpler to manage.</p>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Bot setting</th>
</tr>
</thead>
<tbody>
<tr>
<td>Block AI crawlers (GPTBot, ClaudeBot, etc.)</td>
<td><strong>Block AI bots</strong></td>
</tr>
<tr>
<td>Block definitely automated traffic (bot score of 1)</td>
<td><strong>Definitely automated</strong></td>
</tr>
<tr>
<td>Challenge likely automated traffic (bot score 2-29)</td>
<td><strong>Likely automated</strong></td>
</tr>
<tr>
<td>Allow verified bots (Googlebot, Bingbot, etc.)</td>
<td><strong>Verified bots</strong></td>
</tr>
<tr>
<td>Extend bot protection to static resources</td>
<td><strong>Static resource protection</strong></td>
</tr>
<tr>
<td>Allow WordPress loopback requests</td>
<td><strong>Optimize for WordPress</strong></td>
</tr>
</tbody>
</table>
<p>Custom rules are still valuable when you need path-specific protection (different handling for <code>/api/</code> vs. <code>/login/</code>), custom score thresholds (for example, score below 20 instead of 30), conditional logic combining bot score with other fields, or custom actions not available in the built-in settings.</p>
<p>Bot score ranges from 1 through 99. A low score indicates the request comes from a script, API service, or an automated agent. A high score indicates that a human issued the request from a standard desktop or mobile web browser.</p>
<p>These examples use:</p>
<ul>
<li><a href="/ruleset-engine/rules-language/fields/reference/cf.bot_management.score/"><code>cf.bot_management.score</code></a> to target requests from bots</li>
<li><a href="/ruleset-engine/rules-language/fields/reference/cf.bot_management.verified_bot/"><code>cf.bot_management.verified_bot</code></a> to identify requests from <a href="https://radar.cloudflare.com/verified-bots">known good bots</a></li>
<li><a href="/ruleset-engine/rules-language/fields/reference/cf.bot_management.ja3_hash/"><code>cf.bot_management.ja3_hash</code></a> to target specific <a href="/bots/additional-configurations/ja3-ja4-fingerprint/">JA3 Fingerprints</a></li>
</ul>
<h2 id="suggested-rules">Suggested rules</h2>
<p>For best results:</p>
<ul>
<li>Use <a href="/bots/bot-analytics/#enterprise-bot-management">Bot Analytics</a> to learn about your traffic before applying rules.</li>
<li>Start small and increase your bot threshold over time.</li>
</ul>
<p>Your rules may also vary based on the <a href="/bots/get-started/bot-management/">nature of your site</a> and your tolerance for false positives.</p>
<h3 id="general-protection">General protection</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15471.md")
</aside>
<p>The following three custom rules provide baseline protection against malicious bots:</p>
<p><strong>Rule 1: Skip verified bots</strong></p>
<ul>
<li><strong>Expression</strong>: <code>(cf.bot_management.verified_bot)</code></li>
<li><strong>Action</strong>: <em>Skip:</em>
<ul>
<li><em>All remaining custom rules</em></li>
</ul>
</li>
<li>Known good bots (Googlebot, Bingbot, monitoring services) bypass all custom rules. Refer to the <a href="/bots/concepts/bot/verified-bots/">verified bots list</a> and <a href="https://radar.cloudflare.com/bots/directory">Radar bots directory</a>.</li>
</ul>
<p><strong>Rule 2: Block definitely automated</strong></p>
<ul>
<li><strong>Expression</strong>: <code>(cf.bot_management.score eq 1)</code></li>
<li><strong>Action</strong>: <em>Block</em></li>
<li>Score 1 traffic is definitively automated. Blocking it carries minimal false positive risk.</li>
</ul>
<p><strong>Rule 3: Challenge likely automated</strong></p>
<ul>
<li><strong>Expression</strong>: <code>(cf.bot_management.score gt 1 and cf.bot_management.score lt 30)</code></li>
<li><strong>Action</strong>: <em>Managed Challenge</em></li>
<li>Scores 2-29 indicate likely automated behavior. A challenge lets legitimate users through while stopping bots.</li>
</ul>
<h3 id="specific-protection-for-browser-api-and-mobile-traffic">Specific protection for browser, API, and mobile traffic</h3>
<h4 id="protect-browser-endpoints">Protect browser endpoints</h4>
<p>When a request is definitely automated (score of 1) or likely automated (scores 2 through 29) and is <em>not</em> on the list of known good bots, Cloudflare blocks the request.</p>
<ul>
<li><strong>Expression</strong>: <code>(cf.bot_management.score lt 30 and not cf.bot_management.verified_bot)</code></li>
<li><strong>Action</strong>: <em>Block</em></li>
</ul>
<h4 id="exempt-api-traffic">Exempt API traffic</h4>
<p>Since Bot Management detects automated users, you need to explicitly allow your <strong>good</strong> automated traffic⁠ — this includes your <a href="https://www.cloudflare.com/learning/security/api/what-is-an-api/">APIs</a> and partner APIs.</p>
<p>This example offers the same protection as the browser-only rule, but allows automated traffic to your API.</p>
<ul>
<li><strong>Expression</strong>: <code>(cf.bot_management.score lt 30 and not cf.bot_management.verified_bot and not starts_with(http.request.uri.path, &quot;/api&quot;))</code></li>
<li><strong>Action</strong>: <em>Block</em></li>
</ul>
<h4 id="adjust-for-mobile-traffic">Adjust for mobile traffic</h4>
<p>Since Bot Management can be more sensitive to mobile traffic, you may want to add in additional logic to avoid blocking legitimate requests.</p>
<p>If you are handling requests from your own mobile application, you could potentially allow it based on its specific <a href="/bots/additional-configurations/ja3-ja4-fingerprint/">JA3 fingerprint</a>.</p>
<ul>
<li><strong>Expression</strong>: <code>(cf.bot_management.ja3_hash eq &quot;df669e7ea913f1ac0c0cce9a201a2ec1&quot;)</code></li>
<li><strong>Action</strong>: <em>Skip:</em>
<ul>
<li><em>All remaining custom rules</em></li>
</ul>
</li>
</ul>
<p>Otherwise, you could set lower thresholds for mobile traffic. The following rules would block definitely automated mobile traffic and challenge likely automated traffic.</p>
<p><strong>Rule 1:</strong></p>
<ul>
<li><strong>Expression</strong>: <code>(cf.bot_management.score lt 2 and http.user_agent contains &quot;App_Name 2.0&quot;)</code></li>
<li><strong>Action</strong>: <em>Block</em></li>
</ul>
<p><strong>Rule 2:</strong></p>
<ul>
<li><strong>Expression</strong>: <code>(cf.bot_management.score lt 30 and http.user_agent contains &quot;App_Name 2.0&quot;)</code></li>
<li><strong>Action</strong>: <em>Managed Challenge</em></li>
</ul>
<h4 id="combine-the-different-rules">Combine the different rules</h4>
<p>If your domain handles mobile, browser, and API traffic, you would want to arrange these example rules in the following order:</p>
<ul>
<li>Rule for <a href="#exempt-api-traffic">API traffic</a></li>
<li>Rule(s) for <a href="#adjust-for-mobile-traffic">mobile traffic</a></li>
<li>Rule for <a href="#protect-browser-endpoints">browser traffic</a></li>
</ul>
<h3 id="static-resource-protection">Static resource protection</h3>
<p>Static resources are protected by default when you create custom rules using the <code>cf.bot_management.score</code> field.</p>
<p>To exclude static resources, include <code>not (cf.bot_management.static_resource)</code> in your rule expression. For details, refer to <a href="/bots/additional-configurations/static-resources/">Static resource protection</a>.</p>
<h3 id="additional-considerations">Additional considerations</h3>
<p>From there, you could customize your custom rules based on specific request paths (<code>/login</code> or <code>/signup</code>), common traffic patterns, or many other characteristics.</p>
<p>Make sure you review <a href="/bots/bot-analytics/#enterprise-bot-management">Bot Analytics</a> and <a href="/waf/analytics/security-events/">Security Events</a> to check if your rules need more tuning.</p>
<hr />
<h2 id="other-resources">Other resources</h2>
<ul>
<li><a href="/waf/custom-rules/use-cases/allow-traffic-from-verified-bots/">Use case: Allow traffic from verified bots</a></li>
<li><a href="/turnstile/tutorials/integrating-turnstile-waf-and-bot-management/">Tutorial: Integrate Turnstile, WAF, and Bot Management</a></li>
</ul>
