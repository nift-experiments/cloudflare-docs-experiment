<p>AI Security for Apps (formerly Firewall for AI) provides an estimated token count for each incoming LLM prompt. This lets you monitor prompt sizes, set limits on overly long prompts, and track token usage across your AI endpoints.</p>
<h2 id="how-token-counting-works">How token counting works</h2>
<p>When AI Security for Apps processes a request to a <code>cf-llm</code> labeled endpoint, it calculates an approximate token count for the prompt content. The result is available in the <strong>LLM Token count</strong> (<a href="/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.token_count/"><code>cf.llm.prompt.token_count</code></a>) field, which you can reference in rule expressions and view in analytics.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15559.md")
</aside>
<h2 id="use-cases">Use cases</h2>
<h3 id="block-oversized-prompts">Block oversized prompts</h3>
<p>Set a hard threshold to block prompts that exceed a certain estimated token count. This prevents unexpectedly large inputs from reaching your model.</p>
<ul>
<li>
<p><strong>When incoming requests match</strong>:</p>
<p>Enter the following expression in the editor:<br/>
<code>(cf.llm.prompt.token_count gt 4000)</code></p>
</li>
<li>
<p><strong>Action</strong>: <em>Block</em></p>
</li>
</ul>
<h3 id="rate-limit-large-prompts">Rate limit large prompts</h3>
<p>Create a <a href="/waf/rate-limiting-rules/">rate limiting rule</a> that restricts the number of large prompts a single client can send within a time window. This helps prevent abuse where attackers send excessively long prompts to consume model resources.</p>
<p>Enter the following rule expression in the editor:<br/>
<code>(cf.llm.prompt.token_count gt 2000)</code></p>
<p>Set the rate to, for example, 10 requests per minute per IP, with an action of <em>Block</em> or <em>Managed Challenge</em>.</p>
<h3 id="combine-token-count-with-other-detections">Combine token count with other detections</h3>
<p>Target large prompts that also show signs of prompt injection — a common pattern where attackers pad injection attempts with long context.</p>
<p>Example rule expression:<br/>
<code>(cf.llm.prompt.token_count gt 3000 and cf.llm.prompt.injection_score lt 50)</code></p>
<h2 id="important-considerations">Important considerations</h2>
<ul>
<li><strong>Estimate only.</strong> The token count is a general approximation. Actual token consumption at your model may differ depending on the model's tokenizer.</li>
<li><strong>Input tokens only.</strong> The token count reflects the incoming prompt. It does not estimate output or response tokens.</li>
<li><strong>Extracted prompt only.</strong> The token count is calculated on the prompt text extracted from the request body. Cloudflare extracts the prompt using a set of known JSON paths for major LLM providers. When the prompt cannot be extracted, Cloudflare uses the full request body as a fallback. In these situations, token count will reflect the full request body.</li>
</ul>
