---
cp9:
  canonical: https://developers.cloudflare.com/email-security/account-setup/sso/generic-sso/
  description: Set up SAML-based single sign-on for Email Security with any identity provider.
  full_title: Generic single sign-on integration guide · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Generic single sign-on integration guide · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up SAML-based single sign-on for Email Security with any identity provider."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/account-setup/sso/generic-sso/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/account-setup/sso/generic-sso/index.md"><meta property="og:title" content="Generic single sign-on integration guide · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up SAML-based single sign-on for Email Security with any identity provider."><meta property="og:url" content="https://developers.cloudflare.com/email-security/account-setup/sso/generic-sso/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/account-setup/sso/generic-sso/
  schema: 1
---
<p>Below is a generic guide to successfully set up an identity provider based <span class="nb-glossary-tooltip" title="SAML">SAML</span>. These options might change depending on your identity provider (IDP). However, make sure you set up the options below or their equivalent.</p>
<h2 id="1-identity-provider-saml-setup"><ol>
<li>Identity Provider SAML setup</li>
</ol></h2>
<ol>
<li>
<p>Log in to your SAML provider and access its setup section.</p>
</li>
<li>
<p>Enter the following values to configure your IDP provider:</p>
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
<td><strong>Single sign on URL</strong></td>
<td><code>https://horizon.area1security.com/api/users/saml</code></td>
</tr>
<tr>
<td><strong>Audience URI (SP Entity ID)</strong></td>
<td><code>https://horizon.area1security.com</code></td>
</tr>
<tr>
<td><strong>Name ID format</strong></td>
<td><em>Email Address</em></td>
</tr>
<tr>
<td><strong>Application username</strong></td>
<td><em>Email</em></td>
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
<td><em>RSA</em>-SHA1</td>
</tr>
<tr>
<td><strong>Digest Algorithm</strong></td>
<td><em>SHA1</em></td>
</tr>
</tbody>
</table>
<ol start="3">
<li>
<p>In the <strong>Attribute Statements</strong>, add your application users. Emails you add here should match emails users already have in the Email security dashboard.</p>
</li>
<li>
<p>After finishing the setup, download the IDP metadata file. Copy and paste it into the <strong>METADATA XML</strong> field in the SSO section of Email security’s dashboard. Refer to <strong>step 4</strong> in the guide below for more details.</p>
</li>
</ol>
<h2 id="2-email-security-saml-setup"><ol start="2">
<li>Email security SAML setup</li>
</ol></h2>
<p>After configuring settings in your SSO provider, log in to the Email security dashboard to finish setting up.</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security (formerly Area 1) dashboard</a>.</p>
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
<li>Go to <strong>SSO</strong>, and enable <strong>Single Sign on</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/email-security/sso/generic/step4-sso.png" alt="Enable SSO" /></p>
<ol start="5">
<li>In <strong>SSO Enforcement</strong>, choose one of the settings, according to your specific needs:</li>
</ol>
<ul>
<li><strong>None</strong>: This setting allows each user to choose SSO, or username and password plus <span class="nb-glossary-tooltip" title="two-factor authentication (2FA)">2FA</span> (this is the recommended setting while testing SSO).</li>
<li><strong>Admin</strong>: This setting will force only the administrator account to use SSO. The user that enables this setting will still be able to log in using username and password plus 2FA. This is a backup, so that your organization does not get locked out of the portal in emergencies.</li>
<li><strong>Non-Admin Only</strong>: This option will require that all <code>Read only</code> and <code>Read &amp; Write</code> users use SSO to access the portal. Admins will still have the option to use either SSO or username and password plus 2FA.</li>
</ul>
<ol start="6">
<li>
<p>In <strong>SAML SSO Domain</strong> enter the domain that points to your SSO provider.</p>
</li>
<li>
<p>In <strong>METADATA XML</strong> paste the SAML XML metadata settings from your provider. These settings (and even their exact text descriptions) are in different locations depending on your SSO provider.</p>
</li>
<li>
<p>Select <strong>Update Settings</strong> to save your configuration.</p>
</li>
</ol>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you have trouble connecting your SAML provider to Email security, make sure that:</p>
<ul>
<li>The users you have configured in your SAML provider exist in the Email security dashboard.</li>
<li>You are using email address as an attribute (in step 2, refer to <strong>Name ID format</strong> and <strong>Application username</strong>).</li>
<li>You are using the SHA-1 algorithm.</li>
<li>Your encryption is set to 2048 bits.</li>
</ul>
<p>If all else fails, enable Chrome browser debug logs. Then, log your activity when SSO is initiated, and contact <a href="/support/contacting-cloudflare-support/">Cloudflare support</a>.</p>
