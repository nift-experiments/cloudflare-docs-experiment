---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-network-firewall/how-to/create-rate-limiting-policies/
  description: Create rate limiting policies for network traffic.
  full_title: Create Rate Limiting policies (beta) · Cloudflare Network Firewall docs
  head_html: <title>Create Rate Limiting policies (beta) · Cloudflare Network Firewall docs</title><meta name="generator" content="Nift"><meta name="description" content="Create rate limiting policies for network traffic."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-network-firewall/how-to/create-rate-limiting-policies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-network-firewall/how-to/create-rate-limiting-policies/index.md"><meta property="og:title" content="Create Rate Limiting policies (beta) · Cloudflare Network Firewall docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create rate limiting policies for network traffic."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-network-firewall/how-to/create-rate-limiting-policies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Network Firewall"><meta name="algolia_product_filter" content="Cloudflare Network Firewall"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Network Firewall"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-network-firewall/how-to/create-rate-limiting-policies/#page","headline":"Create Rate Limiting policies (beta) \u00b7 Cloudflare Network Firewall docs","description":"Create rate limiting policies for network traffic.","url":"https://developers.cloudflare.com/cloudflare-network-firewall/how-to/create-rate-limiting-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-network-firewall/how-to/create-rate-limiting-policies/
  schema: 1
---
<p>Rate limiting policies (beta) allow you to manage incoming traffic to your network for specific locations.</p>
<p>This guide will teach you how to create a policy for when incoming packets match, and in cases where your rate exceeds a certain value (in packets or bits).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4272.md")
</aside>
<h2 id="add-a-policy">Add a policy</h2>
<p>To add a policy:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <a href="https://dash.cloudflare.com/?to=/:account/network-security/magic_firewall">Firewall Policies</a> page.</li>
<li>Select the <strong>Rate limiting</strong> tab, then select <strong>Add a policy</strong>.</li>
<li>Fill out the information for your new policy:
<ul>
<li>Select the <strong>Field</strong>: At the moment, you can only choose a <a href="https://developers.cloudflare.com/ruleset-engine/rules-language/fields/cloudflare-network-firewall/">colo name</a>.</li>
<li>Select the <strong>Operator</strong>: Choose among <strong>equals</strong> or <strong>is in</strong>.</li>
<li>Select the <strong>Value</strong>.</li>
</ul>
</li>
<li>When you are done, select <strong>Save policy</strong>.</li>
</ol>
<h2 id="edit-an-existing-policy">Edit an existing policy</h2>
<p>To edit a policy:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <a href="https://dash.cloudflare.com/?to=/:account/network-security/magic_firewall">Firewall Policies</a> page.</li>
<li>Select the <strong>Rate limiting</strong> tab.</li>
<li>Locate the policy you want to edit in the list and select <strong>Edit</strong>.</li>
<li>Edit the policy with your changes and select <strong>Edit policy</strong>.</li>
</ol>
<h2 id="delete-an-existing-policy">Delete an existing policy</h2>
<p>To delete an existing policy:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <a href="https://dash.cloudflare.com/?to=/:account/network-security/magic_firewall">Firewall Policies</a> page.</li>
<li>Select the <strong>Rate limiting</strong> tab.</li>
<li>Locate the policy you want to delete from the list.</li>
<li>Select the three dots, then select <strong>Remove</strong>.</li>
</ol>
