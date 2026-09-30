<p><a href="https://replicate.com/">Replicate</a> runs and fine tunes open-source models.</p>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/replicate&#10;</code></pre>
<h2 id="url-structure">URL structure</h2>
<p>When making requests to Replicate, replace <code>https://api.replicate.com/v1</code> in the URL you're currently using with <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/replicate</code>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to Replicate, ensure you have the following:</p>
<ul>
<li>Your AI Gateway Account ID.</li>
<li>Your AI Gateway gateway name.</li>
<li>An active Replicate API token. You can create one at <a href="https://replicate.com/account/api-tokens">replicate.com/account/api-tokens</a></li>
<li>The name of the Replicate model you want to use, like <code>anthropic/claude-4.5-haiku</code> or <code>google/nano-banana</code>.</li>
</ul>
<h2 id="example">Example</h2>
<h3 id="curl">cURL</h3>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/replicate/predictions \&#10;  &#45;-header &#x27;Authorization: Bearer {replicate_api_token}&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;version&quot;: &quot;anthropic/claude-4.5-haiku&quot;,&#10;    &quot;input&quot;:&#10;      {&#10;        &quot;prompt&quot;: &quot;Write a haiku about Cloudflare&quot;&#10;      }&#10;    }&#x27;&#10;</code></pre>
