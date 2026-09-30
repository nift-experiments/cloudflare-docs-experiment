<p>Use messengers when a Think agent should receive and reply to Chat SDK webhooks directly. Think owns the webhook route, durable reply fiber, conversation routing, and streamed delivery back to the provider.</p>
<h2 id="install">Install</h2>
<p>Install the Think package and the provider adapter you use:</p>
<pre><code class="language-sh">npm install @cloudflare/think agents ai @chat-adapter/telegram&#10;</code></pre>
<p>Provider adapters are exported from provider-specific subpaths so unused adapters are not bundled into your Worker.</p>
<h2 id="telegram">Telegram</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2143.md")
</div>
<p>With the default <code>telegram</code> key, register the Telegram webhook at:</p>
<pre><code class="language-text">https://&lt;your-worker&gt;/messengers/telegram/webhook&#10;</code></pre>
<p><code>telegramMessenger()</code> requires <code>secretToken</code> in webhook mode unless you pass a custom <code>verifyWebhook</code> function or explicitly opt out with <code>verifyWebhook: false</code>.</p>
<p>If one Think agent owns multiple Telegram bots, give each provider a distinct Chat SDK adapter name:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2144.md")
</div>
<p>Duplicate adapter names fail during startup so providers cannot overwrite each other in the shared Chat SDK runtime.</p>
<h2 id="routing">Routing</h2>
<p>The root Think agent handles messenger webhook routes after framework sub-agent routing and Think internal routes, but before user-defined <code>onRequest</code> fallback. Messenger routes are root-only. Defining <code>getMessengers()</code> on a sub-agent class does not create webhook routes for that sub-agent.</p>
<p>By default, Think replies to direct messages and mentions. New mentions subscribe the Chat SDK thread so later mentions in the same thread are still observed, but ordinary subscribed-thread messages and button actions are ignored unless you opt in:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2145.md")
</div>
<p>Action events are converted into Think user messages with the action id, value, source message id, and initiating user. Use <code>getMessengerContext()?.action</code> inside hooks or tools when you need provider-specific action details. Actions are opt-in so interactive cards do not accidentally trigger model turns.</p>
<h2 id="conversation-targets">Conversation targets</h2>
<p>The default conversation mode is one Think sub-agent per Chat SDK thread. This keeps group chats, direct messages, and channels from sharing memory accidentally.</p>
<p>Use the root agent as the conversation when all messenger traffic should share one Think session:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2146.md")
</div>
<p>Use a resolver when routing depends on tenant, channel, thread, or user:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2147.md")
</div>
<h2 id="state">State</h2>
<p>Messenger state is backed by <code>agents/chat-sdk</code>. Export <code>ThinkMessengerStateAgent</code> from the Worker module so sub-agent routing can resolve it. Production applications do not need a separate Durable Object binding or migration for this facet-only state class. Test harnesses may still need explicit bindings.</p>
<h2 id="delivery-and-recovery">Delivery and recovery</h2>
<p>Think replies with the streamed <code>chat()</code> path. The root agent starts an idempotent managed fiber, resolves the conversation target, calls <code>target.chat(message, callback)</code>, and lets the provider delivery policy post or edit visible messages.</p>
<p>Recovery snapshots store only serializable event and Chat SDK thread data. If a restart happens before streaming starts, Think can replay the answer. If a restart happens after streaming starts, Think posts the configured interruption message instead of risking a duplicate partial answer.</p>
<p>Delivery errors use a generic user-facing message by default so internal exception details are not posted into external chats. Override <code>delivery.errorResponseText</code> when you want a custom safe message.</p>
<h2 id="messenger-context">Messenger context</h2>
<p>During a messenger turn, <code>getMessengerContext()</code> returns provider, thread, author, message, capabilities, and attachment metadata for the initiating event. Use it from prompts, tools, or hooks that need channel-specific behavior.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2148.md")
</div>
<h2 id="custom-chat-sdk-adapters">Custom Chat SDK adapters</h2>
<p>Use <code>chatSdkMessenger()</code> for providers that do not have a Think helper yet:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2149.md")
</div>
<p>Every custom messenger must provide <code>verifyWebhook</code> or explicitly use <code>verifyWebhook: false</code>.</p>
<h2 id="advanced-manual-ingress">Advanced manual ingress</h2>
<p>The <code>examples/think-chat-sdk</code> example demonstrates the Think-native <code>getMessengers()</code> path with a small Vite dashboard that inspects the root Think conversation over the Agent WebSocket.</p>
<p>The <code>examples/chat-sdk-messenger</code> example demonstrates a larger manual ingress agent with an admin dashboard, menu handling, and application-owned reply fibers. Use <code>getMessengers()</code> for the simple Think-native path. Use the example when you need to own the Chat SDK runtime and control-plane UI yourself. Refer to <a href="/agents/runtime/communication/chat-sdk/">Chat SDK state</a> for the underlying state adapter.</p>
