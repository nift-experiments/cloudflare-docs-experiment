<p><a href="https://www.11ty.dev/">Eleventy</a> is a simple static site generator. In this guide, you will create a new Eleventy site and deploy it using Cloudflare Pages. You will be using the <code>eleventy</code> CLI to create a new Eleventy site.</p>
<h2 id="installing-eleventy">Installing Eleventy</h2>
<p>Install the <code>eleventy</code> CLI by running the following command in your terminal:</p>
<pre><code class="language-sh">npm install -g @11ty/eleventy&#10;</code></pre>
<h2 id="creating-a-new-project">Creating a new project</h2>
<p>There are a lot of <a href="https://www.11ty.dev/docs/starter/">starter projects</a> available on the Eleventy website. As an example, use the <code>eleventy-base-blog</code> project by running the following commands in your terminal:</p>
<pre><code class="language-sh">git clone https://github.com/11ty/eleventy-base-blog.git my-blog-name&#10;cd my-blog-name&#10;npm install&#10;</code></pre>
<h2 id="before-you-continue">Before you continue</h2>
<p>All of the framework guides assume you already have a fundamental understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to this <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<p>If you clone with SSH, you must <a href="https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generate SSH keys</a> on each computer you use to push or pull from GitHub.</p>
<p>Refer to the <a href="https://guides.github.com/introduction/git-handbook/">GitHub documentation</a> and <a href="https://git-scm.com/book/en/v2">Git documentation</a> for more information.</p>
<h2 id="creating-a-github-repository">Creating a GitHub repository</h2>
<p>Create a new GitHub repository by visiting <a href="https://repo.new">repo.new</a>. After creating a new repository, prepare and push your local application to GitHub by running the following command in your terminal:</p>
<pre><code class="language-sh">git remote set-url origin https://github.com/yourgithubusername/githubrepo&#10;git branch -M main&#10;git push -u origin main&#10;</code></pre>
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
6. In the **Build settings** section, select _Eleventy_ as your **Framework preset**. Your selection will provide the following information:
<table><thead><tr><th>Configuration option</th><th>Value</th></tr></thead><tbody><tr><td>Production branch</td><td><code>main</code></td></tr><tr><td>Build command</td><td><code>npx @11ty/eleventy</code></td></tr><tr><td>Build directory</td><td><code>_site</code></td></tr></tbody></table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11011.md")
</aside>
<p>After deploying your site, you will receive a unique subdomain for your project on <code>*.pages.dev</code>.
Every time you commit new code to your Eleventy site, Cloudflare Pages will automatically rebuild your project and deploy it. You will also get access to <a href="/pages/configuration/preview-deployments/">preview deployments</a> on new pull requests, so you can preview how changes look to your site before deploying them to production.</p>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your Eleventy site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
