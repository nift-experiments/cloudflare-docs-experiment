---
cp9:
  canonical: https://developers.cloudflare.com/pages/functions/local-development/
  description: Run and test your Pages application locally using Wrangler.
  full_title: Local development · Cloudflare Pages docs
  head_html: <title>Local development · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Run and test your Pages application locally using Wrangler."><link rel="canonical" href="https://developers.cloudflare.com/pages/functions/local-development/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/functions/local-development/index.md"><meta property="og:title" content="Local development · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Run and test your Pages application locally using Wrangler."><meta property="og:url" content="https://developers.cloudflare.com/pages/functions/local-development/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/functions/local-development/#page","headline":"Local development \u00b7 Cloudflare Pages docs","description":"Run and test your Pages application locally using Wrangler.","url":"https://developers.cloudflare.com/pages/functions/local-development/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/functions/local-development/
  schema: 1
---
<p>Run your Pages application locally with our Wrangler Command Line Interface (CLI).</p>
<h2 id="install-wrangler">Install Wrangler</h2>
<p>To get started with Wrangler, refer to the <a href="/workers/wrangler/install-and-update/">Install/Update Wrangler</a>.</p>
<h2 id="run-your-pages-project-locally">Run your Pages project locally</h2>
<p>The main command for local development on Pages is <code>wrangler pages dev</code>. This will let you run your Pages application locally, which includes serving static assets and running your Functions.</p>
<p>With your folder of static assets set up, run the following command to start local development:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler pages dev &lt;DIRECTORY-OF-ASSETS&gt;&#10;</code></pre>
<p>This will then start serving your Pages project. You can press <code>b</code> to open the browser on your local site, (available, by default, on <a href="http://localhost:8788">http://localhost:8788</a>).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10950.md")
</aside>
<h3 id="https-support">HTTPS support</h3>
<p>To serve your local development server over HTTPS with a self-signed certificate, you can [set <code>local_protocol</code> via the <a href="/pages/functions/wrangler-configuration/#local-development-settings">Wrangler configuration file</a> or you can pass the <code>--local-protocol=https</code> argument to <a href="/workers/wrangler/commands/pages/#pages-dev"><code>wrangler pages dev</code></a>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler pages dev --local-protocol=https &lt;DIRECTORY-OF-ASSETS&gt;&#10;</code></pre>
<h2 id="attach-bindings-to-local-development">Attach bindings to local development</h2>
<p>To attach a binding to local development, refer to <a href="/pages/functions/bindings/">Bindings</a> and find the Cloudflare Developer Platform resource you would like to work with.</p>
<h2 id="additional-wrangler-configuration">Additional Wrangler configuration</h2>
<p>If you are using a Wrangler configuration file in your project, you can set up dev server values like: <code>port</code>, <code>local protocol</code>, <code>ip</code>, and <code>port</code>. For more information, read about <a href="/pages/functions/wrangler-configuration/#local-development-settings">configuring local development settings</a>.</p>
