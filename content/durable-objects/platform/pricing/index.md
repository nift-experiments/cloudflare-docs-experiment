<p>Durable Objects can incur two types of billing: compute and storage.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8159.md")
</aside>
<p>On Workers Free plan:</p>
<ul>
<li>If you exceed any one of the free tier limits, further operations of that type will fail with an error.</li>
<li>Daily free limits reset at 00:00 UTC.</li>
</ul>
<h2 id="compute-billing">Compute billing</h2>
<p>Durable Objects are billed for compute duration (wall-clock time) while the Durable Object is actively running or is idle in memory but unable to <a href="/durable-objects/concepts/durable-object-lifecycle/">hibernate</a>. Durable Objects that are idle and eligible for hibernation are not billed for duration, even before the runtime has hibernated them. Requests to a Durable Object keep it active or create the object if it was inactive.</p>
<p>For each metered dimension, billable usage is the amount consumed in excess of the included monthly allocation. This billable usage is rounded up to the next billable unit before the corresponding rate is applied. For example, 500,000 GB-s of billable compute duration is rounded up to 1,000,000 GB-s and billed accordingly.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free plan</th>
<th>Paid plan</th>
</tr>
</thead>
<tbody>
<tr>
<td>Requests</td>
<td>100,000 / day</td>
<td>1 million / month, + $0.15/million<br/> Includes HTTP requests, RPC sessions<sup>1</sup>, WebSocket messages<sup>2</sup>, and alarm invocations</td>
</tr>
<tr>
<td>Duration<sup>3</sup></td>
<td>13,000 GB-s / day</td>
<td>400,000 GB-s / month, + $12.50/million GB-s<sup>4,5</sup></td>
</tr>
</tbody>
</table>
<details class="nb-details" open><summary>Footnotes</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8160.md")
</div></details>
<h2 id="storage-billing">Storage billing</h2>
<p>The <a href="/durable-objects/api/sqlite-storage-api/">Durable Objects Storage API</a> is only accessible from within Durable Objects. Pricing depends on the storage backend of your Durable Objects.</p>
<ul>
<li><strong>SQLite-backed Durable Objects (recommended)</strong>: <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">SQLite storage backend</a> is recommended for all new Durable Object classes. Workers Free plan can only create and access SQLite-backed Durable Objects.</li>
<li><strong>Key-value backed Durable Objects</strong>: <a href="/durable-objects/reference/durable-object-class-migrations-legacy/#create-durable-object-class-with-key-value-storage">Key-value storage backend</a> is only available on the Workers Paid plan.</li>
</ul>
<h3 id="sqlite-storage-backend">SQLite storage backend</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="storage-billing-on-sqlite-backed-durable-objects">Storage billing on SQLite-backed Durable Objects</h3>
@markup("md", "content/.markup/bodies/8158.md")
</aside>
<table>
<thead>
<tr>
<th></th>
<th>Workers Free plan</th>
<th>Workers Paid plan</th>
</tr>
</thead>
<tbody>
<tr>
<td>Rows reads <sup>1,2</sup></td>
<td>5 million / day</td>
<td>First 25 billion / month included + $0.001 / million rows</td>
</tr>
<tr>
<td>Rows written <sup>1,2,3,4</sup></td>
<td>100,000 / day</td>
<td>First 50 million / month included + $1.00 / million rows</td>
</tr>
<tr>
<td>SQL Stored data <sup>5</sup></td>
<td>5 GB (total)</td>
<td>5 GB-month, + $0.20/ GB-month</td>
</tr>
</tbody>
</table>
<details class="nb-details" open><summary>Footnotes</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8161.md")
</div></details>
<h3 id="key-value-storage-backend">Key-value storage backend</h3>
<table>
<thead>
<tr>
<th></th>
<th>Workers Paid plan</th>
</tr>
</thead>
<tbody>
<tr>
<td>Read request units<sup>1,2</sup></td>
<td>1 million, + $0.20/million</td>
</tr>
<tr>
<td>Write request units<sup>3</sup></td>
<td>1 million, + $1.00/million</td>
</tr>
<tr>
<td>Delete requests<sup>4</sup></td>
<td>1 million, + $1.00/million</td>
</tr>
<tr>
<td>Stored data<sup>5</sup></td>
<td>1 GB, + $0.20/ GB-month</td>
</tr>
</tbody>
</table>
<details class="nb-details" open><summary>Footnotes</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8162.md")
</div></details>
<h2 id="compute-billing-examples">Compute billing examples</h2>
<p>These examples exclude the costs for the Workers calling the Durable Objects. When modelling the costs of a Durable Object, note that:</p>
<ul>
<li>Inactive objects receiving no requests do not incur any duration charges.</li>
<li>The <a href="/durable-objects/best-practices/websockets/#durable-objects-hibernation-websocket-api">WebSocket Hibernation API</a> can dramatically reduce duration-related charges for Durable Objects communicating with clients over the WebSocket protocol, especially if messages are only transmitted occasionally at sparse intervals.
<ul>
<li>An active outbound connection (via <a href="/workers/runtime-apis/tcp-sockets/"><code>connect()</code></a> or an outbound WebSocket) keeps a Durable Object in memory and causes it to incur duration charges for up to 15 minutes per connection, even with no incoming requests. Refer to <a href="/durable-objects/concepts/durable-object-lifecycle/">Lifecycle of a Durable Object</a> for more information.</li>
</ul>
</li>
</ul>
<h3 id="example-1">Example 1</h3>
<p>This example represents a simple Durable Object used as a co-ordination service invoked via HTTP.</p>
<ul>
<li>A single Durable Object was called by a Worker 1.5 million times</li>
<li>It is active for 1,000,000 seconds in the month</li>
</ul>
<p>In this scenario, the estimated monthly cost would be calculated as:</p>
<p><strong>Requests</strong>:</p>
<ul>
<li>1.5 million requests - included 1 million requests = 500,000 billable requests.</li>
<li>(rounded) 1,000,000 requests x $0.15 / 1,000,000 = $0.15.</li>
</ul>
<p><strong>Compute Duration</strong>:</p>
<ul>
<li>1,000,000 seconds * 128 MB / 1 GB = 128,000 GB-s.</li>
<li>128,000 GB-s is within the 400,000 GB-s included allocation = $0.00.</li>
</ul>
<p><strong>Estimated total</strong>: $0.15 (requests) + $0.00 (compute duration) + minimum $5/mo usage = $5.15 per month</p>
<h3 id="example-2">Example 2</h3>
<p>This example represents a moderately trafficked Durable Objects based application using WebSockets to broadcast game, chat or real-time user state across connected clients:</p>
<ul>
<li>100 Durable Objects have 50 WebSocket connections established to each of them.</li>
<li>Clients send approximately one message a minute for eight active hours a day, every day of the month.</li>
</ul>
<p>In this scenario, the estimated monthly cost would be calculated as:</p>
<p><strong>Requests</strong>:</p>
<ul>
<li>50 WebSocket connections * 100 Durable Objects to establish the WebSockets = 5,000 connections created each day * 30 days = 150,000 WebSocket connection requests.</li>
<li>50 messages per minute * 100 Durable Objects * 60 minutes * 8 hours * 30 days = 72,000,000 WebSocket message requests.</li>
<li>150,000 + (72 million requests / 20 for WebSocket message billing ratio) = 3.75 million billing request.</li>
<li>3.75 million requests - included 1 million requests = 2,750,000 billable requests.</li>
<li>(rounded) 3,000,000 requests x $0.15 / 1,000,000 = $0.45.</li>
</ul>
<p><strong>Compute Duration</strong>:</p>
<ul>
<li>100 Durable Objects * 60 seconds * 60 minutes * 8 hours * 30 days = 86,400,000 seconds.</li>
<li>86,400,000 seconds * 128 MB / 1 GB = 11,059,200 GB-s.</li>
<li>11,059,200 GB-s - included 400,000 GB-s = 10,659,200 GB-s</li>
<li>(rounded) 11,000,000 GB-s x $12.50 / 1,000,000 = $137.50.</li>
</ul>
<p><strong>Estimated total</strong>: $0.45 (requests) + $137.50 (compute duration) + minimum $5/mo usage = $142.95 per month.</p>
<h3 id="example-3">Example 3</h3>
<p>This example represents a horizontally scaled Durable Objects based application using WebSockets to communicate user-specific state to a single client connected to each Durable Object.</p>
<ul>
<li>100 Durable Objects each have a single WebSocket connection established to each of them.</li>
<li>Clients sent one message every second of the month so that the Durable Objects were active for the entire month.</li>
</ul>
<p>In this scenario, the estimated monthly cost would be calculated as:</p>
<p><strong>Requests</strong>:</p>
<ul>
<li>100 WebSocket connection requests.</li>
<li>1 message per second * 100 connections * 60 seconds * 60 minutes * 24 hours * 30 days = 259,200,000 WebSocket message requests.</li>
<li>100 + (259.2 million requests / 20 for WebSocket billing ratio) = 12,960,100 requests.</li>
<li>12,960,100 requests - included 1 million requests = 11,960,100 billable requests.</li>
<li>(rounded) 12,000,000 requests x $0.15 / 1,000,000 = $1.80.</li>
</ul>
<p><strong>Compute Duration</strong>:</p>
<ul>
<li>100 Durable Objects * 60 seconds * 60 minutes * 24 hours * 30 days = 259,200,000 seconds</li>
<li>259,200,000 seconds * 128 MB / 1 GB = 33,177,600 GB-s</li>
<li>33,177,600 GB-s - included 400,000 GB-s = 32,777,600 GB-s</li>
<li>(rounded) 33,000,000 GB-s x $12.50 / 1,000,000 = $412.50</li>
</ul>
<p><strong>Estimated total</strong>: $1.80 (requests) + $412.50 (compute duration) + minimum $5/mo usage = $419.30 per month</p>
<h3 id="example-4">Example 4</h3>
<p>This example represents a moderately trafficked Durable Objects based application using WebSocket Hibernation to broadcast game, chat or real-time user state across connected clients:</p>
<ul>
<li>100 Durable Objects each have 100 Hibernatable WebSocket connections established to each of them.</li>
<li>Clients send one message per minute, and it takes 10ms to process a single message in the <code>webSocketMessage()</code> handler. Since each Durable Object handles 100 WebSockets, cumulatively each Durable Object will be actively executing JS for 1 second each minute (100 WebSockets * 10ms).</li>
</ul>
<p>In this scenario, the estimated monthly cost would be calculated as:</p>
<p><strong>Requests</strong>:</p>
<ul>
<li>100 WebSocket connections * 100 Durable Objects to establish the WebSockets = 10,000 initial WebSocket connection requests.</li>
<li>100 messages per minute<sup>1</sup> * 100 Durable Objects * 60 minutes * 24 hours * 30 days = 432,000,000 requests.</li>
<li>10,000 + (432 million requests / 20 for WebSocket billing ratio) = 21,610,000 million requests.</li>
<li>21,610,000 requests - included 1 million requests = 20,610,000 billable requests.</li>
<li>(rounded) 21,000,000 requests x $0.15 / 1,000,000 = $3.15.</li>
</ul>
<p><strong>Compute Duration</strong>:</p>
<ul>
<li>100 Durable Objects * 1 second<sup>2</sup> * 60 minutes * 24 hours * 30 days = 4,320,000 seconds</li>
<li>4,320,000 seconds * 128 MB / 1 GB = 552,960 GB-s</li>
<li>552,960 GB-s - included 400,000 GB-s = 152,960 GB-s</li>
<li>(rounded) 1,000,000 GB-s x $12.50 / 1,000,000 = $12.50</li>
</ul>
<p><strong>Estimated total</strong>: $3.15 (requests) + $12.50 (compute duration) + minimum $5/mo usage = $20.65 per month</p>
<p><sup>1</sup> 100 messages per minute comes from the fact that 100 clients
connect to each DO, and each sends 1 message per minute.</p>
<p><sup>2</sup> The example uses 1 second because each Durable Object is active for
1 second per minute. This can also be thought of as 432 million requests that
each take 10 ms to execute (4,320,000 seconds).</p>
<h2 id="frequently-asked-questions">Frequently Asked Questions</h2>
<h3 id="when-does-a-durable-object-incur-duration-charges">When does a Durable Object incur duration charges?</h3>
<p>A Durable Object incurs duration charges when it is actively executing JavaScript — either handling a request or running event handlers — or when it is idle but does not meet the <a href="/durable-objects/concepts/durable-object-lifecycle/">conditions for hibernation</a>. An idle Durable Object that qualifies for hibernation does not incur duration charges, even during the brief window before the runtime hibernates it.</p>
<p>Once an object has been evicted from memory, the next time it is needed, it will be recreated (calling the constructor again).</p>
<p>There are several factors that can prevent a Durable Object from hibernating and cause it to continue incurring duration charges.</p>
<p>Find more information in <a href="/durable-objects/concepts/durable-object-lifecycle/">Lifecycle of a Durable Object</a>.</p>
<h3 id="does-an-empty-table-sqlite-database-contribute-to-my-storage">Does an empty table / SQLite database contribute to my storage?</h3>
<p>Yes, although minimal. Empty tables can consume at least a few kilobytes, based on the number of columns (table width) in the table. An empty SQLite database consumes approximately 12 KB of storage.</p>
<h3 id="does-metadata-stored-in-durable-objects-count-towards-my-storage">Does metadata stored in Durable Objects count towards my storage?</h3>
<p>All writes to a SQLite-backed Durable Object stores nominal amounts of metadata in internal tables in the Durable Object, which counts towards your billable storage.</p>
<p>The metadata remains in the Durable Object until you call <a href="/durable-objects/api/sqlite-storage-api/#deleteall"><code>deleteAll()</code></a>.</p>
