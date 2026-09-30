---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpush/permissions/
  description: Review API permissions required for Cloudflare Logs.
  full_title: Permissions · Cloudflare Logs docs
  head_html: <title>Permissions · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Review API permissions required for Cloudflare Logs."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpush/permissions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpush/permissions/index.md"><meta property="og:title" content="Permissions · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review API permissions required for Cloudflare Logs."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpush/permissions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Logpush"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpush/permissions/#page","headline":"Permissions \u00b7 Cloudflare Logs docs","description":"Review API permissions required for Cloudflare Logs.","url":"https://developers.cloudflare.com/logs/logpush/permissions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpush/permissions/
  schema: 1
---
<p>Below is a description of the available permissions for tokens and roles as they relate to Logs. For information about how to create an API token, refer to <a href="/fundamentals/api/get-started/create-token/">Creating API tokens</a>.</p>
<h2 id="tokens">Tokens</h2>
<ul>
<li>
<p><strong>Logs: Read</strong> - Grants read access to logs using Logpull or Instant Logs.</p>
</li>
<li>
<p><strong>Logs: Write</strong> - Grants read and write access to Logpull and Logpush, and read access to Instant Logs. Note that all Logpush API operations require <strong>Logs: Write</strong> permission because Logpush jobs contain sensitive information.</p>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/10470.md")
</aside>
<h2 id="roles">Roles</h2>
<p><strong>Super Administrator</strong>, <strong>Administrator</strong> and the <strong>Log Share</strong> roles have full access to Logpull, Logpush and Instant Logs.</p>
<p>Only roles with <strong>Log Share</strong> edit permissions can read and configure Logpush jobs because job configurations may contain sensitive information.</p>
<p>The <strong>Administrator Read only</strong> and <strong>Log Share Reader</strong> roles only have access to Instant Logs and Logpull. This role does not have permissions to view the configuration of Logpush jobs.</p>
<h3 id="zero-trust-datasets">Zero Trust datasets</h3>
<p>To view, create, update, or delete Logpush jobs for Zero Trust datasets (Access, Gateway, and DEX) users must have both the <code>Logs Edit</code> and <code>Zero Trust: PII Read</code> permissions.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10469.md")
</aside>
<p>If you encounter the error <code>reading job for product '&lt;product&gt;' is not allowed (1004)</code>, this indicates that the API token you are using does not have the required permissions. Ensure your token or user account has both permissions listed above.</p>
<p>For more details, refer to the <a href="https://developers.cloudflare.com/changelog/2025-11-05-logpush-permissions-update/">Logpush Permission Update for Zero Trust Datasets</a>.</p>
<h3 id="assign-or-remove-a-role">Assign or remove a role</h3>
<p>To check the list of members in your account, or to manage roles and permissions:</p>
<ol>
<li>Navigate to the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a> and select your account.</li>
<li>From your Account Home, go to <strong>Manage Account</strong> &gt; <strong>Members</strong>.</li>
<li>Enter a member’s email address to add them to your account, and select <strong>Invite</strong>.</li>
<li>Alternatively, scroll down to the <strong>Members</strong> card to find a list of members with their status and role.</li>
</ol>
<p>For more information, refer to <a href="/fundamentals/manage-members/">Managing roles within your Cloudflare account</a>.</p>
