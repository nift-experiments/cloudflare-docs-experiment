<p>Cloudflare Queues is integrated with <a href="/workers">Cloudflare Workers</a>. To send and receive messages, you must use a Worker.</p>
<p>A Worker that can send messages to a Queue is a producer Worker, while a Worker that can receive messages from a Queue is a consumer Worker. It is possible for the same Worker to be a producer and consumer, if desired.</p>
<p>In the future, we expect to support other APIs, such as HTTP endpoints to send or receive messages. To report bugs or request features, go to the <a href="https://community.cloudflare.com/c/developers/workers/40">Cloudflare Community Forums</a>. To give feedback, go to the <a href="https://discord.cloudflare.com"><code>#queues</code></a> Discord channel.</p>
<h2 id="producer">Producer</h2>
<p>These APIs allow a producer Worker to send messages to a Queue.</p>
<p>An example of writing a single message to a Queue:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11270.md")
</div></div>
<p>The Queues API also supports writing multiple messages at once:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11273.md")
</div></div>
<h3 id="queue"><code>Queue</code></h3>
<p>A binding that allows a producer to send messages to a Queue.</p>
<pre><code class="language-ts">interface Queue&lt;Body = unknown&gt; {&#10;  send(body: Body, options?: QueueSendOptions): Promise&lt;QueueSendResult&gt;;&#10;  sendBatch(messages: Iterable&lt;MessageSendRequest&lt;Body&gt;&gt;, options?: QueueSendBatchOptions): Promise&lt;QueueSendResult&gt;;&#10;  metrics(): Promise&lt;QueueMetrics&gt;;&#10;}&#10;</code></pre>
<ul>
<li>
<p><code>send(body: unknown, options?: {contentType?: QueuesContentType })</code> <span class="nb-type">Promise&lt;QueueSendResult&gt;</span></p>
<ul>
<li>Sends a message to the Queue. The body can be any type supported by the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm#supported_types">structured clone algorithm</a>, as long as its size is less than 128 KB.</li>
<li>When the promise resolves, the message is confirmed to be written to disk.</li>
<li>Returns a <a href="#queuesendresult">QueueSendResult</a> containing realtime metrics about the queue.</li>
</ul>
</li>
<li>
<p><code>sendBatch(messages: Iterable&lt;MessageSendRequest&lt;unknown&gt;&gt;, options?: QueueSendBatchOptions)</code> <span class="nb-type">Promise&lt;QueueSendBatchResult&gt;</span></p>
<ul>
<li>Sends a batch of messages to the Queue. Each item in the provided <a href="https://www.typescriptlang.org/docs/handbook/iterators-and-generators.html">Iterable</a> must be supported by the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm#supported_types">structured clone algorithm</a>. A batch can contain up to 100 messages, though items are limited to 128 KB each, and the total size of the array cannot exceed 256 KB.</li>
<li>The optional <code>options</code> parameter can be used to apply settings (such as <code>delaySeconds</code>) to all messages in the batch. See <a href="#queuesendbatchoptions">QueueSendBatchOptions</a>.</li>
<li>When the promise resolves, the messages are confirmed to be written to disk.</li>
</ul>
</li>
<li>
<p><code>metrics()</code> <span class="nb-type">Promise&lt;QueueMetrics&gt;</span></p>
<ul>
<li>Returns realtime <a href="#queuemetrics">QueueMetrics</a> for the queue.</li>
</ul>
</li>
</ul>
<h3 id="messagesendrequest"><code>MessageSendRequest</code></h3>
<p>A wrapper type used for sending message batches.</p>
<pre><code class="language-ts">interface MessageSendRequest&lt;Body = unknown&gt; {&#10;  body: Body;&#10;  contentType?: QueueContentType;&#10;  delaySeconds?: number;&#10;}&#10;</code></pre>
<ul>
<li>
<p><code>body</code> <span class="nb-type">unknown</span></p>
<ul>
<li>The body of the message.</li>
<li>The body can be any type supported by the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm#supported_types">structured clone algorithm</a>, as long as its size is less than 128 KB.</li>
</ul>
</li>
<li>
<p><code>contentType</code> <span class="nb-type">QueueContentType</span></p>
<ul>
<li>The explicit content type of a message so it can be previewed correctly with the <a href="/queues/examples/list-messages-from-dash/">List messages from the dashboard</a> feature. Optional argument.</li>
<li>See <a href="#queuescontenttype">QueuesContentType</a> for possible values.</li>
</ul>
</li>
<li>
<p><code>delaySeconds</code> <span class="nb-type">number</span></p>
<ul>
<li>The number of seconds to <a href="/queues/configuration/batching-retries/">delay a message</a> for within the queue, before it can be delivered to a consumer.</li>
<li>Must be an integer between 0 and 86400 (24 hours).</li>
</ul>
</li>
</ul>
<h3 id="queuesendoptions"><code>QueueSendOptions</code></h3>
<p>Optional configuration that applies when sending a message to a queue.</p>
<ul>
<li>
<p><code>contentType</code> <span class="nb-type">QueuesContentType</span></p>
<ul>
<li>The explicit content type of a message so it can be previewed correctly with the <a href="/queues/examples/list-messages-from-dash/">List messages from the dashboard</a> feature. Optional argument.</li>
<li>As of now, this option is for internal use. In the future, <code>contentType</code> will be used by alternative consumer types to explicitly mark messages as serialized so they can be consumed in the desired type.</li>
<li>See <a href="#queuescontenttype">QueuesContentType</a> for possible values.</li>
</ul>
</li>
<li>
<p><code>delaySeconds</code> <span class="nb-type">number</span></p>
<ul>
<li>The number of seconds to <a href="/queues/configuration/batching-retries/">delay a message</a> for within the queue, before it can be delivered to a consumer.</li>
<li>Must be an integer between 0 and 86400 (24 hours). Setting this value to zero will explicitly prevent the message from being delayed, even if there is a global (default) delay at the queue level.</li>
</ul>
</li>
</ul>
<h3 id="queuesendbatchoptions"><code>QueueSendBatchOptions</code></h3>
<p>Optional configuration that applies when sending a batch of messages to a queue.</p>
<ul>
<li>
<p><code>delaySeconds</code> <span class="nb-type">number</span></p>
<ul>
<li>The number of seconds to <a href="/queues/configuration/batching-retries/">delay messages</a> for within the queue, before it can be delivered to a consumer.</li>
<li>Must be a positive integer.</li>
</ul>
</li>
</ul>
<h3 id="queuescontenttype"><code>QueuesContentType</code></h3>
<p>A union type containing valid message content types.</p>
<pre><code class="language-ts">// Default: json&#10;type QueuesContentType = &quot;text&quot; | &quot;bytes&quot; | &quot;json&quot; | &quot;v8&quot;;&#10;</code></pre>
<ul>
<li>Use <code>&quot;json&quot;</code> to send a JavaScript object that can be JSON-serialized. This content type can be previewed from the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>. The <code>json</code> content type is the default.</li>
<li>Use <code>&quot;text&quot;</code> to send a <code>String</code>. This content type can be previewed with the <a href="/queues/examples/list-messages-from-dash/">List messages from the dashboard</a> feature.</li>
<li>Use <code>&quot;bytes&quot;</code> to send an <code>ArrayBuffer</code>. This content type cannot be previewed from the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and will display as Base64-encoded.</li>
<li>Use <code>&quot;v8&quot;</code> to send a JavaScript object that cannot be JSON-serialized but is supported by <a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm#supported_types">structured clone</a> (for example <code>Date</code> and <code>Map</code>). This content type cannot be previewed from the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and will display as Base64-encoded.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11267.md")
</aside>
<p>If you specify an invalid content type, or if your specified content type does not match the message content's type, the send operation will fail with an error.</p>
<h3 id="queuesendresult"><code>QueueSendResult</code></h3>
<p>The result of a successful send operation.</p>
<pre><code class="language-ts">interface QueueSendResult {&#10;	metadata: {&#10;		metrics: QueueMetrics;&#10;	};&#10;}&#10;</code></pre>
<ul>
<li>
<p><code>metadata</code> <span class="nb-type">object</span></p>
<ul>
<li>Contains metadata about the queue after the send operation.</li>
</ul>
</li>
<li>
<p><code>metadata.metrics</code> <span class="nb-type">QueueMetrics</span></p>
<ul>
<li>Realtime metrics for the queue. See <a href="#queuemetrics">QueueMetrics</a>.</li>
</ul>
</li>
</ul>
<h3 id="queuemetrics"><code>QueueMetrics</code></h3>
<p>Realtime metrics for a queue.</p>
<pre><code class="language-ts">interface QueueMetrics {&#10;	backlogCount: number;&#10;	backlogBytes: number;&#10;	oldestMessageTimestamp: number;&#10;}&#10;</code></pre>
<ul>
<li>
<p><code>backlogCount</code> <span class="nb-type">number</span></p>
<ul>
<li>The number of messages currently in the queue.</li>
</ul>
</li>
<li>
<p><code>backlogBytes</code> <span class="nb-type">number</span></p>
<ul>
<li>The total size of messages in the queue, in bytes.</li>
</ul>
</li>
<li>
<p><code>oldestMessageTimestamp</code> <span class="nb-type">number</span></p>
<ul>
<li>The timestamp (in milliseconds since epoch) of the oldest message in the queue.</li>
</ul>
</li>
</ul>
<h2 id="consumer">Consumer</h2>
<p>These APIs allow a consumer Worker to consume messages from a Queue.</p>
<p>To define a consumer Worker, add a <code>queue()</code> function to the default export of the Worker. This will allow it to receive messages from the Queue.</p>
<p>By default, all messages in the batch will be acknowledged as soon as all of the following conditions are met:</p>
<ol>
<li>The <code>queue()</code> function has returned.</li>
<li>If the <code>queue()</code> function returned a promise, the promise has resolved.</li>
<li>Any promises passed to <code>waitUntil()</code> have resolved.</li>
</ol>
<p>If the <code>queue()</code> function throws, or the promise returned by it or any of the promises passed to <code>waitUntil()</code> were rejected, then the entire batch will be considered a failure and will be retried according to the consumer's retry settings.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11266.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11276.md")
</div></div>
<p>The <code>env</code> and <code>ctx</code> fields are as <a href="/workers/reference/migrate-to-module-workers/">documented in the Workers documentation</a>.</p>
<h3 id="typescript-message-types">TypeScript message types</h3>
<p>You can type queue messages with <code>Queue&lt;T&gt;</code> on the producer and <code>ExportedHandler&lt;Env, T&gt;</code> on the consumer.</p>
<pre><code class="language-ts">type MyMessage = {&#10;  id: string;&#10;};&#10;&#10;interface Env {&#10;  MY_QUEUE: Queue&lt;MyMessage&gt;;&#10;}&#10;&#10;export default {&#10;  async queue(batch) {&#10;    for (const message of batch.messages) {&#10;      console.log(message.body.id);&#10;    }&#10;  },&#10;} satisfies ExportedHandler&lt;Env, MyMessage&gt;;&#10;</code></pre>
<p>For primitive messages, use <code>Queue&lt;number&gt;</code> or <code>satisfies ExportedHandler&lt;Env, number&gt;</code>. If you do not specify a type, <code>message.body</code> is <code>unknown</code>.</p>
<p>Or alternatively, a queue consumer can be written using the (deprecated) service worker syntax:</p>
<pre><code class="language-js">addEventListener(&#x27;queue&#x27;, (event) =&gt; {&#10;	event.waitUntil(handleMessages(event));&#10;});&#10;</code></pre>
<p>In service worker syntax, <code>event</code> provides the same fields and methods as <code>MessageBatch</code>, as defined below, in addition to <a href="https://developer.mozilla.org/en-US/docs/Web/API/ExtendableEvent/waitUntil"><code>waitUntil()</code></a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11265.md")
</aside>
<h3 id="messagebatch"><code>MessageBatch</code></h3>
<p>A batch of messages that are sent to a consumer Worker.</p>
<pre><code class="language-ts">interface MessageBatch&lt;Body = unknown&gt; {&#10;  readonly queue: string;&#10;  readonly messages: readonly Message&lt;Body&gt;[];&#10;  ackAll(): void;&#10;  retryAll(options?: QueueRetryOptions): void;&#10;}&#10;</code></pre>
<ul>
<li>
<p><code>queue</code> <span class="nb-type">string</span></p>
<ul>
<li>The name of the Queue that belongs to this batch.</li>
</ul>
</li>
<li>
<p><code>messages</code> <span class="nb-type">Message[]</span></p>
<ul>
<li>An array of messages in the batch. Ordering of messages is best effort -- not guaranteed to be exactly the same as the order in which they were published.</li>
</ul>
</li>
<li>
<p><code>ackAll()</code> <span class="nb-type">void</span></p>
<ul>
<li>Marks every message as successfully delivered, regardless of whether your <code>queue()</code> consumer handler returns successfully or not.</li>
</ul>
</li>
<li>
<p><code>retryAll(options?: QueueRetryOptions)</code> <span class="nb-type">void</span></p>
<ul>
<li>Marks every message to be retried in the next batch.</li>
<li>Supports an optional <code>options</code> object.</li>
</ul>
</li>
</ul>
<h3 id="message"><code>Message</code></h3>
<p>A message that is sent to a consumer Worker.</p>
<pre><code class="language-ts">interface Message&lt;Body = unknown&gt; {&#10;  readonly id: string;&#10;  readonly timestamp: Date;&#10;  readonly body: Body;&#10;	readonly attempts: number;&#10;  ack(): void;&#10;  retry(options?: QueueRetryOptions): void;&#10;}&#10;</code></pre>
<ul>
<li>
<p><code>id</code> <span class="nb-type">string</span></p>
<ul>
<li>A unique, system-generated ID for the message.</li>
</ul>
</li>
<li>
<p><code>timestamp</code> <span class="nb-type">Date</span></p>
<ul>
<li>A timestamp when the message was sent.</li>
</ul>
</li>
<li>
<p><code>body</code> <span class="nb-type">unknown</span></p>
<ul>
<li>The body of the message.</li>
<li>The body can be any type supported by the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm#supported_types">structured clone algorithm</a>, as long as its size is less than 128 KB.</li>
</ul>
</li>
<li>
<p><code>attempts</code> <span class="nb-type">number</span></p>
<ul>
<li>The number of times the consumer has attempted to process this message. Starts at 1.</li>
</ul>
</li>
<li>
<p><code>ack()</code> <span class="nb-type">void</span></p>
<ul>
<li>Marks a message as successfully delivered, regardless of whether your <code>queue()</code> consumer handler returns successfully or not.</li>
</ul>
</li>
<li>
<p><code>retry(options?: QueueRetryOptions)</code> <span class="nb-type">void</span></p>
<ul>
<li>Marks a message to be retried in the next batch.</li>
<li>Supports an optional <code>options</code> object.</li>
</ul>
</li>
</ul>
<h3 id="queueretryoptions"><code>QueueRetryOptions</code></h3>
<p>Optional configuration when marking a message or a batch of messages for retry.</p>
<pre><code class="language-ts">interface QueueRetryOptions {&#10;  delaySeconds?: number;&#10;}&#10;</code></pre>
<ul>
<li>
<p><code>delaySeconds</code> <span class="nb-type">number</span></p>
<ul>
<li>The number of seconds to <a href="/queues/configuration/batching-retries/">delay a message</a> for within the queue, before it can be delivered to a consumer.</li>
<li>Must be a positive integer.</li>
</ul>
</li>
<li>
<p>When the promise resolves, the messages are written to disk.</p>
<ul>
<li>Returns a <a href="#queuesendresult">QueueSendResult</a> containing realtime metrics about the queue.</li>
</ul>
</li>
</ul>
