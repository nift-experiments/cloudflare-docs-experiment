<p><a href="https://www.gatsbyjs.com/">Gatsby</a> is an open-source React framework for creating websites and apps. In this guide, you will create a new Gatsby application and deploy it using Cloudflare Pages. You will be using the <code>gatsby</code> CLI to create a new Gatsby site.</p>
<h2 id="install-gatsby">Install Gatsby</h2>
<p>Install the <code>gatsby</code> CLI by running the following command in your terminal:</p>
<pre><code class="language-sh">npm install -g gatsby-cli&#10;</code></pre>
<h2 id="create-a-new-project">Create a new project</h2>
<p>With Gatsby installed, you can create a new project using <code>gatsby new</code>. The <code>new</code> command accepts a GitHub URL for using an existing template. As an example, use the <code>gatsby-starter-lumen</code> template by running the following command in your terminal. You can find more in <a href="https://www.gatsbyjs.com/starters/?v=2">Gatsby's Starters section</a>:</p>
<pre><code class="language-sh">npx gatsby new my-gatsby-site https://github.com/alxshelepenok/gatsby-starter-lumen&#10;</code></pre>
<h2 id="before-you-continue">Before you continue</h2>
<p>All of the framework guides assume you already have a fundamental understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to this <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<p>If you clone with SSH, you must <a href="https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generate SSH keys</a> on each computer you use to push or pull from GitHub.</p>
<p>Refer to the <a href="https://guides.github.com/introduction/git-handbook/">GitHub documentation</a> and <a href="https://git-scm.com/book/en/v2">Git documentation</a> for more information.</p>
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
6. In the **Build settings** section, select _Gatsby_ as your **Framework preset**. Your selection will provide the following information:
<table><thead><tr><th>Configuration option</th><th>Value</th></tr></thead><tbody><tr><td>Production branch</td><td><code>main</code></td></tr><tr><td>Build command</td><td><code>npx gatsby build</code></td></tr><tr><td>Build directory</td><td><code>public</code></td></tr></tbody></table>
<p>After configuring your site, you can begin your first deploy. You should see Cloudflare Pages installing <code>gatsby</code>, your project dependencies, and building your site, before deploying it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11054.md")
</aside>
<p>After deploying your site, you will receive a unique subdomain for your project on <code>*.pages.dev</code>.
Every time you commit new code to your Gatsby site, Cloudflare Pages will automatically rebuild your project and deploy it. You will also get access to <a href="/pages/configuration/preview-deployments/">preview deployments</a> on new pull requests, so you can preview how changes look to your site before deploying them to production.</p>
<h2 id="dynamic-routes">Dynamic routes</h2>
<p>If you are using <a href="https://www.gatsbyjs.com/docs/reference/functions/routing/#dynamic-routing">dynamic routes</a> in your Gatsby project, set up a <a href="/pages/configuration/redirects/#proxying">proxy redirect</a> for these routes to take effect.</p>
<p>If you have a dynamic route, such as <code>/users/[id]</code>, create your proxy redirect by referring to the following example:</p>
<pre><code>/users/* /users/:id 200&#10;</code></pre>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your Gatsby site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
