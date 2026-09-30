---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/
  description: Build secure, isolated code execution environments powered by Cloudflare Workers and Containers.
  full_title: Overview · Cloudflare Sandbox SDK docs
  head_html: <title>Overview · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Build secure, isolated code execution environments powered by Cloudflare Workers and Containers."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/index.md"><meta property="og:title" content="Overview · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build secure, isolated code execution environments powered by Cloudflare Workers and Containers."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Sandbox SDK,Workers,Containers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/sandbox/#page","headline":"Overview \u00b7 Cloudflare Sandbox SDK docs","description":"Build secure, isolated code execution environments powered by Cloudflare Workers and Containers.","url":"https://developers.cloudflare.com/sandbox/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/384.md")
</div>
<div class="nb-plan">
<p>Available on Workers Paid plan</p>
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="sandbox-sdk-1-0-preview">Sandbox SDK 1.0 preview</h3>
@markup("md", "content/.markup/bodies/383.md")
</aside>
<p>The Sandbox SDK enables you to run untrusted code securely in isolated environments. Built on <a href="/containers/">Containers</a>, Sandbox SDK provides a simple API for executing commands, managing files, running background processes, and exposing services — all from your <a href="/workers/">Workers</a> applications.</p>
<p>Sandboxes are ideal for building AI agents that need to execute code, interactive development environments, data analysis platforms, CI/CD systems, and any application that needs secure code execution at the edge. Each sandbox runs in its own isolated container with a full Linux environment, providing strong security boundaries while maintaining performance.</p>
<p>With Sandbox, you can execute Python scripts, run Node.js applications, analyze data, compile code, and perform complex computations — all with a simple TypeScript API and no infrastructure to manage.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/391.md")
</div></div>
<p><a class="nb-link-button" href="/sandbox/get-started/">Get started</a>
<a class="nb-link-button" href="/sandbox/api/">API Reference</a></p>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/394.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/395.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/396.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/397.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/398.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/399.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/400.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/401.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/402.md")
</div>
<hr />
<h2 id="use-cases">Use Cases</h2>
<p>Build powerful applications with Sandbox:</p>
<h3 id="ai-code-execution">AI Code Execution</h3>
<p>Execute code generated by Large Language Models safely and reliably. Native integration with <a href="/workers-ai/">Workers AI</a> models like GPT-OSS enables function calling with sandbox execution. Perfect for AI agents, code assistants, and autonomous systems that need to run untrusted code.</p>
<h3 id="data-analysis-notebooks">Data Analysis &amp; Notebooks</h3>
<p>Create interactive data analysis environments with pandas, NumPy, and Matplotlib. Generate charts, tables, and visualizations with automatic rich output formatting.</p>
<h3 id="interactive-development-environments">Interactive Development Environments</h3>
<p>Build cloud IDEs, coding playgrounds, and collaborative development tools with full Linux environments and preview URLs.</p>
<h3 id="ci-cd-build-systems">CI/CD &amp; Build Systems</h3>
<p>Run tests, compile code, and execute build pipelines in isolated environments with parallel execution and streaming logs.</p>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/403.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/404.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/405.md")
</div>
<hr />
<h2 id="more-resources">More resources</h2>
<h2 id="coding-agents">Coding agents</h2>
<p>Install <a href="https://github.com/cloudflare/skills">Cloudflare Skills</a> for your agent (<a href="/agent-setup/">Agent setup</a>). Use <strong><code>sandbox-stable</code></strong> with the main docs on this site while you are on the current stable package. Use <strong><code>sandbox-next</code></strong> for <code>@cloudflare/sandbox@next</code> (recommended for new projects). When you are ready to port an existing app, use <strong><code>sandbox-migrate-to-next</code></strong>.</p>
<div class="nb-card-grid">
@input("content/.markup/bodies/417.md")
</div>
