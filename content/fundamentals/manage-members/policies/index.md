---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/manage-members/policies/
  description: Understand how Cloudflare account member policies combine actors, roles, and scopes to define access permissions.
  full_title: Policies · Cloudflare Fundamentals docs
  head_html: <title>Policies · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand how Cloudflare account member policies combine actors, roles, and scopes to define access permissions."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/manage-members/policies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/manage-members/policies/index.md"><meta property="og:title" content="Policies · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand how Cloudflare account member policies combine actors, roles, and scopes to define access permissions."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/manage-members/policies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/manage-members/policies/#page","headline":"Policies \u00b7 Cloudflare Fundamentals docs","description":"Understand how Cloudflare account member policies combine actors, roles, and scopes to define access permissions.","url":"https://developers.cloudflare.com/fundamentals/manage-members/policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/manage-members/policies/
  schema: 1
---
<p>Policies define what access a given user has to your account or domains, and are constructed out of three parts:</p>
<ol>
<li>An actor (your user).</li>
<li>A <code>ResourceGroup</code> (a scope).</li>
<li>A <code>PermissionGroup</code> (roles).</li>
</ol>
<p>An account member can have one or several of these policies to represent the most appropriate access. A member’s effective permissions are the union of all policies assigned to them—whether directly, or through group membership.</p>
<p>To increase the usability and flexibility of Cloudflare's role system, changes to the API have been made to expose these underlying data principles and allow users to interact with them.</p>
<p>For example, you may want to assign multiple policies and use scopes to control access to an account where you have a single account with both Production and Staging domains, and a user that should be able see the whole account, purge the production domains, but have the ability to configure the staging domains.</p>
<h2 id="manage-policies">Manage policies</h2>
<p>A set of standard API endpoints is present on every account that allow access to your members, which has recently been enhanced by a list of <code>resourceGroups</code> and <code>PermissionGroups</code>.</p>
<ul>
<li>A <code>resourceGroup</code> is a unique identifier for the scope for which a policy applies.</li>
<li>A <code>permissionGroup</code> is a unique identifier for the set of roles that are assigned to a given policy.</li>
</ul>
<p>Refer to the <a href="/api/">API documentation</a> for more information.</p>
<h2 id="viewing-effective-permissions">Viewing Effective Permissions</h2>
<p>Cloudflare supports assigning permissions to members both directly and through <a href="/fundamentals/manage-members/user-groups/">User Groups</a>. A member’s effective permissions are additive; they represent the union of all permissions granted directly to a member and those inherited through a member's group membership.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8863.md")
</aside>
