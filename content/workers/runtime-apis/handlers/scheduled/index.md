<h2 id="background">Background</h2>
<p>When a Worker is invoked via a <a href="/workers/configuration/cron-triggers/">Cron Trigger</a>, the <code>scheduled()</code> handler handles the invocation.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="testing-scheduled-handlers-in-local-development">Testing scheduled() handlers in local development</h3>
@markup("md", "content/.markup/bodies/17168.md")
</aside>
<hr />
<h2 id="syntax">Syntax</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17172.md")
</div></div>
<h3 id="properties">Properties</h3>
<ul>
<li><code>controller.cron</code> string
<ul>
<li>The value of the <a href="/workers/configuration/cron-triggers/">Cron Trigger</a> that started the <code>ScheduledEvent</code>.</li>
</ul>
</li>
<li><code>controller.type</code> string
<ul>
<li>The type of controller. This will always return <code>&quot;scheduled&quot;</code>.</li>
</ul>
</li>
<li><code>controller.scheduledTime</code> number
<ul>
<li>The time the <code>ScheduledEvent</code> was scheduled to be executed in milliseconds since January 1, 1970, UTC. It can be parsed as <code>new Date(controller.scheduledTime)</code>.</li>
</ul>
</li>
<li><code>env</code> object
<ul>
<li>An object containing the bindings associated with your Worker using ES modules format, such as KV namespaces and Durable Objects.</li>
</ul>
</li>
<li><code>ctx</code> object
<ul>
<li>An object containing the context associated with your Worker using ES modules format. Currently, this object just contains the <code>waitUntil</code> function.</li>
</ul>
</li>
</ul>
<h3 id="handle-multiple-cron-triggers">Handle multiple cron triggers</h3>
<p>When you configure multiple <a href="/workers/configuration/cron-triggers/">Cron Triggers</a> for a single Worker, each trigger invokes the same <code>scheduled()</code> handler. Use <code>controller.cron</code> to distinguish which schedule fired and run different logic for each.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17173.md")
</div>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17177.md")
</div></div>
<p>The value of <code>controller.cron</code> is the exact cron expression string from your configuration. It must match character-for-character, including spacing.</p>
<h3 id="methods">Methods</h3>
<p>When a Workers script is invoked by a <a href="/workers/configuration/cron-triggers/">Cron Trigger</a>, the Workers runtime starts a <code>ScheduledEvent</code> which will be handled by the <code>scheduled</code> function in your Workers Module class. The <code>ctx</code> argument represents the context your function runs in, and contains the following methods to control what happens next:</p>
<ul>
<li><code>ctx.waitUntil(promise)</code> : void - Use this method to
register asynchronous tasks (for example, logging, analytics to third-party
services, streaming and caching) that should settle before the invocation
completes. The first <code>ctx.waitUntil</code> to fail will be observed and recorded as
the status in the <a href="/workers/configuration/cron-triggers/">Cron Trigger</a> Past
Events table. Otherwise, it will be reported as a success.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17167.md")
</aside>
