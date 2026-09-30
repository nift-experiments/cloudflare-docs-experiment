---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-text-add-ons/
  description: Configure text add-ons in Email Security.
  full_title: Configure text add-ons · Cloudflare One docs
  head_html: <title>Configure text add-ons · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure text add-ons in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-text-add-ons/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-text-add-ons/index.md"><meta property="og:title" content="Configure text add-ons · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure text add-ons in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-text-add-ons/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-text-add-ons/#page","headline":"Configure text add-ons \u00b7 Cloudflare One docs","description":"Configure text add-ons in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-text-add-ons/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/settings/detection-settings/configure-text-add-ons/
  schema: 1
---
<p>You can create custom labels to be used as the subject or body prefix for emails with specific dispositions.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4932.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4931.md")
</aside>
<h2 id="subject-prefix">Subject prefix</h2>
<p>To configure a subject prefix:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>.</li>
<li>Select <strong>Email security</strong>.</li>
<li>Select <strong>Settings</strong>, then go to <strong>Detection settings</strong> &gt; <strong>Text add-ons</strong> &gt; <strong>View</strong>.</li>
<li>Select <strong>Configure</strong> &gt; <strong>Subject prefix</strong>.</li>
<li>Populate each disposition with a subject prefix, and turn on the <strong>Status</strong> to enable the subject prefix for a specific disposition.</li>
</ol>
<h3 id="advanced-settings">Advanced settings</h3>
<p>In <strong>Advanced settings</strong>, you can configure <strong>Add &quot;labels&quot; variable</strong>. This option allows you to add a dynamic value for a label that lists dispositions and allows for additional text.</p>
<p>To turn on <strong>Add &quot;labels&quot; variable</strong>:</p>
<ol>
<li>Go to <strong>Advanced settings</strong> &gt; <strong>Add &quot;labels&quot; variable</strong>.</li>
<li>Choose between:
<ul>
<li><strong>Use default</strong>.</li>
<li><strong>Use custom &quot;labels&quot; variable</strong>: Enter the custom label in the text box.</li>
</ul>
</li>
</ol>
<p>Once you have configured the subject prefix, select <strong>Save</strong>.</p>
<h2 id="body-prefix">Body prefix</h2>
<p>A body prefix is a custom label added to the top of the email body for emails with specific dispositions.</p>
<p>Populate each disposition with a body prefix, and turn on the <strong>Status</strong> to enable the body prefix for a specific disposition.</p>
<h3 id="advanced-settings-1">Advanced settings</h3>
<p>In Advanced settings, you can configure <strong>Add &quot;labels&quot; or &quot;threat types&quot; variable</strong>. This option allows you to add a dynamic value for labels that lists dispositions, or threats that lists the threat types behind an assigned disposition.</p>
<p>To turn on <strong>Add &quot;labels&quot; or &quot;threat types&quot; variable</strong>:</p>
<ol>
<li>Go to <strong>Advanced settings</strong>:</li>
<li>Choose between:
<ul>
<li><strong>Add &quot;labels&quot; variable</strong>: This option allows you to add a dynamic value that for a label that lists dispositions and allows for additional text. Choose between:
<ul>
<li><strong>Use default</strong>.</li>
<li><strong>Use custom &quot;labels&quot; variable</strong>: Enter the custom label in the text box.</li>
</ul>
</li>
</ul>
</li>
</ol>
<p>Once you have configured the body prefix, select <strong>Save</strong>.</p>
<h3 id="add-threat-types-variable">Add threat types variable</h3>
<p>This option allows you to include a dynamic value for '%THREATS' that lists the threat types behind an assigned disposition. It can include additional, HTML-formatted text.</p>
<p>The dashboard will display <strong>Default</strong> or <strong>Custom</strong> (to use &quot;labels&quot; or &quot;threat types&quot; variable), depending on how you configured the <a href="/cloudflare-one/email-security/settings/detection-settings/configure-text-add-ons/#advanced-settings-1">advanced settings</a>.</p>
