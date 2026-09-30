<p>Consumer concurrency allows a <a href="/queues/reference/how-queues-works/#consumers">consumer Worker</a> processing messages from a queue to automatically scale out horizontally to keep up with the rate that messages are being written to a queue.</p>
<p>In many systems, the rate at which you write messages to a queue can easily exceed the rate at which a single consumer can read and process those same messages. This is often because your consumer might be parsing message contents, writing to storage or a database, or making third-party (upstream) API calls.</p>
<p>Note that queue producers are always scalable, up to the <a href="/queues/platform/limits/">maximum supported messages-per-second</a> (per queue) limit.</p>
<h2 id="enable-concurrency">Enable concurrency</h2>
<p>By default, all queues have concurrency enabled. Queue consumers will automatically scale up <a href="/queues/platform/limits/">to the maximum concurrent invocations</a> as needed to manage a queue's backlog and/or error rates.</p>
<h2 id="how-concurrency-works">How concurrency works</h2>
<p>After processing a batch of messages, Queues will check to see if the number of concurrent consumers should be adjusted. The number of concurrent consumers invoked for a queue will autoscale based on several factors, including:</p>
<ul>
<li>The number of messages in the queue (backlog) and its rate of growth.</li>
<li>The ratio of failed (versus successful) invocations. A failed invocation is when your <code>queue()</code> handler returns an uncaught exception instead of <code>void</code> (nothing).</li>
<li>The value of <code>max_concurrency</code> set for that consumer.</li>
</ul>
<p>Where possible, Queues will optimize for keeping your backlog from growing exponentially, in order to minimize scenarios where the backlog of messages in a queue grows to the point that they would reach the <a href="/queues/platform/limits/">message retention limit</a> before being processed.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="consumer-concurrency-and-retried-messages">Consumer concurrency and retried messages</h3>
@markup("md", "content/.markup/bodies/11280.md")
</aside>
<h3 id="example">Example</h3>
<p>If you are writing 100 messages/second to a queue with a single concurrent consumer that takes 5 seconds to process a batch of 100 messages, the number of messages in-flight will continue to grow at a rate faster than your consumer can keep up.</p>
<p>In this scenario, Queues will notice the growing backlog and will scale the number of concurrent consumer Workers invocations up to a steady-state of (approximately) five (5) until the rate of incoming messages decreases, the consumer processes messages faster, or the consumer begins to generate errors.</p>
<h3 id="why-are-my-consumers-not-autoscaling">Why are my consumers not autoscaling?</h3>
<p>If your consumers are not autoscaling, there are a few likely causes:</p>
<ul>
<li><code>max_concurrency</code> has been set to 1.</li>
<li>Your consumer Worker is returning errors rather than processing messages. Inspect your consumer to make sure it is healthy.</li>
<li>A batch of messages is being processed. Queues checks if it should autoscale consumers only after processing an entire batch of messages, so it will not autoscale while a batch is being processed. Consider reducing batch sizes or refactoring your consumer to process messages faster.</li>
</ul>
<h2 id="limit-concurrency">Limit concurrency</h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="recommended-concurrency-setting">Recommended concurrency setting</h3>
@markup("md", "content/.markup/bodies/11279.md")
</aside>
<p>If you have a workflow that is limited by an upstream API and/or system, you may prefer for your backlog to grow, trading off increased overall latency in order to avoid overwhelming an upstream system.</p>
<p>You can configure the concurrency of your consumer Worker in two ways:</p>
<ol>
<li>Set concurrency settings in the Cloudflare dashboard</li>
<li>Set concurrency settings via the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a></li>
</ol>
<h3 id="set-concurrency-settings-in-the-cloudflare-dashboard">Set concurrency settings in the Cloudflare dashboard</h3>
<p>To configure the concurrency settings for your consumer Worker from the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Queues</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your queue &gt; <strong>Settings</strong>.</li>
<li>Select <strong>Edit Consumer</strong> under Consumer details.</li>
<li>Set <strong>Maximum consumer invocations</strong> to a value between <code>1</code> and <code>250</code>. This value represents the maximum number of concurrent consumer invocations available to your queue.</li>
</ol>
<p>To remove a fixed maximum value, select <strong>auto (recommended)</strong>.</p>
<p>Note that if you are writing messages to a queue faster than you can process them, messages may eventually reach the <a href="/queues/platform/limits/">maximum retention period</a> set for that queue. Individual messages that reach that limit will expire from the queue and be deleted.</p>
<h3 id="set-concurrency-settings-in-the-wrangler-configuration-file-workers-wrangler-configuration">Set concurrency settings in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11278.md")
</aside>
<p>To set a fixed maximum number of concurrent consumer invocations for a given queue, configure a <code>max_concurrency</code> in your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11281.md")
</div>
<p>To remove the limit, remove the <code>max_concurrency</code> setting from the <code>[[queues.consumers]]</code> configuration for a given queue and call <code>npx wrangler deploy</code> to push your configuration update.</p>
<pre><code>{/* Not yet available but will be very soon&#10;&#10;### wrangler CLI&#10;</code></pre>
<pre><code class="language-sh">&#35; where `N` is a positive integer between 1 and 250&#10;wrangler queues consumer update &lt;script-name&gt; --max-concurrency=N&#10;</code></pre>
<pre><code>To remove the limit and allow Queues to scale your consumer to the maximum number of invocations, call `consumer update` without any flags:&#10;</code></pre>
<pre><code class="language-sh">&#35; Call update without passing a flag to allow concurrency to scale to the maximum&#10;wrangler queues consumer update &lt;script-name&gt;&#10;</code></pre>
<h2 id="billing">Billing</h2>
<p>When multiple consumer Workers are invoked, each Worker invocation incurs <a href="/workers/platform/pricing/#workers">CPU time costs</a>.</p>
<ul>
<li>If you intend to process all messages written to a queue, <em>the effective overall cost is the same</em>, even with concurrency enabled.</li>
<li>Enabling concurrency simply brings those costs forward, and can help prevent messages from reaching the <a href="/queues/platform/limits/">message retention limit</a>.</li>
</ul>
<p>Billing for consumers follows the <a href="/workers/platform/pricing/#example-pricing">Workers standard usage model</a> meaning a developer is billed for the request and for CPU time used in the request.</p>
<h3 id="example-1">Example</h3>
<p>A consumer Worker that takes 2 seconds to process a batch of messages will incur the same overall costs to process 50 million (50,000,000) messages, whether it does so concurrently (faster) or individually (slower).</p>
