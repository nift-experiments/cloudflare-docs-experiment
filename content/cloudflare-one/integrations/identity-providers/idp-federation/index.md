---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/idp-federation/
  description: Share an identity provider across multiple Cloudflare accounts in your organization using IdP federation.
  full_title: IdP federation · Cloudflare One docs
  head_html: <title>IdP federation · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Share an identity provider across multiple Cloudflare accounts in your organization using IdP federation."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/idp-federation/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/idp-federation/index.md"><meta property="og:title" content="IdP federation · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Share an identity provider across multiple Cloudflare accounts in your organization using IdP federation."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/idp-federation/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="REST API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/idp-federation/#page","headline":"IdP federation \u00b7 Cloudflare One docs","description":"Share an identity provider across multiple Cloudflare accounts in your organization using IdP federation.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/idp-federation/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["REST API"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/idp-federation/
  schema: 1
---
<p>IdP federation allows organizations with multiple Cloudflare accounts to use a single identity provider (IdP) configuration across accounts. Instead of configuring the same IdP (for example, Okta or Entra ID) separately in every account, you configure it once in a source account and share it with the other accounts in your organization.</p>
<p>Each recipient account gets a read-only IdP connection that routes authentication back to the source account through a bridge — a hidden application in the source account that brokers the cross-account login. End users sign in with their existing IdP credentials, and each account's Access policies evaluate the resulting identity just like any other IdP login.</p>
<h2 id="how-it-works">How it works</h2>
<p>Setting up IdP federation is a two-step process:</p>
<ol>
<li><strong>Create a federation grant.</strong> A grant permits an IdP to be shared across accounts. Creating a grant also provisions a hidden bridge application in the source account.</li>
<li><strong>Share the grant.</strong> Distribute the grant to specific accounts or to your entire organization. Each recipient account is automatically provisioned with a read-only IdP connection that points to the bridge.</li>
</ol>
<p>When a user in a recipient account authenticates, the request is routed through the bridge to the source IdP. The source IdP handles authentication, and the resulting identity claims are passed back to the recipient account's Access policies.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>You must have permission to edit the source IdP in the source account.</li>
<li>You must be a member of a <a href="/fundamentals/organizations/">Cloudflare Organization</a>.</li>
<li>The source account must belong to a Cloudflare Organization.</li>
</ul>
<h2 id="share-an-idp">Share an IdP</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5051.md")
</div></div>
<h2 id="stop-sharing-an-idp">Stop Sharing an IdP</h2>
<p>To stop sharing an IdP, delete the federation grant, as well as the share.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5048.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5054.md")
</div></div>
<h2 id="limitations">Limitations</h2>
<ul>
<li>An account can federate at most one IdP as a source.</li>
<li>A source IdP cannot be deleted while it has a federation grant associated with it. Delete the grant first.</li>
</ul>
