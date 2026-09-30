<p><a href="/cloudflare-one/faq/">❮ Back to FAQ</a></p>
<h2 id="can-access-work-with-multiple-identity-providers-at-the-same-time">Can Access work with multiple identity providers at the same time?</h2>
<p>Yes. Your team can simultaneously use multiple providers, reducing friction when working with partners or contractors. Get started by adding your preferred identity providers as login methods in Zero Trust. Then, when securing a new application behind Access, you'll be able to choose which providers you want your users to log in with to reach that application.</p>
<h2 id="what-if-the-identity-provider-my-team-uses-is-not-listed">What if the identity provider my team uses is not listed?</h2>
<p>You can add your preferred identity providers to Cloudflare Access even if you do not see them listed in Zero Trust, as long as these providers support SAML 2.0 or <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/">OpenID Connect (OIDC)</a>.</p>
<h2 id="how-do-end-users-log-out-of-an-application-protected-by-access">How do end users log out of an application protected by Access?</h2>
<p>Access provides a URL that will end a user's current session.</p>
<p>To force log out of an Access application, go to:</p>
<p><code>&lt;your-application-domain&gt;/cdn-cgi/access/logout</code></p>
<p>To log out of an App Launcher session, go to:</p>
<p><code>&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/logout</code></p>
<p>For more information, refer to our <a href="/cloudflare-one/access-controls/access-settings/session-management/#log-out-as-a-user">session management page</a>.</p>
