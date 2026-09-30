---
cp9:
  canonical: https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/
  description: Create an Astro application and deploy it to Cloudflare Workers with Workers Assets.
  full_title: Astro · Cloudflare Workers docs
  head_html: <title>Astro · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Create an Astro application and deploy it to Cloudflare Workers with Workers Assets."><link rel="canonical" href="https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/index.md"><meta property="og:title" content="Astro · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create an Astro application and deploy it to Cloudflare Workers with Workers Assets."><meta property="og:url" content="https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="ssg,full-stack,Astro"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/#page","headline":"Astro \u00b7 Cloudflare Workers docs","description":"Create an Astro application and deploy it to Cloudflare Workers with Workers Assets.","url":"https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["ssg","full-stack","Astro"]}</script>
  markdown: true
  noindex: false
  route: /workers/framework-guides/web-apps/astro/
  schema: 1
---
<p><strong>Start from CLI</strong>: Scaffold an Astro project on Workers, and pick your template.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- my-astro-app --framework=astro</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-astro-app --framework=astro" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare my-astro-app --framework=astro</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-astro-app --framework=astro" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest my-astro-app --framework=astro</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-astro-app --framework=astro" aria-label="Copy to clipboard">Copy</button></div></div>
<hr />
<p><strong>Or just deploy</strong>: Create a static blog with Astro and deploy it on Cloudflare Workers, with CI/CD and previews all set up for you.</p>
<p><a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create/deploy-to-workers&amp;repository=https://github.com/cloudflare/templates/tree/main/astro-blog-starter-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<h2 id="what-is-astro">What is Astro?</h2>
<p><a href="https://astro.build/">Astro</a> is a JavaScript web framework designed for creating websites that display large amounts of content (such as blogs, documentation sites, or online stores).</p>
<p>Astro emphasizes performance through minimal client-side JavaScript - by default, it renders as much content as possible at build time, or <a href="https://docs.astro.build/en/guides/on-demand-rendering/">on-demand</a> on the &quot;server&quot; - this can be a Cloudflare Worker. <a href="https://docs.astro.build/en/concepts/islands/">“Islands”</a> of JavaScript are added only where interactivity or personalization is needed.</p>
<p>Astro is also framework-agnostic, and supports every major UI framework, including React, Preact, Svelte, Vue, SolidJS, via its official <a href="https://astro.build/integrations/">integrations</a>.</p>
<h2 id="deploy-a-new-astro-project-on-workers">Deploy a new Astro project on Workers</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16960.md")
</div>
<h2 id="deploy-an-existing-astro-project-on-workers">Deploy an existing Astro project on Workers</h2>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="automatic-configuration">Automatic configuration</h3>
@markup("md", "content/.markup/bodies/16958.md")
</aside>
<div class="nb-interactive-component" data-cf-component="AutoconfigDiagram"></div>
<h2 id="manual-configuration">Manual configuration</h2>
<p>If you prefer to configure your project manually, follow the steps below.</p>
<h3 id="if-you-have-a-static-site">If you have a static site</h3>
<p>If your Astro project is entirely pre-rendered, follow these steps:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16963.md")
</div>
<h3 id="if-your-site-uses-on-demand-rendering">If your site uses on demand rendering</h3>
<p>If your Astro project uses <a href="https://docs.astro.build/en/guides/on-demand-rendering/">on demand rendering (also known as SSR)</a>, follow these steps:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16967.md")
</div>
<h2 id="bindings">Bindings</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16957.md")
</aside>
<p>With bindings, your Astro application can be fully integrated with the Cloudflare Developer Platform, giving you access to compute, storage, AI and more. Refer to the <a href="/workers/runtime-apis/bindings/">bindings overview</a> for more information on what's available and how to configure them.</p>
<p>The <a href="https://docs.astro.build/en/guides/integrations-guide/cloudflare/#cloudflare-runtime">Astro docs</a> provide information about how you can access them in your <code>locals</code>.</p>
<h2 id="sessions">Sessions</h2>
<p>Astro's <a href="https://docs.astro.build/en/guides/sessions/">Sessions API</a> allows you to store user data between requests, such as user preferences, shopping carts, or authentication credentials. When using the Cloudflare adapter, Astro automatically configures <a href="/kv/">Workers KV</a> for session storage.</p>
<p>Wrangler automatically provisions a KV namespace named <code>SESSION</code> when you deploy, so no manual setup is required.</p>
<pre tabindex="0"><code class="language-astro">&#45;--&#10;export const prerender = false;&#10;const cart = await Astro.session?.get(&quot;cart&quot;);&#10;&#45;--&#10;&#10;&lt;a href=&quot;/checkout&quot;&gt;{cart?.length ?? 0} items&lt;/a&gt;&#10;</code></pre>
<p>You can customize the KV binding name with the <a href="https://docs.astro.build/en/guides/integrations-guide/cloudflare/#sessionkvbindingname"><code>sessionKVBindingName</code></a> adapter option if you want to use a different binding name.</p>
<h2 id="custom-404-pages">Custom 404 pages</h2>
<p>To serve a custom 404 page for your Astro site, add <code>not_found_handling</code> to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16968.md")
</div>
<p>This tells Cloudflare to serve your custom 404 page (for example, <code>src/pages/404.astro</code>) when a route is not found. Read more about <a href="/workers/static-assets/routing/">static asset routing behavior</a>.</p>
<h2 id="astro-s-build-configuration">Astro's build configuration</h2>
<p>The Astro Cloudflare adapter sets the build output configuration to <code>output: 'server'</code>, which means all pages are rendered on-demand in your Cloudflare Worker. If there are certain pages that <em>don't</em> need on demand rendering/SSR, for example static pages such as a privacy policy, you should set <code>export const prerender = true</code> for that page or route to pre-render it. You can read more about on-demand rendering <a href="https://docs.astro.build/en/guides/on-demand-rendering/">in the Astro docs</a>.</p>
<p>If you want to use Astro as a static site generator, you do not need the Astro Cloudflare adapter. Astro will pre-render all pages at build time by default, and you can simply upload those static assets to be served by Cloudflare.</p>
<h2 id="node-js-requirements">Node.js requirements</h2>
<p>Astro 5.x supports Node.js 18.20.8, Node.js 20.3.0 and later 20.x releases, or Node.js 22.0.0 or later. Astro 6.x and 7.x require Node.js 22.12.0 or later. If you use <a href="/workers/ci-cd/builds/">Workers Builds</a>, its default Node.js version meets these requirements. If you override the default, select a version that meets <a href="https://docs.astro.build/en/install-and-setup/#prerequisites">Astro's Node.js requirements</a>.</p>
