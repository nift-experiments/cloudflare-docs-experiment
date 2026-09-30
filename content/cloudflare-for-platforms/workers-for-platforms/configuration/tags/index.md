<p>Use tags to organize, search, and filter user Workers at scale. Tag Workers based on customer ID, plan type, project ID, or environment. After you tag user Workers, you can perform bulk operations like deleting all Workers for a specific customer.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4212.md")
</aside>
<h2 id="add-tags-via-dashboard">Add tags via dashboard</h2>
<ol>
<li>Go to <strong>Workers for Platforms</strong> in the Cloudflare dashboard and select your namespace.</li>
<li>Select a user Worker from the list.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Tags</strong>.</li>
<li>Add your tags (for example, <code>customer-123</code>, <code>pro-plan</code>, <code>production</code>).</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>You can also search and filter Workers by tags in the namespace view.</p>
<h2 id="tags-api-reference">Tags API reference</h2>
<p>For complete API documentation, refer to <a href="/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/tags/">Workers for Platforms API</a>.</p>
<h3 id="get-script-tags">Get script tags</h3>
<p>Fetch all tags for a Worker script.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h3 id="set-script-tags">Set script tags</h3>
<p>Replace all tags on a Worker script. Existing tags not in the request are removed.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h3 id="add-a-single-tag">Add a single tag</h3>
<p>Add one tag to a Worker script without affecting existing tags.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags/{tag} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h3 id="delete-a-single-tag">Delete a single tag</h3>
<p>Remove one tag from a Worker script.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags/{tag} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h3 id="filter-workers-by-tag">Filter Workers by tag</h3>
<p>List all Workers that match a tag filter. Use <code>tag:yes</code> to include or <code>tag:no</code> to exclude.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h3 id="delete-workers-by-tag">Delete Workers by tag</h3>
<p>Delete all Workers matching a tag filter. Use this to bulk delete Workers when a customer leaves your platform.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
