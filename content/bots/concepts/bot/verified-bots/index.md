<p>A <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3565.md")
</div> is a bot or agent that Cloudflare has confirmed is **transparent about who it is and what it does**: it represents itself honestly and does not abuse the access that honesty earns. Examples include search engine crawlers, monitoring services, and user-driven agents.
<p>Being Verified means a bot or agent meets two bars:</p>
<ol>
<li><strong>Honest self-identification</strong> — it declares who it is deterministically, through a cryptographic <a href="/bots/reference/bot-verification/web-bot-auth/">Web Bot Auth</a> signature, a published IP list with a stable user-agent, or reverse DNS.</li>
<li><strong>Non-abusive behavior</strong> — it obeys <code>robots.txt</code> and crawl directives, maintains reasonable request rates, and has not been observed evading website owner preferences or attacking sites.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="signed-agents-are-now-verified">Signed agents are now Verified</h3>
@markup("md", "content/.markup/bodies/3564.md")
</aside>
<h2 id="classification">Classification</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3563.md")
</aside>
<p>Cloudflare classifies each tracked bot by its behavior — what the bot may do on your site. A single bot can have one or more of the following behaviors:</p>
<table>
<thead>
<tr>
<th>Behavior</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Search</td>
<td>Crawling to build search indexes or RAG databases.</td>
</tr>
<tr>
<td>Agent</td>
<td>User-directed agents visiting a page on behalf of a human.</td>
</tr>
<tr>
<td>Training</td>
<td>Crawling to train or fine-tune models.</td>
</tr>
<tr>
<td>Transact</td>
<td>Checkout or other transaction actions on behalf of users.</td>
</tr>
<tr>
<td>Data Collection</td>
<td>Price scraping, competitive intelligence gathering, and third-party analytics.</td>
</tr>
<tr>
<td>Security Testing</td>
<td>Vulnerability scanning and penetration testing.</td>
</tr>
<tr>
<td>SEO</td>
<td>SEO crawling, site auditing, and accessibility checks.</td>
</tr>
<tr>
<td>Ads Verification</td>
<td>Ad placement verification and ad fraud detection.</td>
</tr>
<tr>
<td>Social / Link Preview</td>
<td>Link previews for social platforms and messaging apps.</td>
</tr>
<tr>
<td>Feed Fetching</td>
<td>RSS readers, podcast aggregators, and news feed bots.</td>
</tr>
<tr>
<td>Monitoring &amp; Operations</td>
<td>Uptime monitoring, webhooks, and health checks.</td>
</tr>
</tbody>
</table>
<p>Search, Agent, and Training are also available as managed presets you can act on across all plans. For more information, refer to <a href="/bots/concepts/bot/#ai-bots">AI bots</a>.</p>
<p>Cloudflare also labels every Verified bot or agent by how it is operated.</p>
<table>
<thead>
<tr>
<th>Label</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Direct</strong></td>
<td>Operated by a single, narrow operator — usually on the operator's own infrastructure. Only that operator can send requests that present as this bot.</td>
</tr>
<tr>
<td><strong>Intermediary</strong></td>
<td>An agentic service that a wide range of end users can operate. The operator runs the software, but each action is initiated by a different end user.</td>
</tr>
</tbody>
</table>
<p>Because an <strong>intermediary</strong> acts on behalf of many different end users, the operator and the end user are not the same party. This introduces <strong>transitive trust</strong>: you may trust the intermediary operator, but not necessarily every end user driving it. Cloudflare is experimenting with forwarding information about the end user (using the <code>Forwarded</code> header defined in <a href="https://www.rfc-editor.org/info/rfc7239">RFC 7239</a>) so that website owners can apply their preferences to the party ultimately responsible for a request.</p>
<h2 id="becoming-a-verified-bot">Becoming a Verified bot</h2>
<p>You can request for your bot or agent to be added to Cloudflare's bots and agents directory by filling out an <a href="https://dash.cloudflare.com/?to=/:account/configurations/verified-bots">online application</a> in the Cloudflare dashboard.</p>
<p>Once Cloudflare approves a Verified bot, it should appear in <a href="/bots/botbase/">BotBase</a>, shared through <a href="https://radar.cloudflare.com/verified-bots">Cloudflare Radar's bots and agents directory</a>.</p>
<p>The bot must be Verified using one of the following validation methods:</p>
<ul>
<li><a href="/bots/reference/bot-verification/web-bot-auth/">Web Bot Auth</a></li>
<li><a href="/bots/reference/bot-verification/ip-validation/">IP validation</a></li>
</ul>
<h3 id="breach-of-policy">Breach of policy</h3>
<p>If any of the requirements to validate are breached, a service will be removed from the global allowlist.</p>
<p>The following are examples of breaches of policy:</p>
<ul>
<li>Adding a set of IPs that are not solely used by Verified service.</li>
<li>The service IPs are breached by an attacker.</li>
<li>The service has vulnerabilities that have not been patched.</li>
<li>A block of IPs not briefed on onboarding is added to the list.</li>
<li>The disclosed purpose of the service does not reflect on the traffic.</li>
<li>An AI Crawler that does not respect the crawl-delay directive in robots.txt.</li>
</ul>
<h2 id="legacy-categories">Legacy categories</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3562.md")
</aside>
<details>
<summary>Academic research</summary>
<p><strong>String value</strong>: <code>Academic Research</code></p>
<p><strong>Definition</strong>: Gathers data for scholarly research or academic purposes.</p>
<p><strong>Example</strong>: Library of Congress, TurnItInBot, Bibliothèque nationale de France</p>
</details>
<details>
<summary>Accessibility</summary>
<p><strong>String value</strong>: <code>Accessibility</code></p>
<p><strong>Definition</strong>: Scans websites to identify their accessibility.</p>
<p><strong>Example</strong>: Accessible Web Bot</p>
</details>
<details>
<summary>Advertising or marketing</summary>
<p><strong>String value</strong>: <code>Advertising &amp; Marketing</code></p>
<p><strong>Definition</strong>: Automates marketing tasks including, but not limited to, ad placement and performance tracking.</p>
<p><strong>Example</strong>: Google Adsbot</p>
</details>
<details>
<summary>Aggregators</summary>
<p><strong>String value</strong>: <code>Aggregator</code></p>
<p><strong>Definition</strong>: Collects content from various online sources and consolidates it in one place.</p>
<p><strong>Example</strong>: Pinterest, Indeed Jobsbot</p>
</details>
<details>
<summary>AI Assistant</summary>
<p><strong>String value</strong>: <code>AI Assistant</code></p>
<p><strong>Definition</strong>: Automated AI bot driven by user action.</p>
<p><strong>Example</strong>: Perplexity-User, DuckAssistBot</p>
</details>
<details>
<summary>AI Crawler</summary>
<p><strong>String value</strong>: <code>AI Crawler</code></p>
<p><strong>Definition</strong>: Crawls websites for content that is used for training AI models.</p>
<p><strong>Example</strong>: Google Bard, ChatGPT bot</p>
</details>
<details>
<summary>AI Search</summary>
<p><strong>String value</strong>: <code>AI Search</code></p>
<p><strong>Definition</strong>: Powers AI-driven search experiences.</p>
<p><strong>Example</strong>: OAI-SearchBot</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3561.md")
</aside>
</details>
<details>
<summary>Archiver</summary>
<p><strong>String value</strong>: <code>Archiver</code></p>
<p><strong>Definition</strong>: Saves snapshots of websites to preserve digital content for historical records.</p>
<p><strong>Example</strong>: Internet Archive, CommonCrawl</p>
</details>
<details>
<summary>Feed fetcher</summary>
<p><strong>String value</strong>: <code>Feed Fetcher</code></p>
<p><strong>Definition</strong>: Retrieves updates from feeds to power readers or other applications.</p>
<p><strong>Example</strong>: RSS or Podcast feed updaters</p>
</details>
<details>
<summary>Monitoring or analytics</summary>
<p><strong>String value</strong>: <code>Monitoring &amp; Analytics</code></p>
<p><strong>Definition</strong>: Tracks a website's uptime, performance, and user traffic to gather key monitoring metrics.</p>
<p><strong>Example</strong>: Uptime Monitors</p>
</details>
<details>
<summary>Page preview</summary>
<p><strong>String value</strong>: <code>Page Preview</code></p>
<p><strong>Definition</strong>: Generates previews for links shared on social media or in messaging apps.</p>
<p><strong>Example</strong>: Facebook, Slack, Twitter, or Discord Link Preview tools</p>
</details>
<details>
<summary>Search engine crawler</summary>
<p><strong>String value</strong>: <code>Search Engine Crawler</code></p>
<p><strong>Definition</strong>: A bot that discovers and indexes web pages for search results.</p>
<p><strong>Example</strong>: Googlebot, Bingbot, Yandexbot, Baidubot</p>
</details>
<details>
<summary>Search engine optimization</summary>
<p><strong>String value</strong>: <code>Search Engine Optimization</code></p>
<p><strong>Definition</strong>: Analyzes websites to improve their standing in search engine results pages.</p>
<p><strong>Example</strong>: Google Lighthouse, GT Metrix, Pingdom, AddThis</p>
</details>
<details>
<summary>Security</summary>
<p><strong>String value</strong>: <code>Security</code></p>
<p><strong>Definition</strong>: Scans websites to detect security vulnerabilities and potential threats.</p>
<p><strong>Example</strong>: Vulnerability Scanners, SSL Domain Control Validation (DCV) Check Tools</p>
</details>
<details>
<summary>Social media marketing</summary>
<p><strong>String value</strong>: <code>Social Media Marketing</code></p>
<p><strong>Definition</strong>: Manages and automates activities on social platforms.</p>
<p><strong>Example</strong>: Brandwatch</p>
</details>
<details>
<summary>Webhooks</summary>
<p><strong>String value</strong>: <code>Webhooks</code></p>
<p><strong>Definition</strong>: An automated messenger that sends data from one application to another for specific events.</p>
<p><strong>Example</strong>: Payment processors, WordPress Integration tools</p>
</details>
<details>
<summary>Other</summary>
<p><strong>String value</strong>: <code>Other</code></p>
<p><strong>Definition</strong>: A dedicated category for bots that do not fit into the other classifications.</p>
</details>
<p>Cloudflare reserves the right to re-assign Verified bot categories if the bot's public documentation and observed behavior differ from the category listed in the bot submission form.</p>
<h2 id="availability">Availability</h2>
<p>Historically, Verified bots have been excluded in default bot configurations across all plans. Now, all customers have the option to <a href="/bots/additional-configurations/block-ai-bots/">configure AI bot policies</a> to define their block vs. allow expectations.</p>
