---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/
  description: Route AI Gateway requests based on conditions, quotas, and fallbacks using a visual interface or JSON configuration.
  full_title: Dynamic routing · Cloudflare AI Gateway docs
  head_html: <title>Dynamic routing · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route AI Gateway requests based on conditions, quotas, and fallbacks using a visual interface or JSON configuration."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/index.md"><meta property="og:title" content="Dynamic routing · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route AI Gateway requests based on conditions, quotas, and fallbacks using a visual interface or JSON configuration."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/#page","headline":"Dynamic routing \u00b7 Cloudflare AI Gateway docs","description":"Route AI Gateway requests based on conditions, quotas, and fallbacks using a visual interface or JSON configuration.","url":"https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/features/dynamic-routing/
  schema: 1
---
<h2 id="introduction">Introduction</h2>
<p>Dynamic routing enables you to create request routing flows through a <strong>visual interface</strong> or a <strong>JSON-based configuration</strong>. Instead of hard-coding a single model, with Dynamic Routing you compose a small flow that evaluates conditions, enforces quotas, and chooses models with fallbacks. You can iterate without touching application code—publish a new route version and you’re done. With dynamic routing, you can easily implement advanced use cases such as:</p>
<ul>
<li>Directing different segments (paid/not-paid user) to different models</li>
<li>Restricting each user/project/team with budget/rate limits</li>
<li>A/B and gradual rollouts</li>
</ul>
<p>while making it accessible to both developers and non-technical team members.</p>
<p><img src="/assets/upstream/images/ai-gateway/dynamic-routing.png" alt="Dynamic Routing Overview" /></p>
<h2 id="core-concepts">Core Concepts</h2>
<ul>
<li><strong>Route</strong>: A named, versioned flow (for example, dynamic/support) that you can use as instead of the model name in your requests.</li>
<li><strong>Nodes</strong>
<ul>
<li><strong>Start</strong>: Entry point for the route.</li>
<li><strong>Conditional</strong>: If/Else branch based on expressions that reference request body, headers, or metadata (for example, user_plan == &quot;paid&quot;).</li>
<li><strong>Percentage</strong>: Routes requests probabilistically across multiple outputs, useful for A/B testing and gradual rollouts.</li>
<li><strong>Model</strong>: Calls a provider/model with the request parameters</li>
<li><strong>Rate Limit</strong>: Enforces number of requests quotas (per your key, per period) and switches to fallback when exceeded.</li>
<li><strong>Budget Limit</strong>: Enforces cost quotas (per your key, per period) and switches to fallback when exceeded.</li>
<li><strong>End</strong>: Terminates the flow and returns the final model response.</li>
</ul>
</li>
<li><strong>Metadata</strong>: Arbitrary key-value context attached to the request (for example, userId, orgId, plan). You can pass this from your app so rules can reference it.</li>
<li><strong>Versions</strong>: Each change produces a new draft. Deploy to make it live with instant rollback.</li>
</ul>
<h2 id="getting-started">Getting Started</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2896.md")
</aside>
<ol>
<li>Create a route.
<ul>
<li>Go to <strong>(Select your gateway)</strong> &gt; <strong>Dynamic Routes</strong> &gt; <strong>Add Route</strong>, and name it (for example, <code>support</code>).</li>
<li>Open <strong>Editor</strong>.</li>
</ul>
</li>
<li>Define conditionals, limits and other settings.
<ul>
<li>You can use <a href="/ai-gateway/observability/custom-metadata/">Custom Metadata</a> in your conditionals.</li>
</ul>
</li>
<li>Configure model nodes.
<ul>
<li>Example:
<ul>
<li>Node A: Provider OpenAI, Model <code>o4-mini-high</code></li>
<li>Node B: Provider OpenAI, Model <code>gpt-4.1</code></li>
</ul>
</li>
</ul>
</li>
<li>Save a version.
<ul>
<li>Click <strong>Save</strong> to save the state. You can always roll back to earlier versions from <strong>Versions</strong>.</li>
<li>Deploy the version to make it live.</li>
</ul>
</li>
<li>Call the route from your code.
<ul>
<li>Use the <a href="/ai-gateway/usage/chat-completion/">OpenAI compatible</a> endpoint (<code>/compat/chat/completions</code>), and use the route name in place of the model, for example, <code>dynamic/support</code>. See <a href="/ai-gateway/features/dynamic-routing/usage/">Using a dynamic route</a> for examples.</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2895.md")
</aside>
