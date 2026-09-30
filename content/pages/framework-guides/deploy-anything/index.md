---
cp9:
  canonical: https://developers.cloudflare.com/pages/framework-guides/deploy-anything/
  description: Deploy any static HTML website to Cloudflare Pages without a framework.
  full_title: Static HTML · Cloudflare Pages docs
  head_html: <title>Static HTML · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy any static HTML website to Cloudflare Pages without a framework."><link rel="canonical" href="https://developers.cloudflare.com/pages/framework-guides/deploy-anything/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/framework-guides/deploy-anything/index.md"><meta property="og:title" content="Static HTML · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy any static HTML website to Cloudflare Pages without a framework."><meta property="og:url" content="https://developers.cloudflare.com/pages/framework-guides/deploy-anything/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/framework-guides/deploy-anything/#page","headline":"Static HTML \u00b7 Cloudflare Pages docs","description":"Deploy any static HTML website to Cloudflare Pages without a framework.","url":"https://developers.cloudflare.com/pages/framework-guides/deploy-anything/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/framework-guides/deploy-anything/
  schema: 1
---
<p>Cloudflare supports deploying any static HTML website to Cloudflare Pages. If you manage your website without using a framework or static site generator, or if your framework is not listed in <a href="/pages/framework-guides/">Framework guides</a>, you can still deploy it using this guide.</p>
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
<td>Build command (optional)</td>
<td><code>exit 0</code></td>
</tr>
<tr>
<td>Build output directory</td>
<td><code>&lt;YOUR_BUILD_DIR&gt;</code></td>
</tr>
</tbody>
</table>
</div>
<p>Unlike many of the framework guides, the build command and build output directory for your site are going to be completely custom. If you are not using a preset and do not need to build your site, use <code>exit 0</code> as your <strong>Build command</strong>. Cloudflare recommends using <code>exit 0</code> as your <strong>Build command</strong> to access features such as Pages Functions. The <strong>Build output directory</strong> is where your application's content lives.</p>
<p>After configuring your site, you can begin your first deploy. Your custom build command (if provided) will run, and Pages will deploy your static site.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11009.md")
</aside>
<p>After you have deployed your site, you will receive a unique subdomain for your project on <code>*.pages.dev</code>. Cloudflare Pages will automatically rebuild your project and deploy it. You will also get access to <a href="/pages/configuration/preview-deployments/">preview deployments</a> on new pull requests, so you can preview how changes look to your site before deploying them to production.</p>
<details class="nb-details"><summary>Getting 404 errors on *.pages.dev?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11010.md")
</div></details>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your   site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
