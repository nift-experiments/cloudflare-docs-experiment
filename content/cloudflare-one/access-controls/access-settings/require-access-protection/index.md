---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/require-access-protection/
  description: Require Access protection in Access.
  full_title: Require Access protection · Cloudflare One docs
  head_html: <title>Require Access protection · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Require Access protection in Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/require-access-protection/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/require-access-protection/index.md"><meta property="og:title" content="Require Access protection · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Require Access protection in Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/require-access-protection/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Security"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/require-access-protection/#page","headline":"Require Access protection \u00b7 Cloudflare One docs","description":"Require Access protection in Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/require-access-protection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Security"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/access-settings/require-access-protection/
  schema: 1
---
<p>Cloudflare Access allows you to require Access protection for all hostnames in your account. When this setting is turned on, traffic to any hostname without a matching <a href="/cloudflare-one/access-controls/applications/">Access application</a> is automatically blocked.</p>
<p>This deny-by-default approach prevents accidental exposure of internal resources to the public Internet. Without this setting, a developer could deploy a new application or create a DNS record and inadvertently expose the resource before configuring an Access application.</p>
<h2 id="turn-on-access-protection">Turn on Access protection</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4739.md")
</aside>
<ol>
<li>
<p>Log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Access settings</strong>.</p>
</li>
<li>
<p>Turn on <strong>Block traffic to all domains in this account</strong>. You will see a dialog confirming you understand the scope of this change. Select <strong>Confirm</strong>.</p>
<p>Traffic to all hostnames in the account is now blocked unless an Access application exists for the hostname.</p>
</li>
<li>
<p>(Optional) Under <strong>Hostnames to Exempt</strong>, select specific domains to exempt from the <strong>Block traffic to all domains in this account</strong> setting. Traffic to exempted hostnames is allowed even if no Access application exists.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4738.md")
</aside>
<h2 id="allow-traffic-to-a-hostname">Allow traffic to a hostname</h2>
<p>To allow traffic to a hostname when <strong>Block traffic to all domains in this account</strong> is turned on:</p>
<ol>
<li><a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">Create an Access application</a> for the hostname.</li>
<li>Add an <a href="/cloudflare-one/access-controls/policies/#allow">Allow policy</a> to grant access to authorized users.</li>
<li>(Optional) Add a <a href="/cloudflare-one/access-controls/policies/#bypass">Bypass policy</a> if the hostname should be publicly accessible without authentication.</li>
</ol>
<h2 id="blocked-request-behavior">Blocked request behavior</h2>
<p>When a user attempts to access a hostname without an Access application, Cloudflare displays a block page with <code>Error 1050: This resource is blocked by this account's Default-Deny policy.</code> The user cannot proceed until an administrator creates an Access application for that hostname.</p>
