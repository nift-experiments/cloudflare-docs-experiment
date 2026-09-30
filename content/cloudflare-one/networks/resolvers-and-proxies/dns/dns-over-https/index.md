<p>With Cloudflare Gateway, you can filter DNS over HTTPS (DoH) requests by <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">DNS location</a> or by user without needing to install the Cloudflare One Client on your devices.</p>
<p>Location-based policies require that you send DNS requests to a <a href="#filter-doh-requests-by-location">location-specific DoH endpoint</a>, while identity-based policies require that requests include a <a href="#filter-doh-requests-by-user">user-specific DoH token</a>.</p>
<h2 id="filter-doh-requests-by-location">Filter DoH requests by location</h2>
<p>Location-based policies require that you send DNS queries to a unique <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5870.md")
</div> assigned to the location:
<pre><code class="language-txt">https://&lt;YOUR_DOH_SUBDOMAIN&gt;.cloudflare-gateway.com/dns-query&#10;</code></pre>
<h3 id="prerequisites">Prerequisites</h3>
<p>Obtain your location's <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5871.md")
</div>.
<h3 id="configure-browser-for-doh">Configure browser for DoH</h3>
<p>Browsers can be configured to use any DNS over HTTPS (DoH) endpoint. If you choose to configure DoH directly in your browser, you must choose a Gateway DNS location as your DoH endpoint, otherwise DNS filtering will not occur in that browser.</p>
<details class="nb-details"><summary>Mozilla Firefox</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5872.md")
</div></details>
<details class="nb-details"><summary>Google Chrome</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5873.md")
</div></details>
<details class="nb-details"><summary>Microsoft Edge</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5874.md")
</div></details>
<details class="nb-details"><summary>Brave</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5875.md")
</div></details>
<details class="nb-details"><summary>Safari</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5876.md")
</div></details>
<p>Your DNS queries will now be sent to Gateway for filtering. To filter these requests, build a DNS policy using the <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/"><strong>DNS Location</strong></a> selector.</p>
<h3 id="configure-operating-system-for-doh">Configure operating system for DoH</h3>
<details class="nb-details"><summary>Windows 11</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5877.md")
</div></details>
<details class="nb-details"><summary>Windows Server 2022</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5878.md")
</div></details>
<h3 id="use-generic-doh-endpoint">Use generic DoH endpoint</h3>
<p>You can send DoH requests to the generic Cloudflare DoH endpoint, <code>dns.cloudflare-gateway.com</code>. To specify a location in your request, include a header named <code>cf-dns-location</code> with a value of your location's DoH subdomain. For example:</p>
<pre><code class="language-http">GET /dns-query?name=example.com&amp;type=A HTTP/2&#10;Host: dns.cloudflare-gateway.com&#10;cf-dns-location: 9y65g5srsm&#10;Accept: application/dns-message&#10;</code></pre>
<h2 id="filter-doh-requests-by-user">Filter DoH requests by user</h2>
<p>In order to filter DoH queries based on user identity, each query must include a user-specific authentication token. If you have several devices per user and want to apply device-specific policies, you will need to map each device to a different email.</p>
<p>Currently, authentication tokens can only be generated through the API. You can run this <a href="/cloudflare-one/static/authenticated-doh.py">interactive Python script</a> which automates the setup procedure, or follow the steps described below.</p>
<h3 id="1-create-a-service-token-for-the-account"><ol>
<li>Create a service token for the account</li>
</ol></h3>
<p>Each Cloudflare account can only have one active Access <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service token</a> authorized for DNS over HTTPS (DoH) at a time.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/access/service_tokens&quot; \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&quot;name&quot;:&quot;ACME Corporation service token&quot;}&#x27;&#10;</code></pre>
<p>Save the service token's <code>client_id</code>, <code>client_secret</code>, and <code>id</code>.</p>
<details class="nb-details"><summary>Example response</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5879.md")
</div></details>
<h3 id="2-enable-doh-functionality-for-the-service-token"><ol start="2">
<li>Enable DoH functionality for the service token</li>
</ol></h3>
<pre><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/access/organizations/doh/$SERVICE_TOKEN_ID&quot; \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>If you get an <code>access.api.error.service_token_not_found</code> error, check that <code>$SERVICE_TOKEN_ID</code> is the value of <code>id</code> and not <code>client_id</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5868.md")
</aside>
<details class="nb-details"><summary>Example response</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5880.md")
</div></details>
<h3 id="3-create-a-user"><ol start="3">
<li>Create a user</li>
</ol></h3>
<p>Create a new user and optionally add them to a group.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/access/users&quot; \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;John Doe&quot;,&#10;  &quot;email&quot;: &quot;jdoe@acme.com&quot;,&#10;  &quot;custom&quot;: {&quot;groups&quot;:[{&quot;id&quot;: &quot;02fk6b3p3majl10&quot;, &quot;email&quot;: &quot;finance@acme.com&quot;, &quot;name&quot;: &quot;Finance&quot;}]}&#10;}&#x27;&#10;</code></pre>
<p>Save the user's <code>id</code> returned in the response.</p>
<details class="nb-details"><summary>Example response</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5881.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5867.md")
</aside>
<h3 id="4-generate-a-doh-token-for-the-user"><ol start="4">
<li>Generate a DoH token for the user</li>
</ol></h3>
<p>Request a DoH token for the user, using your service token to authenticate into your <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5882.md")
</div>.
<pre><code class="language-bash">curl &quot;https://&lt;TEAM_NAME&gt;.cloudflareaccess.com/cdn-cgi/access/doh-token?account-id=&lt;ACCOUNT_ID&gt;&amp;user-id=&lt;USER_ID&gt;&amp;auth-domain=&lt;TEAM_NAME&gt;.cloudflareaccess.com&quot; \&#10;&#45;-header &quot;Cf-Access-Client-Id: &lt;CLIENT_ID&gt;&quot; \&#10;&#45;-header &quot;Cf-Access-Client-Secret: &lt;CLIENT_SECRET&gt;&quot;&#10;</code></pre>
<p>The response contains a unique DoH token associated with the user. This token expires in 24 hours. We recommend setting up a refresh flow for the DoH token instead of generating a new one for every DoH query.</p>
<details class="nb-details"><summary>Example response</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5883.md")
</div></details>
<h3 id="5-send-an-authenticated-doh-query"><ol start="5">
<li>Send an authenticated DoH query</li>
</ol></h3>
<p>Send DoH queries to the resolver at <code>https://&lt;ACCOUNT_ID&gt;.cloudflare-gateway.com/dns-query</code>, making sure to include the user's DoH token in the <code>CF-Authorization</code> header.</p>
<pre><code class="language-bash">curl --silent &quot;https://&lt;ACCOUNT_ID&gt;.cloudflare-gateway.com/dns-query?name=example.com&quot; \&#10;&#45;-header &quot;accept: application/dns-json&quot; \&#10;&#45;-header &quot;CF-Authorization: &lt;USER_DOH_TOKEN&gt;&quot; | jq&#10;</code></pre>
<p>If the site is blocked and you have turned on the <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/#configure-policy-block-behavior">block page</a> for the policy, the query will return <code>162.159.36.12</code> (the IP address of the Gateway block page). If the block page is disabled, the response will be <code>0.0.0.0</code>.</p>
<details class="nb-details"><summary>Example response</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/5884.md")
</div></details>
<p>You can verify that the request was associated with the correct user email by checking your <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway DNS logs</a>. To filter these requests, build a DNS policy using any of the Gateway <a href="/cloudflare-one/traffic-policies/identity-selectors/">identity-based selectors</a>.</p>
