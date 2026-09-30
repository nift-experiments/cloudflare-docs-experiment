---
cp9:
  canonical: https://developers.cloudflare.com/queues/configuration/pull-consumers/
  description: Pull messages from a Cloudflare Queue over HTTP from any environment or language.
  full_title: Cloudflare Queues - Pull consumers · Cloudflare Queues docs
  head_html: <title>Cloudflare Queues - Pull consumers · Cloudflare Queues docs</title><meta name="generator" content="Nift"><meta name="description" content="Pull messages from a Cloudflare Queue over HTTP from any environment or language."><link rel="canonical" href="https://developers.cloudflare.com/queues/configuration/pull-consumers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/queues/configuration/pull-consumers/index.md"><meta property="og:title" content="Cloudflare Queues - Pull consumers · Cloudflare Queues docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Pull messages from a Cloudflare Queue over HTTP from any environment or language."><meta property="og:url" content="https://developers.cloudflare.com/queues/configuration/pull-consumers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Queues"><meta name="algolia_product_filter" content="Queues"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Queues"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/queues/configuration/pull-consumers/#page","headline":"Cloudflare Queues - Pull consumers \u00b7 Cloudflare Queues docs","description":"Pull messages from a Cloudflare Queue over HTTP from any environment or language.","url":"https://developers.cloudflare.com/queues/configuration/pull-consumers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /queues/configuration/pull-consumers/
  schema: 1
