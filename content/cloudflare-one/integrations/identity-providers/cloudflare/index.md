---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/
  description: Use Cloudflare as an identity provider for Access policies, allowing authentication based on Cloudflare account membership.
  full_title: Cloudflare as identity provider · Cloudflare One docs
  head_html: <title>Cloudflare as identity provider · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Cloudflare as an identity provider for Access policies, allowing authentication based on Cloudflare account membership."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/index.md"><meta property="og:title" content="Cloudflare as identity provider · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Cloudflare as an identity provider for Access policies, allowing authentication based on Cloudflare account membership."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="REST API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/#page","headline":"Cloudflare as identity provider \u00b7 Cloudflare One docs","description":"Use Cloudflare as an identity provider for Access policies, allowing authentication based on Cloudflare account membership.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/cloudflare/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["REST API"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/cloudflare/
  schema: 1
---
<p>Cloudflare Access can use Cloudflare itself as an identity provider, allowing you to build Access policies that match on Cloudflare account membership. This is useful for scenarios where you want to restrict access to users who are members of a specific Cloudflare account, without requiring a third-party identity provider.</p>
<p>When a user authenticates through the Cloudflare identity provider, Access verifies their Cloudflare account membership and grants or denies access based on your policy configuration.</p>
<p>For newly created Zero Trust organizations, Cloudflare adds this identity provider automatically as the default login method, with <strong>Restrict to account members</strong> enabled. You do not need to set it up manually. The following steps describe how to add or reconfigure it.</p>
<h2 id="set-up-cloudflare-as-an-identity-provider">Set up Cloudflare as an identity provider</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5085.md")
</div></div>
<h2 id="configuration-options">Configuration options</h2>
<table>
<thead>
<tr>
<th>Option</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Restrict to account members</strong></td>
<td>When enabled, only users who are members of your Cloudflare account can authenticate. When disabled, any Cloudflare user can authenticate (subject to your Access policies).</td>
<td>Disabled</td>
</tr>
</tbody>
</table>
<p>The <strong>Default</strong> column reflects the value when you add this identity provider manually. When Cloudflare configures it automatically for a new organization, <strong>Restrict to account members</strong> is enabled.</p>
<h2 id="use-cloudflare-account-membership-in-policies">Use Cloudflare account membership in policies</h2>
<p>After configuring Cloudflare as an identity provider, you can use the <strong>Cloudflare Account Member</strong> selector in your <a href="/cloudflare-one/access-controls/policies/">Access policies</a>. This selector matches users based on their membership in a Cloudflare account.</p>
<ul>
<li>If you omit the account ID, the selector matches members of the current account (the account where the Access policy is configured).</li>
<li>If you specify an account ID, the selector matches members of that specific account.</li>
</ul>
<p>This is useful for cross-account access scenarios where you need to grant access to users from a different Cloudflare account.</p>
