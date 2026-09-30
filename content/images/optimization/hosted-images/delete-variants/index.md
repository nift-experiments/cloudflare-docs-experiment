<p>You can delete variants via the Images dashboard or API. The only variant you cannot delete is public.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/9471.md")
</aside>
<h2 id="delete-variants-via-the-cloudflare-dashboard">Delete variants via the Cloudflare dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Hosted Images</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select the <strong>Delivery</strong> tab.</p>
</li>
<li>
<p>Find the variant you want to remove and select <strong>Delete</strong>.</p>
</li>
</ol>
<h2 id="delete-variants-via-the-api">Delete variants via the API</h2>
<p>Make a <code>DELETE</code> request to the delete variant endpoint.</p>
<pre><code class="language-bash">curl --request DELETE https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/variants/{variant_name} \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>After the variant has been deleted, the response returns <code>&quot;success&quot;: true.</code></p>
