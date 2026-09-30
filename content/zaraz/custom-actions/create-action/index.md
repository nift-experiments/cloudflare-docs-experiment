---
cp9:
  canonical: https://developers.cloudflare.com/zaraz/custom-actions/create-action/
  description: Create a custom action to send data to third-party tools.
  full_title: Create an action · Cloudflare Zaraz docs
  head_html: <title>Create an action · Cloudflare Zaraz docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a custom action to send data to third-party tools."><link rel="canonical" href="https://developers.cloudflare.com/zaraz/custom-actions/create-action/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/zaraz/custom-actions/create-action/index.md"><meta property="og:title" content="Create an action · Cloudflare Zaraz docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a custom action to send data to third-party tools."><meta property="og:url" content="https://developers.cloudflare.com/zaraz/custom-actions/create-action/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Zaraz"><meta name="algolia_product_filter" content="Zaraz"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Zaraz"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/zaraz/custom-actions/create-action/#page","headline":"Create an action \u00b7 Cloudflare Zaraz docs","description":"Create a custom action to send data to third-party tools.","url":"https://developers.cloudflare.com/zaraz/custom-actions/create-action/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /zaraz/custom-actions/create-action/
  schema: 1
---
<p>Once you have your triggers ready, you can use them to configure your actions. An action defines a specific task that your tool will perform.</p>
<p>To create an action, first <a href="/zaraz/get-started/">add a third-party tool</a>. If you have already added a third-party tool, follow these steps to create an action.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Tag setup</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Go to **Tools Configuration**.
3. Under **Third-party tools**, locate the tool you want to configure an action for, and select **Edit**.
4. Under Custom actions select **Create action**.
5. Give the action a descriptive name.
6. In the **Firing Triggers** field, choose the relevant trigger or triggers you [previously created](/zaraz/custom-actions/create-trigger/). If you choose more than one trigger, the action will start when any of the selected triggers are matched.
7. Depending on the tool you are adding an action for, you might also have the option to choose an **Action type**. You might also need to fill in more fields in order to complete setting up the action.
8. Select **Save**.
<p>The new action will appear under <strong>Tool actions</strong>. To edit or disable/enable an action, refer to <a href="/zaraz/custom-actions/edit-tools-and-actions/">Edit tools and actions</a>.</p>
