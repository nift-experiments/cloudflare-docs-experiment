<p>Keycloak is an open source identity and access management solution built by JBoss.</p>
<h2 id="set-up-keycloak-saml">Set up Keycloak (SAML)</h2>
<p>To set up Keycloak (SAML) as your identity provider:</p>
<ol>
<li>
<p>In Keycloak, select the realm that you want Cloudflare Access to use.</p>
</li>
<li>
<p>Go to <strong>Clients</strong> &gt; <strong>Create client</strong>.</p>
</li>
<li>
<p>For <strong>Client type</strong>, select <strong>SAML</strong>.</p>
</li>
<li>
<p>Under <strong>Client ID</strong>, enter your Cloudflare Access callback URL:</p>
</li>
</ol>
<pre><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<ol start="5">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Change <strong>Name ID format</strong> to <strong>email</strong>.</p>
</li>
<li>
<p>In <strong>Valid redirect URIs</strong>, enter your Cloudflare Access callback URL:</p>
</li>
</ol>
<pre><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<ol start="8">
<li>In <strong>Master SAML Processing URL</strong>, enter the SAML endpoint for your Keycloak realm:</li>
</ol>
<pre><code class="language-txt">https://&lt;keycloak_domain&gt;/realms/&lt;realm_name&gt;/protocol/saml&#10;</code></pre>
<p>Keycloak v17 and later use <code>/realms/&lt;realm_name&gt;/protocol/saml</code> by default. Keycloak v16 and earlier may use <code>/auth/realms/&lt;realm_name&gt;/protocol/saml</code> instead.</p>
<ol start="9">
<li>
<p>If you wish to enable client signatures, enable <strong>Client Signature Required</strong> and select <strong>Save</strong>.</p>
<ol>
<li>
<p>You will need to <a href="/cloudflare-one/integrations/identity-providers/signed_authn/">follow the steps here to get the certificate and enable it in the Cloudflare dashboard</a>.</p>
</li>
<li>
<p>Import the Access certificate you downloaded into the <strong>Keys</strong> tab. Use <strong>Certificate PEM</strong> as the format.</p>
</li>
</ol>
</li>
<li>
<p>Configure a protocol mapper for the user's email address.</p>
<ol>
<li>Go to <strong>Clients</strong> &gt; your Cloudflare Access SAML client &gt; <strong>Client scopes</strong>.</li>
<li>Select the dedicated client scope for the client.</li>
<li>Go to <strong>Mappers</strong> &gt; <strong>Add mapper</strong> &gt; <strong>By configuration</strong>.</li>
<li>Select <strong>User Property</strong>.</li>
<li>Set <strong>Property</strong> to <code>email</code> and <strong>SAML Attribute Name</strong> to <code>email</code>.</li>
</ol>
<p>Next, you will need to integrate with Cloudflare Access.</p>
</li>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>.</p>
</li>
<li>
<p>Choose <strong>SAML</strong> on the next page.</p>
<p>You will need to input the Keycloak details manually. The examples below should be replaced with the specific domains in use with Keycloak and Cloudflare Access.</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Field</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Single Sign-On URL</td>
<td><code>https://&lt;keycloak_domain&gt;/realms/&lt;realm_name&gt;/protocol/saml</code></td>
</tr>
<tr>
<td>IdP Entity ID or Issuer URL</td>
<td><code>https://&lt;unique_id&gt;.cloudflareaccess.com/cdn-cgi/access/callback</code></td>
</tr>
<tr>
<td>Signing certificate</td>
<td>Use the X509 certificate from the Keycloak realm keys</td>
</tr>
</tbody>
</table>
<ol start="14">
<li>Select <strong>Save</strong>.</li>
</ol>
<p>To test that your connection is working, go to <strong>Integrations</strong> &gt; <strong>Identity providers</strong> and select <strong>Test</strong> next to the login method you want to test.</p>
