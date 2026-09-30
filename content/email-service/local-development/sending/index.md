---
cp9:
  canonical: https://developers.cloudflare.com/email-service/local-development/sending/
  description: Test Email Service sending Workers locally using wrangler dev with simulated email delivery.
  full_title: Email sending · Cloudflare Email Service docs
  head_html: <title>Email sending · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="Test Email Service sending Workers locally using wrangler dev with simulated email delivery."><link rel="canonical" href="https://developers.cloudflare.com/email-service/local-development/sending/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/local-development/sending/index.md"><meta property="og:title" content="Email sending · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Test Email Service sending Workers locally using wrangler dev with simulated email delivery."><meta property="og:url" content="https://developers.cloudflare.com/email-service/local-development/sending/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email Service"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/email-service/local-development/sending/#page","headline":"Email sending \u00b7 Cloudflare Email Service docs","description":"Test Email Service sending Workers locally using wrangler dev with simulated email delivery.","url":"https://developers.cloudflare.com/email-service/local-development/sending/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/local-development/sending/
  schema: 1
---
<p class="article-summary">Test email sending Workers locally using wrangler dev with simulated email delivery</p>
<p>Test email sending functionality locally using <code>wrangler dev</code> to simulate email delivery and verify your sending logic before deploying.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8591.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8592.md")
</div></details>
<h2 id="configuration">Configuration</h2>
<p>Configure your Wrangler file with the email binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8593.md")
</div>
<h2 id="remote-bindings-recommended">Remote bindings (recommended)</h2>
<p>Using <a href="/workers/local-development/#remote-bindings">remote bindings</a> is the recommended way to develop with Email Service locally. By default, <code>wrangler dev</code> simulates the email binding locally -- emails are logged to the console but not actually sent. With remote bindings, your Worker runs locally but sends real emails through Email Service.</p>
<p>Set <code>remote: true</code> on the email binding in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8594.md")
</div>
<p>Then run <code>wrangler dev</code> as usual. Calls to <code>env.EMAIL.send()</code> will send actual emails through Email Service while your Worker code runs locally.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8590.md")
</aside>
<h2 id="local-simulation">Local simulation</h2>
<p>When running <code>wrangler dev</code> without remote bindings, the email binding is simulated locally. Emails are not sent -- instead, the email content is logged to the console and saved to local files for inspection.</p>
<h2 id="basic-sending-worker">Basic sending worker</h2>
<pre tabindex="0"><code class="language-javascript">export default {&#10;	async fetch(request, env, ctx) {&#10;		if (request.method !== &quot;POST&quot;) {&#10;			return new Response(&quot;Method not allowed&quot;, { status: 405 });&#10;		}&#10;&#10;		try {&#10;			const emailData = await request.json();&#10;&#10;			console.log(&quot;Sending email:&quot;, {&#10;				to: emailData.to,&#10;				from: emailData.from,&#10;				subject: emailData.subject,&#10;			});&#10;&#10;			const response = await env.EMAIL.send(emailData);&#10;&#10;			return new Response(&#10;				JSON.stringify({&#10;					success: true,&#10;					id: response.messageId,&#10;				}),&#10;				{&#10;					headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;				},&#10;			);&#10;		} catch (error) {&#10;			return new Response(&#10;				JSON.stringify({&#10;					success: false,&#10;					error: error.message,&#10;				}),&#10;				{&#10;					status: 500,&#10;					headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;				},&#10;			);&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h2 id="testing-locally">Testing locally</h2>
<p>Start your development server:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler dev&#10;</code></pre>
<p>Send a test email:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST http://localhost:8787/ \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;to&quot;: &quot;recipient@example.com&quot;,&#10;    &quot;from&quot;: &quot;sender@yourdomain.com&quot;,&#10;    &quot;subject&quot;: &quot;Test Email&quot;,&#10;    &quot;html&quot;: &quot;&lt;h1&gt;Hello from Wrangler!&lt;/h1&gt;&quot;,&#10;    &quot;text&quot;: &quot;Hello from Wrangler!&quot;&#10;  }&#x27;&#10;</code></pre>
<p>Wrangler will show output like:</p>
<pre tabindex="0"><code class="language-txt">[wrangler:info] send_email binding called with MessageBuilder:&#10;From: sender@yourdomain.com&#10;To: recipient@example.com&#10;Subject: Test Email&#10;&#10;Text: /tmp/miniflare-.../files/email-text/&lt;message-id&gt;.txt&#10;</code></pre>
<p>The email content (text and HTML) is saved to local files that you can inspect to verify your email structure before deploying.</p>
<h2 id="known-limitations">Known limitations</h2>
<h3 id="binary-attachments">Binary attachments</h3>
<p>Local development simulates the <code>send_email</code> binding locally, but <code>ArrayBuffer</code> values in attachment <code>content</code> cannot be serialized by the local simulator. If you pass an <code>ArrayBuffer</code> (for example, for image or PDF attachments), you will see an error like:</p>
<pre tabindex="0"><code class="language-txt">Cannot serialize value: [object ArrayBuffer]&#10;</code></pre>
<p><strong>Workaround:</strong> Use string content for text-based attachments during local development. To test binary attachments (images, PDFs), deploy your Worker with <code>npx wrangler deploy</code> and test against the deployed version.</p>
<p>This limitation only affects local development — <code>ArrayBuffer</code> content works correctly on deployed Workers.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Deploy your sending worker: <a href="/email-service/get-started/send-emails/">Send emails get started</a></li>
<li>See advanced patterns: <a href="/email-service/examples/email-sending/">Email sending examples</a></li>
</ul>
