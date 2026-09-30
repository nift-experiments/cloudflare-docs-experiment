---
cp9:
  canonical: https://developers.cloudflare.com/pages/migrations/migrating-jekyll-from-github-pages/
  description: Learn how to migrate a Jekyll-based site from GitHub Pages to Cloudflare Pages.
  full_title: Migrating a Jekyll-based site from GitHub Pages · Cloudflare Pages docs
  head_html: <title>Migrating a Jekyll-based site from GitHub Pages · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to migrate a Jekyll-based site from GitHub Pages to Cloudflare Pages."><link rel="canonical" href="https://developers.cloudflare.com/pages/migrations/migrating-jekyll-from-github-pages/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/migrations/migrating-jekyll-from-github-pages/index.md"><meta property="og:title" content="Migrating a Jekyll-based site from GitHub Pages · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to migrate a Jekyll-based site from GitHub Pages to Cloudflare Pages."><meta property="og:url" content="https://developers.cloudflare.com/pages/migrations/migrating-jekyll-from-github-pages/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Pages"><meta name="pcx_tags" content="Ruby"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/migrations/migrating-jekyll-from-github-pages/#page","headline":"Migrating a Jekyll-based site from GitHub Pages \u00b7 Cloudflare Pages docs","description":"Learn how to migrate a Jekyll-based site from GitHub Pages to Cloudflare Pages.","url":"https://developers.cloudflare.com/pages/migrations/migrating-jekyll-from-github-pages/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Ruby"]}</script>
  markdown: true
  noindex: false
  route: /pages/migrations/migrating-jekyll-from-github-pages/
  schema: 1
