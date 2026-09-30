---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/active-directory-sync/
  description: Sync and manage email directory users.
  full_title: Manage your active directory · Cloudflare Learning Paths
  head_html: <title>Manage your active directory · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Sync and manage email directory users."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/active-directory-sync/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/active-directory-sync/index.md"><meta property="og:title" content="Manage your active directory · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Sync and manage email directory users."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/active-directory-sync/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email security (formerly Area 1)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/active-directory-sync/#page","headline":"Manage your active directory \u00b7 Cloudflare Learning Paths","description":"Sync and manage email directory users.","url":"https://developers.cloudflare.com/learning-paths/secure-your-email/configure-email-security/active-directory-sync/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/secure-your-email/configure-email-security/active-directory-sync/
  schema: 1
---
<p>Directories are folders to store user data. Email security allows you to manage directories from the Cloudflare dashboard.</p>
<h3 id="manage-your-microsoft-365-directory">Manage your Microsoft 365 directory</h3>
<p>To manage your Microsoft 365 directory:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Zero Trust </a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>Directories</strong>.</li>
<li>Under <strong>Directory name</strong>, select <strong>MS directory</strong>.</li>
<li>From here, you can manage <strong>Groups</strong> or <strong>Users</strong> directories.</li>
</ol>
<h3 id="manage-your-google-workspace-directory">Manage your Google Workspace directory</h3>
<p>To manage your Google Workspace Directory:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Zero Trust </a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>Directories</strong>.</li>
<li>Under <strong>Directory name</strong>, select <strong>Google Workspace Directory</strong>.</li>
<li>From here, you can manage <strong>Groups</strong> or <strong>Users</strong> directories.</li>
</ol>
<p>Email security allows you to view and manage your groups directory and their <a href="/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/">impersonation registry</a>. When a group is added to the registry, all members are registered by default.</p>
<p>To manage your group directory, select your directory, then select the <strong>Groups</strong> tab.</p>
<p>To add a single group to the registry:</p>
<ol>
<li>Select the group name you want to add.</li>
<li>Select the three dots &gt; <strong>Add to registry</strong>.</li>
</ol>
<p>To add multiple groups to the registry at once:</p>
<ol>
<li>Select the group names you want to add to the registry.</li>
<li>Select the <strong>Action</strong> dropdown list.</li>
<li>Select <strong>Add to registry</strong>.</li>
</ol>
<p>In addition, Email security allows you to:</p>
<ul>
<li><a href="/cloudflare-one/email-security/directories/manage-integrated-directories/manage-groups-directory/#remove-groups-from-registry">Remove groups from the registry</a>.</li>
<li><a href="/cloudflare-one/email-security/directories/manage-integrated-directories/manage-groups-directory/#filter-impersonation-registry">Filter the impersonation registry</a>.</li>
<li><a href="/cloudflare-one/email-security/directories/manage-integrated-directories/manage-users-directory/">Manage users in your directory</a>.</li>
</ul>
