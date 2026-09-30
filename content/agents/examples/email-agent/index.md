<p>Agents can send and receive email with Cloudflare <a href="/email-service/api/route-emails/email-handler/">Email Service</a>. This guide shows how to send outbound email with the Workers binding, route inbound mail into Agents, and handle follow-up replies securely.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before using email with Agents, you need:</p>
<ol>
<li>A domain onboarded to <a href="/email-service/">Cloudflare Email Service</a>.</li>
<li>A <code>send_email</code> binding in <code>wrangler.jsonc</code> for outbound email.</li>
<li>An Email Service routing rule that sends inbound mail to your Worker.</li>
<li>Optional: an <code>EMAIL_SECRET</code> secret if you want secure reply routing.</li>
</ol>
<h3 id="domain-setup">Domain setup</h3>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com">Cloudflare Dashboard</a>.</li>
<li>Go to <strong>Compute &amp; AI</strong> &gt; <strong>Email Service</strong>.</li>
<li>Select <strong>Onboard Domain</strong> and choose your domain.</li>
<li>Add the DNS records (SPF and DKIM) to authorize sending.</li>
</ol>
<p>DNS changes usually complete within 5-15 minutes for domains using Cloudflare DNS, but can take up to 24 hours to propagate globally.</p>
<h3 id="wrangler-configuration">Wrangler configuration</h3>
<p>Add the email binding to your Worker:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1908.md")
</div>
<p>The <code>remote = true</code> option lets you call the real Email Service API during local development with <code>wrangler dev</code>.</p>
<h2 id="quick-start">Quick start</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1909.md")
</div>
<h2 id="sending-outbound-email">Sending outbound email</h2>
<h3 id="using-sendemail">Using <code>sendEmail()</code></h3>
<p><code>sendEmail()</code> sends outbound email through a <code>send_email</code> binding that you pass explicitly. It automatically injects agent routing headers (<code>X-Agent-Name</code>, <code>X-Agent-ID</code>) into every message, and optionally signs them with HMAC-SHA256 so that replies can be routed back to the same agent instance.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1910.md")
</div>
<p>When <code>secret</code> is provided, the agent signs the routing headers so that replies verified by <code>createSecureReplyEmailResolver</code> route back to the same agent instance.</p>
<p>Set <code>replyTo</code> to the mailbox that routes back to your Worker when you want recipients to continue the conversation with the same agent.</p>
<h2 id="routing-inbound-mail">Routing inbound mail</h2>
<p>Resolvers determine which Agent instance receives an incoming email. Choose the resolver that matches your use case.</p>
<p>For basic Email Service sending and receiving, <code>createAddressBasedEmailResolver()</code> is enough. The secure reply resolver below is optional and specific to Agents SDK reply signing, not a requirement of Email Service itself.</p>
<h3 id="createaddressbasedemailresolver"><code>createAddressBasedEmailResolver</code></h3>
<p>Recommended for inbound mail. Routes emails based on the recipient address.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1911.md")
</div>
<p><strong>Routing logic:</strong></p>
<table>
<thead>
<tr>
<th>Recipient Address</th>
<th>Agent Name</th>
<th>Agent ID</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>support@example.com</code></td>
<td><code>EmailAgent</code> (default)</td>
<td><code>support</code></td>
</tr>
<tr>
<td><code>sales@example.com</code></td>
<td><code>EmailAgent</code> (default)</td>
<td><code>sales</code></td>
</tr>
<tr>
<td><code>NotificationAgent+user123@example.com</code></td>
<td><code>NotificationAgent</code></td>
<td><code>user123</code></td>
</tr>
</tbody>
</table>
<p>The sub-address format (<code>agent+id@domain</code>) allows routing to different agent namespaces and instances from a single email domain.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1907.md")
</aside>
<h3 id="createsecurereplyemailresolver"><code>createSecureReplyEmailResolver</code></h3>
<p>For reply flows with signature verification. Verifies that incoming emails are authentic replies to your outbound emails, preventing attackers from routing emails to arbitrary agent instances.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1912.md")
</div>
<p>When your agent sends an email with <code>replyToEmail()</code> or <code>sendEmail()</code> and a <code>secret</code>, it signs the routing headers with a timestamp. When a reply comes back, this resolver verifies the signature and checks that it has not expired before routing.</p>
<p><strong>Options:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1913.md")
</div>
<p><strong>When to use:</strong> If your agent initiates email conversations and you need replies to route back to the same agent instance securely.</p>
<h3 id="createcatchallemailresolver"><code>createCatchAllEmailResolver</code></h3>
<p>For single-instance routing. Routes all emails to a specific agent instance regardless of the recipient address.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1914.md")
</div>
<p><strong>When to use:</strong> When you have a single agent instance that handles all emails (for example, a shared inbox).</p>
<h3 id="combining-resolvers">Combining resolvers</h3>
<p>You can combine resolvers to handle different scenarios:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1915.md")
</div>
<h2 id="handling-emails-in-your-agent">Handling emails in your Agent</h2>
<h3 id="the-agentemail-interface">The <code>AgentEmail</code> interface</h3>
<p>When your agent's <code>onEmail</code> method is called, it receives an <code>AgentEmail</code> object:</p>
<pre><code class="language-ts">type AgentEmail = {&#10;	from: string; // Sender&#x27;s email address&#10;	to: string; // Recipient&#x27;s email address&#10;	headers: Headers; // Email headers (subject, message-id, etc.)&#10;	rawSize: number; // Size of the raw email in bytes&#10;&#10;	getRaw(): Promise&lt;Uint8Array&gt;; // Get the full raw email content&#10;	reply(options): Promise&lt;void&gt;; // Send a reply&#10;	forward(rcptTo, headers?): Promise&lt;void&gt;; // Forward the email&#10;	setReject(reason): void; // Reject the email with a reason&#10;};&#10;</code></pre>
<h3 id="parsing-email-content">Parsing email content</h3>
<p>Use a library like <a href="https://www.npmjs.com/package/postal-mime">postal-mime</a> to parse the raw email:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1916.md")
</div>
<h3 id="detecting-auto-reply-emails">Detecting auto-reply emails</h3>
<p>Use <code>isAutoReplyEmail()</code> to detect auto-reply emails and avoid mail loops:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1917.md")
</div>
<p>This checks for standard RFC 3834 headers (<code>Auto-Submitted</code>, <code>X-Auto-Response-Suppress</code>, <code>Precedence</code>) that indicate an email is an auto-reply.</p>
<h3 id="replying-to-emails">Replying to emails</h3>
<p>Use <code>this.replyToEmail()</code> to send a reply through the inbound email's reply channel:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1918.md")
</div>
<h3 id="deferred-replies">Deferred replies</h3>
<p><code>replyToEmail()</code> requires a live <code>AgentEmail</code> object, so it only works inside <code>onEmail()</code>. If you need to reply later — from a scheduled task, a callable method, or after a human-in-the-loop approval — store the sender info in state and use <code>sendEmail()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1919.md")
</div>
<p>The <code>inReplyTo</code> field sets the <code>In-Reply-To</code> header so mail clients thread the reply correctly. The <code>secret</code> signs the agent routing headers so that follow-up replies route back to this agent instance via <code>createSecureReplyEmailResolver</code>.</p>
<h3 id="forwarding-emails">Forwarding emails</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1920.md")
</div>
<h3 id="rejecting-emails">Rejecting emails</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1921.md")
</div>
<h2 id="error-handling">Error handling</h2>
<p>When sending emails via <code>sendEmail()</code> or <code>replyToEmail()</code>, handle these common errors:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1922.md")
</div>
<h3 id="common-error-codes">Common error codes</h3>
<table>
<thead>
<tr>
<th>Error Code</th>
<th>Description</th>
<th>Solution</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>E_SENDER_NOT_VERIFIED</code></td>
<td>Sender domain/address not verified</td>
<td>Verify in Cloudflare dashboard</td>
</tr>
<tr>
<td><code>E_RATE_LIMIT_EXCEEDED</code></td>
<td>Sending rate limit reached</td>
<td>Implement exponential backoff</td>
</tr>
<tr>
<td><code>E_DAILY_LIMIT_EXCEEDED</code></td>
<td>Daily quota exceeded</td>
<td>Wait for quota reset or upgrade plan</td>
</tr>
<tr>
<td><code>E_CONTENT_TOO_LARGE</code></td>
<td>Email exceeds size limit</td>
<td>Reduce attachments or content</td>
</tr>
<tr>
<td><code>E_RECIPIENT_NOT_ALLOWED</code></td>
<td>Recipient not in allowed list</td>
<td>Check allowed destination addresses</td>
</tr>
<tr>
<td><code>E_RECIPIENT_SUPPRESSED</code></td>
<td>Recipient is on suppression list</td>
<td>Remove from suppression list</td>
</tr>
<tr>
<td><code>E_VALIDATION_ERROR</code></td>
<td>Invalid email format</td>
<td>Check email addresses</td>
</tr>
<tr>
<td><code>E_TOO_MANY_RECIPIENTS</code></td>
<td>More than 50 recipients</td>
<td>Split into multiple sends</td>
</tr>
</tbody>
</table>
<h2 id="secure-reply-routing">Secure reply routing</h2>
<p>When your agent sends emails and expects replies, use secure reply routing to prevent attackers from forging headers to route emails to arbitrary agent instances.</p>
<h3 id="how-it-works">How it works</h3>
<ol>
<li><strong>Outbound:</strong> When you call <code>replyToEmail()</code> or <code>sendEmail()</code> with a <code>secret</code>, the agent signs the routing headers (<code>X-Agent-Name</code>, <code>X-Agent-ID</code>) using HMAC-SHA256.</li>
<li><strong>Inbound:</strong> <code>createSecureReplyEmailResolver</code> verifies the signature before routing.</li>
<li><strong>Enforcement:</strong> If an email was routed via the secure resolver, <code>replyToEmail()</code> requires a secret (or explicit <code>null</code> to opt-out).</li>
</ol>
<h3 id="setup">Setup</h3>
<ol>
<li>Store the signing key as a Wrangler secret. Do not put it in <code>vars</code> or commit it to source control:</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler secret put EMAIL_SECRET</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler secret put EMAIL_SECRET" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler secret put EMAIL_SECRET</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler secret put EMAIL_SECRET" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler secret put EMAIL_SECRET</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler secret put EMAIL_SECRET" aria-label="Copy to clipboard">Copy</button></div></div>
<ol start="2">
<li>Use the combined resolver pattern:</li>
</ol>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1923.md")
</div>
<ol start="3">
<li>Sign outbound emails:</li>
</ol>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1924.md")
</div>
<h3 id="enforcement-behavior">Enforcement behavior</h3>
<p>When an email is routed via <code>createSecureReplyEmailResolver</code>, the <code>replyToEmail()</code> method enforces signing:</p>
<table>
<thead>
<tr>
<th><code>secret</code> value</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;my-secret&quot;</code></td>
<td>Signs headers (secure)</td>
</tr>
<tr>
<td><code>undefined</code> (omitted)</td>
<td><strong>Throws error</strong> - must provide secret or explicit opt-out</td>
</tr>
<tr>
<td><code>null</code></td>
<td>Allowed but not recommended - explicitly opts out of signing</td>
</tr>
</tbody>
</table>
<h2 id="complete-example">Complete example</h2>
<p>Here is a complete Email Service agent that sends outbound mail and handles secure replies:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1925.md")
</div>
<h2 id="api-reference">API reference</h2>
<h3 id="emailaddress"><code>EmailAddress</code></h3>
<pre><code class="language-ts">interface EmailAddress {&#10;	email: string;&#10;	name?: string;&#10;}&#10;</code></pre>
<h3 id="sendemail"><code>sendEmail</code></h3>
<pre><code class="language-ts">async sendEmail(options: {&#10;	binding: EmailSendBinding;&#10;	to: string | EmailAddress | (string | EmailAddress)[];&#10;	from: string | EmailAddress;&#10;	subject: string;&#10;	text?: string;&#10;	html?: string;&#10;	replyTo?: string | EmailAddress;&#10;	cc?: string | EmailAddress | (string | EmailAddress)[];&#10;	bcc?: string | EmailAddress | (string | EmailAddress)[];&#10;	inReplyTo?: string;&#10;	headers?: Record&lt;string, string&gt;;&#10;	secret?: string;&#10;}): Promise&lt;EmailSendResult&gt;;&#10;</code></pre>
<p>Send an outbound email through the Email Service binding. Automatically injects <code>X-Agent-Name</code> and <code>X-Agent-ID</code> headers. When <code>secret</code> is provided, signs headers with HMAC-SHA256 for secure reply routing.</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>binding</code></td>
<td>The <code>send_email</code> binding (for example, <code>this.env.EMAIL</code>). Required.</td>
</tr>
<tr>
<td><code>to</code></td>
<td>Recipient address, array of addresses, or <code>EmailAddress</code> object(s)</td>
</tr>
<tr>
<td><code>from</code></td>
<td>Sender address or <code>EmailAddress</code> object</td>
</tr>
<tr>
<td><code>subject</code></td>
<td>Email subject line</td>
</tr>
<tr>
<td><code>text</code></td>
<td>Plain text body (at least one of <code>text</code>/<code>html</code> required)</td>
</tr>
<tr>
<td><code>html</code></td>
<td>HTML body (at least one of <code>text</code>/<code>html</code> required)</td>
</tr>
<tr>
<td><code>replyTo</code></td>
<td>Reply-to address or <code>EmailAddress</code> object</td>
</tr>
<tr>
<td><code>cc</code></td>
<td>CC recipient address, array of addresses, or <code>EmailAddress</code> object(s)</td>
</tr>
<tr>
<td><code>bcc</code></td>
<td>BCC recipient address, array of addresses, or <code>EmailAddress</code> object(s)</td>
</tr>
<tr>
<td><code>inReplyTo</code></td>
<td>Message-ID for threading (sets the <code>In-Reply-To</code> header)</td>
</tr>
<tr>
<td><code>headers</code></td>
<td>Additional custom headers (agent headers take precedence if they collide)</td>
</tr>
<tr>
<td><code>secret</code></td>
<td>Secret for HMAC signing of agent routing headers</td>
</tr>
</tbody>
</table>
<h3 id="routeagentemail"><code>routeAgentEmail</code></h3>
<pre><code class="language-ts">function routeAgentEmail&lt;Env&gt;(&#10;	email: ForwardableEmailMessage,&#10;	env: Env,&#10;	options: {&#10;		resolver: EmailResolver;&#10;		onNoRoute?: (email: ForwardableEmailMessage) =&gt; void | Promise&lt;void&gt;;&#10;	},&#10;): Promise&lt;void&gt;;&#10;</code></pre>
<p>Routes an incoming email to the appropriate Agent based on the resolver's decision.</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>resolver</code></td>
<td>Function that determines which agent to route the email to</td>
</tr>
<tr>
<td><code>onNoRoute</code></td>
<td>Optional callback invoked when no routing information is found. Use this to reject the email or perform custom handling. If not provided, a warning is logged and the email is dropped.</td>
</tr>
</tbody>
</table>
<h3 id="createsecurereplyemailresolver-1"><code>createSecureReplyEmailResolver</code></h3>
<pre><code class="language-ts">function createSecureReplyEmailResolver(&#10;	secret: string,&#10;	options?: {&#10;		maxAge?: number;&#10;		onInvalidSignature?: (&#10;			email: ForwardableEmailMessage,&#10;			reason: SignatureFailureReason,&#10;		) =&gt; void;&#10;	},&#10;): EmailResolver;&#10;&#10;type SignatureFailureReason =&#10;	| &quot;missing_headers&quot;&#10;	| &quot;expired&quot;&#10;	| &quot;invalid&quot;&#10;	| &quot;malformed_timestamp&quot;;&#10;</code></pre>
<p>Creates a resolver for routing email replies with signature verification.</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>secret</code></td>
<td>Secret key for HMAC verification (must match the key used to sign)</td>
</tr>
<tr>
<td><code>maxAge</code></td>
<td>Maximum age of signature in seconds (default: 30 days / 2592000 seconds)</td>
</tr>
<tr>
<td><code>onInvalidSignature</code></td>
<td>Optional callback for logging when signature verification fails</td>
</tr>
</tbody>
</table>
<h3 id="signagentheaders"><code>signAgentHeaders</code></h3>
<pre><code class="language-ts">function signAgentHeaders(&#10;	secret: string,&#10;	agentName: string,&#10;	agentId: string,&#10;): Promise&lt;Record&lt;string, string&gt;&gt;;&#10;</code></pre>
<p>Manually sign agent routing headers. Returns an object with <code>X-Agent-Name</code>, <code>X-Agent-ID</code>, <code>X-Agent-Sig</code>, and <code>X-Agent-Sig-Ts</code> headers.</p>
<p>Useful when sending emails through external services while maintaining secure reply routing. The signature includes a timestamp and will be valid for 30 days by default.</p>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/runtime/communication/http-sse/"><h3 id="card-http-and-sse-agents-runtime-communication-http-sse">HTTP and SSE</h3><p>Handle HTTP requests in your Agent.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/communication-channels/webhooks/"><h3 id="card-webhooks-agents-communication-channels-webhooks">Webhooks</h3><p>Receive events from external services.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/agents-api/"><h3 id="card-agents-api-agents-runtime-agents-api">Agents API</h3><p>Complete API reference for the Agents SDK.</p></a></p>
