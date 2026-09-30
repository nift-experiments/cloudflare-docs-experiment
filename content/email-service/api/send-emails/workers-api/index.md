---
cp9:
  canonical: https://developers.cloudflare.com/email-service/api/send-emails/workers-api/
  description: Send emails directly from Cloudflare Workers using the Email Service binding and send() method.
  full_title: Workers API · Cloudflare Email Service docs
  head_html: <title>Workers API · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="Send emails directly from Cloudflare Workers using the Email Service binding and send() method."><link rel="canonical" href="https://developers.cloudflare.com/email-service/api/send-emails/workers-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/api/send-emails/workers-api/index.md"><meta property="og:title" content="Workers API · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send emails directly from Cloudflare Workers using the Email Service binding and send() method."><meta property="og:url" content="https://developers.cloudflare.com/email-service/api/send-emails/workers-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Email Service,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/email-service/api/send-emails/workers-api/#page","headline":"Workers API \u00b7 Cloudflare Email Service docs","description":"Send emails directly from Cloudflare Workers using the Email Service binding and send() method.","url":"https://developers.cloudflare.com/email-service/api/send-emails/workers-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/api/send-emails/workers-api/
  schema: 1
---
<p>The Workers API provides native email sending capabilities directly from your Cloudflare Workers through bindings. If you are not using Workers, you can send emails using the <a href="/email-service/api/send-emails/rest-api/">REST API</a> instead.</p>
<h2 id="email-binding">Email binding</h2>
<p>Configure a <code>send_email</code> binding in your Wrangler configuration file to enable email sending:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8643.md")
</div>
<p>You can restrict which senders and recipients a binding may use. Refer to <a href="/email-service/configuration/send-bindings/">Configure send bindings</a> for the available restriction attributes and examples.</p>
<h2 id="send-method"><code>send()</code> method</h2>
<p>Send a single email using the <code>send()</code> method on your email binding.</p>
<h3 id="interface">Interface</h3>
<pre tabindex="0"><code class="language-ts">interface SendEmail {&#10;	send(message: EmailMessage | EmailMessageBuilder): Promise&lt;EmailSendResult&gt;;&#10;}&#10;&#10;interface EmailAddress {&#10;	email: string;&#10;	name?: string;&#10;}&#10;&#10;// Structured email builder (recommended)&#10;interface EmailMessageBuilder {&#10;	to: string | EmailAddress | (string | EmailAddress)[]; // Max 50 recipients&#10;	from: string | EmailAddress;&#10;	subject: string;&#10;	html?: string;&#10;	text?: string;&#10;	cc?: string | EmailAddress | (string | EmailAddress)[];&#10;	bcc?: string | EmailAddress | (string | EmailAddress)[];&#10;	replyTo?: string | EmailAddress;&#10;	attachments?: Attachment[];&#10;	// Custom headers. See /email-service/reference/headers/&#10;	headers?: { [key: string]: string };&#10;	// The combined number of addresses in `to`, `cc`, and `bcc` must not&#10;	// exceed 50. See /email-service/platform/limits/ for all limits.&#10;}&#10;&#10;interface Attachment {&#10;	content: string | ArrayBuffer | ArrayBufferView; // Base64 string or binary content&#10;	filename: string;&#10;	type: string; // MIME type&#10;	disposition: &quot;attachment&quot; | &quot;inline&quot;;&#10;	contentId?: string; // For inline attachments&#10;}&#10;&#10;interface EmailSendResult {&#10;	messageId: string; // Unique email ID&#10;}&#10;&#10;// Errors are thrown as standard Error objects with a `code` property&#10;// try { await env.EMAIL.send(...) } catch (e) { console.log(e.code, e.message) }&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="local-development-with-binary-attachments">Local development with binary attachments</h3>
@markup("md", "content/.markup/bodies/8642.md")
</aside>
<h3 id="basic-usage">Basic usage</h3>
<pre tabindex="0"><code class="language-ts">const response = await env.EMAIL.send({&#10;	to: &quot;recipient@example.com&quot;,&#10;	from: &quot;welcome@yourdomain.com&quot;,&#10;	subject: &quot;Welcome to our service!&quot;,&#10;	html: &quot;&lt;h1&gt;Welcome!&lt;/h1&gt;&lt;p&gt;Thanks for signing up.&lt;/p&gt;&quot;,&#10;	text: &quot;Welcome! Thanks for signing up.&quot;,&#10;});&#10;</code></pre>
<p>For multiple recipients, CC/BCC, and named addresses, see <a href="/email-service/examples/email-sending/recipients/">Specify recipients</a>.</p>
<h3 id="attachments">Attachments</h3>
<p>Send files by including base64-encoded content in the <code>attachments</code> array. The total message size must not exceed 5 MiB (including attachments).</p>
<pre tabindex="0"><code class="language-ts">const response = await env.EMAIL.send({&#10;	to: &quot;customer@example.com&quot;,&#10;	from: &quot;invoices@yourdomain.com&quot;,&#10;	subject: &quot;Your Invoice&quot;,&#10;	html: &quot;&lt;h1&gt;Invoice attached&lt;/h1&gt;&lt;p&gt;Please find your invoice attached.&lt;/p&gt;&quot;,&#10;	attachments: [&#10;		{&#10;			content: &quot;JVBERi0xLjQKJeLjz9MKMSAwIG9iag...&quot;, // Base64 PDF content&#10;			filename: &quot;invoice-12345.pdf&quot;,&#10;			type: &quot;application/pdf&quot;,&#10;			disposition: &quot;attachment&quot;,&#10;		},&#10;	],&#10;});&#10;</code></pre>
<p>For inline images and file uploads, see <a href="/email-service/examples/email-sending/email-attachments/">Email attachments</a>.</p>
<h2 id="error-handling">Error handling</h2>
<p>Handle email sending errors gracefully:</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;	async fetch(request: Request, env: Env): Promise&lt;Response&gt; {&#10;		try {&#10;			const response = await env.EMAIL.send({&#10;				to: &quot;user@example.com&quot;,&#10;				from: &quot;noreply@yourdomain.com&quot;,&#10;				subject: &quot;Test Email&quot;,&#10;				text: &quot;This is a test email.&quot;,&#10;			});&#10;&#10;			return new Response(&#10;				JSON.stringify({&#10;					success: true,&#10;					emailId: response.messageId,&#10;				}),&#10;			);&#10;		} catch (error) {&#10;			// Error has .code and .message properties&#10;			console.error(&quot;Email sending failed:&quot;, error.code, error.message);&#10;&#10;			// Handle specific error types&#10;			switch (error.code) {&#10;				case &quot;E_SENDER_NOT_VERIFIED&quot;:&#10;					return new Response(&#10;						JSON.stringify({&#10;							success: false,&#10;							error: &quot;Please verify your sender domain first&quot;,&#10;						}),&#10;						{ status: 400 },&#10;					);&#10;&#10;				case &quot;E_RATE_LIMIT_EXCEEDED&quot;:&#10;					return new Response(&#10;						JSON.stringify({&#10;							success: false,&#10;							error: &quot;Rate limit exceeded. Please try again later&quot;,&#10;						}),&#10;						{ status: 429 },&#10;					);&#10;&#10;				default:&#10;					return new Response(&#10;						JSON.stringify({&#10;							success: false,&#10;							error: error.message,&#10;						}),&#10;						{ status: 500 },&#10;					);&#10;			}&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h2 id="error-codes">Error codes</h2>
<p>The following error codes may be returned when sending emails:</p>
<table>
<thead>
<tr>
<th>Error Code</th>
<th>Description</th>
<th>Common Causes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>E_VALIDATION_ERROR</code></td>
<td>Validation error in the payload</td>
<td>Invalid email format, missing required fields, malformed data</td>
</tr>
<tr>
<td><code>E_FIELD_MISSING</code></td>
<td>Required field is missing</td>
<td>Missing <code>to</code>, <code>from</code>, or <code>subject</code> fields</td>
</tr>
<tr>
<td><code>E_TOO_MANY_RECIPIENTS</code></td>
<td>Too many recipients in to/cc/bcc arrays</td>
<td>Combined recipients exceed 50 limit</td>
</tr>
<tr>
<td><code>E_TOO_MANY_ATTACHMENTS</code></td>
<td>Too many attachments in <code>attachments</code> array</td>
<td><code>attachments</code> array exceeds 32 entries</td>
</tr>
<tr>
<td><code>E_SENDER_NOT_VERIFIED</code></td>
<td>Sender domain not verified</td>
<td>Attempting to send from unverified domain</td>
</tr>
<tr>
<td><code>E_RECIPIENT_NOT_ALLOWED</code></td>
<td>Recipient not in allowed list</td>
<td>Recipient address not in <code>allowed_destination_addresses</code></td>
</tr>
<tr>
<td><code>E_RECIPIENT_SUPPRESSED</code></td>
<td>Suppressed recipient while dropping is off</td>
<td>At least one recipient is suppressed and <strong>Drop suppressed recipients</strong> is off</td>
</tr>
<tr>
<td><code>E_SENDER_DOMAIN_NOT_AVAILABLE</code></td>
<td>Domain not available for sending</td>
<td>Domain not onboarded to Email Service</td>
</tr>
<tr>
<td><code>E_CONTENT_TOO_LARGE</code></td>
<td>Email content exceeds size limit</td>
<td>Total message size exceeds the maximum</td>
</tr>
<tr>
<td><code>E_DELIVERY_FAILED</code></td>
<td>Could not deliver the email</td>
<td>SMTP delivery failure, recipient server rejection</td>
</tr>
<tr>
<td><code>E_RATE_LIMIT_EXCEEDED</code></td>
<td>Rate limit exceeded</td>
<td>Sending rate limit reached</td>
</tr>
<tr>
<td><code>E_DAILY_LIMIT_EXCEEDED</code></td>
<td>Daily limit exceeded</td>
<td>Daily sending quota reached</td>
</tr>
<tr>
<td><code>E_INTERNAL_SERVER_ERROR</code></td>
<td>Internal service error</td>
<td>Email Service temporarily unavailable</td>
</tr>
<tr>
<td><code>E_HEADER_NOT_ALLOWED</code></td>
<td>Header not allowed</td>
<td>Header is platform-controlled or not on the <a href="/email-service/reference/headers/">allowlist</a></td>
</tr>
<tr>
<td><code>E_HEADER_USE_API_FIELD</code></td>
<td>Must use API field</td>
<td>Header like <code>From</code> must be set via the dedicated API field</td>
</tr>
<tr>
<td><code>E_HEADER_VALUE_INVALID</code></td>
<td>Header value invalid</td>
<td>Malformed value, empty, or incorrect format</td>
</tr>
<tr>
<td><code>E_HEADER_VALUE_TOO_LONG</code></td>
<td>Header value too long</td>
<td>Value exceeds 2,048 byte limit</td>
</tr>
<tr>
<td><code>E_HEADER_NAME_INVALID</code></td>
<td>Header name invalid</td>
<td>Invalid characters or exceeds 100 byte limit</td>
</tr>
<tr>
<td><code>E_HEADERS_TOO_LARGE</code></td>
<td>Headers payload too large</td>
<td>Total custom headers exceed 16 KB limit</td>
</tr>
<tr>
<td><code>E_HEADERS_TOO_MANY</code></td>
<td>Too many headers</td>
<td>More than 20 allowlisted (non-X) custom headers</td>
</tr>
</tbody>
</table>
<p><strong>Drop suppressed recipients</strong> is off by default. When you <a href="/email-service/configuration/domains/#drop-suppressed-recipients">turn on the setting</a>, Email Service removes suppressed recipients and processes the remaining recipients.</p>
<h2 id="legacy-emailmessage-api">Legacy <code>EmailMessage</code> API</h2>
<p>The <code>EmailMessage</code> API remains supported for backward compatibility. Use it when you already have a raw <a href="https://datatracker.ietf.org/doc/html/rfc5322">RFC 5322</a> MIME message to send. For new code, prefer the structured <a href="#send-method"><code>send()</code> method</a> above.</p>
<pre tabindex="0"><code class="language-ts">import { EmailMessage } from &quot;cloudflare:email&quot;;&#10;import { createMimeMessage } from &quot;mimetext&quot;;&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env): Promise&lt;Response&gt; {&#10;		const msg = createMimeMessage();&#10;		msg.setSender({ name: &quot;Sender&quot;, addr: &quot;sender@yourdomain.com&quot; });&#10;		msg.setRecipient(&quot;recipient@example.com&quot;);&#10;		msg.setSubject(&quot;Legacy Email&quot;);&#10;		msg.addMessage({&#10;			contentType: &quot;text/html&quot;,&#10;			data: &quot;&lt;h1&gt;Hello from legacy API&lt;/h1&gt;&quot;,&#10;		});&#10;&#10;		const message = new EmailMessage(&#10;			&quot;sender@yourdomain.com&quot;,&#10;			&quot;recipient@example.com&quot;,&#10;			msg.asRaw(),&#10;		);&#10;&#10;		await env.EMAIL.send(message);&#10;		return new Response(&quot;Legacy email sent&quot;);&#10;	},&#10;};&#10;</code></pre>
<hr />
<h2 id="next-steps">Next steps</h2>
<ul>
<li>See the <a href="/email-service/api/send-emails/rest-api/">REST API</a> for sending emails without Workers</li>
<li>See <a href="/email-service/api/send-emails/smtp/">SMTP</a> for sending from any SMTP-capable application or mail client</li>
<li>See <a href="/email-service/examples/">practical examples</a> of email sending patterns</li>
<li>Learn about <a href="/email-service/api/route-emails/">email routing</a> for handling incoming emails</li>
<li>Explore <a href="/email-service/concepts/email-authentication/">email authentication</a> for better deliverability</li>
</ul>
