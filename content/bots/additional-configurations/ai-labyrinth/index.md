<p>The AI Labyrinth adds invisible links on your webpage with specific <code>Nofollow</code> tags to block AI crawlers that do not adhere to the recommended guidelines and crawl without permission. AI crawlers that scrape your website content without permission will be stuck in a maze of never-ending links, and their details are recorded and used by all Cloudflare customers who choose to block <a href="/bots/concepts/bot/#ai-bots">AI bots</a>.</p>
<p>These links do not impact your search engine optimization (SEO) or your website's appearance, and are only seen by bots. AI bots that respect no-crawl instructions will safely ignore this honeypot.</p>
<h2 id="ai-labyrinth-in-security-analytics">AI Labyrinth in Security Analytics</h2>
<p>When AI Labyrinth is enabled, Cloudflare logs security events for AI Labyrinth under the <strong>AI Labyrinth</strong> service. The following actions describe what happened to the request:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>AI Labyrinth Served</strong></td>
<td>Cloudflare injected AI Labyrinth honeypot links into the HTML response.</td>
</tr>
<tr>
<td><strong>AI Labyrinth Crawls</strong></td>
<td>A crawler followed one of the injected honeypot links and entered the maze.</td>
</tr>
</tbody>
</table>
<p>AI Labyrinth actions are not mitigations. Cloudflare does not block or challenge the request.</p>
<p>A high volume of <strong>AI Labyrinth Crawls</strong> relative to <strong>AI Labyrinth Served</strong> indicates that non-compliant AI crawlers are actively following the injected links.</p>
<p>You can view these events in <a href="/waf/analytics/security-analytics/">Security Analytics</a> and <a href="/waf/analytics/security-events/">Security Events</a>.</p>
<h3 id="after-you-turn-off-ai-labyrinth">After you turn off AI Labyrinth</h3>
<p>When you turn off AI Labyrinth, Cloudflare immediately stops injecting new honeypot links into your pages. However, links generated while the feature was on remain valid for a limited time. Cloudflare still serves labyrinth content for these links, so you may continue to see AI Labyrinth actions in Security Analytics and Security Events until the links expire. This is expected behavior and does not mean the feature is still on.</p>
<h2 id="enable-ai-labyrinth">Enable AI Labyrinth</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3541.md")
</div>
