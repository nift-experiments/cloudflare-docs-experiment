---
cp9:
  canonical: https://developers.cloudflare.com/kv/reference/environments/
  description: Bind different Workers KV namespaces to the same Worker across staging and production environments.
  full_title: Environments · Cloudflare Workers KV docs
  head_html: <title>Environments · Cloudflare Workers KV docs</title><meta name="generator" content="Nift"><meta name="description" content="Bind different Workers KV namespaces to the same Worker across staging and production environments."><link rel="canonical" href="https://developers.cloudflare.com/kv/reference/environments/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/kv/reference/environments/index.md"><meta property="og:title" content="Environments · Cloudflare Workers KV docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Bind different Workers KV namespaces to the same Worker across staging and production environments."><meta property="og:url" content="https://developers.cloudflare.com/kv/reference/environments/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="KV"><meta name="algolia_product_filter" content="KV"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="KV"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/kv/reference/environments/#page","headline":"Environments \u00b7 Cloudflare Workers KV docs","description":"Bind different Workers KV namespaces to the same Worker across staging and production environments.","url":"https://developers.cloudflare.com/kv/reference/environments/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /kv/reference/environments/
  schema: 1
---
<p>KV namespaces can be used with <a href="/workers/wrangler/environments/">environments</a>. This is useful when you have code in your Worker that refers to a KV binding like <code>MY_KV</code>, and you want to have these bindings point to different KV namespaces (for example, one for staging and one for production).</p>
<p>The following code in the Wrangler file shows you how to have two environments that have two different KV namespaces but the same binding name:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9493.md")
</div>
<p>Using the same binding name for two different KV namespaces keeps your Worker code more readable.</p>
<p>In the <code>staging</code> environment, <code>MY_KV.get(&quot;KEY&quot;)</code> will read from the namespace ID <code>e29b263ab50e42ce9b637fa8370175e8</code>. In the <code>production</code> environment, <code>MY_KV.get(&quot;KEY&quot;)</code> will read from the namespace ID <code>a825455ce00f4f7282403da85269f8ea</code>.</p>
<p>To insert a value into a <code>staging</code> KV namespace, run:</p>
<pre tabindex="0"><code class="language-sh">wrangler kv key put --env=staging --binding=&lt;YOUR_BINDING&gt; &quot;&lt;KEY&gt;&quot; &quot;&lt;VALUE&gt;&quot;&#10;</code></pre>
<p>Since <code>--namespace-id</code> is always unique (unlike binding names), you do not need to specify an <code>--env</code> argument:</p>
<pre tabindex="0"><code class="language-sh">wrangler kv key put --namespace-id=&lt;YOUR_ID&gt; &quot;&lt;KEY&gt;&quot; &quot;&lt;VALUE&gt;&quot;&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/9492.md")
</aside>
<p>Most <code>kv</code> subcommands also allow you to specify an environment with the optional <code>--env</code> flag.</p>
<p>Specifying an environment with the optional <code>--env</code> flag allows you to publish Workers running the same code but with different KV namespaces.</p>
<p>For example, you could use separate staging and production KV namespaces for KV data in your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9494.md")
</div>
<p>With the Wrangler file above, you can specify <code>--env production</code> when you want to perform a KV action on the KV namespace <code>MY_KV</code> under <code>env.production</code>.</p>
<p>For example, with the Wrangler file above, you can get a value out of a production KV instance with:</p>
<pre tabindex="0"><code class="language-sh">wrangler kv key get --binding &quot;MY_KV&quot; --env=production &quot;&lt;KEY&gt;&quot;&#10;</code></pre>
