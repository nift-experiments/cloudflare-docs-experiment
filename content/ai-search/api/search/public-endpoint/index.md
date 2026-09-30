<p>AI Search public endpoints allow you to expose AI Search capabilities without requiring authentication. This enables you to integrate AI Search into public-facing applications or share it with external users.</p>
<p>For pre-built search and chat components you can embed on your website using the public endpoints, refer to <a href="/ai-search/configuration/retrieval/public-endpoint/embed-search-snippets/">UI snippets</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Enable public endpoints for your AI Search instance:</p>
<ol>
<li>Go to <strong>AI Search</strong> in the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your AI Search instance.
3. Go to **Settings** > **Public Endpoint**.
4. Turn on **Enable Public Endpoint**.
5. Copy the public endpoint URL.
<p>For configuration options like rate limiting and CORS, refer to <a href="/ai-search/configuration/retrieval/public-endpoint/">Public endpoint configuration</a>.</p>
<h2 id="endpoint-hostnames">Endpoint hostnames</h2>
<p>You can enable a public endpoint on a single instance or on a whole <a href="/ai-search/configuration/retrieval/public-endpoint/namespace/">namespace</a>. A namespace endpoint serves the same three paths and searches across the instances you allow in that namespace, merging the results.</p>
<p>Cloudflare generates the hostname when you enable the endpoint:</p>
<table>
<thead>
<tr>
<th>Hostname</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com</code></td>
<td>Serves a single instance.</td>
</tr>
<tr>
<td><code>ns-&lt;NAMESPACE_ENDPOINT_ID&gt;.search.ai.cloudflare.com</code></td>
<td>Serves a <a href="/ai-search/configuration/retrieval/public-endpoint/namespace/">namespace</a>, searching across several instances.</td>
</tr>
</tbody>
</table>
<p>The request and response formats are identical for both. The examples on this page use the instance hostname.</p>
<h2 id="bring-your-own-domain">Bring your own domain</h2>
<p>You can serve the same endpoints from a hostname that you own, such as <code>search.example.com</code>, instead of the generated one:</p>
<pre><code class="language-txt">https://search.example.com/search&#10;https://search.example.com/chat/completions&#10;https://search.example.com/mcp&#10;</code></pre>
<p>The hostname must belong to a zone on the same Cloudflare account. To attach a custom domain:</p>
<ol>
<li>Go to <strong>AI Search</strong> in the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your instance or namespace.
3. Go to **Public Endpoints** and enable the public endpoint. A custom domain requires an active public endpoint.
4. Go to **Custom Domains** and attach your hostname.
<p>A custom domain routes requests through your own zone, so you can also put <a href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/">Cloudflare Access</a> in front of the endpoint and require callers to authenticate before they reach AI Search. Access only protects the custom hostname, so set <code>default_domain_enabled</code> to <code>false</code> as well. Otherwise the default <code>&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com</code> hostname keeps answering unauthenticated requests.</p>
<p>To attach a domain through the API instead, refer to <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">Custom domains</a>.</p>
<h2 id="chat-completions">Chat completions</h2>
<p>The <code>/chat/completions</code> endpoint searches your data source and generates a response using the model and retrieved context. It uses the same OpenAI-compatible format as the <a href="/ai-search/api/search/rest-api/#chat-completions">REST API</a>.</p>
<pre><code class="language-bash">curl https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/chat/completions \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;content&quot;: &quot;How do I configure AI Search?&quot;,&#10;        &quot;role&quot;: &quot;user&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>For the full list of options, refer to the <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/chat_completions/">Chat Completions API reference</a>.</p>
<h2 id="search">Search</h2>
<p>The <code>/search</code> endpoint returns relevant chunks from your data source without generating a response. It uses the same format as the <a href="/ai-search/api/search/rest-api/#search">REST API</a>.</p>
<pre><code class="language-bash">curl https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/search \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;content&quot;: &quot;How do I configure AI Search?&quot;,&#10;        &quot;role&quot;: &quot;user&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>For the full list of options, refer to the <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/search/">Search API reference</a>.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/ai-search/configuration/retrieval/public-endpoint/embed-search-snippets/">UI snippets</a> - Add pre-built search and chat components to your website.</li>
<li><a href="/ai-search/api/search/mcp/">MCP</a> - Connect AI agents using the Model Context Protocol.</li>
<li><a href="/ai-search/configuration/retrieval/public-endpoint/">Public endpoint configuration</a> - Configure rate limiting, CORS, and security settings.</li>
<li><a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">Custom domains</a> - Serve these endpoints from a hostname that you own.</li>
<li><a href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/">Cloudflare Access</a> - Require callers to authenticate before they reach these endpoints.</li>
</ul>
