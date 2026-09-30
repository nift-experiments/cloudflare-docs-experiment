<p><a href="https://www.solidjs.com/">Solid</a> is an open-source web application framework focused on generating performant applications with a modern developer experience based on JSX.</p>
<p>In this guide, you will create a new Solid application implemented via <a href="https://start.solidjs.com/getting-started/what-is-solidstart">SolidStart</a> (Solid's meta-framework) and deploy it using Cloudflare Pages.</p>
<h2 id="create-a-new-project">Create a new project</h2>
<p>Use the <a href="https://www.npmjs.com/package/create-cloudflare"><code>create-cloudflare</code></a> CLI (C3) to set up a new project. C3 will create a new project directory, initiate Solid's official setup tool, and provide the option to deploy instantly.</p>
<p>To use <code>create-cloudflare</code> to create a new Solid project, run the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- my-solid-app --framework=solid</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-solid-app --framework=solid" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare my-solid-app --framework=solid</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-solid-app --framework=solid" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest my-solid-app --framework=solid</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-solid-app --framework=solid" aria-label="Copy to clipboard">Copy</button></div></div>
<p>You will be prompted to select a starter. Choose any of the available options. You will then be asked if you want to enable Server Side Rendering. Reply <code>yes</code>. Finally, you will be asked if you want to use TypeScript, choose either <code>yes</code> or <code>no</code>.</p>
<p><code>create-cloudflare</code> will then install dependencies, including the <a href="/workers/wrangler/install-and-update/#check-your-wrangler-version">Wrangler</a> CLI and the SolidStart Cloudflare Pages adapter, and ask you setup questions.</p>
<p>After you have installed your project dependencies, start your application:</p>
<pre><code class="language-sh">npm run dev&#10;</code></pre>
<h2 id="solidstart-cloudflare-configuration">SolidStart Cloudflare configuration</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11030.md")
</aside>
<p>In order to configure SolidStart so that it can be deployed to Cloudflare pages, update its config file like so:</p>
<pre><code class="language-diff">import { defineConfig } from &quot;@solidjs/start/config&quot;;&#10;&#10;export default defineConfig({&#10;&#43;  server: {&#10;&#43;    preset: &quot;cloudflare-pages&quot;,&#10;&#10;&#43;    rollupConfig: {&#10;&#43;      external: [&quot;node:async_hooks&quot;]&#10;&#43;    }&#10;&#43;  }&#10;});&#10;</code></pre>
<h2 id="before-you-continue">Before you continue</h2>
<p>All of the framework guides assume you already have a fundamental understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to this <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<p>If you clone with SSH, you must <a href="https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generate SSH keys</a> on each computer you use to push or pull from GitHub.</p>
<p>Refer to the <a href="https://guides.github.com/introduction/git-handbook/">GitHub documentation</a> and <a href="https://git-scm.com/book/en/v2">Git documentation</a> for more information.</p>
<h2 id="create-a-github-repository">Create a GitHub repository</h2>
<p>Create a new GitHub repository by visiting <a href="https://repo.new">repo.new</a>. After creating a new repository, go to your newly created project directory to prepare and push your local application to GitHub by running the following commands in your terminal:</p>
<pre><code class="language-sh">git init&#10;git remote add origin https://github.com/&lt;your-gh-username&gt;/&lt;repository-name&gt;&#10;git add .&#10;git commit -m &quot;Initial commit&quot;&#10;git branch -M main&#10;git push -u origin main&#10;</code></pre>
<h2 id="deploy-with-cloudflare-pages">Deploy with Cloudflare Pages</h2>
<h3 id="deploy-via-the-create-cloudflare-cli-c3">Deploy via the <code>create-cloudflare</code> CLI (C3)</h3>
<p>If you use <a href="https://www.npmjs.com/package/create-cloudflare"><code>create-cloudflare</code>(C3)</a> to create your new Solid project, C3 will install all dependencies needed for your project and prompt you to deploy your project via the CLI. If you deploy, your site will be live and you will be provided with a deployment URL.</p>
<h3 id="deploy-via-the-cloudflare-dashboard">Deploy via the Cloudflare dashboard</h3>
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
<p>After configuring your site, you can begin your first deploy. You should see Cloudflare Pages installing <code>npm</code>, your project dependencies, and building your site before deploying it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11029.md")
</aside>
<p>After deploying your site, you will receive a unique subdomain for your project on <code>*.pages.dev</code>.
Every time you commit new code to your Solid repository, Cloudflare Pages will automatically rebuild your project and deploy it. You will also get access to <a href="/pages/configuration/preview-deployments/">preview deployments</a> on new pull requests, to preview how changes look to your site before deploying them to production.</p>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your Solid site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
