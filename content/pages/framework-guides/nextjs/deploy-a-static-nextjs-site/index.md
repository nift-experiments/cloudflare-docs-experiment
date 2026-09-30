<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11087.md")
</aside>
<p><a href="https://nextjs.org">Next.js</a> is an open-source React framework for creating websites and applications. In this guide, you will create a static Next.js application and deploy it using Cloudflare Pages.</p>
<p>This guide will instruct you how to deploy a static site Next.js project with <a href="https://nextjs.org/docs/app/building-your-application/deploying/static-exports">static exports</a>.</p>
<h2 id="before-you-continue">Before you continue</h2>
<p>All of the framework guides assume you already have a fundamental understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to this <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<p>If you clone with SSH, you must <a href="https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generate SSH keys</a> on each computer you use to push or pull from GitHub.</p>
<p>Refer to the <a href="https://guides.github.com/introduction/git-handbook/">GitHub documentation</a> and <a href="https://git-scm.com/book/en/v2">Git documentation</a> for more information.</p>
<h2 id="select-your-next-js-project">Select your Next.js project</h2>
<p>If you already have a Next.js project that you wish to deploy, ensure that it is <a href="https://nextjs.org/docs/app/building-your-application/deploying/static-exports">configured for static exports</a>, change to its directory, and proceed to the next step. Otherwise, use <code>create-next-app</code> to create a new Next.js project.</p>
<pre><code class="language-sh">npx create-next-app --example with-static-export my-app&#10;</code></pre>
<p>After creating your project, a new <code>my-app</code> directory will be generated using the official <a href="https://github.com/vercel/next.js/tree/canary/examples/with-static-export"><code>with-static-export</code></a> example as a template. Change to this directory to continue.</p>
<pre><code class="language-sh">cd my-app&#10;</code></pre>
<h3 id="create-a-github-repository">Create a GitHub repository</h3>
<p>Create a new GitHub repository by visiting <a href="https://repo.new">repo.new</a>. After creating a new repository, prepare and push your local application to GitHub by running the following commands in your terminal:</p>
<pre><code class="language-sh">git remote add origin https://github.com/&lt;GH_USERNAME&gt;/&lt;REPOSITORY_NAME&gt;.git&#10;git branch -M main&#10;git push -u origin main&#10;</code></pre>
<h3 id="deploy-your-application-to-cloudflare-pages">Deploy your application to Cloudflare Pages</h3>
<p>To deploy your site to Pages:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Create application**.
3. Select the **Pages** tab.
4. Select **Import an existing Git repository**.
5. Select the new GitHub repository that you created and then select **Begin setup**.
6. In the **Build settings** section, select _Next.js (Static HTML Export)_ as your **Framework preset**. Your selection will provide the following information:
<table><thead><tr><th>Configuration option</th><th>Value</th></tr></thead><tbody><tr><td>Production branch</td><td><code>main</code></td></tr><tr><td>Build command</td><td><code>npx next build</code></td></tr><tr><td>Build directory</td><td><code>out</code></td></tr></tbody></table>
<p>After configuring your site, you can begin your first deploy. Cloudflare Pages will install <code>next</code>, your project dependencies, and build your site before deploying it.</p>
<h2 id="preview-your-site">Preview your site</h2>
<p>After deploying your site, you will receive a unique subdomain for your project on <code>*.pages.dev</code>.</p>
<p>Every time you commit new code to your Next.js site, Cloudflare Pages will automatically rebuild your project and deploy it. You will also get access to <a href="/pages/configuration/preview-deployments/">preview deployments</a> on new pull requests, so you can preview how changes look to your site before deploying them to production.</p>
<p>For the complete guide to deploying your first site to Cloudflare Pages, refer to the <a href="/pages/get-started/">Get started guide</a>.</p>
