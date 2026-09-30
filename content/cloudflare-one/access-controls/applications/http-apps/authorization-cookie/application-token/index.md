---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/
  description: Learn how Cloudflare Access uses application tokens to secure your origin. Understand JWT structure and payloads.
  full_title: Application token · Cloudflare One docs
  head_html: <title>Application token · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how Cloudflare Access uses application tokens to secure your origin. Understand JWT structure and payloads."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/index.md"><meta property="og:title" content="Application token · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how Cloudflare Access uses application tokens to secure your origin. Understand JWT structure and payloads."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="JSON web token (JWT)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/#page","headline":"Application token \u00b7 Cloudflare One docs","description":"Learn how Cloudflare Access uses application tokens to secure your origin. Understand JWT structure and payloads.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JSON web token (JWT)"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/
  schema: 1
---
<p>Cloudflare Access includes the application token with all authenticated requests to your origin. A typical JWT looks like this:</p>
<p><code>eyJhbGciOiJSUzI1NiIsImtpZCI6IjkzMzhhYmUxYmFmMmZlNDkyZjY0.eyJhdWQiOlsiOTdlMmFhZ TEyMDEyMWY5MDJkZjhiYzk5ZmMzNDU5MTNh.zLYsHmLEginAQUXdygQo08gLTExWNXsN4jBc6PKdB</code></p>
<p>As shown above, the JWT contains three Base64-URL values separated by dots:</p>
<ul>
<li><a href="#header">Header</a></li>
<li><a href="#payload">Payload</a></li>
<li><a href="#signature">Signature</a></li>
</ul>
<p>Unless your application is connected to Access through Cloudflare Tunnel, your application must <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/">validate the token</a> to ensure the security of your origin. Validation of the header alone is not sufficient — the JWT and signature must be confirmed to avoid identity spoofing.</p>
<h2 id="header">Header</h2>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;alg&quot;: &quot;RS256&quot;,&#10;	&quot;kid&quot;: &quot;9338abe1baf2fe492f646a736f25afbf7b025e35c627be4f60c414d4c73069b8&quot;,&#10;	&quot;typ&quot;: &quot;JWT&quot;&#10;}&#10;</code></pre>
<ul>
<li><code>alg</code> identifies the encoding algorithm.</li>
<li><code>kid</code> identifies the key used to sign the token.</li>
<li><code>typ</code> designates the token format.</li>
</ul>
<h2 id="payload">Payload</h2>
<p>The payload contains the actual claim and user information to pass to the application. Payload contents vary depending on whether you authenticated to the application with an identity provider or with a <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service token</a>.</p>
<h3 id="identity-based-authentication">Identity-based authentication</h3>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;aud&quot;: [&quot;32eafc7626e974616deaf0dc3ce63d7bcbed58a2731e84d06bc3cdf1b53c4228&quot;],&#10;	&quot;email&quot;: &quot;user@example.com&quot;,&#10;	&quot;exp&quot;: 1659474457,&#10;	&quot;iat&quot;: 1659474397,&#10;	&quot;nbf&quot;: 1659474397,&#10;	&quot;iss&quot;: &quot;https://yourteam.cloudflareaccess.com&quot;,&#10;	&quot;type&quot;: &quot;app&quot;,&#10;	&quot;identity_nonce&quot;: &quot;6ei69kawdKzMIAPF&quot;,&#10;	&quot;sub&quot;: &quot;7335d417-61da-459d-899c-0a01c76a2f94&quot;,&#10;	&quot;country&quot;: &quot;US&quot;&#10;}&#10;</code></pre>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>aud</td>
<td><a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/#get-your-aud-tag">Application audience (AUD) tag</a> of the Access application.</td>
</tr>
<tr>
<td>email</td>
<td>The email address of the authenticated user, verified by the identity provider.</td>
</tr>
<tr>
<td>exp</td>
<td>The expiration timestamp for the token (Unix time).</td>
</tr>
<tr>
<td>iat</td>
<td>The issuance timestamp for the token (Unix time).</td>
</tr>
<tr>
<td>nbf</td>
<td>The not-before timestamp for the token (Unix time), used to check if the token was received before it should be used.</td>
</tr>
<tr>
<td>iss</td>
<td>The Cloudflare Access domain URL for the application.</td>
</tr>
<tr>
<td>type</td>
<td>The type of Access token (<code>app</code> for application token or <code>org</code> for global session token).</td>
</tr>
<tr>
<td>identity_nonce</td>
<td>A cache key used to get the <a href="#user-identity">user's identity</a>.</td>
</tr>
<tr>
<td>sub</td>
<td>The ID of the user. This value is unique to an email address per account. The user would get a different <code>sub</code> if they are <a href="/cloudflare-one/team-and-resources/users/seat-management/#remove-a-user">removed</a> and re-added to your Zero Trust organization, or if they log into a different organization.</td>
</tr>
<tr>
<td>country</td>
<td>The country where the user authenticated from.</td>
</tr>
</tbody>
</table>
<h4 id="custom-saml-attributes-and-oidc-claims">Custom SAML attributes and OIDC claims</h4>
<p>Access allows you to add custom SAML attributes and OIDC claims to your JWT for enhanced verification, if supported by your identity provider. This is configured when you setup your <a href="/cloudflare-one/integrations/identity-providers/generic-saml/">SAML</a> or <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/">OIDC</a> provider. Identity provider groups are only included in the token when you explicitly configure <code>groups</code> as a custom SAML attribute or OIDC claim. Access does not add them automatically.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="custom-claims-may-be-trimmed-to-fit-cookie-size-limits">Custom claims may be trimmed to fit cookie size limits</h3>
@markup("md", "content/.markup/bodies/4888.md")
</aside>
<h4 id="user-identity">User identity</h4>
<p>User identity is useful for checking application permissions. For example, your application can validate that a given user is a member of an Okta or Microsoft Entra ID group such as <code>Finance-Team</code>.</p>
<p>Due to cookie size limits and bandwidth considerations, the application token only contains a subset of the user's identity. To get the user's full identity, send the <code>CF_Authorization</code> cookie to <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/get-identity</code>. Your request should be structured as follows:</p>
<pre tabindex="0"><code class="language-sh">curl -H &#x27;cookie: CF_Authorization=&lt;user-token&gt;&#x27; https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/get-identity&#10;</code></pre>
<p>Access will return a JSON structure containing the following data:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>email</td>
<td>The email address of the user.</td>
</tr>
<tr>
<td>idp</td>
<td>Data from your identity provider.</td>
</tr>
<tr>
<td>geo</td>
<td>The country where the user authenticated from.</td>
</tr>
<tr>
<td>user_uuid</td>
<td>The ID of the user.</td>
</tr>
<tr>
<td>devicePosture</td>
<td>The device posture attributes.</td>
</tr>
<tr>
<td>account_id</td>
<td>The account ID for your organization.</td>
</tr>
<tr>
<td>iat</td>
<td>The timestamp indicating when the user logged in.</td>
</tr>
<tr>
<td>ip</td>
<td>The IP address of the user.</td>
</tr>
<tr>
<td>auth_status</td>
<td>The status if authenticating with mTLS.</td>
</tr>
<tr>
<td>common_name</td>
<td>The common name on the mTLS client certificate.</td>
</tr>
<tr>
<td>service_token_id</td>
<td>The Client ID of the service token used for authentication.</td>
</tr>
<tr>
<td>service_token_status</td>
<td>True if authentication was through a service token instead of an IdP.</td>
</tr>
<tr>
<td>is_warp</td>
<td>True if the user enabled WARP.</td>
</tr>
<tr>
<td>is_gateway</td>
<td>True if the user enabled the Cloudflare One Client and authenticated to a Zero Trust team.</td>
</tr>
<tr>
<td>gateway_account_id</td>
<td>An ID generated by the Cloudflare One Client when authenticated to a Zero Trust team.</td>
</tr>
<tr>
<td>device_id</td>
<td>The ID of the device used for authentication.</td>
</tr>
<tr>
<td>version</td>
<td>The version of the <code>get-identity</code> object.</td>
</tr>
<tr>
<td>device_sessions</td>
<td>A list of all sessions initiated by the user.</td>
</tr>
</tbody>
</table>
<h3 id="service-token-authentication">Service token authentication</h3>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;type&quot;: &quot;app&quot;,&#10;	&quot;aud&quot;: [&quot;32eafc7626e974616deaf0dc3ce63d7bcbed58a2731e84d06bc3cdf1b53c4228&quot;],&#10;	&quot;exp&quot;: 1659474457,&#10;	&quot;iss&quot;: &quot;https://yourteam.cloudflareaccess.com&quot;,&#10;	&quot;common_name&quot;: &quot;e367826f93b8d71185e03fe518aff3b4.access&quot;,&#10;	&quot;iat&quot;: 1659474397,&#10;	&quot;sub&quot;: &quot;&quot;&#10;}&#10;</code></pre>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>type</td>
<td>The type of Access token (<code>app</code> for application token or <code>org</code> for global session token).</td>
</tr>
<tr>
<td>aud</td>
<td>The <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/#get-your-aud-tag">application audience (AUD) tag</a> of the Access application.</td>
</tr>
<tr>
<td>exp</td>
<td>The expiration timestamp of the JWT (Unix time).</td>
</tr>
<tr>
<td>iss</td>
<td>The Cloudflare Access domain URL for the application.</td>
</tr>
<tr>
<td>common_name</td>
<td>The Client ID of the service token (<code>CF-Access-Client-Id</code>).</td>
</tr>
<tr>
<td>iat</td>
<td>The issuance timestamp of the JWT (Unix time).</td>
</tr>
<tr>
<td>sub</td>
<td>Contains an empty string when authentication was through a service token.</td>
</tr>
</tbody>
</table>
<h2 id="signature">Signature</h2>
<p>Cloudflare generates the signature by signing the encoded header and payload using the SHA-256 algorithm (RS256). In RS256, a private key signs the JWTs and a separate <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/#access-signing-keys">public key</a> verifies the signature.</p>
<p>For more information on JWTs, refer to <a href="https://jwt.io/">jwt.io</a>.</p>