---
<p>A pull-based consumer allows you to pull from a queue over HTTP from any environment and/or programming language outside of Cloudflare Workers. A pull-based consumer can be useful when your message consumption rate is limited by upstream infrastructure or long-running tasks.</p>
<h2 id="how-to-choose-between-push-or-pull-consumer">How to choose between push or pull consumer</h2>
<p>Deciding whether to configure a push-based consumer or a pull-based consumer will depend on how you are using your queues, as well as the configuration of infrastructure upstream from your queue consumer.</p>
<ul>
<li><strong>Starting with a <a href="/queues/reference/how-queues-works/#consumers">push-based consumer</a> is the easiest way to get started and consume from a queue</strong>. A push-based consumer runs on Workers, and by default, will automatically scale up and consume messages as they are written to the queue.</li>
<li>Use a pull-based consumer if you need to consume messages from existing infrastructure outside of Cloudflare Workers, and/or where you need to carefully control how fast messages are consumed. A pull-based consumer must explicitly make a call to pull (and then acknowledge) messages from the queue, only when it is ready to do so.</li>
</ul>
<p>You can remove and attach a new consumer on a queue at any time, allowing you to change from a pull-based to a push-based consumer if your requirements change.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="retrieve-an-api-bearer-token">Retrieve an API bearer token</h3>
@markup("md", "content/.markup/bodies/11255.md")
</aside>
<p>To configure a pull-based consumer and receive messages from a queue, you need to:</p>
<ol>
<li>Enable HTTP pull for the queue.</li>
<li>Create a valid authentication token for the HTTP client.</li>
<li>Pull message batches from the queue.</li>
<li>Acknowledge and/or retry messages within a batch.</li>
</ol>
<h2 id="1-enable-http-pull"><ol>
<li>Enable HTTP pull</li>
</ol></h2>
<p>You can enable HTTP pull or change a queue from push-based to pull-based via the <code>wrangler</code> CLI or via the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>. Enabling HTTP pull from a <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> is no longer supported.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11254.md")
</aside>
<h3 id="wrangler-cli">wrangler CLI</h3>
<p>You can enable a pull-based consumer on any existing queue by using the <code>wrangler queues consumer http</code> sub-commands and providing a queue name.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler queues consumer http add $QUEUE-NAME&#10;</code></pre>
<p>If you have an existing push-based consumer, you will need to remove that first. <code>wrangler</code> will return an error if you attempt to call <code>consumer http add</code> on a queue with an existing consumer configuration:</p>
<pre tabindex="0"><code class="language-sh">wrangler queues consumer worker remove $QUEUE-NAME $SCRIPT_NAME&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11253.md")
</aside>
<h2 id="2-consumer-authentication"><ol start="2">
<li>Consumer authentication</li>
</ol></h2>
<p>HTTP Pull consumers require an <a href="/fundamentals/api/get-started/create-token/">API token</a> with the <code>com.cloudflare.api.account.queues_read</code> and <code>com.cloudflare.api.account.queues_write</code> permissions.</p>
<p>Both read <em>and</em> write are required as a pull-based consumer needs to write to the queue state to acknowledge the messages it receives. Consuming messages mutates the queue.</p>
<p>API tokens are presented as Bearer tokens in the <code>Authorization</code> header of a HTTP request in the format <code>Authorization: Bearer $YOUR_TOKEN_HERE</code>. The following example shows how to pass an API token using the <code>curl</code> HTTP client:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/${CF_ACCOUNT_ID}/queues/${QUEUE_ID}/messages/pull&quot; \&#10;&#45;-header &quot;Authorization: Bearer ${QUEUES_TOKEN}&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{ &quot;visibility_timeout_ms&quot;: 10000, &quot;batch_size&quot;: 2 }&#x27;&#10;</code></pre>
<p>You may authenticate and run multiple concurrent pull-based consumers against a single queue.</p>
<h3 id="create-api-tokens">Create API tokens</h3>
<p>To create an API token:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>.</li>
<li>Go to <strong>My Profile</strong> &gt; <a href="https://dash.cloudflare.com/profile/api-tokens">API Tokens</a>.</li>
<li>Select <strong>Create Token</strong>.</li>
<li>Scroll to the bottom of the page and select <strong>Create Custom Token</strong>.</li>
<li>Give the token a name. For example, <code>queue-pull-token</code>.</li>
<li>Under the <strong>Permissions</strong> section, choose <strong>Account</strong> and then <strong>Queues</strong>. Ensure you have selected <strong>Edit</strong> (read+write).</li>
<li>(Optional) Select <strong>All accounts</strong> (default) or a specific account to scope the token to.</li>
<li>Select <strong>Continue to summary</strong> and then <strong>Create token</strong>.</li>
</ol>
<p>You will need to note the token down: it will only be displayed once.</p>
<h2 id="3-pull-messages"><ol start="3">
<li>Pull messages</li>
</ol></h2>
<p>To pull a message, make a HTTP POST request to the <a href="/api/resources/queues/subresources/messages/methods/pull/">Queues REST API</a> with a JSON-encoded body that optionally specifies a <code>visibility_timeout</code> and a <code>batch_size</code>, or an empty JSON object (<code>{}</code>):</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11258.md")
</div></div>
<p>This will return an array of messages (up to the specified <code>batch_size</code>) in the below format:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result&quot;: {&#10;		&quot;message_backlog_count&quot;: 10,&#10;		&quot;messages&quot;: [&#10;			{&#10;				&quot;body&quot;: &quot;hello&quot;,&#10;				&quot;id&quot;: &quot;1ad27d24c83de78953da635dc2ea208f&quot;,&#10;				&quot;timestamp_ms&quot;: 1689615013586,&#10;				&quot;attempts&quot;: 2,&#10;				&quot;metadata&quot;: {&#10;					&quot;CF-sourceMessageSource&quot;: &quot;dash&quot;,&#10;					&quot;CF-Content-Type&quot;: &quot;json&quot;&#10;				},&#10;				&quot;lease_id&quot;: &quot;eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIn0..NXmbr8h6tnKLsxJ_AuexHQ.cDt8oBb_XTSoKUkVKRD_Jshz3PFXGIyu7H1psTO5UwI.smxSvQ8Ue3-ymfkV6cHp5Va7cyUFPIHuxFJA07i17sc&quot;&#10;			},&#10;			{&#10;				&quot;body&quot;: &quot;world&quot;,&#10;				&quot;id&quot;: &quot;95494c37bb89ba8987af80b5966b71a7&quot;,&#10;				&quot;timestamp_ms&quot;: 1689615013586,&#10;				&quot;attempts&quot;: 2,&#10;				&quot;metadata&quot;: {&#10;					&quot;CF-sourceMessageSource&quot;: &quot;dash&quot;,&#10;					&quot;CF-Content-Type&quot;: &quot;json&quot;&#10;				},&#10;				&quot;lease_id&quot;: &quot;eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIn0..QXPgHfzETsxYQ1Vd-H0hNA.mFALS3lyouNtgJmGSkTzEo_imlur95EkSiH7fIRIn2U.PlwBk14CY_EWtzYB-_5CR1k30bGuPFPUx1Nk5WIipFU&quot;&#10;			}&#10;		]&#10;	}&#10;}&#10;</code></pre>
<p>Pull consumers follow a &quot;short polling&quot; approach: if there are messages available to be delivered, Queues will return a response immediately with messages up to the configured <code>batch_size</code>. If there are no messages to deliver, Queues will return an empty response. Queues does not hold an open connection (often referred to as &quot;long polling&quot;) if there are no messages to deliver.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11252.md")
</aside>
<p>Each message object has five fields:</p>
<ol>
<li><code>body</code> - this may be base64 encoded based on the <a href="#content-types">content-type the message was published as</a>.</li>
<li><code>id</code> - a unique, read-only ephemeral identifier for the message.</li>
<li><code>timestamp_ms</code> - when the message was published to the queue in milliseconds since the <a href="https://en.wikipedia.org/wiki/Unix_time">Unix epoch</a>. This allows you to determine how old a message is by subtracting it from the current timestamp.</li>
<li><code>attempts</code> - how many times the message has been attempted to be delivered in full. When this reaches the value of <code>max_retries</code>, the message will not be re-delivered and will be deleted from the queue permanently.</li>
<li><code>lease_id</code> - the encoded lease ID of the message. The <code>lease_id</code> is used to explicitly acknowledge or retry the message.</li>
</ol>
<p>The <code>lease_id</code> allows your pull consumer to explicitly acknowledge some, none or all messages in the batch or mark them for retry. If messages are not acknowledged or marked for retry by the consumer, then they will be marked for re-delivery once the <code>visibility_timeout</code> is reached. A <code>lease_id</code> is no longer valid once this timeout has been reached.</p>
<p>You can configure both <code>batch_size</code> and <code>visibility_timeout</code> when pulling from a queue:</p>
<ul>
<li><code>batch_size</code> (defaults to 5; max 100) - how many messages are returned to the consumer in each pull.</li>
<li><code>visibility_timeout</code> (defaults to 30 second; max 12 hours) - defines how long the consumer has to explicitly acknowledge messages delivered in the batch based on their <code>lease_id</code>. Once this timeout expires, messages are assumed unacknowledged and queued for re-delivery again.</li>
</ul>
<h3 id="concurrent-consumers">Concurrent consumers</h3>
<p>You may have multiple HTTP clients pulling from the same queue concurrently: each client will receive a unique batch of messages and retain the &quot;lease&quot; on those messages up until the <code>visibility_timeout</code> expires, or until those messages are marked for retry.</p>
<p>Messages marked for retry will be put back into the queue and can be delivered to any consumer. Messages are <em>not</em> tied to a specific consumer, as consumers do not have an identity and to avoid a slow or stuck consumer from holding up processing of messages in a queue.</p>
<p>Multiple consumers can be useful in cases where you have multiple upstream resources (for example, GPU infrastructure), where you want to autoscale based on the <a href="/queues/observability/metrics/">backlog</a> of a queue, and/or cost.</p>
<h2 id="4-acknowledge-messages"><ol start="4">
<li>Acknowledge messages</li>
</ol></h2>
<p>Messages pulled by a consumer need to be either acknowledged or marked for retry.</p>
<p>To acknowledge and/or mark messages to be retried, make a HTTP <code>POST</code> request to <code>/ack</code> endpoint of your queue per the <a href="/api/resources/queues/subresources/messages/methods/ack/">Queues REST API</a> by providing an array of <code>lease_id</code> objects to acknowledge and/or retry:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11261.md")
</div></div>
<p>You may optionally specify the number of seconds to delay a message for when marking it for retry by providing a <code>{ lease_id: string, delay_seconds: number }</code> object in the <code>retries</code> array:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;acks&quot;: [&#10;		{ &quot;lease_id&quot;: &quot;lease_id1&quot; },&#10;		{ &quot;lease_id&quot;: &quot;lease_id2&quot; },&#10;		{ &quot;lease_id&quot;: &quot;lease_id3&quot; }&#10;	],&#10;	&quot;retries&quot;: [{ &quot;lease_id&quot;: &quot;lease_id4&quot;, &quot;delay_seconds&quot;: 600 }]&#10;}&#10;</code></pre>
<p>Additionally:</p>
<ul>
<li>You should provide every <code>lease_id</code> in the request to the <code>/ack</code> endpoint if you are processing those messages in your consumer. If you do not acknowledge a message, it will be marked for re-delivery (put back in the queue).</li>
<li>You can optionally mark messages to be retried: for example, if there is an error processing the message or you have upstream resource pressure. Explicitly marking a message for retry will place it back into the queue immediately, instead of waiting for a (potentially long) <code>visibility_timeout</code> to be reached.</li>
<li>You can make multiple calls to the <code>/ack</code> endpoint as you make progress through a batch of messages, but we recommend grouping acknowledgements to reduce the number of API calls required.</li>
</ul>
<p>Queues aims to be permissive when it comes to lease IDs: if a consumer acknowledges a message by its lease ID <em>after</em> the visibility timeout is reached, Queues will still accept that acknowledgment. If the message was delivered to another consumer during the intervening period, it will also be able to acknowledge the message without an error.</p>
<h2 id="content-types">Content types</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11251.md")
</aside>
<p>When publishing to a queue that has an external consumer, you should be aware that certain content types may be encoded in a way that allows them to be safely serialized within a JSON object.</p>
<p>For both the <code>json</code> and <code>bytes</code> content types, this means that they will be base64-encoded (<a href="https://datatracker.ietf.org/doc/html/rfc4648">RFC 4648</a>). The <code>text</code> type will be sent as a plain UTF-8 encoded string.</p>
<p>Your consumer will need to decode the <code>json</code> and <code>bytes</code> types before operating on the data.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Review the <a href="/api/resources/queues/subresources/consumers/methods/create/">REST API documentation</a> and schema for Queues.</li>
<li>Learn more about <a href="/fundamentals/api/how-to/make-api-calls/">how to make API calls</a> to the Cloudflare API.</li>
<li>Understand <a href="/queues/platform/limits/">what limit apply</a> when consuming and writing to a queue.</li>
</ul>
