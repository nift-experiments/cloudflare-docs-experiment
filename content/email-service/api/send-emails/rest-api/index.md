---
cp9:
  canonical: https://developers.cloudflare.com/email-service/api/send-emails/rest-api/
  description: Send emails from any application using the Email Service REST API with standard HTTP requests.
  full_title: REST API · Cloudflare Email Service docs
  head_html: <title>REST API · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="Send emails from any application using the Email Service REST API with standard HTTP requests."><link rel="canonical" href="https://developers.cloudflare.com/email-service/api/send-emails/rest-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/api/send-emails/rest-api/index.md"><meta property="og:title" content="REST API · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send emails from any application using the Email Service REST API with standard HTTP requests."><meta property="og:url" content="https://developers.cloudflare.com/email-service/api/send-emails/rest-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Email Service"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/email-service/api/send-emails/rest-api/#page","headline":"REST API \u00b7 Cloudflare Email Service docs","description":"Send emails from any application using the Email Service REST API with standard HTTP requests.","url":"https://developers.cloudflare.com/email-service/api/send-emails/rest-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/api/send-emails/rest-api/
  schema: 1
---
<p>The REST API allows you to send emails from any application using a standard HTTP request to <code>POST /accounts/{account_id}/email/sending/send</code>. Use it from any backend, serverless function, or CI/CD pipeline — no Cloudflare Workers binding is required.</p>
<p>For the full OpenAPI specification, refer to the <a href="/api/resources/email_sending/methods/send/">Email Sending API reference</a>.</p>
<p>Cloudflare also provides official SDKs for the REST API: <a href="/api/node/">Node</a>, <a href="/api/python/">Python</a>, and <a href="/api/go/">Go</a>.</p>
<h2 id="authentication">Authentication</h2>
<p>Authenticate with a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> that has permission to send emails. Include it in the <code>Authorization</code> header:</p>
<pre tabindex="0"><code class="language-txt">Authorization: Bearer &lt;API_TOKEN&gt;&#10;</code></pre>
<h2 id="send-an-email">Send an email</h2>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/email/sending/send&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;to&quot;: &quot;recipient@example.com&quot;,&#10;    &quot;from&quot;: &quot;welcome@yourdomain.com&quot;,&#10;    &quot;subject&quot;: &quot;Welcome to our service!&quot;,&#10;    &quot;html&quot;: &quot;&lt;h1&gt;Welcome!&lt;/h1&gt;&lt;p&gt;Thanks for signing up.&lt;/p&gt;&quot;,&#10;    &quot;text&quot;: &quot;Welcome! Thanks for signing up.&quot;&#10;  }&#x27;&#10;</code></pre>
<p>For multiple recipients, CC/BCC, and named addresses, see <a href="/email-service/examples/email-sending/recipients/">Specify recipients</a>.</p>
<h2 id="attachments">Attachments</h2>
<p>Send files by including base64-encoded content in the <code>attachments</code> array. The total message size must not exceed <strong>5 MiB</strong> (including attachments).</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/email/sending/send&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;to&quot;: &quot;customer@example.com&quot;,&#10;    &quot;from&quot;: &quot;invoices@yourdomain.com&quot;,&#10;    &quot;subject&quot;: &quot;Your Invoice&quot;,&#10;    &quot;html&quot;: &quot;&lt;h1&gt;Invoice attached&lt;/h1&gt;&lt;p&gt;Please find your invoice attached.&lt;/p&gt;&quot;,&#10;    &quot;attachments&quot;: [&#10;      {&#10;        &quot;content&quot;: &quot;JVBERi0xLjQKJeLjz9MK...&quot;,&#10;        &quot;filename&quot;: &quot;invoice-12345.pdf&quot;,&#10;        &quot;type&quot;: &quot;application/pdf&quot;,&#10;        &quot;disposition&quot;: &quot;attachment&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>For inline images and file uploads, see <a href="/email-service/examples/email-sending/email-attachments/">Email attachments</a>.</p>
<h2 id="custom-headers">Custom headers</h2>
<p>Set custom headers for threading, list management, or tracking. Refer to the <a href="/email-service/reference/headers/">email headers reference</a> for the full list of allowed headers.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/email/sending/send&quot; \&#10;  &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;to&quot;: &quot;user@example.com&quot;,&#10;    &quot;from&quot;: &quot;notifications@yourdomain.com&quot;,&#10;    &quot;subject&quot;: &quot;Your weekly digest&quot;,&#10;    &quot;html&quot;: &quot;&lt;h1&gt;Weekly Digest&lt;/h1&gt;&quot;,&#10;    &quot;headers&quot;: {&#10;      &quot;List-Unsubscribe&quot;: &quot;&lt;https://yourdomain.com/unsubscribe?id=abc123&gt;&quot;,&#10;      &quot;List-Unsubscribe-Post&quot;: &quot;List-Unsubscribe=One-Click&quot;,&#10;      &quot;X-Campaign-ID&quot;: &quot;weekly-digest-2026-03&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h2 id="response">Response</h2>
<p>A successful response returns the delivery status for each recipient:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result&quot;: {&#10;		&quot;delivered&quot;: [&quot;recipient@example.com&quot;],&#10;		&quot;permanent_bounces&quot;: [],&#10;		&quot;queued&quot;: []&#10;	}&#10;}&#10;</code></pre>
<ul>
<li><code>delivered</code> - Email addresses to which the message was delivered immediately</li>
<li><code>permanent_bounces</code> - Email addresses that permanently bounced</li>
<li><code>queued</code> - Email addresses for which delivery was queued for later</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workers-binding-vs-rest-api-responses">Workers binding vs REST API responses</h3>
@markup("md", "content/.markup/bodies/8645.md")
</aside>
<h2 id="error-handling">Error handling</h2>
<p>The REST API returns standard Cloudflare API error responses. A failed request returns an <code>errors</code> array with numeric error codes and machine-readable messages:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: false,&#10;	&quot;errors&quot;: [&#10;		{&#10;			&quot;code&quot;: 10001,&#10;			&quot;message&quot;: &quot;email.sending.error.invalid_request_schema&quot;&#10;		}&#10;	],&#10;	&quot;messages&quot;: [],&#10;	&quot;result&quot;: null&#10;}&#10;</code></pre>
<p>REST API error codes:</p>
<table>
<thead>
<tr>
<th>HTTP Status</th>
<th>Code</th>
<th>Message</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>400</td>
<td>10001</td>
<td><code>email.sending.error.invalid_request_schema</code></td>
<td>Invalid request format</td>
</tr>
<tr>
<td>400</td>
<td>10200</td>
<td><code>email.sending.error.email.too_big</code></td>
<td>Email exceeds size limit</td>
</tr>
<tr>
<td>400</td>
<td>10201</td>
<td><code>email.sending.error.email.no_content_length</code></td>
<td>Missing content length</td>
</tr>
<tr>
<td>400</td>
<td>10202</td>
<td><code>email.sending.error.email.invalid</code></td>
<td>Invalid email content</td>
</tr>
<tr>
<td>401</td>
<td>10101</td>
<td><code>email.sending.error.authentication.unauthorized</code></td>
<td>Missing or invalid API token</td>
</tr>
<tr>
<td>401</td>
<td>10103</td>
<td><code>email.sending.error.authentication.bad_token_type</code></td>
<td>Wrong token type for this endpoint</td>
</tr>
<tr>
<td>403</td>
<td>10102</td>
<td><code>email.sending.error.authentication.forbidden</code></td>
<td>Token lacks permission to send</td>
</tr>
<tr>
<td>403</td>
<td>10105</td>
<td><code>email.sending.error.authentication.not_entitled</code></td>
<td>Account not entitled to use Email Sending</td>
</tr>
<tr>
<td>403</td>
<td>10203</td>
<td><code>email.sending.error.email.sending_disabled</code></td>
<td>Sending disabled for this zone or account</td>
</tr>
<tr>
<td>404</td>
<td>10000</td>
<td><code>email.sending.error.not_found</code></td>
<td>Resource not found</td>
</tr>
<tr>
<td>429</td>
<td>10004</td>
<td><code>email.sending.error.throttled</code></td>
<td>Rate limit exceeded</td>
</tr>
<tr>
<td>500</td>
<td>10002</td>
<td><code>email.sending.error.internal_server</code></td>
<td>Internal server error</td>
</tr>
<tr>
<td>500</td>
<td>10003</td>
<td><code>email.sending.error.not_implemented</code></td>
<td>Operation not implemented</td>
</tr>
<tr>
<td>503</td>
<td>10100</td>
<td><code>email.sending.error.authentication.upstream</code></td>
<td>Authentication service temporarily unavailable</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workers-binding-vs-rest-api-errors">Workers binding vs REST API errors</h3>
@markup("md", "content/.markup/bodies/8644.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Refer to the <a href="/api/resources/email_sending/methods/send/">Email Sending API reference</a> for the full request and response schemas.</li>
<li>See the <a href="/email-service/api/send-emails/workers-api/">Workers API</a> for sending emails directly from Cloudflare Workers using bindings.</li>
<li>See <a href="/email-service/api/send-emails/smtp/">SMTP</a> for sending from any SMTP-capable application or mail client.</li>
<li>Review <a href="/email-service/reference/headers/">email headers</a> for threading, list management, and custom tracking headers.</li>
</ul>
