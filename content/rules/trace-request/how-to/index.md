---
cp9:
  canonical: https://developers.cloudflare.com/rules/trace-request/how-to/
  description: Learn how to use Cloudflare Trace in the dashboard and with the API.
  full_title: How to - Cloudflare Trace · Cloudflare Rules docs
  head_html: <title>How to - Cloudflare Trace · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to use Cloudflare Trace in the dashboard and with the API."><link rel="canonical" href="https://developers.cloudflare.com/rules/trace-request/how-to/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/trace-request/how-to/index.md"><meta property="og:title" content="How to - Cloudflare Trace · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to use Cloudflare Trace in the dashboard and with the API."><meta property="og:url" content="https://developers.cloudflare.com/rules/trace-request/how-to/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/trace-request/how-to/#page","headline":"How to - Cloudflare Trace \u00b7 Cloudflare Rules docs","description":"Learn how to use Cloudflare Trace in the dashboard and with the API.","url":"https://developers.cloudflare.com/rules/trace-request/how-to/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/trace-request/how-to/
  schema: 1
---
<h2 id="use-trace-in-the-dashboard">Use Trace in the dashboard</h2>
<h3 id="1-configure-one-or-more-cloudflare-products"><ol>
<li>Configure one or more Cloudflare products</li>
</ol></h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/12774.md")
</div>
<h3 id="2-build-a-trace"><ol start="2">
<li>Build a trace</li>
</ol></h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/12775.md")
</div>
<h3 id="3-assess-results"><ol start="3">
<li>Assess results</li>
</ol></h3>
<p>The <strong>Trace results</strong> page shows all evaluated and executed configurations from different Cloudflare products, in evaluation order. Any inactive rules are not evaluated.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/12776.md")
</div>
<h3 id="4-optional-save-the-trace-configuration"><ol start="4">
<li>(Optional) Save the trace configuration</li>
</ol></h3>
<p>To run a trace later with the same configuration:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/12777.md")
</div>
<h2 id="use-trace-via-api">Use Trace via API</h2>
<p>Use the <a href="/api/resources/request_tracers/subresources/traces/methods/create/">Request Trace</a> operation to perform a trace using the Cloudflare API.</p>
<hr />
<h2 id="steps-in-trace-results">Steps in trace results</h2>
<ul>
<li>Execution of one or more rules of Cloudflare products built on the <a href="/ruleset-engine/">Ruleset Engine</a>. Refer to the Ruleset Engine's <a href="/ruleset-engine/reference/phases-list/">Phases list</a> for a list of such products.</li>
<li><a href="/rules/page-rules/">Page Rules</a>: Execution of one or more rules.</li>
<li><a href="/workers/">Workers</a>: Execution of one or more scripts.</li>
</ul>
