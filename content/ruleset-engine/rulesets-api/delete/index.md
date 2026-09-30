<p>You can use the API to delete all the versions of a ruleset or delete a specific version of a ruleset.</p>
<ul>
<li><a href="#delete-ruleset">Delete ruleset (all versions)</a></li>
<li><a href="#delete-ruleset-version">Delete ruleset version</a></li>
</ul>
<h2 id="delete-ruleset">Delete ruleset</h2>
<p>Deletes all the versions of an existing ruleset at the account or zone level.</p>
<p>Use one of the following API endpoints:</p>
<ul>
<li><a href="/api/resources/rulesets/methods/delete/">Delete an account ruleset</a><br/>
<code>DELETE /accounts/{account_id}/rulesets/{ruleset_id}</code></li>
<li><a href="/api/resources/rulesets/methods/delete/">Delete a zone ruleset</a><br/>
<code>DELETE /zones/{zone_id}/rulesets/{ruleset_id}</code></li>
</ul>
<p>If the delete operation succeeds, the API method call returns a <code>204 No Content</code> HTTP status code.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13242.md")
</aside>
<h3 id="example">Example</h3>
<p>The following example request deletes an existing ruleset with ID <code>$RULESET_ID</code>.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/{ruleset_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h2 id="delete-ruleset-version">Delete ruleset version</h2>
<p>Deletes a specific version of a ruleset.</p>
<p>Use one of the following API endpoints:</p>
<ul>
<li><a href="/api/resources/rulesets/subresources/versions/methods/delete/">Delete an account ruleset version</a><br/>
<code>DELETE /accounts/{account_id}/rulesets/{ruleset_id}/versions/{version_number}</code></li>
<li><a href="/api/resources/rulesets/subresources/versions/methods/delete/">Delete a zone ruleset version</a><br/>
<code>DELETE /zones/{zone_id}/rulesets/{ruleset_id}/versions/{version_number}</code></li>
</ul>
<p>If the delete operation succeeds, the method call returns a <code>204 No Content</code> HTTP status code.</p>
<p>Later updates to the ruleset will not reuse the version number of a deleted ruleset version.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13241.md")
</aside>
<h3 id="example-1">Example</h3>
<p>The following example request deletes a version of an existing ruleset.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/{ruleset_id}/versions/{ruleset_version} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
