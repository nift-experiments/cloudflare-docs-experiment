<p>Queues expose metrics which allow you to measure the queue backlog, consumer concurrency, and message operations.</p>
<p>The metrics displayed in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> are queried from Cloudflare’s <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. You can access the metrics <a href="#query-via-the-graphql-api">programmatically</a> via GraphQL or HTTP client.</p>
<h2 id="metrics">Metrics</h2>
<h3 id="backlog">Backlog</h3>
<p>Queues export the below metrics within the <code>queuesBacklogAdaptiveGroups</code> dataset.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>GraphQL Field Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Backlog bytes</td>
<td><code>bytes</code></td>
<td>Average size of the backlog, in bytes</td>
</tr>
<tr>
<td>Backlog messages</td>
<td><code>messages</code></td>
<td>Average size of the backlog, in number of messages</td>
</tr>
</tbody>
</table>
<p>The <code>queuesBacklogAdaptiveGroups</code> dataset provides the following dimensions for filtering and grouping queries:</p>
<ul>
<li><code>queueID</code> - ID of the queue</li>
<li><code>datetime</code> - Timestamp for when the message was sent</li>
<li><code>date</code> - Timestamp for when the message was sent, truncated to the start of a day</li>
<li><code>datetimeHour</code> - Timestamp for when the message was sent, truncated to the start of an hour</li>
<li><code>datetimeMinute</code> - Timestamp for when the message was sent, truncated to the start of a minute</li>
</ul>
<h3 id="consumer-concurrency">Consumer concurrency</h3>
<p>Queues export the below metrics within the <code>queueConsumerMetricsAdaptiveGroups</code> dataset.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>GraphQL Field Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Avg. Consumer Concurrency</td>
<td><code>concurrency</code></td>
<td>Average number of concurrent consumers over the period</td>
</tr>
</tbody>
</table>
<p>The <code>queueConsumerMetricsAdaptiveGroups</code> dataset provides the following dimensions for filtering and grouping queries:</p>
<ul>
<li><code>queueID</code> - ID of the queue</li>
<li><code>datetime</code> - Timestamp for the consumer metrics</li>
<li><code>date</code> - Timestamp for the consumer metrics, truncated to the start of a day</li>
<li><code>datetimeHour</code> - Timestamp for the consumer metrics, truncated to the start of an hour</li>
<li><code>datetimeMinute</code> - Timestamp for the consumer metrics, truncated to the start of a minute</li>
</ul>
<h3 id="message-operations">Message operations</h3>
<p>Queues export the below metrics within the <code>queueMessageOperationsAdaptiveGroups</code> dataset.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>GraphQL Field Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Total billable operations</td>
<td><code>billableOperations</code></td>
<td>Sum of billable operations (writes, reads, and deletes) over the time period</td>
</tr>
<tr>
<td>Total Bytes</td>
<td><code>bytes</code></td>
<td>Sum of bytes read, written, and deleted from the queue</td>
</tr>
<tr>
<td>Lag</td>
<td><code>lagTime</code></td>
<td>Average lag time in milliseconds between when the message was written and the operation to consume the message.</td>
</tr>
<tr>
<td>Retries</td>
<td><code>retryCount</code></td>
<td>Average number of retries per message</td>
</tr>
<tr>
<td>Message Size</td>
<td><code>messageSize</code></td>
<td>Maximum message size over the specified period</td>
</tr>
</tbody>
</table>
<p>The <code>queueMessageOperationsAdaptiveGroups</code> dataset provides the following dimensions for filtering and grouping queries:</p>
<ul>
<li><code>queueID</code> - ID of the queue</li>
<li><code>actionType</code> - The type of message operation. Can be <code>WriteMessage</code>, <code>ReadMessage</code> or <code>DeleteMessage</code></li>
<li><code>consumerType</code> - The queue consumer type. Can be <code>worker</code> or <code>http</code>. Only applicable for <code>ReadMessage</code> and <code>DeleteMessage</code> action types</li>
<li><code>outcome</code> - The outcome of the message operation. Only applicable for <code>DeleteMessage</code> action types. Can be <code>success</code>, <code>dlq</code> or <code>fail</code>.</li>
<li><code>datetime</code> - Timestamp for the message operation</li>
<li><code>date</code> - Timestamp for the message operation, truncated to the start of a day</li>
<li><code>datetimeHour</code> - Timestamp for the message operation, truncated to the start of an hour</li>
<li><code>datetimeMinute</code> - Timestamp for the message operation, truncated to the start of a minute</li>
</ul>
<h3 id="realtime-backlog">Realtime backlog</h3>
<p>You can access realtime backlog metrics via the <a href="/api/resources/queues/">Queues REST API</a> and <a href="/queues/configuration/javascript-apis/">JavaScript API</a>. These metrics provide point-in-time values rather than aggregated data.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Field Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Backlog count</td>
<td><code>backlog_count</code></td>
<td>Number of messages currently in the queue</td>
</tr>
<tr>
<td>Backlog bytes</td>
<td><code>backlog_bytes</code></td>
<td>Total size of messages in the queue, in bytes</td>
</tr>
<tr>
<td>Oldest message timestamp</td>
<td><code>oldest_message_timestamp_ms</code></td>
<td>Timestamp (in milliseconds) of the oldest message in the queue</td>
</tr>
</tbody>
</table>
<p>To retrieve these metrics via the REST API, use the metrics endpoint (<code>/accounts/{account_id}/queues/{queue_id}/metrics</code>).</p>
<p>These fields are also included in <code>metadata.metrics</code> when calling <code>send()</code>, <code>sendBatch()</code>, or <code>metrics()</code> via the JavaScript API.</p>
<h2 id="example-graphql-queries">Example GraphQL Queries</h2>
<h3 id="get-average-queue-backlog-over-time-period">Get average queue backlog over time period</h3>
<pre><code class="language-graphql">query QueueBacklog(&#10;	$accountTag: string!&#10;	$queueId: string!&#10;	$datetimeStart: Time!&#10;	$datetimeEnd: Time!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			queueBacklogAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					queueId: $queueId&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;			) {&#10;				avg {&#10;					messages&#10;					bytes&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="get-average-consumer-concurrency-by-hour">Get average consumer concurrency by hour</h3>
<pre><code class="language-graphql">query QueueConcurrencyByHour(&#10;	$accountTag: string!&#10;	$queueId: string!&#10;	$datetimeStart: Time!&#10;	$datetimeEnd: Time!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			queueConsumerMetricsAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					queueId: $queueId&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;				orderBy: [datetimeHour_DESC]&#10;			) {&#10;				avg {&#10;					concurrency&#10;				}&#10;				dimensions {&#10;					datetimeHour&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="get-message-operations-by-minute">Get message operations by minute</h3>
<pre><code class="language-graphql">query QueueMessageOperationsByMinute(&#10;	$accountTag: string!&#10;	$queueId: string!&#10;	$datetimeStart: Date!&#10;	$datetimeEnd: Date!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			queueMessageOperationsAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					queueId: $queueId&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;				orderBy: [datetimeMinute_DESC]&#10;			) {&#10;				count&#10;				sum {&#10;					bytes&#10;				}&#10;				dimensions {&#10;					datetimeMinute&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
