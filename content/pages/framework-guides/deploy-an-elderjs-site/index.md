---
cp9:
  canonical: https://developers.cloudflare.com/pages/framework-guides/deploy-an-elderjs-site/
  description: Deploy an Elder.js static site to Cloudflare Pages.
  full_title: Elder.js · Cloudflare Pages docs
  head_html: <title>Elder.js · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy an Elder.js static site to Cloudflare Pages."><link rel="canonical" href="https://developers.cloudflare.com/pages/framework-guides/deploy-an-elderjs-site/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/framework-guides/deploy-an-elderjs-site/index.md"><meta property="og:title" content="Elder.js · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy an Elder.js static site to Cloudflare Pages."><meta property="og:url" content="https://developers.cloudflare.com/pages/framework-guides/deploy-an-elderjs-site/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/framework-guides/deploy-an-elderjs-site/#page","headline":"Elder.js \u00b7 Cloudflare Pages docs","description":"Deploy an Elder.js static site to Cloudflare Pages.","url":"https://developers.cloudflare.com/pages/framework-guides/deploy-an-elderjs-site/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/framework-guides/deploy-an-elderjs-site/
  schema: 1
---
<p><a href="https://elderguide.com/tech/elderjs/">Elder.js</a> is an SEO-focused framework for building static sites with <a href="/pages/framework-guides/deploy-a-svelte-kit-site/">SvelteKit</a>.</p>
<p>In this guide, you will create a new Elder.js application and deploy it using Cloudflare Pages.</p>
<h2 id="setting-up-a-new-project">Setting up a new project</h2>
<p>Create a new project using <a href="https://docs.npmjs.com/cli/v6/commands/npm-init"><code>npx degit Elderjs/template</code></a>, giving it a project name:</p>
<pre tabindex="0"><code class="language-sh">npx degit Elderjs/template elderjs-app&#10;cd elderjs-app&#10;</code></pre>
<p>The Elder.js template includes a number of pages and examples showing how to build your static site, but by simply generating the project, it is already ready to be deployed to Cloudflare Pages.</p>
<h2 id="before-you-continue">Before you continue</h2>
<p>All of the framework guides assume you already have a fundamental understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to this <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<p>If you clone with SSH, you must <a href="https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generate SSH keys</a> on each computer you use to push or pull from GitHub.</p>
<p>Refer to the <a href="https://guides.github.com/introduction/git-handbook/">GitHub documentation</a> and <a href="https://git-scm.com/book/en/v2">Git documentation</a> for more information.</p>
<h2 id="create-a-github-repository">Create a GitHub repository</h2>
<p>Create a new GitHub repository by visiting <a href="https://repo.new">repo.new</a>. After creating a new repository, go to your newly created project directory to prepare and push your local application to GitHub by running the following commands in your terminal:</p>
<pre tabindex="0"><code class="language-sh">git init&#10;git remote add origin https://github.com/&lt;your-gh-username&gt;/&lt;repository-name&gt;&#10;git add .&#10;git commit -m &quot;Initial commit&quot;&#10;git branch -M main&#10;git push -u origin main&#10;</code></pre>
<h2 id="deploy-with-cloudflare-pages">Deploy with Cloudflare Pages</h2>
<p>To deploy your site to Pages:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Create application**.
3. Select the **Pages** tab.
4. Select **Import an existing Git repository**.
5. Select the new GitHub repository that you created and then select **Begin setup**.
6. In the **Build settings** section, select _Elder.js_ as your **Framework preset**. Your selection will provide the following information:
<table><thead><tr><th>Configuration option</th><th>Value</th></tr></thead><tbody><tr><td>Production branch</td><td><code>main</code></td></tr><tr><td>Build command</td><td><code>npm run build</code></td></tr><tr><td>Build directory</td><td><code>public</code></td></tr></tbody></table>
<p>Optionally, you can customize the <strong>Project name</strong> field. It defaults to the GitHub repository's name, but it does not need to match. The <strong>Project name</strong> value is assigned as your <code>*.pages.dev</code> subdomain.</p>
<h3 id="finalize-setup">Finalize Setup</h3>
<p>After completing configuration, click the <strong>Save and Deploy</strong> button.</p>
<p>You will see your first deploy pipeline in progress. Pages installs all dependencies and builds the project as specified.</p>
<p>Cloudflare Pages will automatically rebuild your project and deploy it on every new pushed commit.</p>
<p>Additionally, you will have access to <a href="/pages/configuration/preview-deployments/">preview deployments</a>, which repeat the build-and-deploy process for pull requests. With these, you can preview changes to your project with a real URL before deploying them to production.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11012.md")
</aside>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your Elder.js site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
