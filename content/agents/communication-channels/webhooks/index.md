<p>Receive webhook events from external services and route them to dedicated agent instances. Each webhook source (repository, customer, device) can have its own agent with isolated state, persistent storage, and real-time client connections.</p>
<h2 id="quick-start">Quick start</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1989.md")
</div>
<h2 id="use-cases">Use cases</h2>
<p>Webhooks combined with agents enable patterns where each external entity gets its own isolated, stateful agent instance.</p>
<h3 id="developer-tools">Developer tools</h3>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>GitHub Repo Monitor</strong></td>
<td>One agent per repository tracking commits, PRs, issues, and stars</td>
</tr>
<tr>
<td><strong>CI/CD Pipeline Agent</strong></td>
<td>React to build/deploy events, notify on failures, track deployment history</td>
</tr>
<tr>
<td><strong>Linear/Jira Tracker</strong></td>
<td>Auto-triage issues, assign based on content, track resolution times</td>
</tr>
</tbody>
</table>
<h3 id="e-commerce-and-payments">E-commerce and payments</h3>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Stripe Customer Agent</strong></td>
<td>One agent per customer tracking payments, subscriptions, and disputes</td>
</tr>
<tr>
<td><strong>Shopify Order Agent</strong></td>
<td>Order lifecycle from creation to fulfillment with inventory sync</td>
</tr>
<tr>
<td><strong>Payment Reconciliation</strong></td>
<td>Match webhook events to internal records, flag discrepancies</td>
</tr>
</tbody>
</table>
<h3 id="communication-and-notifications">Communication and notifications</h3>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Twilio SMS/Voice</strong></td>
<td>Conversational agents triggered by inbound messages or calls</td>
</tr>
<tr>
<td><strong>Slack Bot</strong></td>
<td>Respond to slash commands, button clicks, and interactive messages</td>
</tr>
<tr>
<td><strong>Email Tracking</strong></td>
<td>SendGrid/Mailgun delivery events, bounce handling, engagement analytics</td>
</tr>
</tbody>
</table>
<h3 id="iot-and-infrastructure">IoT and infrastructure</h3>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Device Telemetry</strong></td>
<td>One agent per device processing sensor data streams</td>
</tr>
<tr>
<td><strong>Alert Aggregation</strong></td>
<td>Collect alerts from PagerDuty, Datadog, or custom monitoring</td>
</tr>
<tr>
<td><strong>Home Automation</strong></td>
<td>React to IFTTT/Zapier triggers with persistent state</td>
</tr>
</tbody>
</table>
<h3 id="saas-integrations">SaaS integrations</h3>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>CRM Sync</strong></td>
<td>Salesforce/HubSpot contact and deal updates</td>
</tr>
<tr>
<td><strong>Calendar Agent</strong></td>
<td>Google Calendar event notifications and scheduling</td>
</tr>
<tr>
<td><strong>Form Submissions</strong></td>
<td>Typeform, Tally, or custom form webhooks with follow-up actions</td>
</tr>
</tbody>
</table>
<h2 id="routing-webhooks-to-agents">Routing webhooks to agents</h2>
<p>The key pattern is verifying the raw request before parsing it, then deriving the Agent identity from authenticated payload data. A body signature does not authenticate an unrelated URL segment or arbitrary header.</p>
<h3 id="extract-entity-from-payload">Extract entity from payload</h3>
<p>Most webhooks include an identifier in the payload:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1990.md")
</div>
<h3 id="validate-entity-ids-in-urls">Validate entity IDs in URLs</h3>
<p>A provider's body signature does not authenticate the webhook URL. If the URL includes an entity ID, compare it with the corresponding identity from the verified provider payload and reject a mismatch before calling <code>getAgentByName()</code>.</p>
<h3 id="derive-slack-identity-from-the-verified-body">Derive Slack identity from the verified body</h3>
<p>Slack does not send an authenticated <code>X-Slack-Team-Id</code> routing header. Validate Slack's timestamped signature and replay window against the raw body, then read <code>team_id</code> from the verified event or form body.</p>
<h2 id="signature-verification">Signature verification</h2>
<p>Always verify webhook signatures before trusting or processing the payload.</p>
<h3 id="github-hmac-sha256-pattern">GitHub HMAC-SHA256 pattern</h3>
<p>The quick start's <code>verifyGitHubWebhook()</code> helper verifies GitHub's <code>sha256=&lt;hex&gt;</code> signature over the raw body with <code>crypto.subtle.verify()</code>. This format is GitHub-specific. Other providers use different signature encodings, signed inputs, timestamp checks, and replay protections. Follow the provider documentation linked under <a href="#common-webhook-providers">Common webhook providers</a>.</p>
<h3 id="provider-specific-headers">Provider-specific headers</h3>
<table>
<thead>
<tr>
<th>Provider</th>
<th>Signature Header</th>
<th>Algorithm</th>
</tr>
</thead>
<tbody>
<tr>
<td>GitHub</td>
<td><code>X-Hub-Signature-256</code></td>
<td>HMAC-SHA256</td>
</tr>
<tr>
<td>Stripe</td>
<td><code>Stripe-Signature</code></td>
<td>HMAC-SHA256 (with timestamp)</td>
</tr>
<tr>
<td>Twilio</td>
<td><code>X-Twilio-Signature</code></td>
<td>HMAC-SHA1</td>
</tr>
<tr>
<td>Slack</td>
<td><code>X-Slack-Signature</code></td>
<td>HMAC-SHA256 (with timestamp)</td>
</tr>
<tr>
<td>Shopify</td>
<td><code>X-Shopify-Hmac-Sha256</code></td>
<td>HMAC-SHA256 (base64)</td>
</tr>
</tbody>
</table>
<h2 id="processing-webhooks">Processing webhooks</h2>
<h3 id="the-onrequest-handler">The onRequest handler</h3>
<p>Use <code>onRequest()</code> to handle incoming webhooks in your agent. If the Worker has not already verified the request, verify it before parsing the body. This example reuses the quick start's <code>verifyGitHubWebhook()</code> helper:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1991.md")
</div>
<h2 id="storing-webhook-events">Storing webhook events</h2>
<p>Use SQLite to persist webhook events for history and replay.</p>
<h3 id="event-table-schema">Event table schema</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1992.md")
</div>
<h3 id="cleanup-old-events">Cleanup old events</h3>
<p>Prevent unbounded growth by keeping only recent events:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1993.md")
</div>
<h3 id="query-events">Query events</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1994.md")
</div>
<h2 id="real-time-broadcasting">Real-time broadcasting</h2>
<p>When a webhook arrives, update agent state to automatically broadcast to connected WebSocket clients.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1995.md")
</div>
<p>On the client side:</p>
<pre><code class="language-tsx">import { useAgent } from &quot;agents/react&quot;;&#10;&#10;function Dashboard() {&#10;	const [state, setState] = useState(null);&#10;&#10;	const agent = useAgent({&#10;		agent: &quot;webhook-agent&quot;,&#10;		name: &quot;my-entity-id&quot;,&#10;		onStateUpdate: (newState) =&gt; {&#10;			setState(newState); // Automatically updates when webhooks arrive&#10;		},&#10;	});&#10;&#10;	return &lt;div&gt;Last event: {state?.lastEvent?.type}&lt;/div&gt;;&#10;}&#10;</code></pre>
<h2 id="patterns">Patterns</h2>
<h3 id="event-deduplication">Event deduplication</h3>
<p>Prevent processing duplicate events using event IDs:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1996.md")
</div>
<h3 id="respond-quickly-process-asynchronously">Respond quickly, process asynchronously</h3>
<p>Webhook providers expect fast responses. Use the queue for heavy processing:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1997.md")
</div>
<p>If the asynchronous work is a single Think chat turn, use <code>submitMessages()</code> instead. It returns a durable submission ID immediately and lets retries use an idempotency key instead of duplicating the message turn:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1998.md")
</div>
<p>If the webhook owns application side effects around a turn, such as restoring a provider thread and posting a visible reply, use <a href="/agents/runtime/execution/durable-execution/#startfiber"><code>startFiber()</code></a> around that job. Managed fibers retain status, dedupe provider retries, and let <code>onFiberRecovered()</code> or <code>resolveFiber()</code> record the app-level recovery outcome.</p>
<h3 id="multi-provider-routing">Multi-provider routing</h3>
<p>Use one typed helper for provider-specific verification and parsing. It must validate the raw request according to the provider documentation linked under <a href="#common-webhook-providers">Common webhook providers</a>, then derive <code>agentName</code> only from the verified body.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1999.md")
</div>
<h2 id="sending-outgoing-webhooks">Sending outgoing webhooks</h2>
<p>Agents can also send webhooks to external services:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2000.md")
</div>
<h2 id="security-best-practices">Security best practices</h2>
<ol>
<li><strong>Always verify signatures</strong> - Never trust unverified webhooks.</li>
<li><strong>Use environment secrets</strong> - Store secrets with <code>wrangler secret put</code>, not in code.</li>
<li><strong>Respond quickly</strong> - Return 200/202 within seconds to avoid retries.</li>
<li><strong>Validate payloads</strong> - Check required fields before processing.</li>
<li><strong>Log rejections</strong> - Track invalid signatures for security monitoring.</li>
<li><strong>Use HTTPS</strong> - Webhook URLs should always use TLS.</li>
</ol>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2001.md")
</div>
<h2 id="common-webhook-providers">Common webhook providers</h2>
<table>
<thead>
<tr>
<th>Provider</th>
<th>Documentation</th>
</tr>
</thead>
<tbody>
<tr>
<td>GitHub</td>
<td><a href="https://docs.github.com/en/webhooks">Webhook events and payloads</a></td>
</tr>
<tr>
<td>Stripe</td>
<td><a href="https://stripe.com/docs/webhooks/signatures">Webhook signatures</a></td>
</tr>
<tr>
<td>Twilio</td>
<td><a href="https://www.twilio.com/docs/usage/webhooks/webhooks-security">Validate webhook requests</a></td>
</tr>
<tr>
<td>Slack</td>
<td><a href="https://api.slack.com/authentication/verifying-requests-from-slack">Verifying requests</a></td>
</tr>
<tr>
<td>Shopify</td>
<td><a href="https://shopify.dev/docs/apps/webhooks/configuration/https#step-5-verify-the-webhook">Webhook verification</a></td>
</tr>
<tr>
<td>SendGrid</td>
<td><a href="https://docs.sendgrid.com/for-developers/tracking-events/getting-started-event-webhook">Event webhook</a></td>
</tr>
<tr>
<td>Linear</td>
<td><a href="https://developers.linear.app/docs/graphql/webhooks">Webhooks</a></td>
</tr>
</tbody>
</table>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/runtime/execution/queue-tasks/"><h3 id="card-queue-tasks-agents-runtime-execution-queue-tasks">Queue tasks</h3><p>Background task processing.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/communication-channels/email/"><h3 id="card-email-routing-agents-communication-channels-email">Email routing</h3><p>Handle inbound emails in your agent.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/agents-api/"><h3 id="card-agents-api-agents-runtime-agents-api">Agents API</h3><p>Complete API reference for the Agents SDK.</p></a></p>
