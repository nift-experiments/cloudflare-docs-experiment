---
cp9:
  canonical: https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/cloudflare-wordpress-plugin-automatic-cache-management/
  description: Manage automatic cache purging with the WordPress plugin.
  full_title: Cloudflare WordPress Plugin Automatic Cache Management · Cloudflare Support docs
  head_html: <title>Cloudflare WordPress Plugin Automatic Cache Management · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage automatic cache purging with the WordPress plugin."><link rel="canonical" href="https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/cloudflare-wordpress-plugin-automatic-cache-management/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/cloudflare-wordpress-plugin-automatic-cache-management/index.md"><meta property="og:title" content="Cloudflare WordPress Plugin Automatic Cache Management · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage automatic cache purging with the WordPress plugin."><meta property="og:url" content="https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/cloudflare-wordpress-plugin-automatic-cache-management/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/cloudflare-wordpress-plugin-automatic-cache-management/#page","headline":"Cloudflare WordPress Plugin Automatic Cache Management \u00b7 Cloudflare Support docs","description":"Manage automatic cache purging with the WordPress plugin.","url":"https://developers.cloudflare.com/support/third-party-software/content-management-system-cms/cloudflare-wordpress-plugin-automatic-cache-management/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/third-party-software/content-management-system-cms/cloudflare-wordpress-plugin-automatic-cache-management/
  schema: 1
---
<h2 id="overview">Overview</h2>
<p>The Cloudflare WordPress plugin contains a feature called Automatic Cache Management. When a user adds, edits, or deletes a post, page, attachment, or comment - any associated URLs are purged from the Cloudflare cache.</p>
<p>When you switch a theme or customise a theme within the WordPress admin panel, the cache will automatically be cleared too.</p>
<p>Automatic Cache Management uses native hooks built into WordPress. The Cloudflare WordPress plugin purges the following cache URLs:</p>
<ul>
<li>deleted_post</li>
<li>edit_post</li>
<li>delete_attachment</li>
<li>autoptimize_action_cachepurged (for compatibility with the Autoptimize WordPress plugin)</li>
<li>switch_theme</li>
<li>customize_save_after</li>
</ul>
<hr />
<h2 id="enable-automatic-cache-management">Enable Automatic Cache Management</h2>
<p>To enable Automatic Cache Management after <a href="/automatic-platform-optimization/">installing the WordPress plugin</a>:</p>
<ol>
<li>Log in to your WordPress account.</li>
<li>Click <strong>Settings</strong> and choose the Cloudflare plugin. The Cloudflare plugin home page appears.</li>
<li>Click <strong>Enable</strong> to the right of the <strong>Automatic Cache</strong> feature. A confirmation dialog appears.</li>
<li>Click <strong>I'm sure</strong> in the confirmation dialog to confirm.</li>
</ol>
