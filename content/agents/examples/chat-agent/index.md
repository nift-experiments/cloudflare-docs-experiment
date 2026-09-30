<p>Build a chat agent that streams AI responses, calls server-side tools, executes client-side tools in the browser, and asks for user approval before sensitive actions.</p>
<p><strong>What you will build:</strong> A chat agent powered by Workers AI with three tool types — automatic, client-side, and approval-gated.</p>
<p><strong>Time:</strong> ~15 minutes</p>
<p>This tutorial starts from a minimal Hello World Worker so you can see each moving part. If you want a complete starter app with the same core pieces already wired together, start with the <a href="/agents/getting-started/quick-start/">quick start</a> and then return here to understand how the chat pieces fit together.</p>
<p><strong>Prerequisites:</strong></p>
<ul>
<li>Node.js 18+</li>
<li>A Cloudflare account (free tier works)</li>
</ul>
<h2 id="1-create-the-project"><ol>
<li>Create the project</li>
</ol></h2>
<pre><code class="language-sh">npm create cloudflare@latest chat-agent&#10;</code></pre>
<p>Select <strong>&quot;Hello World&quot; Worker</strong> when prompted. Then install the dependencies:</p>
<pre><code class="language-sh">cd chat-agent&#10;npm install agents @cloudflare/ai-chat ai workers-ai-provider zod&#10;</code></pre>
<h2 id="2-configure-wrangler"><ol start="2">
<li>Configure Wrangler</li>
</ol></h2>
<p>Replace your <code>wrangler.jsonc</code> with:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1926.md")
</div>
<p>Key settings:</p>
<ul>
<li><code>ai</code> binds Workers AI — no API key needed</li>
<li><code>durable_objects</code> registers your chat agent class</li>
<li><code>new_sqlite_classes</code> enables SQLite storage for message persistence</li>
</ul>
<h2 id="3-write-the-server"><ol start="3">
<li>Write the server</li>
</ol></h2>
<p>Create <code>src/server.ts</code>. This is where your agent lives:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1927.md")
</div>
<h3 id="what-each-tool-type-does">What each tool type does</h3>
<table>
<thead>
<tr>
<th>Tool</th>
<th><code>execute</code>?</th>
<th><code>needsApproval</code>?</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>getWeather</code></td>
<td>Yes</td>
<td>No</td>
<td>Runs on the server automatically</td>
</tr>
<tr>
<td><code>getUserTimezone</code></td>
<td>No</td>
<td>No</td>
<td>Sent to the client; browser provides the result</td>
</tr>
<tr>
<td><code>calculate</code></td>
<td>Yes</td>
<td>Yes (large numbers)</td>
<td>Pauses for user approval, then runs on server</td>
</tr>
</tbody>
</table>
<h2 id="4-write-the-client"><ol start="4">
<li>Write the client</li>
</ol></h2>
<p>Create <code>src/client.tsx</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1928.md")
</div>
<h3 id="key-client-concepts">Key client concepts</h3>
<ul>
<li><strong><code>useAgent</code></strong> connects to your <code>ChatAgent</code> over WebSocket</li>
<li><strong><code>useAgentChat</code></strong> manages the chat lifecycle (messages, streaming, tools)</li>
<li><strong><code>onToolCall</code></strong> handles client-side tools — when the LLM calls <code>getUserTimezone</code>, the browser provides the result and the conversation auto-continues</li>
<li><strong><code>addToolApprovalResponse</code></strong> approves or rejects tools that have <code>needsApproval</code></li>
<li>Messages, streaming, and resumption are all handled automatically</li>
</ul>
<h2 id="5-run-locally"><ol start="5">
<li>Run locally</li>
</ol></h2>
<p>Generate types and start the dev server:</p>
<pre><code class="language-sh">npx wrangler types&#10;npm run dev&#10;</code></pre>
<p>Try these prompts:</p>
<ul>
<li><strong>&quot;What is the weather in Tokyo?&quot;</strong> — calls the server-side <code>getWeather</code> tool</li>
<li><strong>&quot;What timezone am I in?&quot;</strong> — calls the client-side <code>getUserTimezone</code> tool (the browser provides the answer)</li>
<li><strong>&quot;What is 5000 times 3?&quot;</strong> — triggers the approval UI before executing (numbers over 1000)</li>
</ul>
<h2 id="6-deploy"><ol start="6">
<li>Deploy</li>
</ol></h2>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Your agent is now live on Cloudflare's global network. Messages persist in SQLite, streams resume on disconnect, and the agent hibernates when idle to save resources.</p>
<h2 id="what-you-built">What you built</h2>
<p>Your chat agent has:</p>
<ul>
<li><strong>Streaming AI responses</strong> via Workers AI (no API keys)</li>
<li><strong>Message persistence</strong> in SQLite — conversations survive restarts</li>
<li><strong>Server-side tools</strong> that execute automatically</li>
<li><strong>Client-side tools</strong> that run in the browser and feed results back to the LLM</li>
<li><strong>Human-in-the-loop approval</strong> for sensitive operations</li>
<li><strong>Resumable streaming</strong> — if a client disconnects mid-stream, it picks up where it left off</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/communication-channels/chat/chat-agents/"><h3 id="card-chat-agents-api-reference-agents-communication-channels-chat-chat-agents">Chat agents API reference</h3><p>Full reference for AIChatAgent and useAgentChat — providers, storage, advanced patterns.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/lifecycle/state/"><h3 id="card-store-and-sync-state-agents-runtime-lifecycle-state">Store and sync state</h3><p>Add real-time state beyond chat messages.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/lifecycle/callable-methods/"><h3 id="card-callable-methods-agents-runtime-lifecycle-callable-methods">Callable methods</h3><p>Expose agent methods as typed RPC for your client.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/concepts/agentic-patterns/human-in-the-loop/"><h3 id="card-human-in-the-loop-agents-concepts-agentic-patterns-human-in-the-loop">Human-in-the-loop</h3><p>Deeper patterns for approval flows and manual intervention.</p></a></p>
