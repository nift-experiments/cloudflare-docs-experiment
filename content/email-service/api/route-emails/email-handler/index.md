<p class="article-summary">Process incoming emails with the email() handler in Cloudflare Workers. Forward, reply, reject, or process emails programmatically.
</p>
<p>Process incoming emails using the <code>email()</code> handler in your Cloudflare Workers. This allows you to programmatically handle email routing with custom logic.</p>
<h2 id="email-handler-syntax">Email handler syntax</h2>
<p>Add the <code>email</code> handler function to your Worker's exported handlers:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8648.md")
</div></div>
<h3 id="parameters">Parameters</h3>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>message</code></td>
<td><code>ForwardableEmailMessage</code></td>
<td>The incoming email message</td>
</tr>
<tr>
<td><code>env</code></td>
<td><code>object</code></td>
<td>Worker environment bindings (KV, EMAIL, etc.)</td>
</tr>
<tr>
<td><code>ctx</code></td>
<td><code>object</code></td>
<td>Execution context with <code>waitUntil</code> function</td>
</tr>
</tbody>
</table>
<h2 id="forwardableemailmessage-interface"><code>ForwardableEmailMessage</code> interface</h2>
<p>The <code>message</code> parameter provides access to the incoming email:</p>
<pre><code class="language-ts">interface ForwardableEmailMessage {&#10;	readonly from: string; // Sender email address (envelope MAIL FROM)&#10;	readonly to: string; // Recipient email address (envelope RCPT TO)&#10;	readonly headers: Headers; // Email headers (Subject, Message-ID, etc.)&#10;	readonly raw: ReadableStream; // Raw MIME email content stream&#10;	readonly rawSize: number; // Size of raw email in bytes&#10;	readonly canBeForwarded: boolean; // Whether the message can be forwarded&#10;&#10;	// Actions&#10;	setReject(reason: string): void;&#10;	forward(rcptTo: string, headers?: Headers): Promise&lt;EmailSendResult&gt;;&#10;	reply(message: EmailMessage): Promise&lt;EmailSendResult&gt;;&#10;}&#10;</code></pre>
<h3 id="properties">Properties</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8651.md")
</div></div>
<h2 id="email-actions">Email actions</h2>
<h3 id="forward-emails">Forward emails</h3>
<p>Forward incoming emails to verified destination addresses:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8655.md")
</div></div>
<h3 id="forward-with-custom-headers">Forward with custom headers</h3>
<p>Add custom headers when forwarding. Only headers with an <code>X-</code> prefix can be added through <code>forward()</code>. Other headers are removed.</p>
<pre><code class="language-ts">export default {&#10;	async email(message, env, ctx): Promise&lt;void&gt; {&#10;		// Create custom headers&#10;		const customHeaders = new Headers();&#10;		customHeaders.set(&quot;X-Processed-By&quot;, &quot;Email-Worker&quot;);&#10;		customHeaders.set(&quot;X-Processing-Time&quot;, new Date().toISOString());&#10;		customHeaders.set(&quot;X-Original-Recipient&quot;, message.to);&#10;		customHeaders.set(&quot;X-Spam-Score&quot;, &quot;0.1&quot;); // Example spam score&#10;&#10;		// Forward with custom headers&#10;		await message.forward(&quot;processed@example.com&quot;, customHeaders);&#10;	},&#10;};&#10;</code></pre>
<h3 id="reply-to-emails">Reply to emails</h3>
<p>Send automatic replies with <code>message.reply()</code>. Replies built this way are threaded with the original message and pass through the same SMTP session, so they preserve the original <code>Message-ID</code> chain.</p>
<p>Replies through the Workers API must satisfy the following requirements, otherwise <code>reply()</code> throws an exception:</p>
<ul>
<li>The incoming email must have a valid DMARC result.</li>
<li>An email can only be replied to once per <code>EmailMessage</code> event.</li>
<li>The recipient in the reply must match the sender of the incoming email.</li>
<li>The outgoing sender domain must match the domain that received the email.</li>
<li>The reply is rejected if the incoming email has more than 100 entries in its <code>References</code> header, to prevent reply loops and abuse.</li>
</ul>
<p>The reply payload is an <code>EmailMessage</code> built from a raw MIME string. The examples below use <a href="https://www.npmjs.com/package/mimetext"><code>mimetext</code></a> to build the MIME body. The <code>mimetext</code> package requires the <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code></a> compatibility flag.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8658.md")
</div></div>
<h3 id="reject-emails">Reject emails</h3>
<p>Reject emails with a permanent SMTP error:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8661.md")
</div></div>
<h2 id="error-handling">Error handling</h2>
<p>Handle errors gracefully in email processing:</p>
<pre><code class="language-ts">export default {&#10;	async email(message, env, ctx): Promise&lt;void&gt; {&#10;		try {&#10;			// Main email processing logic&#10;			await processEmail(message, env);&#10;		} catch (error) {&#10;			console.error(&quot;Email processing failed:&quot;, error);&#10;&#10;			// Log error for monitoring&#10;			if (env.ERROR_LOGS) {&#10;				await env.ERROR_LOGS.put(&#10;					`error-${Date.now()}`,&#10;					JSON.stringify({&#10;						error: error.message,&#10;						stack: error.stack,&#10;						from: message.from,&#10;						to: message.to,&#10;						timestamp: new Date().toISOString(),&#10;					}),&#10;				);&#10;			}&#10;&#10;			// Fallback: forward to admin&#10;			try {&#10;				await message.forward(&quot;admin@example.com&quot;);&#10;			} catch (fallbackError) {&#10;				console.error(&quot;Fallback forwarding failed:&quot;, fallbackError);&#10;				// Last resort: reject the email&#10;				message.setReject(&quot;Internal processing error&quot;);&#10;			}&#10;		}&#10;	},&#10;};&#10;&#10;async function processEmail(message, env) {&#10;	// Your main email processing logic here&#10;	const recipient = message.to;&#10;&#10;	if (recipient.includes(&quot;support@&quot;)) {&#10;		await message.forward(&quot;support@example.com&quot;);&#10;	} else if (recipient.includes(&quot;sales@&quot;)) {&#10;		await message.forward(&quot;sales@example.com&quot;);&#10;	} else {&#10;		await message.forward(&quot;general@example.com&quot;);&#10;	}&#10;}&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Test locally: <a href="/email-service/local-development/routing/">Email routing development</a></li>
<li>Manage rules and addresses programmatically with the <a href="/email-service/platform/email-routing-rest-api/">Email Routing REST API</a></li>
<li>Set up <a href="/email-service/configuration/email-routing-addresses/">email routing configuration</a></li>
<li>See <a href="/email-service/examples/email-routing/">email routing examples</a> for advanced email processing</li>
<li>Learn about <a href="/email-service/examples/email-routing/spam-filtering/">spam filtering</a> with Workers</li>
</ul>
