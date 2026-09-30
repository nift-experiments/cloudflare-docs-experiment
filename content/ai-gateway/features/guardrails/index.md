---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/features/guardrails/
  description: Evaluate AI Gateway prompts and responses for harmful content and enforce safety policies across providers.
  full_title: Guardrails · Cloudflare AI Gateway docs
  head_html: <title>Guardrails · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Evaluate AI Gateway prompts and responses for harmful content and enforce safety policies across providers."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/features/guardrails/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/features/guardrails/index.md"><meta property="og:title" content="Guardrails · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Evaluate AI Gateway prompts and responses for harmful content and enforce safety policies across providers."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/features/guardrails/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="AI Gateway"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/ai-gateway/features/guardrails/#page","headline":"Guardrails \u00b7 Cloudflare AI Gateway docs","description":"Evaluate AI Gateway prompts and responses for harmful content and enforce safety policies across providers.","url":"https://developers.cloudflare.com/ai-gateway/features/guardrails/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/features/guardrails/
  schema: 1
---
<p>Guardrails help you deploy AI applications safely by intercepting and evaluating both user prompts and model responses for harmful content. Acting as a proxy between your application and <a href="/ai-gateway/usage/providers/">model providers</a> (such as OpenAI, Anthropic, DeepSeek, and others), AI Gateway's Guardrails ensure a consistent and secure experience across your entire AI ecosystem.</p>
<p>Guardrails proactively monitor interactions between users and AI models, giving you:</p>
<ul>
<li><strong>Consistent moderation</strong>: Uniform moderation layer that works across models and providers.</li>
<li><strong>Enhanced safety and user trust</strong>: Proactively protect users from harmful or inappropriate interactions.</li>
<li><strong>Flexibility and control over allowed content</strong>: Specify which categories to monitor and choose between flagging or outright blocking.</li>
<li><strong>Auditing and compliance capabilities</strong>: Receive updates on evolving regulatory requirements with logs of user prompts, model responses, and enforced guardrails.</li>
</ul>
<h2 id="video-demo">Video demo</h2>
<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/Its1H0jTxrQ" title="YouTube video" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h2 id="how-guardrails-work">How Guardrails work</h2>
<p>AI Gateway inspects all interactions in real time by evaluating content against predefined safety parameters. Guardrails work by:</p>
<ol>
<li>
<p>Intercepting interactions:
AI Gateway proxies requests and responses, sitting between the user and the AI model.</p>
</li>
<li>
<p>Inspecting content:</p>
<ul>
<li>User prompts: AI Gateway checks prompts against safety parameters (for example, violence, hate, or sexual content). Based on your settings, prompts can be flagged or blocked before reaching the model.</li>
<li>Model responses: Once processed, the AI model response is inspected. If hazardous content is detected, it can be flagged or blocked before being delivered to the user.</li>
</ul>
</li>
<li>
<p>Applying actions:
Depending on your configuration, flagged content is logged for review, while blocked content is prevented from proceeding.</p>
</li>
</ol>
<h2 id="related-resource">Related resource</h2>
<ul>
<li><a href="https://blog.cloudflare.com/guardrails-in-ai-gateway/">Cloudflare Blog: Keep AI interactions secure and risk-free with Guardrails in AI Gateway</a></li>
</ul>
