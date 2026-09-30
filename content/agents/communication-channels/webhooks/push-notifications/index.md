---
cp9:
  canonical: https://developers.cloudflare.com/agents/communication-channels/webhooks/push-notifications/
  description: Send browser push notifications from a Cloudflare Agent, even when the user has closed the tab.
  full_title: Push notifications · Cloudflare Agents docs
  head_html: <title>Push notifications · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Send browser push notifications from a Cloudflare Agent, even when the user has closed the tab."><link rel="canonical" href="https://developers.cloudflare.com/agents/communication-channels/webhooks/push-notifications/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/communication-channels/webhooks/push-notifications/index.md"><meta property="og:title" content="Push notifications · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send browser push notifications from a Cloudflare Agent, even when the user has closed the tab."><meta property="og:url" content="https://developers.cloudflare.com/agents/communication-channels/webhooks/push-notifications/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/communication-channels/webhooks/push-notifications/#page","headline":"Push notifications \u00b7 Cloudflare Agents docs","description":"Send browser push notifications from a Cloudflare Agent, even when the user has closed the tab.","url":"https://developers.cloudflare.com/agents/communication-channels/webhooks/push-notifications/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/communication-channels/webhooks/push-notifications/
  schema: 1
---
<p>Send browser push notifications from your agent — even when the user has closed the tab. By combining the agent's persistent state (for storing push subscriptions), scheduling (for timed delivery), and the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Push_API">Web Push API</a>, you can reach users who are completely offline.</p>
<h2 id="how-it-works">How it works</h2>
<pre tabindex="0"><code>Browser                              Agent (Durable Object)&#10;───────                              ──────────────────────&#10;1. Register service worker&#10;2. Subscribe to push (VAPID key)&#10;3. Send subscription to agent ──────► Store in this.state&#10;4. Create reminder ─────────────────► this.schedule(delay, &quot;sendReminder&quot;, payload)&#10;&#10;   ... user closes tab ...&#10;&#10;5.                                    Alarm fires → sendReminder()&#10;                                      web-push sends encrypted payload&#10;                                              │&#10;6. Service worker receives push ◄─────────────┘&#10;7. showNotification()&#10;</code></pre>
<p>The agent stores push subscriptions durably in its state and uses <code>this.schedule()</code> to fire notifications at the right time. When the alarm triggers, the agent calls the push service endpoint using the <a href="https://www.npmjs.com/package/web-push"><code>web-push</code></a> library. The browser's service worker receives the push event and displays a native notification.</p>
<h2 id="prerequisites">Prerequisites</h2>
<h3 id="generate-vapid-keys">Generate VAPID keys</h3>
<p>Web Push requires a VAPID (Voluntary Application Server Identification) key pair. Generate one:</p>
<pre tabindex="0"><code class="language-bash">npx web-push generate-vapid-keys&#10;</code></pre>
<p>Store the keys in a <code>.env</code> file for local development:</p>
<pre tabindex="0"><code>VAPID_PUBLIC_KEY=BGxK...&#10;VAPID_PRIVATE_KEY=abc1...&#10;VAPID_SUBJECT=mailto:you@example.com&#10;</code></pre>
<p>For production, use <code>wrangler secret put</code>:</p>
<pre tabindex="0"><code class="language-bash">wrangler secret put VAPID_PUBLIC_KEY&#10;wrangler secret put VAPID_PRIVATE_KEY&#10;wrangler secret put VAPID_SUBJECT&#10;</code></pre>
<h2 id="create-the-agent">Create the agent</h2>
<p>The agent has three responsibilities: store push subscriptions, schedule reminders, and send notifications when alarms fire.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1984.md")
</div>
<p>The <code>sendReminder</code> callback handles three things: delivering the push notification via the <code>web-push</code> library, cleaning up dead subscriptions (the push service returns 404 or 410 when a subscription is no longer valid), and broadcasting to any connected clients so the UI updates in real time.</p>
<h2 id="set-up-the-service-worker">Set up the service worker</h2>
<p>The service worker runs in the browser and receives push events even when no tabs are open. Place this file at <code>public/sw.js</code> so it is served from the root of your domain:</p>
<pre tabindex="0"><code class="language-js">self.addEventListener(&quot;push&quot;, (event) =&gt; {&#10;	if (!event.data) return;&#10;&#10;	const data = event.data.json();&#10;&#10;	event.waitUntil(&#10;		self.registration.showNotification(data.title || &quot;Notification&quot;, {&#10;			body: data.body || &quot;&quot;,&#10;			icon: data.icon || &quot;/favicon.ico&quot;,&#10;			tag: data.tag,&#10;			data: data.data,&#10;		}),&#10;	);&#10;});&#10;&#10;self.addEventListener(&quot;notificationclick&quot;, (event) =&gt; {&#10;	event.notification.close();&#10;&#10;	event.waitUntil(&#10;		self.clients.matchAll({ type: &quot;window&quot; }).then((windowClients) =&gt; {&#10;			for (const client of windowClients) {&#10;				if (&#10;					client.url.includes(self.location.origin) &amp;&amp;&#10;					&quot;focus&quot; in client&#10;				) {&#10;					return client.focus();&#10;				}&#10;			}&#10;			return self.clients.openWindow(&quot;/&quot;);&#10;		}),&#10;	);&#10;});&#10;</code></pre>
<p>The <code>push</code> event handler parses the JSON payload and displays a native notification. The <code>notificationclick</code> handler focuses an existing tab or opens a new one when the user taps the notification.</p>
<h2 id="build-the-client">Build the client</h2>
<p>The client needs to: register the service worker, request notification permission, subscribe to push using the VAPID public key, and send the subscription to the agent.</p>
<h3 id="register-the-service-worker">Register the service worker</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1985.md")
</div>
<h3 id="subscribe-to-push">Subscribe to push</h3>
<p>Fetch the VAPID public key from the agent, then subscribe through the Push API:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1986.md")
</div>
<h3 id="create-reminders">Create reminders</h3>
<p>With the subscription stored, creating a reminder is a single RPC call. The agent handles scheduling and delivery:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1987.md")
</div>
<p>The agent schedules an alarm for 300 seconds (5 minutes). When it fires, the push notification arrives — even if the user closed the tab minutes ago.</p>
<h2 id="configuration">Configuration</h2>
<h3 id="wrangler-jsonc">wrangler.jsonc</h3>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;name&quot;: &quot;push-notifications&quot;,&#10;	&quot;compatibility_date&quot;: &quot;2026-01-28&quot;,&#10;	&quot;compatibility_flags&quot;: [&quot;nodejs_compat&quot;],&#10;	&quot;main&quot;: &quot;src/server.ts&quot;,&#10;	&quot;durable_objects&quot;: {&#10;		&quot;bindings&quot;: [&#10;			{ &quot;name&quot;: &quot;ReminderAgent&quot;, &quot;class_name&quot;: &quot;ReminderAgent&quot; },&#10;		],&#10;	},&#10;	&quot;migrations&quot;: [{ &quot;tag&quot;: &quot;v1&quot;, &quot;new_sqlite_classes&quot;: [&quot;ReminderAgent&quot;] }],&#10;	&quot;assets&quot;: {&#10;		&quot;not_found_handling&quot;: &quot;single-page-application&quot;,&#10;	},&#10;}&#10;</code></pre>
<p>The <code>nodejs_compat</code> compatibility flag is required for the <code>web-push</code> library.</p>
<h3 id="dependencies">Dependencies</h3>
<pre tabindex="0"><code class="language-bash">npm install agents web-push&#10;</code></pre>
<h2 id="production-considerations">Production considerations</h2>
<h3 id="subscription-expiry">Subscription expiry</h3>
<p>Push subscriptions can expire or be revoked by the user. Always handle 404 and 410 responses from the push service by removing the dead subscription from state, as shown in the <code>sendReminder</code> example above.</p>
<h3 id="per-user-vs-shared-agents">Per-user vs shared agents</h3>
<p>For most applications, use one agent per user (using the user ID as the agent name). This isolates each user's subscriptions and reminders. For broadcast-style notifications (same message to many users), a shared agent can store all subscriptions, but be aware of the state size as the subscription list grows.</p>
<h3 id="combining-push-with-websocket-broadcast">Combining push with WebSocket broadcast</h3>
<p>Use <code>this.broadcast()</code> for clients that are currently connected (instant, no push service roundtrip) and Web Push for clients that are offline. The <code>sendReminder</code> example above does both — connected clients get a real-time WebSocket message, and offline clients get a push notification.</p>
<h3 id="multiple-devices">Multiple devices</h3>
<p>A single user may subscribe from multiple browsers or devices. The agent stores each subscription separately, and <code>sendReminder</code> iterates over all of them. Each device receives its own push notification.</p>
<h3 id="retry-on-failure">Retry on failure</h3>
<p>If the push service returns a 5xx error (temporary failure), you can retry using <code>this.schedule()</code> with a short delay:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1988.md")
</div>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-schedule-tasks-agents-runtime-execution-schedule-tasks"><a href="/agents/runtime/execution/schedule-tasks/">Schedule tasks</a></h3><p>Learn about scheduling and keepAlive for long-running operations.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-store-and-sync-state-agents-runtime-lifecycle-state"><a href="/agents/runtime/lifecycle/state/">Store and sync state</a></h3><p>Manage agent state for storing subscriptions.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-callable-methods-agents-runtime-lifecycle-callable-methods"><a href="/agents/runtime/lifecycle/callable-methods/">Callable methods</a></h3><p>Expose agent methods as RPC endpoints.</p></div>
