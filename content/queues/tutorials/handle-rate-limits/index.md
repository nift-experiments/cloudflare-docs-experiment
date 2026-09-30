<p class="article-summary">Example of how to use Queues to handle rate limits of external APIs.</p>
<p>This tutorial explains how to use Queues to handle rate limits of external APIs by building an application that sends email notifications using <a href="https://www.resend.com/">Resend</a>. However, you can use this pattern to handle rate limits of any external API.</p>
<p>Resend is a service that allows you to send emails from your application via an API. Resend has a default <a href="https://resend.com/docs/api-reference/introduction#rate-limit">rate limit</a> of two requests per second. You will use Queues to handle the rate limit of Resend.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11317.md")
</div></details>
<ol start="4">
<li>
<p>Sign up for <a href="https://resend.com/">Resend</a> and generate an API key by following the guide on the <a href="https://resend.com/docs/dashboard/api-keys/introduction">Resend documentation</a>.</p>
</li>
<li>
<p>Additionally, you will need access to Cloudflare Queues.</p>
</li>
</ol>
<p>Queues is included in the monthly subscription cost of your Workers Paid plan, and charges based on operations against your queues. A limited version of Queues is also available on the Workers Free plan. Refer to <a href="/queues/platform/pricing/">Pricing</a> for more details.</p>
<p>Before you can use Queues, you must enable it via <a href="https://dash.cloudflare.com/?to=/:account/workers/queues">the Cloudflare dashboard</a>. You need a Workers Paid plan to enable Queues.</p>
<p>To enable Queues:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Queues</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Enable Queues</strong>.</li>
</ol>
<h2 id="1-create-a-new-workers-application"><ol>
<li>Create a new Workers application</li>
</ol></h2>
<p>To get started, create a Worker application using the <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare"><code>create-cloudflare</code> CLI</a>. Open a terminal window and run the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- resend-rate-limit-queue</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- resend-rate-limit-queue" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare resend-rate-limit-queue</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare resend-rate-limit-queue" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest resend-rate-limit-queue</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest resend-rate-limit-queue" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Then, go to your newly created directory:</p>
<pre><code class="language-sh">cd resend-rate-limit-queue&#10;</code></pre>
<h2 id="2-set-up-a-queue"><ol start="2">
<li>Set up a Queue</li>
</ol></h2>
<p>You need to create a Queue and a binding to your Worker. Run the following command to create a Queue named <code>rate-limit-queue</code>:</p>
<pre><code class="language-sh">npx wrangler queues create rate-limit-queue&#10;</code></pre>
<pre><code class="language-sh">Creating queue rate-limit-queue.&#10;Created queue rate-limit-queue.&#10;</code></pre>
<h3 id="add-queue-bindings-to-your-wrangler-configuration-file-workers-wrangler-configuration">Add Queue bindings to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a></h3>
<p>In your Wrangler file, add the following:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11318.md")
</div>
<p>It is important to include the <code>max_batch_size</code> of two to the consumer queue is important because the Resend API has a default rate limit of two requests per second. This batch size allows the queue to process the message in the batch size of two. If the batch size is less than two, the queue will wait for 10 seconds to collect the next message. If no more messages are available, the queue will process the message in the batch. For more information, refer to the <a href="/queues/configuration/batching-retries">Batching, Retries and Delays documentation</a></p>
<p>Your final Wrangler file should look similar to the example below.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11319.md")
</div>
<h2 id="3-add-bindings-to-environment"><ol start="3">
<li>Add bindings to environment</li>
</ol></h2>
<p>Add the bindings to the environment interface in <code>worker-configuration.d.ts</code>, so TypeScript correctly types the bindings. The queue is typed as <code>Queue&lt;Message&gt;</code>, where <code>Message</code> is defined in the following step.</p>
<pre><code class="language-ts">interface Env {&#10;	EMAIL_QUEUE: Queue&lt;Message&gt;;&#10;}&#10;</code></pre>
<h2 id="4-send-message-to-the-queue"><ol start="4">
<li>Send message to the queue</li>
</ol></h2>
<p>The application will send a message to the queue when the Worker receives a request. For simplicity, you will send the email address as a message to the queue. A new message will be sent to the queue with a delay of one second.</p>
<pre><code class="language-ts">export default {&#10;	async fetch(req, env, ctx): Promise&lt;Response&gt; {&#10;		try {&#10;			await env.EMAIL_QUEUE.send(&#10;				{ email: await req.text() },&#10;				{ delaySeconds: 1 },&#10;			);&#10;			return new Response(&quot;Success!&quot;);&#10;		} catch (e) {&#10;			return new Response(&quot;Error!&quot;, { status: 500 });&#10;		}&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>This will accept requests to any subpath and forwards the request's body. It expects that the request body to contain only an email. In production, you should check that the request was a <code>POST</code> request. You should also avoid sending such sensitive information (email) directly to the queue. Instead, you can send a message to the queue that contains a unique identifier for the user. Then, your consumer queue can use the unique identifier to look up the email address in a database and use that to send the email.</p>
<h2 id="5-process-the-messages-in-the-queue"><ol start="5">
<li>Process the messages in the queue</li>
</ol></h2>
<p>After the message is sent to the queue, it will be processed by the consumer Worker. The consumer Worker will process the message and send the email.</p>
<p>Since you have not configured Resend yet, you will log the message to the console. After you configure Resend, you will use it to send the email.</p>
<p>Add the <code>queue()</code> handler as shown below:</p>
<pre><code class="language-ts">interface Message {&#10;	email: string;&#10;}&#10;&#10;export default {&#10;	async fetch(req, env, ctx): Promise&lt;Response&gt; {&#10;		try {&#10;			await env.EMAIL_QUEUE.send(&#10;				{ email: await req.text() },&#10;				{ delaySeconds: 1 },&#10;			);&#10;			return new Response(&quot;Success!&quot;);&#10;		} catch (e) {&#10;			return new Response(&quot;Error!&quot;, { status: 500 });&#10;		}&#10;	},&#10;	async queue(batch, env, ctx): Promise&lt;void&gt; {&#10;		for (const message of batch.messages) {&#10;			try {&#10;				console.log(message.body.email);&#10;				// After configuring Resend, you can send email&#10;				message.ack();&#10;			} catch (e) {&#10;				console.error(e);&#10;				message.retry({ delaySeconds: 5 });&#10;			}&#10;		}&#10;	},&#10;} satisfies ExportedHandler&lt;Env, Message&gt;;&#10;</code></pre>
<p>The above <code>queue()</code> handler will log the email address to the console and send the email. It will also retry the message if sending the email fails. The <code>delaySeconds</code> is set to five seconds to avoid sending the email too quickly.</p>
<p>To test the application, run the following command:</p>
<pre><code class="language-sh">npm run dev&#10;</code></pre>
<p>Use the following cURL command to send a request to the application:</p>
<pre><code class="language-sh">curl -X POST -d &quot;test@example.com&quot; http://localhost:8787/&#10;</code></pre>
<pre><code class="language-sh">[wrangler:inf] POST / 200 OK (2ms)&#10;QueueMessage {&#10;  attempts: 1,&#10;  body: { email: &#x27;test@example.com&#x27; },&#10;  timestamp: 2024-09-12T13:48:07.236Z,&#10;  id: &#x27;72a25ff18dd441f5acb6086b9ce87c8c&#x27;&#10;}&#10;</code></pre>
<h2 id="6-set-up-resend"><ol start="6">
<li>Set up Resend</li>
</ol></h2>
<p>To call the Resend API, you need to configure the Resend API key. Create a <code>.dev.vars</code> file in the root of your project and add the following:</p>
<pre><code class="language-txt">RESEND_API_KEY=&#x27;your-resend-api-key&#x27;&#10;</code></pre>
<p>Replace <code>your-resend-api-key</code> with your actual Resend API key.</p>
<p>Next, update the <code>Env</code> interface in <code>worker-configuration.d.ts</code> to include the <code>RESEND_API_KEY</code> variable.</p>
<pre><code class="language-ts">interface Env {&#10;	EMAIL_QUEUE: Queue&lt;Message&gt;;&#10;	RESEND_API_KEY: string;&#10;}&#10;</code></pre>
<p>Lastly, install the <a href="https://www.npmjs.com/package/resend"><code>resend</code> package</a> using the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i resend</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i resend" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add resend</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add resend" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add resend</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add resend" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add resend</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add resend" aria-label="Copy to clipboard">Copy</button></div></div>
<p>You can now use the <code>RESEND_API_KEY</code> variable in your code.</p>
<h2 id="7-send-email-with-resend"><ol start="7">
<li>Send email with Resend</li>
</ol></h2>
<p>In your <code>src/index.ts</code> file, import the Resend package and update the <code>queue()</code> handler to send the email.</p>
<pre><code class="language-ts">import { Resend } from &quot;resend&quot;;&#10;&#10;interface Message {&#10;	email: string;&#10;}&#10;&#10;export default {&#10;	async fetch(req, env, ctx): Promise&lt;Response&gt; {&#10;		try {&#10;			await env.EMAIL_QUEUE.send(&#10;				{ email: await req.text() },&#10;				{ delaySeconds: 1 },&#10;			);&#10;			return new Response(&quot;Success!&quot;);&#10;		} catch (e) {&#10;			return new Response(&quot;Error!&quot;, { status: 500 });&#10;		}&#10;	},&#10;	async queue(batch, env, ctx): Promise&lt;void&gt; {&#10;		// Initialize Resend&#10;		const resend = new Resend(env.RESEND_API_KEY);&#10;		for (const message of batch.messages) {&#10;			try {&#10;				console.log(message.body.email);&#10;				// send email&#10;				const sendEmail = await resend.emails.send({&#10;					from: &quot;onboarding@resend.dev&quot;,&#10;					to: [message.body.email],&#10;					subject: &quot;Hello World&quot;,&#10;					html: &quot;&lt;strong&gt;Sending an email from Worker!&lt;/strong&gt;&quot;,&#10;				});&#10;&#10;				// check if the email failed&#10;				if (sendEmail.error) {&#10;					console.error(sendEmail.error);&#10;					message.retry({ delaySeconds: 5 });&#10;				} else {&#10;					// if success, ack the message&#10;					message.ack();&#10;				}&#10;				message.ack();&#10;			} catch (e) {&#10;				console.error(e);&#10;				message.retry({ delaySeconds: 5 });&#10;			}&#10;		}&#10;	},&#10;} satisfies ExportedHandler&lt;Env, Message&gt;;&#10;</code></pre>
<p>The <code>queue()</code> handler will now send the email using the Resend API. It also checks if sending the email failed and will retry the message.</p>
<p>The final script is included below:</p>
<pre><code class="language-ts">import { Resend } from &quot;resend&quot;;&#10;&#10;interface Message {&#10;	email: string;&#10;}&#10;&#10;export default {&#10;	async fetch(req, env, ctx): Promise&lt;Response&gt; {&#10;		try {&#10;			await env.EMAIL_QUEUE.send(&#10;				{ email: await req.text() },&#10;				{ delaySeconds: 1 },&#10;			);&#10;			return new Response(&quot;Success!&quot;);&#10;		} catch (e) {&#10;			return new Response(&quot;Error!&quot;, { status: 500 });&#10;		}&#10;	},&#10;	async queue(batch, env, ctx): Promise&lt;void&gt; {&#10;		// Initialize Resend&#10;		const resend = new Resend(env.RESEND_API_KEY);&#10;		for (const message of batch.messages) {&#10;			try {&#10;				// send email&#10;				const sendEmail = await resend.emails.send({&#10;					from: &quot;onboarding@resend.dev&quot;,&#10;					to: [message.body.email],&#10;					subject: &quot;Hello World&quot;,&#10;					html: &quot;&lt;strong&gt;Sending an email from Worker!&lt;/strong&gt;&quot;,&#10;				});&#10;&#10;				// check if the email failed&#10;				if (sendEmail.error) {&#10;					console.error(sendEmail.error);&#10;					message.retry({ delaySeconds: 5 });&#10;				} else {&#10;					// if success, ack the message&#10;					message.ack();&#10;				}&#10;			} catch (e) {&#10;				console.error(e);&#10;				message.retry({ delaySeconds: 5 });&#10;			}&#10;		}&#10;	},&#10;} satisfies ExportedHandler&lt;Env, Message&gt;;&#10;</code></pre>
<p>To test the application, start the development server using the following command:</p>
<pre><code class="language-sh">npm run dev&#10;</code></pre>
<p>Use the following cURL command to send a request to the application:</p>
<pre><code class="language-sh">curl -X POST -d &quot;delivered@resend.dev&quot; http://localhost:8787/&#10;</code></pre>
<p>On the Resend dashboard, you should see that the email was sent to the provided email address.</p>
<h2 id="8-deploy-your-worker"><ol start="8">
<li>Deploy your Worker</li>
</ol></h2>
<p>To deploy your Worker, run the following command:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Lastly, add the Resend API key using the following command:</p>
<pre><code class="language-sh">npx wrangler secret put RESEND_API_KEY&#10;</code></pre>
<p>Enter the value of your API key. Your API key will get added to your project. You can now use the <code>RESEND_API_KEY</code> variable in your code.</p>
<p>You have successfully created a Worker which can send emails using the Resend API respecting rate limits.</p>
<p>To test your Worker, you could use the following cURL request. Replace <code>&lt;YOUR_WORKER_URL&gt;</code> with the URL of your deployed Worker.</p>
<pre><code class="language-bash">curl -X POST -d &quot;delivered@resend.dev&quot; &lt;YOUR_WORKER_URL&gt;&#10;</code></pre>
<p>Refer to the <a href="https://github.com/harshil1712/queues-rate-limit">GitHub repository</a> for the complete code for this tutorial. If you are using <a href="https://hono.dev/">Hono</a>, you can refer to the <a href="https://github.com/harshil1712/resend-rate-limit-demo">Hono example</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/queues/reference/how-queues-works/">How Queues works</a></li>
<li><a href="/queues/configuration/batching-retries/">Queues Batching and Retries</a></li>
<li><a href="https://resend.com/docs/">Resend</a></li>
</ul>
