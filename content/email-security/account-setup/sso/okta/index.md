---
cp9:
  canonical: https://developers.cloudflare.com/email-security/account-setup/sso/okta/
  description: Connect your Email Security account to Okta for SAML-based single sign-on authentication.
  full_title: Okta integration guide · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Okta integration guide · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect your Email Security account to Okta for SAML-based single sign-on authentication."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/account-setup/sso/okta/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/account-setup/sso/okta/index.md"><meta property="og:title" content="Okta integration guide · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect your Email Security account to Okta for SAML-based single sign-on authentication."><meta property="og:url" content="https://developers.cloudflare.com/email-security/account-setup/sso/okta/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/account-setup/sso/okta/
  schema: 1
---
<p>In this tutorial you will learn how to connect your Email security (formerly Area 1) account to Okta. When single sign-on (SSO) is correctly configured, your authorized employees can connect to the Email security dashboard using a familiar user name and password.</p>
<h2 id="1-create-an-email-security-app-in-okta"><ol>
<li>Create an Email security app in Okta</li>
</ol></h2>
<p>You will need to manually create an app for Email security in Okta.</p>
<ol>
<li>
<p>Log in to Okta as an administrator.</p>
</li>
<li>
<p>In the Admin console, go to <strong>Applications</strong> &gt; <strong>Applications</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/sso/okta/step2-applications.png" alt="Go to Applications in your Okta Admin console" /></p>
<ol start="3">
<li>Select <strong>Create App Integration</strong> &gt; <strong>SAML 2.0</strong>, and select <strong>Next</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/sso/okta/step3-saml.png" alt="Choose SAML 2.0 as the new app integration type" /></p>
<ol start="4">
<li>
<p>Enter a descriptive name for your app, such as <code>Email security</code>, and select <strong>Next</strong>.</p>
</li>
<li>
<p>Enter the following settings for <strong>SAML Settings</strong>:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Single sing on URL</strong></td>
<td><code>https://horizon.area1security.com/api/users/saml</code></td>
</tr>
<tr>
<td><strong>Audience URI (SP Entity ID)</strong></td>
<td><code>https://horizon.area1security.com/api/users/saml</code></td>
</tr>
<tr>
<td><strong>Name ID format</strong></td>
<td>Select <em>EmailAddress</em> from the drop-down menu.</td>
</tr>
<tr>
<td><strong>Application username</strong></td>
<td>Select <em>Email</em> from the drop-down menu.</td>
</tr>
<tr>
<td><strong>Response</strong></td>
<td><em>Signed</em></td>
</tr>
<tr>
<td><strong>Assertion signature</strong></td>
<td><em>Unsigned</em></td>
</tr>
<tr>
<td><strong>Signature Algorithm</strong></td>
<td><em>RSA-SHA1</em></td>
</tr>
<tr>
<td><strong>Digest Algorithm</strong></td>
<td><em>SHA1</em></td>
</tr>
<tr>
<td><strong>Attribute statements (optional)</strong></td>
<td></td>
</tr>
<tr>
<td><strong>Name</strong></td>
<td>Enter email addresses for your users. Should match users already added to Email security (formerly Area 1) dashboard.</td>
</tr>
<tr>
<td><strong>Name format</strong></td>
<td>Select <em>Unspecified</em> from the drop-down menu.</td>
</tr>
<tr>
<td><strong>Value</strong></td>
<td>Select <code>user.email</code> from the drop-down menu.</td>
</tr>
</tbody>
</table>
<p><img src="/assets/upstream/images/email-security/sso/okta/step5-saml-settings.png" alt="Input the correct settings in SAML settings" /></p>
<ol start="6">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Under <strong>Are you a customer or a partner?</strong>, select <strong>I'm an Okta customer adding an internal app</strong>.</p>
</li>
<li>
<p>In <strong>App type</strong>, select <strong>This is an internal app that we have created</strong>.</p>
</li>
<li>
<p>Select <strong>Finish</strong>.</p>
</li>
<li>
<p>Okta should display the app you have just created. If not, go to <strong>Applications</strong> &gt; <strong>Applications</strong>, and select it.</p>
</li>
<li>
<p>In the <strong>Sign On</strong> tab, go to <strong>View SAML setup instructions</strong> and select it to retrieve the SAML provider information.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/sso/okta/step11-saml-instructions.png" alt="Find the View SAML setup instructions button" /></p>
<ol start="12">
<li>Copy and save the link in <strong>Identity Provider Single Sign-On URL</strong>. You will need it later to use in the Email security dashboard.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/sso/okta/step12-sso-url.png" alt="Copy and save the SSO URL to use later in the Email security dashboard" /></p>
<ol start="13">
<li>Scroll down to <strong>Optional</strong>. You might need to enlarge the text box to copy and save all the XML data. You will need this information to finish configuration in the Email security dashboard. The start of the metadata should be similar to the following:</li>
</ol>
<pre tabindex="0"><code class="language-txt">&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;&lt;EntityDescriptor ID=&quot;_&lt;YOUR_DESCRIPTOR_ID&gt;&quot; entityID=&quot;https://&lt;YOUR_ENTITY_ID&gt; &quot; xmlns=&quot;urn:oasis:names:tc:SAML:2.0:metadata&quot;&gt;...&#10;</code></pre>
<p><img src="/assets/upstream/images/email-security/sso/okta/step13-optional.png" alt="Copy and save the XML metadata to use later in the Email security dashboard" /></p>
<h2 id="2-configure-email-security-to-connect-to-okta"><ol start="2">
<li>Configure Email security to connect to Okta</li>
</ol></h2>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>In <strong>Users and Actions</strong> &gt; <strong>Users and Permissions</strong> add the email addresses of all your authorized administrators.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/sso/generic/step3-users-actions.png" alt="Fill out your authorized administrators" /></p>
<ol start="4">
<li>Go to <strong>SSO Settings</strong> and enable <strong>Single Sign On</strong> switch.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/sso/generic/step4-sso.png" alt="Enable SSO" /></p>
<ol start="5">
<li>In <strong>SSO Enforcement</strong>, choose one of the settings according to your specific needs:</li>
</ol>
<ul>
<li><strong>None</strong>: This setting allows each user to choose SSO, or username and password plus <span class="nb-glossary-tooltip" title="two-factor authentication (2FA)">2FA</span> (this is the recommended setting while testing SSO).</li>
<li><strong>Admin</strong>: This setting will force only the administrator account to use SSO. The user that enables this setting will still be able to log in using username and password plus 2FA. This is a backup, so that your organization does not get locked out of the portal in emergencies.</li>
<li><strong>Non-Admin Only</strong>: This option will require that all <code>Read only</code> and <code>Read &amp; Write</code> users use SSO to access the portal. Admins will still have the option to use either SSO or username and password plus 2FA.</li>
</ul>
<ol start="6">
<li>
<p>In <strong>SAML SSO Domain</strong> enter the domain you saved from step 13. For example, <code>area1security-examplecorp.okta.com</code>.</p>
</li>
<li>
<p>In <strong>Metadata XML</strong> paste the XML metadata you saved from step 14.</p>
</li>
<li>
<p>Select <strong>Update Settings</strong> to save your configuration.</p>
</li>
</ol>
<p>Log out of any customer portal sessions. Your Okta account should now show a tile for Email security (formerly Area 1).</p>
