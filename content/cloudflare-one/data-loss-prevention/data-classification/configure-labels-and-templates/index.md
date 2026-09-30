---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/data-classification/configure-labels-and-templates/
  description: Create labels and build from templates in Cloudflare DLP Data Classification.
  full_title: Configure labels and templates · Cloudflare One docs
  head_html: <title>Configure labels and templates · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Create labels and build from templates in Cloudflare DLP Data Classification."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/data-classification/configure-labels-and-templates/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/data-classification/configure-labels-and-templates/index.md"><meta property="og:title" content="Configure labels and templates · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create labels and build from templates in Cloudflare DLP Data Classification."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/data-classification/configure-labels-and-templates/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Compliance"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/data-classification/configure-labels-and-templates/#page","headline":"Configure labels and templates \u00b7 Cloudflare One docs","description":"Create labels and build from templates in Cloudflare DLP Data Classification.","url":"https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/data-classification/configure-labels-and-templates/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Compliance"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/data-loss-prevention/data-classification/configure-labels-and-templates/
  schema: 1
---
<p>Labels and templates define the classification metadata you can apply to sensitive content in Cloudflare DLP.</p>
<p>Use the <strong>Labels</strong> tab to create and manage sensitivity schemas, sensitivity levels, data tag groups, and data tags. Use the <strong>Templates</strong> tab to review Cloudflare-managed starting points for sensitivity schemas and data tag groups.</p>
<h2 id="labels">Labels</h2>
<p>Labels help you describe matched content in a consistent way.</p>
<p>Data Classification supports two label types:</p>
<ul>
<li><strong>Sensitivity schemas and levels</strong> define an ordered classification hierarchy.</li>
<li><strong>Data tag groups and tags</strong> define additional descriptors you can apply to content.</li>
</ul>
<p>You can use labels directly in custom DLP profiles and assign them through data classes.</p>
<h3 id="sensitivity-schemas-and-levels">Sensitivity schemas and levels</h3>
<p>A sensitivity schema is a named hierarchy of sensitivity levels, such as <code>Public</code>, <code>Internal</code>, <code>Confidential</code>, or <code>Restricted</code>.</p>
<p>Each schema contains one or more ordered levels. In custom DLP profiles, selecting a sensitivity level lets you match content at that level or higher within the selected schema.</p>
<h3 id="create-a-sensitivity-schema">Create a sensitivity schema</h3>
<p>When creating a sensitivity schema, you can either create a custom schema from scratch or start from a template.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Data classification</strong> &gt; <strong>Labels</strong>.</li>
<li>Select <strong>Create labels</strong>.</li>
<li>In <strong>Sensitivity schema</strong>, choose one of the following:
<ul>
<li><strong>Create a custom schema</strong> to define the schema from scratch</li>
<li><strong>Choose a template</strong> to start from a Cloudflare-managed template</li>
</ul>
</li>
<li>Enter or review the name and description.</li>
<li>Add or update the sensitivity levels you want to include, in order.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>You can edit the resulting sensitivity schema after creation.</p>
<h3 id="data-tag-groups-and-tags">Data tag groups and tags</h3>
<p>A data tag group contains related tags you can use to describe content beyond its sensitivity level. For example, a data tag group could contain tags for business function, data owner, or content category.</p>
<h3 id="create-a-data-tag-group">Create a data tag group</h3>
<p>When creating a data tag group, you can either create a custom group from scratch or start from a template.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Data classification</strong> &gt; <strong>Labels</strong>.</li>
<li>Select <strong>Create labels</strong>.</li>
<li>In <strong>Data tag group</strong>, choose one of the following:
<ul>
<li><strong>Create a custom group</strong> to define the group from scratch</li>
<li><strong>Choose a template</strong> to start from a Cloudflare-managed template</li>
</ul>
</li>
<li>Enter or review the name and description.</li>
<li>Add or update the data tags you want to include.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>You can edit the resulting data tag group after creation.</p>
<h2 id="templates">Templates</h2>
<p>Templates provide Cloudflare-managed starting points for sensitivity schemas and data tag groups.</p>
<p>Templates are not linked objects. When you build from a template, Cloudflare creates a new sensitivity schema or data tag group in your account. After that, you can edit it like any other label object you create.</p>
<p>You can start from a template in either of the following ways:</p>
<ul>
<li>from the <strong>Templates</strong> tab, by reviewing a template and selecting <strong>Build with template</strong></li>
<li>from the <strong>Labels</strong> tab, by selecting <strong>Create labels</strong> and then <strong>Choose a template</strong> inline during creation</li>
</ul>
<h3 id="build-from-a-template-from-the-templates-tab">Build from a template from the Templates tab</h3>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Data classification</strong> &gt; <strong>Templates</strong>.</li>
<li>Select a template to review its details.</li>
<li>Select <strong>Build with template</strong>.</li>
<li>Review and customize the resulting sensitivity schema or data tag group.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>After you build from a template, the resulting object appears in the <strong>Labels</strong> tab and can be used in data classes and DLP profiles.</p>
<h2 id="use-labels-in-dlp">Use labels in DLP</h2>
<p>After you create labels, you can use them in either of the following ways:</p>
<ul>
<li>assign them to content through <a href="/cloudflare-one/data-loss-prevention/data-classification/build-a-data-class/">Build a data class</a></li>
<li>apply them directly in <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">custom DLP profiles</a></li>
</ul>
<p>In custom DLP profiles, sensitivity levels and data tags can be used directly as profile criteria, even when they are not assigned through a data class.</p>
