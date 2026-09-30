---
cp9:
  canonical: https://developers.cloudflare.com/email-security/account-setup/sso/azure/
  description: Configure Azure Active Directory for SAML SSO with Email Security.
  full_title: Azure integration guide · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Azure integration guide · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Azure Active Directory for SAML SSO with Email Security."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/account-setup/sso/azure/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/account-setup/sso/azure/index.md"><meta property="og:title" content="Azure integration guide · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Azure Active Directory for SAML SSO with Email Security."><meta property="og:url" content="https://developers.cloudflare.com/email-security/account-setup/sso/azure/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/account-setup/sso/azure/
  schema: 1
---
<p>This tutorial will walk you through the steps for configuring a non-gallery enterprise application within Azure Active Directory to establish a <span class="nb-glossary-tooltip" title="SAML">SAML</span> SSO connection with Email security (formerly Area 1).</p>
<h2 id="1-azure-active-directory-configuration"><ol>
<li>Azure Active Directory configuration</li>
</ol></h2>
<ol>
<li>
<p><a href="https://portal.azure.com/">Log in to Azure portal</a> and open <strong>Enterprise Applications</strong>.</p>
</li>
<li>
<p>Select <strong>New Application</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/sso/azure/step2-new-app.png" alt="Create a new application" /></p>
<ol start="3">
<li>Select <strong>Create your own application</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/sso/azure/step3-create-your-own-app.png" alt="Select create your own application" /></p>
<ol start="4">
<li>Input a descriptive name for your app and select <strong>Integrate any other application you don't find in the gallery (Non-gallery)</strong> &gt; <strong>Create</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/sso/azure/step4-name.png" alt="Give your application a descriptive name" /></p>
<ol start="5">
<li>On the application <strong>Overview</strong> page that opens, select <strong>2. Set up single sign on</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/sso/azure/step5-sso.png" alt="Select single sign-on as the type of app" /></p>
<ol start="6">
<li>Select <strong>SAML</strong> as your single sign-on method.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/sso/azure/step6-saml.png" alt="Select SAML as the sign-on method" /></p>
<ol start="7">
<li>Select the pencil icon to edit the <strong>Basic SAML Configuration</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/sso/azure/step7-basic-saml.png" alt="Select the pencil icon to edit Basic SAML Configuration" /></p>
<ol start="8">
<li>Enter the following configuration settings:</li>
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
<td><strong>Identifier (Entity ID)</strong></td>
<td><code>https://horizon.area1security.com</code></td>
</tr>
<tr>
<td><strong>Reply URL (Assertion Consumer Service URL)</strong></td>
<td><code>https://horizon.area1security.com/api/users/saml</code></td>
</tr>
<tr>
<td><strong>Sign-On URL</strong></td>
<td>Leave blank</td>
</tr>
<tr>
<td><strong>Relay State</strong></td>
<td>Leave blank</td>
</tr>
<tr>
<td><strong>Logout URL</strong></td>
<td>Leave blank</td>
</tr>
</tbody>
</table>
<ol start="9">
<li>
<p>Select <strong>Save</strong> and the cross button to exit <strong>Basic SAML Configuration</strong>.</p>
</li>
<li>
<p>Select the pencil icon to edit <strong>SAML Certificates</strong> and make the following changes:</p>
<ul>
<li><strong>Signing Option</strong>: Select <em>Sign SAML response</em> from the drop-down menu.</li>
<li><strong>Signing Algorithm</strong>: Select <em>SHA-1</em> from the drop-down menu.</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/sso/azure/step10-saml-signing-certificate.png" alt="Select Sign SAML response and SHA-1 from the menu" /></p>
<ol start="11">
<li>
<p>Select <strong>Save</strong> and the cross button to exit <strong>SAML Certificates</strong>.</p>
</li>
<li>
<p>Still in the <strong>SAML Certificates</strong> section, find <strong>Federation Metadata XML</strong> and select <strong>Download</strong>. You will need this information for the SSO Configuration in the Email security dashboard.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/sso/azure/step12-download.png" alt="Download the Metadata XML information" /></p>
<p>Your Azure configuration is now complete. It should look similar to this:</p>
<p><img src="/assets/upstream/images/email-security/sso/azure/config-finished.png" alt="Your Azure configuration should be similar to this one" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8502.md")
</aside>
<h2 id="2-configure-email-security-to-connect-to-azure"><ol start="2">
<li>Configure Email security to connect to Azure</li>
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
<li>Go to <strong>SSO Settings</strong>, and enable <strong>Single Sign On</strong>.</li>
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
<p>For <strong>SAML SSO Domain</strong>, enter <code>login.microsoftonline.com</code>.</p>
</li>
<li>
<p>In <strong>Metadata XML</strong> paste the XML metadata you downloaded in the previous step 11. You can open the downloaded file with a text editor to copy all the text. Make sure there are no leading carriage returns or spaces when you copy the text. Your copied text should begin with:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;&lt;EntityDescriptor ID=&quot;_&lt;YOUR_DESCRIPTOR_ID&gt;&quot; entityID=&quot;https://&lt;YOUR_ENTITY_ID&gt; &quot; xmlns=&quot;urn:oasis:names:tc:SAML:2.0:metadata&quot;&gt;...&#10;</code></pre>
<ol start="8">
<li>Select <strong>Update Settings</strong> to save your configuration.</li>
</ol>
<h2 id="3-test-sso-configuration"><ol start="3">
<li>Test SSO configuration</li>
</ol></h2>
<p>After completing both the Azure and Email security setups, you can test your SSO access.
In this example, the logo for Email security has been updated.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8501.md")
</aside>
<ol>
<li>
<p>Log in to your <a href="https://portal.office.com">Office 365 portal</a>.</p>
</li>
<li>
<p>Select <strong>All Apps</strong>.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> &gt; <strong>SSO</strong>.</p>
</li>
<li>
<p>Locate the Email security Horizon application (or whichever name you gave your application), and select it to initiate your SSO login with Email security.</p>
</li>
<li>
<p>If you configured everything correctly, you should be signed in to the Email security Portal and redirected to the dashboard.</p>
</li>
</ol>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you have trouble connecting your Azure account to Email security, make sure that:</p>
<ul>
<li>The user exists in the Email security dashboard.</li>
<li>The <strong>Identifier</strong> and <strong>Reply URLs</strong> in Azure AD are correct (refer to <strong>Basic SAML Configuration</strong> in step 7 of <a href="#1-azure-active-directory-configuration">Azure Active Directory configuration</a>).</li>
<li><strong>Sign SAML response</strong> and <strong>SHA-1</strong> are selected in Azure AD (refer to <strong>SAML Certificates</strong> in step 9 of <a href="#1-azure-active-directory-configuration">Azure Active Directory configuration</a>).</li>
<li>The SAML SSO Domain is set correctly in the Email security dashboard (refer to step 6 in <a href="#2-configure-email-security-to-connect-to-azure">Configure Email security to connect to Azure</a>).</li>
<li>The name ID identifier is set to <strong>Email Address</strong>.</li>
</ul>
<p>If all else fails, enable Chrome browser debug logs. Then, log your activity when SSO is initiated, and contact <a href="/support/contacting-cloudflare-support/">Cloudflare support</a>.</p>
