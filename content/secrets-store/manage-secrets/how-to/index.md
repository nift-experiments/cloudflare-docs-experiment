---
cp9:
  canonical: https://developers.cloudflare.com/secrets-store/manage-secrets/how-to/
  description: Create, update, duplicate, and delete secrets using the dashboard, API, or Wrangler.
  full_title: How to · Cloudflare Secrets Store docs
  head_html: <title>How to · Cloudflare Secrets Store docs</title><meta name="generator" content="Nift"><meta name="description" content="Create, update, duplicate, and delete secrets using the dashboard, API, or Wrangler."><link rel="canonical" href="https://developers.cloudflare.com/secrets-store/manage-secrets/how-to/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/secrets-store/manage-secrets/how-to/index.md"><meta property="og:title" content="How to · Cloudflare Secrets Store docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create, update, duplicate, and delete secrets using the dashboard, API, or Wrangler."><meta property="og:url" content="https://developers.cloudflare.com/secrets-store/manage-secrets/how-to/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Secrets Store"><meta name="algolia_product_filter" content="Secrets Store"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Secrets Store"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/secrets-store/manage-secrets/how-to/#page","headline":"How to \u00b7 Cloudflare Secrets Store docs","description":"Create, update, duplicate, and delete secrets using the dashboard, API, or Wrangler.","url":"https://developers.cloudflare.com/secrets-store/manage-secrets/how-to/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /secrets-store/manage-secrets/how-to/
  schema: 1
---
<p>Refer to the sections below to learn about common actions you might want to take when managing your data in Secrets Store.</p>
<p>You must have a <a href="/secrets-store/access-control/">Super Administrator or Secrets Store Admin role</a> within your Cloudflare account.</p>
<h2 id="manage-via-wrangler">Manage via Wrangler</h2>
<p><a href="/workers/wrangler/">Wrangler</a> is a command-line interface (CLI) that allows you to manage <a href="/workers/">Cloudflare Workers</a> projects. Refer to <a href="/workers/wrangler/commands/secrets-store/#secrets-store-secret">Wrangler commands</a> for guidance on how to use it with Secrets Store.</p>
<h2 id="create-a-secret">Create a secret</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13788.md")
</div></div>
<h2 id="duplicate-a-secret">Duplicate a secret</h2>
<p>Duplicate a secret to keep the same secret value but change name, scope, or comments.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13791.md")
</div></div>
<h2 id="edit-a-secret">Edit a secret</h2>
<p>Edit a secret to replace an existing value with a new one.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13783.md")
</aside>
<p>You can also edit the secret <strong>Permission scope</strong> and <strong>Comment</strong>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13794.md")
</div></div>
<h2 id="delete-a-secret">Delete a secret</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13782.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13797.md")
</div></div>
