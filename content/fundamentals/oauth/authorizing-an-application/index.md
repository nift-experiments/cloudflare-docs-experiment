---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/oauth/authorizing-an-application/
  description: Learn more about what it means to authorize a third-party application on Cloudflare
  full_title: Authorizing an application · Cloudflare Fundamentals docs
  head_html: <title>Authorizing an application · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn more about what it means to authorize a third-party application on Cloudflare"><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/oauth/authorizing-an-application/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/oauth/authorizing-an-application/index.md"><meta property="og:title" content="Authorizing an application · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn more about what it means to authorize a third-party application on Cloudflare"><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/oauth/authorizing-an-application/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals,OAuth documentation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/oauth/authorizing-an-application/#page","headline":"Authorizing an application \u00b7 Cloudflare Fundamentals docs","description":"Learn more about what it means to authorize a third-party application on Cloudflare","url":"https://developers.cloudflare.com/fundamentals/oauth/authorizing-an-application/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/oauth/authorizing-an-application/
  schema: 1
---
<h2 id="overview">Overview</h2>
<p>When you authorize a third-party OAuth application, you grant it permission to access specific Cloudflare resources on your behalf. Cloudflare provides tools to view, manage, and revoke these authorizations at any time.</p>
<h2 id="authorize-a-third-party-application">Authorize a third-party application</h2>
<p>When a third-party application requests access to your Cloudflare account, you will see a consent screen that displays:</p>
<ul>
<li><strong>Application name and logo</strong>: The name and branding of the requesting application</li>
<li><strong>Publisher domain</strong>: The domain and verification status of the application publisher</li>
<li><strong>Account selection</strong>: Choose which Cloudflare account(s) the application can access</li>
<li><strong>Requested permissions</strong>: After selecting the account(s) the application may access, the specific scopes the application is requesting will be displayed before consent is complete. You can also decline optional permissions. To finish the authorization process, review the permissions the application is requesting and select “<strong>Authorize</strong>”</li>
</ul>
<p>Each shield icon indicates who owns the application and whether its domain ownership is verified:</p>
<ul>
<li><strong>Green filled shield</strong>: Cloudflare owns and manages the application.</li>
<li><strong>Blue outlined shield</strong>: A third-party application with verified ownership of its domain.</li>
<li><strong>Amber filled shield</strong>: A third-party application without verified ownership of a domain.</li>
</ul>
<p>Domain verification only confirms that the application owner controls the displayed domain.</p>
<h3 id="edit-optional-permissions">Edit optional permissions</h3>
<p>All requested permissions are selected by default. You can turn off optional permissions, but required permissions remain selected. Select <strong>Read only</strong> to include only optional scopes with read access, or <strong>Full access</strong> to include all optional scopes. If the client has no permissions configured as optional, editing controls do not appear.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8848.md")
</div>
<h2 id="view-and-revoke-authorized-applications">View and revoke authorized applications</h2>
<p>Application authorizations may be viewed and revoked at any time from the profile page on the Cloudflare dashboard.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8849.md")
</div>
<h2 id="account-administrator-controls">Account administrator controls</h2>
<p>If an account is not available for selection during the consent flow, it may be due to an administrator of that account disabling access to account resources via OAuth.</p>
<p>Account administrators can restrict OAuth applications from accessing account resources via <strong>Manage Account</strong> &gt; <strong>Members &gt; Settings &gt; Public OAuth App access</strong>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8847.md")
</aside>
