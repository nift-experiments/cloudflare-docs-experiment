---
cp9:
  canonical: https://developers.cloudflare.com/r2/buckets/event-notifications/
  description: Send messages to Cloudflare Queues when objects in your R2 bucket change.
  full_title: Event notifications · Cloudflare R2 docs
  head_html: <title>Event notifications · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Send messages to Cloudflare Queues when objects in your R2 bucket change."><link rel="canonical" href="https://developers.cloudflare.com/r2/buckets/event-notifications/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/buckets/event-notifications/index.md"><meta property="og:title" content="Event notifications · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send messages to Cloudflare Queues when objects in your R2 bucket change."><meta property="og:url" content="https://developers.cloudflare.com/r2/buckets/event-notifications/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="R2,Queues"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/buckets/event-notifications/#page","headline":"Event notifications \u00b7 Cloudflare R2 docs","description":"Send messages to Cloudflare Queues when objects in your R2 bucket change.","url":"https://developers.cloudflare.com/r2/buckets/event-notifications/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/buckets/event-notifications/
  schema: 1
---
<p>Event notifications send messages to your <a href="/queues/">queue</a> when data in your R2 bucket changes. You can consume these messages with a <a href="/queues/reference/how-queues-works/#create-a-consumer-worker">consumer Worker</a> or <a href="/queues/configuration/pull-consumers/">pull over HTTP</a> from outside of Cloudflare Workers.</p>
<h2 id="get-started-with-event-notifications">Get started with event notifications</h2>
<h3 id="prerequisites">Prerequisites</h3>
<p>Before getting started, you will need:</p>
<ul>
<li>An existing R2 bucket. If you do not already have an existing R2 bucket, refer to <a href="/r2/buckets/create-buckets/">Create buckets</a>.</li>
<li>An existing queue. If you do not already have a queue, refer to <a href="/queues/get-started/#2-create-a-queue">Create a queue</a>.</li>
<li>A <a href="/queues/reference/how-queues-works/#create-a-consumer-worker">consumer Worker</a> or <a href="/queues/configuration/pull-consumers/">HTTP pull</a> enabled on your Queue.</li>
</ul>
<h3 id="enable-event-notifications-via-dashboard">Enable event notifications via Dashboard</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select the bucket you'd like to add an event notification rule to.
3. Switch to the **Settings** tab, then scroll down to the **Event notifications** card.
4. Select **Add notification** and choose the queue you'd like to receive notifications and the [type of events](/r2/buckets/event-notifications/#event-types) that will trigger them.
5. Select **Add notification**.
<h3 id="enable-event-notifications-via-wrangler">Enable event notifications via Wrangler</h3>
<h4 id="set-up-wrangler">Set up Wrangler</h4>
<p>To begin, install <a href="https://docs.npmjs.com/getting-started"><code>npm</code></a>. Then <a href="/workers/wrangler/install-and-update/">install Wrangler, the Developer Platform CLI</a>.</p>
<h4 id="enable-event-notifications-on-your-r2-bucket">Enable event notifications on your R2 bucket</h4>
<p>Log in to Wrangler with the <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code> command</a>. Then add an <a href="/r2/buckets/event-notifications/#event-notification-rules">event notification rule</a> to your bucket by running the <a href="/workers/wrangler/commands/r2/#r2-bucket-notification-create"><code>r2 bucket notification create</code> command</a>.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket notification create &lt;BUCKET_NAME&gt; --event-type &lt;EVENT_TYPE&gt; --queue &lt;QUEUE_NAME&gt;&#10;</code></pre>
<p>To add filtering based on <code>prefix</code> or <code>suffix</code> use the <code>--prefix</code> or <code>--suffix</code> flag, respectively.</p>
<pre tabindex="0"><code class="language-sh">&#35; Filter using prefix&#10;$ npx wrangler r2 bucket notification create &lt;BUCKET_NAME&gt; --event-type &lt;EVENT_TYPE&gt; --queue &lt;QUEUE_NAME&gt; --prefix &quot;&lt;PREFIX_VALUE&gt;&quot;&#10;&#10;&#35; Filter using suffix&#10;$ npx wrangler r2 bucket notification create &lt;BUCKET_NAME&gt; --event-type &lt;EVENT_TYPE&gt; --queue &lt;QUEUE_NAME&gt; --suffix &quot;&lt;SUFFIX_VALUE&gt;&quot;&#10;&#10;&#35; Filter using prefix and suffix. Both the conditions will be used for filtering&#10;$ npx wrangler r2 bucket notification create &lt;BUCKET_NAME&gt; --event-type &lt;EVENT_TYPE&gt; --queue &lt;QUEUE_NAME&gt; --prefix &quot;&lt;PREFIX_VALUE&gt;&quot; --suffix &quot;&lt;SUFFIX_VALUE&gt;&quot;&#10;</code></pre>
<p>For a more complete step-by-step example, refer to the <a href="/r2/tutorials/upload-logs-event-notifications/">Log and store upload events in R2 with event notifications</a> example.</p>
<h2 id="event-notification-rules">Event notification rules</h2>
<p>Event notification rules determine the <a href="/r2/buckets/event-notifications/#event-types">event types</a> that trigger notifications and optionally enable filtering based on object <code>prefix</code> and <code>suffix</code>. You can have up to 100 event notification rules per R2 bucket.</p>
<h2 id="event-types">Event types</h2>
<table>
<thead>
<tr>
<th>Event type</th>
<th>Description</th>
<th>Trigger actions</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>object-create</code></td>
<td>Triggered when new objects are created or existing objects are overwritten.</td>
<td><ul><li><code>PutObject</code></li><li><code>CopyObject</code></li><li><code>CompleteMultipartUpload</code></li></ul></td>
</tr>
<tr>
<td><code>object-delete</code></td>
<td>Triggered when an object is explicitly removed from the bucket.</td>
<td><ul><li><code>DeleteObject</code></li><li><code>LifecycleDeletion</code></li></ul></td>
</tr>
</tbody>
</table>
<h2 id="message-format">Message format</h2>
<p>Queue consumers receive notifications as <a href="/queues/configuration/javascript-apis/#message">Messages</a>. The following is an example of the body of a message that a consumer Worker will receive:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;account&quot;: &quot;3f4b7e3dcab231cbfdaa90a6a28bd548&quot;,&#10;	&quot;action&quot;: &quot;CopyObject&quot;,&#10;	&quot;bucket&quot;: &quot;my-bucket&quot;,&#10;	&quot;object&quot;: {&#10;		&quot;key&quot;: &quot;my-new-object&quot;,&#10;		&quot;size&quot;: 65536,&#10;		&quot;eTag&quot;: &quot;c846ff7a18f28c2e262116d6e8719ef0&quot;&#10;	},&#10;	&quot;eventTime&quot;: &quot;2024-05-24T19:36:44.379Z&quot;,&#10;	&quot;copySource&quot;: {&#10;		&quot;bucket&quot;: &quot;my-bucket&quot;,&#10;		&quot;object&quot;: &quot;my-original-object&quot;&#10;	}&#10;}&#10;</code></pre>
<h3 id="properties">Properties</h3>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>account</code></td>
<td>String</td>
<td>The Cloudflare account ID that the event is associated with.</td>
</tr>
<tr>
<td><code>action</code></td>
<td>String</td>
<td>The type of action that triggered the event notification. Example actions include: <code>PutObject</code>, <code>CopyObject</code>, <code>CompleteMultipartUpload</code>, <code>DeleteObject</code>.</td>
</tr>
<tr>
<td><code>bucket</code></td>
<td>String</td>
<td>The name of the bucket where the event occurred.</td>
</tr>
<tr>
<td><code>object</code></td>
<td>Object</td>
<td>A nested object containing details about the object involved in the event.</td>
</tr>
<tr>
<td><code>object.key</code></td>
<td>String</td>
<td>The key (or name) of the object within the bucket.</td>
</tr>
<tr>
<td><code>object.size</code></td>
<td>Number</td>
<td>The size of the object in bytes. Note: not present for object-delete events.</td>
</tr>
<tr>
<td><code>object.eTag</code></td>
<td>String</td>
<td>The entity tag (eTag) of the object. Note: not present for object-delete events.</td>
</tr>
<tr>
<td><code>eventTime</code></td>
<td>String</td>
<td>The time when the action that triggered the event occurred.</td>
</tr>
<tr>
<td><code>copySource</code></td>
<td>Object</td>
<td>A nested object containing details about the source of a copied object. Note: only present for events triggered by <code>CopyObject</code>.</td>
</tr>
<tr>
<td><code>copySource.bucket</code></td>
<td>String</td>
<td>The bucket that contained the source object.</td>
</tr>
<tr>
<td><code>copySource.object</code></td>
<td>String</td>
<td>The name of the source object.</td>
</tr>
</tbody>
</table>
<h2 id="notes">Notes</h2>
<ul>
<li>Queues <a href="/queues/platform/limits/">per-queue message throughput</a> is currently 5,000 messages per second. If your workload produces more than 5,000 notifications per second, we recommend splitting notification rules across multiple queues.</li>
<li>Rules without prefix/suffix apply to all objects in the bucket.</li>
<li>Overlapping or conflicting rules that could trigger multiple notifications for the same event are not allowed. For example, if you have an <code>object-create</code> (or <code>PutObject</code> action) rule without a prefix and suffix, then adding another <code>object-create</code> (or <code>PutObject</code> action) rule with a prefix like <code>images/</code> could trigger more than one notification for a single upload, which is invalid.</li>
</ul>
