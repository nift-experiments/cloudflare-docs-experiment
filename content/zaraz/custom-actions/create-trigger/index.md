---
cp9:
  canonical: https://developers.cloudflare.com/zaraz/custom-actions/create-trigger/
  description: Create triggers that fire actions based on page events.
  full_title: Create a trigger · Cloudflare Zaraz docs
  head_html: <title>Create a trigger · Cloudflare Zaraz docs</title><meta name="generator" content="Nift"><meta name="description" content="Create triggers that fire actions based on page events."><link rel="canonical" href="https://developers.cloudflare.com/zaraz/custom-actions/create-trigger/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/zaraz/custom-actions/create-trigger/index.md"><meta property="og:title" content="Create a trigger · Cloudflare Zaraz docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create triggers that fire actions based on page events."><meta property="og:url" content="https://developers.cloudflare.com/zaraz/custom-actions/create-trigger/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Zaraz"><meta name="algolia_product_filter" content="Zaraz"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Zaraz"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/zaraz/custom-actions/create-trigger/#page","headline":"Create a trigger \u00b7 Cloudflare Zaraz docs","description":"Create triggers that fire actions based on page events.","url":"https://developers.cloudflare.com/zaraz/custom-actions/create-trigger/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /zaraz/custom-actions/create-trigger/
  schema: 1
---
<p>Triggers define the conditions under which a tool will start an action. Since a tool must have actions in order to work, and actions must have triggers, it is important to set up your website's triggers correctly. A trigger can be made out of one or more Rules. Zaraz supports <a href="/zaraz/reference/triggers/">multiple types of Trigger Rules</a>.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Tag setup</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Go to **Tools Configuration**.
3. Select the **Triggers** tab.
4. Select **Create trigger**.
5. In **Trigger Name** enter a descriptive name for your trigger.
6. In **Rule type**, choose from the actions available in the drop-down menu to start building your rule. Refer to [Triggers and rules](/zaraz/reference/triggers/) for more information on what each rule type means.
7. In **Variable name**, input the variable you want as the trigger. For example, use _Event Name_ if you are using [`zaraz.track()`](/zaraz/web-api/track/) in your website. If you want to use a variable you have previously [created in Variables](/zaraz/variables/create-variables/), select the `+` sign in the drop-down menu, scroll to **Variables**, and choose your variable.
8. Use the **Match operation** drop-down list to choose a comparison operator. For an expression to match, the value in **Variable name** and **Match string** must satisfy the comparison operator.
9. In **Match string**, input the string that completes the rule.
10. You can add more than one rule to your trigger. Select **Add rule** and repeat steps 5-8 to add another set of rules and conditions. If you add more than one rule, your trigger will only be valid when all conditions are true.
11. Select **Save**.
<p>Your trigger is now complete. If you go back to the main page you will see it listed under <strong>Triggers</strong>, as well as which tools use it. You can also <a href="/zaraz/custom-actions/edit-triggers/"><strong>Edit</strong> or <strong>Delete</strong> your trigger</a>.</p>
