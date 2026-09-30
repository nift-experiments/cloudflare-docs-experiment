---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/
  description: Use Access authentication logs to review authentication events and requests to protected URI paths and infrastructure targets.
  full_title: Access authentication logs · Cloudflare One docs
  head_html: <title>Access authentication logs · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Access authentication logs to review authentication events and requests to protected URI paths and infrastructure targets."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/index.md"><meta property="og:title" content="Access authentication logs · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Access authentication logs to review authentication events and requests to protected URI paths and infrastructure targets."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Logging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/#page","headline":"Access authentication logs \u00b7 Cloudflare One docs","description":"Use Access authentication logs to review authentication events and requests to protected URI paths and infrastructure targets.","url":"https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Logging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/
  schema: 1
---
<p>Access authentication logs help you track who accessed your protected applications, when they accessed them, and whether they were allowed in. Use these logs to investigate suspicious login attempts, audit user activity, or troubleshoot access issues.</p>
<p>Cloudflare Access generates two types of audit logs:</p>
<ul>
<li><strong><a href="#authentication-logs">Authentication audit logs</a></strong> record each login attempt (successful or failed) by a user or service to an Access application.</li>
<li><strong><a href="#per-request-logs">Per-request audit logs</a></strong> record individual HTTP requests that authenticated users make to protected <a href="/cloudflare-one/access-controls/policies/app-paths/">application paths</a> and infrastructure targets.</li>
</ul>
<h2 id="authentication-logs">Authentication logs</h2>
<p>Cloudflare Access logs an authentication event whenever a user or service attempts to log in to an application, whether the attempt succeeds or not.</p>
<p><a href="#identity-based-authentication">Identity-based authentication</a> refers to login attempts that were evaluated based on who the user is — for example, their email address, identity provider (IdP) group, SAML group, or OIDC claim.</p>
<p><a href="#non-identity-authentication">Non-identity authentication</a> refers to login attempts that were evaluated based on context rather than user identity — for example, IP address, device posture, country, valid certificate, or service token.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4982.md")
</aside>
<h3 id="identity-based-authentication">Identity-based authentication</h3>
<h4 id="view-access-authentication-logs">View Access authentication logs</h4>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4985.md")
</div></div>
<h4 id="explanation-of-the-fields">Explanation of the fields</h4>
<p>Identity-based authentication logs contain the following fields:</p>
<h5 id="basic-information">Basic information</h5>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>App</strong></td>
<td>Name of the Access application.</td>
</tr>
<tr>
<td><strong>User email</strong></td>
<td>Email address of the authenticating user.</td>
</tr>
<tr>
<td><strong>User ID</strong></td>
<td>Unique identifier (UUID) of the authenticating user.</td>
</tr>
<tr>
<td><strong>IP address</strong></td>
<td>IP address of the authenticating user.</td>
</tr>
<tr>
<td><strong>App UID</strong></td>
<td>Unique identifier (UUID) of the Access application.</td>
</tr>
<tr>
<td><strong>App domain</strong></td>
<td>URL of the Access application.</td>
</tr>
<tr>
<td><strong>App type</strong></td>
<td>Specifies the type of Access application: self-hosted, browser SSH, browser VNC, browser RDP, SaaS, or infrastructure.</td>
</tr>
<tr>
<td><strong>Event</strong></td>
<td>Type of authentication event, such as a login attempt.</td>
</tr>
<tr>
<td><strong>Connection</strong></td>
<td>Identity provider used to authenticate (for example, <code>saml</code>, <code>onetimepin</code>, <code>google-apps</code>).</td>
</tr>
<tr>
<td><strong>Allow</strong></td>
<td>Whether the authentication attempt was allowed (<code>true</code>) or denied (<code>false</code>).</td>
</tr>
<tr>
<td><strong>Request time</strong></td>
<td>Timestamp of the authentication event.</td>
</tr>
<tr>
<td><strong>Ray ID</strong></td>
<td>A unique identifier for every request through Cloudflare. Useful for tracing a specific request through Cloudflare logs.</td>
</tr>
<tr>
<td><strong>Country</strong></td>
<td>Country associated with the user's IP address.</td>
</tr>
</tbody>
</table>
<h5 id="infrastructure-applications">Infrastructure applications</h5>
<p>Cloudflare Access logs the following information when the user authenticates to an <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">infrastructure application</a>:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Hostname</strong></td>
<td>Hostname of the infrastructure target.</td>
</tr>
<tr>
<td><strong>Target ID</strong></td>
<td>UUID of the infrastructure target.</td>
</tr>
<tr>
<td><strong>SSH user</strong></td>
<td>The UNIX user, such as <code>root</code>, that the authenticating user specified when connecting to the infrastructure target.</td>
</tr>
<tr>
<td><strong>SSH logs</strong></td>
<td>SSH commands that the user ran on the target. Requires configuring an <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#ssh-command-logs">SSH encryption key</a> before the session begins.</td>
</tr>
</tbody>
</table>
<h3 id="non-identity-authentication">Non-identity authentication</h3>
<p>To retrieve logs for non-identity authentication events, use the <a href="/analytics/graphql-api/tutorials/querying-access-login-events/">GraphQL Analytics API</a>. These logs are not available in the Cloudflare One dashboard.</p>
<h2 id="per-request-logs">Per-request logs</h2>
<p>Users who have authenticated through Access have access to authorized URL paths for the duration of their session. Cloudflare provides several ways to audit these requests.</p>
<h3 id="using-cloudflare-logs">Using Cloudflare Logs</h3>
<p>Enterprise customers have access to detailed logs of requests on their Cloudflare dashboard. Enterprise customers also have access to Cloudflare's Logpush service, which can be configured from the Cloudflare dashboard or API. For more information about Cloudflare HTTP and infrastructure logging, refer to <a href="/logs/">Cloudflare Logs</a>.</p>
<p>Once a member of your team authenticates to reach an HTTP resource behind Access, Cloudflare generates a <span class="nb-glossary-tooltip" title="JSON web token">JSON Web Token (JWT)</span> for that user that contains their SSO identity. Cloudflare signs this token using RS256 (RSA Signature with SHA-256), an asymmetric algorithm, and makes the public key available so that you can verify the token is authentic.</p>
<p>When a user requests a URL, Access appends the user identity from that token as a request header, which Cloudflare logs as the request passes through the network. Your team can collect these logs in your preferred third-party Security information and event management (SIEM) software or storage destination by using <a href="/cloudflare-one/insights/logs/logpush/">Cloudflare Logpush</a>. When enabled with the Access user identity field, the logs export to your systems as JSON similar to the example below.</p>
<pre tabindex="0"><code class="language-json">{&#10;   &quot;ClientIP&quot;: &quot;198.51.100.206&quot;,&#10;   &quot;ClientRequestHost&quot;: &quot;jira.widgetcorp.tech&quot;,&#10;   &quot;ClientRequestMethod&quot;: &quot;GET&quot;,&#10;   &quot;ClientRequestURI&quot;: &quot;/secure/Dashboard/jspa&quot;,&#10;   &quot;ClientRequestUserAgent&quot;:&quot;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36&quot;,&#10;   &quot;EdgeEndTimestamp&quot;: &quot;2019-11-10T09:51:07Z&quot;,&#10;   &quot;EdgeResponseBytes&quot;: 4600,&#10;   &quot;EdgeResponseStatus&quot;: 200,&#10;   &quot;EdgeStartTimestamp&quot;: &quot;2019-11-10T09:51:07Z&quot;,&#10;   &quot;RayID&quot;: &quot;5y1250bcjd621y99&quot;,&#10;   &quot;RequestHeaders&quot;:{&quot;cf-access-user&quot;:&quot;srhea&quot;}&#10;},&#10;{&#10;   &quot;ClientIP&quot;: &quot;198.51.100.206&quot;,&#10;   &quot;ClientRequestHost&quot;: &quot;jira.widgetcorp.tech&quot;,&#10;   &quot;ClientRequestMethod&quot;: &quot;GET&quot;,&#10;   &quot;ClientRequestURI&quot;: &quot;/browse/EXP-12&quot;,&#10;   &quot;ClientRequestUserAgent&quot;:&quot;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36&quot;,&#10;   &quot;EdgeEndTimestamp&quot;: &quot;2019-11-10T09:51:27Z&quot;,&#10;   &quot;EdgeResponseBytes&quot;: 4570,&#10;   &quot;EdgeResponseStatus&quot;: 200,&#10;   &quot;EdgeStartTimestamp&quot;: &quot;2019-11-10T09:51:27Z&quot;,&#10;   &quot;RayID&quot;: &quot;yzrCqUhRd6DVz72a&quot;,&#10;   &quot;RequestHeaders&quot;:{&quot;cf-access-user&quot;:&quot;srhea&quot;}&#10;}&#10;</code></pre>
<h3 id="using-the-cf-access-user-field">Using the <code>cf-access-user</code> field</h3>
<p>In addition to the HTTP request fields available in Cloudflare Enterprise logging, requests made to applications behind Access include the <code>cf-access-user</code> field, which contains the user identity string. This offers another tool for auditing user behavior. To add the <code>cf-access-user</code> field to your HTTP request logs, you must add it as a custom field. Refer to <a href="/logs/logpush/logpush-job/custom-fields/">Custom fields</a> for instructions.</p>
<p>Keep in mind that Access does not log all interactions. Per-request audit logs can indicate that a specific user visited <code>domain.com/admin</code> and then <code>domain.com/admin/panel</code>, but the logs only capture interactions that result in a new HTTP request. Purely client-side interactions that do not generate server requests are not logged.</p>
