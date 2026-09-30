<p>All tag operations use the Tagging API. Authentication requires an <a href="/fundamentals/api/get-started/account-owned-tokens/">account API token</a> or user API token with appropriate permissions.</p>
<h2 id="set-tags-on-a-resource">Set tags on a resource</h2>
<p>Use <code>PUT</code> to set tags on an account-level resource. This operation replaces all existing tags on the resource.</p>
<pre><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;resource_type&quot;: &quot;worker&quot;,&#10;    &quot;resource_id&quot;: &quot;&#x27;&quot;$RESOURCE_ID&quot;&#x27;&quot;,&#10;    &quot;tags&quot;: {&#10;      &quot;environment&quot;: &quot;production&quot;,&#10;      &quot;team&quot;: &quot;platform&quot;,&#10;      &quot;cost-center&quot;: &quot;engineering&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>For zone-level resources, use the zone endpoint:</p>
<pre><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID/tags&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;resource_type&quot;: &quot;zone&quot;,&#10;    &quot;resource_id&quot;: &quot;&#x27;&quot;$ZONE_ID&quot;&#x27;&quot;,&#10;    &quot;tags&quot;: {&#10;      &quot;environment&quot;: &quot;production&quot;,&#10;      &quot;customer&quot;: &quot;acme-corp&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>Some resource types require additional fields. Refer to <a href="/resource-tagging/reference/resource-types/">supported resource types</a> for details.</p>
<h2 id="get-tags-for-a-resource">Get tags for a resource</h2>
<p>Retrieve tags for a specific resource:</p>
<pre><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags?resource_type=worker&amp;resource_id=$RESOURCE_ID&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12768.md")
</aside>
<h2 id="add-a-single-tag">Add a single tag</h2>
<p>The API does not support partial updates — <code>PUT</code> always replaces all tags. To add a tag without removing existing ones, use the <code>GET</code>, merge, <code>PUT</code> pattern:</p>
<ol>
<li><code>GET</code> the current tags.</li>
</ol>
<pre><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags?resource_type=worker&amp;resource_id=$RESOURCE_ID&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;&#10;&#35; Response: {&quot;result&quot;: {&quot;tags&quot;: {&quot;environment&quot;: &quot;production&quot;, &quot;team&quot;: &quot;platform&quot;}}}&#10;</code></pre>
<ol start="2">
<li>Merge the new tag into the existing set locally.</li>
</ol>
<pre><code class="language-json">{&#10;  &quot;environment&quot;: &quot;production&quot;,&#10;  &quot;team&quot;: &quot;platform&quot;,&#10;  &quot;cost-center&quot;: &quot;engineering&quot;&#10;}&#10;</code></pre>
<ol start="3">
<li><code>PUT</code> the complete merged tag set.</li>
</ol>
<pre><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;resource_type&quot;: &quot;worker&quot;,&#10;    &quot;resource_id&quot;: &quot;&#x27;&quot;$RESOURCE_ID&quot;&#x27;&quot;,&#10;    &quot;tags&quot;: {&#10;      &quot;environment&quot;: &quot;production&quot;,&#10;      &quot;team&quot;: &quot;platform&quot;,&#10;      &quot;cost-center&quot;: &quot;engineering&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/12767.md")
</aside>
<h2 id="remove-a-single-tag">Remove a single tag</h2>
<p>Follow the same <code>GET</code>, merge, <code>PUT</code> pattern, but omit the tag you want to remove from the set before calling <code>PUT</code>.</p>
<h2 id="delete-all-tags">Delete all tags</h2>
<p>To remove all tags from a resource:</p>
<pre><code class="language-bash">curl -X DELETE &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tags&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;resource_type&quot;: &quot;worker&quot;,&#10;    &quot;resource_id&quot;: &quot;&#x27;&quot;$RESOURCE_ID&quot;&#x27;&quot;&#10;  }&#x27;&#10;</code></pre>
<p>This returns <code>204 No Content</code> on success. Only use <code>DELETE</code> when you want to remove all tags from a resource (for example, when decommissioning it).</p>
