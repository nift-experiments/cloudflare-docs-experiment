---
cp9:
  canonical: https://developers.cloudflare.com/secrets-store/manage-secrets/
  description: Learn about different operations to manage your secrets in Cloudflare Secrets Store.
  full_title: Manage account secrets · Cloudflare Secrets Store docs
  head_html: <title>Manage account secrets · Cloudflare Secrets Store docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn about different operations to manage your secrets in Cloudflare Secrets Store."><link rel="canonical" href="https://developers.cloudflare.com/secrets-store/manage-secrets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/secrets-store/manage-secrets/index.md"><meta property="og:title" content="Manage account secrets · Cloudflare Secrets Store docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about different operations to manage your secrets in Cloudflare Secrets Store."><meta property="og:url" content="https://developers.cloudflare.com/secrets-store/manage-secrets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Secrets Store"><meta name="algolia_product_filter" content="Secrets Store"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Secrets Store"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/secrets-store/manage-secrets/#page","headline":"Manage account secrets \u00b7 Cloudflare Secrets Store docs","description":"Learn about different operations to manage your secrets in Cloudflare Secrets Store.","url":"https://developers.cloudflare.com/secrets-store/manage-secrets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /secrets-store/manage-secrets/
  schema: 1
---
<p>Secrets can be API tokens, public/private keys, authorization keys, passwords, or even code variables. The only limitation is that a secret must be a string that does not exceed 1024 bytes.</p>
<p>Once a secret is added to the Secrets Store, it can no longer be decrypted or accessed via API or on the dashboard. Only the service associated with a given secret will be able to access it.</p>
<h2 id="limits">Limits</h2>
<p>Customers who create a secrets store in the open beta can have up to 100 secrets per account. Also, there can only be one store per account.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="production-secrets">Production secrets</h3>
@markup("md", "content/.markup/bodies/13781.md")
</aside>
<h2 id="resources">Resources</h2>
<ul>
<li><a href="/workers/wrangler/commands/secrets-store/#secrets-store-secret">Manage via Wrangler</a></li>
<li><a href="/secrets-store/manage-secrets/how-to/#create-a-secret">Create a secret</a></li>
<li><a href="/secrets-store/manage-secrets/how-to/#duplicate-a-secret">Duplicate a secret</a></li>
<li><a href="/secrets-store/manage-secrets/how-to/#edit-a-secret">Edit a secret</a></li>
<li><a href="/secrets-store/manage-secrets/how-to/#delete-a-secret">Delete a secret</a></li>
</ul>
