---
cp9:
  canonical: https://developers.cloudflare.com/workers/tutorials/send-emails-with-postmark/
  description: This tutorial explains how to send transactional emails from Workers using Postmark.
  full_title: Send Emails With Postmark · Cloudflare Workers docs
  head_html: <title>Send Emails With Postmark · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial explains how to send transactional emails from Workers using Postmark."><link rel="canonical" href="https://developers.cloudflare.com/workers/tutorials/send-emails-with-postmark/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/tutorials/send-emails-with-postmark/index.md"><meta property="og:title" content="Send Emails With Postmark · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial explains how to send transactional emails from Workers using Postmark."><meta property="og:url" content="https://developers.cloudflare.com/workers/tutorials/send-emails-with-postmark/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="JavaScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/tutorials/send-emails-with-postmark/#page","headline":"Send Emails With Postmark \u00b7 Cloudflare Workers docs","description":"This tutorial explains how to send transactional emails from Workers using Postmark.","url":"https://developers.cloudflare.com/workers/tutorials/send-emails-with-postmark/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript"]}</script>
  markdown: true
  noindex: false
  route: /workers/tutorials/send-emails-with-postmark/
  schema: 1
---
<p>In this tutorial, you will learn how to send transactional emails from Workers using <a href="https://postmarkapp.com/">Postmark</a>. At the end of this tutorial, you’ll be able to:</p>
<ul>
<li>Create a Worker to send emails.</li>
<li>Sign up and add a Cloudflare domain to Postmark.</li>
<li>Send emails from your Worker using Postmark.</li>
<li>Store API keys securely with secrets.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<p>To continue with this tutorial, you’ll need:</p>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>, if you don’t already have one.</li>
<li>A <a href="/registrar/get-started/register-domain/">registered</a> domain.</li>
<li>Installed <a href="https://docs.npmjs.com/getting-started">npm</a>.</li>
<li>A <a href="https://account.postmarkapp.com/sign_up">Postmark account</a>.</li>
</ul>
<h2 id="create-a-worker-project">Create a Worker project</h2>
<p>Start by using <a href="/pages/get-started/c3/">C3</a> to create a Worker project in the command line, then, answer the prompts:</p>
<pre tabindex="0"><code class="language-sh">npm create cloudflare@latest&#10;</code></pre>
<p>Alternatively, you can use CLI arguments to speed things up:</p>
<pre tabindex="0"><code class="language-sh">npm create cloudflare@latest email-with-postmark -- --type=hello-world --ts=false --git=true --deploy=false&#10;</code></pre>
<p>This creates a simple hello-world Worker having the following content:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		return new Response(&quot;Hello World!&quot;);&#10;	},&#10;};&#10;</code></pre>
<h2 id="add-your-domain-to-postmark">Add your domain to Postmark</h2>
<p>If you don’t already have a Postmark account, you can sign up for a <a href="https://account.postmarkapp.com/sign_up">free account here</a>. After signing up, check your inbox for a link to confirm your sender signature. This verifies and enables you to send emails from your registered email address.</p>
<p>To enable email sending from other addresses on your domain, navigate to <code>Sender Signatures</code> on the Postmark dashboard, <code>Add Domain or Signature</code> &gt; <code>Add Domain</code>, then type in your domain and click on <code>Verify Domain</code>.</p>
<p>Next, you’re presented with a list of DNS records to add to your Cloudflare domain. On your Cloudflare dashboard, select the domain you entered earlier and navigate to <code>DNS</code> &gt; <code>Records</code>. Copy/paste the DNS records (DKIM, and Return-Path) from Postmark to your Cloudflare domain.</p>
<p><img src="/assets/upstream/images/workers/tutorials/postmarkapp/add_dns_records.png" alt="Image of adding DNS records to a Cloudflare domain" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16053.md")
</aside>
<p>When that’s done, head back to Postmark and click on the <code>Verify</code> buttons. If all records are properly configured, your domain status should be updated to <code>Verified</code>.</p>
<p><img src="/assets/upstream/images/workers/tutorials/postmarkapp/verified_domain.png" alt="Image of domain verification on the Postmark dashboard" /></p>
<p>To grab your API token, navigate to the <code>Servers</code> tab, then <code>My First Server</code> &gt; <code>API Tokens</code>, then copy your API key to a safe place.</p>
<h2 id="send-emails-from-your-worker">Send emails from your Worker</h2>
<p>The final step is putting it all together in a Worker. In your Worker, make a post request with <code>fetch</code> to Postmark’s email API and include your token and message body:</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16052.md")
</aside>
<pre tabindex="0"><code class="language-jsx">export default {&#10;	async fetch(request, env, ctx) {&#10;		return await fetch(&quot;https://api.postmarkapp.com/email&quot;, {&#10;			method: &quot;POST&quot;,&#10;			headers: {&#10;				&quot;Content-Type&quot;: &quot;application/json&quot;,&#10;				&quot;X-Postmark-Server-Token&quot;: &quot;your_postmark_api_token_here&quot;,&#10;			},&#10;			body: JSON.stringify({&#10;				From: &quot;hello@example.com&quot;,&#10;				To: &quot;someone@example.com&quot;,&#10;				Subject: &quot;Hello World&quot;,&#10;				HtmlBody: &quot;&lt;p&gt;Hello from Workers&lt;/p&gt;&quot;,&#10;			}),&#10;		});&#10;	},&#10;};&#10;</code></pre>
<p>To test your code locally, run the following command and navigate to <a href="http://localhost:8787/">http://localhost:8787/</a> in a browser:</p>
<pre tabindex="0"><code class="language-sh">npm start&#10;</code></pre>
<p>Deploy your Worker with <code>npm run deploy</code>.</p>
<h2 id="move-api-token-to-secrets">Move API token to Secrets</h2>
<p>Sensitive information such as API keys and token should always be stored in secrets. All secrets are encrypted to add an extra layer of protection. That said, it’s a good idea to move your API token to a secret and access it from the environment of your Worker.</p>
<p>To add secrets for local development, create a <code>.dev.vars</code> file which works exactly like a <code>.env</code> file:</p>
<pre tabindex="0"><code class="language-txt">POSTMARK_API_TOKEN=your_postmark_api_token_here&#10;</code></pre>
<p>Also ensure the secret is added to your deployed worker by running:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler secret put POSTMARK_API_TOKEN&#10;</code></pre>
<p>The added secret can be accessed on via the <code>env</code> parameter passed to your Worker’s fetch event handler:</p>
<pre tabindex="0"><code class="language-jsx">export default {&#10;	async fetch(request, env, ctx) {&#10;		return await fetch(&quot;https://api.postmarkapp.com/email&quot;, {&#10;			method: &quot;POST&quot;,&#10;			headers: {&#10;				&quot;Content-Type&quot;: &quot;application/json&quot;,&#10;				&quot;X-Postmark-Server-Token&quot;: env.POSTMARK_API_TOKEN,&#10;			},&#10;			body: JSON.stringify({&#10;				From: &quot;hello@example.com&quot;,&#10;				To: &quot;someone@example.com&quot;,&#10;				Subject: &quot;Hello World&quot;,&#10;				HtmlBody: &quot;&lt;p&gt;Hello from Workers&lt;/p&gt;&quot;,&#10;			}),&#10;		});&#10;	},&#10;};&#10;</code></pre>
<p>And finally, deploy this update with <code>npm run deploy</code>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/configuration/secrets/">Storing API keys and tokens with Secrets</a>.</li>
<li><a href="/registrar/get-started/transfer-domain-to-cloudflare/">Transferring your domain to Cloudflare</a>.</li>
<li><a href="/email-service/api/send-emails/workers-api/">Send emails from Workers</a></li>
</ul>
