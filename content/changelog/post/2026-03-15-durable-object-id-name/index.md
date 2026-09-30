<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 15, 2026</time><h2 id="post-title">Access Durable Object name via `ctx.id.name`</h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>When your Worker accesses a Durable Object via <code>idFromName()</code> or <code>getByName()</code>, the same name is now available on <code>ctx.id.name</code> inside the object — no need to pass it through method arguments or persist it in storage. This brings the runtime behavior in line with the <a href="/workers/languages/typescript/">Workers runtime types</a>.</p>
<p>This is especially useful for <a href="/durable-objects/api/alarms/">alarms</a>, where there is no calling client to pass the name as an argument. When an alarm handler runs, <code>ctx.id.name</code> will hold the same name the object was originally accessed with.</p>
<pre><code class="language-js">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;export class ChatRoom extends DurableObject {&#10;  async getRoomName() {&#10;    // ctx.id.name returns the name passed to getByName() or idFromName()&#10;    return this.ctx.id.name;&#10;  }&#10;}&#10;&#10;// Worker&#10;export default {&#10;  async fetch(request, env) {&#10;    const stub = env.CHAT_ROOM.getByName(&quot;general&quot;);&#10;    const roomName = await stub.getRoomName();&#10;    return new Response(`Welcome to ${roomName}!`);&#10;  },&#10;};&#10;</code></pre>
<p><code>ctx.id.name</code> is <code>undefined</code> in the following cases:</p>
<ul>
<li>For Durable Objects created with <code>newUniqueId()</code>.</li>
<li>When accessed via <code>idFromString()</code>, even if the ID was originally created from a name.</li>
<li>For <a href="/durable-objects/api/id/#name">names longer than 1,024 bytes</a>.</li>
</ul>
<p>This works the same way in local development with <code>wrangler dev</code> as it does in production. Run <code>npm update wrangler</code> to ensure you are on a version with this support.</p>
<p>For more information, refer to the <a href="/durable-objects/api/id/#name">Durable Object ID documentation</a>.</p>
</div></article></div>
