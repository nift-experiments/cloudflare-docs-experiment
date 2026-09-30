---
cp9:
  canonical: https://developers.cloudflare.com/pages/framework-guides/deploy-an-angular-site/
  description: Deploy an Angular application to Cloudflare Pages.
  full_title: Angular · Cloudflare Pages docs
  head_html: <title>Angular · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy an Angular application to Cloudflare Pages."><link rel="canonical" href="https://developers.cloudflare.com/pages/framework-guides/deploy-an-angular-site/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/framework-guides/deploy-an-angular-site/index.md"><meta property="og:title" content="Angular · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy an Angular application to Cloudflare Pages."><meta property="og:url" content="https://developers.cloudflare.com/pages/framework-guides/deploy-an-angular-site/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/framework-guides/deploy-an-angular-site/#page","headline":"Angular \u00b7 Cloudflare Pages docs","description":"Deploy an Angular application to Cloudflare Pages.","url":"https://developers.cloudflare.com/pages/framework-guides/deploy-an-angular-site/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/framework-guides/deploy-an-angular-site/
  schema: 1
---
<p><a href="https://angular.io/">Angular</a> is an incredibly popular framework for building reactive and powerful front-end applications.</p>
<p>In this guide, you will create a new Angular application and deploy it using Cloudflare Pages.</p>
<h2 id="create-a-new-project-using-the-create-cloudflare-cli-c3">Create a new project using the <code>create-cloudflare</code> CLI (C3)</h2>
<p>Use the <a href="https://www.npmjs.com/package/create-cloudflare"><code>create-cloudflare</code></a> CLI (C3) to set up a new project. C3 will create a new project directory, initiate Angular's official setup tool, and provide the option to deploy instantly.</p>
<p>To use <code>create-cloudflare</code> to create a new Angular project, run the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- my-angular-app --framework=angular --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-angular-app --framework=angular --platform=pages" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare my-angular-app --framework=angular --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-angular-app --framework=angular --platform=pages" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest my-angular-app --framework=angular --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-angular-app --framework=angular --platform=pages" aria-label="Copy to clipboard">Copy</button></div></div>
<p><code>create-cloudflare</code> will install dependencies, including the <a href="/workers/wrangler/install-and-update/#check-your-wrangler-version">Wrangler</a> CLI and the Cloudflare Pages adapter, and ask you setup questions.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="git-integration">Git integration</h3>
@markup("md", "content/.markup/bodies/11017.md")
</aside>
<h2 id="git-integration-1">Git integration</h2>
<p>In addition to <a href="/pages/get-started/direct-upload/">Direct Upload</a> deployments, you can deploy projects via <a href="/pages/configuration/git-integration">Git integration</a>. Git integration allows you to connect a GitHub or GitLab repository to your Pages application and have your Pages application automatically built and deployed after each new commit is pushed to it.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="git-integration-2">Git integration</h3>
@markup("md", "content/.markup/bodies/11016.md")
</aside>
<p>Setup requires a basic understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to GitHub's <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<h3 id="create-a-github-repository">Create a GitHub repository</h3>
<p>Create a new GitHub repository by visiting <a href="https://repo.new">repo.new</a>. After creating a new repository, go to your newly created project directory to prepare and push your local application to GitHub by running the following commands in your terminal:
<br /></p>
<pre tabindex="0"><code class="language-sh">&#35; Skip the following three commands if you have built your application&#10;&#35; using C3 or already committed your changes&#10;git init&#10;git add .&#10;git commit -m &quot;Initial commit&quot;&#10;&#10;git branch -M main&#10;git remote add origin https://github.com/&lt;YOUR_GH_USERNAME&gt;/&lt;REPOSITORY_NAME&gt;&#10;git push -u origin main&#10;</code></pre>
<h3 id="create-a-pages-project">Create a Pages project</h3>
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
<table><thead><tr><th>Configuration option</th><th>Value</th></tr></thead><tbody><tr><td>Production branch</td><td><code>main</code></td></tr><tr><td>Build command</td><td><code>npm run build</code></td></tr><tr><td>Build directory</td><td><code>dist/cloudflare</code></td></tr></tbody></table>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="on-some-versions-of-angular-you-may-need-to">On some versions of Angular, you may need to:</h3>
@markup("md", "content/.markup/bodies/11015.md")
</aside>
<p>Optionally, you can customize the <strong>Project name</strong> field. It defaults to the GitHub repository's name, but it does not need to match. The <strong>Project name</strong> value is assigned as your <code>*.pages.dev</code> subdomain.</p>
<ol start="7">
<li>After completing configuration, select the <strong>Save and Deploy</strong>.</li>
</ol>
<p>Review your first deploy pipeline in progress. Pages installs all dependencies and builds the project as specified. Cloudflare Pages will automatically rebuild your project and deploy it on every new pushed commit.</p>
<p>Additionally, you will have access to <a href="/pages/configuration/preview-deployments/">preview deployments</a>, which repeat the build-and-deploy process for pull requests. With these, you can preview changes to your project with a real URL before deploying your changes to production.</p>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your Angular site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
