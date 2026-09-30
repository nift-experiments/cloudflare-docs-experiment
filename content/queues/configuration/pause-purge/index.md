<h2 id="pause-delivery">Pause Delivery</h2>
<p>You can pause delivery of messages from your queue to any connected consumers. Pausing a queue is useful when managing downtime (for example, if your consumer Worker is unhealthy) without losing any messages.</p>
<p>Queues continue to receive and store messages even while delivery is paused. Messages in a paused queue are still subject to expiry, if the messages become older than the queue message retention period.</p>
<p>Pausing affects both <a href="/queues/reference/how-queues-works#consumers">push-based consumer Workers</a> and <a href="/queues/configuration/pull-consumers">pull based consumers</a>.</p>
<h3 id="pause-and-resume-delivery-using-wrangler">Pause and resume delivery using Wrangler</h3>
<p>The following command will pause message delivery from your queue:</p>
<pre><code class="language-sh">$ npx wrangler queues pause-delivery &lt;QUEUE-NAME&gt;&#10;</code></pre>
<ul>
<li><code>queue-name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name of the queue for which delivery should be paused.</li>
</ul>
</li>
</ul>
<p>The following command will resume message delivery:</p>
<pre><code class="language-sh">$ npx wrangler queues resume-delivery &lt;QUEUE-NAME&gt;&#10;</code></pre>
<ul>
<li><code>queue-name</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The name of the queue for which delivery should be resumed.</li>
</ul>
</li>
</ul>
<h3 id="what-happens-to-http-pull-consumers-with-a-paused-queue">What happens to HTTP Pull consumers with a paused queue?</h3>
When a queue is paused, messages cannot be pulled by an [HTTP pull based consumer](/queues/configuration/pull-consumers). Requests to pull messages will receive a `409` response, along with an error message stating `queue_delivery_paused`.
<h2 id="purge-queue">Purge queue</h2>
Purging a queue permanently deletes any messages currently stored in the Queue. Purging is useful while developing a new application, especially to clear out any test data. It can also be useful in production to handle scenarios when a batch of bad messages have been sent to a Queue.
<p>Note that any in flight messages, which are currently being processed by consumers, might still be processed. Messages sent to a queue during a purge operation might not be purged. Any delayed messages will also be deleted from the queue.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11262.md")
</aside>
<h3 id="purge-queue-using-wrangler">Purge queue using Wrangler</h3>
The following command will purge messages from your queue. You will be prompted to enter the queue name to confirm the operation.
<pre><code class="language-sh">$ npx wrangler queues purge &lt;QUEUE-NAME&gt;&#10;<p>This operation will permanently delete all the messages in Queue &lt;QUEUE-NAME&gt;. Type &lt;QUEUE-NAME&gt; to proceed.&#10;</code></pre></p>
<h3 id="does-purging-a-queue-affect-my-bill">Does purging a Queue affect my bill?</h3>
Purging a queue counts as a single billable operation, regardless of how many messages are deleted. For example, if you purge a queue which has 100 messages, all 100 messages will be permanently deleted, and you will be billed for 1 billable operation. Refer to the [pricing](/queues/platform/pricing) page for more information about how Queues is billed.
