<p><a href="https://hexo.io/">Hexo</a> is a tool for generating static websites, powered by Node.js. Hexo's benefits include speed, simplicity, and flexibility, allowing it to render Markdown files into static web pages via Node.js.</p>
<p>In this guide, you will create a new Hexo application and deploy it using Cloudflare Pages. You will use the <code>hexo</code> CLI to create a new Hexo site.</p>
<h2 id="installing-hexo">Installing Hexo</h2>
<p>First, install the Hexo CLI with <code>npm</code> or <code>yarn</code> by running either of the following commands in your terminal:</p>
<pre><code class="language-sh">npm install hexo-cli -g&#10;&#35; or&#10;yarn global add hexo-cli&#10;</code></pre>
<p>On macOS and Linux, you can install with <a href="https://brew.sh/">brew</a>:</p>
<pre><code class="language-sh">brew install hexo&#10;</code></pre>
<h2 id="before-you-continue">Before you continue</h2>
<p>All of the framework guides assume you already have a fundamental understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to this <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<p>If you clone with SSH, you must <a href="https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generate SSH keys</a> on each computer you use to push or pull from GitHub.</p>
<p>Refer to the <a href="https://guides.github.com/introduction/git-handbook/">GitHub documentation</a> and <a href="https://git-scm.com/book/en/v2">Git documentation</a> for more information.</p>
<h2 id="creating-a-new-project">Creating a new project</h2>
<p>With Hexo CLI installed, create a new project by running the <code>hexo init</code> command in your terminal:</p>
<pre><code class="language-sh">hexo init my-hexo-site&#10;cd my-hexo-site&#10;</code></pre>
<p>Hexo sites use themes to customize the appearance of statically built HTML sites. Hexo has a default theme automatically installed, which you can find on <a href="https://hexo.io/themes/">Hexo's Themes page</a>.</p>
<h2 id="creating-a-post">Creating a post</h2>
<p>Create a new post to give your Hexo site some initial content. Run the <code>hexo new</code> command in your terminal to generate a new post:</p>
<pre><code class="language-sh">hexo new &quot;hello hexo&quot;&#10;</code></pre>
<p>Inside of <code>hello-hexo.md</code>, use Markdown to write the content of the article. You can customize the tags, categories or other variables in the article. Refer to the <a href="https://hexo.io/docs/front-matter">Front Matter section</a> of the <a href="https://hexo.io/docs/">Hexo documentation</a> for more information.</p>
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
<td><code>public</code></td>
</tr>
</tbody>
</table>
</div>
<p>After completing configuration, click the <strong>Save and Deploy</strong> button. You should see Cloudflare Pages installing <code>hexo</code> and your project dependencies, and building your site, before deploying it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11052.md")
</aside>
<p>After deploying your site, you will receive a unique subdomain for your project on <code>*.pages.dev</code>.
Every time you commit new code to your Hexo site, Cloudflare Pages will automatically rebuild your project and deploy it. You will also get access to <a href="/pages/configuration/preview-deployments/">preview deployments</a> on new pull requests, so you can preview how changes look to your site before deploying them to production.</p>
<h2 id="using-a-specific-node-js-version">Using a specific Node.js version</h2>
<p>Some Hexo themes or plugins have additional requirements for different Node.js versions. To use a specific Node.js version for Hexo:</p>
<ol>
<li>Go to your Pages project.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Environment variables</strong>.</li>
<li>Set the environment variable <code>NODE_VERSION</code> and a value of your required Node.js version (for example, <code>14.3</code>).</li>
</ol>
<p><img src="/assets/upstream/images/pages/framework-guides/node-version-pages.png" alt="Follow the instructions above to set up an environment variable in the Pages dashboard" /></p>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your Hexo site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
