---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/authentik/
  description: Configure Authentik as a SCIM identity provider to provision users and groups into your Cloudflare account.
  full_title: Provision with Authentik · Cloudflare Fundamentals docs
  head_html: <title>Provision with Authentik · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Authentik as a SCIM identity provider to provision users and groups into your Cloudflare account."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/authentik/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/authentik/index.md"><meta property="og:title" content="Provision with Authentik · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Authentik as a SCIM identity provider to provision users and groups into your Cloudflare account."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/authentik/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/authentik/#page","headline":"Provision with Authentik \u00b7 Cloudflare Fundamentals docs","description":"Configure Authentik as a SCIM identity provider to provision users and groups into your Cloudflare account.","url":"https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/authentik/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/account/account-security/scim-setup/authentik/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8964.md")
</aside>
<p>Once you have <a href="/fundamentals/account/account-security/scim-setup/#gather-the-required-data">gathered the required data</a>, the following steps will be required to finish the provisioning with Authentik.</p>
<h2 id="set-up-your-authentik-scim-provider">Set up your Authentik SCIM provider</h2>
<ol>
<li>In the Authentik Admin interface, go to <strong>Applications</strong> &gt; <strong>Providers</strong>.</li>
<li>Select <strong>Create</strong> and choose <strong>SCIM Provider</strong>.</li>
<li>Name your provider (for example, <code>Cloudflare SCIM</code>).</li>
<li>In <strong>URL</strong>, enter: <code>https://api.cloudflare.com/client/v4/accounts/&lt;accountID&gt;/scim/v2</code>, substituting <code>&lt;accountID&gt;</code> for your <a href="/fundamentals/account/account-security/scim-setup/#get-the-account-id">Cloudflare Account ID</a>.</li>
<li>In <strong>Token</strong>, Paste the SCIM provisioning API token.</li>
<li>(Optional) Adjust the <strong>User filtering</strong> and <strong>Group filtering</strong> settings to control which users and groups are synchronized.</li>
<li>Select <strong>Finish</strong> to create the provider.</li>
</ol>
<h2 id="create-an-authentik-application">Create an Authentik application</h2>
<ol>
<li>In the Authentik Admin interface, go to <strong>Applications</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create</strong>.</li>
<li>Name your application (for example, <code>Cloudflare Dashboard</code>).</li>
<li>In <strong>Provider</strong>, select the SCIM provider you created in the previous step.</li>
<li>Select <strong>Create</strong> to save the application.</li>
</ol>
<h2 id="configure-user-and-group-sync-in-authentik">Configure user and group sync in Authentik</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8963.md")
</aside>
<ol>
<li>In the Authentik Admin interface, go to <strong>Directory</strong> &gt; <strong>Groups</strong>.</li>
<li>Create or select the groups you want to synchronize with Cloudflare. Ensure the users you want to provision are members of these groups.</li>
<li>Return to <strong>Applications</strong> &gt; <strong>Providers</strong> and select your SCIM provider.</li>
<li>Under <strong>Backchannel Providers</strong>, verify that your SCIM provider is correctly linked to the application.</li>
<li>To trigger a manual sync, select <strong>Sync</strong> from the provider page. Authentik will also perform automatic periodic syncs based on your configured schedule.</li>
</ol>
<h2 id="verify-the-integration">Verify the integration</h2>
<p>To verify the integration:</p>
<ol>
<li>In Authentik, go to <strong>Applications</strong> &gt; <strong>Providers</strong>, select your SCIM provider, and review the <strong>Sync status</strong> section for any errors.</li>
<li>In the Cloudflare dashboard, go to <strong>Manage Account</strong> &gt; <strong>Members</strong> &gt; <strong>User Groups</strong> to view the synchronized groups.</li>
<li>Check the Audit Logs in the Cloudflare dashboard by going to <strong>Manage Account</strong> &gt; <strong>Audit Log</strong>.</li>
</ol>
<h2 id="assign-policies-to-user-groups">Assign policies to user groups</h2>
<p>After users and groups are synchronized, you can assign <a href="/fundamentals/manage-members/policies/">policies</a> to user groups:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Manage Account</strong> &gt; <strong>Members</strong> &gt; <strong>User Groups</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the group you want to configure.</li>
<li>Assign the appropriate policies to define the <a href="/fundamentals/manage-members/roles/">roles</a> for group members.</li>
</ol>
