<p>This example provides a step-by-step guide on using <a href="/r2/buckets/event-notifications/">event notifications</a> to capture and store R2 upload logs in a separate bucket.</p>
<p><img src="/assets/upstream/images/reference-architecture/event-notifications-for-storage/pushed-based-event-notification.svg" alt="Push-Based R2 Event Notifications" /></p>
<h2 id="1-install-wrangler"><ol>
<li>Install Wrangler</li>
</ol></h2>
<p>To begin, refer to <a href="/workers/wrangler/install-and-update/#install-wrangler">Install/Update Wrangler</a> to install Wrangler, the Cloudflare Developer Platform CLI.</p>
<h2 id="2-create-r2-buckets"><ol start="2">
<li>Create R2 buckets</li>
</ol></h2>
<p>You will need to create two R2 buckets:</p>
<ul>
<li><code>example-upload-bucket</code>: When new objects are uploaded to this bucket, your <a href="/queues/get-started/#4-create-your-consumer-worker">consumer Worker</a> will write logs.</li>
<li><code>example-log-sink-bucket</code>: Upload logs from <code>example-upload-bucket</code> will be written to this bucket.</li>
</ul>
<p>To create the buckets, run the following Wrangler commands:</p>
<pre><code class="language-sh">npx wrangler r2 bucket create example-upload-bucket&#10;npx wrangler r2 bucket create example-log-sink-bucket&#10;</code></pre>
<h2 id="3-create-a-queue"><ol start="3">
<li>Create a queue</li>
</ol></h2>
<p>Event notifications capture changes to data in <code>example-upload-bucket</code>. You will need to create a new queue to receive notifications:</p>
<pre><code class="language-sh">npx wrangler queues create example-event-notification-queue&#10;</code></pre>
<h2 id="4-create-a-worker"><ol start="4">
<li>Create a Worker</li>
</ol></h2>
<p>Before you enable event notifications for <code>example-upload-bucket</code>, you need to create a <a href="/queues/reference/how-queues-works/#create-a-consumer-worker">consumer Worker</a> to receive the notifications.</p>
<p>Create a new Worker with C3 (<code>create-cloudflare</code> CLI). <a href="/pages/get-started/c3/">C3</a> is a command-line tool designed to help you set up and deploy new applications, including Workers, to Cloudflare.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- consumer-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- consumer-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare consumer-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare consumer-worker" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest consumer-worker</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest consumer-worker" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Then, move into your newly created directory:</p>
<pre><code class="language-sh">cd consumer-worker&#10;</code></pre>
<h2 id="5-configure-your-worker"><ol start="5">
<li>Configure your Worker</li>
</ol></h2>
<p>In your Worker project's [<a href="/workers/wrangler/configuration/">Wrangler configuration file</a>](/workers/wrangler/configuration/), add a <a href="/workers/wrangler/configuration/#queues">queue consumer</a> and <a href="/workers/wrangler/configuration/#r2-buckets">R2 bucket binding</a>. The queues consumer bindings will register your Worker as a consumer of your future event notifications and the R2 bucket bindings will allow your Worker to access your R2 bucket.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11355.md")
</div>
<h2 id="6-write-event-notification-messages-to-r2"><ol start="6">
<li>Write event notification messages to R2</li>
</ol></h2>
<p>Add a <a href="/queues/configuration/javascript-apis/#consumer"><code>queue</code> handler</a> to <code>src/index.ts</code> to handle writing batches of notifications to our log sink bucket (you do not need a <a href="/workers/runtime-apis/handlers/fetch/">fetch handler</a>):</p>
<pre><code class="language-ts">export interface Env {&#10;	LOG_SINK: R2Bucket;&#10;}&#10;&#10;export default {&#10;	async queue(batch, env): Promise&lt;void&gt; {&#10;		const batchId = new Date().toISOString().replace(/[:.]/g, &quot;-&quot;);&#10;		const fileName = `upload-logs-${batchId}.json`;&#10;&#10;		// Serialize the entire batch of messages to JSON&#10;		const fileContent = new TextEncoder().encode(&#10;			JSON.stringify(batch.messages),&#10;		);&#10;&#10;		// Write the batch of messages to R2&#10;		await env.LOG_SINK.put(fileName, fileContent, {&#10;			httpMetadata: {&#10;				contentType: &quot;application/json&quot;,&#10;			},&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<h2 id="7-deploy-your-worker"><ol start="7">
<li>Deploy your Worker</li>
</ol></h2>
<p>To deploy your consumer Worker, run the <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a> command:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<h2 id="8-enable-event-notifications"><ol start="8">
<li>Enable event notifications</li>
</ol></h2>
<p>Now that you have your consumer Worker ready to handle incoming event notification messages, you need to enable event notifications with the <a href="/workers/wrangler/commands/r2/#r2-bucket-notification-create"><code>wrangler r2 bucket notification create</code> command</a> for <code>example-upload-bucket</code>:</p>
<pre><code class="language-sh">npx wrangler r2 bucket notification create example-upload-bucket --event-type object-create --queue example-event-notification-queue&#10;</code></pre>
<h2 id="9-test"><ol start="9">
<li>Test</li>
</ol></h2>
<p>Now you can test the full end-to-end flow by uploading an object to <code>example-upload-bucket</code> in the Cloudflare dashboard. After you have uploaded an object, logs will appear in <code>example-log-sink-bucket</code> in a few seconds.</p>
