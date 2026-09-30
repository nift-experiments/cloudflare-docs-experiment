---
cp9:
  canonical: https://developers.cloudflare.com/security/web-assets/
  description: Discover operations in applications proxied through Cloudflare and use that context to protect important traffic.
  full_title: Web Assets · Security dashboard docs
  head_html: <title>Web Assets · Security dashboard docs</title><meta name="generator" content="Nift"><meta name="description" content="Discover operations in applications proxied through Cloudflare and use that context to protect important traffic."><link rel="canonical" href="https://developers.cloudflare.com/security/web-assets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/security/web-assets/index.md"><meta property="og:title" content="Web Assets · Security dashboard docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Discover operations in applications proxied through Cloudflare and use that context to protect important traffic."><meta property="og:url" content="https://developers.cloudflare.com/security/web-assets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Security dashboard"><meta name="algolia_product_filter" content="Security dashboard"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Security dashboard"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/security/web-assets/#page","headline":"Web Assets \u00b7 Security dashboard docs","description":"Discover operations in applications proxied through Cloudflare and use that context to protect important traffic.","url":"https://developers.cloudflare.com/security/web-assets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /security/web-assets/
  schema: 1
---
<p>Web Assets automatically discovers operations in web applications proxied through Cloudflare. Operation context helps you define security protections against application-specific functionalities.</p>
<p>For example, discovering operations that receive LLM prompts so <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a> can help you define targeted protections such as deterring prompt injections.</p>
<p>To access Web Assets in the Cloudflare dashboard, go to the <strong>Web Assets</strong> page.</p>
<div class="nb-dash-button"></div>
<h2 id="definition-of-an-operation">Definition of an operation</h2>
<p>An operation is a group of HTTP requests that serve the same purpose in your application. Each operation is defined by:</p>
<ul>
<li>HTTP method</li>
<li>Hostname pattern</li>
<li>Path pattern</li>
</ul>
<p>For example, Web Assets can group requests to product detail pages into one operation:</p>
<pre tabindex="0"><code class="language-txt">GET example.com/products/{var1}&#10;</code></pre>
<p>The operation can match requests such as:</p>
<pre tabindex="0"><code class="language-txt">GET https://example.com/products/shoes&#10;GET https://example.com/products/hats&#10;GET https://example.com/products/jackets&#10;</code></pre>
<p>This lets Cloudflare identify requests that serve the same purpose in your application.</p>
<h2 id="how-cloudflare-identifies-operations">How Cloudflare identifies operations</h2>
<p>Operations can come from several sources:</p>
<ul>
<li><strong>Discovery</strong>: Web Assets continuously reviews proxied HTTP traffic and groups similar requests into operations using machine learning (for <a href="/api-shield/security/api-discovery/">API discovery</a>) and heuristics.</li>
<li><strong>Manual entry</strong>: You can add operations by method, hostname pattern, and path pattern.</li>
<li><strong>Schema upload</strong>: You can <a href="/api-shield/management-and-monitoring/endpoint-management/#add-endpoints-from-schema-validation">upload an OpenAPI schema</a> to create operations from an existing API definition.</li>
</ul>
<p>These sources contribute to the same operation inventory. You do not need to review every discovered operation before security detections can use operation context.</p>
<h2 id="operation-states-and-profile-learning">Operation states and profile learning</h2>
<p>Operations can be in the <code>candidate</code>, <code>shadow</code>, or <code>full</code> state. These states control operation matching and available features.</p>
<p>An operation state alone does not start profile learning. To learn a Schema Profile, select <strong>Learn profile</strong> from the operation overflow menu.</p>
<p>For the profile lifecycle, refer to <a href="/waf/detections/application-profiles/">Application Profiles</a>. For uploaded OpenAPI schemas, refer to <a href="/api-shield/security/schema-validation/">Schema Validation</a>.</p>
<h2 id="describe-operations-context">Describe operations context</h2>
<p><a href="/security/web-assets/label-operations/">Labels</a> describe what an operation does, such as a login flow, sign-up flow, AI-powered operation, or another use case.</p>
<p>Cloudflare defines managed labels. Some managed labels can be discovered automatically, but not every managed label is currently auto-discovered.</p>
<p>Custom labels let you organize operations for your own workflows. They do not replace managed labels for Cloudflare security detections.</p>
<h2 id="define-security-protections">Define security protections</h2>
<p>Security detections can use Web Assets to focus on the operations where their signals matter. For example, <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a> uses the <code>cf-llm</code> managed label to scan requests to AI-powered operations. For more information, refer to <a href="/security/web-assets/define-security-protections/">Define security protections</a>.</p>
<div class="nb-card"><h3 class="nb-component-title" id="related-api-shield-features">Related API Shield features</h3>
@markup("md", "content/.markup/bodies/13839.md")
</div>
