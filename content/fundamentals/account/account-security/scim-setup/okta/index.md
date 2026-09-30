---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/okta/
  description: Configure Okta as a SCIM identity provider to provision users and groups into your Cloudflare account.
  full_title: Provision with Okta · Cloudflare Fundamentals docs
  head_html: <title>Provision with Okta · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Okta as a SCIM identity provider to provision users and groups into your Cloudflare account."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/okta/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/okta/index.md"><meta property="og:title" content="Provision with Okta · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Okta as a SCIM identity provider to provision users and groups into your Cloudflare account."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/okta/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/okta/#page","headline":"Provision with Okta \u00b7 Cloudflare Fundamentals docs","description":"Configure Okta as a SCIM identity provider to provision users and groups into your Cloudflare account.","url":"https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/okta/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/account/account-security/scim-setup/okta/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8956.md")
</aside>
<p>Once you have <a href="/fundamentals/account/account-security/scim-setup/#gather-the-required-data">gathered the required data</a>, the following steps will be required to finish the provisioning with Okta.</p>
<h2 id="set-up-your-okta-scim-application">Set up your Okta SCIM application</h2>
<ol>
<li>In the Okta dashboard, go to <strong>Applications</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Browse App Catalog</strong>.</li>
<li>Locate and select <strong>SCIM 2.0 Test App (OAuth Bearer Token)</strong>.</li>
<li>Select <strong>Add Integration</strong> and name your integration.</li>
<li>Enable the following options:
<ul>
<li><strong>Do not display application icon to users</strong></li>
<li><strong>Do not display application icon in the Okta Mobile App</strong></li>
</ul>
</li>
<li>Disable <strong>Automatically log in when user lands on login page</strong>.</li>
<li>Select <strong>Next</strong>, then select <strong>Done</strong>.</li>
</ol>
<h2 id="integrate-the-cloudflare-api">Integrate the Cloudflare API</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8955.md")
</aside>
<ol>
<li>In your integration page, go to <strong>Provisioning</strong> &gt; <strong>Configure API Integration</strong>.</li>
<li>Enable <strong>Enable API Integration</strong>.</li>
<li>In SCIM 2.0 Base URL, enter: <code>https://api.cloudflare.com/client/v4/accounts/&lt;accountID&gt;/scim/v2</code>, substituting <code>accountID</code> for your <a href="/fundamentals/account/account-security/scim-setup/#get-the-account-id">Cloudflare Account ID</a>.</li>
<li>In the <strong>OAuth Bearer Token</strong> field, enter your API token value.</li>
<li>Deselect <strong>Import Groups</strong>.</li>
</ol>
<h2 id="configure-user-group-sync-in-okta">Configure user &amp; group sync in Okta</h2>
<ol>
<li>In <strong>Provisioning to App</strong>, select <strong>Edit</strong>.</li>
<li>Enable <strong>Create Users</strong> and <strong>Deactivate Users</strong>. Select <strong>Save</strong>.</li>
<li>Select <strong>Done</strong>.</li>
<li>In the Assignments tab, add the users you want to synchronize with Cloudflare dashboard. You can add users in batches by assigning a group. If a user is removed from the application assignment via either direct user assignment or removed from the group that was assigned to the app, this will trigger a deprovisioning event from Okta to Cloudflare.</li>
<li>In the Push Groups tab, add the Okta groups you want to synchronize with Cloudflare dashboard. View these Okta groups in the dashboard under Manage Account &gt; Manage members &gt; Members &gt; User Groups.</li>
</ol>
<p>To verify the integration, select <strong>View Logs</strong> in the Okta SCIM application, and check the Audit Logs in the Cloudflare dashboard by navigating to <strong>Manage Account</strong> &gt; <strong>Audit Log</strong>.</p>
<p>This will provision all of the users in the group(s) affected to your Cloudflare account with &quot;minimal account access.&quot;</p>
