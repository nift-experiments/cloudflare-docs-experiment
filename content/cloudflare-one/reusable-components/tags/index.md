---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/reusable-components/tags/
  description: Tags in Zero Trust.
  full_title: Tags · Cloudflare One docs
  head_html: <title>Tags · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Tags in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/tags/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/tags/index.md"><meta property="og:title" content="Tags · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Tags in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/reusable-components/tags/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/reusable-components/tags/#page","headline":"Tags \u00b7 Cloudflare One docs","description":"Tags in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/reusable-components/tags/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/reusable-components/tags/
  schema: 1
---
<p>You can label an Access application with up to 25 custom tags. End users can then filter the applications in their <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a> by their tags.</p>
<h3 id="create-a-tag">Create a tag</h3>
<p>To create a new tag:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Tags</strong>.</li>
<li>Select <strong>Add a tag</strong>.</li>
<li>Enter up to 35 alphanumeric characters for the tag (for example, <code>Human Resources</code>) and select it in the dropdown menu.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>You can now <a href="#tag-an-access-application">add this tag</a> to an Access application.</p>
<h3 id="tag-an-access-application">Tag an Access application</h3>
<p>To add a tag to an existing Access application:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select an application and select <strong>Configure</strong>.</li>
<li>Go to <strong>Additional settings</strong>.</li>
<li>In the <strong>Tags</strong> dropdown, select the tags that you would like to assign to this application. The tag must be <a href="#create-a-tag">created</a> before you can select it in the dropdown.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>The tag will now appear on the application's App Launcher tile.</p>
