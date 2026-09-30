---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/reference/cloudy-ai-agent/
  description: Cloudy is Cloudflare's AI agent that helps you understand and optimize your Cloudflare configurations across multiple products.
  full_title: Cloudy AI agent (beta) · Cloudflare Fundamentals docs
  head_html: <title>Cloudy AI agent (beta) · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudy is Cloudflare&#x27;s AI agent that helps you understand and optimize your Cloudflare configurations across multiple products."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/reference/cloudy-ai-agent/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/reference/cloudy-ai-agent/index.md"><meta property="og:title" content="Cloudy AI agent (beta) · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudy is Cloudflare&#x27;s AI agent that helps you understand and optimize your Cloudflare configurations across multiple products."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/reference/cloudy-ai-agent/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/reference/cloudy-ai-agent/#page","headline":"Cloudy AI agent (beta) \u00b7 Cloudflare Fundamentals docs","description":"Cloudy is Cloudflare's AI agent that helps you understand and optimize your Cloudflare configurations across multiple products.","url":"https://developers.cloudflare.com/fundamentals/reference/cloudy-ai-agent/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/reference/cloudy-ai-agent/
  schema: 1
---
<p>Cloudy is Cloudflare's first version of an AI agent, with assistant-like functionality designed to help users understand and improve their Cloudflare configurations in multiple areas of the product suite.</p>
<p>Cloudy is powered by <a href="/workers-ai/">Workers AI</a> and helps identify and solve issues such as identifying redundant rules, optimizing execution order, analyzing conflicting rules, and identifying disabled rules. Cloudy can also help investigate threat events and provide actionable recommendations.</p>
<h2 id="availability">Availability</h2>
<p>Cloudy, currently in beta, is available in several Cloudflare products such as WAF, Zero Trust, and Analytics. Throughout the rest of 2025, Cloudflare plans to roll out additional AI agent capabilities across other areas of Cloudflare.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="send-us-your-feedback">Send us your feedback</h3>
@markup("md", "content/.markup/bodies/8806.md")
</aside>
<h2 id="what-data-does-cloudy-have-access-to">What data does Cloudy have access to?</h2>
<p>Cloudy has access to your Cloudflare configuration. It combines this data with a purpose-built LLM prompt.</p>
<p>Additionally, Cloudy takes Role-Based Access Control (RBAC) restrictions into account: it can only access the same Cloudflare configuration settings as the currently logged in user, based on their <a href="/fundamentals/manage-members/roles/">roles and permissions</a>.</p>
<p>All your configuration information is only included in the purpose-built prompt — it is not used to train Cloudy or the LLM model(s) powering it.</p>
<h2 id="is-cloudy-trained-on-user-or-customer-data">Is Cloudy trained on user or customer data?</h2>
<p>No. Your Cloudflare configuration is used in the purpose-built prompt that enables Cloudy to turn raw configuration data into consistent, clear summaries and actionable recommendations.</p>
<p>Cloudy does not share your Cloudflare configuration with other customers. Your configuration is also not used for LLM model training.</p>
<p>Cloudy brings the same enterprise-grade security as the rest of Cloudflare's offerings. You can learn more about Cloudflare's approach to responsible AI in the <a href="https://www.cloudflare.com/trust-hub/responsible-ai/">Trust Hub</a>.</p>
<h2 id="can-i-opt-out-of-cloudy">Can I opt out of Cloudy?</h2>
<p>Currently, Cloudflare does not provide an opt out mechanism that completely disables all possible use of Cloudy. You can only opt out of the chat interface available in the Cloudflare dashboard.</p>
<p>However, Cloudy is an entirely optional tool that you can choose not to use. By not using Cloudy, you will not get summaries based on your current configuration or any actionable recommendations.</p>
<p>To opt out of the chat interface, do the following:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Configurations</strong>.</li>
<li>Turn off the <strong>Cloudy features</strong> setting.</li>
</ol>
<p>As noted above, Cloudy is not trained on user or customer data and does not share your Cloudflare setup with other customers.</p>
