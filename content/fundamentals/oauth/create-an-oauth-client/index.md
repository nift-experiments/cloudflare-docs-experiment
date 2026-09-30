<h2 id="prerequisites">Prerequisites</h2>
<p>To create an OAuth client, you must have one of these roles for the associated account: Super Administrator, Administrator, or OAuth Client Write.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8832.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8828.md")
</aside>
<h2 id="select-scopes">Select scopes</h2>
<p>OAuth scope names correspond to Cloudflare API token permission names. Use the Cloudflare API documentation to identify the permissions your client needs.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8835.md")
</div></div>
<h2 id="supported-oauth-flows">Supported OAuth flows</h2>
<p>Cloudflare OAuth clients support the OAuth 2.0 Authorization Code flow.</p>
<p>Cloudflare does not support Client Credentials, Implicit, Resource Owner Password Credentials, Device Authorization, or other OAuth grant types for third-party clients.</p>
<h3 id="choose-a-flow">Choose a flow</h3>
<p>Use the following guidance to choose an OAuth flow:</p>
<table>
<thead>
<tr>
<th>Client type</th>
<th>Flow</th>
<th>Token endpoint authentication</th>
<th>PKCE</th>
</tr>
</thead>
<tbody>
<tr>
<td>Server-side web app or backend service</td>
<td>Authorization Code with a client secret</td>
<td><code>client_secret_basic</code> or <code>client_secret_post</code></td>
<td>Optional/not required</td>
</tr>
<tr>
<td>Browser-based, mobile, desktop, or CLI app</td>
<td>Authorization Code with PKCE</td>
<td><code>none</code></td>
<td>Required, <code>S256</code></td>
</tr>
</tbody>
</table>
<h3 id="client-secret">Client secret</h3>
<p>The Authorization Code flow is intended for secure server-side applications that can protect a client secret from exposure.</p>
<ul>
<li><strong>Use when:</strong> Your OAuth client is a server-side web application or backend service.</li>
<li><strong>How it works:</strong> Your client redirects the user to the authorization page. After authorization, Cloudflare returns an authorization code to your backend. Your backend exchanges the code and client secret for an access token.</li>
<li><strong>Security note:</strong> Never expose your client secret in client-side code or embed it in mobile client binaries.</li>
</ul>
<h3 id="pkce">PKCE</h3>
<p>Proof Key for Code Exchange (PKCE) extends the Authorization Code flow for public clients, such as mobile or single-page apps, where a client secret cannot be securely stored.</p>
<ul>
<li><strong>Use when:</strong> Your OAuth client is a single-page, mobile, desktop, or CLI application.</li>
<li><strong>How it works:</strong> Your application generates a unique code verifier and code challenge for every login request instead of using a static client secret.</li>
<li><strong>Security note:</strong> Clients that use PKCE do not need a client secret.</li>
</ul>
<h2 id="private-and-public-clients">Private and public clients</h2>
<p>New OAuth clients default to private visibility. Private clients can only be authorized by members of the parent Cloudflare account. Public clients allow authorization from any Cloudflare user.</p>
<p>Before you make a client public, complete the required actions and populate the required fields.</p>
<h3 id="required-fields">Required fields</h3>
<ul>
<li>Client name</li>
<li>Logo</li>
<li>Client URL</li>
<li>Scopes</li>
</ul>
<h3 id="required-actions">Required actions</h3>
<p>OAuth clients must complete <a href="#client-url-domain-ownership-verification">domain verification</a> for the client URL before they can be made public.</p>
<h3 id="promote-a-client-to-public">Promote a client to public</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8827.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8839.md")
</div></div>
<h2 id="client-url-domain-ownership-verification">Client URL domain ownership verification</h2>
<p>Cloudflare requires client URL domain ownership verification before a client can become public. If your client is only for private use by members of the account, domain ownership verification is not required.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8826.md")
</aside>
<p>Copy the verification code and create a <code>TXT</code> record in your DNS configuration with that value. The record must include all text, including the <code>cloudflare_oauth_client_publisher=</code> prefix.</p>
<p>Cloudflare polls this DNS record until it is found or until the request times out after two days.</p>
<h3 id="restart-verification">Restart verification</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8842.md")
</div></div>
<h2 id="rotate-client-secrets">Rotate client secrets</h2>
<p>Each client can have two secrets. This lets you create a new secret, update your client to use the new secret, and delete the old secret.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8846.md")
</div></div>
