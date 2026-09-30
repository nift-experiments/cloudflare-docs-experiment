<p>Use the AI Search REST API to upload, list, and manage individual documents within an instance.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3073.md")
</aside>
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
<h2 id="api-paths">API paths</h2>
<p>Item APIs are scoped to a <a href="/ai-search/concepts/namespaces/">namespace</a>:</p>
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
<td>Operates on instances within a namespace</td>
</tr>
</tbody>
</table>
<p>Every account has a <code>default</code> namespace. Use <code>default</code> unless you created a custom namespace. For the full specification, refer to the <a href="/api/resources/ai_search/subresources/namespaces/">Namespace API reference</a>.</p>
<h2 id="items">Items</h2>
<p>Upload, list, get, delete, and download items within an instance. For the full specification, refer to the <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/">Items API reference</a>.</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/upload/">Upload</a></td>
<td><code>POST</code></td>
<td>Upload a document for indexing</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/list/">List</a></td>
<td><code>GET</code></td>
<td>List all items in an instance</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/get/">Get</a></td>
<td><code>GET</code></td>
<td>Get item info by ID</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/delete/">Delete</a></td>
<td><code>DELETE</code></td>
<td>Delete an item</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/items/methods/download/">Download</a></td>
<td><code>GET</code></td>
<td>Download the original file</td>
</tr>
</tbody>
</table>
<h3 id="example-upload-a-document">Example: Upload a document</h3>
<p>Upload a file to an instance:</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/&lt;INSTANCE_NAME&gt;/items&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;F &quot;file=@/path/to/your/file.pdf&quot;&#10;</code></pre>
<h3 id="example-list-items">Example: List items</h3>
<p>List all items in an instance:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/&lt;INSTANCE_NAME&gt;/items&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>To find a single item by its exact object key, pass the <code>key</code> query parameter:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/&lt;INSTANCE_NAME&gt;/items?key=docs/readme.md&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Keys are unique per data source, so combine <code>key</code> with <code>source</code> (for example, <code>source=builtin</code>) to disambiguate when the same key exists across multiple sources.</p>
