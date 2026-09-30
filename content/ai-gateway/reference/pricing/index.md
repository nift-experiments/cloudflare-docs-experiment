---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/reference/pricing/
  description: Review AI Gateway pricing, including free core features, persistent log storage limits, and premium add-ons.
  full_title: Pricing · Cloudflare AI Gateway docs
  head_html: <title>Pricing · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Review AI Gateway pricing, including free core features, persistent log storage limits, and premium add-ons."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/reference/pricing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/reference/pricing/index.md"><meta property="og:title" content="Pricing · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review AI Gateway pricing, including free core features, persistent log storage limits, and premium add-ons."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/reference/pricing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/reference/pricing/#page","headline":"Pricing \u00b7 Cloudflare AI Gateway docs","description":"Review AI Gateway pricing, including free core features, persistent log storage limits, and premium add-ons.","url":"https://developers.cloudflare.com/ai-gateway/reference/pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/reference/pricing/
  schema: 1
---
<p>AI Gateway is available to use on all plans.</p>
<p>AI Gateway's core features available today are offered for free, and all it takes is a Cloudflare account and one line of code to <a href="/ai-gateway/get-started/">get started</a>. Core features include: dashboard analytics, caching, and rate limiting.</p>
<p>We will continue to build and expand AI Gateway. Some new features may be additional core features that will be free while others may be part of a premium plan. We will announce these as they become available.</p>
<p>You can monitor your usage in the AI Gateway dashboard.</p>
<h2 id="persistent-logs">Persistent logs</h2>
<p>Persistent logs are available on all plans. Log storage limits vary by plan.</p>
<h3 id="log-storage-limits">Log storage limits</h3>
<table>
<thead>
<tr>
<th>Plan</th>
<th>Log storage limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Workers Free</td>
<td>100,000 logs total across all gateways</td>
</tr>
<tr>
<td>Workers Paid</td>
<td>10,000,000 logs per gateway</td>
</tr>
</tbody>
</table>
<p>For more details on log storage behavior and automatic log deletion, refer to <a href="/ai-gateway/reference/limits/">Limits</a> and <a href="/ai-gateway/observability/logging/#automatic-log-deletion">Logging</a>.</p>
<h2 id="data-loss-prevention-dlp">Data Loss Prevention (DLP)</h2>
<p>DLP scanning in AI Gateway is free on all plans. Accounts without a Zero Trust subscription have access to two predefined <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profiles</a>: Financial Information and Social / Insurance / National Identifier Numbers.</p>
<p>DLP profiles are shared at the account level with <a href="/cloudflare-one/data-loss-prevention/">Cloudflare One</a>. If your account has a Zero Trust subscription that includes DLP, the full set of profiles — including all predefined profiles, custom profiles, integration profiles, DLP datasets, and OCR — is automatically available in AI Gateway.</p>
<h2 id="guardrails">Guardrails</h2>
<p><a href="/ai-gateway/features/guardrails/">Guardrails</a> evaluates prompts and responses using <a href="/workers-ai/models/llama-guard-3-8b/"><code>@cf/meta/llama-guard-3-8b</code></a> on Workers AI. Usage is billed as <a href="/workers-ai/platform/pricing/">Workers AI</a> token-based inference — cost scales with the length of the prompts and responses being evaluated.</p>
<h2 id="unified-billing">Unified Billing</h2>
<p>A 5% fee is applied to all credits purchased through <a href="/ai-gateway/features/unified-billing/">Unified Billing</a>. For example, a $100 credit purchase will result in a $105 charge. Inference pricing from providers is passed through with no markup — you pay the same per-token rates as you would directly with the provider.</p>
<h2 id="logpush">Logpush</h2>
<p>Logpush is only available on the Workers Paid plan.</p>
<table>
<thead>
<tr>
<th></th>
<th>Paid plan</th>
</tr>
</thead>
<tbody>
<tr>
<td>Requests</td>
<td>10 million / month, +$0.05/million</td>
</tr>
</tbody>
</table>
<h2 id="pricing-notes">Pricing notes</h2>
<p>Prices subject to change. If you are an Enterprise customer, reach out to your account team to confirm pricing details.</p>
