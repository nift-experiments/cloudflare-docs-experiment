<p>You can securely publish internal tools and applications by adding Cloudflare Access as an authentication layer between the end user and your origin server.</p>
<p>This page describes how to make a web application accessible to anyone on the Internet via a public hostname. To make the application available over a private IP or hostname, refer to <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Add a self-hosted private application</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/fundamentals/manage-domains/add-site/">active domain on Cloudflare</a></li>
<li>Domain uses either a <a href="/dns/zone-setups/full-setup/">full setup</a> or a <a href="/dns/zone-setups/partial-setup/">partial (<code>CNAME</code>) setup</a></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4822.md")
</aside>
<h2 id="1-add-your-application-to-access"><ol>
<li>Add your application to Access</li>
</ol></h2>
<div class="video-frame"><img class="video-poster" src="https://pub-d9bf66e086fb4b639107aa52105b49dd.r2.dev/tunnel%203_%20set%20up%20access.png" alt="How to set up Cloudflare Access"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/68749ece14a062ff81eeb1079e0325ed/iframe?preload=true&amp;letterboxColor=transparent" title="How to set up Cloudflare Access" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
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
<h2 id="2-connect-your-origin-to-cloudflare"><ol start="2">
<li>Connect your origin to Cloudflare</li>
</ol></h2>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">Set up a Cloudflare Tunnel</a> to publish your internal application. Only users who match your Access policies will be granted access.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4821.md")
</aside>
<p>If your application is already publicly routable, a tunnel is not strictly required. However, you will then need to protect your origin IP using <a href="/fundamentals/security/protect-your-origin-server/">other methods</a>.</p>
<h2 id="3-validate-the-access-token"><ol start="3">
<li>Validate the Access token</li>
</ol></h2>
<p>To secure your origin, you must validate the <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/">application token</a> issued by Cloudflare Access. Token validation ensures that any requests which bypass Cloudflare Access (for example, due to a network misconfiguration) are rejected.</p>
<p>One option is to configure the Cloudflare Tunnel daemon, <code>cloudflared</code>, to validate the token on your behalf. This is done by enabling <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/origin-parameters/#access"><strong>Protect with Access</strong></a> in your Cloudflare Tunnel settings. Alternatively, if you do not wish to perform automatic validation with Cloudflare Tunnel, you can instead <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/">manually configure your origin</a> to check all requests for a valid token.</p>
<p>Users can now connect to your self-hosted application after authenticating with Cloudflare Access.</p>
<h2 id="partial-cname-setup">Partial (CNAME) setup</h2>
<p>If your domain uses a <a href="/dns/zone-setups/partial-setup/">partial (<code>CNAME</code>) setup</a>, Cloudflare does not manage your DNS zone. You must manually create DNS records at your external provider after adding a published application route to your tunnel.</p>
<h3 id="add-a-published-application-route">Add a published application route</h3>
<p>In the tunnel configuration, <a href="/cloudflare-one/networks/routes/add-routes/#add-a-published-application-route">add a published application route</a> that maps a hostname to your internal service. For example, set the hostname to <code>app.example.com</code> and point it to <code>http://localhost:8080</code>.</p>
<h3 id="create-a-cname-record-at-your-dns-provider">Create a CNAME record at your DNS provider</h3>
<p>In a <a href="/dns/zone-setups/full-setup/">full DNS setup</a>, Cloudflare automatically creates DNS records when you add a published application route to a tunnel. In a partial (<code>CNAME</code>) setup, you must add a CNAME record at the DNS provider that hosts your domain (your authoritative DNS provider).</p>
<p>At your external DNS provider, create a CNAME record with the following values:</p>
<ul>
<li><strong>Name</strong>: The hostname you configured in the tunnel (for example, <code>app.example.com</code>)</li>
<li><strong>Target</strong>: <code>&lt;HOSTNAME&gt;.cdn.cloudflare.net</code> (for example, <code>app.example.com.cdn.cloudflare.net</code>)</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4820.md")
</aside>
<h2 id="product-compatibility">Product compatibility</h2>
<p>When using Access self-hosted applications, the majority of Cloudflare products will be compatible with your application.</p>
<p>However, the following products are not supported:</p>
<ul>
<li><a href="/automatic-platform-optimization">Automatic Platform Optimization</a></li>
<li><a href="/zaraz">Zaraz</a></li>
<li><a href="/google-tag-gateway">Google tag gateway for advertisers</a></li>
</ul>
<p>You can disable Zaraz for a specific application - instead of across your entire zone - using a <a href="/rules/configuration-rules/">Configuration Rule</a> scoped to the application domain.</p>
<p>Google tag gateway is configured at the zone level and cannot be scoped to specific hostnames. To use Access binding cookie on a hostname, disable Google tag gateway for the entire zone.</p>
