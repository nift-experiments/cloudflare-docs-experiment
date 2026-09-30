<p>Configure public endpoints to expose your AI Search instance directly to users without requiring authentication. This enables you to share your AI Search functionality with external users, or to integrate it into public-facing applications.</p>
<p>You can enable a public endpoint on a single instance or on a whole <a href="/ai-search/concepts/namespaces/">namespace</a>, which searches across several instances and merges the results. Everything on this page applies to both. For what is specific to namespaces, such as choosing which instances the endpoint can reach, refer to <a href="/ai-search/configuration/retrieval/public-endpoint/namespace/">Namespace public endpoints</a>.</p>
<h2 id="available-endpoints">Available endpoints</h2>
<p>An instance or a namespace can expose three public endpoints:</p>
<table>
<thead>
<tr>
<th>Endpoint</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/mcp</code></td>
<td>Model Context Protocol endpoint for AI agents</td>
</tr>
<tr>
<td><code>/chat/completions</code></td>
<td>OpenAI-compatible chat completion endpoint</td>
</tr>
<tr>
<td><code>/search</code></td>
<td>Search endpoint that returns relevant chunks</td>
</tr>
</tbody>
</table>
<p>For details on how to use these endpoints, refer to <a href="/ai-search/api/search/public-endpoint/">Public endpoint usage</a>.</p>
<h2 id="public-url-format">Public URL format</h2>
<p>Cloudflare generates the hostname when you enable the endpoint. It is not the instance or namespace name.</p>
<table>
<thead>
<tr>
<th>Hostname</th>
<th>Serves</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com</code></td>
<td>A single instance.</td>
</tr>
<tr>
<td><code>ns-&lt;NAMESPACE_ENDPOINT_ID&gt;.search.ai.cloudflare.com</code></td>
<td>A <a href="/ai-search/configuration/retrieval/public-endpoint/namespace/">namespace</a>, searching across several instances.</td>
</tr>
</tbody>
</table>
<p>For example:</p>
<ul>
<li><code>https://abc123.search.ai.cloudflare.com/search</code></li>
<li><code>https://ns-abc123.search.ai.cloudflare.com/search</code></li>
</ul>
<p>The identifier is generated the first time you enable the endpoint and is never rotated. Disabling the endpoint keeps the identifier, so re-enabling it reuses the same URL.</p>
<p>You can also serve the same endpoints from a hostname that you own, such as <code>https://search.example.com/search</code>. Refer to <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">Custom domains</a>.</p>
<h2 id="enabling-and-disabling-public-endpoints">Enabling and disabling public endpoints</h2>
<p>You can enable or disable each public endpoint independently:</p>
<ol>
<li>Log in to your Cloudflare account, and go to <strong>AI Search</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your AI Search instance or namespace.
3. Go to **Settings** > **Public Endpoints**.
4. Toggle on **Public Endpoints** to enable the feature, then toggle each individual endpoint on or off as needed.
<p>Each endpoint has its own configuration panel for granular control.</p>
<p>To enable a namespace endpoint through the API, refer to <a href="/ai-search/configuration/retrieval/public-endpoint/namespace/#enable-a-namespace-public-endpoint">Namespace public endpoints</a>.</p>
<h2 id="rate-limiting">Rate limiting</h2>
<p>Configure rate limits to control usage across all public endpoints:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td>Requests per period</td>
<td>Maximum number of requests allowed</td>
<td>120</td>
</tr>
<tr>
<td>Time period</td>
<td>Time window for the rate limit</td>
<td>1 minute</td>
</tr>
<tr>
<td>Period type</td>
<td>Rate limiting technique: <code>fixed</code> or <code>sliding</code></td>
<td><code>fixed</code></td>
</tr>
</tbody>
</table>
<p>Rate limits apply across all enabled public endpoints for the AI Search instance.</p>
<h2 id="cors-configuration">CORS configuration</h2>
<p>Cross-Origin Resource Sharing (CORS) is enabled by default to support browser-based applications.</p>
<p>The default allowed origins depend on your data source type:</p>
<ul>
<li><strong>Website data sources</strong>: The source domain is automatically added as an allowed origin.</li>
<li><strong>Other data sources</strong>: All origins (<code>*</code>) are allowed by default.</li>
</ul>
<p>You can customize allowed origins in the <strong>Public Endpoints</strong> settings by adding specific hostnames to <strong>Authorized hosts</strong>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3099.md")
</aside>
<h2 id="tool-description">Tool description</h2>
<p>The <strong>Tool Description</strong> field allows you to customize how your AI Search instance is described to MCP clients. The default description is <code>Finds exactly what you're looking for</code>. This description helps AI agents understand what content is available, and when to use your search tool. A good tool description should explain what type of content is indexed, and what kinds of questions it can answer.</p>
<p>For example:</p>
<pre><code class="language-txt">Search the Acme product documentation for information about&#10;installation, configuration, API references, and troubleshooting&#10;guides. Use this tool when users ask questions about how to set up&#10;or use Acme products.&#10;</code></pre>
<h2 id="security-considerations">Security considerations</h2>
<p>A public endpoint does not require authentication. Anyone who knows the URL can query your indexed content.</p>
<p>To restrict who can query the endpoint, add a <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">custom domain</a> and protect it with <a href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/">Cloudflare Access</a>. Users then authenticate with your identity provider before any request reaches AI Search.</p>
<p>If you keep the endpoint open:</p>
<ul>
<li>Only index content that is safe to expose publicly.</li>
<li>Set a <a href="#rate-limiting">rate limit</a> to limit abuse.</li>
<li>Disable the endpoints you do not use, such as <code>/mcp</code>.</li>
<li>Monitor usage through your dashboard analytics.</li>
</ul>
<h2 id="related">Related</h2>
<p><a class="nb-card nb-link-card" href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/"><h3 id="card-custom-domains-ai-search-configuration-retrieval-public-endpoint-custom-domains">Custom domains</h3><p>Serve a public endpoint from a hostname that you own.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/"><h3 id="card-cloudflare-access-ai-search-configuration-retrieval-public-endpoint-cloudflare-access">Cloudflare Access</h3><p>Require users to authenticate before they can query your content.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/configuration/retrieval/public-endpoint/namespace/"><h3 id="card-namespace-public-endpoints-ai-search-configuration-retrieval-public-endpoint-namespace">Namespace public endpoints</h3><p>Search across several instances from a single public endpoint.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/configuration/retrieval/public-endpoint/embed-search-snippets/"><h3 id="card-ui-snippets-ai-search-configuration-retrieval-public-endpoint-embed-search-snippets">UI snippets</h3><p>Add pre-built search and chat components to your website.</p></a></p>
