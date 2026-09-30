<p><a href="https://www.mkdocs.org/">MkDocs</a> is a modern documentation platform where teams can document products, internal knowledge bases and APIs.</p>
<h2 id="install-mkdocs">Install MkDocs</h2>
<p>MkDocs requires a recent version of Python and the Python package manager, pip, to be installed on your system. To install pip, refer to the <a href="https://www.mkdocs.org/user-guide/installation/">MkDocs Installation guide</a>. With pip installed, run:</p>
<pre><code class="language-sh">pip install mkdocs&#10;</code></pre>
<h2 id="create-an-mkdocs-project">Create an MkDocs project</h2>
<p>Use the <code>mkdocs new</code> command to create a new application:</p>
<pre><code class="language-sh">mkdocs new &lt;PROJECT_NAME&gt;&#10;</code></pre>
<p>Then <code>cd</code> into your project, take MkDocs and its dependencies and put them into a <code>requirements.txt</code> file:</p>
<pre><code class="language-sh">pip freeze &gt; requirements.txt&#10;</code></pre>
<h2 id="before-you-continue">Before you continue</h2>
<p>All of the framework guides assume you already have a fundamental understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to this <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<p>If you clone with SSH, you must <a href="https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generate SSH keys</a> on each computer you use to push or pull from GitHub.</p>
<p>Refer to the <a href="https://guides.github.com/introduction/git-handbook/">GitHub documentation</a> and <a href="https://git-scm.com/book/en/v2">Git documentation</a> for more information.</p>
<h2 id="create-a-github-repository">Create a GitHub repository</h2>
<p>Create a new GitHub repository by visiting <a href="https://repo.new">repo.new</a>. After creating a new repository, go to your newly created project directory to prepare and push your local application to GitHub by running the following commands in your terminal:</p>
<pre><code class="language-sh">git init&#10;git remote add origin https://github.com/&lt;your-gh-username&gt;/&lt;repository-name&gt;&#10;git add .&#10;git commit -m &quot;Initial commit&quot;&#10;git branch -M main&#10;git push -u origin main&#10;</code></pre>
<p>You have successfully created a GitHub repository and pushed your MkDocs project to that repository.</p>
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
<table><thead><tr><th>Configuration option</th><th>Value</th></tr></thead><tbody><tr><td>Production branch</td><td><code>main</code></td></tr><tr><td>Build command</td><td><code>mkdocs build</code></td></tr><tr><td>Build directory</td><td><code>site</code></td></tr></tbody></table>
<ol start="7">
<li>Go to <strong>Environment variables (advanced)</strong> &gt; <strong>Add variable</strong> &gt; and add the variable <code>PYTHON_VERSION</code> with a value of <code>3.7</code>.</li>
</ol>
<p>After deploying your site, you will receive a unique subdomain for your project on <code>*.pages.dev</code>.</p>
<p>Every time you commit new code to your MkDocs site, Cloudflare Pages will automatically rebuild your project and deploy it. You will also get access to <a href="/pages/configuration/preview-deployments/">preview deployments</a> on new pull requests and be able to preview how changes to your site look before deploying them to production.</p>
<p>For the complete guide to deploying your first site to Cloudflare Pages, refer to the <a href="/pages/get-started/">Get started guide</a>.</p>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your MkDocs site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
