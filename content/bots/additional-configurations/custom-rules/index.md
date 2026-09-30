<p>Bot protection on Cloudflare works through two complementary mechanisms: built-in settings configured through toggles in <strong>Security Settings</strong>, and <a href="/waf/custom-rules/">WAF custom rules</a> that you write using <a href="/bots/reference/bot-management-variables/">bot management fields</a>. Understanding when to use each approach helps you avoid creating duplicate rules and simplifies your security configuration.</p>
<p>The following features are configured through toggles and dropdowns in <a href="/security/settings/">Security Settings</a>. They do not require you to write any rule expressions.</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>What it does</th>
<th>Availability</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/bots/additional-configurations/block-ai-bots/">Block AI bots</a></td>
<td>Blocks AI crawlers (GPTBot, ClaudeBot, Bytespider, and others) using an auto-updating managed rule</td>
<td>All plans</td>
</tr>
<tr>
<td><a href="/bots/additional-configurations/ai-labyrinth/">AI Labyrinth</a></td>
<td>Feeds non-compliant AI crawlers into a maze of generated content</td>
<td>All plans</td>
</tr>
<tr>
<td><a href="/bots/additional-configurations/managed-robots-txt/">Managed robots.txt</a></td>
<td>Prepends AI crawler disallow directives to your <code>robots.txt</code></td>
<td>All plans</td>
</tr>
<tr>
<td>Super Bot Fight Mode &gt; <strong>Definitely automated</strong></td>
<td>Blocks or challenges traffic with a <a href="/bots/concepts/bot-score/">bot score</a> of 1</td>
<td>Pro, Business, Enterprise</td>
</tr>
<tr>
<td>Super Bot Fight Mode &gt; <strong>Likely automated</strong></td>
<td>Blocks or challenges traffic with a bot score of 2-29</td>
<td>Business, Enterprise</td>
</tr>
<tr>
<td><a href="/bots/concepts/bot/verified-bots/">Verified bots</a></td>
<td>Managed category of high-trust bots (Googlebot, Bingbot, and others)</td>
<td>Pro, Business, Enterprise</td>
</tr>
<tr>
<td><a href="/bots/additional-configurations/static-resources/">Static resource protection</a></td>
<td>Extends bot actions to cover static file types</td>
<td>Pro, Business, Enterprise</td>
</tr>
<tr>
<td><a href="/bots/troubleshooting/wordpress-loopback-issue/">Optimize for WordPress</a></td>
<td>Allows WordPress loopback requests through bot protection</td>
<td>Pro, Business, Enterprise</td>
</tr>
<tr>
<td><a href="/cloudflare-challenges/challenge-types/javascript-detections/">JavaScript detections</a></td>
<td>Injects a lightweight script to identify clients that cannot execute JavaScript</td>
<td>All plans (automatic on Free)</td>
</tr>
</tbody>
</table>
<p>Bot settings update automatically as Cloudflare identifies new bot signatures and AI crawlers, while custom rules require manual updates. They do not count toward your <a href="/waf/custom-rules/#availability">custom rule limits</a>, and apply uniformly across your domain without the risk of expression errors.</p>
<h2 id="custom-rules-use-cases">Custom rules use cases</h2>
<p>Custom rules are valuable when you need capabilities that built-in settings do not offer. The following scenarios require <a href="/waf/custom-rules/">WAF custom rules</a> with <a href="/bots/reference/bot-management-variables/">bot management fields</a>. Bot management fields are available to customers with a <a href="/bots/get-started/bot-management/">Bot Management</a> subscription.</p>
<h3 id="path-specific-protection">Path-specific protection</h3>
<p>Since Bot settings apply to all traffic across your domain, you may need an alternative approach to bot handling for different paths using custom rules — for example, stricter protection on <code>/login/</code> than on <code>/public/</code>.</p>
<h4 id="example">Example</h4>
<p>Block likely automated traffic only on your login endpoint:</p>
<pre><code class="language-txt">(cf.bot_management.score lt 30 and not cf.bot_management.verified_bot and http.request.uri.path eq &quot;/login&quot;)&#10;</code></pre>
<h3 id="custom-score-thresholds">Custom score thresholds</h3>
<p>The <strong>Definitely automated</strong> and <strong>Likely automated</strong> settings in Super Bot Fight Mode use fixed bot score groupings (1 and 2-29). If you need a different threshold, for example, challenging all traffic with a score below 20, you need a custom rule.</p>
<h3 id="conditional-logic">Conditional logic</h3>
<p>If you need to combine bot score with other request fields, such as country, ASN, URI path, JA3/JA4 fingerprint, or user agent, you need custom rules. Bot settings do not support compound conditions.</p>
<h4 id="example-1">Example</h4>
<p>Challenge likely automated traffic only from specific ASNs:</p>
<pre><code class="language-txt">(cf.bot_management.score lt 30 and not cf.bot_management.verified_bot and ip.src.asnum in {64496 65536})&#10;</code></pre>
<h3 id="custom-actions">Custom actions</h3>
<p>Bot settings offer <strong>Block</strong>, <strong>Managed Challenge</strong>, and <strong>Allow</strong> as actions.</p>
<p>If you need other actions, such as <strong>Log</strong> (for testing rules before enforcement), <strong>Interactive Challenge</strong>, or <strong>Skip</strong> (to bypass other rules), you need custom rules.</p>
<h3 id="detection-id-targeting">Detection ID targeting</h3>
<p>To act on specific bot heuristic detections, such as <a href="/bots/additional-configurations/detection-ids/account-takeover-detections/">account takeover</a> or <a href="/bots/additional-configurations/detection-ids/scraping-detections/">scraping</a> patterns, you need custom rules using the <code>cf.bot_management.detection_ids</code> field. Bot settings do not expose individual detection IDs.</p>
<h3 id="forwarding-bot-data-to-origin">Forwarding bot data to origin</h3>
<p>To send bot scores, verified bot status, or JA3/JA4 fingerprints to your origin server, use <a href="/rules/transform/">Transform Rules</a> (including <a href="/rules/transform/managed-transforms/">Managed Transforms</a>) or <a href="/rules/snippets/">Snippets</a>. These are not part of the built-in bot settings.</p>
<h2 id="execution-order">Execution order</h2>
<p>Custom rules execute before Super Bot Fight Mode managed rules. If a custom rule takes a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3539.md")
</div> (such as _Block_ or _Managed Challenge_), the request does not reach bot settings.
<p>Refer to <a href="/waf/feature-interoperability/">Security features interoperability</a> for more information.</p>
