---
cp9:
  canonical: https://developers.cloudflare.com/pages/framework-guides/deploy-a-hono-site/
  description: Deploy a Hono web application to Cloudflare Pages.
  full_title: Hono · Cloudflare Pages docs
  head_html: <title>Hono · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy a Hono web application to Cloudflare Pages."><link rel="canonical" href="https://developers.cloudflare.com/pages/framework-guides/deploy-a-hono-site/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/framework-guides/deploy-a-hono-site/index.md"><meta property="og:title" content="Hono · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy a Hono web application to Cloudflare Pages."><meta property="og:url" content="https://developers.cloudflare.com/pages/framework-guides/deploy-a-hono-site/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Pages"><meta name="pcx_tags" content="Hono"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/framework-guides/deploy-a-hono-site/#page","headline":"Hono \u00b7 Cloudflare Pages docs","description":"Deploy a Hono web application to Cloudflare Pages.","url":"https://developers.cloudflare.com/pages/framework-guides/deploy-a-hono-site/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Hono"]}</script>
  markdown: true
  noindex: false
  route: /pages/framework-guides/deploy-a-hono-site/
  schema: 1
---
<p><a href="https://honojs.dev/">Hono</a> is a small, simple, and ultrafast web framework for Cloudflare Pages and Workers, Deno, and Bun. Learn more about the creation of Hono by <a href="#creator-interview">watching an interview</a> with its creator, <a href="https://yusu.ke/">Yusuke Wada</a>.</p>
<p>In this guide, you will create a new Hono application and deploy it using Cloudflare Pages.</p>
<h2 id="create-a-new-project">Create a new project</h2>
<p>Use the <a href="https://www.npmjs.com/package/create-cloudflare"><code>create-cloudflare</code></a> CLI (C3) to create a new project. C3 will create a new project directory, initiate Hono's official setup tool, and provide the option to deploy instantly.</p>
<p>To use <code>create-cloudflare</code> to create a new Hono project, run the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- my-hono-app --framework=hono --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-hono-app --framework=hono --platform=pages" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare my-hono-app --framework=hono --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-hono-app --framework=hono --platform=pages" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest my-hono-app --framework=hono --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-hono-app --framework=hono --platform=pages" aria-label="Copy to clipboard">Copy</button></div></div>
<p>In your new Hono project, you will find a <code>public/static</code> directory for your static files, and a <code>src/index.ts</code> file which is the entrypoint for your server-side code.</p>
<h2 id="run-in-local-dev">Run in local dev</h2>
<p>Develop your app locally by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm run dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm run dev" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn run dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn run dev" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm run dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm run dev" aria-label="Copy to clipboard">Copy</button></div></div>
<p>You should be able to review your generated web application at <code>http://localhost:8788</code>.</p>
<h2 id="before-you-continue">Before you continue</h2>
<p>All of the framework guides assume you already have a fundamental understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to this <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<p>If you clone with SSH, you must <a href="https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generate SSH keys</a> on each computer you use to push or pull from GitHub.</p>
<p>Refer to the <a href="https://guides.github.com/introduction/git-handbook/">GitHub documentation</a> and <a href="https://git-scm.com/book/en/v2">Git documentation</a> for more information.</p>
<h2 id="create-a-github-repository">Create a GitHub repository</h2>
<p>Create a new GitHub repository by visiting <a href="https://repo.new">repo.new</a>. After creating a new repository, go to your newly created project directory to prepare and push your local application to GitHub by running the following commands in your terminal:</p>
<pre tabindex="0"><code class="language-sh">git init&#10;git remote add origin https://github.com/&lt;your-gh-username&gt;/&lt;repository-name&gt;&#10;git add .&#10;git commit -m &quot;Initial commit&quot;&#10;git branch -M main&#10;git push -u origin main&#10;</code></pre>
<h2 id="deploy-with-cloudflare-pages">Deploy with Cloudflare Pages</h2>
<h3 id="deploy-via-the-create-cloudflare-cli-c3">Deploy via the <code>create-cloudflare</code> CLI (C3)</h3>
<p>If you use <a href="https://www.npmjs.com/package/create-cloudflare"><code>create-cloudflare</code>(C3)</a> to create your new Hono project, C3 will install all dependencies needed for your project and prompt you to deploy your project via the CLI. If you deploy, your site will be live and you will be provided with a deployment URL.</p>
<h3 id="deploy-via-the-cloudflare-dashboard">Deploy via the Cloudflare dashboard</h3>
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
<td>Build command</td>
<td><code>npm run build</code></td>
</tr>
<tr>
<td>Build directory</td>
<td><code>dist</code></td>
</tr>
</tbody>
</table>
</div>
<p>After configuring your site, you can begin your first deploy. You should see Cloudflare Pages installing <code>my-hono-app</code>, your project dependencies, and building your site before deploying it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11051.md")
</aside>
<p>After deploying your site, you will receive a unique subdomain for your project on <code>*.pages.dev</code>.
Every time you commit new code to your Hono site, Cloudflare Pages will automatically rebuild your project and deploy it. You will also get access to <a href="/pages/configuration/preview-deployments/">preview deployments</a> on new pull requests, so you can preview how changes look to your site before deploying them to production.</p>
<h2 id="related-resources">Related resources</h2>
<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/yoqtk85HITM" title="YouTube video" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
