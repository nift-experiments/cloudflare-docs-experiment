---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/components/wrangler-config/
  description: Display Wrangler config in TOML and JSON tabs.
  full_title: WranglerConfig · Cloudflare Style Guide
  head_html: <title>WranglerConfig · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Display Wrangler config in TOML and JSON tabs."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/components/wrangler-config/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/components/wrangler-config/index.md"><meta property="og:title" content="WranglerConfig · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Display Wrangler config in TOML and JSON tabs."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/components/wrangler-config/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/components/wrangler-config/#page","headline":"WranglerConfig \u00b7 Cloudflare Style Guide","description":"Display Wrangler config in TOML and JSON tabs.","url":"https://developers.cloudflare.com/style-guide/build-the-page/components/wrangler-config/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/components/wrangler-config/
  schema: 1
---
<p>This component can be used to automatically generate a <code>jsonc</code> version of the <code>toml</code> file (or vice versa) of the Cloudflare <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<h2 id="import">Import</h2>
<pre tabindex="0"><code class="language-mdx">import { WranglerConfig } from &quot;~/components&quot;;&#10;</code></pre>
<h2 id="usage">Usage</h2>
<pre tabindex="0"><code class="language-mdx">import { WranglerConfig } from &quot;~/components&quot;;&#10;&#10;&lt;WranglerConfig&gt;&#10;</code></pre>
<p>[[d1_databases]]
binding = &quot;DB&quot; # available in your Worker on env.DB
database_name = &quot;prod-d1-tutorial&quot;
database_id = &quot;<unique-ID-for-your-database>&quot;</p>
<pre tabindex="0"><code>&lt;/WranglerConfig&gt;&#10;</code></pre>
<h2 id="compatibility-date">Compatibility date</h2>
<p>You should generally use <code>$today</code> for the <code>compatibility_date</code> value for new projects. This magic string is automatically replaced with the current date at build time, ensuring documentation always suggests the latest date. When <code>$today</code> is used, the component also automatically injects a comment above the <code>compatibility_date</code> line (for example, <code># Set this to today's date</code> in TOML and <code>// Set this to today's date</code> in JSONC) so that readers know to keep the value current. If you need to specify a fixed date, you can do so as well, but you may miss out on the latest features and performance improvements. You can disable specific features by using <a href="/workers/configuration/compatibility-flags/">compatibility flags</a>.</p>
<pre tabindex="0"><code class="language-mdx">import { WranglerConfig } from &quot;~/components&quot;;&#10;&#10;&lt;WranglerConfig&gt;&#10;</code></pre>
<p>{
&quot;name&quot;: &quot;my-worker&quot;,
&quot;compatibility_date&quot;: &quot;$today&quot;
}</p>
<pre tabindex="0"><code>&lt;/WranglerConfig&gt;&#10;</code></pre>
<h3 id="minimum-compatibility-dates">Minimum compatibility dates</h3>
<p>Some features require a minimum compatibility date. When documenting these features, use a <code>:::note</code> component to communicate the requirement clearly on the docs page:</p>
<pre tabindex="0"><code class="language-mdx">:::note&#10;This feature requires a `compatibility_date` of `2024-09-23` or later.&#10;:::&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14624.md")
</aside>
<p>The <code>removeSchema</code> prop can be used to remove the <code>$schema</code> reference from the generated JSON file. This can be useful if you want to add snippets of configuration files that are easier to copy paste, and are providing toml as the source config format.</p>
<p>If you provide jsonc as the source config format, the <code>removeSchema</code> prop will be ignored.</p>
<pre tabindex="0"><code class="language-mdx">import { WranglerConfig } from &quot;~/components&quot;;&#10;&#10;&lt;WranglerConfig removeSchema&gt;&#10;</code></pre>
<p>[[d1_databases]]
binding = &quot;DB&quot; # available in your Worker on env.DB
database_name = &quot;prod-d1-tutorial&quot;
database_id = &quot;<unique-ID-for-your-database>&quot;</p>
<pre tabindex="0"><code>&lt;/WranglerConfig&gt;&#10;</code></pre>
