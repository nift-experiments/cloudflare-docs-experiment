---
cp9:
  canonical: https://developers.cloudflare.com/zaraz/advanced/blocking-triggers/
  description: Prevent triggers from firing under specific conditions.
  full_title: Blocking Triggers · Cloudflare Zaraz docs
  head_html: <title>Blocking Triggers · Cloudflare Zaraz docs</title><meta name="generator" content="Nift"><meta name="description" content="Prevent triggers from firing under specific conditions."><link rel="canonical" href="https://developers.cloudflare.com/zaraz/advanced/blocking-triggers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/zaraz/advanced/blocking-triggers/index.md"><meta property="og:title" content="Blocking Triggers · Cloudflare Zaraz docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Prevent triggers from firing under specific conditions."><meta property="og:url" content="https://developers.cloudflare.com/zaraz/advanced/blocking-triggers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Zaraz"><meta name="algolia_product_filter" content="Zaraz"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Zaraz"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/zaraz/advanced/blocking-triggers/#page","headline":"Blocking Triggers \u00b7 Cloudflare Zaraz docs","description":"Prevent triggers from firing under specific conditions.","url":"https://developers.cloudflare.com/zaraz/advanced/blocking-triggers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /zaraz/advanced/blocking-triggers/
  schema: 1
---
<p>Blocking Triggers are triggers that instead of being used to define when to start an action, are used to define when to <em>not</em> start an action. You may need to block one or more actions in a tool from firing when a specific condition arises. For these cases, you can set Blocking Triggers.</p>
<p>Every tool action has Firing Triggers assigned to it. Blocking Triggers are optional and, if defined, will conditionally prevent the action from starting. When you add Blocking Triggers to an action, the action will not fire if any of its Blocking Triggers are true. If the tool has more than one action, other actions without these Blocking Triggers will still work.</p>
<p>To conditionally block all actions in a tool, you have to configure Blocking Triggers on every action that belongs to that tool. Note that when you use Blocking Triggers, Zaraz will still load on the page.</p>
<p>To use Blocking Triggers, start by <a href="/zaraz/custom-actions/create-trigger/">creating the trigger</a> with the conditions you want to use to block an event. Then:</p>
<ol>
<li>Go to <a href="https://dash.cloudflare.com/?to=/:account/:zone/zaraz"><strong>Zaraz</strong></a> &gt; <strong>Tools Configuration</strong>.</li>
<li>Under <strong>Third-party tools</strong>, locate the tool with the action you want to block and select <strong>Edit</strong>.</li>
<li>In <strong>Action Name</strong>, select the action you want to block.</li>
<li>In <strong>Blocking Triggers</strong>, use the dropdown menu to add a trigger to block the action.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17612.md")
</aside>
