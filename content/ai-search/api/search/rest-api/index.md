<p>Use the AI Search REST API to query your AI Search instances over HTTP.</p>
<h2 id="authentication">Authentication</h2>
<p>All requests require an API token with <strong>AI Search:Edit</strong> and <strong>AI Search:Run</strong> permissions.</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create Token</strong>.</li>
<li>Select <strong>Create Custom Token</strong>.</li>
<li>Enter a <strong>Token name</strong>, for example <code>AI Search Manager</code>.</li>
<li>Under <strong>Permissions</strong>, add two permissions:
<ul>
<li><strong>Account</strong> &gt; <strong>AI Search:Edit</strong></li>
<li><strong>Account</strong> &gt; <strong>AI Search:Run</strong></li>
</ul>
</li>
<li>Select <strong>Continue to summary</strong>, then select <strong>Create Token</strong>.</li>
<li>Copy and save the token value. This is your <code>API_TOKEN</code>.</li>
</ol>
<p>Include the token in the <code>Authorization</code> header for all requests:</p>
<pre><code class="language-txt">Authorization: Bearer &lt;API_TOKEN&gt;&#10;</code></pre>
<h2 id="search-and-chat">Search and chat</h2>
<p>AI Search provides two APIs for querying an instance. Both use an OpenAI-compatible <code>messages</code> format.</p>
<ul>
<li><strong>Search</strong> returns relevant content chunks. Use this when you want to handle generation yourself or display results directly.</li>
<li><strong>Chat completions</strong> retrieves content and generates a response in one call.</li>
</ul>
<h3 id="api-paths">API paths</h3>
<p>Search and chat APIs are scoped to a <a href="/ai-search/concepts/namespaces/">namespace</a>:</p>
<table>
<thead>
<tr>
<th>Path</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/accounts/{account_id}/ai-search/namespaces/{namespace}/instances/{id}/</code></td>
<td>Operates on a specific instance within a namespace</td>
</tr>
</tbody>
</table>
<p>Every account has a <code>default</code> namespace. Use <code>default</code> unless you created a custom namespace. For the full specification, refer to the <a href="/api/resources/ai_search/subresources/namespaces/">Namespace API reference</a>.</p>
<h3 id="search">Search</h3>
<p>Search a specific instance. The search endpoint also accepts a <code>query</code> string parameter. For the full specification, refer to the <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/search/">Search API reference</a>.</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/&lt;INSTANCE_NAME&gt;/search&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;,&#10;        &quot;role&quot;: &quot;user&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h3 id="chat-completions">Chat completions</h3>
<p>Generate a response from a specific instance. For the full specification, refer to the <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/chat_completions/">Chat completions API reference</a>.</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/&lt;INSTANCE_NAME&gt;/chat/completions&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;,&#10;        &quot;role&quot;: &quot;user&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h4 id="streaming">Streaming</h4>
<p>Set <code>stream</code> to <code>true</code> to receive responses as Server-Sent Events (SSE). The retrieved chunks are sent first as a <code>chunks</code> event, followed by the streamed response.</p>
<pre><code class="language-txt">event: chunks&#10;data: [{&quot;id&quot;:&quot;chunk-001&quot;,&quot;type&quot;:&quot;text&quot;,&quot;score&quot;:0.85,&quot;text&quot;:&quot;...&quot;,&quot;item&quot;:{&quot;key&quot;:&quot;about-cloudflare.md&quot;,&quot;timestamp&quot;:1775925540000},&quot;scoring_details&quot;:{&quot;vector_score&quot;:0.85}}]&#10;&#10;data: {&quot;id&quot;:&quot;id-1776072781845&quot;,&quot;created&quot;:1776072781,&quot;model&quot;:&quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&quot;object&quot;:&quot;chat.completion.chunk&quot;,&quot;choices&quot;:[{&quot;index&quot;:0,&quot;delta&quot;:{&quot;content&quot;:&quot; document&quot;}}]}&#10;&#10;data: {&quot;id&quot;:&quot;id-1776072781845&quot;,&quot;created&quot;:1776072781,&quot;model&quot;:&quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&quot;object&quot;:&quot;chat.completion.chunk&quot;,&quot;choices&quot;:[{&quot;index&quot;:0,&quot;delta&quot;:{&quot;content&quot;:&quot; you provided doesn&quot;}}]}&#10;&#10;data: {&quot;id&quot;:&quot;id-1776072781845&quot;,&quot;created&quot;:1776072781,&quot;model&quot;:&quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&quot;object&quot;:&quot;chat.completion.chunk&quot;,&quot;choices&quot;:[{&quot;index&quot;:0,&quot;delta&quot;:{&quot;content&quot;:&quot;&#x27;t contain&quot;}}]}&#10;&#10;data: {&quot;id&quot;:&quot;id-1776072781845&quot;,&quot;created&quot;:1776072781,&quot;model&quot;:&quot;@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&quot;object&quot;:&quot;chat.completion.chunk&quot;,&quot;choices&quot;:[{&quot;index&quot;:0,&quot;delta&quot;:{&quot;content&quot;:&quot; information&quot;}}]}&#10;&#10;data: [DONE]&#10;</code></pre>
<h2 id="cross-instance-search-and-chat">Cross-instance search and chat</h2>
<p>The search and chat completions APIs are also available at the namespace level. These work the same as the instance endpoints, but you pass an <code>instance_ids</code> array to specify which instances to query. Each chunk in the response includes an <code>instance_id</code> field identifying which instance it came from. For the full specification, refer to the <a href="/api/resources/ai_search/subresources/namespaces/">Namespace API reference</a>.</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/&lt;NAMESPACE&gt;/search&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;      }&#10;    ],&#10;    &quot;ai_search_options&quot;: {&#10;      &quot;instance_ids&quot;: [&quot;product-docs&quot;, &quot;customer-abc123&quot;]&#10;    }&#10;  }&#x27;&#10;</code></pre>
