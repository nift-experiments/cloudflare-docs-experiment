---
cp9:
  canonical: https://developers.cloudflare.com/pages/how-to/deploy-a-wordpress-site/
  description: Learn how to deploy a static WordPress site using Cloudflare Pages.
  full_title: Deploy a static WordPress site · Cloudflare Pages docs
  head_html: <title>Deploy a static WordPress site · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to deploy a static WordPress site using Cloudflare Pages."><link rel="canonical" href="https://developers.cloudflare.com/pages/how-to/deploy-a-wordpress-site/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/how-to/deploy-a-wordpress-site/index.md"><meta property="og:title" content="Deploy a static WordPress site · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to deploy a static WordPress site using Cloudflare Pages."><meta property="og:url" content="https://developers.cloudflare.com/pages/how-to/deploy-a-wordpress-site/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Pages"><meta name="pcx_tags" content="WordPress"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/how-to/deploy-a-wordpress-site/#page","headline":"Deploy a static WordPress site \u00b7 Cloudflare Pages docs","description":"Learn how to deploy a static WordPress site using Cloudflare Pages.","url":"https://developers.cloudflare.com/pages/how-to/deploy-a-wordpress-site/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["WordPress"]}</script>
  markdown: true
  noindex: false
  route: /pages/how-to/deploy-a-wordpress-site/
  schema: 1
---
<h2 id="overview">Overview</h2>
<p>In this guide, you will use a WordPress plugin, <a href="https://wordpress.org/plugins/simply-static/">Simply Static</a>, to convert your existing WordPress site to a static website deployed with Cloudflare Pages.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>This guide assumes that you are:</p>
<ul>
<li>The Administrator account on your WordPress site.</li>
<li>Able to install WordPress plugins on the site.</li>
</ul>
<h2 id="setup">Setup</h2>
<p>To start, install the <a href="https://wordpress.org/plugins/simply-static/">Simply Static</a> plugin to export your WordPress site. In your WordPress dashboard, go to <strong>Plugins</strong> &gt; <strong>Add New</strong>.</p>
<p>Search for <code>Simply Static</code> and confirm that the resulting plugin that you will be installing matches the plugin below.</p>
<p><img src="/assets/upstream/images/pages/how-to/simply-static.png" alt="Simply Static plugin" /></p>
<p>Select <strong>Install</strong> on the plugin. After it has finished installing, select <strong>Activate</strong>.</p>
<h3 id="export-your-wordpress-site">Export your WordPress site</h3>
<p>After you have installed the plugin, go to your WordPress dashboard &gt; <strong>Simply Static</strong> &gt; <strong>GENERATE STATIC FILES</strong>.</p>
<p>In the <strong>Activity Log</strong>, find the <strong>ZIP archive created</strong> message and select <strong>Click here to download</strong> to download your ZIP file.</p>
<h3 id="deploy-your-wordpress-site-with-pages">Deploy your WordPress site with Pages</h3>
<p>With your ZIP file downloaded, deploy your site to Pages:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create application</strong> &gt; <strong>Pages</strong> &gt; <strong>Use direct upload</strong>.</li>
<li>Name your project, then select <strong>Create project</strong>.</li>
<li>Drag and drop your ZIP file (or unzipped folder of assets) or select it from your computer.</li>
<li>After your files have been uploaded, select <strong>Deploy site</strong>.</li>
</ol>
<p>Your WordPress site will now be live on Pages.</p>
<p>Every time you make a change to your WordPress site, you will need to download a new ZIP file from the WordPress dashboard and redeploy to Cloudflare Pages. Automatic updates are not available with the free version of Simply Static.</p>
<h2 id="limitations">Limitations</h2>
<p>There are some features available in WordPress sites that will not be supported in a static site environment:</p>
<ul>
<li>WordPress Forms.</li>
<li>WordPress Comments.</li>
<li>Any links to <code>/wp-admin</code> or similar internal WordPress routes.</li>
</ul>
<h2 id="conclusion">Conclusion</h2>
<p>By following this guide, you have successfully deployed a static version of your WordPress site to Cloudflare Pages.</p>
<p>With a static version of your site being served, you can:</p>
<ul>
<li>Move your WordPress site to a custom domain or subdomain. Refer to <a href="/pages/configuration/custom-domains/">Custom domains</a> to learn more.</li>
<li>Run your WordPress instance locally, or put your WordPress site behind <a href="/pages/configuration/preview-deployments/#customize-preview-deployments-access">Cloudflare Access</a> to only give access to your contributors. This has a significant effect on the number of attack vectors for your WordPress site and its content.</li>
<li>Downgrade your WordPress hosting plan to a cheaper plan. Because the memory and bandwidth requirements for your WordPress instance are now smaller, you can often host it on a cheaper plan, or moving to shared hosting.</li>
</ul>
<p>Connect with the <a href="https://discord.cloudflare.com">Cloudflare Developer community on Discord</a> to ask questions and discuss the platform with other developers.</p>
