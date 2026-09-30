<p>An <a href="/tenant/glossary/#account"><strong>Account</strong></a> will contain various settings, resources, and subscriptions to products for users. Each Tenant can have multiple associated accounts.</p>
<p>To retrieve a list of accounts associated with a Tenant details, send a <code>GET</code> request to the <code>/tenants/{tenant_id}/accounts</code> endpoint. You can find the Tenant tag and all Tenants associated with the user with the <a href="/tenant/how-to/get-tenant-details/"><strong>Tenant Details</strong></a> API. The Tenant Accounts API also requires pagination passed as query parameters:</p>
<ul>
<li>
<p><code>page</code> number</p>
<ul>
<li>Page number of accounts list response, indexed from 1</li>
</ul>
</li>
<li>
<p><code>per_page</code> number</p>
<ul>
<li>Number of accounts to display per page</li>
</ul>
</li>
<li>
<p><code>order</code> string</p>
<ul>
<li>
<p>(optional) Order by a specific column, has to be a valid top-level key from the response</p>
</li>
<li>
<p><code>direction</code> number</p>
<ul>
<li>(optional) 0 for ascending or 1 for descending, is 0 by default</li>
</ul>
</li>
</ul>
</li>
</ul>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/tenants/{tenant_id}/accounts?page=1&amp;per_page=10&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
<p>A successful request will return an HTTP status of <code>200</code> and a response body containing account information and feature flags for all accounts managed by the Tenant.</p>
