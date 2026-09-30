<p>You can monitor the status of your waiting rooms using the <a href="#status-in-the-dashboard">dashboard</a> or the <a href="#status-in-the-api">API</a>.</p>
<p>Note that the <strong>Total active users</strong> and <strong>Queued users</strong> shown in the dashboard, as well as through API endpoints are estimates. That data corresponding to each of these metrics is cached for around 30 seconds after the time it takes to be synced from all data centers globally. Therefore, the status will range between 20-50 seconds in the past, depending on the exact moment the data was queried, aggregated, as well as the age of the cache.</p>
<p>Refer to <a href="/waiting-room/waiting-room-analytics/">Waiting Room Analytics</a> for more details about the traffic going through your waiting room.</p>
<h2 id="status-in-the-dashboard">Status in the dashboard</h2>
<p>Open the <strong>Waiting Room</strong> dashboard to view the list of your waiting rooms.</p>
<p>The <strong>Status</strong> column displays the current state of the waiting room:</p>
<ul>
<li><strong>Not queueing</strong>:
<ul>
<li>Waiting room enabled, but has not reached traffic threshold to send visitors to waiting room.</li>
<li>Shows estimated number of users in the application.</li>
</ul>
</li>
<li><strong>Queueing</strong>:
<ul>
<li>Waiting room enabled and sending visitors to waiting room.</li>
<li>Shows estimated number of users in the queue.</li>
<li>On hover, shows maximum wait time expected for users.</li>
</ul>
</li>
<li><strong>Disabled</strong>: The waiting room is suspended.</li>
<li><strong>Queue-all</strong>:
<ul>
<li>Forces all traffic to queue in the waiting room.</li>
<li>On hover, shows estimated number of users in the queue.</li>
</ul>
</li>
</ul>
<h2 id="status-in-the-api">Status in the API</h2>
<p><a href="/api/resources/waiting_rooms/subresources/statuses/methods/get/">Check whether traffic is queueing in a configured waiting room</a> by appending the following endpoint to the Cloudflare API base URL:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/waiting_rooms/{waiting_room_id}/status \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<p>The response is:</p>
<ul>
<li><code>queueing</code> if visitors are currently queueing in the waiting room.</li>
<li><code>not_queueing</code> if the room is empty or if the waiting room is suspended.</li>
</ul>
<p>To check whether a configured waiting room is suspended or whether the traffic is force-queued to the waiting room, append the following endpoint to the Cloudflare API base URL.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/waiting_rooms/{waiting_room_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<p>The endpoint above <a href="/api/resources/waiting_rooms/methods/get/">fetches all settings</a> for a configured waiting room:</p>
<pre><code class="language-bash">      &quot;success&quot;: true,&#10;      &quot;errors&quot;: [],&#10;      &quot;messages&quot;: [],&#10;      &quot;result&quot;: {&#10;        &quot;id&quot;: &quot;REDACTED&quot;,&#10;        &quot;created_on&quot;: &quot;2014-01-01T05:20:00.12345Z&quot;,&#10;        &quot;modified_on&quot;: &quot;2014-01-01T05:20:00.12345Z&quot;,&#10;        &quot;name&quot;: &quot;shop_waiting_room&quot;,&#10;        &quot;description&quot;: &quot;Waiting room for webshop&quot;,&#10;        &quot;suspended&quot;: false,&#10;        &quot;host&quot;: &quot;shop.example.com&quot;,&#10;        &quot;path&quot;: &quot;/shop&quot;,&#10;        &quot;queue_all&quot;: true,&#10;        &quot;new_users_per_minute&quot;: 200,&#10;        &quot;total_active_users&quot;: 300,&#10;        &quot;session_duration&quot;: 1,&#10;        &quot;disable_session_renewal&quot;: false,&#10;        &quot;json_response_enabled&quot;: false,&#10;        &quot;queueing_method&quot;: &quot;random&quot;,&#10;        &quot;cookie_attributes&quot;: {&#10;          &quot;samesite&quot;: &quot;auto&quot;,&#10;          &quot;secure&quot;: &quot;auto&quot;&#10;        },&#10;        &quot;custom_page_html&quot;: &quot;{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Queue all enabled {{/waitTimeKnown}}&quot;&#10;      }&#10;</code></pre>
<p>The value of <code>suspended</code> indicates whether a waiting room is activated or suspended:</p>
<ul>
<li><code>false</code>: The waiting room is activated.</li>
<li><code>true</code>: The waiting room is suspended.</li>
</ul>
<p>The value of <code>queue_all</code> indicates whether all traffic is forced to queue in the waiting room:</p>
<ul>
<li><code>false</code>: Visitors are diverted to the waiting room only if traffic exceeds the configured threshold.</li>
<li><code>true</code>: All traffic is forced to queue in the waiting room, and no traffic passes from the waiting room to the origin.</li>
</ul>
<h2 id="queueing-activation">Queueing activation</h2>
<p>Waiting Room queues traffic at the data-center level to increase scalability, letting each data center make decisions independently.</p>
<p>Because of this design, the configured traffic limits of a waiting room are target values which your waiting room will work to keep your traffic volumes near. A waiting room might queue traffic from a specific data center before the waiting room reaches its limit of <code>new_users_per_minute</code> or <code>total_active_users</code>.</p>
<p>Waiting Room also continuously monitors the rate of users entering throughout each minute, and not just at the end of the minute. Therefore, if at the beginning of your minute, a large fraction of your set <code>new_users_per_minute</code> value already joined, we may start queueing users, even if the overall <code>new_users_per_minute</code> value that is reached for that minute is not hit.</p>
<p>To help prevent a waiting room from active queueing, increase the values for <code>new_users_per_minute</code> and/or <code>total_active_users</code>. For more information about how Waiting Room makes queueing decisions, review our <a href="https://blog.cloudflare.com/how-waiting-room-queues">blogpost</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15743.md")
</aside>