---
<p>In this tutorial, you will learn how to migrate an existing <a href="https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll">GitHub Pages site using Jekyll</a> to Cloudflare Pages. Jekyll is one of the most popular static site generators used with GitHub Pages, and migrating your GitHub Pages site to Cloudflare Pages will take a few short steps.</p>
<p>This tutorial will guide you through:</p>
<ol>
<li>Adding the necessary dependencies used by GitHub Pages to your project configuration.</li>
<li>Creating a new Cloudflare Pages site, connected to your existing GitHub repository.</li>
<li>Building and deploying your site on Cloudflare Pages.</li>
<li>(Optional) Migrating your custom domain.</li>
</ol>
<p>Including build times, this tutorial should take you less than 15 minutes to complete.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10878.md")
</aside>
<h2 id="before-you-begin">Before you begin</h2>
<p>This tutorial assumes:</p>
<ol>
<li>You have an existing GitHub Pages site using <a href="https://jekyllrb.com/">Jekyll</a></li>
<li>You have some familiarity with running Ruby's command-line tools, and have both <code>gem</code> and <code>bundle</code> installed.</li>
<li>You know how to use a few basic Git operations, including <code>add</code>, <code>commit</code>, <code>push</code>, and <code>pull</code>.</li>
<li>You have read the <a href="/pages/get-started/">Get Started</a> guide for Cloudflare Pages.</li>
</ol>
<p>If you do not have Rubygems (<code>gem</code>) or Bundler (<code>bundle</code>) installed on your machine, refer to the installation guides for <a href="https://rubygems.org/pages/download">Rubygems</a> and <a href="https://bundler.io/">Bundler</a>.</p>
<h2 id="preparing-your-github-pages-repository">Preparing your GitHub Pages repository</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10877.md")
</aside>
<p>Your existing Jekyll-based repository must specify a <code>Gemfile</code> (Ruby's dependency configuration file) to allow Cloudflare Pages to fetch and install those dependencies during the <a href="/pages/configuration/build-configuration/">build step</a>.</p>
<p>Specifically, you will need to create a <code>Gemfile</code> and install the <code>github-pages</code> gem, which includes all of the dependencies that the GitHub Pages environment assumes.</p>
<p><a href="/pages/configuration/build-image/#languages-and-runtime">Version 2 of the Pages build environment</a> will use Ruby 3.2.2 for the default Jekyll build. Please make sure your local development environment is compatible.</p>
<pre tabindex="0"><code class="language-sh">brew install ruby@3.2&#10;export PATH=&quot;/usr/local/opt/ruby@3.2/bin:$PATH&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">cd my-github-pages-repo&#10;bundle init&#10;</code></pre>
<p>Open the <code>Gemfile</code> that was created for you, and add the following line to the bottom of the file:</p>
<pre tabindex="0"><code class="language-ruby">gem &quot;github-pages&quot;, group: :jekyll_plugins&#10;</code></pre>
<p>Your <code>Gemfile</code> should resemble the below:</p>
<pre tabindex="0"><code class="language-ruby">&#35; frozen_string_literal: true&#10;&#10;source &quot;https://rubygems.org&quot;&#10;&#10;git_source(:github) { |repo_name| &quot;https://github.com/#{repo_name}&quot; }&#10;&#10;&#35; gem &quot;rails&quot;&#10;gem &quot;github-pages&quot;, group: :jekyll_plugins&#10;</code></pre>
<p>Run <code>bundle update</code>, which will install the <code>github-pages</code> gem for you, and create a <code>Gemfile.lock</code> file with the resolved dependency versions.</p>
<pre tabindex="0"><code class="language-sh">bundle update&#10;&#35; Bundler will show a lot of output as it fetches the dependencies&#10;</code></pre>
<p>This should complete successfully. If not, verify that you have copied the <code>github-pages</code> line above exactly, and have not commented it out with a leading <code>#</code>.</p>
<p>You will now need to commit these files to your repository so that Cloudflare Pages can reference them in the following steps:</p>
<pre tabindex="0"><code class="language-sh">git add Gemfile Gemfile.lock&#10;git commit -m &quot;deps: added Gemfiles&quot;&#10;git push origin main&#10;</code></pre>
<h2 id="configuring-your-pages-project">Configuring your Pages project</h2>
<p>With your GitHub Pages project now explicitly specifying its dependencies, you can start configuring Cloudflare Pages. The process is almost identical to <a href="/pages/framework-guides/deploy-a-jekyll-site/">deploying a Jekyll site</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10876.md")
</aside>
<p>To deploy your site to Pages:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create application</strong> &gt; <strong>Pages</strong> &gt; <strong>Import an existing Git repository</strong>.</li>
<li>Select the new GitHub repository that you created and, in the <strong>Set up builds and deployments</strong> section, provide the following information:</li>
</ol>
<div>
<table>
<thead>
<tr>
<th>Configuration option</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Production branch</td>
<td><code>main</code></td>
</tr>
<tr>
<td>Build command</td>
<td><code>jekyll build</code></td>
</tr>
<tr>
<td>Build directory</td>
<td><code>_site</code></td>
</tr>
</tbody>
</table>
</div>
<p>After you have configured your site, you can begin your first deploy. You should see Cloudflare Pages installing <code>jekyll</code>, your project dependencies, and building your site, before deploying it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10875.md")
</aside>
<p>After deploying your site, you will receive a unique subdomain for your project on <code>*.pages.dev</code>. Every time you commit new code to your Jekyll site, Cloudflare Pages will automatically rebuild your project and deploy it. You will also get access to <a href="/pages/configuration/preview-deployments/">preview deployments</a> on new pull requests, so you can preview how changes look to your site before deploying them to production.</p>
<h2 id="migrating-your-custom-domain">Migrating your custom domain</h2>
<p>If you are using a <a href="https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site">custom domain with GitHub Pages</a>, you must update your DNS record(s) to point at your new Cloudflare Pages deployment. This will require you to update the <code>CNAME</code> record at the DNS provider for your domain to point to <code>&lt;your-pages-site&gt;.pages.dev</code>, replacing <code>&lt;your-username&gt;.github.io</code>.</p>
<p>Note that it may take some time for DNS caches to expire and for this change to be reflected, depending on the DNS TTL (time-to-live) value you set when you originally created the record.</p>
<p>Refer to the <a href="/pages/configuration/custom-domains/#add-a-custom-domain">adding a custom domain</a> section of the Get started guide for a list of detailed steps.</p>
<h2 id="what-s-next">What's next?</h2>
<ul>
<li>Learn how to <a href="/pages/how-to/add-custom-http-headers/">customize HTTP response headers</a> for your Pages site using Cloudflare Workers.</li>
<li>Understand how to <a href="/pages/configuration/rollbacks/">rollback a potentially broken deployment</a> to a previously working version.</li>
<li><a href="/pages/configuration/redirects/">Configure redirects</a> so that visitors are always directed to your 'canonical' custom domain.</li>
</ul>
