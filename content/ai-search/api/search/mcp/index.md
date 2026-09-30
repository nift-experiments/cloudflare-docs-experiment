<p>The Model Context Protocol (MCP) endpoint allows AI agents to discover and interact with your AI Search content. This endpoint follows the <a href="https://modelcontextprotocol.io/">MCP specification</a> and provides tools for querying your indexed content.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Enable public endpoints for your AI Search instance:</p>
<ol>
<li>Go to <strong>AI Search</strong> in the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your AI Search instance.
3. Go to **Settings** > **Public Endpoint**.
4. Turn on **Enable Public Endpoint**.
5. Copy the public endpoint URL.
<h2 id="namespace-mcp-endpoints">Namespace MCP endpoints</h2>
<p>You can enable a public endpoint on a single instance or on a whole <a href="/ai-search/configuration/retrieval/public-endpoint/namespace/">namespace</a>. A namespace endpoint serves <code>/mcp</code> as well, and searches across the instances you allow in that namespace. Its hostname is prefixed with <code>ns-</code>:</p>
<pre><code class="language-txt">https://ns-&lt;NAMESPACE_ENDPOINT_ID&gt;.search.ai.cloudflare.com/mcp&#10;</code></pre>
<p>The tools and request format are the same for both. The examples on this page use the instance hostname.</p>
<h2 id="available-tools">Available tools</h2>
<p>The AI Search MCP endpoint exposes a <code>search</code> tool that queries your indexed content.</p>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>search</code></td>
<td>Finds exactly what you're looking for</td>
</tr>
</tbody>
</table>
<p>You can customize this in your AI Search instance settings. For more details, refer to <a href="/ai-search/configuration/retrieval/public-endpoint/">Public endpoint configuration</a>.</p>
<h2 id="test-the-mcp-endpoint">Test the MCP endpoint</h2>
<p>Send a request to the <code>/mcp</code> endpoint with the <code>Accept: application/json, text/event-stream</code> header:</p>
<pre><code class="language-bash">curl https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/mcp \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Accept: application/json, text/event-stream&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;jsonrpc&quot;: &quot;2.0&quot;,&#10;    &quot;id&quot;: 1,&#10;    &quot;method&quot;: &quot;tools/call&quot;,&#10;    &quot;params&quot;: {&#10;      &quot;name&quot;: &quot;search&quot;,&#10;      &quot;arguments&quot;: {&#10;        &quot;query&quot;: &quot;How do I configure AI Search?&quot;&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h2 id="bring-your-own-domain">Bring your own domain</h2>
<p>You can serve the MCP endpoint from a hostname that you own, such as <code>https://search.example.com/mcp</code>, instead of the generated one. The hostname must belong to a zone on the same Cloudflare account. To attach a custom domain:</p>
<ol>
<li>Go to <strong>AI Search</strong> in the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your instance or namespace.
3. Go to **Public Endpoints** and enable the public endpoint. A custom domain requires an active public endpoint.
4. Go to **Custom Domains** and attach your hostname.
<p>A custom domain routes requests through your own zone, so you can then put <a href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/">Cloudflare Access</a> in front of the endpoint. MCP clients authenticate with an Access <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service token</a>, sent as <code>CF-Access-Client-Id</code> and <code>CF-Access-Client-Secret</code> headers, so only the agents you issue tokens to can reach the endpoint. Access only protects the custom hostname, so set <code>default_domain_enabled</code> to <code>false</code> as well. Otherwise the default <code>&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com</code> hostname keeps answering unauthenticated requests.</p>
<p>To attach a domain through the API instead, refer to <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">Custom domains</a>.</p>
