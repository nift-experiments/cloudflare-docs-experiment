<p><a href="https://jekyllrb.com/">Jekyll</a> is an open-source framework for creating websites, based around Markdown with Liquid templates. In this guide, you will create a new Jekyll application and deploy it using Cloudflare Pages. You use the <code>jekyll</code> CLI to create a new Jekyll site.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11043.md")
</aside>
<h2 id="installing-jekyll">Installing Jekyll</h2>
<p>Jekyll is written in Ruby, meaning that you will need a functioning Ruby installation, like <code>rbenv</code>, to install Jekyll.</p>
<p>To install Ruby on your computer, follow the <a href="https://github.com/rbenv/rbenv#installation"><code>rbenv</code> installation instructions</a> and select a recent version of Ruby by running the <code>rbenv</code> command in your terminal. The Ruby version you install will also be used to configure the Pages deployment for your application.</p>
<pre><code class="language-sh">rbenv install &lt;RUBY_VERSION&gt; # For example, 3.1.3&#10;</code></pre>
<p>With Ruby installed, you can install the <code>jekyll</code> Ruby gem:</p>
<pre><code class="language-sh">gem install jekyll&#10;</code></pre>
<h2 id="creating-a-new-project">Creating a new project</h2>
<p>With Jekyll installed, you can create a new project running the <code>jekyll new</code> in your terminal:</p>
<pre><code class="language-sh">jekyll new my-jekyll-site&#10;</code></pre>
<p>Create a base <code>index.html</code> in your newly created folder to give your site content:</p>
<pre><code class="language-html">&lt;!doctype html&gt;&#10;&lt;html&gt;&#10;	&lt;head&gt;&#10;		&lt;meta charset=&quot;utf-8&quot; /&gt;&#10;		&lt;title&gt;Hello from Cloudflare Pages&lt;/title&gt;&#10;	&lt;/head&gt;&#10;	&lt;body&gt;&#10;		&lt;h1&gt;Hello from Cloudflare Pages&lt;/h1&gt;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<p>Optionally, you may use a theme with your new Jekyll site if you would like to start with great styling defaults. For example, the <a href="https://github.com/mmistakes/minimal-mistakes"><code>minimal-mistakes</code></a> theme has a <a href="https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/#starting-from-jekyll-new">&quot;Starting from <code>jekyll new</code>&quot;</a> section to help you add the theme to your new site.</p>
<h2 id="before-you-continue">Before you continue</h2>
<p>All of the framework guides assume you already have a fundamental understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to this <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<p>If you clone with SSH, you must <a href="https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generate SSH keys</a> on each computer you use to push or pull from GitHub.</p>
<p>Refer to the <a href="https://guides.github.com/introduction/git-handbook/">GitHub documentation</a> and <a href="https://git-scm.com/book/en/v2">Git documentation</a> for more information.</p>
<h2 id="create-a-github-repository">Create a GitHub repository</h2>
<p>Create a new GitHub repository by visiting <a href="https://repo.new">repo.new</a>. After creating a new repository, go to your newly created project directory to prepare and push your local application to GitHub by running the following commands in your terminal:</p>
<pre><code class="language-sh">git remote add origin https://github.com/&lt;your-gh-username&gt;/&lt;repository-name&gt;&#10;git branch -M main&#10;git push -u origin main&#10;</code></pre>
<p>If you are migrating an existing Jekyll project to Pages, confirm that your <code>Gemfile</code> is committed as part of your codebase. Pages will look at your Gemfile and run <code>bundle install</code> to install the required dependencies for your project, including the <code>jekyll</code> gem.</p>
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
<table><thead><tr><th>Configuration option</th><th>Value</th></tr></thead><tbody><tr><td>Production branch</td><td><code>main</code></td></tr><tr><td>Build command</td><td><code>jekyll build</code></td></tr><tr><td>Build directory</td><td><code>_site</code></td></tr></tbody></table>
<p>Add an <a href="/pages/configuration/build-image/">environment variable</a> that matches the Ruby version that you are using locally. Set this as <code>RUBY_VERSION</code> on both your preview and production deployments. Below, <code>3.1.3</code> is used as an example:</p>
<table>
<thead>
<tr>
<th>Environment variable</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>RUBY_VERSION</code></td>
<td><code>3.1.3</code></td>
</tr>
</tbody>
</table>
<p>After configuring your site, you can begin your first deployment. You should see Cloudflare Pages installing <code>jekyll</code>, your project dependencies, and building your site before deploying it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11042.md")
</aside>
<p>After deploying your site, you will receive a unique subdomain for your project on <code>*.pages.dev</code>.
Every time you commit new code to your Jekyll site, Cloudflare Pages will automatically rebuild your project and deploy it. You will also get access to <a href="/pages/configuration/preview-deployments/">preview deployments</a> on new pull requests, so you can preview how changes look to your site before deploying them to production.</p>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your Jekyll site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
