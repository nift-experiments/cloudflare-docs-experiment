<p>A <a href="/ai-search/configuration/retrieval/public-endpoint/">public endpoint</a> is unauthenticated by design. Anyone who knows the URL can query your indexed content.</p>
<p>Put a <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">custom domain</a> in front of the public endpoint and protect it with <a href="/cloudflare-one/access-controls/applications/http-apps/">Cloudflare Access</a>. Users then authenticate with your identity provider before any request reaches AI Search. This turns a public knowledge base into an internal one without writing an authentication layer.</p>
<h2 id="how-it-works">How it works</h2>
<p>A custom domain is a hostname in a zone that you own. When the <code>CNAME</code> record for that hostname is <strong>Proxied</strong>, requests pass through your own zone before they reach AI Search:</p>
<pre><code class="language-mermaid">flowchart LR&#10;  A[Client] --&gt; B[&quot;Your zone&lt;br/&gt;Access, WAF, Bots&quot;]&#10;  B --&gt; C[&quot;AI Search&lt;br/&gt;public endpoint&quot;]&#10;  C --&gt; D[Your indexed content]&#10;</code></pre>
<p>Access runs in your zone, so it evaluates every request first. Requests that fail a policy never reach AI Search. AI Search needs no configuration to support this and applies its own <a href="/ai-search/configuration/retrieval/public-endpoint/#rate-limiting">rate limits</a> afterwards.</p>
<p>This routing is called <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/">orange-to-orange</a>. It requires the <code>CNAME</code> record to be proxied. A <strong>DNS only</strong> record bypasses your zone entirely, and Access never runs.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">custom domain</a> on the instance or namespace you want to protect, with a <strong>Proxied</strong> <code>CNAME</code> record.</li>
<li>Cloudflare Access enabled on your account.</li>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> connected to Cloudflare Access, or Cloudflare's one-time PIN.</li>
</ul>
<h2 id="1-turn-off-the-default-hostname"><ol>
<li>Turn off the default hostname</li>
</ol></h2>
<p>Access only protects your custom domain. The default <code>&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com</code> hostname does not pass through your zone, so it keeps answering unauthenticated requests and defeats the policy you are about to write.</p>
<p>Set <code>default_domain_enabled</code> to <code>false</code> before you create the Access application.</p>
<pre><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/namespaces/default/instances/&lt;INSTANCE_NAME&gt;&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;public_endpoint_params&quot;: {&#10;      &quot;enabled&quot;: true,&#10;      &quot;custom_domains&quot;: [&quot;access.search.example.com&quot;],&#10;      &quot;default_domain_enabled&quot;: false&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>The default hostname now returns a <code>404</code> with error <code>60018</code>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3110.md")
</aside>
<h2 id="2-create-an-access-application"><ol start="2">
<li>Create an Access application</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3111.md")
</div>
<p>For the full set of options, refer to <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">Publish a self-hosted application</a>.</p>
<h2 id="3-add-policies"><ol start="3">
<li>Add policies</li>
</ol></h2>
<p>An application with no policy denies every request. Add at least one <a href="/cloudflare-one/access-controls/policies/#allow">Allow policy</a> that describes who may query your content.</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Rule type</th>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Allow</td>
<td>Include</td>
<td>Emails ending in</td>
<td><code>@example.com</code></td>
</tr>
</tbody>
</table>
<p>Use the email, country, IP range, or identity provider group <a href="/cloudflare-one/access-controls/policies/#cloudflare-access-selectors">selectors</a> to match your organization. Refer to <a href="/cloudflare-one/access-controls/policies/common-policies/">Common policies</a> for more examples.</p>
<h2 id="4-authenticate-non-browser-clients"><ol start="4">
<li>Authenticate non-browser clients</li>
</ol></h2>
<p>Browsers follow the Access login redirect and receive a <code>CF_Authorization</code> cookie. MCP clients, backend services, and scripts cannot complete an interactive login, so they need a <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service token</a>.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3112.md")
</div>
<p>Send both credentials as headers on every request.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3115.md")
</div></div>
<p>Header support varies by MCP client. If your client cannot send custom headers, refer to <a href="/cloudflare-one/access-controls/ai-controls/secure-mcp-servers/">Secure MCP servers</a> for identity-based alternatives, or use <a href="/cloudflare-one/access-controls/authenticate-agents/#make-requests-with-cloudflared-access-curl"><code>cloudflared access curl</code></a> for command-line requests.</p>
<h2 id="5-verify"><ol start="5">
<li>Verify</li>
</ol></h2>
<p>A request without credentials returns the Access login page instead of search results:</p>
<pre><code class="language-bash">curl --include https://access.search.example.com/search \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&quot;messages&quot;:[{&quot;content&quot;:&quot;test&quot;,&quot;role&quot;:&quot;user&quot;}]}&#x27;&#10;</code></pre>
<p>Confirm that the default hostname is closed:</p>
<pre><code class="language-bash">curl https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/search \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&quot;messages&quot;:[{&quot;content&quot;:&quot;test&quot;,&quot;role&quot;:&quot;user&quot;}]}&#x27;&#10;</code></pre>
<p>The response is a <code>404</code> with error code <code>60018</code>.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li><strong>UI snippets on a public website stop working.</strong> <a href="/ai-search/configuration/retrieval/public-endpoint/embed-search-snippets/">UI snippets</a> call the public endpoint from the visitor's browser. Behind Access, only visitors who pass your policies can use them. Use Access for internal sites, and leave the endpoint open for public marketing sites.</li>
<li><strong>Cross-origin browser requests need an Access CORS configuration.</strong> If a page on a different origin calls the protected hostname, configure CORS settings on the Access application in addition to the <a href="/ai-search/configuration/retrieval/public-endpoint/#cors-configuration">allowed origins</a> on the public endpoint.</li>
<li><strong>Rate limits still apply.</strong> AI Search enforces its own rate limit after Access, and it is shared across all authenticated callers.</li>
<li><strong>Allowed origins are not authentication.</strong> The <code>authorized_hosts</code> setting sets CORS response headers, which only browsers honor. It does not stop a direct request from <code>curl</code> or a script.</li>
</ul>
<h2 id="alternatives">Alternatives</h2>
<p>Once the <code>CNAME</code> record is proxied, other Cloudflare products also apply to the hostname:</p>
<table>
<thead>
<tr>
<th>Product</th>
<th>Use it to</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/waf/custom-rules/">WAF custom rules</a></td>
<td>Allow specific countries, ASNs, IP ranges, or headers</td>
</tr>
<tr>
<td><a href="/waf/rate-limiting-rules/">Rate limiting rules</a></td>
<td>Apply per-client limits beyond the public endpoint limit</td>
</tr>
<tr>
<td><a href="/bots/">Bot Management</a></td>
<td>Score and challenge automated traffic</td>
</tr>
<tr>
<td><a href="/turnstile/">Turnstile</a></td>
<td>Verify humans before a browser client calls the endpoint</td>
</tr>
</tbody>
</table>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/"><h3 id="card-custom-domains-ai-search-configuration-retrieval-public-endpoint-custom-domains">Custom domains</h3><p>Serve a public endpoint from a hostname that you own.</p></a></p>
<p><a class="nb-card nb-link-card" href="/ai-search/configuration/retrieval/public-endpoint/"><h3 id="card-public-endpoint-settings-ai-search-configuration-retrieval-public-endpoint">Public endpoint settings</h3><p>Rate limiting, allowed origins, and per-endpoint controls.</p></a></p>
