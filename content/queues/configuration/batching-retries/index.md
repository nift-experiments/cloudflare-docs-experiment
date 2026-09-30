<h2 id="batching">Batching</h2>
<p>When configuring a <a href="/queues/reference/how-queues-works#consumers">consumer Worker</a> for a queue, you can also define how messages are batched as they are delivered.</p>
<p>Batching can:</p>
<ol>
<li>Reduce the total number of times your consumer Worker needs to be invoked (which can reduce costs).</li>
<li>Allow you to batch messages when writing to an external API or service (reducing writes).</li>
<li>Disperse load over time, especially if your producer Workers are associated with user-facing activity.</li>
</ol>
<p>There are two ways to configure how messages are batched. You configure batching when connecting your consumer Worker to a queue.</p>
<ul>
<li><code>max_batch_size</code> - The maximum size of a batch delivered to a consumer (defaults to 10 messages).</li>
<li><code>max_batch_timeout</code> - the <em>maximum</em> amount of time the queue will wait before delivering a batch to a consumer (defaults to 5 seconds)</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="batch-size-configuration">Batch size configuration</h3>
@markup("md", "content/.markup/bodies/11289.md")
</aside>
<p>For example, a <code>max_batch_size = 30</code> and a <code>max_batch_timeout = 10</code> means that if 30 messages are written to the queue, the consumer will receive a batch of 30 messages. However, if it takes longer than 10 seconds for those 30 messages to be written to the queue, then the consumer will get a batch of messages that contains however many messages were on the queue at the time (somewhere between 1 and 29, in this case).</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="empty-queues">Empty queues</h3>
@markup("md", "content/.markup/bodies/11288.md")
</aside>
<p>When determining what size and timeout settings to configure, you will want to consider latency (how long can you wait to receive messages?), overall batch size (when writing to external systems), and cost (fewer-but-larger batches).</p>
<h3 id="batch-settings">Batch settings</h3>
<p>The following batch-level settings can be configured to adjust how Queues delivers batches to your configured consumer.</p>
<table-wrap>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Default</th>
<th>Minimum</th>
<th>Maximum</th>
</tr>
</thead>
<tbody>
<tr>
<td>Maximum Batch Size <code>max_batch_size</code></td>
<td>10 messages</td>
<td>1 message</td>
<td>100 messages</td>
</tr>
<tr>
<td>Maximum Batch Timeout <code>max_batch_timeout</code></td>
<td>5 seconds</td>
<td>0 seconds</td>
<td>60 seconds</td>
</tr>
</tbody>
</table>
</table-wrap>
<h2 id="explicit-acknowledgement-and-retries">Explicit acknowledgement and retries</h2>
<p>You can acknowledge individual messages within a batch by explicitly acknowledging each message as it is processed. Messages that are explicitly acknowledged will not be re-delivered, even if your queue consumer fails on a subsequent message and/or fails to return successfully when processing a batch.</p>
<ul>
<li>Each message can be acknowledged as you process it within a batch, and avoids the entire batch from being re-delivered if your consumer throws an error during batch processing.</li>
<li>Acknowledging individual messages is useful when you are calling external APIs, writing messages to a database, or otherwise performing non-idempotent (state changing) actions on individual messages.</li>
</ul>
<p>To explicitly acknowledge a message as delivered, call the <code>ack()</code> method on the message.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11292.md")
</div></div>
<p>You can also call <code>retry()</code> to explicitly force a message to be redelivered in a subsequent batch. This is referred to as &quot;negative acknowledgement&quot;. This can be particularly useful when you want to process the rest of the messages in that batch without throwing an error that would force the entire batch to be redelivered.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11295.md")
</div></div>
<p>You can also acknowledge or negatively acknowledge messages at a batch level with <code>ackAll()</code> and <code>retryAll()</code>. Calling <code>ackAll()</code> on the batch of messages (<code>MessageBatch</code>) delivered to your consumer Worker has the same behaviour as a consumer Worker that successfully returns (does not throw an error).</p>
<p>Note that calls to <code>ack()</code>, <code>retry()</code> and their <code>ackAll()</code> / <code>retryAll()</code> equivalents follow the below precedence rules:</p>
<ul>
<li>If you call <code>ack()</code> on a message, subsequent calls to <code>ack()</code> or <code>retry()</code> are silently ignored.</li>
<li>If you call <code>retry()</code> on a message and then call <code>ack()</code>: the <code>ack()</code> is ignored. The first method call wins in all cases.</li>
<li>If you call either <code>ack()</code> or <code>retry()</code> on a single message, and then either/any of <code>ackAll()</code> or <code>retryAll()</code> on the batch, the call on the single message takes precedence. That is, the batch-level call does not apply to that message (or messages, if multiple calls were made).</li>
</ul>
<h2 id="delivery-failure">Delivery failure</h2>
<p>When a message is failed to be delivered, the default behaviour is to retry delivery three times before marking the delivery as failed. You can set <code>max_retries</code> (defaults to 3) when configuring your consumer, but in most cases we recommend leaving this as the default.</p>
<p>Messages that reach the configured maximum retries will be deleted from the queue, or if a <a href="/queues/configuration/dead-letter-queues/">dead-letter queue</a> (DLQ) is configured, written to the DLQ instead.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11287.md")
</aside>
<p>When a single message within a batch fails to be delivered, the entire batch is retried, unless you have <a href="#explicit-acknowledgement-and-retries">explicitly acknowledged</a> a message (or messages) within that batch. For example, if a batch of 10 messages is delivered, but the 8th message fails to be delivered, all 10 messages will be retried and thus redelivered to your consumer in full.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="retried-messages-and-consumer-concurrency">Retried messages and consumer concurrency</h3>
@markup("md", "content/.markup/bodies/11286.md")
</aside>
<h2 id="delay-messages">Delay messages</h2>
<p>When publishing messages to a queue, or when <a href="#explicit-acknowledgement-and-retries">marking a message or batch for retry</a>, you can choose to delay messages from being processed for a period of time.</p>
<p>Delaying messages allows you to defer tasks until later, and/or respond to backpressure when consuming from a queue. For example, if an upstream API you are calling to returns a <code>HTTP 429: Too Many Requests</code>, you can delay messages to slow down how quickly you are consuming them before they are re-processed.</p>
<p>Messages can be delayed by up to 24 hours.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11285.md")
</aside>
<h3 id="delay-on-send">Delay on send</h3>
<p>To delay a message or batch of messages when sending to a queue, you can provide a <code>delaySeconds</code> parameter when sending a message.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11298.md")
</div></div>
<p>You can also configure a default, global delay on a per-queue basis by passing <code>--delivery-delay-secs</code> when creating a queue via the <code>wrangler</code> CLI:</p>
<pre><code class="language-sh">&#35; Delay all messages by 5 minutes as a default&#10;npx wrangler queues create $QUEUE-NAME --delivery-delay-secs=300&#10;</code></pre>
<h3 id="delay-on-retry">Delay on retry</h3>
<p>When <a href="/queues/reference/how-queues-works/#consumers">consuming messages from a queue</a>, you can choose to <a href="#explicit-acknowledgement-and-retries">explicitly mark messages to be retried</a>. Messages can be retried and delayed individually, or as an entire batch.</p>
<p>To delay an individual message within a batch:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11301.md")
</div></div>
<p>To delay a batch of messages:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11304.md")
</div></div>
<p>You can also choose to set a default retry delay to any messages that are retried due to either implicit failure or when calling <code>retry()</code> explicitly. This is set at the consumer level, and is supported in both push-based (Worker) and pull-based (HTTP) consumers.</p>
<p>Delays can be configured via the <code>wrangler</code> CLI:</p>
<pre><code class="language-sh">&#35; Push-based consumers&#10;&#35; Delay any messages that are retried by 60 seconds (1 minute) by default.&#10;npx wrangler@latest queues consumer worker add $QUEUE-NAME $WORKER_SCRIPT_NAME --retry-delay-secs=60&#10;&#10;&#35; Pull-based consumers&#10;&#35; Delay any messages that are retried by 60 seconds (1 minute) by default.&#10;npx wrangler@latest queues consumer http add $QUEUE-NAME --retry-delay-secs=60&#10;</code></pre>
<p>Delays can also be configured in the <a href="/workers/wrangler/configuration/#queues">Wrangler configuration file</a> with the <code>delivery_delay</code> setting for producers (when sending) and/or the <code>retry_delay</code> (when retrying) per-consumer:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11305.md")
</div>
<p>If you use both the <code>wrangler</code> CLI and the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> to change the settings associated with a queue or a queue consumer, the most recent configuration change will take effect.</p>
<p>Refer to the <a href="/api/resources/queues/subresources/consumers/methods/get/">Queues REST API documentation</a> to learn how to configure message delays and retry delays programmatically.</p>
<h3 id="message-delay-precedence">Message delay precedence</h3>
<p>Messages can be delayed by default at the queue level, or per-message (or batch).</p>
<ul>
<li>Per-message/batch delay settings take precedence over queue-level settings.</li>
<li>Setting <code>delaySeconds: 0</code> on a message when sending or retrying will ignore any queue-level delays and cause the message to be delivered in the next batch.</li>
<li>A message sent or retried with <code>delaySeconds: &lt;any positive integer&gt;</code> to a queue with a shorter default delay will still respect the message-level setting.</li>
</ul>
<h3 id="apply-a-backoff-algorithm">Apply a backoff algorithm</h3>
<p>You can apply a backoff algorithm to increasingly delay messages based on the current number of attempts to deliver the message.</p>
<p>Each message delivered to a consumer includes an <code>attempts</code> property that tracks the number of delivery attempts made.</p>
<p>For example, to generate an <a href="https://en.wikipedia.org/wiki/Exponential_backoff">exponential backoff</a> for a message, you can create a helper function that calculates this for you:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11308.md")
</div></div>
<p>In your consumer, you then pass the value of <code>msg.attempts</code> and your desired delay factor as the argument to <code>delaySeconds</code> when calling <code>retry()</code> on an individual message:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11311.md")
</div></div>
<h2 id="related">Related</h2>
<ul>
<li>Review the <a href="/queues/configuration/javascript-apis/">JavaScript API</a> documentation for Queues.</li>
<li>Learn more about <a href="/queues/reference/how-queues-works/">How Queues Works</a>.</li>
<li>Understand the <a href="/queues/observability/metrics/">metrics available</a> for your queues, including backlog and delayed message counts.</li>
</ul>
