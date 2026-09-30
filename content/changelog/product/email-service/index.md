<h1 id="changelog">Changelog</h1>

<h2 id="preview-sent-emails-in-the-activity-log"><a href="/changelog/post/2026-07-17-email-message-preview/">Preview sent emails in the Activity log</a></h2>
<p><em>2026-07-17</em></p>
<p>You can now preview the content of sent emails directly from the Email Service Activity log. Expand a sent email and open the new <strong>Preview</strong> section to inspect the message as it was sent, across tabs for the rendered <strong>HTML</strong> body, the <strong>Text</strong> body, the <strong>Headers</strong>, the <strong>Attachments</strong>, and the full <strong>Raw</strong> <a href="https://datatracker.ietf.org/doc/html/rfc5322">RFC 5322</a> source.</p>
<p><img src="/assets/upstream/images/changelog/email-service/email-message-preview.png" alt="The rendered HTML preview of a sent email in the Email Service Activity log" /></p>
<p>Previously, the Activity log surfaced delivery and authentication metadata but not the message content, making rendering and content issues harder to debug. Message preview closes that gap.</p>
<p>To make messages previewable, turn on <strong>Email preview</strong> in your sending domain's settings. Previews cover messages sent while the setting is turned on and are retained for about seven days. Sending domains onboarded on or after 2026-07-02 have <strong>Email preview</strong> turned on automatically.</p>
<p><img src="/assets/upstream/images/changelog/email-service/email-preview-setting.png" alt="The Email preview setting in a sending domain's settings" /></p>
<p>Refer to <a href="/email-service/observability/logs/#message-preview">Email logs</a> for more information.</p>


