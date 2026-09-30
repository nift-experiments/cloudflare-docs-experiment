---
cp9:
  canonical: https://developers.cloudflare.com/pages/migrations/migrating-from-workers/
  description: Learn how to migrate from Workers Sites to Cloudflare Pages.
  full_title: Migrating from Workers Sites to Pages · Cloudflare Pages docs
  head_html: <title>Migrating from Workers Sites to Pages · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to migrate from Workers Sites to Cloudflare Pages."><link rel="canonical" href="https://developers.cloudflare.com/pages/migrations/migrating-from-workers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/migrations/migrating-from-workers/index.md"><meta property="og:title" content="Migrating from Workers Sites to Pages · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to migrate from Workers Sites to Cloudflare Pages."><meta property="og:url" content="https://developers.cloudflare.com/pages/migrations/migrating-from-workers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/migrations/migrating-from-workers/#page","headline":"Migrating from Workers Sites to Pages \u00b7 Cloudflare Pages docs","description":"Learn how to migrate from Workers Sites to Cloudflare Pages.","url":"https://developers.cloudflare.com/pages/migrations/migrating-from-workers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/migrations/migrating-from-workers/
  schema: 1
---
<p>In this tutorial, you will learn how to migrate an existing <a href="/workers/configuration/sites/">Cloudflare Workers Sites</a> application to Cloudflare Pages.</p>
<p>As a prerequisite, you should have a Cloudflare Workers Sites project, created with <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/wrangler">Wrangler</a>.</p>
<p>Cloudflare Pages provides built-in defaults for every aspect of serving your site. You can port custom behavior in your Worker — such as custom caching logic — to your Cloudflare Pages project using <a href="/pages/functions/">Functions</a>. This enables an easy-to-use, file-based routing system. You can also migrate your custom headers and redirects to Pages.</p>
<p>You may already have a reasonably complex Worker and/or it would be tedious to splice it up into Pages' file-based routing system. For these cases, Pages offers developers the ability to define a <code>_worker.js</code> file in the output directory of your Pages project.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10881.md")
</aside>
<p>By migrating to Cloudflare Pages, you will be able to access features like <a href="/pages/configuration/preview-deployments/">preview deployments</a> and automatic branch deploys with no extra configuration needed.</p>
<h2 id="remove-unnecessary-code">Remove unnecessary code</h2>
<p>Workers Sites projects consist of the following pieces:</p>
<ol>
<li>An application built with a <a href="/pages/how-to/">static site tool</a> or a static collection of HTML, CSS and JavaScript files.</li>
<li>If using a static site tool, a build directory (called <code>bucket</code> in the <a href="/pages/functions/wrangler-configuration/">Wrangler configuration file</a>) where the static project builds your HTML, CSS, and JavaScript files.</li>
<li>A Worker application for serving that build directory. For most projects, this is likely to be the <code>workers-site</code> directory.</li>
</ol>
<p>When moving to Cloudflare Pages, remove the Workers application and any associated Wrangler configuration files or build output. Instead, note and record your <code>build</code> command (if you have one), and the <code>bucket</code> field, or build directory, from the Wrangler file in your project's directory.</p>
<h2 id="migrate-headers-and-redirects">Migrate headers and redirects</h2>
<p>You can migrate your redirects to Pages, by creating a <code>_redirects</code> file in your output directory. Pages currently offers limited support for advanced redirects. More support will be added in the future. For a list of support types, refer to the <a href="/pages/configuration/redirects/">Redirects documentation</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10880.md")
</aside>
<p>In addition to a <code>_redirects</code> file, Cloudflare also offers <a href="/pages/configuration/redirects/#surpass-_redirects-limits">Bulk Redirects</a>, which handles redirects that surpasses the 2,100 redirect rules limit set by Pages.</p>
<p>Your custom headers can also be moved into a <code>_headers</code> file in your output directory. It is important to note that custom headers defined in the <code>_headers</code> file are not currently applied to responses from Functions, even if the Function route matches the URL pattern. To learn more about handling headers, refer to <a href="/pages/configuration/headers/">Headers</a>.</p>
<h2 id="create-a-new-pages-project">Create a new Pages project</h2>
<h3 id="connect-to-your-git-provider">Connect to your git provider</h3>
<p>After you have recorded your <strong>build command</strong> and <strong>build directory</strong> in a separate location, remove everything else from your application, and push the new version of your project up to your git provider. Follow the <a href="/pages/get-started/">Get started guide</a> to add your project to Cloudflare Pages, using the <strong>build command</strong> and <strong>build directory</strong> that you saved earlier.</p>
<p>If you choose to use a custom domain for your Pages project, you can set it to the same custom domain as your currently deployed Workers application. Follow the steps for <a href="/pages/configuration/custom-domains/#add-a-custom-domain">adding a custom domain</a> to your Pages project.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10879.md")
</aside>
<h3 id="using-direct-upload">Using Direct Upload</h3>
<p>If your Workers site has its custom build settings, you can bring your prebuilt assets to Pages with <a href="/pages/get-started/direct-upload/">Direct Upload</a>. In addition, you can serve your website's assets right to the Cloudflare global network by either using the <a href="/workers/wrangler/install-and-update/">Wrangler CLI</a> or the drag and drop option.</p>
<p>These options allow you to create and name a new project from the CLI or dashboard. After your project deployment is complete, you can set the custom domain by following the <a href="/pages/configuration/custom-domains/#add-a-custom-domain">adding a custom domain</a> steps to your Pages project.</p>
<h2 id="cleaning-up-your-old-application-and-assigning-the-domain">Cleaning up your old application and assigning the domain</h2>
<p>After you have deployed your Pages application, to delete your Worker:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your Worker.</li>
<li>Go to <strong>Manage</strong> &gt; <strong>Delete Worker</strong>.</li>
</ol>
<p>With your Workers application removed, requests will go to your Pages application. You have successfully migrated your Workers Sites project to Cloudflare Pages by completing this guide.</p>
