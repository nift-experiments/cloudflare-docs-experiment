---
cp9:
  canonical: https://developers.cloudflare.com/pages/framework-guides/deploy-a-zola-site/
  description: Deploy a Zola static site to Cloudflare Pages.
  full_title: Zola · Cloudflare Pages docs
  head_html: <title>Zola · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy a Zola static site to Cloudflare Pages."><link rel="canonical" href="https://developers.cloudflare.com/pages/framework-guides/deploy-a-zola-site/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/framework-guides/deploy-a-zola-site/index.md"><meta property="og:title" content="Zola · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy a Zola static site to Cloudflare Pages."><meta property="og:url" content="https://developers.cloudflare.com/pages/framework-guides/deploy-a-zola-site/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/framework-guides/deploy-a-zola-site/#page","headline":"Zola \u00b7 Cloudflare Pages docs","description":"Deploy a Zola static site to Cloudflare Pages.","url":"https://developers.cloudflare.com/pages/framework-guides/deploy-a-zola-site/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/framework-guides/deploy-a-zola-site/
  schema: 1
---
<p><a href="https://www.getzola.org/">Zola</a> is a fast static site generator in a single binary with everything built-in. In this guide, you will create a new Zola application and deploy it using Cloudflare Pages. You will use the <code>zola</code> CLI to create a new Zola site.</p>
<h2 id="installing-zola">Installing Zola</h2>
<p>First, <a href="https://www.getzola.org/documentation/getting-started/installation/">install</a> the <code>zola</code> CLI, using the specific instructions for your operating system below:</p>
<h3 id="macos-homebrew">macOS (Homebrew)</h3>
<p>If you use the package manager <a href="https://brew.sh">Homebrew</a>, run the <code>brew install</code> command in your terminal to install Zola:</p>
<pre tabindex="0"><code class="language-sh">brew install zola&#10;</code></pre>
<h3 id="windows-chocolatey">Windows (Chocolatey)</h3>
<p>If you use the package manager <a href="https://chocolatey.org/">Chocolatey</a>, run the <code>choco install</code> command in your terminal to install Zola:</p>
<pre tabindex="0"><code class="language-sh">choco install zola&#10;</code></pre>
<h3 id="windows-scoop">Windows (Scoop)</h3>
<p>If you use the package manager <a href="https://scoop.sh/">Scoop</a>, run the <code>scoop install</code> command in your terminal to install Zola:</p>
<pre tabindex="0"><code class="language-sh">scoop install zola&#10;</code></pre>
<h3 id="linux-pkg">Linux (pkg)</h3>
<p>Your Linux distro's package manager may include Zola. If this is the case, you can install it directly using your distro's package manager -- for example, using <code>pkg</code>, run the following command in your terminal:</p>
<pre tabindex="0"><code class="language-sh">pkg install zola&#10;</code></pre>
<p>If your package manager does not include Zola or you would like to download a release directly, refer to the <a href="/pages/framework-guides/deploy-a-zola-site/#manual-installation"><strong>Manual</strong></a> section below.</p>
<h3 id="manual-installation">Manual installation</h3>
<p>The Zola GitHub repository contains pre-built versions of the Zola command-line tool for various operating systems, which can be found on <a href="https://github.com/getzola/zola/releases">the Releases page</a>.</p>
<p>For more instruction on installing these releases, refer to <a href="https://www.getzola.org/documentation/getting-started/installation/">Zola's install guide</a>.</p>
<h2 id="creating-a-new-project">Creating a new project</h2>
<p>With Zola installed, create a new project by running the <code>zola init</code> command in your terminal using the default template:</p>
<pre tabindex="0"><code class="language-sh">zola init my-zola-project&#10;</code></pre>
<p>Upon running <code>zola init</code>, you will prompted with three questions:</p>
<ol>
<li>
<p>What is the URL of your site? (<a href="https://example.com">https://example.com</a>):
You can leave this one blank for now.</p>
</li>
<li>
<p>Do you want to enable Sass compilation? [Y/n]: Y</p>
</li>
<li>
<p>Do you want to enable syntax highlighting? [y/N]: y</p>
</li>
<li>
<p>Do you want to build a search index of the content? [y/N]: y</p>
</li>
</ol>
<h2 id="before-you-continue">Before you continue</h2>
<p>All of the framework guides assume you already have a fundamental understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to this <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<p>If you clone with SSH, you must <a href="https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generate SSH keys</a> on each computer you use to push or pull from GitHub.</p>
<p>Refer to the <a href="https://guides.github.com/introduction/git-handbook/">GitHub documentation</a> and <a href="https://git-scm.com/book/en/v2">Git documentation</a> for more information.</p>
<h2 id="create-a-github-repository">Create a GitHub repository</h2>
<p>Create a new GitHub repository by visiting <a href="https://repo.new">repo.new</a>. After creating a new repository, go to your newly created project directory to prepare and push your local application to GitHub by running the following commands in your terminal:</p>
<pre tabindex="0"><code class="language-sh">git remote add origin https://github.com/&lt;your-gh-username&gt;/&lt;repository-name&gt;&#10;git branch -M main&#10;git push -u origin main&#10;</code></pre>
<h2 id="deploy-with-cloudflare-pages">Deploy with Cloudflare Pages</h2>
<table><thead><tr><th>Configuration option</th><th>Value</th></tr></thead><tbody><tr><td>Production branch</td><td><code>main</code></td></tr><tr><td>Build command</td><td><code>zola build</code></td></tr><tr><td>Build directory</td><td><code>public</code></td></tr></tbody></table>
<p>Zola is preinstalled in the Cloudflare Pages build environment, so no additional configuration is required. You can optionally set the <code>ZOLA_VERSION</code> environment variable under <strong>Environment Variables (advanced)</strong> to pin a specific version.</p>
<p>For example, <code>ZOLA_VERSION</code>: <code>0.19.2</code>.</p>
<p>After configuring your site, you can begin your first deploy. You should see Cloudflare Pages building your site with Zola, before deploying it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11018.md")
</aside>
<p>After deploying your site, you will receive a unique subdomain for your project on <code>*.pages.dev</code>.</p>
<p>You can now add that subdomain as the <code>base_url</code> in your <code>config.toml</code> file.</p>
<p>For example:</p>
<pre tabindex="0"><code class="language-yaml">&#35; The URL the site will be built for&#10;base_url = &quot;https://my-zola-project.pages.dev&quot;&#10;</code></pre>
<p>Every time you commit new code to your Zola site, Cloudflare Pages will automatically rebuild your project and deploy it. You will also get access to <a href="/pages/configuration/preview-deployments/">preview deployments</a> on new pull requests, so you can preview how changes look to your site before deploying them to production.</p>
<h3 id="handling-preview-deployments">Handling Preview Deployments</h3>
<p>When working with Cloudflare Pages, you might use preview deployments for testing changes before merging to your main branch. However, these preview deployments use different URLs (like <code>https://your-branch-name.my-zola-project.pages.dev</code>), which can cause issues with asset loading if your <code>base_url</code> is hardcoded.</p>
<p>To fix this, modify your build command in the Cloudflare Pages configuration to dynamically set the base URL depending on the environment:</p>
<pre tabindex="0"><code class="language-sh">if [ &quot;$CF_PAGES_BRANCH&quot; = &quot;main&quot; ]; then zola build; else zola build --base-url $CF_PAGES_URL; fi&#10;</code></pre>
<p>This command uses:</p>
<ul>
<li>The <code>base_url</code> set in <code>config.toml</code> when building from the <code>main</code> branch</li>
<li>The preview deployment URL (automatically provided by Cloudflare Pages as <code>$CF_PAGES_URL</code>) for all other branches</li>
</ul>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your Zola site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
