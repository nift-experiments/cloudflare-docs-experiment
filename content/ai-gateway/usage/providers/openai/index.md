<p><a href="https://openai.com/about/">OpenAI</a> helps you build with GPT models.</p>
<h2 id="endpoint">Endpoint</h2>
<p><strong>Base URL</strong></p>
<pre><code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai&#10;</code></pre>
<p>When making requests to OpenAI, replace <code>https://api.openai.com/v1</code> in the URL you are currently using with <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai</code>.</p>
<p><strong>Chat completions endpoint</strong></p>
<p><code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions</code></p>
<p><strong>Responses endpoint</strong></p>
<p><code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/responses</code></p>
<h2 id="examples">Examples</h2>
<h3 id="openai-sdk">OpenAI SDK</h3>
<details class="nb-details"><summary>With Key in Request</summary><div class="nb-details-body">
@input("content/.markup/bodies/2958.md")
</div></details>
<details class="nb-details" open><summary>With Stored Keys (BYOK) / Unified Billing</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2959.md")
</div></details>
<h3 id="curl">cURL</h3>
<details class="nb-details"><summary>Responses API with API Key in Request</summary><div class="nb-details-body">
@input("content/.markup/bodies/2963.md")
</div></details>
<details class="nb-details"><summary>Chat Completions with API Key in Request</summary><div class="nb-details-body">
@input("content/.markup/bodies/2967.md")
</div></details>
<details class="nb-details"><summary>Responses API with Stored Keys (BYOK) / Unified Billing</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2968.md")
</div></details>
<details class="nb-details" open><summary>Chat Completions with Stored Keys (BYOK) / Unified Billing</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2969.md")
</div></details>
