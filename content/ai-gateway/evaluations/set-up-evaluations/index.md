---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/evaluations/set-up-evaluations/
  description: Create datasets, select evaluators, and run evaluations for your AI Gateway logs.
  full_title: Set up Evaluations · Cloudflare AI Gateway docs
  head_html: <title>Set up Evaluations · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Create datasets, select evaluators, and run evaluations for your AI Gateway logs."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/evaluations/set-up-evaluations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/evaluations/set-up-evaluations/index.md"><meta property="og:title" content="Set up Evaluations · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create datasets, select evaluators, and run evaluations for your AI Gateway logs."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/evaluations/set-up-evaluations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/evaluations/set-up-evaluations/#page","headline":"Set up Evaluations \u00b7 Cloudflare AI Gateway docs","description":"Create datasets, select evaluators, and run evaluations for your AI Gateway logs.","url":"https://developers.cloudflare.com/ai-gateway/evaluations/set-up-evaluations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/evaluations/set-up-evaluations/
  schema: 1
---
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2847.md")
</aside>
<p>This guide walks you through the process of setting up an evaluation in AI Gateway. These steps are done in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</p>
<h2 id="1-select-or-create-a-dataset"><ol>
<li>Select or create a dataset</li>
</ol></h2>
<p>Datasets are collections of logs stored for analysis that can be used in an evaluation. You can create datasets by applying filters in the Logs tab. Datasets will update automatically based on the set filters.</p>
<h3 id="set-up-a-dataset-from-the-logs-tab">Set up a dataset from the Logs tab</h3>
<ol>
<li>Apply filters to narrow down your logs. Filter options include provider, number of tokens, request status, and more.</li>
<li>Select <strong>Create Dataset</strong> to store the filtered logs for future analysis.</li>
</ol>
<p>You can manage datasets by selecting <strong>Manage datasets</strong> from the Logs tab.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/2846.md")
</aside>
<h3 id="list-of-available-filters">List of available filters</h3>
<table>
<thead>
<tr>
<th>Filter category</th>
<th>Filter options</th>
<th>Filter by description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Status</td>
<td>error, status</td>
<td>error type or status.</td>
</tr>
<tr>
<td>Cache</td>
<td>cached, not cached</td>
<td>based on whether they were cached or not.</td>
</tr>
<tr>
<td>Provider</td>
<td>specific providers</td>
<td>the selected AI provider.</td>
</tr>
<tr>
<td>AI Models</td>
<td>specific models</td>
<td>the selected AI model.</td>
</tr>
<tr>
<td>Cost</td>
<td>less than, greater than</td>
<td>cost, specifying a threshold.</td>
</tr>
<tr>
<td>Request type</td>
<td>Workers AI Binding, WebSockets</td>
<td>the type of request.</td>
</tr>
<tr>
<td>Tokens</td>
<td>Total tokens, Tokens In, Tokens Out</td>
<td>token count (less than or greater than).</td>
</tr>
<tr>
<td>Duration</td>
<td>less than, greater than</td>
<td>request duration.</td>
</tr>
<tr>
<td>Feedback</td>
<td>equals, does not equal (thumbs up, thumbs down, no feedback)</td>
<td>feedback type.</td>
</tr>
<tr>
<td>Metadata Key</td>
<td>equals, does not equal</td>
<td>specific metadata keys.</td>
</tr>
<tr>
<td>Metadata Value</td>
<td>equals, does not equal</td>
<td>specific metadata values.</td>
</tr>
<tr>
<td>Log ID</td>
<td>equals, does not equal</td>
<td>a specific Log ID.</td>
</tr>
<tr>
<td>Event ID</td>
<td>equals, does not equal</td>
<td>a specific Event ID.</td>
</tr>
</tbody>
</table>
<h2 id="2-select-evaluators"><ol start="2">
<li>Select evaluators</li>
</ol></h2>
<p>After creating a dataset, choose the evaluation parameters:</p>
<ul>
<li>Cost: Calculates the average cost of inference requests within the dataset (only for requests with <a href="/ai-gateway/observability/costs/">cost data</a>).</li>
<li>Speed: Calculates the average duration of inference requests within the dataset.</li>
<li>Performance:
<ul>
<li>Human feedback: measures performance based on human feedback, calculated by the % of thumbs up on the logs, annotated from the Logs tab.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-1">Note</h3>
@markup("md", "content/.markup/bodies/2845.md")
</aside>
<h2 id="3-name-review-and-run-the-evaluation"><ol start="3">
<li>Name, review, and run the evaluation</li>
</ol></h2>
<ol>
<li>Create a unique name for your evaluation to reference it in the dashboard.</li>
<li>Review the selected dataset and evaluators.</li>
<li>Select <strong>Run</strong> to start the process.</li>
</ol>
<h2 id="4-review-and-analyze-results"><ol start="4">
<li>Review and analyze results</li>
</ol></h2>
<p>Evaluation results will appear in the Evaluations tab. The results show the status of the evaluation (for example, in progress, completed, or error). Metrics for the selected evaluators will be displayed, excluding any logs with missing fields. You will also see the number of logs used to calculate each metric.</p>
<p>While datasets automatically update based on filters, evaluations do not. You will have to create a new evaluation if you want to evaluate new logs.</p>
<p>Use these insights to optimize based on your application's priorities. Based on the results, you may choose to:</p>
<ul>
<li>Change the model or <a href="/ai-gateway/usage/providers/">provider</a></li>
<li>Adjust your prompts</li>
<li>Explore further optimizations, such as setting up <a href="/reference-architecture/diagrams/ai/ai-rag/">Retrieval Augmented Generation (RAG)</a></li>
</ul>
