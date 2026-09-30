---
cp9:
  canonical: https://developers.cloudflare.com/workers/tutorials/github-sms-notifications-using-twilio/
  description: This tutorial shows you how to build an SMS notification system on Workers to receive updates on a GitHub repository. Your Worker will send you a text update using Twilio when there is new activity on your repository.
  full_title: GitHub SMS notifications using Twilio · Cloudflare Workers docs
  head_html: <title>GitHub SMS notifications using Twilio · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial shows you how to build an SMS notification system on Workers to receive updates on a GitHub repository. Your Worker will send you a text update using Twilio when there is new activity on your repository."><link rel="canonical" href="https://developers.cloudflare.com/workers/tutorials/github-sms-notifications-using-twilio/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/tutorials/github-sms-notifications-using-twilio/index.md"><meta property="og:title" content="GitHub SMS notifications using Twilio · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial shows you how to build an SMS notification system on Workers to receive updates on a GitHub repository. Your Worker will send you a text update using Twilio when there is new activity on your repository."><meta property="og:url" content="https://developers.cloudflare.com/workers/tutorials/github-sms-notifications-using-twilio/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="JavaScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/tutorials/github-sms-notifications-using-twilio/#page","headline":"GitHub SMS notifications using Twilio \u00b7 Cloudflare Workers docs","description":"This tutorial shows you how to build an SMS notification system on Workers to receive updates on a GitHub repository. Your Worker will send you a text update using Twilio when there is new activity on your repository.","url":"https://developers.cloudflare.com/workers/tutorials/github-sms-notifications-using-twilio/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript"]}</script>
  markdown: true
  noindex: false
  route: /workers/tutorials/github-sms-notifications-using-twilio/
  schema: 1
