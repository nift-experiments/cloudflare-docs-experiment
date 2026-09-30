<p>Use <code>agents/chat-sdk</code> when you run the <a href="https://chat-sdk.dev/">Chat SDK</a> inside an Agent. The first integration helper is a Chat SDK <code>StateAdapter</code> that stores state in Agents sub-agents.</p>
<p>The adapter stores Chat SDK subscriptions, locks, queues, dedupe keys, thread state, channel state, callback metadata, transcript lists, and thread history in Durable Object SQLite. Each state shard is a <code>ChatSdkStateAgent</code> sub-agent under your ingress Agent.</p>
<h2 id="install">Install</h2>
<p>Install both packages in the Worker that hosts your messenger ingress:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents chat</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents chat" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents chat</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents chat" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents chat</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents chat" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents chat</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents chat" aria-label="Copy to clipboard">Copy</button></div></div>
<p><code>agents/chat-sdk</code> provides durable state for Chat SDK. Use it with any Chat SDK adapter, such as Telegram, Slack, Discord, Teams, or Google Chat.</p>
<h2 id="basic-setup">Basic setup</h2>
<p>Create a parent Agent that owns your Chat SDK runtime. Pass <code>createChatSdkState()</code> as the Chat SDK <code>state</code> option.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2637.md")
</div>
<p>Add the parent Agent to your Durable Object migration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2638.md")
</div>
<p>Export <code>ChatSdkStateAgent</code> from your Worker entry point so sub-agent routing can resolve it. When <code>createChatSdkState()</code> is called inside an Agent lifecycle method or request handler, it uses the current Agent as the parent and creates state shards with <code>this.subAgent()</code>.</p>
<h2 id="state-sharding">State sharding</h2>
<p>By default, Chat SDK state is sharded by the first two colon-separated segments of a thread-like key.</p>
<p>For example, <code>telegram:-100123:456</code> and <code>telegram:-100123:789</code> share the same state shard, <code>telegram:-100123</code>.</p>
<p>The default key sharder recognizes these Chat SDK key prefixes:</p>
<ul>
<li><code>thread-state:</code></li>
<li><code>channel-state:</code></li>
<li><code>msg-history:</code></li>
<li><code>transcripts:user:</code></li>
</ul>
<p>Unknown keys use the adapter's default shard name, <code>default</code>.</p>
<h2 id="custom-sharding">Custom sharding</h2>
<p>Use <code>shardKey</code> to control how thread IDs map to state sub-agent names:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2639.md")
</div>
<p>Use <code>keyShard</code> when an adapter stores non-thread-shaped keys that should still route to a provider-specific shard:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2640.md")
</div>
<p>Returning <code>undefined</code> falls back to the built-in key sharder and then to the default shard.</p>
<h2 id="api">API</h2>
<h3 id="createchatsdkstate-options"><code>createChatSdkState(options)</code></h3>
<p>Creates a Chat SDK <code>StateAdapter</code> backed by a <code>ChatSdkStateAgent</code> sub-agent.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2641.md")
</div>
<p>Options:</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>agent</code></td>
<td>Optional custom subclass of <code>ChatSdkStateAgent</code>. Defaults to <code>ChatSdkStateAgent</code>.</td>
</tr>
<tr>
<td><code>parent</code></td>
<td>Optional parent Agent that will call <code>subAgent()</code> to create state shards. Defaults to the current Agent from <code>getCurrentAgent()</code>.</td>
</tr>
<tr>
<td><code>name</code></td>
<td>Default shard name for keys that cannot be mapped. Defaults to <code>default</code>.</td>
</tr>
<tr>
<td><code>shardKey</code></td>
<td>Maps Chat SDK thread IDs and lock keys to a shard name.</td>
</tr>
<tr>
<td><code>keyShard</code></td>
<td>Maps generic Chat SDK cache or list keys to a shard name.</td>
</tr>
</tbody>
</table>
<h3 id="chatsdkstateagent"><code>ChatSdkStateAgent</code></h3>
<p>The sub-agent class that stores state in SQLite. Export it from your Worker entry point so the runtime can create it.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2642.md")
</div>
<h3 id="chatsdkstateadapter"><code>ChatSdkStateAdapter</code></h3>
<p>The concrete <code>StateAdapter</code> implementation returned by <code>createChatSdkState()</code>. Most applications do not need to instantiate it directly.</p>
<h2 id="what-is-stored">What is stored</h2>
<p>The adapter implements the full Chat SDK <code>StateAdapter</code> interface:</p>
<ul>
<li>Subscriptions for <code>thread.subscribe()</code> and <code>thread.unsubscribe()</code>.</li>
<li>Locks for per-thread or per-channel concurrency.</li>
<li>Pending message queues for <code>queue</code>, <code>debounce</code>, and <code>burst</code> concurrency strategies.</li>
<li>Generic key-value cache entries with optional TTL.</li>
<li>Append-only lists with max-length trimming and list-level TTL refresh.</li>
</ul>
<p>Chat SDK features built on these primitives include:</p>
<ul>
<li>Message deduplication.</li>
<li>Thread and channel state.</li>
<li>Persistent thread history for adapters that opt in to <code>persistThreadHistory</code>.</li>
<li>Callback URL token storage.</li>
<li>Modal context storage.</li>
<li>Cross-platform transcripts.</li>
</ul>
<h2 id="cleanup-behavior">Cleanup behavior</h2>
<p>TTL reads are strict: expired locks, cache values, queue entries, and list entries are ignored or deleted before they are returned.</p>
<p>Physical cleanup is lazy. <code>ChatSdkStateAgent</code> schedules one cleanup callback for the earliest known expiry and reschedules after cleanup runs. This keeps idle shards quiet while preventing expired rows from accumulating indefinitely.</p>
<h2 id="example">Example</h2>
<p><a class="nb-card nb-link-card" href="https://github.com/cloudflare/agents/tree/main/examples/chat-sdk-messenger"><h3 id="card-chat-sdk-messenger-example-https-github-com-cloudflare-agents-tree-main-examples-chat-sdk-messenger">Chat SDK messenger example</h3><p>Build a Telegram messenger bot with Chat SDK state in sub-agents, burst/debounce concurrency, and Think-backed AI replies running in managed fibers.</p></a></p>
