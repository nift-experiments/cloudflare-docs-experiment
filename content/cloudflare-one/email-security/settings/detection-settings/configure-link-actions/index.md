---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/
  description: Configure link actions in Email Security.
  full_title: Configure link actions · Cloudflare One docs
  head_html: <title>Configure link actions · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure link actions in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/index.md"><meta property="og:title" content="Configure link actions · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure link actions in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/#page","headline":"Configure link actions \u00b7 Cloudflare One docs","description":"Configure link actions in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/settings/detection-settings/configure-link-actions/
  schema: 1
---
<p>You can configure how Email security handles links in emails.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4933.md")
</aside>
<p>To configure link actions:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>Settings</strong>, then go to <strong>Detection settings</strong> &gt; <strong>Link actions</strong> &gt; <strong>View</strong>.</li>
</ol>
<p>You can configure <strong>Link actions settings</strong>, or <strong>URL rewrite ignore patterns</strong>.</p>
<h2 id="link-actions-settings">Link actions settings</h2>
<p>To configure link actions, select <strong>Configure</strong>.</p>
<p>The dashboard will display <strong>Open links evaluated as suspicious in a remote browser (Recommended)</strong>. This option is turned on by default. Email security will also allow you to select message dispositions to open all the links for dispositioned emails in a remote browser.</p>
<p>Select one or more disposition, then select <strong>Save</strong>.</p>
<p>If <strong>Open links evaluated as suspicious in a remote browser (Recommended)</strong> is turned off, you can select <strong>URL defang</strong> or <strong>No action</strong> on each disposition. Select <strong>Save</strong> once you have completed the configuration.</p>
<p>When opening links, Email security will not allow you to:</p>
<ul>
<li><a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">Copy (from remote to client)</a></li>
<li><a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">Paste (from client to remote)</a></li>
<li>Use <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">keyboard</a></li>
<li><a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">Print</a></li>
<li><a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">Download files</a></li>
<li><a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">Uploads files</a></li>
</ul>
<h2 id="add-patterns-for-urls">Add patterns for URLs</h2>
<p>You can add patterns for URLs that should be rewritten.</p>
<ol>
<li>Under <strong>URL rewrite ignore patterns</strong>, select <strong>Add a pattern</strong>.</li>
<li>Enter a valid IP, URL, or regular expression. You can enter up to 512 characters.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>To edit a pattern, go to the pattern you want to edit, select the three dots, then <strong>Edit</strong>. Once you have finished modifying the URL patter, select <strong>Save</strong>.</p>
<p>To delete a pattern, go to the pattern you want to delete, select the three dots, then <strong>Delete</strong>.</p>
