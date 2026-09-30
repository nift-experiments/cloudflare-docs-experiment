---
cp9:
  canonical: https://developers.cloudflare.com/security/web-assets/define-security-protections/
  description: Use Web Assets operations and labels with Cloudflare detections, then create rules to act on risky traffic.
  full_title: Define security protections · Security dashboard docs
  head_html: <title>Define security protections · Security dashboard docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Web Assets operations and labels with Cloudflare detections, then create rules to act on risky traffic."><link rel="canonical" href="https://developers.cloudflare.com/security/web-assets/define-security-protections/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/security/web-assets/define-security-protections/index.md"><meta property="og:title" content="Define security protections · Security dashboard docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Web Assets operations and labels with Cloudflare detections, then create rules to act on risky traffic."><meta property="og:url" content="https://developers.cloudflare.com/security/web-assets/define-security-protections/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Security dashboard"><meta name="algolia_product_filter" content="Security dashboard"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Security dashboard"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/security/web-assets/define-security-protections/#page","headline":"Define security protections \u00b7 Security dashboard docs","description":"Use Web Assets operations and labels with Cloudflare detections, then create rules to act on risky traffic.","url":"https://developers.cloudflare.com/security/web-assets/define-security-protections/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /security/web-assets/define-security-protections/
  schema: 1
---
<p>Web Assets provides application context to security detections. This helps detections inspect the right traffic and lets you create rules focusing on targeted protections.</p>
<p>Use this guide to connect a Web Assets operation to a security detection and create a rule that logs, challenges, blocks, or rate limits risky traffic.</p>
<h2 id="protection-workflow">Protection workflow</h2>
<p>Most protections that use Web Assets follow the same workflow:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13840.md")
</div>
<h2 id="example-protect-ai-powered-operations">Example: Protect AI-powered operations</h2>
<p><a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a> runs targeted scans on requests to AI-powered operations. Use it to detect prompt injection, personally identifiable information (PII) in prompts, unsafe topics, and other Large Language Model (LLM)-specific signals.</p>
<p>To define protection for an LLM-powered operation:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13841.md")
</div>
<p>For the full setup workflow, refer to <a href="/waf/detections/ai-security-for-apps/get-started/">Get started with AI Security for Apps</a>.</p>
<h2 id="validate-detection-behavior">Validate detection behavior</h2>
<p>Use Security Analytics to confirm that the expected requests carry the right operation and label context before you create a blocking rule.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13842.md")
</div>
<p>You can also export operation and label data with Logpush or query it with the GraphQL Analytics API. For more information, refer to <a href="/security/web-assets/label-operations/#use-labels-in-analytics-and-logs/">Use labels in analytics and logs</a>.</p>
<h2 id="mitigate-matched-traffic">Mitigate matched traffic</h2>
<p>After you validate detection behavior, create rules that act on relevant detection fields.</p>
<p>For example, a rule can match requests addressed to an operation labeled <code>cf-llm</code> that also carry personally identifiable information in an LLM prompt.</p>
<p>You can use <a href="/waf/custom-rules/create-dashboard/">custom rules</a> to log, challenge, block, or skip traffic. You can use <a href="/waf/rate-limiting-rules/">rate limiting rules</a> to limit high-volume activity.</p>
