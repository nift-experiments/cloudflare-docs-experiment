---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/setup/manage-domains/
  description: Add, edit, and manage domains protected by Email Security.
  full_title: Manage domains · Cloudflare One docs
  head_html: <title>Manage domains · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Add, edit, and manage domains protected by Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/manage-domains/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/manage-domains/index.md"><meta property="og:title" content="Manage domains · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Add, edit, and manage domains protected by Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/setup/manage-domains/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/manage-domains/#page","headline":"Manage domains \u00b7 Cloudflare One docs","description":"Add, edit, and manage domains protected by Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/manage-domains/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/setup/manage-domains/
  schema: 1
---
<p>Once you have deployed your domain, Email security allows you to add, filter and edit domains. You can also choose to stop a domain from being scanned.</p>
<h2 id="add-domains">Add domains</h2>
<p>To protect a new domain:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com">Cloudflare One</a> &gt; Email security.</li>
<li>Select <strong>Settings</strong>, go to <strong>Domains</strong> and select <strong>View</strong>.</li>
<li>Select <strong>Add a domain</strong>.</li>
</ol>
<h2 id="filter-domains">Filter domains</h2>
<p>To filter your domains:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> &gt; <strong>Email security</strong>.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domain management</strong> &gt; <strong>Domains</strong>, then select <strong>View</strong>.</li>
<li>Select <strong>Show filters</strong> &gt; <strong>Configured method</strong>. Choose among the following filters: - <strong>MS Graph API</strong>: To view domains connected via MS Graph API. - <strong>BCC/Journaling</strong>: To view domains connected via BCC/Journaling. - <strong>MX/Inline</strong>: To view domains connected via MX/Inline. - <strong>Retro Scan</strong>: To view domains scanned by Retro Scan.</li>
<li>Select <strong>Apply filters</strong>.</li>
</ol>
<h2 id="edit-domains">Edit domains</h2>
<p>To edit your domains:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> &gt; <strong>Email security</strong>.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domain management</strong> &gt; <strong>Domains</strong>, then select <strong>View</strong>.</li>
<li>On the <strong>Domains</strong> page, locate your domain, select the three dots &gt; <strong>Edit</strong>.</li>
<li>If you did not manually add your domain, you will only be able to edit <strong>Hops</strong>. If you manually added your domain, you will be able to edit <strong>Domain name</strong> and <strong>Hops</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="prevent-cloudflare-from-scanning-a-domain">Prevent Cloudflare from scanning a domain</h2>
<p>To stop scanning domains:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> &gt; <strong>Email security</strong>.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domain management</strong> &gt; <strong>Domains</strong>, then select <strong>View</strong>.</li>
<li>On the <strong>Domains</strong> page, locate your domain, select the three dots &gt; <strong>Stop scanning</strong>.</li>
<li>Select <strong>Stop scanning</strong> again to stop Cloudflare from scanning your domain.</li>
</ol>
