<p>Agents can call AI models from any provider. <a href="/workers-ai/">Workers AI</a> is built in and requires no API keys. You can also use <a href="https://platform.openai.com/docs/quickstart?language=javascript">OpenAI</a>, <a href="https://docs.anthropic.com/en/api/client-sdks#typescript">Anthropic</a>, <a href="https://ai.google.dev/gemini-api/docs/openai">Google Gemini</a>, or any service that exposes an OpenAI-compatible API.</p>
<p>The <a href="https://ai-sdk.dev/docs/introduction">AI SDK</a> provides a unified interface across all of these providers, and is what <code>AIChatAgent</code> and the starter template use under the hood. You can also use the model routing features in <a href="/ai-gateway/">AI Gateway</a> to route across providers, eval responses, and manage rate limits.</p>
<h2 id="calling-ai-models">Calling AI Models</h2>
<p>You can call models from any method within an Agent, including from HTTP requests using the <a href="/agents/runtime/agents-api/"><code>onRequest</code></a> handler, when a <a href="/agents/runtime/execution/schedule-tasks/">scheduled task</a> runs, when handling a WebSocket message in the <a href="/agents/runtime/communication/websockets/"><code>onMessage</code></a> handler, or from any of your own methods.</p>
<p>Agents can call AI models on their own — autonomously — and can handle long-running responses that take minutes (or longer) to respond in full. If a client disconnects mid-stream, the Agent keeps running and can catch the client up when it reconnects.</p>
<h3 id="streaming-over-websockets-long-running-model-requests">Streaming over WebSockets </h3>
<p>Modern reasoning models can take some time to both generate a response <em>and</em> stream the response back to the client. Instead of buffering the entire response, you can stream it back over <a href="/agents/runtime/communication/websockets/">WebSockets</a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2292.md")
</div>
<p>You can also persist AI model responses back to <a href="/agents/runtime/lifecycle/state/">Agent state</a> using <code>this.setState</code>. If a user disconnects, read the message history back and send it to the user when they reconnect.</p>
<h2 id="workers-ai">Workers AI</h2>
<p>You can use <a href="/workers-ai/models/">any of the models available in Workers AI</a> within your Agent by <a href="/workers-ai/configuration/bindings/">configuring a binding</a>. No API keys are required.</p>
<p>Workers AI supports streaming responses by setting <code>stream: true</code>. Use streaming to avoid buffering and delaying responses, especially for larger models or reasoning models.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2293.md")
</div>
<p>Your Wrangler configuration needs an <code>ai</code> binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2294.md")
</div>
<h3 id="model-routing">Model routing</h3>
<p>You can use <a href="/ai-gateway/">AI Gateway</a> directly from an Agent by specifying a <a href="/ai-gateway/usage/providers/workersai/"><code>gateway</code> configuration</a> when calling the AI binding. Model routing lets you route requests across providers based on availability, rate limits, or cost budgets.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2295.md")
</div>
<p>The <code>ai</code> binding in your Wrangler configuration is shared across both Workers AI and AI Gateway.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2296.md")
</div>
<p>Visit the <a href="/ai-gateway/">AI Gateway documentation</a> to learn how to configure a gateway and retrieve a gateway ID.</p>
<h2 id="ai-sdk">AI SDK</h2>
<p>The <a href="https://ai-sdk.dev/docs/introduction">AI SDK</a> provides a unified API for text generation, tool calling, structured responses, and more. It works with any provider that has an AI SDK adapter, including Workers AI via <a href="https://www.npmjs.com/package/workers-ai-provider"><code>workers-ai-provider</code></a>.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i ai workers-ai-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i ai workers-ai-provider" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add ai workers-ai-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add ai workers-ai-provider" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add ai workers-ai-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add ai workers-ai-provider" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add ai workers-ai-provider</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add ai workers-ai-provider" aria-label="Copy to clipboard">Copy</button></div></div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2297.md")
</div>
<p>You can swap the provider to use OpenAI, Anthropic, or any other AI SDK-compatible adapter:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i ai @ai-sdk/openai</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i ai @ai-sdk/openai" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add ai @ai-sdk/openai</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add ai @ai-sdk/openai" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add ai @ai-sdk/openai</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add ai @ai-sdk/openai" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add ai @ai-sdk/openai</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add ai @ai-sdk/openai" aria-label="Copy to clipboard">Copy</button></div></div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2298.md")
</div>
<h2 id="openai-compatible-endpoints">OpenAI-compatible endpoints</h2>
<p>Agents can call models across any service that supports the OpenAI API. For example, you can use the OpenAI SDK to call one of <a href="https://ai.google.dev/gemini-api/docs/openai#node.js">Google's Gemini models</a> directly from your Agent.</p>
<p>Agents can stream responses back over HTTP using Server-Sent Events (SSE) from within an <code>onRequest</code> handler, or by using the native <a href="/agents/runtime/communication/websockets/">WebSocket API</a> to stream responses back to a client.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2299.md")
</div>
