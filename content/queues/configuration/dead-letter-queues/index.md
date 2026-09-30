<p>A Dead Letter Queue (DLQ) is a common concept in a messaging system, and represents where messages are sent when a delivery failure occurs with a consumer after <code>max_retries</code> is reached. A Dead Letter Queue is like any other queue, and can be produced to and consumed from independently.</p>
<p>With Cloudflare Queues, a Dead Letter Queue is defined within your <a href="/queues/configuration/configure-queues/">consumer configuration</a>. Messages are delivered to the DLQ when they reach the configured retry limit for the consumer. Without a DLQ configured, messages that reach the retry limit are deleted permanently.</p>
<p>For example, the following consumer configuration would send messages to our DLQ named <code>&quot;my-other-queue&quot;</code> after retrying delivery (by default, 3 times):</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11277.md")
</div>
<p>You can also configure a DLQ when creating a consumer from the command-line using <code>wrangler</code>:</p>
<pre><code class="language-sh">wrangler queues consumer add $QUEUE_NAME $SCRIPT_NAME --dead-letter-queue=$NAME_OF_OTHER_QUEUE&#10;</code></pre>
<p>To process messages placed on your DLQ, you need to <a href="/queues/configuration/configure-queues/">configure a consumer</a> for that queue as you would with any other queue.</p>
<p>Messages delivered to a DLQ without an active consumer will persist for four (4) days before being deleted from the queue.</p>
