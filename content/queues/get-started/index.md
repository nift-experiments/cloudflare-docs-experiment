---
cp9:
  canonical: https://developers.cloudflare.com/queues/get-started/
  description: Create your first Cloudflare Queue, a producer Worker, and a consumer Worker.
  full_title: Getting started · Cloudflare Queues docs
  head_html: <title>Getting started · Cloudflare Queues docs</title><meta name="generator" content="Nift"><meta name="description" content="Create your first Cloudflare Queue, a producer Worker, and a consumer Worker."><link rel="canonical" href="https://developers.cloudflare.com/queues/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/queues/get-started/index.md"><meta property="og:title" content="Getting started · Cloudflare Queues docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create your first Cloudflare Queue, a producer Worker, and a consumer Worker."><meta property="og:url" content="https://developers.cloudflare.com/queues/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Queues"><meta name="algolia_product_filter" content="Queues"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Queues,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/queues/get-started/#page","headline":"Getting started \u00b7 Cloudflare Queues docs","description":"Create your first Cloudflare Queue, a producer Worker, and a consumer Worker.","url":"https://developers.cloudflare.com/queues/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /queues/get-started/
  schema: 1
---
<p>Cloudflare Queues is a flexible messaging queue that allows you to queue messages for asynchronous processing. By following this guide, you will create your first queue, a Worker to publish messages to that queue, and a consumer Worker to consume messages from that queue.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To use Queues, you will need:</p>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/589.md")
</div></details>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<p>You will access your queue from a Worker, the producer Worker. You must create at least one producer Worker to publish messages onto your queue. If you are using <a href="/r2/buckets/event-notifications/">R2 Bucket Event Notifications</a>, then you do not need a producer Worker.</p>
<p>To create a producer Worker, run:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- producer-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- producer-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare producer-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare producer-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest producer-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest producer-worker" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>This will create a new directory, which will include both a <code>src/index.ts</code> Worker script, and a <a href="/workers/wrangler/configuration/"><code>wrangler.jsonc</code></a> configuration file. After you create your Worker, you will create a Queue to access.</p>
<p>Move into the newly created directory:</p>
<pre tabindex="0"><code class="language-sh">cd producer-worker&#10;</code></pre>
<h2 id="2-create-a-queue"><ol start="2">
<li>Create a queue</li>
</ol></h2>
<p>To use queues, you need to create at least one queue to publish messages to and consume messages from.</p>
<p>To create a queue, run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler queues create &lt;MY-QUEUE-NAME&gt;&#10;</code></pre>
<p>Choose a name that is descriptive and relates to the types of messages you intend to use this queue for. Descriptive queue names look like: <code>debug-logs</code>, <code>user-clickstream-data</code>, or <code>password-reset-prod</code>.</p>
<p>Queue names must be 1 to 63 characters long. Queue names cannot contain special characters outside dashes (<code>-</code>), and must start and end with a letter or number.</p>
<p>You cannot change your queue name after you have set it. After you create your queue, you will set up your producer Worker to access it.</p>
<h2 id="3-set-up-your-producer-worker"><ol start="3">
<li>Set up your producer Worker</li>
</ol></h2>
<p>To expose your queue to the code inside your Worker, you need to connect your queue to your Worker by creating a binding. <a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Worker to access resources, such as Queues, on the Cloudflare developer platform.</p>
<p>To create a binding, open your newly generated <code>wrangler.jsonc</code> file and add the following:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/590.md")
</div>
<p>Replace <code>MY-QUEUE-NAME</code> with the name of the queue you created in <a href="/queues/get-started/#2-create-a-queue">step 2</a>. Next, replace <code>MY_QUEUE</code> with the name you want for your <code>binding</code>. The binding must be a valid JavaScript variable name. This is the variable you will use to reference this queue in your Worker.</p>
<h3 id="write-your-producer-worker">Write your producer Worker</h3>
<p>You will now configure your producer Worker to create messages to publish to your queue. Your producer Worker will:</p>
<ol>
<li>Take a request it receives from the browser.</li>
<li>Transform the request to JSON format.</li>
<li>Write the request directly to your queue.</li>
</ol>
<p>In your Worker project directory, open the <code>src</code> folder and add the following to your <code>index.ts</code> file:</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;  async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;    const log = {&#10;      url: request.url,&#10;      method: request.method,&#10;      headers: Object.fromEntries(request.headers),&#10;    };&#10;    await env.&lt;MY_QUEUE&gt;.send(log);&#10;    return new Response(&quot;Success!&quot;);&#10;  },&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>Replace <code>MY_QUEUE</code> with the name you have set for your binding from your <code>wrangler.jsonc</code> file.</p>
<p>Also add the queue to <code>Env</code> interface in <code>index.ts</code>.</p>
<pre tabindex="0"><code class="language-ts">export interface Env {&#10;   &lt;MY_QUEUE&gt;: Queue;&#10;}&#10;</code></pre>
<p>If this write fails, your Worker will return an error (raise an exception). If this write works, it will return <code>Success</code> back with a HTTP <code>200</code> status code to the browser.</p>
<p>In a production application, you would likely use a <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch"><code>try...catch</code></a> statement to catch the exception and handle it directly (for example, return a custom error or even retry).</p>
<h3 id="publish-your-producer-worker">Publish your producer Worker</h3>
<p>With your Wrangler file and <code>index.ts</code> file configured, you are ready to publish your producer Worker. To publish your producer Worker, run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>You should see output that resembles the below, with a <code>*.workers.dev</code> URL by default.</p>
<pre tabindex="0"><code>Uploaded &lt;YOUR-WORKER-NAME&gt; (0.76 sec)&#10;Published &lt;YOUR-WORKER-NAME&gt; (0.29 sec)&#10;  https://&lt;YOUR-WORKER-NAME&gt;.&lt;YOUR-ACCOUNT&gt;.workers.dev&#10;</code></pre>
<p>Copy your <code>*.workers.dev</code> subdomain and paste it into a new browser tab. Refresh the page a few times to start publishing requests to your queue. Your browser should return the <code>Success</code> response after writing the request to the queue each time.</p>
<p>You have built a queue and a producer Worker to publish messages to the queue. You will now create a consumer Worker to consume the messages published to your queue. Without a consumer Worker, the messages will stay on the queue until they expire, which defaults to four (4) days.</p>
<h2 id="4-create-your-consumer-worker"><ol start="4">
<li>Create your consumer Worker</li>
</ol></h2>
<p>A consumer Worker receives messages from your queue. When the consumer Worker receives your queue's messages, it can write them to another source, such as a logging console or storage objects.</p>
<p>In this guide, you will create a consumer Worker and use it to log and inspect the messages with <a href="/workers/wrangler/commands/general/#tail"><code>wrangler tail</code></a>. You will create your consumer Worker in the same Worker project that you created your producer Worker.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/588.md")
</aside>
<p>To create a consumer Worker, open your <code>index.ts</code> file and add the following <code>queue</code> handler to your existing <code>fetch</code> handler:</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;  async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;    const log = {&#10;      url: request.url,&#10;      method: request.method,&#10;      headers: Object.fromEntries(request.headers),&#10;    };&#10;    await env.&lt;MY_QUEUE&gt;.send(log);&#10;    return new Response(&quot;Success!&quot;);&#10;  },&#10;  async queue(batch, env, ctx): Promise&lt;void&gt; {&#10;    for (const message of batch.messages) {&#10;      console.log(&quot;consumed from our queue:&quot;, JSON.stringify(message.body));&#10;    }&#10;  },&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>Replace <code>MY_QUEUE</code> with the name you have set for your binding from your <code>wrangler.jsonc</code> file.</p>
<p>Every time messages are published to the queue, your consumer Worker's <code>queue</code> handler (<code>async queue</code>) is called and it is passed one or more messages.</p>
<p>In this example, your consumer Worker transforms the queue's JSON formatted message into a string and logs that output. In a real world application, your consumer Worker can be configured to write messages to object storage (such as <a href="/r2/">R2</a>), write to a database (like <a href="/d1/">D1</a>), further process messages before calling an external API (such as an <a href="/workers/tutorials/">email API</a>) or a data warehouse with your legacy cloud provider.</p>
<p>When performing asynchronous tasks from within your consumer handler, use <code>waitUntil()</code> to ensure the response of the function is handled. Other asynchronous methods are not supported within the scope of this method.</p>
<h3 id="connect-the-consumer-worker-to-your-queue">Connect the consumer Worker to your queue</h3>
<p>After you have configured your consumer Worker, you are ready to connect it to your queue.</p>
<p>Each queue can only have one consumer Worker connected to it. If you try to connect multiple consumers to the same queue, you will encounter an error when attempting to publish that Worker.</p>
<p>To connect your queue to your consumer Worker, open your Wrangler file and add this to the bottom:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/591.md")
</div>
<p>Replace <code>MY-QUEUE-NAME</code> with the queue you created in <a href="/queues/get-started/#2-create-a-queue">step 2</a>.</p>
<p>In your consumer Worker, you are using queues to auto batch messages using the <code>max_batch_size</code> option and the <code>max_batch_timeout</code> option. The consumer Worker will receive messages in batches of <code>10</code> or every <code>5</code> seconds, whichever happens first.</p>
<p><code>max_batch_size</code> (defaults to 10) helps to reduce the amount of times your consumer Worker needs to be called. Instead of being called for every message, it will only be called after 10 messages have entered the queue.</p>
<p><code>max_batch_timeout</code> (defaults to 5 seconds) helps to reduce wait time. If the producer Worker is not sending up to 10 messages to the queue for the consumer Worker to be called, the consumer Worker will be called every 5 seconds to receive messages that are waiting in the queue.</p>
<h3 id="publish-your-consumer-worker">Publish your consumer Worker</h3>
<p>With your Wrangler file and <code>index.ts</code> file configured, publish your consumer Worker by running:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<h2 id="5-read-messages-from-your-queue"><ol start="5">
<li>Read messages from your queue</li>
</ol></h2>
<p>After you set up consumer Worker, you can read messages from the queue.</p>
<p>Run <code>wrangler tail</code> to start waiting for our consumer to log the messages it receives:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler tail&#10;</code></pre>
<p>With <code>wrangler tail</code> running, open the Worker URL you opened in <a href="/queues/get-started/#3-set-up-your-producer-worker">step 3</a>.</p>
<p>You should receive a <code>Success</code> message in your browser window.</p>
<p>If you receive a <code>Success</code> message, refresh the URL a few times to generate messages and push them onto the queue.</p>
<p>With <code>wrangler tail</code> running, your consumer Worker will start logging the requests generated by refreshing.</p>
<p>If you refresh less than 10 times, it may take a few seconds for the messages to appear because batch timeout is configured for 10 seconds. After 10 seconds, messages should arrive in your terminal.</p>
<p>If you get errors when you refresh, check that the queue name you created in <a href="/queues/get-started/#2-create-a-queue">step 2</a> and the queue you referenced in your Wrangler file is the same. You should ensure that your producer Worker is returning <code>Success</code> and is not returning an error.</p>
<p>By completing this guide, you have now created a queue, a producer Worker that publishes messages to that queue, and a consumer Worker that consumes those messages from it.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>Learn more about <a href="/workers/">Cloudflare Workers</a> and the applications you can build on Cloudflare.</li>
</ul>
