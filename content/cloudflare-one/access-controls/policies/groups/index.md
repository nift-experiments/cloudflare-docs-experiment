---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/policies/groups/
  description: How Rule groups works in Access.
  full_title: Rule groups · Cloudflare One docs
  head_html: <title>Rule groups · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How Rule groups works in Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/groups/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/groups/index.md"><meta property="og:title" content="Rule groups · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Rule groups works in Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/groups/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="REST API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/policies/groups/#page","headline":"Rule groups \u00b7 Cloudflare One docs","description":"How Rule groups works in Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/policies/groups/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["REST API"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/policies/groups/
  schema: 1
---
<p>A rule group is a collection of Access rules that can be configured once and then quickly applied across many Access policies. Rule groups use the same <a href="/cloudflare-one/access-controls/policies/#rule-types">rule types</a> and <a href="/cloudflare-one/access-controls/policies/#selectors">selectors</a> shown in the Access policy builder.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4589.md")
</aside>
<h2 id="create-a-rule-group">Create a rule group</h2>
<p>To create an Access rule group:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4592.md")
</div></div>
<p>You can now add this group to an Access policy using the <em>Rule groups</em> selector.</p>
<h2 id="use-cases">Use cases</h2>
<h3 id="ip-based-rules">IP-based rules</h3>
<p>We recommend using rule groups to define any IP address-based rules you configure in policies. Keeping IP addresses in one place allows you to modify or remove addresses once, rather than in each policy, and reduces the potential for mistakes.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4588.md")
</aside>
<h3 id="country-requirements">Country requirements</h3>
<p>You can create a rule group that consists of countries to allow or block. Access will treat the countries in the Include rule with an OR logical operator. When building policies for an Access application, you can assign this rule group to a Require policy to require at least one of the countries inside of the group. For an example policy, refer to <a href="/cloudflare-one/access-controls/policies/#require-rules-with-or-operators">Require rules with OR operators</a>.</p>
