---
cp9:
  canonical: https://developers.cloudflare.com/workers/tutorials/deploy-a-realtime-chat-app/
  description: This tutorial shows how to deploy a serverless, real-time chat application. The chat application uses a Durable Object to control each chat room.
  full_title: Deploy a real-time chat application · Cloudflare Workers docs
  head_html: <title>Deploy a real-time chat application · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial shows how to deploy a serverless, real-time chat application. The chat application uses a Durable Object to control each chat room."><link rel="canonical" href="https://developers.cloudflare.com/workers/tutorials/deploy-a-realtime-chat-app/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/tutorials/deploy-a-realtime-chat-app/index.md"><meta property="og:title" content="Deploy a real-time chat application · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial shows how to deploy a serverless, real-time chat application. The chat application uses a Durable Object to control each chat room."><meta property="og:url" content="https://developers.cloudflare.com/workers/tutorials/deploy-a-realtime-chat-app/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Durable Objects"><meta name="pcx_tags" content="JavaScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/tutorials/deploy-a-realtime-chat-app/#page","headline":"Deploy a real-time chat application \u00b7 Cloudflare Workers docs","description":"This tutorial shows how to deploy a serverless, real-time chat application. The chat application uses a Durable Object to control each chat room.","url":"https://developers.cloudflare.com/workers/tutorials/deploy-a-realtime-chat-app/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript"]}</script>
  markdown: true
  noindex: false
  route: /workers/tutorials/deploy-a-realtime-chat-app/
  schema: 1
---
<p>In this tutorial, you will deploy a serverless, real-time chat application that runs using <a href="/durable-objects/">Durable Objects</a>.</p>
<p>This chat application uses a Durable Object to control each chat room. Users connect to the Object using WebSockets. Messages from one user are broadcast to all the other users. The chat history is also stored in durable storage. Real-time messages are relayed directly from one user to others without going through the storage layer.</p>
<h2 id="before-you-start">Before you start</h2>
<p>All of the tutorials assume you have already completed the <a href="/workers/get-started/guide/">Get started guide</a>, which gets you set up with a Cloudflare Workers account, <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a>, and <a href="/workers/wrangler/install-and-update/">Wrangler</a>.</p>
<h2 id="clone-the-chat-application-repository">Clone the chat application repository</h2>
<p>Open your terminal and clone the <a href="https://github.com/cloudflare/workers-chat-demo">workers-chat-demo</a> repository:</p>
<pre tabindex="0"><code class="language-sh">git clone https://github.com/cloudflare/workers-chat-demo.git&#10;</code></pre>
<h2 id="authenticate-wrangler">Authenticate Wrangler</h2>
<p>After you have cloned the repository, authenticate Wrangler by running:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login&#10;</code></pre>
<h2 id="deploy-your-project">Deploy your project</h2>
<p>When you are ready to deploy your application, run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Your application will be deployed to your <code>*.workers.dev</code> subdomain.</p>
<p>To deploy your application to a custom domain within the Cloudflare dashboard, go to your Worker &gt; <strong>Triggers</strong> &gt; <strong>Add Custom Domain</strong>.</p>
<p>To deploy your application to a custom domain using Wrangler, open your project's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<p>To configure a route in your Wrangler configuration file, add the following to your environment:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16075.md")
</div>
<p>If you have specified your zone ID in the environment of your Wrangler configuration file, you will not need to write it again in object form.</p>
<p>To configure a subdomain in your Wrangler configuration file, add the following to your environment:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16076.md")
</div>
<p>To test your live application:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your Worker &gt; <strong>Triggers</strong> &gt; <strong>Routes</strong> &gt; Select the <code>edge-chat-demo.&lt;SUBDOMAIN&gt;.workers.dev</code> route.</li>
<li>Enter a name in the <strong>your name</strong> field.</li>
<li>Choose whether to enter a public room or create a private room.</li>
<li>Send the link to other participants. You will be able to view room participants on the right side of the screen.</li>
</ol>
<h2 id="uninstall-your-application">Uninstall your application</h2>
<p>To uninstall your chat application, modify your Wrangler file to remove the <code>durable_objects</code> bindings and add a <code>deleted_classes</code> migration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16077.md")
</div>
<p>Then run <code>npx wrangler deploy</code>.</p>
<p>To delete your Worker:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Overview</strong>, select your Worker.</li>
<li>Select <strong>Manage Service</strong> &gt; <strong>Delete</strong>. For complete instructions on set up and deletion, refer to the <code>README.md</code> in your cloned repository.</li>
</ol>
<p>By completing this tutorial, you have deployed a real-time chat application with Durable Objects and Cloudflare Workers.</p>
<h2 id="related-resources">Related resources</h2>
<p>Continue building with other Cloudflare Workers tutorials below.</p>
<ul>
<li><a href="/workers/tutorials/build-a-slackbot/">Build a Slackbot</a></li>
<li><a href="/workers/tutorials/github-sms-notifications-using-twilio/">Create SMS notifications for your GitHub repository using Twilio</a></li>
<li><a href="/workers/tutorials/build-a-qr-code-generator/">Build a QR code generator</a></li>
</ul>
