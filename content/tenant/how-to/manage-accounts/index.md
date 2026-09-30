---
cp9:
  canonical: https://developers.cloudflare.com/tenant/how-to/manage-accounts/
  description: Create, update, and delete customer accounts using the Cloudflare Tenant API or dashboard.
  full_title: Manage accounts · Cloudflare Tenant docs
  head_html: <title>Manage accounts · Cloudflare Tenant docs</title><meta name="generator" content="Nift"><meta name="description" content="Create, update, and delete customer accounts using the Cloudflare Tenant API or dashboard."><link rel="canonical" href="https://developers.cloudflare.com/tenant/how-to/manage-accounts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/tenant/how-to/manage-accounts/index.md"><meta property="og:title" content="Manage accounts · Cloudflare Tenant docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create, update, and delete customer accounts using the Cloudflare Tenant API or dashboard."><meta property="og:url" content="https://developers.cloudflare.com/tenant/how-to/manage-accounts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Tenant"><meta name="algolia_product_filter" content="Tenant"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Tenant"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/tenant/how-to/manage-accounts/#page","headline":"Manage accounts \u00b7 Cloudflare Tenant docs","description":"Create, update, and delete customer accounts using the Cloudflare Tenant API or dashboard.","url":"https://developers.cloudflare.com/tenant/how-to/manage-accounts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /tenant/how-to/manage-accounts/
  schema: 1
---
<p>Each customer or team that uses Cloudflare should have their own account. This ensures proper security and access of resources. Each account acts as a container of zones and other resources. Depending on your needs, you may even provision multiple accounts for a single customer or team.</p>
<p>When you create an account with the Tenant API, your Cloudflare user owns that account from creation, ongoing management, and finally deletion.</p>
<h2 id="create-account">Create account</h2>
<p>Each customer or team that uses Cloudflare should have their own account. This ensures proper security and access of resources. Each account acts as a container of zones and other resources. Depending on your needs, you may even provision multiple accounts for a single customer or team.</p>
<p>When you create an account with the Tenant API, your Cloudflare user owns that account from creation, ongoing management, and finally deletion.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14748.md")
</div></div>
<h2 id="view-accounts">View accounts</h2>
<p>When you create an account with the Tenant API, your Cloudflare user owns that account from creation, ongoing management, and finally deletion.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14751.md")
</div></div>
<h2 id="update-account">Update account</h2>
<p>To update an account, send a <a href="/api/resources/accounts/methods/update/"><code>PUT</code></a> request to the <code>/accounts/{account_id}</code> endpoint.</p>
<h2 id="delete-account">Delete account</h2>
<p>To delete an account you have created, send a <code>DELETE</code> request to the <code>/accounts/{account_id}</code> endpoint.</p>
<p>Account deletion is permanent and will delete any zones or other resources under the account.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="some-resources-require-manual-deletion">Some resources require manual deletion</h3>
@markup("md", "content/.markup/bodies/14745.md")
</aside>
<pre tabindex="0"><code class="language-bash">curl --request DELETE \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id} \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
<p>A successful request will return the id to confirm the operation:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;1b16db169c9cb7853009857198fae1b9&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
