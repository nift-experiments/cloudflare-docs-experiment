---
cp9:
  canonical: https://developers.cloudflare.com/zaraz/variables/create-variables/
  description: Create custom variables for use in Zaraz actions.
  full_title: Create a variable · Cloudflare Zaraz docs
  head_html: <title>Create a variable · Cloudflare Zaraz docs</title><meta name="generator" content="Nift"><meta name="description" content="Create custom variables for use in Zaraz actions."><link rel="canonical" href="https://developers.cloudflare.com/zaraz/variables/create-variables/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/zaraz/variables/create-variables/index.md"><meta property="og:title" content="Create a variable · Cloudflare Zaraz docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create custom variables for use in Zaraz actions."><meta property="og:url" content="https://developers.cloudflare.com/zaraz/variables/create-variables/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Zaraz"><meta name="algolia_product_filter" content="Zaraz"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Zaraz"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/zaraz/variables/create-variables/#page","headline":"Create a variable \u00b7 Cloudflare Zaraz docs","description":"Create custom variables for use in Zaraz actions.","url":"https://developers.cloudflare.com/zaraz/variables/create-variables/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /zaraz/variables/create-variables/
  schema: 1
---
<p>Variables are reusable blocks of information. They allow you to have one source of data you can reuse across tools and triggers in the dashboard. You can then update this data in a single place.</p>
<p>For example, instead of typing a specific user ID in multiple fields, you can create a variable with that information instead. If there is a change and you have to update the user ID, you just need to update the variable and the change will be reflected across the dashboard.</p>
<p><a href="/zaraz/variables/worker-variables/">Worker Variables</a> are a special type of variable that generates value dynamically.</p>
<h2 id="create-a-new-variable">Create a new variable</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Tag setup</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Go to **Tools Configuration** > **Variables**.
3. Select **Create variable**, and give it a name.
4. In **Variable type** select between `String`, `Masked variable` or `Worker` from the drop-down menu. Use `Masked variable` when you have a private value that you do not want to share, such as an API token.
5. In **Variable value** enter the value of your variable.
6. Select **Save**.
<p>Your variable is now ready to be used with tools and triggers.</p>
<h2 id="next-steps">Next steps</h2>
<p>Refer to <a href="/zaraz/get-started/">Add a third-party tool</a> and <a href="/zaraz/custom-actions/create-trigger/">Create a trigger</a> for more information on how to add a variable to tools and triggers.</p>
<p>If you need to edit or delete variables, refer to <a href="/zaraz/variables/edit-variables/">Edit variables</a>.</p>
