<p>To learn more about features and functionality, select a plan.</p>
<p><a class="nb-link-button" href="/bots/plans/free/">Free</a><a class="nb-link-button" href="/bots/plans/pro/">Pro</a><a class="nb-link-button" href="/bots/plans/biz-and-ent/">Business</a><a class="nb-link-button" href="/bots/plans/bm-subscription/">Bot Management for Enterprise</a></p>
<table>
<thead>
<tr>
<th width="25%"></th>
<th width="30%"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
				<b>Plan name</b>
</td>
<td>Bot Management for Enterprise</td>
</tr>
<tr>
<td>
				<b>Availability</b>
</td>
<td>Added to Enterprise plans by your account team</td>
</tr>
<tr>
<td>
				<b>Enablement</b>
</td>
<td>Quick onboarding with help from our Solutions Engineering team</td>
</tr>
<tr>
<td>
				<b>Type of bots detected</b>
</td>
<td>
				Simple and sophisticated bots, headless browsers, and domain-specific
				anomalies
</td>
</tr>
<tr>
<td>
				<b>Actions</b>
</td>
<td>
				Customer chooses from several options, including block and various
				challenges
</td>
</tr>
<tr>
<td>
				<b>Analytics</b>
</td>
<td>
				Dedicated Bot Analytics tool, available in <b>Security Analytics</b>
</td>
</tr>
<tr>
<td>
				<b>Control</b>
</td>
<td>
				Ability to restrict by path, IP address, and more. <br /><br />Access to <a href="/bots/concepts/bot-score/">bot score</a>, <a href="/bots/additional-configurations/ja3-ja4-fingerprint/">JA3/JA4 fingerprint</a>, <a href="/bots/concepts/bot-tags/">bot tags</a> fields, and <a href="/bots/additional-configurations/detection-ids/">detection IDs</a>.
</td>
</tr>
<tr>
<td>
				<b>Additional features</b>
</td>
<td>
				<a href="/bots/additional-configurations/block-ai-bots/">Block AI bots</a>, <br/>
				<a href="/bots/additional-configurations/ai-labyrinth/">AI Labyrinth</a>, <br />
				<a href="/bots/additional-configurations/managed-robots-txt/">Instruct AI bot traffic with <code>robots.txt</code></a>, <br />
				<a href="/bots/concepts/bot-score/#bot-groupings">Definitely and Likely automated bots</a>, <br />
				<a href="/bots/concepts/bot/verified-bots/">Verified bots</a>, <br />
				<a href="/bots/additional-configurations/static-resources/">Static resource protection</a>, <br />
				<a href="/bots/troubleshooting/wordpress-loopback-issue/">Optimize for WordPress</a>, <br />
				<a href="/cloudflare-challenges/challenge-types/javascript-detections/">JavaScript Detections</a> 
</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3483.md")
</aside>
<h2 id="bot-settings-vs-custom-rules">Bot settings vs. custom rules</h2>
<p>Bot Management customers have both bot settings (configured in <strong>Security Settings</strong>) and the ability to create custom rules using bot score fields. Start with the bot settings for baseline protection, then add custom rules only when you need additional control.</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Handled by bot settings</th>
<th>When to use custom rules instead</th>
</tr>
</thead>
<tbody>
<tr>
<td>Block or challenge definitely automated traffic</td>
<td>No</td>
<td>Path-specific rules, custom thresholds, or combining with other fields</td>
</tr>
<tr>
<td>Block or challenge likely automated traffic</td>
<td>No</td>
<td>Path-specific rules, custom thresholds, or combining with other fields</td>
</tr>
<tr>
<td>Allow or block verified bots</td>
<td>No</td>
<td>Granular control by verified bot category</td>
</tr>
<tr>
<td>Block AI crawlers</td>
<td>Yes</td>
<td>Target individual AI crawlers using detection IDs</td>
</tr>
<tr>
<td>Protect static resources</td>
<td>No</td>
<td>Exclude static resources from specific rules</td>
</tr>
<tr>
<td>Optimize for WordPress</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<td>Forward bot data to origin</td>
<td>No</td>
<td>Use <a href="/rules/transform/">Transform Rules</a> or <a href="/rules/snippets/">Snippets</a></td>
</tr>
<tr>
<td>Detection ID targeting</td>
<td>No</td>
<td>Use <code>cf.bot_management.detection_ids</code> in <a href="/waf/custom-rules/">custom rules</a></td>
</tr>
<tr>
<td>JA3/JA4 fingerprint rules</td>
<td>No</td>
<td>Use <code>cf.bot_management.ja3_hash</code> or <code>cf.bot_management.ja4</code> in <a href="/waf/custom-rules/">custom rules</a></td>
</tr>
</tbody>
</table>
<p>For more details on when custom rules are needed, refer to <a href="/bots/additional-configurations/custom-rules/">custom rules</a>.</p>
<h2 id="how-do-i-get-started">How do I get started?</h2>
<p>To get started, review our <a href="/bots/get-started/">setup guides</a>. If you have any questions, visit the <a href="https://community.cloudflare.com/">community</a> to engage with other Cloudflare users.</p>
