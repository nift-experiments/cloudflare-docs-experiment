<p><a href="https://preactjs.com">Preact</a> is a popular, open-source framework for building modern web applications. Preact can also be used as a lightweight alternative to React because the two share the same API and component model.</p>
<p>In this guide, you will create a new Preact application and deploy it using Cloudflare Pages.
You will use <a href="https://github.com/preactjs/create-preact"><code>create-preact</code></a>, a lightweight project scaffolding tool to set up a new Preact app in seconds.</p>
<h2 id="setting-up-a-new-project">Setting up a new project</h2>
<p>Create a new project by running the <a href="https://docs.npmjs.com/cli/v6/commands/npm-init"><code>npm init</code></a> command in your terminal, giving it a title:</p>
<pre><code class="language-sh">npm init preact&#10;cd your-project-name&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11035.md")
</aside>
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
<p>Optionally, you can customize the <strong>Project name</strong> field. It defaults to the GitHub repository's name, but it does not need to match. The <strong>Project name</strong> value is assigned as your <code>*.pages.dev</code> subdomain.</p>
<p>After completing configuration, select <strong>Save and Deploy</strong>.</p>
<p>You will see your first deploy pipeline in progress. Pages installs all dependencies and builds the project as specified.</p>
<p>After you have deployed your site, you will receive a unique subdomain for your project on <code>*.pages.dev</code>.</p>
<p>Cloudflare Pages will automatically rebuild your project and deploy it on every new pushed commit.</p>
<p>Additionally, you will have access to <a href="/pages/configuration/preview-deployments/">preview deployments</a>, which repeat the build-and-deploy process for pull requests. With these, you can preview changes to your project with a real URL before deploying them to production.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11034.md")
</aside>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your Preact site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
