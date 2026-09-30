---
cp9:
  canonical: https://developers.cloudflare.com/zaraz/custom-actions/additional-fields/
  description: Additional fields available in Zaraz custom actions.
  full_title: Additional fields · Cloudflare Zaraz docs
  head_html: <title>Additional fields · Cloudflare Zaraz docs</title><meta name="generator" content="Nift"><meta name="description" content="Additional fields available in Zaraz custom actions."><link rel="canonical" href="https://developers.cloudflare.com/zaraz/custom-actions/additional-fields/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/zaraz/custom-actions/additional-fields/index.md"><meta property="og:title" content="Additional fields · Cloudflare Zaraz docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Additional fields available in Zaraz custom actions."><meta property="og:url" content="https://developers.cloudflare.com/zaraz/custom-actions/additional-fields/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Zaraz"><meta name="algolia_product_filter" content="Zaraz"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Zaraz"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/zaraz/custom-actions/additional-fields/#page","headline":"Additional fields \u00b7 Cloudflare Zaraz docs","description":"Additional fields available in Zaraz custom actions.","url":"https://developers.cloudflare.com/zaraz/custom-actions/additional-fields/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /zaraz/custom-actions/additional-fields/
  schema: 1
---
<p>Some tools supported by Zaraz let you add fields in addition to the required field. Fields can usually be added either to a specific action, or to all the action within a tool, by adding the field as a <strong>Default Field</strong>.</p>
<h2 id="add-an-additional-field-to-a-specific-action">Add an additional field to a specific action</h2>
<p>Adding an additional field to an action will attach it to this action only, and will not affect your other actions.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Tag setup</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Tools Configuration** > **Third-party tools**.
3. Locate the third-party tool with the action you want to add the additional field to, and select **Edit**.
4. Select the action you wish to modify.
5. Select **Add Field**.
6. Choose the desired field from the drop-down menu and select **Add**.
7. Enter the value you wish to pass to the action.
8. Select **Save**.
<p>The new field will now be used in this event.</p>
<h2 id="add-an-additional-field-to-all-actions-in-a-tool">Add an additional field to all actions in a tool</h2>
<p>Adding an additional field to the tool sets it as a default field for all of the tool actions. It is the same as adding it to every action in the tool.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Tag setup</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Tools Configuration** > **Third-party tools**.
3. Locate the third-party tool where you want to add the field, and select **Edit**.
4. Select **Settings** > **Add Field**.
5. Choose the desired field from the drop-down menu, and select **Add**.
6. Enter the value you wish to pass to all the actions in the tool.
7. Select **Save**.
<p>The new field will now be attached to every action that belongs to the tool.</p>
