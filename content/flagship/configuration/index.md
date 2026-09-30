---
cp9:
  canonical: https://developers.cloudflare.com/flagship/configuration/
  description: Add and configure a Flagship binding in your Wrangler configuration file to evaluate feature flags in a Worker.
  full_title: Configuration · Cloudflare Flagship docs
  head_html: <title>Configuration · Cloudflare Flagship docs</title><meta name="generator" content="Nift"><meta name="description" content="Add and configure a Flagship binding in your Wrangler configuration file to evaluate feature flags in a Worker."><link rel="canonical" href="https://developers.cloudflare.com/flagship/configuration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/flagship/configuration/index.md"><meta property="og:title" content="Configuration · Cloudflare Flagship docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Add and configure a Flagship binding in your Wrangler configuration file to evaluate feature flags in a Worker."><meta property="og:url" content="https://developers.cloudflare.com/flagship/configuration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Flagship"><meta name="algolia_product_filter" content="Flagship"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Flagship"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/flagship/configuration/#page","headline":"Configuration \u00b7 Cloudflare Flagship docs","description":"Add and configure a Flagship binding in your Wrangler configuration file to evaluate feature flags in a Worker.","url":"https://developers.cloudflare.com/flagship/configuration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /flagship/configuration/
  schema: 1
---
<p>To use Flagship in a Cloudflare Worker, add a Flagship binding to your Wrangler configuration file. The binding gives your Worker access to <code>env.FLAGS</code>, which provides methods to evaluate feature flags.</p>
<h2 id="add-the-binding">Add the binding</h2>
<p>Add the <code>flagship</code> block to your Wrangler configuration file with a binding name and your app ID.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1017.md")
</div>
<p>Replace <code>&lt;APP_ID&gt;</code> with the app ID from your Flagship app. If you have not created an app yet, refer to the <a href="/flagship/get-started/#create-an-app-and-a-flag">Get started guide</a>. The <code>binding</code> field sets the name you use to access Flagship in your Worker code (for example, <code>env.FLAGS</code>).</p>
<h2 id="bind-to-multiple-apps">Bind to multiple apps</h2>
<p>A single Worker can bind to multiple Flagship apps. Use the array form to define more than one binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1018.md")
</div>
<p>Each binding is available as a separate property on the <code>env</code> object (for example, <code>env.FLAGS</code> and <code>env.EXPERIMENT_FLAGS</code>).</p>
<h2 id="generate-types">Generate types</h2>
<p>After adding the binding, run <code>npx wrangler types</code> to generate TypeScript types. This creates the <code>Env</code> interface with each binding typed as <code>Flagship</code>.</p>
<pre tabindex="0"><code class="language-ts">interface Env {&#10;	FLAGS: Flagship;&#10;	EXPERIMENT_FLAGS: Flagship;&#10;}&#10;</code></pre>
<h2 id="use-the-binding">Use the binding</h2>
<p>Call evaluation methods on <code>env.FLAGS</code> to resolve flag values at runtime. Each method accepts a flag key, a default value, and an optional evaluation context.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1019.md")
</div>
<p>Refer to the <a href="/flagship/binding/">binding API reference</a> for the full list of methods.</p>
<h2 id="local-development">Local development</h2>
<p>Flagship bindings work with <code>wrangler dev</code>. Local Workers use the live Flagship app configured by <code>app_id</code>. There is no local flag store. Make sure your local Wrangler configuration points to a valid Flagship app before testing evaluations.</p>
