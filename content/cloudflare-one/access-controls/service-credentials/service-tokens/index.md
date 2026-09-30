---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/
  description: Service tokens in Access.
  full_title: Service tokens · Cloudflare One docs
  head_html: <title>Service tokens · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Service tokens in Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/index.md"><meta property="og:title" content="Service tokens · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Service tokens in Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="JSON web token (JWT),Authentication"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/#page","headline":"Service tokens \u00b7 Cloudflare One docs","description":"Service tokens in Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JSON web token (JWT)","Authentication"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/service-credentials/service-tokens/
  schema: 1
---
<p>You can provide automated systems with service tokens to authenticate against your Cloudflare One policies. Cloudflare Access will generate service tokens that consist of a Client ID and a Client Secret. Automated systems or applications can then use these values to reach an application protected by Access.</p>
<p>This section covers how to create, rotate, renew, disable, and revoke a service token.</p>
<h2 id="create-a-service-token">Create a service token</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4545.md")
</div></div>
<p>You can now configure your Access applications and <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/#check-for-service-token">device enrollment permissions</a> to accept this service token. Make sure to set the policy action to <a href="/cloudflare-one/access-controls/policies/#service-auth"><strong>Service Auth</strong></a>; otherwise, Access will prompt for an identity provider login.</p>
<h3 id="client-secret-format">Client Secret format</h3>
<p>As of August 26, 2026, new service token Client Secrets use the format <code>cfast_[40 alphanumeric characters][8-character checksum]</code>. The prefix and checksum make the secrets easier for credential scanning tools to identify.</p>
<p>Existing Client Secrets use a 64-character hexadecimal format. These secrets continue to work and do not require rotation. Both formats use the same Client ID and authentication headers.</p>
<h2 id="connect-your-service-to-access">Connect your service to Access</h2>
<h3 id="request">Request</h3>
<p>To authenticate to an Access application using your service token, add the following to the headers of any HTTP request:</p>
<p><code>CF-Access-Client-Id: &lt;CLIENT_ID&gt;</code></p>
<p><code>CF-Access-Client-Secret: &lt;CLIENT_SECRET&gt;</code></p>
<p>For example,</p>
<pre tabindex="0"><code class="language-sh">curl -H &quot;CF-Access-Client-Id: &lt;CLIENT_ID&gt;&quot; -H &quot;CF-Access-Client-Secret: &lt;CLIENT_SECRET&gt;&quot; https://app.example.com&#10;</code></pre>
<h4 id="authenticate-with-a-single-header">Authenticate with a single header</h4>
<p>You can configure a self-hosted Access application to accept a service token in a single HTTP header, as an alternative to the <code>CF-Access-Client-Id</code> and <code>CF-Access-Client-Secret</code> pair of headers. This is useful for authenticating SaaS services that only support sending one custom header in a request (for example, the <code>Authorization</code> header).</p>
<p>To authenticate using a single header:</p>
<ol>
<li>Get your existing Access application configuration:</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/access/apps/{app_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<ol start="2">
<li>Make a <code>PUT</code> request with the name of the header you want to use for service token authentication. To avoid overwriting your existing configuration, the <code>PUT</code> request body should contain all fields returned by the previous <code>GET</code> request.</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/access/apps/{app_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;domain&quot;: &quot;app.example.com&quot;,&#10;  &quot;type&quot;: &quot;self_hosted&quot;,&#10;  &quot;read_service_tokens_from_header&quot;: &quot;Authorization&quot;&#10;}&#x27;</code></pre>
<ol start="3">
<li>Add the header to any HTTP request. For example,</li>
</ol>
<pre tabindex="0"><code class="language-sh">curl -H &quot;Authorization: {\&quot;cf-access-client-id\&quot;: \&quot;&lt;CLIENT_ID&gt;\&quot;, \&quot;cf-access-client-secret\&quot;: \&quot;&lt;CLIENT_SECRET&gt;\&quot;}&quot; https://app.example.com&#10;</code></pre>
<h2 id="rotate-service-token-secrets">Rotate service token secrets</h2>
<p>Rotate a service token secret when you suspect exposure or as part of regular credential rotation. The Client ID remains the same, but Access generates a new Client Secret.</p>
<p>You can set a grace period during which both secrets work. Use this period to update your services before Access revokes the previous secret.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4549.md")
</div></div>
<h2 id="renew-service-tokens">Renew service tokens</h2>
<p>Service tokens expire according to the token duration you selected when you created the token.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4553.md")
</div></div>
<h2 id="turn-a-service-token-on-or-off">Turn a service token on or off</h2>
<p>Turn off a service token to temporarily prevent it from authenticating. Access preserves the token so you can turn it on again later.</p>
<p>Turning off a token also stops its previous secret from working during an active rotation grace period.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4557.md")
</div></div>
<h2 id="revoke-service-tokens">Revoke service tokens</h2>
<p>If you need to revoke access before the token expires, delete the token. Services that rely on a deleted service token can no longer reach your application.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4561.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4537.md")
</aside>
<h2 id="set-a-token-expiration-alert">Set a token expiration alert</h2>
<p>An alert can be configured to notify a week before a service token expires to allow an administrator to invoke a token refresh.</p>
<details><summary>Expiring Access Service Token Alert</summary><strong>Who is it for?</strong><p><a href="/cloudflare-one/access-controls/policies/">Access</a> customers who want to receive a notification when their service token is about to expire.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of Access</p>
<strong>What should you do if you receive one?</strong><p>Extend the expiration date of the service token. For more details, refer to <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/#renew-service-tokens">Renew your service token</a>.</p>
</details>
<p>To configure a service token expiration alert:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Add**.
3. Select _Expiring Access Service Token_.
4. Enter a name for your alert and an optional description.
5. (Optional) Add other recipients for the notification email.
6. Select **Save**.
<p>Your alert has been set and is now visible on the <strong>Notifications</strong> page.</p>
