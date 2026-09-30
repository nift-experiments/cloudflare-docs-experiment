<p>Gateway HTTP policies with Allow actions can modify the headers of matching requests before they reach their destination. You can add dynamic values to set headers to forward information like user identity, source IP, and other inputs to upstream services, enforce SaaS tenant control, strip internal headers, override header content.</p>
<p>Header manipulation requires <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a>, because HTTP headers are only visible on traffic which Gateway can decrypt.</p>
<h2 id="header-operations">Header operations</h2>
<p>Gateway supports three header operations on HTTP policies. When a request matches an Allow policy with header operations configured, Gateway applies them in the following order:</p>
<ol>
<li><strong>Delete</strong> - Remove headers from the request.</li>
<li><strong>Overwrite</strong> - Overwrite headers on the request. Headers with matched names will have their values overwritten. If the header does not exist, it is created.</li>
<li><strong>Add</strong> - Append headers to the request. If the header already exists, the added value is appended to the existing value.</li>
</ol>
<p>You can configure up to 20 header operations per policy. Header names are limited to 256 bytes, and header values are limited to 4 KB.</p>
<h3 id="add-headers">Add headers</h3>
<p>Adding a header appends a value to the request. If the header already exists, the value is added alongside the existing value rather than replacing it.</p>
<h3 id="overwrite-headers">Overwrite headers</h3>
<p>Overwriting a header overwrites any existing value. If the header does not already exist on the request, it is created. Use this operation when you need to guarantee a specific header value regardless of what the client sent.</p>
<h3 id="delete-headers">Delete headers</h3>
<p>Deleting a header removes it from the request entirely. If the header does not exist, the operation has no effect.</p>
<h2 id="dynamic-header-values">Dynamic header values</h2>
<p>Header values can include dynamic variables that Gateway resolves at request time using identity, device, and network context from the current session. Dynamic variables use the <code>@{...}</code> syntax and can be mixed with static text in the same value.</p>
<p>For example, a header value of <code>user-@{identity.email}</code> resolves to <code>user-jdoe@example.com</code> at request time.</p>
<p>The following dynamic variables are available:</p>
<table>
<thead>
<tr>
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@{identity.email}</code></td>
<td>User's email address from the identity provider.</td>
</tr>
<tr>
<td><code>@{identity.name}</code></td>
<td>User's display name from the identity provider.</td>
</tr>
<tr>
<td><code>@{identity.id}</code></td>
<td>User's Cloudflare identity UUID.</td>
</tr>
<tr>
<td><code>@{identity.groups}</code></td>
<td>User's identity provider group memberships.</td>
</tr>
<tr>
<td><code>@{identity.SAML}</code></td>
<td>User's SAML attributes from the identity provider if configured.</td>
</tr>
<tr>
<td><code>@{identity.OIDC}</code></td>
<td>User's OIDC claims from the identity provider if configured.</td>
</tr>
<tr>
<td><code>@{source.ip}</code></td>
<td>Source IP address of the user's connection as seen in Gateway.</td>
</tr>
<tr>
<td><code>@{destination.ip}</code></td>
<td>Destination IP address of the request.</td>
</tr>
<tr>
<td><code>@{device.id}</code></td>
<td>Cloudflare One Client device UUID.</td>
</tr>
<tr>
<td><code>@{device.posture}</code></td>
<td>Device posture check results (serialized as a JSON string).</td>
</tr>
</tbody>
</table>
<p>Dynamic variables require an active identity session. If Gateway cannot resolve a variable (for example, the user is not authenticated), the variable is replaced with a warning string such as <code>cf-unresolved</code> or <code>cf-invalid</code>, and a warning is added to the HTTP log.</p>
<h2 id="configure-header-operations">Configure header operations</h2>
<h3 id="dashboard">Dashboard</h3>
<p>To create an HTTP policy with header operations:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/one">Cloudflare One dashboard</a>, go to <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong> &gt; <strong>HTTP</strong>.</li>
<li>Select <strong>Add a policy</strong>.</li>
<li>Build an expression to match the traffic you want to modify.</li>
<li>In <strong>Action</strong>, select <em>Allow</em>.</li>
<li>Under <strong>Modify request headers</strong>, select <strong>Add</strong> or <strong>Overwrite</strong> to add or overwrite headers, or select <strong>Remove</strong> to delete a header.</li>
<li>For Add and Overwrite operations, enter the header name and value. To use a dynamic variable, enter the <code>@{...}</code> syntax in the value field, or select the <code>{}</code> button to see the list of available values. For Remove operations, enter only the header name.</li>
<li>Save your policy.</li>
</ol>
<h3 id="api">API</h3>
<p>To create an HTTP policy with header operations via the API, include <code>add_headers</code>, <code>set_headers</code>, and <code>delete_headers</code> in the <code>rule_settings</code> object.</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/gateway/rules \&#10;&#45;-header &quot;Authorization: Bearer {api_token}&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;Forward identity headers&quot;,&#10;  &quot;action&quot;: &quot;allow&quot;,&#10;  &quot;enabled&quot;: true,&#10;  &quot;filters&quot;: [&quot;http&quot;],&#10;  &quot;traffic&quot;: &quot;any(http.request.domains[*] in {\&quot;app.example.com\&quot;})&quot;,&#10;  &quot;rule_settings&quot;: {&#10;    &quot;add_headers&quot;: {&#10;      &quot;X-User-Email&quot;: [&quot;@{identity.email}&quot;],&#10;      &quot;X-User-Groups&quot;: [&quot;@{identity.groups}&quot;]&#10;    },&#10;    &quot;set_headers&quot;: {&#10;      &quot;X-Forwarded-User&quot;: [&quot;@{identity.email}&quot;]&#10;    },&#10;    &quot;delete_headers&quot;: [&quot;X-Debug-Token&quot;, &quot;X-Internal-Only&quot;]&#10;  }&#10;}&#x27;&#10;</code></pre>
<p>The <code>rule_settings</code> fields for header manipulation are:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>add_headers</code></td>
<td><code>map&lt;string, array&lt;string&gt;&gt;</code></td>
<td>Headers to append. Each key is a header name, each value is a list of values to add.</td>
</tr>
<tr>
<td><code>set_headers</code></td>
<td><code>map&lt;string, array&lt;string&gt;&gt;</code></td>
<td>Headers to overwrite. Each key is a header name, each value is a list of values to set.</td>
</tr>
<tr>
<td><code>delete_headers</code></td>
<td><code>array&lt;string&gt;</code></td>
<td>Header names to remove from the request.</td>
</tr>
</tbody>
</table>
<p>A single header value can contain a mix of static text and dynamic variables. For example:</p>
<pre><code class="language-json">{&#10;  &quot;add_headers&quot;: {&#10;    &quot;X-Request-Context&quot;: [&quot;user=@{identity.email}, device=@{device.id}, src=@{source.ip}&quot;]&#10;  }&#10;}&#10;</code></pre>
<h3 id="verify-custom-headers">Verify custom headers</h3>
<p>If you save a HAR (HTTP Archive) file from a browser to analyze your web traffic, custom headers defined with Gateway will not appear in the file. This is because Gateway injects the header after the request leaves the browser.</p>
<p>To verify Gateway is applying a custom header:</p>
<ol>
<li>In your policy with custom headers, add a selector to match traffic for <a href="https://httpbin.org/">HTTPBin</a>, an open-source site for testing HTTP requests. For example:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
<th>Untrusted certificate action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Application</td>
<td>in</td>
<td><em>Google Workspace</em></td>
<td>Or</td>
<td>Allow</td>
<td>Block</td>
</tr>
<tr>
<td>Domain</td>
<td>in</td>
<td><code>httpbin.org</code></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<ol start="2">
<li>On your device, go to <a href="https://httpbin.org/anything"><code>httpbin.org/anything</code></a>. Your custom header will appear in the list of headers.</li>
<li>(Optional) Remove the HTTPBin expression from your policy.</li>
</ol>
<h2 id="use-cases">Use cases</h2>
<h3 id="saas-tenant-control">SaaS tenant control</h3>
<p>Tenant control allows your users to access corporate SaaS applications while blocking access to personal accounts on the same service. For example, you can allow access to your company's Google Workspace while blocking personal Gmail logins.</p>
<p>Gateway implements tenant control by injecting custom HTTP headers into matching requests. These headers tell the SaaS application which tenant (organization) is authorized. If the user attempts to authenticate with a personal account, the SaaS application reads the header and rejects the request.</p>
<details class="nb-details"><summary>Microsoft 365</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6486.md")
</div></details>
<details class="nb-details"><summary>Google Workspace</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6487.md")
</div></details>
<details class="nb-details"><summary>Slack</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6488.md")
</div></details>
<details class="nb-details"><summary>Dropbox</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6489.md")
</div></details>
<details class="nb-details"><summary>ChatGPT</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6490.md")
</div></details>
<details class="nb-details"><summary>Claude</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6491.md")
</div></details>
<h3 id="forward-user-identity-to-upstream-services">Forward user identity to upstream services</h3>
<p>You can use dynamic header values to forward user identity information to your upstream applications without requiring those applications to integrate with Cloudflare Access directly.</p>
<table>
<thead>
<tr>
<th>Header name</th>
<th>Header value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>X-User-Email</code></td>
<td><code>@{identity.email}</code></td>
</tr>
<tr>
<td><code>X-User-Name</code></td>
<td><code>@{identity.name}</code></td>
</tr>
<tr>
<td><code>X-User-Groups</code></td>
<td><code>@{identity.groups}</code></td>
</tr>
<tr>
<td><code>X-Source-IP</code></td>
<td><code>@{source.ip}</code></td>
</tr>
</tbody>
</table>
<p>Your upstream application can read these headers to identify the user, enforce authorization logic, or populate audit logs.</p>
<h3 id="strip-internal-headers">Strip internal headers</h3>
<p>To prevent clients from spoofing internal headers, use the delete operation to remove headers before forwarding the request, then use the add or set operation to re-inject them with verified values.</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/gateway/rules \&#10;&#45;-header &quot;Authorization: Bearer {api_token}&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;Replace internal headers&quot;,&#10;  &quot;action&quot;: &quot;allow&quot;,&#10;  &quot;enabled&quot;: true,&#10;  &quot;filters&quot;: [&quot;http&quot;],&#10;  &quot;traffic&quot;: &quot;any(http.request.domains[*] in {\&quot;internal.example.com\&quot;})&quot;,&#10;  &quot;rule_settings&quot;: {&#10;    &quot;delete_headers&quot;: [&quot;X-Internal-User&quot;],&#10;    &quot;set_headers&quot;: {&#10;      &quot;X-Internal-User&quot;: [&quot;@{identity.email}&quot;]&#10;    }&#10;  }&#10;}&#x27;&#10;</code></pre>
<h3 id="exempt-users-in-cloudflare-waf">Exempt users in Cloudflare WAF</h3>
<p>You can include custom headers in an HTTP policy to allow your users through <a href="/waf/">Cloudflare WAF</a>. This is useful for allowing only Cloudflare One Client users through your WAF.</p>
<ol>
<li>Create an Allow policy for an internal domain behind your WAF with a custom header.</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Domain</td>
<td>in</td>
<td><code>internalapp.com</code></td>
<td>Allow</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>Custom header name</th>
<th>Custom header value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>X-Example-Header</code></td>
<td><code>example-value</code></td>
</tr>
</tbody>
</table>
<ol start="2">
<li>In Cloudflare WAF, <a href="/waf/custom-rules/">create a custom rule</a> to <a href="/waf/custom-rules/use-cases/require-specific-headers/#example-2-require-http-header-with-a-specific-value">require the same HTTP header</a>.</li>
</ol>
<h3 id="use-custom-headers-with-browser-isolation">Use custom headers with Browser Isolation</h3>
<p>You can configure <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> to send custom headers. This is useful for implementing tenant control for isolated SaaS applications or sending arbitrary custom request headers to isolated websites.</p>
<p>To use custom headers with Browser Isolation, create two HTTP policies targeting the same domain or application group. For example, you can create policies for <a href="https://httpbin.org/">HTTPBin</a>, an open-source site for testing HTTP requests:</p>
<ol>
<li>Create an Isolate policy for <code>httpbin.org</code>.</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Domain</td>
<td>in</td>
<td><code>httpbin.org</code></td>
<td>Isolate</td>
</tr>
</tbody>
</table>
<ol start="2">
<li>Create an Allow policy for <code>httpbin.org</code> with a custom header.</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Domain</td>
<td>in</td>
<td><code>httpbin.org</code></td>
<td>Allow</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>Custom header name</th>
<th>Custom header value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Example-Header</code></td>
<td><code>example-value</code></td>
</tr>
</tbody>
</table>
<ol start="3">
<li>Go to <a href="https://httpbin.org/anything"><code>httpbin.org/anything</code></a>. Cloudflare will render the site in an isolated browser. Your custom header will appear in the list of headers.</li>
</ol>
