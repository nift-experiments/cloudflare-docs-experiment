<p class="article-summary">Use the dashboard to fetch and acknowledge the messages currently in a queue.</p>
<h2 id="list-messages-from-the-dashboard">List messages from the dashboard</h2>
<p>Listing messages from the dashboard allows you to debug Queues or queue producers without a consumer Worker. Fetching a batch of messages to preview will not acknowledge or retry the message or affect its position in the queue. The queue can still be consumed normally by a consumer Worker.</p>
<p>To list messages in the dashboard:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11246.md")
</div>
<p>This will preview a batch of messages currently in the Queue.</p>
<h2 id="acknowledge-messages-from-the-dashboard">Acknowledge messages from the dashboard</h2>
<p>Acknowledging messages from the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> will permanently remove them from the queue, with equivalent behavior as <code>ack()</code> in a Worker.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11247.md")
</div>
<p>This will remove the selected messages from the queue and prevent consumers from processing them further.</p>
<p>Refer to the <a href="/queues/get-started/">Get Started guide</a> to learn how to process and acknowledge messages from a queue in a Worker.</p>
