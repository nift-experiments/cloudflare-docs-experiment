---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/reference/migration-guides/scim-virtual-groups-migration/
  description: Migrate from SCIM v1 Virtual Groups to Cloudflare's GA SCIM User Groups
  full_title: SCIM v1 to v2 Migration · Cloudflare Fundamentals docs
  head_html: <title>SCIM v1 to v2 Migration · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Migrate from SCIM v1 Virtual Groups to Cloudflare&#x27;s GA SCIM User Groups"><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/reference/migration-guides/scim-virtual-groups-migration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/reference/migration-guides/scim-virtual-groups-migration/index.md"><meta property="og:title" content="SCIM v1 to v2 Migration · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Migrate from SCIM v1 Virtual Groups to Cloudflare&#x27;s GA SCIM User Groups"><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/reference/migration-guides/scim-virtual-groups-migration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/reference/migration-guides/scim-virtual-groups-migration/#page","headline":"SCIM v1 to v2 Migration \u00b7 Cloudflare Fundamentals docs","description":"Migrate from SCIM v1 Virtual Groups to Cloudflare's GA SCIM User Groups","url":"https://developers.cloudflare.com/fundamentals/reference/migration-guides/scim-virtual-groups-migration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/reference/migration-guides/scim-virtual-groups-migration/
  schema: 1
---
<p>Cloudflare's first iteration of SCIM integration introduced a concept called <em>Virtual Groups</em>, typically identified by the pattern <code>CF-&lt;accountID&gt;-&lt;Role Name&gt;</code> in your IdP. Virtual Groups were an early implementation of group-based access control: they acted as placeholders created automatically by SCIM to map IdP groups to account memberships.</p>
<p>While customers could add or remove members from these groups within their IdP, Virtual Groups had important limitations:</p>
<ul>
<li>They could not be renamed or deleted in the IdP.</li>
<li>They could not be managed within Cloudflare.</li>
<li>Functionally, managing a Virtual Group was equivalent to syncing users and editing each member’s policies individually.</li>
</ul>
<p>With the GA of <a href="/changelog/2025-06-23-user-groups-ga/">User Groups</a>, Virtual Groups are now deprecated. Customers should migrate to <a href="/fundamentals/manage-members/user-groups/">User Groups</a>, which provide a more flexible and scalable way to assign and manage policies. To maintain SCIM synchronization with the Cloudflare Dashboard, we strongly recommend migrating to <strong>SCIM User Groups</strong>.</p>
<p>If you have never synced a group linked to a <code>CF-&lt;accountID&gt;-&lt;Role Name&gt;</code> Virtual Group from your IdP to Cloudflare, no action is needed.</p>
<h2 id="migration-steps">Migration steps</h2>
<ol>
<li><strong>Create a new SCIM integration</strong> in your IdP using an <a href="/fundamentals/account/account-security/scim-setup/">Account Owned Token</a> provisioned in Cloudflare.</li>
<li><strong>Assign users &amp; groups to your new Application</strong> in your IdP, following a naming convention that aligns with your internal processes.</li>
<li><strong>Sync groups to Cloudflare</strong> and verify they appear in the <strong>User Groups</strong> pane of the Cloudflare Dashboard.</li>
<li><strong>Attach permission policies</strong> to the new User Groups so members inherit the correct access upon assignment to the group.</li>
<li><strong>Migrate users</strong> into the new groups incrementally, testing synchronization of users &amp; groups into the Cloudflare Dashboard.</li>
<li><strong>Clean up legacy resources</strong> by removing SCIM v1 Virtual Groups and IdP mappings that follow the <code>CF-&lt;accountID&gt;-&lt;Role Name&gt;</code> pattern.</li>
</ol>
<h2 id="more-resources">More resources</h2>
<ul>
<li><a href="/changelog/2025-06-02-user-groups-beta/">User Groups changelog</a></li>
<li><a href="/fundamentals/manage-members/user-groups/">User Groups documentation</a></li>
<li><a href="/fundamentals/api/get-started/account-owned-tokens/#create-an-account-owned-token">Create an Account Owned Token</a></li>
<li><a href="/fundamentals/account/account-security/scim-setup/">SCIM provisioning setup guide</a></li>
</ul>
