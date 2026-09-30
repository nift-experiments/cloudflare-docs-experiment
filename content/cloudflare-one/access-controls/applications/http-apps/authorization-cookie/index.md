---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/
  description: Learn how Cloudflare Access uses CF_Authorization cookies to secure self-hosted web applications.
  full_title: Authorization cookie · Cloudflare One docs
  head_html: <title>Authorization cookie · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how Cloudflare Access uses CF_Authorization cookies to secure self-hosted web applications."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/index.md"><meta property="og:title" content="Authorization cookie · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how Cloudflare Access uses CF_Authorization cookies to secure self-hosted web applications."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Cookies,JSON web token (JWT)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#page","headline":"Authorization cookie \u00b7 Cloudflare One docs","description":"Learn how Cloudflare Access uses CFAuthorization cookies to secure self-hosted web applications.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Cookies","JSON web token (JWT)"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/authorization-cookie/
  schema: 1
---
<p>When you protect a site with Cloudflare Access, Cloudflare checks every HTTP request bound for that site to ensure that the request has a valid <code>CF_Authorization</code> cookie. If a request does not include the cookie, Access will block the request.</p>
<h2 id="access-jwts">Access JWTs</h2>
<p>The <code>CF_Authorization</code> cookie contains the user's identity in the form of a <a href="https://www.cloudflare.com/learning/access-management/token-based-authentication/">JSON Web Token (JWT)</a>. Cloudflare securely creates these tokens through the OAUTH or SAML integration between Cloudflare Access and the configured identity provider.</p>
<p>Access generates two separate <code>CF_Authorization</code> tokens depending on the domain:</p>
<ul>
<li><strong>Global session token</strong>: Generated when a user logs in to Access. This token is stored as a cookie at your <span class="nb-glossary-tooltip" title="team domain">team domain</span> (for example, <code>https://&lt;your-team-name&gt;.cloudflareaccess.com</code>) and prevents a user from needing to log in to each application.</li>
<li><a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/"><strong>Application token</strong></a>: Generated for each application that a user reaches. This token is stored as a cookie on the protected domain (for example, <code>https://jira.site.com</code>) and may be used to <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json">validate requests</a> on your origin.</li>
</ul>
<h3 id="multi-domain-applications">Multi-domain applications</h3>
<p>Cloudflare Access allows you to protect and manage multiple domains in a single <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted application</a>. After a user has successfully authenticated to one domain, Access will automatically issue a <code>CF_Authorization</code> cookie when they go to another domain in the same Access application. This means that users only need to authenticate once to a multi-domain application.</p>
<p>Access can preemptively set the cookie for every domain through a series of redirects when the user first authenticates. This allows single-page applications (SPAs) to retrieve data from other subdomains before the user visits each subdomain. Wildcarded subdomains (for example, <code>*.example.com</code>) cannot receive preemptive cookies because Access does not know which concrete subdomain to redirect to. Wildcarded paths are supported.</p>
<p>Use the <a href="#eager-redirect-cookie">Eager redirect cookie</a> setting to control this behavior.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4879.md")
</aside>
<h2 id="access-cookies">Access cookies</h2>
<p>The following Access cookies are essential to Access functionality. Cookies that are marked as required cannot be opted out of. The following cookies are not used for tracking or analytics.</p>
<h3 id="cf-authorization-team-domain">CF_Authorization (team domain)</h3>
<table>
<thead>
<tr>
<th>Details</th>
<th>Expiration</th>
<th>HttpOnly</th>
<th>SameSite</th>
<th>Required?</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#access-jwts">JSON web token (JWT)</a> set on the <code>cloudflareaccess.com</code> <a href="/cloudflare-one/faq/getting-started-faq/#what-is-a-team-domainteam-name">team domain</a> that contains the user's identity and enables Access to perform single sign-on (SSO)</td>
<td><details><summary>View</summary>If set, adheres to <a href="/cloudflare-one/access-controls/access-settings/session-management/#global-session-duration">global session duration</a>.<br/><br/>If not, adheres to <a href="/cloudflare-one/access-controls/access-settings/session-management/#application-session-duration">application session duration</a>.<br/><br/>If neither are set, defaults to 24 hours.
</details></td>
<td>Yes</td>
<td>None</td>
<td>Required</td>
</tr>
</tbody>
</table>
<h3 id="cf-authorization-access-application-domain">CF_Authorization (Access application domain)</h3>
<table>
<thead>
<tr>
<th>Details</th>
<th>Expiration</th>
<th>HttpOnly</th>
<th>SameSite</th>
<th>Required?</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#access-jwts">JSON web token (JWT)</a> set on the domain protected by Access that allows Access to confirm that the user has been authenticated and is authorized to reach the origin</td>
<td><details><summary>View</summary>If set, adheres to <a href="/cloudflare-one/access-controls/access-settings/session-management/#policy-session-duration">policy session duration</a>.<br/><br/>If not, adheres to <a href="/cloudflare-one/access-controls/access-settings/session-management/#application-session-duration">application session duration</a>.<br/><br/>If neither are set, defaults to 24 hours.
</details></td>
<td>Admin choice (Default: None)</td>
<td>Admin choice (Default: None)</td>
<td>Required</td>
</tr>
</tbody>
</table>
<h3 id="cf-binding">CF_Binding</h3>
<table>
<thead>
<tr>
<th>Details</th>
<th>Expiration</th>
<th>HttpOnly</th>
<th>SameSite</th>
<th>Required?</th>
</tr>
</thead>
<tbody>
<tr>
<td>Refer to <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#binding-cookie">Binding cookie</a></td>
<td><details><summary>View</summary>If set, adheres to <a href="/cloudflare-one/access-controls/access-settings/session-management/#policy-session-duration">policy session duration</a>.<br/><br/>If not, adheres to <a href="/cloudflare-one/access-controls/access-settings/session-management/#application-session-duration">application session duration</a>.<br/><br/>If neither are set, defaults to 24 hours.
</details></td>
<td>Yes</td>
<td>None</td>
<td>Optional</td>
</tr>
</tbody>
</table>
<h3 id="cf-session">CF_Session</h3>
<table>
<thead>
<tr>
<th>Details</th>
<th>Expiration</th>
<th>HttpOnly</th>
<th>SameSite</th>
<th>Required?</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://www.cloudflare.com/learning/security/threats/cross-site-request-forgery/">CSRF</a> token used on the <code>cloudflareaccess.com</code> <a href="/cloudflare-one/faq/getting-started-faq/#what-is-a-team-domainteam-name">team domain</a></td>
<td>4 hours</td>
<td>Yes</td>
<td>None</td>
<td>Required</td>
</tr>
</tbody>
</table>
<h3 id="cf-appsession">CF_AppSession</h3>
<table>
<thead>
<tr>
<th>Details</th>
<th>Expiration</th>
<th>HttpOnly</th>
<th>SameSite</th>
<th>Required?</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://www.cloudflare.com/learning/security/threats/cross-site-request-forgery/">CSRF</a> token used per application domain, scoped to individual applications behind Access</td>
<td>24 hours</td>
<td>Yes</td>
<td>None</td>
<td>Required</td>
</tr>
</tbody>
</table>
<h3 id="cf-device">CF_Device</h3>
<table>
<thead>
<tr>
<th>Details</th>
<th>Expiration</th>
<th>HttpOnly</th>
<th>SameSite</th>
<th>Required?</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cookie set on the <code>cloudflareaccess.com</code> <a href="/cloudflare-one/faq/getting-started-faq/#what-is-a-team-domainteam-name">team domain</a>, used to prevent abuse of <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time PIN</a> and <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">multi-factor authentication</a> flows</td>
<td>30 days</td>
<td>Yes</td>
<td>Strict</td>
<td>Required</td>
</tr>
</tbody>
</table>
<h2 id="cookie-settings">Cookie settings</h2>
<p>Cloudflare Access provides optional security settings that can be added to the browser cookies generated by Access for an authenticated user.</p>
<ul>
<li><a href="#samesite-attribute">SameSite</a></li>
<li><a href="#httponly">HttpOnly flag</a></li>
<li><a href="#binding-cookie">Binding cookie</a></li>
<li><a href="#cookie-path-attribute">Cookie path</a></li>
<li><a href="#eager-redirect-cookie">Eager redirect cookie</a></li>
</ul>
<p>To enable these settings:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Locate the application you would like to configure and select <strong>Configure</strong>.</li>
<li>Select <strong>Advanced settings</strong> and scroll down to <strong>Cookie settings</strong>.</li>
<li>Configure the desired cookie settings.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h3 id="samesite-attribute">SameSite Attribute</h3>
<p>The <a href="https://web.dev/samesite-cookies-explained/"><code>SameSite</code></a> Attribute selector restricts the cookie to only being sent if the cookie's defined site matches the site being requested in the browser. This adds protection against <a href="https://en.wikipedia.org/wiki/Cross-site_request_forgery">cross-site request forgery (CSRF)</a>.</p>
<p>The selector options are:</p>
<ul>
<li><strong>None</strong> - Cookies will be sent in all contexts, including cross-origin requests.</li>
<li><strong>Lax</strong> - Cookies are allowed to be sent with top-level navigations and will be sent along with GET requests initiated by third party websites.</li>
<li><strong>Strict</strong> - Cookies will only be sent in a first-party context and not be sent along with requests initiated by third party websites.</li>
</ul>
<p>Refer to the <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie#samesitesamesite-value">Mozilla documentation</a> for more information.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4878.md")
</aside>
<h4 id="when-not-to-use-samesite">When not to use SameSite</h4>
<p>Do not enable <code>SameSite</code> restrictions if you have additional sites or applications that rely on a specific application's authorization cookie.</p>
<h3 id="httponly">HttpOnly</h3>
<p>The <code>HttpOnly</code> flag is a cookie attribute that prevents the cookie from being accessed by any client-side scripts, reducing the likelihood of Cross-Site Scripting (XSS) attacks. This flag is enabled by default.</p>
<h4 id="when-not-to-use-httponly">When not to use HttpOnly</h4>
<p>Do not enable <code>HttpOnly</code> if:</p>
<ul>
<li>You are using the Access application for non-browser based tools (such as SSH or RDP).</li>
<li>You have software that relies on being able to access a user's cookie generated by Access.</li>
</ul>
<h3 id="binding-cookie">Binding cookie</h3>
<p>The binding cookie (<code>CF_Binding</code>) is an optional cookie issued when a user successfully authenticates. The binding cookie is sent by the user's browser and tied to a specific application's <code>CF_Authorization</code> cookie. This cookie is stripped at Cloudflare's network and never forwarded to the origin server.</p>
<p>The <code>CF_Authorization</code> cookie cannot be used without the associated binding cookie, which prevents a stolen <code>CF_Authorization</code> cookie from being reused by an attacker. If a request arrives at Cloudflare's network with a valid <code>CF_Authorization</code> cookie but without the expected binding cookie, Cloudflare rejects the request.</p>
<h4 id="when-not-to-use-binding-cookie">When not to use Binding Cookie</h4>
<p>Do not enable Binding Cookie if:</p>
<ul>
<li>You are using the Access application for non-browser based tools (such as SSH or RDP).</li>
<li>You have enabled <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/#product-compatibility">incompatible Cloudflare products</a> on the application domain, such as <a href="/zaraz">Zaraz</a> or <a href="/google-tag-gateway/">Google tag gateway</a>. Enabling Binding Cookie alongside these products can cause an authentication redirect loop (<code>ERR_TOO_MANY_REDIRECTS</code>).</li>
<li>You have turned on <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/">Authenticate with Cloudflare One Client</a> for the application.</li>
</ul>
<h3 id="cookie-path-attribute">Cookie Path Attribute</h3>
<p>The Cookie Path Attribute adds the application's path URL to the <code>CF_Authorization</code> cookie. When enabled, a user who logs in to <code>example.com/path1</code> must re-authenticate to access <code>example.com/path2</code>. When disabled, the <code>CF_Authorization</code> cookie is only scoped to the domain and subdomain.</p>
<h3 id="eager-redirect-cookie">Eager redirect cookie</h3>
<p>When turned on, the Eager redirect cookie setting preemptively sets a <code>CF_Authorization</code> cookie for every concrete domain in a multi-domain application. Access redirects the browser through each domain after the user first authenticates. This setting is turned on by default for new applications.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4877.md")
</aside>
<h2 id="allow-third-party-cookies-in-the-browser">Allow third-party cookies in the browser</h2>
<p>By default, some browsers block all third-party cookies in private browsing mode, including the <code>CF_Authorization</code> cookie. For XHR requests to work in private windows, you will need to exempt your application and <span class="nb-glossary-tooltip" title="team domain">team domain</span> from the browser's tracking protection system.</p>
<p>To enable third-party cookies for an Access application:</p>
<details class="nb-details"><summary>Chrome</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4882.md")
</div></details>
<details class="nb-details"><summary>Safari</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4883.md")
</div></details>
<details class="nb-details"><summary>Firefox</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4884.md")
</div></details>
<details class="nb-details"><summary>Brave</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4885.md")
</div></details>
