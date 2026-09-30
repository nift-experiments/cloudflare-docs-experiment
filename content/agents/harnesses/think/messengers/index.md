---
cp9:
  canonical: https://developers.cloudflare.com/agents/harnesses/think/messengers/
  description: Receive and reply to Chat SDK messenger webhooks directly from a Think agent, including Telegram setup, routing, conversation targets, and recovery.
  full_title: Messengers · Cloudflare Agents docs
  head_html: <title>Messengers · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Receive and reply to Chat SDK messenger webhooks directly from a Think agent, including Telegram setup, routing, conversation targets, and recovery."><link rel="canonical" href="https://developers.cloudflare.com/agents/harnesses/think/messengers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/harnesses/think/messengers/index.md"><meta property="og:title" content="Messengers · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Receive and reply to Chat SDK messenger webhooks directly from a Think agent, including Telegram setup, routing, conversation targets, and recovery."><meta property="og:url" content="https://developers.cloudflare.com/agents/harnesses/think/messengers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/harnesses/think/messengers/#page","headline":"Messengers \u00b7 Cloudflare Agents docs","description":"Receive and reply to Chat SDK messenger webhooks directly from a Think agent, including Telegram setup, routing, conversation targets, and recovery.","url":"https://developers.cloudflare.com/agents/harnesses/think/messengers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/harnesses/think/messengers/
  schema: 1
---
<p>Use messengers when a Think agent should receive and reply to Chat SDK webhooks directly. Think owns the webhook route, durable reply fiber, conversation routing, and streamed delivery back to the provider.</p>
<h2 id="install">Install</h2>
<p>Install the Think package and the provider adapter you use:</p>
<pre tabindex="0"><code class="language-sh">npm install @cloudflare/think agents ai @chat-adapter/telegram&#10;</code></pre>
<p>Provider adapters are exported from provider-specific subpaths so unused adapters are not bundled into your Worker.</p>
<h2 id="telegram">Telegram</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2143.md")
</div>
<p>With the default <code>telegram</code> key, register the Telegram webhook at:</p>
<pre tabindex="0"><code class="language-text">https://&lt;your-worker&gt;/messengers/telegram/webhook&#10;</code></pre>
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
