<p>Cloudflare Access allows you to securely publish internal tools and applications to the Internet by providing an authentication layer between the end user and your origin server. You can use signals from your existing identity providers (IdPs), device posture providers, and <a href="/cloudflare-one/access-controls/policies/#selectors">other rules</a> to control who can access your application.</p>
<p>Each application can have multiple policies with different constraints depending on what user group is accessing the application. For example, you can create one policy that requires corporate users to present specific device posture checks or mutual TLS authentication events, and a second policy for contractors which does not require these attributes.</p>
<h2 id="add-your-application-to-access">Add your application to Access</h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Select <strong>Create new application</strong>.</p>
</li>
<li>
<p>Select <strong>Self-hosted and private</strong>.</p>
</li>
<li>
<p>Select <strong>Add public hostname</strong>.</p>
</li>
<li></li>
</ol>
<p>In the <strong>Domain</strong> dropdown, select the domain that will represent the application. Domains must belong to an active zone in your Cloudflare account. You can use <a href="/cloudflare-one/access-controls/policies/app-paths/">wildcards</a> to protect multiple parts of an application that share a root path.</p>
<pre><code>	Alternatively, to use a [Cloudflare for SaaS custom hostname](/cloudflare-for-platforms/cloudflare-for-saas/security/secure-with-access/), select **Switch to custom input** and enter your custom hostname.&#10;</code></pre>
<ol start="6">
<li></li>
</ol>
<p>Under <strong>Access policies</strong>, add an existing policy or <a href="/cloudflare-one/access-controls/policies/policy-management/">create a new policy</a> to control who can connect to your application. All Access applications are deny by default -- a user must match an Allow policy before they are granted access.</p>
<ol start="7">
<li></li>
</ol>
<p>Configure how users will authenticate:</p>
<ol>
<li>
Select the [identity providers](/cloudflare-one/integrations/identity-providers/) you want to enable for your application.
</li>
<li>
(Recommended) If you plan to only allow access via a single IdP, turn on **Apply instant authentication**. End users will not be shown the [Cloudflare Access login page](/cloudflare-one/reusable-components/custom-pages/access-login-page/). Instead, Cloudflare will redirect users directly to your SSO login event.
</li>
<li> (Optional) Turn on  <b>Authenticate with Cloudflare One Client</b> to allow users to authenticate to the application using their <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/"> Cloudflare One Client session identity</a>. </li>
</ol>
<ol start="8">
<li></li>
</ol>
<p>(Optional) Configure <a href="/cloudflare-one/access-controls/policies/mfa-requirements/#configure-independent-mfa-for-an-application">independent MFA</a> for the application.</p>
<ol start="9">
<li></li>
</ol>
<p>In <strong>Session Duration</strong>, choose how often the user's <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/">application token</a> should expire.</p>
<p>Cloudflare checks every HTTP request to your application for a valid application token. If the user's application token (and global token) has expired, they will be prompted to reauthenticate with the IdP. For more information, refer to <a href="/cloudflare-one/access-controls/access-settings/session-management/">Session management</a>.</p>
<ol start="10">
<li>
<p>(Optional) Go to the <strong>Additional settings</strong> tab to customize the application experience:</p>
<ul>
<li><strong>App Launcher customization</strong>: Configure how this application appears to users in the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a>.</li>
<li></li>
</ul>
</li>
</ol>
<p><strong>Custom block pages</strong>: Choose what users will see when they are denied access to the application.</p>
<ul>
<li><strong>Cloudflare default</strong>: Reload the <a href="/cloudflare-one/reusable-components/custom-pages/access-login-page/">login page</a> and display a block message below the Cloudflare Access logo. The default message is <code>That account does not have access</code>, or you can enter a custom message.</li>
<li><strong>Redirect URL</strong>: Redirect to the specified website.</li>
<li><strong>Custom page template</strong>: Display a <a href="/cloudflare-one/reusable-components/custom-pages/access-block-page/">custom block page</a> hosted in Cloudflare One.</li>
</ul>
<ul>
<li><a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/cors/"><strong>Cross-Origin Resource Sharing (CORS) settings</strong></a></li>
<li><a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#cookie-settings"><strong>Cookie settings</strong></a></li>
<li><strong>401 Response for Service Auth policies</strong>: Return a <code>401</code> response code when a user (or machine) makes a request to the application without the correct <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service token</a>.</li>
</ul>
<ol start="11">
<li>Select <strong>Create</strong>.</li>
</ol>
<p>When users go to the application, they will be prompted to login with your identity provider.</p>
