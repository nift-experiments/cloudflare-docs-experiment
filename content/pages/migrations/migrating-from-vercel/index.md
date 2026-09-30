---
cp9:
  canonical: https://developers.cloudflare.com/pages/migrations/migrating-from-vercel/
  description: In this tutorial, you will learn how to deploy your Vercel application to Cloudflare Pages.
  full_title: Migrating from Vercel to Pages · Cloudflare Pages docs
  head_html: <title>Migrating from Vercel to Pages · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="In this tutorial, you will learn how to deploy your Vercel application to Cloudflare Pages."><link rel="canonical" href="https://developers.cloudflare.com/pages/migrations/migrating-from-vercel/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/migrations/migrating-from-vercel/index.md"><meta property="og:title" content="Migrating from Vercel to Pages · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="In this tutorial, you will learn how to deploy your Vercel application to Cloudflare Pages."><meta property="og:url" content="https://developers.cloudflare.com/pages/migrations/migrating-from-vercel/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/migrations/migrating-from-vercel/#page","headline":"Migrating from Vercel to Pages \u00b7 Cloudflare Pages docs","description":"In this tutorial, you will learn how to deploy your Vercel application to Cloudflare Pages.","url":"https://developers.cloudflare.com/pages/migrations/migrating-from-vercel/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/migrations/migrating-from-vercel/
  schema: 1
---
<p>In this tutorial, you will learn how to deploy your Vercel application to Cloudflare Pages.</p>
<p>You should already have an existing project deployed on Vercel that you would like to host on Cloudflare Pages. Features such as Vercel's serverless functions are currently not supported in Cloudflare Pages.</p>
<h2 id="find-your-build-command-and-build-directory">Find your build command and build directory</h2>
<p>To move your application to Cloudflare Pages, you will need to find your build command and build directory. Cloudflare Pages will use this information to build your application and deploy it.</p>
<p>In your Vercel Dashboard, find the project that you want to deploy. It should be configured to deploy from a GitHub repository.</p>
<p><img src="/assets/upstream/images/pages/migrations/vercel-deploy-1.png" alt="Selecting a site in the Vercel Dashboard" /></p>
<p>Inside of your site dashboard, select <strong>Settings</strong>, then <strong>General</strong>.</p>
<p><img src="/assets/upstream/images/pages/migrations/vercel-deploy-2.png" alt="Selecting Site Settings in site dashboard" /></p>
<p>Find the <strong>Build &amp; Development settings</strong> panel, which will have the <strong>Build Command</strong> and <strong>Output Directory</strong> fields. If you are using a framework, these values may not be filled in, but will show the defaults used by the framework. Save these for deploying to Cloudflare Pages. In the below image, the <strong>Build Command</strong> is <code>npm run build</code>, and the <strong>Output Directory</strong> is <code>build</code>.</p>
<p><img src="/assets/upstream/images/pages/migrations/vercel-deploy-3.png" alt="Finding the Build Command and Output Directory fields" /></p>
<h2 id="create-a-new-pages-project">Create a new Pages project</h2>
<p>After you have found your build directory and build command, you can move your project to Cloudflare Pages.</p>
<p>The <a href="/pages/get-started/">Get started guide</a> will instruct you how to add your GitHub project to Cloudflare Pages.</p>
<h2 id="add-a-custom-domain">Add a custom domain</h2>
<p>Next, connect a <a href="/pages/configuration/custom-domains/">custom domain</a> to your Pages project. This domain should be the same one as your currently deployed Vercel application.</p>
<h3 id="change-domain-nameservers">Change domain nameservers</h3>
<p>In most cases, you will want to <a href="/dns/zone-setups/full-setup/setup/">add your domain to Cloudflare</a>.</p>
<p>This does involve changing your domain nameservers, but simplifies your Pages setup and allows you to use an apex domain for your project (like <code>example.com</code>).</p>
<p>If you want to take a different approach, read more about <a href="/pages/configuration/custom-domains/">custom domains</a>.</p>
<h3 id="set-up-custom-domain">Set up custom domain</h3>
<p>To add a custom domain:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project > **Custom domains**.
3. Select **Set up a domain**.
4. Provide the domain that you would like to serve your Cloudflare Pages site on and select **Continue**.
<p><img src="/assets/upstream/images/pages/platform/domains.png" alt="Adding a custom domain for your Pages project through the Cloudflare dashboard" /></p>
<p>The next steps vary based on if you <a href="#change-domain-nameservers">added your domain to Cloudflare</a>:</p>
<ul>
<li><strong>Added to Cloudflare</strong>: Cloudflare will set everything up for you automatically and your domain will move to an <code>Active</code> status.</li>
<li><strong>Not added to Cloudflare</strong>: You need to <a href="/pages/configuration/custom-domains/#add-a-custom-subdomain">update some DNS records</a> at your DNS provider to finish your setup.</li>
</ul>
<h2 id="delete-your-vercel-app">Delete your Vercel app</h2>
<p>Once your custom domain is set up and sending requests to Cloudflare Pages, you can safely delete your Vercel application.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>Cloudflare does not provide IP addresses for your Pages project because we do not require <code>A</code> or <code>AAAA</code> records to link your domain to your project. Instead, Cloudflare uses <code>CNAME</code> records.</p>
<p>For more details, refer to <a href="/pages/configuration/custom-domains/">Custom domains</a>.</p>
