<p><a href="https://gohugo.io/">Hugo</a> is a tool for generating static sites, written in Go. It is incredibly fast and has great high-level, flexible primitives for managing your content using different <a href="https://gohugo.io/content-management/formats/">content formats</a>.</p>
<p>In this guide, you will create a new Hugo application and deploy it using Cloudflare Pages. You will use the <code>hugo</code> CLI to create a new Hugo site.</p>
<h2 id="before-you-continue">Before you continue</h2>
<p>All of the framework guides assume you already have a fundamental understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to this <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<p>If you clone with SSH, you must <a href="https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generate SSH keys</a> on each computer you use to push or pull from GitHub.</p>
<p>Refer to the <a href="https://guides.github.com/introduction/git-handbook/">GitHub documentation</a> and <a href="https://git-scm.com/book/en/v2">Git documentation</a> for more information.</p>
<p>Go to <a href="#deploy-with-cloudflare-pages">Deploy with Cloudflare Pages</a> if you already have a Hugo site hosted with your <a href="/pages/get-started/git-integration/">Git provider</a>.</p>
<h2 id="install-hugo">Install Hugo</h2>
<p>Install the Hugo CLI, using the specific instructions for your operating system.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11050.md")
</div></div>
<h3 id="manual-installation">Manual installation</h3>
<p>The Hugo GitHub repository contains pre-built versions of the Hugo command-line tool for various operating systems, which can be found on <a href="https://github.com/gohugoio/hugo/releases">the Releases page</a>.</p>
<p>For more instruction on installing these releases, refer to <a href="https://gohugo.io/getting-started/installing/">Hugo's documentation</a>.</p>
<h2 id="create-a-new-project">Create a new project</h2>
<p>With Hugo installed, refer to <a href="https://gohugo.io/getting-started/quick-start/">Hugo's Quick Start</a> to create your project or create a new project by running the <code>hugo new</code> command in your terminal:</p>
<pre><code class="language-sh">hugo new site my-hugo-site&#10;</code></pre>
<p>Hugo sites use themes to customize the look and feel of the statically built HTML site. There are a number of themes available at <a href="https://themes.gohugo.io">themes.gohugo.io</a> — for now, use the <a href="https://themes.gohugo.io/themes/gohugo-theme-ananke/">Ananke theme</a> by running the following commands in your terminal:</p>
<pre><code class="language-sh">cd my-hugo-site&#10;git init&#10;git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke&#10;echo &quot;theme = &#x27;ananke&#x27;&quot; &gt;&gt; hugo.toml&#10;</code></pre>
<h2 id="create-a-post">Create a post</h2>
<p>Create a new post to give your Hugo site some initial content. Run the <code>hugo new</code> command in your terminal to generate a new post:</p>
<pre><code class="language-sh">hugo new content posts/hello-world.md&#10;</code></pre>
<p>Inside of <code>hello-world.md</code>, add some initial content to create your post. Remove the <code>draft</code> line in your post's frontmatter when you are ready to publish the post. Any posts with <code>draft: true</code> set will be skipped by Hugo's build process.</p>
<h2 id="create-a-github-repository">Create a GitHub repository</h2>
<p>Create a new GitHub repository by visiting <a href="https://repo.new">repo.new</a>. After creating a new repository, go to your newly created project directory to prepare and push your local application to GitHub by running the following commands in your terminal:</p>
<pre><code class="language-sh">git remote add origin https://github.com/&lt;your-gh-username&gt;/&lt;repository-name&gt;&#10;git branch -M main&#10;git push -u origin main&#10;</code></pre>
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
<table><thead><tr><th>Configuration option</th><th>Value</th></tr></thead><tbody><tr><td>Production branch</td><td><code>main</code></td></tr><tr><td>Build command</td><td><code>hugo</code></td></tr><tr><td>Build directory</td><td><code>public</code></td></tr></tbody></table>
<p>While <code>public</code> is the default build directory for Hugo sites, this setting can be configured with the <a href="https://gohugo.io/configuration/all/#publishdir"><code>publishDir</code> setting</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="base-url-configuration">Base URL configuration</h3>
@markup("md", "content/.markup/bodies/11046.md")
</aside>
<p>After completing deployment configuration, select the <strong>Save and Deploy</strong>. You should see Cloudflare Pages installing <code>hugo</code> and your project dependencies, and building your site, before deploying it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11045.md")
</aside>
<p>After deploying your site, you will receive a unique subdomain for your project on <code>*.pages.dev</code>.
Every time you commit new code to your Hugo site, Cloudflare Pages will automatically rebuild your project and deploy it. You will also get access to <a href="/pages/configuration/preview-deployments/">preview deployments</a> on new pull requests, so you can preview how changes look to your site before deploying them to production.</p>
<h2 id="use-a-specific-or-newer-hugo-version">Use a specific or newer Hugo version</h2>
<p>To use a <a href="https://github.com/gohugoio/hugo/releases">specific or newer version of Hugo</a>, create the <code>HUGO_VERSION</code> environment variable in your Pages project &gt; <strong>Settings</strong> &gt; <strong>Environment variables</strong>. Set the value as the Hugo version you want to specify (see the <a href="https://gohugo.io/getting-started/quick-start/#prerequisites">Prerequisites</a> for the minimum recommended version).</p>
<p>For example, <code>HUGO_VERSION</code>: <code>0.128.0</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11044.md")
</aside>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your Hugo site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
