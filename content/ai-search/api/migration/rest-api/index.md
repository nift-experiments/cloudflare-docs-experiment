<p>The <a href="/api/resources/autorag/">AutoRAG API endpoints</a> are the legacy REST API for AI Search. They will continue to work, but all new features and improvements are only available through the new <a href="/ai-search/api/search/rest-api/">AI Search API endpoints</a>.</p>
<h2 id="endpoint-changes">Endpoint changes</h2>
<p>The legacy AutoRAG API endpoints under <code>/autorag/rags/</code> have been replaced by new endpoints under <code>/ai-search/namespaces/{namespace}/instances/</code>.</p>
<table>
<thead>
<tr>
<th>Description</th>
<th>New endpoint</th>
<th>Reference</th>
</tr>
</thead>
<tbody>
<tr>
<td>Chat completions</td>
<td><code>/ai-search/namespaces/{namespace}/instances/{id}/chat/completions</code></td>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/chat_completions/">API reference</a></td>
</tr>
<tr>
<td>Search</td>
<td><code>/ai-search/namespaces/{namespace}/instances/{id}/search</code></td>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/search/">API reference</a></td>
</tr>
</tbody>
</table>
<p>The new API also includes endpoints for <a href="/ai-search/api/instances/rest-api/">instance management</a>, <a href="/ai-search/api/items/rest-api/">items</a>, and <a href="/ai-search/api/search/rest-api/#cross-instance-search-and-chat">namespace-level search</a> that are not available in the legacy API. For the legacy endpoints, refer to the <a href="/api/resources/autorag/">AutoRAG API reference</a>.</p>
<h2 id="api-token-permissions">API token permissions</h2>
<p>The legacy AutoRAG endpoints used the <strong>AutoRAG</strong> API token permission. The new AI Search endpoints require the <strong>AI Search</strong> permission instead, so update the permissions on the token you use to call the API. We recommend using <a href="/fundamentals/api/get-started/account-owned-tokens/">account API tokens</a>, which are owned by the account rather than a single user, and adding the <strong>AI Search</strong> permission found under <strong>AI &amp; Machine Learning</strong> &gt; <strong>AI Search</strong>.</p>
<h3 id="create-a-new-token">Create a new token</h3>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Manage Account</strong> &gt; <strong>API Tokens</strong>.</li>
<li>Select <strong>Create Token</strong>, then start a custom token.</li>
<li>Enter a name for the token.</li>
<li>Add a permission policy and select <strong>AI &amp; Machine Learning</strong> &gt; <strong>AI Search</strong>, then choose the access level you need. AI Search offers <strong>Read</strong>, <strong>Run</strong>, and <strong>Edit</strong> access.</li>
<li>(Optional) Set client IP address filtering and a token expiration.</li>
<li>Create the token and copy its value.</li>
</ol>
<h3 id="edit-an-existing-token">Edit an existing token</h3>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Manage Account</strong> &gt; <strong>API Tokens</strong>.</li>
<li>Select the token you want to update.</li>
<li>Add or update a permission policy to include <strong>AI &amp; Machine Learning</strong> &gt; <strong>AI Search</strong> with the access level you need, then save.</li>
</ol>
<p>For the full token creation flow, refer to <a href="/fundamentals/api/get-started/create-token/">Create API token</a>.</p>
<h2 id="chat-completions">Chat completions</h2>
<p>How to migrate from the AutoRAG <code>/ai-search</code> endpoint to the new <code>/chat/completions</code> endpoint:</p>
<p><strong>Before (AutoRAG API):</strong></p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/autorag/rags/&lt;INSTANCE_NAME&gt;/ai-search&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;query&quot;: &quot;What is Cloudflare?&quot;&#10;  }&#x27;&#10;</code></pre>
<p><strong>After (AI Search API):</strong></p>
<p>The new API uses the <code>messages</code> array format.</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/&lt;INSTANCE_NAME&gt;/chat/completions&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;,&#10;        &quot;role&quot;: &quot;user&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h2 id="search">Search</h2>
<p>How to migrate from the AutoRAG <code>/search</code> endpoint to the new <code>/search</code> endpoint:</p>
<p><strong>Before (AutoRAG API):</strong></p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/autorag/rags/&lt;INSTANCE_NAME&gt;/search&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;query&quot;: &quot;What is Cloudflare?&quot;&#10;  }&#x27;&#10;</code></pre>
<p><strong>After (AI Search API):</strong></p>
<p>The new API uses the <code>messages</code> array format. The <code>query</code> string format is also supported.</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/&lt;INSTANCE_NAME&gt;/search&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;,&#10;        &quot;role&quot;: &quot;user&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h2 id="streaming-behavior-changes">Streaming behavior changes</h2>
<p>In the old AutoRAG API, when <code>stream</code> was set to <code>true</code>, you would only receive the streamed response without the retrieved chunks.</p>
<p>In the new AI Search API, streaming responses include the chunks. The retrieved chunks are sent first as a <code>chunks</code> event, followed by the streamed response data. This allows you to display the source chunks immediately while streaming the generated response to the user.</p>
<h2 id="filter-format">Filter format</h2>
<p>The new AI Search REST API uses Vectorize-style metadata filtering, which differs from the AutoRAG API format. Filters are now nested under <code>ai_search_options.retrieval.filters</code> in the request body. For full documentation of the old format, refer to <a href="/ai-search/api/migration/autorag-filter-format/">Metadata filter format (legacy)</a>.</p>
<h3 id="operator-mapping">Operator mapping</h3>
<p>The filter operators have been renamed to use a <code>$</code> prefix:</p>
<table>
<thead>
<tr>
<th>AutoRAG API</th>
<th>AI Search API</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>eq</code></td>
<td><code>$eq</code> (or implicit)</td>
</tr>
<tr>
<td><code>ne</code></td>
<td><code>$ne</code></td>
</tr>
<tr>
<td><code>gt</code></td>
<td><code>$gt</code></td>
</tr>
<tr>
<td><code>gte</code></td>
<td><code>$gte</code></td>
</tr>
<tr>
<td><code>lt</code></td>
<td><code>$lt</code></td>
</tr>
<tr>
<td><code>lte</code></td>
<td><code>$lte</code></td>
</tr>
<tr>
<td></td>
<td><code>$in</code> (new)</td>
</tr>
<tr>
<td></td>
<td><code>$nin</code> (new)</td>
</tr>
</tbody>
</table>
<h3 id="examples">Examples</h3>
<h4 id="simple-filter">Simple filter</h4>
<p>Filter by a single metadata field using implicit equality:</p>
<p><strong>Before (AutoRAG API):</strong></p>
<pre><code class="language-json">{&#10;	&quot;filters&quot;: {&#10;		&quot;type&quot;: &quot;eq&quot;,&#10;		&quot;key&quot;: &quot;folder&quot;,&#10;		&quot;value&quot;: &quot;customer-a/&quot;&#10;	}&#10;}&#10;</code></pre>
<p><strong>After (AI Search API):</strong></p>
<pre><code class="language-json">{&#10;	&quot;ai_search_options&quot;: {&#10;		&quot;retrieval&quot;: {&#10;			&quot;filters&quot;: { &quot;folder&quot;: &quot;customer-a/&quot; }&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h4 id="compound-filter-and">Compound filter (AND)</h4>
<p>Combine multiple conditions where all must match:</p>
<p><strong>Before (AutoRAG API):</strong></p>
<pre><code class="language-json">{&#10;	&quot;filters&quot;: {&#10;		&quot;type&quot;: &quot;and&quot;,&#10;		&quot;filters&quot;: [&#10;			{ &quot;type&quot;: &quot;eq&quot;, &quot;key&quot;: &quot;folder&quot;, &quot;value&quot;: &quot;customer-a/&quot; },&#10;			{ &quot;type&quot;: &quot;gte&quot;, &quot;key&quot;: &quot;timestamp&quot;, &quot;value&quot;: &quot;1735689600000&quot; }&#10;		]&#10;	}&#10;}&#10;</code></pre>
<p><strong>After (AI Search API):</strong></p>
<pre><code class="language-json">{&#10;	&quot;ai_search_options&quot;: {&#10;		&quot;retrieval&quot;: {&#10;			&quot;filters&quot;: {&#10;				&quot;folder&quot;: &quot;customer-a/&quot;,&#10;				&quot;timestamp&quot;: { &quot;$gte&quot;: 1735689600 }&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h2 id="api-references">API references</h2>
<ul>
<li><a href="/ai-search/api/search/rest-api/">REST API documentation</a></li>
<li><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/chat_completions/">Chat Completions API reference</a></li>
<li><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/search/">Search API reference</a></li>
<li><a href="/api/resources/autorag/">Legacy AutoRAG API reference</a></li>
</ul>
