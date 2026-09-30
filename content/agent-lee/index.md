<div class="nb-description">
@markup("md", "content/.markup/bodies/1737.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="beta">Beta</h3>
@markup("md", "content/.markup/bodies/1736.md")
</aside>
<p>With Agent Lee, you can:</p>
<ul>
<li>Ask questions about your account configuration and get answers based on your actual data.</li>
<li>Make changes to DNS records, zone settings, and security rules, with your approval required before anything executes.</li>
<li>Run network diagnostics like DNS lookups and certificate checks.</li>
<li>Generate inline charts and visualizations from your account analytics.</li>
</ul>
<p>To get started, log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select <strong>Ask AI</strong> in the upper-right corner of any dashboard page.</p>
<hr />
<h2 id="capabilities">Capabilities</h2>
<h3 id="account-aware-answers">Account-aware answers</h3>
<p>Agent Lee answers based on your actual account data, not just documentation. When you ask a question, it fetches your zone configuration, DNS records, and security settings before responding.</p>
<h3 id="write-operations">Write operations</h3>
<p>You can ask Agent Lee to create, update, or delete resources across your account using natural language. Every write operation requires your explicit approval before it executes, Agent Lee shows you exactly what it plans to do and waits for confirmation.</p>
<p>Example requests:</p>
<ul>
<li>&quot;Add an A record for blog.example.com pointing to 192.0.2.10.&quot;</li>
<li>&quot;Enable Always Use HTTPS on my zone.&quot;</li>
<li>&quot;Set the SSL mode for example.com to Full (strict).&quot;</li>
</ul>
<h3 id="network-diagnostics">Network diagnostics</h3>
<p>Run diagnostic commands to troubleshoot connectivity and configuration issues:</p>
<ul>
<li><strong>DNS lookups</strong>: Query DNS records for any domain</li>
<li><strong>Certificate checks</strong>: Inspect TLS/SSL certificates</li>
<li><strong>Domain information</strong>: Look up WHOIS and RDAP registration data</li>
</ul>
<h3 id="generative-ui">Generative UI</h3>
<p>Agent Lee renders inline charts and data visualizations directly in the chat panel based on your account analytics.
Example requests:</p>
<ul>
<li>&quot;Show me a chart of my traffic over the last 7 days.&quot;</li>
<li>&quot;What does my error rate look like for the past 24 hours?&quot;</li>
</ul>
<hr />
<h2 id="data-access-and-privacy">Data access and privacy</h2>
<h3 id="what-agent-lee-can-access">What Agent Lee can access</h3>
<ul>
<li>Zone settings, DNS records, firewall and WAF rules</li>
<li>Workers scripts, routes, and bindings</li>
<li>R2 bucket names, Cloudflare Tunnel configuration, cache rules</li>
<li>Registrar domain data, account plan and usage metadata</li>
</ul>
<p>Agent Lee fetches this data on demand when your question requires it.</p>
<h3 id="what-agent-lee-cannot-access">What Agent Lee cannot access</h3>
<ul>
<li>Payment methods, billing history, or invoice details</li>
<li>Account passwords, login credentials, or API tokens</li>
<li>Raw log data or Logpush datasets</li>
<li>Data from other Cloudflare accounts</li>
</ul>
<h3 id="conversation-storage">Conversation storage</h3>
<p>Conversations are stored per user using <a href="/durable-objects/">Durable Objects</a>, isolated to your account. Conversation data is retained for one year in accordance with Cloudflare's data retention policy. Agent Lee does not currently reference previous conversation context when responding.</p>
<h3 id="data-usage">Data usage</h3>
<p>Agent Lee does not currently use your conversations, prompts, or account data to train AI models, nor do we share your data with other Cloudflare customers. Should these practices change in the future, we will provide advance notice to keep you informed. For Cloudflare's authoritative data handling commitments, refer to the <a href="https://www.cloudflare.com/privacypolicy/">Cloudflare Privacy Policy</a>.</p>
<hr />
<h2 id="limitations">Limitations</h2>
<p>Agent Lee cannot:</p>
<ul>
<li>Write Workers scripts or generate application code</li>
<li>Replace <a href="https://support.cloudflare.com">Cloudflare Support</a> for billing issues, account recovery, or outages</li>
<li>Access payment methods, billing history, or API tokens</li>
<li>Operate across multiple accounts: sessions are scoped to your authenticated account</li>
<li>Remember previous conversations: each session starts fresh</li>
<li>Query raw log data or Logpush datasets</li>
<li>Execute write operations without your explicit approval</li>
</ul>
<p>Agent Lee is entirely optional. If you do not open the Ask AI panel, none of your data is sent to or processed by it.</p>
<hr />
<h2 id="built-on-cloudflare">Built on Cloudflare</h2>
<p>Agent Lee is built on Cloudflare's own developer platform using the same primitives available to any Cloudflare developer.</p>
<table>
<thead>
<tr>
<th>Component</th>
<th>Role</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/agents/">Agents SDK</a></td>
<td>Agent lifecycle, state management, and scheduling</td>
</tr>
<tr>
<td><a href="/durable-objects/">Durable Objects</a></td>
<td>Per-user conversation storage and write approval gate</td>
</tr>
<tr>
<td><a href="/workers-ai/">Workers AI</a></td>
<td>LLM inference</td>
</tr>
<tr>
<td><a href="/agents/model-context-protocol/apis/agent-api/">Cloudflare MCP server</a></td>
<td>Tool definitions for Cloudflare API operations</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/agents/">Agents SDK</a></li>
<li><a href="/agents/concepts/agentic-patterns/human-in-the-loop/">Human in the Loop</a></li>
<li><a href="/workers-ai/">Workers AI</a></li>
<li><a href="https://blog.cloudflare.com/introducing-agent-lee">Blog post: Introducing Agent Lee</a></li>
</ul>
