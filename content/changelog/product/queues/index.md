<h1 id="changelog">Changelog</h1>

<h2 id="subscribe-to-email-sending-events-with-queues"><a href="/changelog/post/2026-07-15-event-subscriptions/">Subscribe to Email Sending events with Queues</a></h2>
<p><em>2026-07-15</em></p>
<p>You can now subscribe to <strong><a href="/email-service/api/send-emails/">Email Sending</a> events</strong> through <a href="/queues/event-subscriptions/">Queues event subscriptions</a> and receive outbound transactional email lifecycle events on a queue. Each subscription is scoped to one sending domain — either the zone apex, such as <code>example.com</code>, or a verified sending subdomain, such as <code>send.example.com</code>.</p>
<p>Six event types are published: <code>message.delivered</code>, <code>message.deferred</code>, <code>message.bounced</code>, <code>message.failed</code>, <code>message.rejected</code>, and <code>message.complained</code>. Use them to track deliverability, react to bounces and complaints, and drive suppression or retry logic. Email Routing events are not published on this source.</p>
<p>Each event includes the message details, delivery status, and SMTP response:</p>
<pre><code class="language-json">{&#10;	&quot;type&quot;: &quot;cf.email.sending.message.delivered&quot;,&#10;	&quot;source&quot;: {&#10;		&quot;type&quot;: &quot;email.sending&quot;,&#10;		&quot;zoneId&quot;: &quot;023e105f4ecef8ad9ca31a8372d0c353&quot;,&#10;		&quot;domain&quot;: &quot;example.com&quot;&#10;	},&#10;	&quot;payload&quot;: {&#10;		&quot;messageId&quot;: &quot;0101018f7d0c4d9a-msg-deadbeef&quot;,&#10;		&quot;recipient&quot;: &quot;user@example.net&quot;,&#10;		&quot;terminal&quot;: true,&#10;		&quot;delivery&quot;: {&#10;			&quot;status&quot;: &quot;delivered&quot;,&#10;			&quot;smtpStatusCode&quot;: &quot;250&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Refer to <a href="/email-service/platform/event-subscriptions/">Event subscriptions</a> to see all event types and example payloads.</p>


<h2 id="billable-usage-and-budget-alerts-now-in-product-sidebars"><a href="/changelog/post/2026-06-04-billable-usage-product-sidebar/">Billable usage and budget alerts now in product sidebars</a></h2>
<p><em>2026-06-04</em></p>
<p>Pay-as-you-go customers can now view billable usage and create <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">budget alerts</a> directly from the product overview pages for <a href="/workers/">Workers &amp; Pages</a>, <a href="/d1/">D1</a>, <a href="/r2/">R2</a>, <a href="/kv/">Workers KV</a>, <a href="/queues/">Queues</a>, <a href="/vectorize/">Vectorize</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/containers/">Containers</a>. A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.</p>
<p>The widget pulls from the same data as the <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">Billable Usage dashboard</a> and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-06-04-billable-usage-product-sidebar.png" alt="Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service" /></p>
<p>Selecting <strong>Create budget alert</strong> opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.</p>
<p>For more information, refer to the <a href="/billing/">Usage-based billing documentation</a>.</p>


<h2 id="event-subscriptions-for-artifacts-lifecycle-events"><a href="/changelog/post/2026-05-19-event-subscriptions/">Event subscriptions for Artifacts lifecycle events</a></h2>
<p><em>2026-05-19</em></p>
<p>You can now receive <a href="/queues/event-subscriptions/">event notifications</a> for <a href="/artifacts/">Artifacts</a> repository changes and consume them from a Worker to build commit-driven automation.</p>
<p>This allows you to:</p>
<ul>
<li>Run custom workflows when a repository is created or imported</li>
<li>Kick off a build and deploy a change when an agent pushes to a repo</li>
<li>Trigger a review agent on every push</li>
</ul>
<p>Available events include:</p>
<ul>
<li><strong>Account-level events</strong> (<code>artifacts</code> source) — <code>repo.created</code>, <code>repo.deleted</code>, <code>repo.forked</code>, <code>repo.imported</code></li>
<li><strong>Repository-level events</strong> (<code>artifacts.repo</code> source) — <code>pushed</code>, <code>cloned</code>, <code>fetched</code></li>
</ul>
<p>To learn more, refer to <a href="/artifacts/guides/event-subscriptions/">Artifacts documentation</a>.</p>


<h2 id="realtime-backlog-metrics-now-available-for-queues"><a href="/changelog/post/2026-04-28-improved-queues-metrics/">Realtime backlog metrics now available for Queues</a></h2>
<p><em>2026-04-28</em></p>
<p><a href="/queues/">Queues</a>, Cloudflare's managed message queue, now exposes realtime backlog metrics via the dashboard, REST API, and JavaScript API. Three new fields are available:</p>
<ul>
<li><strong><code>backlog_count</code></strong> — the number of unacknowledged messages in the queue</li>
<li><strong><code>backlog_bytes</code></strong> — the total size of those messages in bytes</li>
<li><strong><code>oldest_message_timestamp_ms</code></strong> — the timestamp of the oldest unacknowledged message</li>
</ul>
<p>The following endpoints also now include a <code>metadata.metrics</code> object on the result field after successful message consumption:</p>
<ul>
<li><code>/accounts/{account_id}/queues/{queue_id}/messages/pull</code></li>
<li><code>/accounts/{account_id}/queues/{queue_id}/messages</code></li>
<li><code>/accounts/{account_id}/queues/{queue_id}/messages/batch</code></li>
</ul>
<h4 id="2026-04-28-improved-queues-metrics-javascript-apis">Javascript APIs</h4>
<p>Call <code>env.QUEUE.metrics()</code> to get realtime backlog metrics:</p>
<pre><code class="language-ts">const {&#10;	backlogCount, // number&#10;	backlogBytes, // number&#10;	oldestMessageTimestamp, // Date | undefined&#10;} = await env.QUEUE.metrics();&#10;</code></pre>
<p><code>env.QUEUE.send()</code> and <code>env.QUEUE.sendBatch()</code> also now return a metrics object on the response.</p>
<p>You can also query these fields via the <a href="/analytics/graphql-api/">GraphQL Analytics API</a> or view realtime backlog on the <a href="https://dash.cloudflare.com/?to=/:account/workers/queues">dashboard</a>.</p>
<p><img src="/assets/upstream/images/changelog/queues/2026-04-28-queues-metrics.png" alt="Queues realtime backlog" /></p>
<p>For more information, refer to <a href="/queues/observability/metrics/">Queues metrics</a>.</p>


<h2 id="cloudflare-queues-now-available-on-workers-free-plan"><a href="/changelog/post/2026-02-04-queues-free-plan/">Cloudflare Queues now available on Workers Free plan</a></h2>
<p><em>2026-02-04</em></p>
<p><a href="/queues">Cloudflare Queues</a> is now part of the Workers free plan, offering guaranteed message delivery across up to <strong>10,000 queues</strong> to either <a href="/workers">Cloudflare Workers</a> or <a href="/queues/configuration/pull-consumers">HTTP pull consumers</a>. Every Cloudflare account now includes <strong>10,000 operations per day</strong> across reads, writes, and deletes. For more details on how each operation is defined, refer to <a href="https://developers.cloudflare.com/workers/platform/pricing/#queues">Queues pricing</a>.</p>
<p>All features of the existing Queues functionality are available on the free plan, including unlimited <a href="/queues/event-subscriptions/">event subscriptions</a>. Note that the maximum retention period on the free tier, however, is 24 hours rather than 14 days.</p>
<p>If you are new to Cloudflare Queues, follow <a href="https://developers.cloudflare.com/queues/get-started/">this guide</a> or try one of our <a href="/queues/tutorials/">tutorials</a> to get started.</p>


<h2 id="get-notified-when-your-workers-builds-succeed-or-fail"><a href="/changelog/post/2025-12-11-builds-event-subscriptions/">Get notified when your Workers builds succeed or fail</a></h2>
<p><em>2026-01-09</em></p>
<p>You can now receive notifications when your Workers' builds start, succeed, fail, or get cancelled using <a href="/queues/event-subscriptions/">Event Subscriptions</a>.</p>
<p><a href="/workers/ci-cd/builds/">Workers Builds</a> publishes events to a <a href="/queues/">Queue</a> that your Worker can read messages from, and then send notifications wherever you need — Slack, Discord, email, or any webhook endpoint.</p>
<p>You can deploy <a href="https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template">this Worker</a> to your own Cloudflare account to send build notifications to Slack:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>The template includes:</p>
<ul>
<li>Build status with Preview/Live URLs for successful deployments</li>
<li>Inline error messages for failed builds</li>
<li>Branch, commit hash, and author name</li>
</ul>
<p><img src="/assets/upstream/images/changelog/workers/builds-notifications-slack.png" alt="Slack notifications showing build events" /></p>
<p>For setup instructions, refer to the <a href="https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template#readme">template README</a> or the <a href="/queues/event-subscriptions/manage-event-subscriptions/">Event Subscriptions documentation</a>.</p>


<h2 id="subscribe-to-events-from-cloudflare-services-with-queues"><a href="/changelog/post/2025-08-19-event-subscriptions/">Subscribe to events from Cloudflare services with Queues</a></h2>
<p><em>2025-08-19 12:00:00 UTC</em></p>
<p>You can now subscribe to events from other Cloudflare services (for example, <a href="/kv/">Workers KV</a>, <a href="/workers-ai">Workers AI</a>, <a href="/workers">Workers</a>) and consume those events via <a href="/queues/">Queues</a>, allowing you to build custom workflows, integrations, and logic in response to account activity.</p>
<p><img src="/assets/upstream/images/queues/queues-event-subscriptions.png" alt="Event subscriptions architecture" /></p>
<p>Event subscriptions allow you to receive messages when events occur across your Cloudflare account. Cloudflare products can publish structured events to a queue, which you can then consume with <a href="/workers/">Workers</a> or <a href="/queues/configuration/pull-consumers/">pull via HTTP from anywhere</a>.</p>
<p>To create a subscription, use the dashboard or <a href="/workers/wrangler/commands/queues/#queues-subscription-create">Wrangler</a>:</p>
<pre><code class="language-bash">npx wrangler queues subscription create my-queue --source r2 --events bucket.created&#10;</code></pre>
<p>An event is a structured record of something happening in your Cloudflare account – like a Workers AI batch request being queued, a Worker build completing, or an R2 bucket being created. Events follow a consistent structure:</p>
<pre><code class="language-json">{&#10;  &quot;type&quot;: &quot;cf.r2.bucket.created&quot;,&#10;  &quot;source&quot;: {&#10;    &quot;type&quot;: &quot;r2&quot;&#10;  },&#10;  &quot;payload&quot;: {&#10;    &quot;name&quot;: &quot;my-bucket&quot;,&#10;    &quot;location&quot;: &quot;WNAM&quot;&#10;  },&#10;  &quot;metadata&quot;: {&#10;    &quot;accountId&quot;: &quot;f9f79265f388666de8122cfb508d7776&quot;,&#10;    &quot;eventTimestamp&quot;: &quot;2025-07-28T10:30:00Z&quot;&#10;  }&#10;}&#10;</code></pre>
<p>Current <a href="/queues/event-subscriptions/events-schemas/">event sources</a> include <a href="/r2/">R2</a>, <a href="/kv/">Workers KV</a>, <a href="/workers-ai/">Workers AI</a>, <a href="/workers/ci-cd/builds/">Workers Builds</a>, <a href="/vectorize/">Vectorize</a>, <a href="/r2/data-migration/super-slurper/">Super Slurper</a>, and <a href="/workflows/">Workflows</a>. More sources and events are on the way.</p>
<p>For more information on event subscriptions, available events, and how to get started, refer to our <a href="/queues/event-subscriptions/">documentation</a>.</p>


<h2 id="publish-messages-to-queues-directly-via-http"><a href="/changelog/post/2025-05-09-publish-to-queues-via-http/">Publish messages to Queues directly via HTTP</a></h2>
<p><em>2025-05-09 12:00:00 UTC</em></p>
<p>You can now publish messages to <a href="/queues/">Cloudflare Queues</a> directly via HTTP from any service or programming language that supports sending HTTP requests. Previously, publishing to queues was only possible from within <a href="/workers/">Cloudflare Workers</a>. You can already consume from queues via Workers or <a href="/queues/configuration/pull-consumers/">HTTP pull consumers</a>, and now publishing is just as flexible.</p>
<p>Publishing via HTTP requires a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> with <code>Queues Edit</code> permissions for authentication. Here's a simple example:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/queues/&lt;queue_id&gt;/messages&quot; \&#10;  &#45;X POST \&#10;  &#45;H &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;-data &#x27;{ &quot;body&quot;: { &quot;greeting&quot;: &quot;hello&quot;, &quot;timestamp&quot;:  &quot;2025-07-24T12:00:00Z&quot;} }&#x27;&#10;</code></pre>
<p>You can also use our <a href="/fundamentals/api/reference/sdks/">SDKs</a> for TypeScript, Python, and Go.</p>
<p>To get started with HTTP publishing, check out our <a href="/queues/examples/publish-to-a-queue-via-http/">step-by-step example</a> and the full API documentation in our <a href="/api/resources/queues/subresources/messages/methods/push/">API reference</a>.</p>


<h2 id="increased-limits-for-queues-pull-consumers"><a href="/changelog/post/2025-04-17-pull-consumer-limits/">Increased limits for Queues pull consumers</a></h2>
<p><em>2025-04-17 12:00:00 UTC</em></p>
<p><a href="/queues/configuration/pull-consumers/">Queues pull consumers</a> can now pull and acknowledge up to <strong>5,000 messages / second per queue</strong>. Previously, pull consumers were rate limited to 1,200 requests / 5 minutes, aggregated across all queues.</p>
<p>Pull consumers allow you to consume messages over HTTP from any environment—including outside of <a href="/workers">Cloudflare Workers</a>. They’re also useful when you need fine-grained control over how quickly messages are consumed.</p>
<p>To setup a new queue with a pull based consumer using <a href="/workers/wrangler/">Wrangler</a>, run:</p>
<pre><code class="language-sh">npx wrangler queues create my-queue&#10;npx wrangler queues consumer http add my-queue&#10;</code></pre>
<p>You can also configure a pull consumer using the <a href="/api/resources/queues/subresources/consumers/methods/create/">REST API</a> or the Queues dashboard.</p>
<p>Once configured, you can pull messages from the queue using any HTTP client. You'll need a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API Token</a> with <code>queues_read</code> and <code>queues_write</code> permissions. For example:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/${CF_ACCOUNT_ID}/queues/${QUEUE_ID}/messages/pull&quot; \&#10;&#45;-header &quot;Authorization: Bearer ${API_TOKEN}&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{ &quot;visibility_timeout&quot;: 10000, &quot;batch_size&quot;: 2 }&#x27;&#10;</code></pre>
<p>To learn more about how to acknowledge messages, pull batches at once, and setup multiple consumers, refer to the <a href="/queues/configuration/pull-consumers">pull consumer documentation</a>.</p>
<p>As always, Queues doesn't charge for data egress. Pull operations continue to be billed at the <a href="/queues/platform/pricing">existing rate</a>, of $0.40 / million operations. The increased limits are available now, on all new and existing queues. If you're new to Queues, <a href="/queues/get-started">get started with the Cloudflare Queues guide</a>.</p>


<h2 id="new-pause-purge-apis-for-queues"><a href="/changelog/post/2025-03-25-pause-purge-queues/">New Pause & Purge APIs for Queues</a></h2>
<p><em>2025-03-27 12:00:00 UTC</em></p>
<p><a href="/queues/">Queues</a> now supports the ability to pause message delivery and/or purge (delete) messages on a queue. These operations can be useful when:</p>
<ul>
<li>Your consumer has a bug or downtime, and you want to temporarily stop messages from being processed while you fix the bug</li>
<li>You have pushed invalid messages to a queue due to a code change during development, and you want to clean up the backlog</li>
<li>Your queue has a backlog that is stale and you want to clean it up to allow new messages to be consumed</li>
</ul>
<p>To pause a queue using <a href="/workers/wrangler/">Wrangler</a>, run the <code>pause-delivery</code> command. Paused queues continue to receive messages. And you can easily unpause a queue using the <code>resume-delivery</code> command.</p>
<pre><code class="language-bash">$ wrangler queues pause-delivery my-queue&#10;Pausing message delivery for queue my-queue.&#10;Paused message delivery for queue my-queue.&#10;&#10;$ wrangler queues resume-delivery my-queue&#10;Resuming message delivery for queue my-queue.&#10;Resumed message delivery for queue my-queue.&#10;</code></pre>
<p>Purging a queue permanently deletes all messages in the queue. Unlike pausing, purging is an irreversible operation:</p>
<pre><code class="language-bash">$ wrangler queues purge my-queue&#10;✔ This operation will permanently delete all the messages in queue my-queue. Type my-queue to proceed. … my-queue&#10;Purged queue &#x27;my-queue&#x27;&#10;</code></pre>
<p>You can also do these operations using the <a href="/api/resources/queues/">Queues REST API</a>, or the dashboard page for a queue.</p>
<p><img src="/assets/upstream/images/queues/pause-purge.png" alt="Pause and purge using the dashboard" /></p>
<p>This feature is available on all new and existing queues. Head over to the <a href="/queues/configuration/pause-purge">pause and purge documentation</a> to learn more. And if you haven't used Cloudflare Queues before, <a href="/queues/get-started">get started with the Cloudflare Queues guide</a>.</p>


<h2 id="customize-queue-message-retention-periods"><a href="/changelog/post/2025-02-14-customize-queue-retention-period/">Customize queue message retention periods</a></h2>
<p><em>2025-02-14 12:00:00 UTC</em></p>
<p>You can now customize a queue's message retention period, from a minimum of 60 seconds to a maximum of 14 days. Previously, it was fixed to the default of 4 days.</p>
<p><img src="/assets/upstream/images/queues/customize-retention-period.png" alt="Customize a queue's message retention period" /></p>
<p>You can customize the retention period on the settings page for your queue, or using Wrangler:</p>
<pre><code class="language-bash">$ wrangler queues update my-queue --message-retention-period-secs 600&#10;</code></pre>
<p>This feature is available on all new and existing queues. If you haven't used Cloudflare Queues before, <a href="/queues/get-started">get started with the Cloudflare Queues guide</a>.</p>



