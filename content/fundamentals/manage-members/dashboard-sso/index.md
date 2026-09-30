---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/
  description: Configure single sign-on (SSO) for the Cloudflare dashboard using your identity provider to enforce authenticated access for your email domain.
  full_title: Set up dashboard SSO · Cloudflare Fundamentals docs
  head_html: <title>Set up dashboard SSO · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure single sign-on (SSO) for the Cloudflare dashboard using your identity provider to enforce authenticated access for your email domain."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/index.md"><meta property="og:title" content="Set up dashboard SSO · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure single sign-on (SSO) for the Cloudflare dashboard using your identity provider to enforce authenticated access for your email domain."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><meta name="pcx_tags" content="SSO"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/#page","headline":"Set up dashboard SSO \u00b7 Cloudflare Fundamentals docs","description":"Configure single sign-on (SSO) for the Cloudflare dashboard using your identity provider to enforce authenticated access for your email domain.","url":"https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SSO"]}</script>
  markdown: true
  noindex: false
  route: /fundamentals/manage-members/dashboard-sso/
  schema: 1
---
<p>Cloudflare offers single sign-on (SSO) for all customers who log in with a custom email domain. By creating a Cloudflare SSO connector, you can enforce SSO to the Cloudflare dashboard with the identity provider (IdP) of your choice. SSO will be enforced for every user in your email domain.</p>
<h2 id="availability">Availability</h2>
<p>Cloudflare Dashboard SSO is available for free to all plans.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>
<p>You must control your email domain and be able to add a TXT record to verify this.</p>
<ul>
<li>Public email providers such as <code>@gmail.com</code> are not allowed.</li>
<li>Every user with that email domain must be an employee in your organization. For example, university domains such as <code>@harvard.edu</code> are not allowed because they include student emails.</li>
</ul>
</li>
<li>
<p>You must be a super administrator and be able to access the Cloudflare API.</p>
</li>
<li>
<p>A Cloudflare Zero Trust organization with any subscription tier (including Free) must be created. To set up a Cloudflare Zero Trust organization, refer to <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Create a Cloudflare Zero Trust organization</a>.</p>
</li>
</ol>
<h2 id="1-set-up-an-idp"><ol>
<li>Set up an IdP</li>
</ol></h2>
<p>Add an IdP to Cloudflare Zero Trust by following <a href="/cloudflare-one/integrations/identity-providers/">our detailed instructions</a>.</p>
<p>Once you configure your IdP, make sure you also <a href="/cloudflare-one/integrations/identity-providers/#test-idps-in-cloudflare-one">test your IdP</a>.</p>
<h2 id="2-register-your-domain-with-cloudflare-for-sso"><ol start="2">
<li>Register your domain with Cloudflare for SSO</li>
</ol></h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8882.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8885.md")
</div></div>
<h2 id="3-verify-domain-ownership"><ol start="3">
<li>Verify domain ownership</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8888.md")
</div></div>
<p>Once the verification process has completed or timed out, you will receive an email notification with the verification result.</p>
<h2 id="4-enable-dashboard-sso"><ol start="4">
<li>Enable dashboard SSO</li>
</ol></h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8880.md")
</aside>
<p>Once the verification process has completed and successfully verified domain ownership, you may enable the connector.</p>
<p>Domains that are associated with an already enabled connector belonging to a different account may not be enabled on a new account until disabled on the old account.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8891.md")
</div></div>
<h2 id="test-your-idp-before-enforcement">Test your IdP before enforcement</h2>
<p>Before enabling SSO for your domain, verify that your identity provider is configured correctly:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</li>
<li>Find your IdP and select <strong>Test</strong>.</li>
<li>Confirm that the test returns a successful authentication result.</li>
</ol>
<p>If the test fails, review your IdP configuration against the <a href="/cloudflare-one/integrations/identity-providers/">identity provider setup instructions</a> before enabling the SSO connector.</p>
<h3 id="troubleshoot-idp-errors">Troubleshoot IdP errors</h3>
<p>If you encounter errors during IdP setup or testing, provide the following when <a href="/support/contacting-cloudflare-support/">contacting support</a>:</p>
<ol>
<li>The error message returned by the IdP test.</li>
<li>A sanitized <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#generate-a-har-file">HAR file</a> captured while running the IdP test from the dashboard.</li>
</ol>
<h2 id="limitations">Limitations</h2>
<p>Cloudflare dashboard SSO does not support:</p>
<ul>
<li>Users with plus-addressed emails, such as <code>example+2@domain.com</code>. If you have users like this added to your Cloudflare organization, they will be unable to login with SSO.</li>
<li>Adding a separate email-based policy to the Zero Trust SSO application that does not match your SSO domain policy.</li>
<li>Multiple Zero Trust domain policies. If another domain policy is required, you can create another SSO connector. This will create a second policy for that new domain in your SSO application.</li>
<li>Deleting the auto-generated Zero Trust <code>allow email domain</code> policy. If this policy is deleted, your organization's administrators cannot access the Cloudflare dashboard.</li>
</ul>
<h2 id="idp-initiated-sso">IdP-initiated SSO</h2>
<p>IdP-initiated login is supported for Cloudflare dashboard SSO, with configuration available via your identity provider (IdP).</p>
<p>A step-by-step guide is currently available for Okta, and similar configurations are possible with other identity providers that support custom SSO endpoints.</p>
<h3 id="okta">Okta</h3>
<p>Configure an identity provider (IdP)-initiated single sign-on (SSO) session using Cloudflare Zero Trust and Okta.</p>
<h4 id="prerequisites-1">Prerequisites</h4>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong> &gt; select your <strong>SSO App</strong>.</li>
<li>Select <strong>Configure</strong> to access the application settings.</li>
<li>In the <strong>Basic Information</strong> section, copy the <strong>SSO Endpoint URL</strong> and <strong>Access Entity ID or Issuer</strong>. You will need these values for your IdP setup.</li>
</ol>
<h4 id="configure-okta-as-the-idp">Configure Okta as the IdP</h4>
<ol>
<li>Log in to your <a href="https://login.okta.com/">Okta Admin Dashboard</a> and go to <strong>Applications</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create App Integration</strong> to start a new SAML integration to handle the IdP-initiated SSO flow. Note that this is a second, distinct Cloudflare-Okta integration, created separately from the <a href="/cloudflare-one/integrations/identity-providers/">IdP integration with Zero Trust</a>.</li>
<li>In the pop-up, select <strong>SAML 2.0</strong> and select <strong>Next</strong>.</li>
<li>Enter a name for the app and select <strong>Next</strong>.</li>
<li>In the <strong>Single Sign-On URL</strong> field, paste the <strong>SSO Endpoint URL</strong> <a href="/fundamentals/manage-members/dashboard-sso/#prerequisites-1">you copied earlier</a>.</li>
<li>In the <strong>Audience URI (SP Entity ID)</strong> field, paste the <strong>Access Entity ID or Issuer</strong> <a href="/fundamentals/manage-members/dashboard-sso/#prerequisites-1">you copied earlier</a>.</li>
<li>Set the <strong>Name ID Format</strong> to <strong>EmailAddress</strong>.</li>
<li>Set the <strong>Application Username</strong> to <strong>Email</strong>.</li>
<li>Select <strong>Next</strong> &gt; <strong>Finish</strong> to save the integration.</li>
<li>Test the integration by going to your Okta User Dashboard, locating the new app tile, and selecting it to verify the SSO flow.</li>
</ol>
<p><strong>(Optional) Enforce single IdP login with instant authentication</strong></p>
<p>If you use only one IdP (for example, Okta) for Cloudflare SSO and want users to skip the identity provider selection prompt:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong> &gt; select your <strong>SSO App</strong>.</li>
<li>Go to <strong>Authentication</strong>.</li>
<li>Disable <strong>Accept all available identity providers</strong> and ensure only Okta is selected as the login method.</li>
<li>Enable <strong>Apply instant authentication</strong> to allow users to skip identity provider selection.</li>
</ol>
<h2 id="bypass-dashboard-sso">Bypass dashboard SSO</h2>
<p>This section describes how to restore access to the Cloudflare dashboard in case you are unable to login with SSO.</p>
<h3 id="option-1-add-a-backup-idp">Option 1: Add a backup IdP</h3>
<p>If there is an issue with your SSO IdP provider, you can add an alternate IdP using the API. The following example shows how to add <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">Cloudflare One-time PIN</a> as a login method:</p>
<ol>
<li><a href="/api/resources/zero_trust/subresources/identity_providers/methods/create/">Add</a> one-time PIN login:</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/access/identity_providers \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;type&quot;: &quot;onetimepin&quot;,&#10;  &quot;config&quot;: {}&#10;}&#x27;</code></pre>
<ol start="2">
<li><a href="/api/resources/zero_trust/subresources/access/subresources/applications/methods/list/">Get</a> the <code>id</code> of the <code>dash_sso</code> Access application. You can use <a href="https://jqlang.github.io/jq/download/"><code>jq</code></a> to quickly find the correct application:</li>
</ol>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/access/apps&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  | jq &#x27;.result[] | select(.type == &quot;dash_sso&quot;)&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">   {&#10;   	&quot;id&quot;: &quot;3537a672-e4d8-4d89-aab9-26cb622918a1&quot;,&#10;   	&quot;uid&quot;: &quot;3537a672-e4d8-4d89-aab9-26cb622918a1&quot;,&#10;   	&quot;type&quot;: &quot;dash_sso&quot;,&#10;   	&quot;name&quot;: &quot;SSO App&quot;&#10;   	// ...&#10;   }&#10;</code></pre>
<ol start="3">
<li>Using the <code>id</code> obtained above, <a href="/api/resources/zero_trust/subresources/access/subresources/applications/methods/update/">update</a> <strong>SSO App</strong> to accept all identity providers. To avoid overwriting your existing configuration, the PUT request body should contain all fields returned by the previous GET request.</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/access/apps/{app_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;   		id: &quot;3537a672-e4d8-4d89-aab9-26cb622918a1&quot;,&#10;   		uid: &quot;3537a672-e4d8-4d89-aab9-26cb622918a1&quot;,&#10;   		type: &quot;dash_sso&quot;,&#10;   		name: &quot;SSO App&quot;,&#10;   		allowed_idps: [],&#10;   		// ... (other existing properties)&#10;   	}&#x27;</code></pre>
<p>Users will now have the option to log in using a one-time PIN.</p>
<h3 id="option-2-disable-dashboard-sso">Option 2: Disable dashboard SSO</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8879.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8894.md")
</div></div>
<p>Users can now log in using their Cloudflare account email and password. If a user does not have a password, they can use the <a href="/fundamentals/user-profiles/change-password-or-email/#forgot-your-password">forgot password</a> method on the login page to create one.</p>
<h2 id="change-your-zero-trust-team-name">Change your Zero Trust team name</h2>
<p>Cloudflare does not allow you to change your <span class="nb-glossary-tooltip" title="team name">team name</span> while a SSO connector is created. To change your team name, you must disable and delete your SSO connector(s).</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8898.md")
</div></div>
<ol start="4">
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Custom pages</strong>.</li>
<li>Under <strong>Team domain</strong>, select <strong>Edit</strong> to enter the new team name. Select <strong>Save</strong>.</li>
<li>In your identity provider, update your Cloudflare integration with the new team name. For example, if you are using a SAML IdP, you will need to update the Single Sign-on URL and Entity ID to <code>https://&lt;new-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback</code>.</li>
<li>Recreate any deleted SSO connectors using the steps in <a href="/fundamentals/manage-members/dashboard-sso/#2-register-your-domain-with-cloudflare-for-sso">Register your domain with Cloudflare for SSO</a>.</li>
<li>Follow the verification and enable steps after recreating the SSO connectors.</li>
</ol>
