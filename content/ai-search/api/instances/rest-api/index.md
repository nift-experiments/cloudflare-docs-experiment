<p>Use the AI Search REST API to manage instances and sync jobs over HTTP.</p>
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
<p>AI Search scopes Instance APIs to a <a href="/ai-search/concepts/namespaces/">namespace</a>:</p>
<table>
<thead>
<tr>
<th>Path</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/accounts/{account_id}/ai-search/namespaces/{namespace}/instances/{id}</code></td>
<td>Operates on instances within a namespace</td>
</tr>
</tbody>
</table>
<p>Every account has a <code>default</code> namespace. Use <code>default</code> unless you created a custom namespace. For the full specification, refer to the <a href="/api/resources/ai_search/subresources/namespaces/">Namespace API reference</a>.</p>
<h2 id="instances">Instances</h2>
<p>Create, list, get, update, and delete AI Search instances. For the full specification, refer to the <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/">Instances API reference</a>.</p>
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
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/create/">Create</a></td>
<td><code>POST</code></td>
<td>Create a new instance</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/list/">List</a></td>
<td><code>GET</code></td>
<td>List all instances</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/read/">Get</a></td>
<td><code>GET</code></td>
<td>Get an instance by ID</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/update/">Update</a></td>
<td><code>PUT</code></td>
<td>Update instance configuration</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/delete/">Delete</a></td>
<td><code>DELETE</code></td>
<td>Delete an instance</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/methods/stats/">Stats</a></td>
<td><code>GET</code></td>
<td>Get indexing statistics</td>
</tr>
</tbody>
</table>
<h3 id="example-create-an-instance">Example: Create an instance</h3>
<p>Create an instance in the default namespace:</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;id&quot;: &quot;my-instance&quot;&#10;  }&#x27;&#10;</code></pre>
<h2 id="jobs">Jobs</h2>
<p>Trigger and monitor <a href="/ai-search/configuration/indexing/syncing/">sync jobs</a> that scan your data source and index new or updated content. For the full specification, refer to the <a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/">Jobs API reference</a>.</p>
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
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/create/">Create</a></td>
<td><code>POST</code></td>
<td>Trigger a new sync job</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/list/">List</a></td>
<td><code>GET</code></td>
<td>List all jobs for an instance</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/get/">Get</a></td>
<td><code>GET</code></td>
<td>Get job details</td>
</tr>
<tr>
<td><a href="/api/resources/ai_search/subresources/namespaces/subresources/instances/subresources/jobs/methods/logs/">Logs</a></td>
<td><code>GET</code></td>
<td>View job logs</td>
</tr>
</tbody>
</table>
<h3 id="example-trigger-a-sync-job">Example: Trigger a sync job</h3>
<p>Start a new sync job for an instance:</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/&lt;INSTANCE_NAME&gt;/jobs&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
