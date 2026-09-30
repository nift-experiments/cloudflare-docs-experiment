<p><a href="https://www.anthropic.com/">Anthropic</a> helps build reliable, interpretable, and steerable AI systems.</p>
<h2 id="endpoint">Endpoint</h2>
**Base URL**
<pre><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/anthropic&#10;</code></pre>
<h2 id="examples">Examples</h2>
<h3 id="curl">cURL</h3>
<details class="nb-details"><summary>With API Key in Request</summary><div class="nb-details-body">
@input("content/.markup/bodies/2988.md")
</div></details>
<details class="nb-details" open><summary>With Stored Keys (BYOK) / Unified Billing</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2989.md")
</div></details>
<h3 id="anthropic-sdk">Anthropic SDK</h3>
<details class="nb-details"><summary>With Key in Request</summary><div class="nb-details-body">
@input("content/.markup/bodies/2993.md")
</div></details>
<details class="nb-details" open><summary>With Stored Keys (BYOK) / Unified Billing</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/2995.md")
</div></details>
<h2 id="openai-compatible-endpoint">OpenAI-Compatible Endpoint</h2>
<p>You can also access Anthropic models using the OpenAI API schema through the <a href="/ai-gateway/usage/rest-api/">REST API</a>. Send your requests to:</p>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions&#10;</code></pre>
<p>Specify:</p>
<pre><code class="language-json">{&#10;		&amp;quot;model&amp;quot;: &amp;quot;anthropic/{model}&amp;quot;&#10;}</code></pre>
