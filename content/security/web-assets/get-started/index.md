---
cp9:
  canonical: https://developers.cloudflare.com/security/web-assets/get-started/
  description: Use Web Assets to review operations, labels, matched traffic, learned schemas, and risks.
  full_title: Get started · Security dashboard docs
  head_html: <title>Get started · Security dashboard docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Web Assets to review operations, labels, matched traffic, learned schemas, and risks."><link rel="canonical" href="https://developers.cloudflare.com/security/web-assets/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/security/web-assets/get-started/index.md"><meta property="og:title" content="Get started · Security dashboard docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Web Assets to review operations, labels, matched traffic, learned schemas, and risks."><meta property="og:url" content="https://developers.cloudflare.com/security/web-assets/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Security dashboard"><meta name="algolia_product_filter" content="Security dashboard"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Security dashboard"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/security/web-assets/get-started/#page","headline":"Get started \u00b7 Security dashboard docs","description":"Use Web Assets to review operations, labels, matched traffic, learned schemas, and risks.","url":"https://developers.cloudflare.com/security/web-assets/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /security/web-assets/get-started/
  schema: 1
---
<p>You do not need to complete a fixed setup flow before discovered operations can be used for protection. Use this page to choose the capability that matches your task.</p>
<h2 id="review-operations">Review operations</h2>
<p>Review operations to understand the parts of your application that receive traffic, such as login, sign-up, checkout, upload, and AI-powered flows.</p>
<p>Discovered operations can be used for matching and downstream security detections before you manually refine them. For more information, refer to <a href="/security/web-assets/manage-operations/">Manage operations</a>.</p>
<h2 id="add-or-refine-operations">Add or refine operations</h2>
<p>Add an operation when traffic you want to protect does not appear, or when you want to define the operation structure yourself.</p>
<p>Manual creation and editing only update operation inventory. Refine an operation when its method, hostname pattern, or path pattern does not match your intended grouping.</p>
<p>For more information, refer to <a href="/security/web-assets/manage-operations/">Manage operations</a>.</p>
<h2 id="review-labeled-operations">Review labeled operations</h2>
<p>Labels describe what an operation does. Detections can use labels to focus on traffic for a specific use case.</p>
<p>Refine labels when the current label set does not describe the operation correctly. For example, add <code>cf-llm</code> to operations that receive Large Language Model (LLM) prompts so <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a> can scan incoming prompts for threats such as prompt injection.</p>
<p>For more information, refer to <a href="/security/web-assets/label-operations/">Label operations</a>.</p>
<h2 id="review-traffic-matched-to-operations">Review traffic matched to operations</h2>
<p>Use <a href="/waf/analytics/security-analytics/">Security Analytics</a> to review traffic matched to individual operations or labels.</p>
<div class="nb-dash-button"></div>
<p>For individual operations, use the operation ID or operation details to review matched traffic and logs. For labeled traffic, filter by managed labels such as <code>cf-llm</code> or <code>cf-log-in</code>.</p>
<p>Certain metrics, such as latency, may not populate when a request is handled by <a href="/workers/">Cloudflare Workers</a> or a product built on Workers, such as <a href="/waiting-room/">Waiting Room</a>. You can also export operation and label fields through Logpush or query them through the GraphQL Analytics API. For more information, refer to <a href="/security/web-assets/label-operations/#use-labels-in-analytics-and-logs/">Use labels in analytics and logs</a>.</p>
<h2 id="use-learned-schemas">Use learned schemas</h2>
<p>Discovered operations do not automatically start profile learning. To learn a Schema Profile, select <strong>Learn profile</strong> from the operation overflow menu.</p>
<p>After the profile becomes available, select <strong>View details</strong>. Review the learned schema under <strong>Security overview</strong>.</p>
<p>If you already maintain OpenAPI schemas, you can upload them to create operations and use them with API Shield <a href="/api-shield/security/schema-validation/">Schema Validation</a>.</p>
<p>For the complete workflow, refer to <a href="/waf/detections/application-profiles/">Application Profiles</a> and <a href="/api-shield/management-and-monitoring/endpoint-management/schema-learning/">Schema learning</a>.</p>
<h2 id="define-security-protections">Define security protections</h2>
<p>After traffic is matched to the relevant operation, define relevant security rules to act on that traffic.</p>
<p>For example, AI Security for Apps scans requests to operations labeled with <code>cf-llm</code>. You can then create rules that log or block requests with unsafe LLM prompt signals.</p>
<p>For more information, refer to <a href="/security/web-assets/define-security-protections/">Define security protections</a>.</p>
<h2 id="review-risks">Review risks</h2>
<p>Web Assets can show risks on operations that may need attention. A corresponding <a href="/security-center/">Security Center</a> Insight may also be raised.</p>
<p>For the current risk reference, refer to <a href="/api-shield/management-and-monitoring/endpoint-labels/#risk-labels">API endpoint risks</a>.</p>
