<p>Email is a communication channel for agents that need to interact with users or systems through inboxes instead of chat UIs. Agents can send outbound email, receive inbound email, route replies back to an existing session, and use email content as part of an agent workflow.</p>
<p>Use email when you want an agent to:</p>
<ul>
<li>Send notifications, summaries, receipts, or follow-up messages.</li>
<li>Process inbound messages through <a href="/email-service/">Cloudflare Email Service</a>.</li>
<li>Continue a conversation from a reply.</li>
<li>Route support, sales, or operational workflows through an agent.</li>
</ul>
<h2 id="how-it-works">How it works</h2>
<p>Outbound email uses a <code>send_email</code> binding in your Worker. Inbound email uses an Email Service routing rule that sends messages to your Worker, where the agent can parse the sender, recipients, headers, and body before deciding how to respond.</p>
<p>For reply handling, include a stable identifier in the reply address, message metadata, or headers so the Worker can route follow-up messages to the right agent instance.</p>
<h2 id="basic-pattern">Basic pattern</h2>
<p>Implement <code>onEmail()</code> to handle inbound email, and use <code>sendEmail()</code> or <code>replyToEmail()</code> when the agent needs to send a response.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1982.md")
</div>
<h2 id="configuration">Configuration</h2>
<p>Add a <code>send_email</code> binding for outbound email, then configure an Email Service routing rule to send inbound mail to your Worker.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1983.md")
</div>
<p>The <code>remote = true</code> option lets you call the real Email Service API during local development with <code>wrangler dev</code>.</p>
<h2 id="build-an-email-agent">Build an email agent</h2>
<p>For a complete walkthrough, including domain setup, bindings, inbound routing, and secure replies, use the email agent example.</p>
<p><a class="nb-card nb-link-card" href="/agents/examples/email-agent/"><h3 id="card-email-agent-agents-examples-email-agent">Email agent</h3><p>Build an agent that sends, receives, routes, and replies to email using Cloudflare Email Service and the Agents SDK.</p></a></p>
<h2 id="related-resources">Related resources</h2>
<p><a class="nb-card nb-link-card" href="/email-service/"><h3 id="card-email-service-email-service">Email Service</h3><p>Route, receive, and send email with Cloudflare Email Service.</p></a></p>
<p><a class="nb-card nb-link-card" href="/email-service/api/send-emails/workers-api/"><h3 id="card-send-email-from-workers-email-service-api-send-emails-workers-api">Send email from Workers</h3><p>Use the Workers API to send outbound email.</p></a></p>
