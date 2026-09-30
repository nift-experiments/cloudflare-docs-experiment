---
cp9:
  canonical: https://developers.cloudflare.com/tenant/glossary/
  description: Key terms and definitions used throughout the Cloudflare Tenant API documentation.
  full_title: Glossary · Cloudflare Tenant docs
  head_html: <title>Glossary · Cloudflare Tenant docs</title><meta name="generator" content="Nift"><meta name="description" content="Key terms and definitions used throughout the Cloudflare Tenant API documentation."><link rel="canonical" href="https://developers.cloudflare.com/tenant/glossary/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/tenant/glossary/index.md"><meta property="og:title" content="Glossary · Cloudflare Tenant docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Key terms and definitions used throughout the Cloudflare Tenant API documentation."><meta property="og:url" content="https://developers.cloudflare.com/tenant/glossary/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Tenant"><meta name="algolia_product_filter" content="Tenant"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Glossary"><meta name="algolia_content_type" content="Glossary"><meta name="pcx_additional_products" content="Tenant"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/tenant/glossary/#page","headline":"Glossary \u00b7 Cloudflare Tenant docs","description":"Key terms and definitions used throughout the Cloudflare Tenant API documentation.","url":"https://developers.cloudflare.com/tenant/glossary/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /tenant/glossary/
  schema: 1
---
<p>The following terms are used throughout the Tenant API docs. For more details on how these concepts interact with each other, refer to <a href="/tenant/structure/">Tenant structure</a>.</p>
<h2 id="tenant">Tenant</h2>
<p>A <strong>Tenant</strong> is a special type of Cloudflare account that contains other accounts and resources.</p>
<h2 id="tenant-admin">Tenant admin</h2>
<p>Once you sign a partner agreement with Cloudflare, we create a special Tenant account and then add your user to that account as a <strong>Tenant admin</strong>. Cloudflare can add multiple users as Tenant admins upon request.</p>
<p>Tenant admins then become the default <a href="/fundamentals/manage-members/roles/"><strong>Super administrator(s)</strong></a> for all accounts and zones contained within the Tenant.</p>
<p>This means that each Tenant admin's user API key can be used to provision accounts based on the catalog specified in your partner agreement.</p>
<p>If needed, you can also <a href="/fundamentals/manage-members/manage/">create additional <strong>Super administrators</strong></a>.</p>
<h2 id="account">Account</h2>
<p>An entity that contains various settings, users, and resources (zones, Zero Trust applications, Workers).</p>
<h2 id="user">User</h2>
<p>A member of a Cloudflare account with their own user profile and <a href="/fundamentals/manage-members/roles/">an associated role</a> that specifies their privileges within that account.</p>
<h2 id="resource">Resource</h2>
<p>A resource is an entity owned by an account, which could be a zone/domain, a Workers instance, or a Zero Trust application.</p>
