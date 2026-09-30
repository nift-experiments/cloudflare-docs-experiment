---
cp9:
  canonical: https://developers.cloudflare.com/pages/framework-guides/deploy-a-blazor-site/
  description: Deploy a Blazor WebAssembly application to Cloudflare Pages.
  full_title: Blazor · Cloudflare Pages docs
  head_html: <title>Blazor · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy a Blazor WebAssembly application to Cloudflare Pages."><link rel="canonical" href="https://developers.cloudflare.com/pages/framework-guides/deploy-a-blazor-site/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/framework-guides/deploy-a-blazor-site/index.md"><meta property="og:title" content="Blazor · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy a Blazor WebAssembly application to Cloudflare Pages."><meta property="og:url" content="https://developers.cloudflare.com/pages/framework-guides/deploy-a-blazor-site/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/framework-guides/deploy-a-blazor-site/#page","headline":"Blazor \u00b7 Cloudflare Pages docs","description":"Deploy a Blazor WebAssembly application to Cloudflare Pages.","url":"https://developers.cloudflare.com/pages/framework-guides/deploy-a-blazor-site/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/framework-guides/deploy-a-blazor-site/
  schema: 1
---
<p><a href="https://blazor.net">Blazor</a> is an SPA framework that can use C# code, rather than JavaScript in the browser. In this guide, you will build a site using Blazor, and deploy it using Cloudflare Pages.</p>
<h2 id="install-net">Install .NET</h2>
<p>Blazor uses C#. You will need the latest version of the <a href="https://dotnet.microsoft.com/download">.NET SDK</a> to continue creating a Blazor project. If you don't have the SDK installed on your system please download and run the installer.</p>
<h2 id="creating-a-new-blazor-wasm-project">Creating a new Blazor WASM project</h2>
<p>There are two types of Blazor hosting models: <a href="https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-8.0#blazor-server">Blazor Server</a> which requires a server to serve the Blazor application to the end user, and <a href="https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-8.0#blazor-webassembly">Blazor WebAssembly</a> which runs in the browser. Blazor Server is incompatible with the Cloudflare edge network model, thus this guide only use Blazor WebAssembly.</p>
<p>Create a new Blazor WebAssembly (WASM) application by running the following command:</p>
<pre tabindex="0"><code class="language-sh">dotnet new blazorwasm -o my-blazor-project&#10;</code></pre>
<h2 id="create-the-build-script">Create the build script</h2>
<p>To deploy, Cloudflare Pages will need a way to build the Blazor project. In the project's directory root, create a <code>build.sh</code> file. Populate the file with this (updating the <code>.dotnet-install.sh</code> line appropriately if you're not using the latest .NET SDK):</p>
<pre tabindex="0"><code>&#35;!/bin/sh&#10;curl -sSL https://dot.net/v1/dotnet-install.sh &gt; dotnet-install.sh&#10;chmod +x dotnet-install.sh&#10;./dotnet-install.sh -c 8.0 -InstallDir ./dotnet&#10;./dotnet/dotnet --version&#10;./dotnet/dotnet publish -c Release -o output&#10;</code></pre>
<p>Your <code>build.sh</code> file needs to be executable for the build command to work. You can make it so by running <code>chmod +x build.sh</code>.</p>
<h2 id="before-you-continue">Before you continue</h2>
<p>All of the framework guides assume you already have a fundamental understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to this <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<p>If you clone with SSH, you must <a href="https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generate SSH keys</a> on each computer you use to push or pull from GitHub.</p>
<p>Refer to the <a href="https://guides.github.com/introduction/git-handbook/">GitHub documentation</a> and <a href="https://git-scm.com/book/en/v2">Git documentation</a> for more information.</p>
<h2 id="create-a-gitignore-file">Create a <code>.gitignore</code> file</h2>
<p>Creating a <code>.gitignore</code> file ensures that only what is needed gets pushed onto your GitHub repository. Create a <code>.gitignore</code> file by running the following command:</p>
<pre tabindex="0"><code class="language-sh">dotnet new gitignore&#10;</code></pre>
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
<td>Build command</td>
<td><code>./build.sh</code></td>
</tr>
<tr>
<td>Build directory</td>
<td><code>output/wwwroot</code></td>
</tr>
</tbody>
</table>
</div>
<p>After configuring your site, you can begin your first deploy. You should see Cloudflare Pages installing <code>dotnet</code>, your project dependencies, and building your site, before deploying it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11055.md")
</aside>
<p>After deploying your site, you will receive a unique subdomain for your project on <code>*.pages.dev</code>.
Every time you commit new code to your Blazor site, Cloudflare Pages will automatically rebuild your project and deploy it. You will also get access to <a href="/pages/configuration/preview-deployments/">preview deployments</a> on new pull requests, so you can preview how changes look to your site before deploying them to production.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="a-file-is-over-the-25-mib-limit">A file is over the 25 MiB limit</h3>
<p>If you receive the error message <code>Error: Asset &quot;/opt/buildhome/repo/output/wwwroot/_framework/dotnet.wasm&quot; is over the 25MiB limit</code>, resolve this by doing one of the following actions:</p>
<ol>
<li>Reduce the size of your assets with the following <a href="https://docs.microsoft.com/en-us/aspnet/core/blazor/performance?view=aspnetcore-6.0#minimize-app-download-size">guide</a>.</li>
</ol>
<p>Or</p>
<ol start="2">
<li>Remove the <code>*.wasm</code> files from the output (<code>rm output/wwwroot/_framework/*.wasm</code>) and modify your Blazor application to <a href="https://docs.microsoft.com/en-us/aspnet/core/blazor/host-and-deploy/webassembly?view=aspnetcore-6.0#compression">load the Brotli compressed files</a> instead.</li>
</ol>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your Blazor site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
