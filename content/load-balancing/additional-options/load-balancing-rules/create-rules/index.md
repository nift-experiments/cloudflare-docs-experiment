---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/create-rules/
  description: Create custom rules for load balancing behavior.
  full_title: Create custom rules · Cloudflare Load Balancing docs
  head_html: <title>Create custom rules · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Create custom rules for load balancing behavior."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/create-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/create-rules/index.md"><meta property="og:title" content="Create custom rules · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create custom rules for load balancing behavior."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/create-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/create-rules/#page","headline":"Create custom rules \u00b7 Cloudflare Load Balancing docs","description":"Create custom rules for load balancing behavior.","url":"https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/create-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/additional-options/load-balancing-rules/create-rules/
  schema: 1
---
<p>Create and manage <a href="/load-balancing/additional-options/load-balancing-rules/">Load Balancing rules</a> in the <strong>Custom Rules</strong> page, which is part of the Create/Edit Load Balancer workflow found in <strong>Traffic</strong> in the dashboard.</p>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li><strong>Understand whether Cloudflare proxies your traffic</strong>: Depending on the <a href="/load-balancing/understand-basics/proxy-modes/">proxy status</a> of your traffic, you may have access to different fields for your load balancing rules. For more details, refer to <a href="/load-balancing/additional-options/load-balancing-rules/reference/">Supported fields and expressions</a>.</li>
</ul>
<hr />
<h2 id="example-workflow">Example Workflow</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Load Balancing</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Edit an existing load balancer or <a href="/load-balancing/load-balancers/create-load-balancer/">create a new load balancer</a>.</li>
<li>From the Load Balancer workflow, select <strong>Custom Rules</strong>.</li>
<li>Select <strong>Create Custom Rule</strong>.</li>
<li>In the <strong>Field</strong> drop-down list, choose an HTTP property. For more details, refer to <a href="/load-balancing/additional-options/load-balancing-rules/reference/">Supported fields</a>.</li>
<li>In the <strong>Operator</strong> drop-down list, choose an operator. For more details, refer to <a href="/load-balancing/additional-options/load-balancing-rules/reference/#operators-and-grouping-symbols">Operators</a>.</li>
<li>Enter the value to match. When the field is an ordered list, <strong>Value</strong> is a drop-down list. Otherwise, <strong>Value</strong> is a text input.</li>
<li>(Optional) To create a compound expression using logical operators, select <strong>And</strong> or <strong>Or</strong>.</li>
<li>For an action, choose <strong>Respond with fixed response</strong> or <strong>Override</strong> and enter additional details. For a full list of actions, refer to <a href="/load-balancing/additional-options/load-balancing-rules/actions/">Actions</a>.</li>
<li>(Optional) Select <strong>Add another override</strong>.</li>
<li>After you create your rule, select <strong>Save and Deploy</strong> or <strong>Save as Draft</strong>.</li>
<li>Select <strong>Next</strong> and review your changes.</li>
<li>Select <strong>Save</strong> to confirm.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/10439.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10438.md")
</aside>
<h2 id="example-use-case">Example use case</h2>
<h3 id="url-based-routing">URL-based routing</h3>
<p>If you want to host <code>example.com/blog</code> separately from your main website, for example, use the following custom rule.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/10440.md")
</div>
