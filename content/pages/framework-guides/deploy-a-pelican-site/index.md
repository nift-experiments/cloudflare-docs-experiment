---
cp9:
  canonical: https://developers.cloudflare.com/pages/framework-guides/deploy-a-pelican-site/
  description: Deploy a Pelican static site to Cloudflare Pages.
  full_title: Pelican · Cloudflare Pages docs
  head_html: <title>Pelican · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy a Pelican static site to Cloudflare Pages."><link rel="canonical" href="https://developers.cloudflare.com/pages/framework-guides/deploy-a-pelican-site/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/framework-guides/deploy-a-pelican-site/index.md"><meta property="og:title" content="Pelican · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy a Pelican static site to Cloudflare Pages."><meta property="og:url" content="https://developers.cloudflare.com/pages/framework-guides/deploy-a-pelican-site/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/framework-guides/deploy-a-pelican-site/#page","headline":"Pelican \u00b7 Cloudflare Pages docs","description":"Deploy a Pelican static site to Cloudflare Pages.","url":"https://developers.cloudflare.com/pages/framework-guides/deploy-a-pelican-site/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/framework-guides/deploy-a-pelican-site/
  schema: 1
---
<p><a href="https://docs.getpelican.com">Pelican</a> is a static site generator, written in Python. With Pelican, you can write your content directly with your editor of choice in reStructuredText or Markdown formats.</p>
<h2 id="create-a-pelican-project">Create a Pelican project</h2>
<p>To begin, create a Pelican project directory. <code>cd</code> into your new directory and run:</p>
<pre tabindex="0"><code class="language-sh">python3 -m pip install pelican&#10;</code></pre>
<p>Then run:</p>
<pre tabindex="0"><code class="language-sh">pip freeze &gt; requirements.txt&#10;</code></pre>
<p>Create a directory in your project named <code>content</code>:</p>
<pre tabindex="0"><code class="language-sh">mkdir content&#10;</code></pre>
<p>This is the directory name that you will set in the build command.</p>
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
6. In the **Set up builds and deployments** section, provide the following information:
<table><thead><tr><th>Configuration option</th><th>Value</th></tr></thead><tbody><tr><td>Production branch</td><td><code>main</code></td></tr><tr><td>Build command</td><td><code>pelican content</code></td></tr><tr><td>Build directory</td><td><code>output</code></td></tr></tbody></table>
<ol start="7">
<li>Select <strong>Environment variables (advanced)</strong> and set the <code>PYTHON_VERSION</code> variable with the value of <code>3.7</code>.</li>
</ol>
<p>For the complete guide to deploying your first site to Cloudflare Pages, refer to the <a href="/pages/get-started/">Get started guide</a>.</p>
<p>After deploying your site, you will receive a unique subdomain for your project on <code>*.pages.dev</code>.</p>
<p>Every time you commit new code to your Pelican site, Cloudflare Pages will automatically rebuild your project and deploy it. You will also get access to <a href="/pages/configuration/preview-deployments/">preview deployments</a> on new pull requests and be able to preview how changes look to your site before deploying them to production.</p>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your Pelican site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
