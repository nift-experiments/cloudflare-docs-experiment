---
cp9:
  canonical: https://developers.cloudflare.com/workers/tutorials/send-emails-with-resend/
  description: This tutorial explains how to send emails from Cloudflare Workers using Resend.
  full_title: Send Emails With Resend · Cloudflare Workers docs
  head_html: <title>Send Emails With Resend · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial explains how to send emails from Cloudflare Workers using Resend."><link rel="canonical" href="https://developers.cloudflare.com/workers/tutorials/send-emails-with-resend/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/tutorials/send-emails-with-resend/index.md"><meta property="og:title" content="Send Emails With Resend · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial explains how to send emails from Cloudflare Workers using Resend."><meta property="og:url" content="https://developers.cloudflare.com/workers/tutorials/send-emails-with-resend/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="JavaScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/tutorials/send-emails-with-resend/#page","headline":"Send Emails With Resend \u00b7 Cloudflare Workers docs","description":"This tutorial explains how to send emails from Cloudflare Workers using Resend.","url":"https://developers.cloudflare.com/workers/tutorials/send-emails-with-resend/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript"]}</script>
  markdown: true
  noindex: false
  route: /workers/tutorials/send-emails-with-resend/
  schema: 1
---
<p>In this tutorial, you will learn how to send transactional emails from Workers using <a href="https://resend.com/">Resend</a>. At the end of this tutorial, you’ll be able to:</p>
<ul>
<li>Create a Worker to send emails.</li>
<li>Sign up and add a Cloudflare domain to Resend.</li>
<li>Send emails from your Worker using Resend.</li>
<li>Store API keys securely with secrets.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<p>To continue with this tutorial, you’ll need:</p>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>, if you don’t already have one.</li>
<li>A <a href="/registrar/get-started/register-domain/">registered</a> domain.</li>
<li>Installed <a href="https://docs.npmjs.com/getting-started">npm</a>.</li>
<li>A <a href="https://resend.com/signup">Resend account</a>.</li>
</ul>
<h2 id="create-a-worker-project">Create a Worker project</h2>
<p>Start by using <a href="/pages/get-started/c3/">C3</a> to create a Worker project in the command line, then, answer the prompts:</p>
<pre tabindex="0"><code class="language-sh">npm create cloudflare@latest&#10;</code></pre>
<p>Alternatively, you can use CLI arguments to speed things up:</p>
<pre tabindex="0"><code class="language-sh">npm create cloudflare@latest email-with-resend -- --type=hello-world --ts=false --git=true --deploy=false&#10;</code></pre>
<p>This creates a simple hello-world Worker having the following content:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		return new Response(&quot;Hello World!&quot;);&#10;	},&#10;};&#10;</code></pre>
<h2 id="add-your-domain-to-resend">Add your domain to Resend</h2>
<p>If you don’t already have a Resend account, you can sign up for a <a href="https://resend.com/signup">free account here</a>. After signing up, go to <code>Domains</code> using the side menu, and click the button to add a new domain. On the modal, enter the domain you want to add and then select a region.</p>
<p>Next, you’re presented with a list of DNS records to add to your Cloudflare domain. On your Cloudflare dashboard, select the domain you entered earlier and navigate to <code>DNS</code> &gt; <code>Records</code>. Copy/paste the DNS records (DKIM, SPF, and DMARC records) from Resend to your Cloudflare domain.</p>
<p><img src="/assets/upstream/images/workers/tutorials/resend/add_dns_records.png" alt="Image of adding DNS records to a Cloudflare domain" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16051.md")
</aside>
<p>When that’s done, head back to Resend and click on the <code>Verify DNS Records</code> button. If all records are properly configured, your domain status should be updated to <code>Verified</code>.</p>
<p><img src="/assets/upstream/images/workers/tutorials/resend/verified_domain.png" alt="Image of domain verification on the Resend dashboard" /></p>
<p>Lastly, navigate to <code>API Keys</code> with the side menu, to create an API key. Give your key a descriptive name and the appropriate permissions. Click the button to add your key and then copy your API key to a safe location.</p>
<h2 id="send-emails-from-your-worker">Send emails from your Worker</h2>
<p>The final step is putting it all together in a Worker. Open up a terminal in the directory of the Worker you created earlier. Then, install the Resend SDK:</p>
<pre tabindex="0"><code class="language-sh">npm i resend&#10;</code></pre>
<p>In your Worker, import and use the Resend library like so:</p>
<pre tabindex="0"><code class="language-jsx">import { Resend } from &quot;resend&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		const resend = new Resend(&quot;your_resend_api_key&quot;);&#10;&#10;		const { data, error } = await resend.emails.send({&#10;			from: &quot;hello@example.com&quot;,&#10;			to: &quot;someone@example.com&quot;,&#10;			subject: &quot;Hello World&quot;,&#10;			html: &quot;&lt;p&gt;Hello from Workers&lt;/p&gt;&quot;,&#10;		});&#10;&#10;		return Response.json({ data, error });&#10;	},&#10;};&#10;</code></pre>
<p>To test your code locally, run the following command and navigate to <a href="http://localhost:8787/">http://localhost:8787/</a> in a browser:</p>
<pre tabindex="0"><code class="language-sh">npm start&#10;</code></pre>
<p>Deploy your Worker with <code>npm run deploy</code>.</p>
<h2 id="move-api-keys-to-secrets">Move API keys to Secrets</h2>
<p>Sensitive information such as API keys and token should always be stored in secrets. All secrets are encrypted to add an extra layer of protection. That said, it’s a good idea to move your API key to a secret and access it from the environment of your Worker.</p>
<p>To add secrets for local development, create a <code>.dev.vars</code> file which works exactly like a <code>.env</code> file:</p>
<pre tabindex="0"><code class="language-txt">RESEND_API_KEY=your_resend_api_key&#10;</code></pre>
<p>Also ensure the secret is added to your deployed worker by running:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler secret put RESEND_API_KEY&#10;</code></pre>
<p>The added secret can be accessed on via the <code>env</code> parameter passed to your Worker’s fetch event handler:</p>
<pre tabindex="0"><code class="language-jsx">import { Resend } from &quot;resend&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		const resend = new Resend(env.RESEND_API_KEY);&#10;&#10;		const { data, error } = await resend.emails.send({&#10;			from: &quot;hello@example.com&quot;,&#10;			to: &quot;someone@example.com&quot;,&#10;			subject: &quot;Hello World&quot;,&#10;			html: &quot;&lt;p&gt;Hello from Workers&lt;/p&gt;&quot;,&#10;		});&#10;&#10;		return Response.json({ data, error });&#10;	},&#10;};&#10;</code></pre>
<p>And finally, deploy this update with <code>npm run deploy</code>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/configuration/secrets/">Storing API keys and tokens with Secrets</a>.</li>
<li><a href="/registrar/get-started/transfer-domain-to-cloudflare/">Transferring your domain to Cloudflare</a>.</li>
<li><a href="/email-service/api/send-emails/workers-api/">Send emails from Workers</a></li>
</ul>
