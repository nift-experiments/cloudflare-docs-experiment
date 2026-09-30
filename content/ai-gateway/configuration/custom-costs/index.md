<p>AI Gateway allows you to set custom costs at the request level. Custom costs can reflect your negotiated input, output, cache-read, and cache-write rates. They override the default or public model costs.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/2885.md")
</aside>
<h2 id="custom-cost">Custom cost</h2>
<p>To add custom costs to your API requests, use the <code>cf-aig-custom-cost</code> header. This header supports the following properties:</p>
<ul>
<li><code>per_token_in</code>: Cost per input token.</li>
<li><code>per_token_out</code>: Cost per output token.</li>
<li><code>per_cache_read_token</code>: Cost per cache-read token.</li>
<li><code>per_cache_write_token</code>: Cost per cache-write token.</li>
</ul>
<p>There is no limit to the number of decimal places you can include, ensuring precise cost calculations, regardless of how small the values are.</p>
<p>Cache-token pricing is optional. To turn it on, specify at least one cache rate. If you specify only one cache rate, the other defaults to <code>per_token_in</code>. If you omit both cache rates, AI Gateway ignores cache-token counts and uses the existing input and output calculation.</p>
<h2 id="cache-token-calculations">Cache-token calculations</h2>
<p>Providers report cache usage in different ways. Some include cache-read and cache-write tokens within the input token count. Others report input and cache tokens as separate counts.</p>
<p>AI Gateway automatically accounts for how each provider and model reports cache usage. When cache tokens are included in the input count, AI Gateway subtracts them before applying <code>per_token_in</code>. When cache tokens are reported separately, AI Gateway applies their costs in addition to the input cost. This prevents cache tokens from being double-counted.</p>
<p>For example, an inclusive response reports the following usage:</p>
<ul>
<li>1,000 input tokens</li>
<li>600 cache-read tokens</li>
<li>200 cache-write tokens</li>
<li>100 output tokens</li>
</ul>
<p>AI Gateway calculates 200 fresh input tokens: <code>1,000 - 600 - 200</code>. It then applies each custom rate to its corresponding token count.</p>
<p>Custom costs will appear in the logs with an underline, making it easy to identify when custom pricing has been applied.</p>
<p>In this example, the negotiated prices are $1 per million input tokens, $2 per million output tokens, $0.10 per million cache-read tokens, and $0.50 per million cache-write tokens.</p>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai/chat/completions \&#10;  &#45;-header &quot;Authorization: Bearer $TOKEN&quot; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-header &#x27;cf-aig-custom-cost: {&quot;per_token_in&quot;:0.000001,&quot;per_token_out&quot;:0.000002,&quot;per_cache_read_token&quot;:0.0000001,&quot;per_cache_write_token&quot;:0.0000005}&#x27; \&#10;  &#45;-data &#x27; {&#10;        &quot;model&quot;: &quot;gpt-4o-mini&quot;,&#10;        &quot;messages&quot;: [&#10;          {&#10;            &quot;role&quot;: &quot;user&quot;,&#10;            &quot;content&quot;: &quot;When is Cloudflare’s Birthday Week?&quot;&#10;          }&#10;        ]&#10;      }&#x27;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2884.md")
</aside>
