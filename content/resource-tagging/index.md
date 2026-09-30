<div class="nb-description">
@markup("md", "content/.markup/bodies/443.md")
</div>
<div class="nb-plan">
<p>Available on all plans</p>
</div>
<p>Resource Tagging lets you attach key-value pairs to a wide range of <a href="/resource-tagging/reference/resource-types/">Cloudflare resource types</a> — including zones, custom hostnames, Cloudflare Tunnels, Workers, D1 databases, R2 buckets, KV namespaces, and more. Tags are stored separately from the resources themselves, enabling cross-resource queries and policy enforcement without modifying underlying resource configurations.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="public-beta">Public beta</h3>
@markup("md", "content/.markup/bodies/442.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>Tags are simple key-value string pairs stored as a JSON object:</p>
<pre><code class="language-json">{&#10;  &quot;environment&quot;: &quot;production&quot;,&#10;  &quot;team&quot;: &quot;platform&quot;,&#10;  &quot;region&quot;: &quot;us-west-1&quot;&#10;}&#10;</code></pre>
<p>You manage tags through the Tagging API using <code>GET</code>, <code>PUT</code>, and <code>DELETE</code> operations. The API supports <a href="/resource-tagging/how-to/filter-resources/">filtering resources by tags</a> with AND/OR logic, negation, and key-only matching.</p>
<p>Authentication uses <a href="/fundamentals/api/get-started/account-owned-tokens/">Account Owned Tokens (AOTs)</a>, which are account-level tokens independent of individual users.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>The dashboard is in beta. You can view and manage tags in the dashboard under <strong>Manage Account</strong> &gt; <strong>Resource Tagging</strong>, but the API remains the recommended interface for automation workflows.</li>
<li><code>PUT</code> replaces all tags. There is no <code>PATCH</code> endpoint. The <code>PUT</code> operation replaces all tags on a resource. Use the <a href="/resource-tagging/how-to/manage-tags/#add-a-single-tag"><code>GET</code>, merge, <code>PUT</code> workflow</a> to modify individual tags.</li>
<li><code>DELETE</code> removes all tags. There is no way to delete a single tag. Use <code>PUT</code> with the remaining tags instead.</li>
<li>Querying tags for a resource that has never been tagged returns a <code>500</code> error instead of <code>404</code>. This is a known beta limitation.</li>
</ul>
<h2 id="get-started">Get started</h2>
<p>Follow the <a href="/resource-tagging/get-started/">Get started guide</a> to set up authentication and make your first API calls.</p>
