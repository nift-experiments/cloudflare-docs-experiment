<p><a href="https://vitepress.dev/">VitePress</a> is a <a href="https://en.wikipedia.org/wiki/Static_site_generator">static site generator</a> (SSG) designed for building fast, content-centric websites. VitePress takes your source content written in <a href="https://en.wikipedia.org/wiki/Markdown">Markdown</a>, applies a theme to it, and generates static HTML pages that can be easily deployed anywhere.</p>
<p>In this guide, you will create a new VitePress project and deploy it using Cloudflare Pages.</p>
<h2 id="set-up-a-new-project">Set up a new project</h2>
<p>VitePress ships with a command line setup wizard that will help you scaffold a basic project.</p>
<p>Run the following command in your terminal to create a new VitePress project:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx vitepress@latest init</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx vitepress@latest init" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn dlx vitepress@latest init</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn dlx vitepress@latest init" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpx vitepress@latest init</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpx vitepress@latest init" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Amongst other questions, the setup wizard will ask you in which directory to save your new project, make sure
to be in the project's directory and then install the <code>vitepress</code> dependency with the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i vitepress@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i vitepress@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add vitepress@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add vitepress@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add vitepress@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add vitepress@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add vitepress@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add vitepress@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11021.md")
</aside>
<p>Finally create a <code>.gitignore</code> file with the following content:</p>
<pre><code>node_modules&#10;.vitepress/cache&#10;.vitepress/dist&#10;</code></pre>
<p>This step makes sure that unnecessary files are not going to be included in the project's git repository (which we will set up next).</p>
<h2 id="before-you-continue">Before you continue</h2>
<p>All of the framework guides assume you already have a fundamental understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to this <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<p>If you clone with SSH, you must <a href="https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generate SSH keys</a> on each computer you use to push or pull from GitHub.</p>
<p>Refer to the <a href="https://guides.github.com/introduction/git-handbook/">GitHub documentation</a> and <a href="https://git-scm.com/book/en/v2">Git documentation</a> for more information.</p>
<h2 id="create-a-github-repository">Create a GitHub repository</h2>
<p>Create a new GitHub repository by visiting <a href="https://repo.new">repo.new</a>. After creating a new repository, go to your newly created project directory to prepare and push your local application to GitHub by running the following commands in your terminal:</p>
<pre><code class="language-sh">git init&#10;git remote add origin https://github.com/&lt;your-gh-username&gt;/&lt;repository-name&gt;&#10;git add .&#10;git commit -m &quot;Initial commit&quot;&#10;git branch -M main&#10;git push -u origin main&#10;</code></pre>
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
6. In the **Build settings** section, select _VitePress_ as your **Framework preset**. Your selection will provide the following information:
<table><thead><tr><th>Configuration option</th><th>Value</th></tr></thead><tbody><tr><td>Production branch</td><td><code>main</code></td></tr><tr><td>Build command</td><td><code>npx vitepress build</code></td></tr><tr><td>Build directory</td><td><code>.vitepress/dist</code></td></tr></tbody></table>
<p>After configuring your site, you can begin your first deploy. Cloudflare Pages will install <code>vitepress</code>, your project dependencies, and build your site, before deploying it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11020.md")
</aside>
<p>After deploying your site, you will receive a unique subdomain for your project on <code>*.pages.dev</code>. Every time you commit and push new code to your VitePress project, Cloudflare Pages will automatically rebuild your project and deploy it. You will also get access to <a href="/pages/configuration/preview-deployments/">preview deployments</a> on new pull requests, so you can preview how changes to your site look before deploying them to production.</p>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your VitePress site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