<h2 id="subscribe-to-email-sending-events-with-queues"><a href="/changelog/post/2026-07-15-event-subscriptions/">Subscribe to Email Sending events with Queues</a></h2>
<p><em>2026-07-15</em></p>
<p>You can now subscribe to <strong><a href="/email-service/api/send-emails/">Email Sending</a> events</strong> through <a href="/queues/event-subscriptions/">Queues event subscriptions</a> and receive outbound transactional email lifecycle events on a queue. Each subscription is scoped to one sending domain — either the zone apex, such as <code>example.com</code>, or a verified sending subdomain, such as <code>send.example.com</code>.</p>
<p>Six event types are published: <code>message.delivered</code>, <code>message.deferred</code>, <code>message.bounced</code>, <code>message.failed</code>, <code>message.rejected</code>, and <code>message.complained</code>. Use them to track deliverability, react to bounces and complaints, and drive suppression or retry logic. Email Routing events are not published on this source.</p>
<p>Each event includes the message details, delivery status, and SMTP response:</p>
<pre><code class="language-json">{&#10;	&quot;type&quot;: &quot;cf.email.sending.message.delivered&quot;,&#10;	&quot;source&quot;: {&#10;		&quot;type&quot;: &quot;email.sending&quot;,&#10;		&quot;zoneId&quot;: &quot;023e105f4ecef8ad9ca31a8372d0c353&quot;,&#10;		&quot;domain&quot;: &quot;example.com&quot;&#10;	},&#10;	&quot;payload&quot;: {&#10;		&quot;messageId&quot;: &quot;0101018f7d0c4d9a-msg-deadbeef&quot;,&#10;		&quot;recipient&quot;: &quot;user@example.net&quot;,&#10;		&quot;terminal&quot;: true,&#10;		&quot;delivery&quot;: {&#10;			&quot;status&quot;: &quot;delivered&quot;,&#10;			&quot;smtpStatusCode&quot;: &quot;250&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Refer to <a href="/email-service/platform/event-subscriptions/">Event subscriptions</a> to see all event types and example payloads.</p>


<h2 id="authenticated-smtp-submission-now-available-in-beta"><a href="/changelog/post/2026-06-08-smtp-submission/">Authenticated SMTP submission now available in beta</a></h2>
<p><em>2026-06-08</em></p>
<p>You can now send emails through <strong>Cloudflare Email Service</strong> using authenticated <a href="/email-service/api/send-emails/smtp/">SMTP submission</a> on <code>smtp.mx.cloudflare.net:465</code>. SMTP joins the <a href="/email-service/api/send-emails/rest-api/">REST API</a> and the <a href="/email-service/api/send-emails/workers-api/">Workers binding</a> as a third way to send transactional email — useful for existing applications that already speak SMTP and language-native SMTP libraries (Nodemailer, <code>smtplib</code>, PHPMailer, JavaMail).</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Host</td>
<td><code>smtp.mx.cloudflare.net</code></td>
</tr>
<tr>
<td>Port</td>
<td><code>465</code> (implicit TLS)</td>
</tr>
<tr>
<td>AUTH</td>
<td><code>PLAIN</code> or <code>LOGIN</code></td>
</tr>
<tr>
<td>Username</td>
<td><code>api_token</code></td>
</tr>
<tr>
<td>Password</td>
<td>A Cloudflare API token (account-owned or user-owned) with <strong>Email Sending: Edit</strong></td>
</tr>
</tbody>
</table>
<p>Submissions enter the same delivery pipeline as the REST API and Workers binding: identical <a href="/email-service/platform/limits/">limits</a>, automatic DKIM and ARC signing, and shared dashboard logs.</p>
<p>Send your first email with a single command:</p>
<pre><code class="language-sh">curl --ssl-reqd \&#10;  &#45;-url &quot;smtps://smtp.mx.cloudflare.net:465&quot; \&#10;  &#45;-user &quot;api_token:&lt;API_TOKEN&gt;&quot; \&#10;  &#45;-mail-from &quot;welcome@yourdomain.com&quot; \&#10;  &#45;-mail-rcpt &quot;user@example.com&quot; \&#10;  &#45;-upload-file mail.txt&#10;</code></pre>
<p>Refer to the <a href="/email-service/api/send-emails/smtp/">SMTP reference</a> for authentication details, response codes, and language-specific examples.</p>


<h2 id="send-emails-with-named-recipient-addresses"><a href="/changelog/post/2026-05-28-named-email-recipients/">Send emails with named recipient addresses</a></h2>
<p><em>2026-05-28</em></p>
<p>You can now send emails with display names on recipient addresses in addition to the existing <code>from</code> support. Pass an object with <code>email</code> and an optional <code>name</code> field for <code>to</code>, <code>cc</code>, <code>bcc</code>, <code>replyTo</code>, or <code>from</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17723.md")</div>
<p>Plain strings remain fully supported for backward compatibility, and you can mix strings and named objects in the same array.</p>
<p>Refer to the <a href="/email-service/api/send-emails/workers-api/">Workers API</a> and <a href="/email-service/api/send-emails/rest-api/">REST API</a> documentation for full request examples.</p>


<h2 id="email-sending-now-in-public-beta"><a href="/changelog/post/2026-04-16-email-sending-public-beta/">Email Sending now in public beta</a></h2>
<p><em>2026-04-16</em></p>
<p><strong><a href="/email-service/api/send-emails/">Email Sending</a></strong> is now in public beta. Send transactional emails directly from Workers (<code>env.EMAIL.send()</code>) or the REST API, with support for HTML, plain text, attachments, inline images, and custom headers. Email Sending joins <a href="https://blog.cloudflare.com/introducing-email-routing/">Email Routing</a> under the new <strong>Cloudflare Email Service</strong> — a single service for sending and receiving email on the Cloudflare developer platform.</p>
<p>Send an email from a Worker in a few lines of code:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17722.md")</div>
<p>Email Service also integrates with the <a href="/agents/">Agents SDK</a>, giving your agents a native <code>onEmail</code> hook to receive, process, and reply to emails. Combined with the new <a href="https://github.com/cloudflare/mcp-server-cloudflare">Email MCP server</a> and Wrangler CLI email commands, any agent can send email regardless of where it runs.</p>
<p>Start sending and receiving emails from Workers and agents today. Email Sending is available on the Workers paid plan. Refer to the <a href="/email-service/">Email Service documentation</a> to get started.</p>


<h2 id="subaddressing-support-in-email-routing"><a href="/changelog/post/2025-07-21-subaddressing/">Subaddressing support in Email Routing</a></h2>
<p><em>2025-07-21</em></p>
<p>Subaddressing, as defined in <a href="https://www.rfc-editor.org/rfc/rfc5233">RFC 5233</a>, also known as plus addressing, is now supported in Email Routing. This enables using the &quot;+&quot; separator to augment your custom addresses with arbitrary detail information.</p>
<p>Now you can send an email to <code>user+detail@example.com</code> and it will be captured by the <code>user@example.com</code> custom address. The <code>+detail</code> part is ignored by Email Routing, but it can be captured next in the processing chain in the logs, an <a href="/email-service/api/route-emails/email-handler/">Email Worker</a> or an <a href="https://github.com/cloudflare/agents/tree/main/examples/email-agent">Agent application</a>.</p>
<p>Customers can use this feature to dynamically add context to their emails, such as tracking the source of an email or categorizing emails without needing to create multiple custom addresses.</p>
<p><img src="/assets/upstream/images/changelog/email-service/subaddressing.png" alt="Subaddressing" /></p>
<p>Check our <a href="/email-service/configuration/email-routing-addresses/#subaddressing">Developer Docs</a> to learn how to enable subaddressing in Email Routing.</p>


<h2 id="mail-authentication-requirements-for-email-routing"><a href="/changelog/post/2025-06-30-mail-authentication/">Mail authentication requirements for Email Routing</a></h2>
<p><em>2025-06-30</em></p>
<p>The Email Routing platform supports <a href="https://datatracker.ietf.org/doc/html/rfc7208">SPF</a> records and <a href="https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail">DKIM (DomainKeys Identified Mail)</a> signatures and
honors these protocols when the sending domain has them configured. However, if the sending domain doesn't implement them,
we still forward the emails to upstream mailbox providers.</p>
<p>Starting on July 3, 2025, we will require all emails to be authenticated using at least one of the protocols, SPF or DKIM, to
forward them. We also strongly recommend that all senders implement the DMARC protocol.</p>
<p>If you are using a Worker with an Email trigger to receive email messages and forward them upstream, you will need to handle the case where
the forward action may fail due to missing authentication on the incoming email.</p>
<p>SPAM has been a long-standing issue with email. By enforcing mail authentication, we will increase the efficiency of identifying abusive senders and blocking
bad emails.
If you're an email server delivering emails to large mailbox providers, it's likely you already use these protocols; otherwise, please ensure
you have them properly configured.</p>


<h2 id="local-development-support-for-email-workers"><a href="/changelog/post/2025-04-08-local-development/">Local development support for Email Workers</a></h2>
<p><em>2025-04-08</em></p>
<p>Email Workers enables developers to programmatically take action on anything that hits their email inbox. If you're building with Email Workers, you can now test the behavior of an Email Worker script, receiving, replying and sending emails in your local environment using <code>wrangler dev</code>.</p>
<p>Below is an example that shows you how you can receive messages using the <code>email()</code> handler and parse them using <a href="https://www.npmjs.com/package/postal-mime">postal-mime</a>:</p>
<pre><code class="language-ts">import * as PostalMime from &quot;postal-mime&quot;;&#10;&#10;export default {&#10;	async email(message, env, ctx) {&#10;		const parser = new PostalMime.default();&#10;		const rawEmail = new Response(message.raw);&#10;		const email = await parser.parse(await rawEmail.arrayBuffer());&#10;		console.log(email);&#10;	},&#10;};&#10;</code></pre>
<p>Now when you run <code>npx wrangler dev</code>, wrangler will expose a local <code>/cdn-cgi/local/email</code> endpoint that you can <code>POST</code> email messages to and trigger your Worker's <code>email()</code> handler:</p>
<pre><code class="language-bash">curl -X POST &#x27;http://localhost:8787/cdn-cgi/local/email&#x27; \&#10;  &#45;-url-query &#x27;from=sender@example.com&#x27; \&#10;  &#45;-url-query &#x27;to=recipient@example.com&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data-raw &#x27;Received: from smtp.example.com (127.0.0.1)&#10;        by cloudflare-email.com (unknown) id 4fwwffRXOpyR&#10;        for &lt;recipient@example.com&gt;; Tue, 27 Aug 2024 15:50:20 +0000&#10;From: &quot;John&quot; &lt;sender@example.com&gt;&#10;Reply-To: sender@example.com&#10;To: recipient@example.com&#10;Subject: Testing Email Workers Local Dev&#10;Content-Type: text/html; charset=&quot;windows-1252&quot;&#10;X-Mailer: Curl&#10;Date: Tue, 27 Aug 2024 08:49:44 -0700&#10;Message-ID: &lt;6114391943504294873000@ZSH-GHOSTTY&gt;&#10;&#10;Hi there&#x27;&#10;</code></pre>
<p>This is what you get in the console:</p>
<pre><code class="language-json">{&#10;	&quot;headers&quot;: [&#10;		{&#10;			&quot;key&quot;: &quot;received&quot;,&#10;			&quot;value&quot;: &quot;from smtp.example.com (127.0.0.1) by cloudflare-email.com (unknown) id 4fwwffRXOpyR for &lt;recipient@example.com&gt;; Tue, 27 Aug 2024 15:50:20 +0000&quot;&#10;		},&#10;		{ &quot;key&quot;: &quot;from&quot;, &quot;value&quot;: &quot;\&quot;John\&quot; &lt;sender@example.com&gt;&quot; },&#10;		{ &quot;key&quot;: &quot;reply-to&quot;, &quot;value&quot;: &quot;sender@example.com&quot; },&#10;		{ &quot;key&quot;: &quot;to&quot;, &quot;value&quot;: &quot;recipient@example.com&quot; },&#10;		{ &quot;key&quot;: &quot;subject&quot;, &quot;value&quot;: &quot;Testing Email Workers Local Dev&quot; },&#10;		{ &quot;key&quot;: &quot;content-type&quot;, &quot;value&quot;: &quot;text/html; charset=\&quot;windows-1252\&quot;&quot; },&#10;		{ &quot;key&quot;: &quot;x-mailer&quot;, &quot;value&quot;: &quot;Curl&quot; },&#10;		{ &quot;key&quot;: &quot;date&quot;, &quot;value&quot;: &quot;Tue, 27 Aug 2024 08:49:44 -0700&quot; },&#10;		{&#10;			&quot;key&quot;: &quot;message-id&quot;,&#10;			&quot;value&quot;: &quot;&lt;6114391943504294873000@ZSH-GHOSTTY&gt;&quot;&#10;		}&#10;	],&#10;	&quot;from&quot;: { &quot;address&quot;: &quot;sender@example.com&quot;, &quot;name&quot;: &quot;John&quot; },&#10;	&quot;to&quot;: [{ &quot;address&quot;: &quot;recipient@example.com&quot;, &quot;name&quot;: &quot;&quot; }],&#10;	&quot;replyTo&quot;: [{ &quot;address&quot;: &quot;sender@example.com&quot;, &quot;name&quot;: &quot;&quot; }],&#10;	&quot;subject&quot;: &quot;Testing Email Workers Local Dev&quot;,&#10;	&quot;messageId&quot;: &quot;&lt;6114391943504294873000@ZSH-GHOSTTY&gt;&quot;,&#10;	&quot;date&quot;: &quot;2024-08-27T15:49:44.000Z&quot;,&#10;	&quot;html&quot;: &quot;Hi there\n&quot;,&#10;	&quot;attachments&quot;: []&#10;}&#10;</code></pre>
<p>Local development is a critical part of the development flow, and also works for sending, replying and forwarding emails. See <a href="/email-service/local-development/routing/">our documentation</a> for more information.</p>


<h2 id="threaded-replies-now-possible-in-email-workers"><a href="/changelog/post/2025-03-12-reply-limits/">Threaded replies now possible in Email Workers</a></h2>
<p><em>2025-03-12</em></p>
<p>We’re removing some of the restrictions in Email Routing so that AI Agents and task automation can better handle email workflows, including how Workers can <a href="/email-service/api/route-emails/email-handler/#reply-to-emails">reply</a> to incoming emails.</p>
<p>It's now possible to keep a threaded email conversation with an <a href="/email-service/api/route-emails/email-handler/">Email Worker</a> script as long as:</p>
<ul>
<li>The incoming email has to have valid <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/">DMARC</a>.</li>
<li>The email can only be replied to once in the same <code>EmailMessage</code> event.</li>
<li>The recipient in the reply must match the incoming sender.</li>
<li>The outgoing sender domain must match the same domain that received the email.</li>
<li>Every time an email passes through Email Routing or another MTA, an entry is added to the <code>References</code> list. We stop accepting replies to emails with more than 100 <code>References</code> entries to prevent abuse or accidental loops.</li>
</ul>
<p>Here's an example of a Worker responding to Emails using a Workers AI model:</p>
<pre><code class="language-ts">import PostalMime from &quot;postal-mime&quot;;&#10;import { createMimeMessage } from &quot;mimetext&quot;;&#10;import { EmailMessage } from &quot;cloudflare:email&quot;;&#10;&#10;export default {&#10;	async email(message, env, ctx) {&#10;		const email = await PostalMime.parse(message.raw);&#10;		const res = await env.AI.run(&quot;@cf/meta/llama-2-7b-chat-fp16&quot;, {&#10;			messages: [&#10;				{&#10;					role: &quot;user&quot;,&#10;					content: email.text ?? &quot;&quot;,&#10;				},&#10;			],&#10;		});&#10;&#10;		// message-id is generated by mimetext&#10;		const response = createMimeMessage();&#10;		response.setHeader(&quot;In-Reply-To&quot;, message.headers.get(&quot;Message-ID&quot;)!);&#10;		response.setSender(&quot;agent@example.com&quot;);&#10;		response.setRecipient(message.from);&#10;		response.setSubject(&quot;Llama response&quot;);&#10;		response.addMessage({&#10;			contentType: &quot;text/plain&quot;,&#10;			data:&#10;				res instanceof ReadableStream&#10;					? await new Response(res).text()&#10;					: res.response!,&#10;		});&#10;&#10;		const replyMessage = new EmailMessage(&#10;			&quot;&lt;email&gt;&quot;,&#10;			message.from,&#10;			response.asRaw(),&#10;		);&#10;		await message.reply(replyMessage);&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>See <a href="/email-service/api/route-emails/email-handler/#reply-to-emails">Reply to emails from Workers</a> for more information.</p>



