<p>Cloudflare Queues can be configured using <a href="/workers/wrangler/install-and-update/">Wrangler</a>, the command-line interface for Cloudflare's Developer Platform, which includes <a href="/workers/">Workers</a>, <a href="/r2/">R2</a>, and other developer products.</p>
<p>Each Producer and Consumer Worker has a <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> that specifies environment variables, triggers, and resources, such as a queue. To enable Worker-to-resource communication, you must set up a <a href="/workers/runtime-apis/bindings/">binding</a> in your Worker project's Wrangler file.</p>
<p>Use the options below to configure your queue.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11282.md")
</aside>
<h2 id="queue-configuration">Queue configuration</h2>
The following queue level settings can be configured using Wrangler:
<pre><code class="language-sh">npx wrangler queues update &lt;QUEUE-NAME&gt; --delivery-delay-secs 60 --message-retention-period-secs 3000&#10;</code></pre>
<ul>
<li>
<p><code>--delivery-delay-secs</code> <span class="nb-type">number</span> <span class="nb-type">optional</span></p>
<ul>
<li>How long a published message is delayed for, before it is delivered to consumers.</li>
<li>Must be between 0 and 86400 (24 hours).</li>
<li>Defaults to 0.</li>
</ul>
</li>
<li>
<p><code>--message-retention-period-secs</code>  <span class="nb-type">number</span> <span class="nb-type">optional</span></p>
<ul>
<li>How long messages are retained on the Queue.</li>
<li>Defaults to 345600 (4 days).</li>
<li>Must be between 60 and 1209600 (14 days)</li>
</ul>
</li>
</ul>
<h2 id="producer-worker-configuration">Producer Worker configuration</h2>
<p>A producer is a <a href="/workers/">Cloudflare Worker</a> that writes to one or more queues. A producer can accept messages over HTTP, asynchronously write messages when handling requests, and/or write to a queue from within a <a href="/durable-objects/">Durable Object</a>. Any Worker can write to a queue.</p>
<p>To produce to a queue, set up a binding in your Wrangler file. These options should be used when a Worker wants to send messages to a queue.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11283.md")
</div>
<ul>
<li>
<p><code>queue</code> <span class="nb-type">string</span></p>
<ul>
<li>The name of the queue.</li>
</ul>
</li>
<li>
<p><code>binding</code> <span class="nb-type">string</span></p>
<ul>
<li>The name of the binding, which is a JavaScript variable.</li>
</ul>
</li>
</ul>
<h2 id="consumer-worker-configuration">Consumer Worker Configuration</h2>
<p>To consume messages from one or more queues, set up a binding in your Wrangler file. These options should be used when a Worker wants to receive messages from a queue.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11284.md")
</div>
<p>Refer to <a href="/queues/platform/limits">Limits</a> to review the maximum values for each of these options.</p>
<ul>
<li>
<p><code>queue</code> <span class="nb-type">string</span></p>
<ul>
<li>The name of the queue.</li>
</ul>
</li>
<li>
<p><code>max_batch_size</code> <span class="nb-type">number</span> <span class="nb-type">optional</span></p>
<ul>
<li>The maximum number of messages allowed in each batch.</li>
<li>Defaults to <code>10</code> messages.</li>
</ul>
</li>
<li>
<p><code>max_batch_timeout</code> <span class="nb-type">number</span> <span class="nb-type">optional</span></p>
<ul>
<li>The maximum number of seconds to wait until a batch is full.</li>
<li>Defaults to <code>5</code> seconds.</li>
</ul>
</li>
<li>
<p><code>max_retries</code> <span class="nb-type">number</span> <span class="nb-type">optional</span></p>
<ul>
<li>The maximum number of retries for a message, if it fails or <a href="/queues/configuration/javascript-apis/#messagebatch"><code>retryAll()</code></a> is invoked.</li>
<li>Defaults to <code>3</code> retries.</li>
</ul>
</li>
<li>
<p><code>dead_letter_queue</code> <span class="nb-type">string</span> <span class="nb-type">optional</span></p>
<ul>
<li>The name of another queue to send a message if it fails processing at least <code>max_retries</code> times.</li>
<li>If a <code>dead_letter_queue</code> is not defined, messages that repeatedly fail processing will eventually be discarded.</li>
<li>If there is no queue with the specified name, it will be created automatically.</li>
</ul>
</li>
<li>
<p><code>max_concurrency</code> <span class="nb-type">number</span> <span class="nb-type">optional</span></p>
<ul>
<li>The maximum number of concurrent consumers allowed to run at once. Leaving this unset will mean that the number of invocations will scale to the <a href="/queues/platform/limits/">currently supported maximum</a>.</li>
<li>Refer to <a href="/queues/configuration/consumer-concurrency/">Consumer concurrency</a> for more information on how consumers autoscale, particularly when messages are retried.</li>
</ul>
</li>
</ul>
<h2 id="pull-based">Pull-based</h2>
<p>A queue can have a HTTP-based consumer that pulls from the queue. This consumer can be any HTTP-speaking service that can communicate over the Internet. Review <a href="/queues/configuration/pull-consumers/">Pull consumers</a> to learn how to configure a pull-based consumer.</p>
