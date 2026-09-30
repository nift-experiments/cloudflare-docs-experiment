---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/api/alarms/
  description: Schedule future wake-ups for Durable Objects using the Alarms API with guaranteed at-least-once execution.
  full_title: Alarms · Cloudflare Durable Objects docs
  head_html: <title>Alarms · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="Schedule future wake-ups for Durable Objects using the Alarms API with guaranteed at-least-once execution."><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/api/alarms/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/api/alarms/index.md"><meta property="og:title" content="Alarms · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Schedule future wake-ups for Durable Objects using the Alarms API with guaranteed at-least-once execution."><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/api/alarms/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/durable-objects/api/alarms/#page","headline":"Alarms \u00b7 Cloudflare Durable Objects docs","description":"Schedule future wake-ups for Durable Objects using the Alarms API with guaranteed at-least-once execution.","url":"https://developers.cloudflare.com/durable-objects/api/alarms/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /durable-objects/api/alarms/
  schema: 1
---
<h2 id="background">Background</h2>
<p>Durable Objects alarms allow you to schedule the Durable Object to be woken up at a time in the future. When the alarm's scheduled time comes, the <code>alarm()</code> handler method will be called. Alarms are modified using the <span class="nb-glossary-tooltip" title="Storage API">Storage API</span>, and alarm operations follow the same rules as other storage operations.</p>
<p>Notably:</p>
<ul>
<li>Each Durable Object is able to schedule a single alarm at a time by calling <code>setAlarm()</code>.</li>
<li>Alarms have guaranteed at-least-once execution and are retried automatically when the <code>alarm()</code> handler throws.</li>
<li>Retries are performed using exponential backoff starting at a 2 second delay from the first failure with up to 6 retries allowed.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="how-are-alarms-different-from-cron-triggers">How are alarms different from Cron Triggers?</h3>
@markup("md", "content/.markup/bodies/8425.md")
</aside>
<p>Alarms can be used to build distributed primitives, like queues or batching of work atop Durable Objects. Alarms also provide a mechanism to guarantee that operations within a Durable Object will complete without relying on incoming requests to keep the Durable Object alive. For a complete example, refer to <a href="/durable-objects/examples/alarms-api/">Use the Alarms API</a>.</p>
<h2 id="scheduling-multiple-events-with-a-single-alarm">Scheduling multiple events with a single alarm</h2>
<p>Although each Durable Object can only have one alarm set at a time, you can manage many scheduled and recurring events by storing your event schedule in storage and having the <code>alarm()</code> handler process due events, then reschedule itself for the next one.</p>
<pre tabindex="0"><code class="language-js">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;export class AgentServer extends DurableObject {&#10;  // Schedule a one-time or recurring event&#10;  async scheduleEvent(id, runAt, repeatMs = null) {&#10;    await this.ctx.storage.put(`event:${id}`, { id, runAt, repeatMs });&#10;    const currentAlarm = await this.ctx.storage.getAlarm();&#10;    if (!currentAlarm || runAt &lt; currentAlarm) {&#10;      await this.ctx.storage.setAlarm(runAt);&#10;    }&#10;  }&#10;&#10;  async alarm() {&#10;    const now = Date.now();&#10;    const events = await this.ctx.storage.list({ prefix: &quot;event:&quot; });&#10;    let nextAlarm = null;&#10;&#10;    for (const [key, event] of events) {&#10;      if (event.runAt &lt;= now) {&#10;        await this.processEvent(event);&#10;        if (event.repeatMs) {&#10;          event.runAt = now + event.repeatMs;&#10;          await this.ctx.storage.put(key, event);&#10;        } else {&#10;          await this.ctx.storage.delete(key);&#10;        }&#10;      }&#10;      // Track the next event time&#10;      if (event.runAt &gt; now &amp;&amp; (!nextAlarm || event.runAt &lt; nextAlarm)) {&#10;        nextAlarm = event.runAt;&#10;      }&#10;    }&#10;&#10;    if (nextAlarm) await this.ctx.storage.setAlarm(nextAlarm);&#10;  }&#10;&#10;  async processEvent(event) {&#10;    // Your event handling logic here&#10;  }&#10;}&#10;</code></pre>
<h2 id="storage-methods">Storage methods</h2>
<h3 id="getalarm"><code>getAlarm</code></h3>
<ul>
<li>
<p><code>getAlarm()</code>: <span class="nb-type">number | null</span></p>
<ul>
<li>
<p>If there is an alarm set, then return the currently set alarm time as the number of milliseconds elapsed since the UNIX epoch. Otherwise, return <code>null</code>.</p>
</li>
<li>
<p>If <code>getAlarm</code> is called while an <a href="/durable-objects/api/alarms/#alarm"><code>alarm</code></a> is already running, it returns <code>null</code> unless <code>setAlarm</code> has also been called since the alarm handler started running.</p>
</li>
</ul>
</li>
</ul>
<h3 id="setalarm"><code>setAlarm</code></h3>
<ul>
<li>
<p><code> setAlarm(scheduledTimeMs <span class="nb-type">number</span>) </code>: <span class="nb-type">void</span></p>
<ul>
<li>Set the time for the alarm to run. Specify the time as the number of milliseconds elapsed since the UNIX epoch.</li>
<li>If you call <code>setAlarm</code> when there is already one scheduled, it will override the existing alarm.</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="calling-setalarm-inside-the-constructor">Calling `setAlarm` inside the constructor</h3>
@markup("md", "content/.markup/bodies/8424.md")
</aside>
<h3 id="deletealarm"><code>deleteAlarm</code></h3>
<ul>
<li>
<p><code>deleteAlarm()</code>: <span class="nb-type">void</span></p>
<ul>
<li>
<p>Unset the alarm if there is a currently set alarm.</p>
</li>
<li>
<p>Calling <code>deleteAlarm()</code> inside the <code>alarm()</code> handler may prevent retries on a best-effort basis, but is not guaranteed.</p>
</li>
</ul>
</li>
</ul>
<h2 id="handler-methods">Handler methods</h2>
<h3 id="alarm"><code>alarm</code></h3>
<ul>
<li>
<p><code>alarm(alarmInfo <span class="nb-type">Object</span>)</code>: <span class="nb-type">void</span></p>
<ul>
<li>
<p>Called by the system when a scheduled alarm time is reached.</p>
</li>
<li>
<p>The optional parameter <code>alarmInfo</code> object has two properties:</p>
<ul>
<li><code>retryCount</code> <span class="nb-type">number</span>: The number of times this alarm event has been retried.</li>
<li><code>isRetry</code> <span class="nb-type">boolean</span>: A boolean value to indicate if the alarm has been retried. This value is <code>true</code> if this alarm event is a retry.</li>
</ul>
</li>
<li>
<p>Only one instance of <code>alarm()</code> will ever run at a given time per Durable Object instance.</p>
</li>
<li>
<p>The <code>alarm()</code> handler has guaranteed at-least-once execution and will be retried upon failure using exponential backoff, starting at 2 second delays for up to 6 retries. This only applies to the most recent <code>setAlarm()</code> call. Retries will be performed if the method fails with an uncaught exception.</p>
</li>
<li>
<p>This method can be <code>async</code>.</p>
</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="catching-exceptions-in-alarm-handlers">Catching exceptions in alarm handlers</h3>
@markup("md", "content/.markup/bodies/8423.md")
</aside>
<h2 id="example">Example</h2>
<p>This example shows how to both set alarms with the <code>setAlarm(timestamp)</code> method and handle alarms with the <code>alarm()</code> handler within your Durable Object.</p>
<ul>
<li>The <code>alarm()</code> handler will be called once every time an alarm fires.</li>
<li>If an unexpected error terminates the Durable Object, the <code>alarm()</code> handler may be re-instantiated on another machine.</li>
<li>Following a short delay, the <code>alarm()</code> handler will run from the beginning on the other machine.</li>
</ul>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8429.md")
</div></div>
<p>The following example shows how to use the <code>alarmInfo</code> property to identify if the alarm event has been attempted before.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8432.md")
</div></div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>Understand how to <a href="/durable-objects/examples/alarms-api/">use the Alarms API</a> in an end-to-end example.</li>
<li>Read the <a href="https://blog.cloudflare.com/durable-objects-alarms/">Durable Objects alarms announcement blog post</a>.</li>
<li>Review the <a href="/durable-objects/api/sqlite-storage-api/">Storage API</a> documentation for Durable Objects.</li>
</ul>
