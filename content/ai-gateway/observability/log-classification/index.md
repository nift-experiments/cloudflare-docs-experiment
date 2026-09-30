---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/observability/log-classification/
  description: Classify AI Gateway traffic by task and assess whether each model matches the task requirements.
  full_title: Log classification · Cloudflare AI Gateway docs
  head_html: <title>Log classification · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Classify AI Gateway traffic by task and assess whether each model matches the task requirements."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/observability/log-classification/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/observability/log-classification/index.md"><meta property="og:title" content="Log classification · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Classify AI Gateway traffic by task and assess whether each model matches the task requirements."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/observability/log-classification/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/observability/log-classification/#page","headline":"Log classification \u00b7 Cloudflare AI Gateway docs","description":"Classify AI Gateway traffic by task and assess whether each model matches the task requirements.","url":"https://developers.cloudflare.com/ai-gateway/observability/log-classification/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/observability/log-classification/
  schema: 1
---
<p>Log classification analyzes the request and response content stored in AI Gateway logs. It classifies eligible traffic by task and assesses whether the model used matches the task requirements.</p>
<p>These results power <strong>Task and model analysis</strong> in <a href="/ai-gateway/observability/user-insights/">User Insights</a>. Log classification is turned off by default. You must turn it on for each gateway individually.</p>
<h2 id="classification-results">Classification results</h2>
<h3 id="tasks-by-model">Tasks by model</h3>
<p>AI Gateway assigns task classifications such as debugging, code planning, code Q&amp;A, text drafting, and coding. The <strong>Tasks by model</strong> chart shows how token usage and estimated spend are distributed across these classifications for each model.</p>
<h3 id="model-fit">Model fit</h3>
<p>AI Gateway compares the task requirements with the capabilities of the model used. It classifies model fit as <strong>Overkill</strong>, <strong>Appropriate</strong>, <strong>Underpowered</strong>, or <strong>Could not assess</strong>. You can compare these results by token usage or estimated spend.</p>
<h2 id="what-cloudflare-processes">What Cloudflare processes</h2>
<p>When log classification is turned on, Cloudflare may process stored request and response content, including:</p>
<ul>
<li>Prompts</li>
<li>Model responses</li>
<li>Request metadata</li>
<li>Identifiers used to associate related requests into a conversation</li>
</ul>
<p>Cloudflare uses this information to generate task and model-fit classifications for AI Gateway analysis features.</p>
<p>Log classification is not required to use AI Gateway or standard log collection. Turning on this setting allows Cloudflare to analyze eligible logs for the selected gateway as described on this page. This setting is gateway-specific: turning it on for one gateway does not turn it on for other gateways in your account.</p>
<h2 id="requirements-and-behavior">Requirements and behavior</h2>
<ul>
<li><strong>Collect logs</strong> must also be turned on for the gateway.</li>
<li>Only activity recorded while both <strong>Collect logs</strong> and <strong>Log classification</strong> are turned on is eligible for classification.</li>
<li>Turning off <strong>Collect logs</strong> also turns off log classification.</li>
<li>Turning off <strong>Log classification</strong> prevents new gateway activity from being classified. Work already in progress and previously generated results remain subject to applicable retention and deletion policies.</li>
</ul>
<h2 id="turn-on-log-classification">Turn on log classification</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2800.md")
</div>
<h2 id="turn-off-log-classification">Turn off log classification</h2>
<p>To stop classifying new activity, go to your gateway's <strong>Settings</strong> and turn off <strong>Log classification</strong>.</p>
<p>You can continue collecting logs without turning on classification.</p>
