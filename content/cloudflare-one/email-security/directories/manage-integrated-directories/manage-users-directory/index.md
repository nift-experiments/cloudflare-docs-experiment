---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/directories/manage-integrated-directories/manage-users-directory/
  description: Manage users in your directory in Email Security.
  full_title: Manage users in your directory · Cloudflare One docs
  head_html: <title>Manage users in your directory · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage users in your directory in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/directories/manage-integrated-directories/manage-users-directory/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/directories/manage-integrated-directories/manage-users-directory/index.md"><meta property="og:title" content="Manage users in your directory · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage users in your directory in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/directories/manage-integrated-directories/manage-users-directory/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/directories/manage-integrated-directories/manage-users-directory/#page","headline":"Manage users in your directory \u00b7 Cloudflare One docs","description":"Manage users in your directory in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/directories/manage-integrated-directories/manage-users-directory/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/directories/manage-integrated-directories/manage-users-directory/
  schema: 1
---
<p>Email security allows you to view and manage the <a href="/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/">impersonation registry</a> status of your users directory.</p>
<p>To manage users directory:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Email security</strong> &gt; <strong>Directories</strong>.</li>
<li>Locate your directory, select the three dots &gt; <strong>View details</strong>.</li>
<li>Select <strong>Users</strong>.</li>
</ol>
<h2 id="add-users-to-registry">Add users to registry</h2>
<p>To add a single user to the registry:</p>
<ol>
<li>Select the name you want to add.</li>
<li>Select the three dots &gt; <strong>Add to registry</strong>.</li>
</ol>
<p>To add multiple users to the registry at once:</p>
<ol>
<li>Select the names you want to add to the registry.</li>
<li>Select the <strong>Action</strong> dropdown list.</li>
<li>Select <strong>Add to registry</strong>.</li>
</ol>
<h2 id="remove-users-from-registry">Remove users from registry</h2>
<p>Email security allows you to remove users from the registry.</p>
<p>To remove a single user from the registry:</p>
<ol>
<li>Select the name you want to remove.</li>
<li>Select the three dots &gt; <strong>Remove from registry</strong>.</li>
</ol>
<p>To remove multiple users from the registry at once:</p>
<ol>
<li>Select the names you want to remove from the registry.</li>
<li>Select the <strong>Action</strong> dropdown list.</li>
<li>Select <strong>Remove from registry</strong>.</li>
</ol>
<h2 id="edit-a-user">Edit a user</h2>
<p>To edit a user:</p>
<ol>
<li>Under <strong>Display name</strong>, locate the user you want to edit.</li>
<li>Select the three dots &gt; <strong>Edit</strong>.</li>
<li>Edit the user, then select <strong>Save</strong>.</li>
</ol>
<h2 id="filter-a-user">Filter a user</h2>
<p>You can filter the list of users by registered and unregistered.</p>
<p>A user is registered when they are added to the <a href="/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/">impersonation registry</a>. A user is unregistered when they are not part of the impersonation registry.</p>
<p>To filter the impersonation registry:</p>
<ol>
<li>Select <strong>Show filters</strong> &gt; <strong>Impersonation registry</strong>.</li>
<li>Choose one of the following:
<ul>
<li><strong>All</strong>: To view registered and unregistered users.</li>
<li><strong>Registered</strong>: To view registered users.</li>
<li><strong>Unregistered</strong>: To view unregistered users.</li>
</ul>
</li>
<li>Select <strong>Apply filters</strong>.</li>
</ol>
<p>To filter users:</p>
<ol>
<li>Select <strong>Show filters</strong> &gt; <strong>Users</strong>.</li>
<li>Choose one of the following:
<ul>
<li><strong>All</strong>: To view users in groups and not in groups.</li>
<li><strong>Users in groups</strong>: To view users in groups.</li>
<li><strong>Users not in groups</strong>: To view users not in groups.</li>
</ul>
</li>
<li>Select <strong>Apply filters</strong>.</li>
</ol>