---
<p>In this tutorial, you will learn to build an SMS notification system on Workers to receive updates on a GitHub repository. Your Worker will send you a text update using Twilio when there is new activity on your repository.</p>
<p>You will learn how to:</p>
<ul>
<li>Build webhooks using Workers.</li>
<li>Integrate Workers with GitHub and Twilio.</li>
<li>Use Worker secrets with Wrangler.</li>
</ul>
<p><img src="/images/workers/tutorials/github-sms/video-of-receiving-a-text-after-pushing-to-a-repo.gif" alt="Animated gif of receiving a text message on your phone after pushing changes to a repository" /></p>
<hr />
<h2 id="before-you-start">Before you start</h2>
<p>All of the tutorials assume you have already completed the <a href="/workers/get-started/guide/">Get started guide</a>, which gets you set up with a Cloudflare Workers account, <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a>, and <a href="/workers/wrangler/install-and-update/">Wrangler</a>.</p>
<h2 id="create-a-worker-project">Create a Worker project</h2>
<p>Start by using <code>npm create cloudflare@latest</code> to create a Worker project in the command line:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- github-twilio-notifications</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- github-twilio-notifications" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare github-twilio-notifications</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare github-twilio-notifications" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest github-twilio-notifications</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest github-twilio-notifications" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>JavaScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Make note of the URL that your application was deployed to. You will be using it when you configure your GitHub webhook.</p>
<pre tabindex="0"><code class="language-sh">cd github-twilio-notifications&#10;</code></pre>
<p>Inside of your new <code>github-sms-notifications</code> directory, <code>src/index.js</code> represents the entry point to your Cloudflare Workers application. You will configure this file for most of the tutorial.</p>
<p>You will also need a GitHub account and a repository for this tutorial. If you do not have either setup, <a href="https://github.com/join">create a new GitHub account</a> and <a href="https://docs.github.com/en/get-started/quickstart/create-a-repo">create a new repository</a> to continue with this tutorial.</p>
<p>First, create a webhook for your repository to post updates to your Worker. Inside of your Worker, you will then parse the updates. Finally, you will send a <code>POST</code> request to Twilio to send a text message to you.</p>
<p>You can reference the finished code at this <a href="https://github.com/rickyrobinett/workers-sdk/tree/main/templates/examples/github-sms-notifications-using-twilio">GitHub repository</a>.</p>
<hr />
<h2 id="configure-github">Configure GitHub</h2>
<p>To start, configure a GitHub webhook to post to your Worker when there is an update to the repository:</p>
<ol>
<li>
<p>Go to your GitHub repository's <strong>Settings</strong> &gt; <strong>Webhooks</strong> &gt; <strong>Add webhook</strong>.</p>
</li>
<li>
<p>Set the Payload URL to the <code>/webhook</code> path on the Worker URL that you made note of when your application was first deployed.</p>
</li>
<li>
<p>In the <strong>Content type</strong> dropdown, select <em>application/json</em>.</p>
</li>
<li>
<p>In the <strong>Secret</strong> field, input a secret key of your choice.</p>
</li>
<li>
<p>In <strong>Which events would you like to trigger this webhook?</strong>, select <strong>Let me select individual events</strong>. Select the events you want to get notifications for (such as <strong>Pull requests</strong>, <strong>Pushes</strong>, and <strong>Branch or tag creation</strong>).</p>
</li>
<li>
<p>Select <strong>Add webhook</strong> to finish configuration.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/workers/tutorials/github-sms/github-config-screenshot.png" alt="Following instructions to set up your webhook in the GitHub webhooks settings dashboard" /></p>
<hr />
<h2 id="parsing-the-response">Parsing the response</h2>
<p>With your local environment set up, parse the repository update with your Worker.</p>
<p>Initially, your generated <code>index.js</code> should look like this:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		return new Response(&quot;Hello World!&quot;);&#10;	},&#10;};&#10;</code></pre>
<p>Use the <code>request.method</code> property of <a href="/workers/runtime-apis/request/"><code>Request</code></a> to check if the request coming to your application is a <code>POST</code> request, and send an error response if the request is not a <code>POST</code> request.</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		if (request.method !== &quot;POST&quot;) {&#10;			return new Response(&quot;Please send a POST request!&quot;);&#10;		}&#10;	},&#10;};&#10;</code></pre>
<p>Next, validate that the request is sent with the right secret key. GitHub attaches a hash signature for <a href="https://docs.github.com/en/developers/webhooks-and-events/webhooks/securing-your-webhooks">each payload using the secret key</a>. Use a helper function called <code>checkSignature</code> on the request to ensure the hash is correct. Then, you can access data from the webhook by parsing the request as JSON.</p>
<pre tabindex="0"><code class="language-js">async fetch(request, env, ctx) {&#10;  if(request.method !== &#x27;POST&#x27;) {&#10;    return new Response(&#x27;Please send a POST request!&#x27;);&#10;  }&#10;  try {&#10;    const rawBody = await request.text();&#10;&#10;    if (!checkSignature(rawBody, request.headers, env.GITHUB_SECRET_TOKEN)) {&#10;      return new Response(&quot;Wrong password, try again&quot;, {status: 403});&#10;    }&#10;  } catch (e) {&#10;    return new Response(`Error:  ${e}`);&#10;  }&#10;},&#10;</code></pre>
<p>The <code>checkSignature</code> function will use the Node.js crypto library to hash the received payload with your known secret key to ensure it matches the request hash. GitHub uses an HMAC hexdigest to compute the hash in the SHA-256 format. You will place this function at the top of your <code>index.js</code> file, before your export.</p>
<pre tabindex="0"><code class="language-js">import { createHmac, timingSafeEqual } from &quot;node:crypto&quot;;&#10;import { Buffer } from &quot;node:buffer&quot;;&#10;&#10;function checkSignature(text, headers, githubSecretToken) {&#10;	const hmac = createHmac(&quot;sha256&quot;, githubSecretToken);&#10;	hmac.update(text);&#10;	const expectedSignature = hmac.digest(&quot;hex&quot;);&#10;	const actualSignature = headers.get(&quot;x-hub-signature-256&quot;);&#10;&#10;	const trusted = Buffer.from(`sha256=${expectedSignature}`, &quot;ascii&quot;);&#10;	const untrusted = Buffer.from(actualSignature, &quot;ascii&quot;);&#10;&#10;	return (&#10;		trusted.byteLength == untrusted.byteLength &amp;&amp;&#10;		timingSafeEqual(trusted, untrusted)&#10;	);&#10;}&#10;</code></pre>
<p>To make this work, you need to use <a href="/workers/wrangler/commands/general/#secret-put"><code>wrangler secret put</code></a> to set your <code>GITHUB_SECRET_TOKEN</code>. This token is the secret you picked earlier when configuring you GitHub webhook:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler secret put GITHUB_SECRET_TOKEN&#10;</code></pre>
<p>Add the nodejs_compat flag to your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16069.md")
</div>
<hr />
<h2 id="sending-a-text-with-twilio">Sending a text with Twilio</h2>
<p>You will send a text message to you about your repository activity using Twilio. You need a Twilio account and a phone number that can receive text messages. <a href="https://www.twilio.com/messaging/sms">Refer to the Twilio guide to get set up</a>. (If you are new to Twilio, they have <a href="https://www.twilio.com/quest">an interactive game</a> where you can learn how to use their platform and get some free credits for beginners to the service.)</p>
<p>You can then create a helper function to send text messages by sending a <code>POST</code> request to the Twilio API endpoint. <a href="https://www.twilio.com/docs/sms/api/message-resource#create-a-message-resource">Refer to the Twilio reference</a> to learn more about this endpoint.</p>
<p>Create a new function called <code>sendText()</code> that will handle making the request to Twilio:</p>
<pre tabindex="0"><code class="language-js">async function sendText(accountSid, authToken, message) {&#10;	const endpoint = `https://api.twilio.com/2010-04-01/Accounts/${accountSid}/Messages.json`;&#10;&#10;	const encoded = new URLSearchParams({&#10;		To: &quot;%YOUR_PHONE_NUMBER%&quot;,&#10;		From: &quot;%YOUR_TWILIO_NUMBER%&quot;,&#10;		Body: message,&#10;	});&#10;&#10;	const token = btoa(`${accountSid}:${authToken}`);&#10;&#10;	const request = {&#10;		body: encoded,&#10;		method: &quot;POST&quot;,&#10;		headers: {&#10;			Authorization: `Basic ${token}`,&#10;			&quot;Content-Type&quot;: &quot;application/x-www-form-urlencoded&quot;,&#10;		},&#10;	};&#10;&#10;	const response = await fetch(endpoint, request);&#10;	const result = await response.json();&#10;&#10;	return Response.json(result);&#10;}&#10;</code></pre>
<p>To make this work, you need to set some secrets to hide your <code>ACCOUNT_SID</code> and <code>AUTH_TOKEN</code> from the source code. You can set secrets with <a href="/workers/wrangler/commands/general/#secret-put"><code>wrangler secret put</code></a> in your command line.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler secret put TWILIO_ACCOUNT_SID&#10;npx wrangler secret put TWILIO_AUTH_TOKEN&#10;</code></pre>
<p>Modify your <code>githubWebhookHandler</code> to send a text message using the <code>sendText</code> function you just made.</p>
<pre tabindex="0"><code class="language-js">async fetch(request, env, ctx) {&#10;  if(request.method !== &#x27;POST&#x27;) {&#10;    return new Response(&#x27;Please send a POST request!&#x27;);&#10;  }&#10;  try {&#10;    const rawBody = await request.text();&#10;    if (!checkSignature(rawBody, request.headers, env.GITHUB_SECRET_TOKEN)) {&#10;      return new Response(&#x27;Wrong password, try again&#x27;, {status: 403});&#10;    }&#10;&#10;    const action = request.headers.get(&#x27;X-GitHub-Event&#x27;);&#10;    const json = JSON.parse(rawBody);&#10;    const repoName = json.repository.full_name;&#10;    const senderName = json.sender.login;&#10;&#10;    return await sendText(&#10;      env.TWILIO_ACCOUNT_SID,&#10;      env.TWILIO_AUTH_TOKEN,&#10;      `${senderName} completed ${action} onto your repo ${repoName}`&#10;    );&#10;  } catch (e) {&#10;    return new Response(`Error:  ${e}`);&#10;  }&#10;};&#10;</code></pre>
<p>Run the <code>npx wrangler deploy</code> command to redeploy your Worker project:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p><img src="/images/workers/tutorials/github-sms/video-of-receiving-a-text-after-pushing-to-a-repo.gif" alt="Video of receiving a text after pushing to a repo" /></p>
<p>Now when you make an update (that you configured in the GitHub <strong>Webhook</strong> settings) to your repository, you will get a text soon after. If you have never used Git before, refer to the <a href="https://www.datacamp.com/tutorial/git-push-pull">GIT Push and Pull Tutorial</a> for pushing to your repository.</p>
<p>Reference the finished code <a href="https://github.com/rickyrobinett/workers-sdk/tree/main/templates/examples/github-sms-notifications-using-twilio">on GitHub</a>.</p>
<p>By completing this tutorial, you have learned how to build webhooks using Workers, integrate Workers with GitHub and Twilio, and use Worker secrets with Wrangler.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/tutorials/build-a-jamstack-app/">Build a JAMStack app</a></li>
<li><a href="/workers/tutorials/build-a-qr-code-generator/">Build a QR code generator</a></li>
</ul>
