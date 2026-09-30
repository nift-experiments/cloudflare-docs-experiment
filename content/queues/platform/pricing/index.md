<p>Cloudflare Queues charges for the total number of operations against each of your queues during a given month.</p>
<ul>
<li>An operation is counted for each 64 KB of data that is written, read, or deleted.</li>
<li>Messages larger than 64 KB are charged as if they were multiple messages: for example, a 65 KB message and a 127 KB message would both incur two operation charges when written, read, or deleted.</li>
<li>A KB is defined as 1,000 bytes, and each message includes approximately 100 bytes of internal metadata.</li>
<li>Operations are per message, not per batch. A batch of 10 messages (the default batch size), if processed, would incur 10x write, 10x read, and 10x delete operations: one for each message in the batch.</li>
<li>There are no data transfer (egress) or throughput (bandwidth) charges.</li>
</ul>
<table>
<thead>
<tr>
<th></th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Standard operations</td>
<td>10,000 operations/day included</td>
<td>1,000,000 operations/month included + $0.40/million operations</td>
</tr>
<tr>
<td>Message retention</td>
<td>24 hours (non-configurable)</td>
<td>4 days default, configurable up to 14 days</td>
</tr>
</tbody>
</table>
<p>In most cases, it takes 3 operations to deliver a message: 1 write, 1 read, and 1 delete. Therefore, you can use the following formula to estimate your monthly bill:</p>
<pre><code class="language-txt">((Number of Messages * 3) - 1,000,000) / 1,000,000  * $0.40&#10;</code></pre>
<p>Additionally:</p>
<ul>
<li>Each retry incurs a read operation. A batch of 10 messages that is retried would incur 10 operations for each retry.</li>
<li>Messages that reach the maximum retries and that are written to a <a href="/queues/configuration/batching-retries/">Dead Letter Queue</a> incur a write operation for each 64 KB chunk. A message that was retried 3 times (the default), fails delivery on the fourth time and is written to a Dead Letter Queue would incur five (5) read operations.</li>
<li>Messages that are written to a queue, but that reach the maximum persistence duration (or &quot;expire&quot;) before they are read, incur only a write and delete operation per 64 KB chunk.</li>
</ul>
<h2 id="examples">Examples</h2>
<p>If an application writes, reads and deletes (consumes) one million messages a day (in a 30 day month), and each message is less than 64 KB in size, the estimated bill for the month would be:</p>
<table>
<thead>
<tr>
<th></th>
<th>Total Usage</th>
<th>Free Usage</th>
<th>Billed Usage</th>
<th>Price</th>
</tr>
</thead>
<tbody>
<tr>
<td>Standard operations</td>
<td>3 * 30 * 1,000,000</td>
<td>1,000,000</td>
<td>89,000,000</td>
<td>$35.60</td>
</tr>
<tr>
<td></td>
<td>(write, read, delete)</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>TOTAL</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$35.60</strong></td>
</tr>
</tbody>
</table>
<p>An application that writes, reads and deletes (consumes) 100 million ~127 KB messages (each message counts as two 64 KB chunks) per month would have an estimated bill resembling the following:</p>
<table>
<thead>
<tr>
<th></th>
<th>Total Usage</th>
<th>Free Usage</th>
<th>Billed Usage</th>
<th>Price</th>
</tr>
</thead>
<tbody>
<tr>
<td>Standard operations</td>
<td>2 * 3 * 100 * 1,000,000</td>
<td>1,000,000</td>
<td>599,000,000</td>
<td>$239.60</td>
</tr>
<tr>
<td></td>
<td>(2x ops for &gt; 64KB messages)</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>TOTAL</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$239.60</strong></td>
</tr>
</tbody>
</table>
