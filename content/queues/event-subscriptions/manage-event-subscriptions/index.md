<p>Learn how to:</p>
<ul>
<li>Create event subscriptions to receive messages from Cloudflare services.</li>
<li>View existing subscriptions on your queues.</li>
<li>Delete subscriptions you no longer need.</li>
</ul>
<h2 id="create-subscription">Create subscription</h2>
<p>Creating a subscription allows your queue to receive messages when events occur in Cloudflare services. You can specify which source and events you want to subscribe to.</p>
<h3 id="dashboard">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11248.md")
</div>
<h3 id="wrangler-cli">Wrangler CLI</h3>
<p>To create a subscription using Wrangler, run the <a href="/queues/reference/wrangler-commands/#queues-subscription-create"><code>queues subscription create command</code></a>:</p>
<pre><code class="language-bash">npx wrangler queues subscription create &lt;queue-name&gt; --source &lt;source-type&gt; --events &lt;event1,event2&gt; --&lt;source-specific-option&gt; &lt;value&gt;&#10;</code></pre>
<p>To learn more about which sources and events you can subscribe to, refer to <a href="/queues/event-subscriptions/events-schemas/">Events &amp; schemas</a>.</p>
<h2 id="view-existing-subscriptions">View existing subscriptions</h2>
<p>You can view all subscriptions configured for a queue to see what events it is currently receiving.</p>
<h3 id="dashboard-1">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11249.md")
</div>
<h3 id="wrangler-cli-1">Wrangler CLI</h3>
<p>To list subscriptions for a queue, run the <a href="/queues/reference/wrangler-commands/#queues-subscription-list"><code>queues subscription list command</code></a>:</p>
<pre><code class="language-bash">npx wrangler queues subscription list &lt;queue-name&gt;&#10;</code></pre>
<h2 id="delete-subscription">Delete subscription</h2>
<p>When you delete a subscription, your queue will stop receiving messages for those events immediately.</p>
<h3 id="dashboard-2">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11250.md")
</div>
<h3 id="wrangler-cli-2">Wrangler CLI</h3>
<p>To delete a subscription, run the <a href="/queues/reference/wrangler-commands/#queues-subscription-delete"><code>queues subscription delete command</code></a>:</p>
<pre><code class="language-bash">npx wrangler queues subscription delete &lt;queue-name&gt; --id &lt;subscription-id&gt;&#10;</code></pre>
<h2 id="learn-more">Learn more</h2>
<p><a class="nb-card nb-link-card" href="/queues/event-subscriptions/events-schemas/"><h3 id="card-events-schemas-queues-event-subscriptions-events-schemas">Events &amp; schemas</h3><p>Explore available event sources and types that you can subscribe to.</p></a></p>
