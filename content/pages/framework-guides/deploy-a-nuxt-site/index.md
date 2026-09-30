<p><a href="https://nuxt.com">Nuxt</a> is a web framework making Vue.js-based development simple and powerful.</p>
<p>In this guide, you will create a new Nuxt application and deploy it using Cloudflare Pages.</p>
<h3 id="video-tutorial">Video Tutorial</h3>
<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/er5PXTI9rXo" title="YouTube video" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h2 id="create-a-new-project-using-the-create-cloudflare-cli-c3">Create a new project using the <code>create-cloudflare</code> CLI (C3)</h2>
<p>The <a href="/pages/get-started/c3/"><code>create-cloudflare</code> CLI (C3)</a> will configure your Nuxt site for Cloudflare Pages. Run the following command in your terminal to create a new Nuxt site:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- my-nuxt-app --framework=nuxt --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-nuxt-app --framework=nuxt --platform=pages" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare my-nuxt-app --framework=nuxt --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-nuxt-app --framework=nuxt --platform=pages" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest my-nuxt-app --framework=nuxt --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-nuxt-app --framework=nuxt --platform=pages" aria-label="Copy to clipboard">Copy</button></div></div>
<p>C3 will ask you a series of setup questions and create a new project with <a href="https://github.com/nuxt/cli"><code>nuxi</code> (the official Nuxt CLI)</a>. C3 will also install the necessary adapters along with the <a href="/workers/wrangler/install-and-update/#check-your-wrangler-version">Wrangler CLI</a>.</p>
<p>After creating your project, C3 will generate a new <code>my-nuxt-app</code> directory using the default Nuxt template, updated to be fully compatible with Cloudflare Pages.</p>
<p>When creating your new project, C3 will give you the option of deploying an initial version of your application via <a href="/pages/how-to/use-direct-upload-with-continuous-integration/">Direct Upload</a>. You can redeploy your application at any time by running following command inside your project directory:</p>
<pre><code class="language-sh">npm run deploy&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="git-integration">Git integration</h3>
@markup("md", "content/.markup/bodies/11038.md")
</aside>
<h2 id="configure-and-deploy-a-project-without-c3">Configure and deploy a project without C3</h2>
<p>To deploy a Nuxt project without C3, follow the <a href="https://nuxt.com/docs/getting-started/installation">Nuxt Get Started guide</a>. After you have set up your Nuxt project, choose either the <a href="/pages/get-started/git-integration/">Git integration guide</a> or <a href="/pages/get-started/direct-upload/">Direct Upload guide</a> to deploy your Nuxt project on Cloudflare Pages.</p>
<h2 id="git-integration-1">Git integration</h2>
<p>In addition to <a href="/pages/get-started/direct-upload/">Direct Upload</a> deployments, you can deploy projects via <a href="/pages/configuration/git-integration">Git integration</a>. Git integration allows you to connect a GitHub or GitLab repository to your Pages application and have your Pages application automatically built and deployed after each new commit is pushed to it.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="git-integration-2">Git integration</h3>
@markup("md", "content/.markup/bodies/11037.md")
</aside>
<p>Setup requires a basic understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to GitHub's <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<h3 id="create-a-github-repository">Create a GitHub repository</h3>
<p>Create a new GitHub repository by visiting <a href="https://repo.new">repo.new</a>. After creating a new repository, go to your newly created project directory to prepare and push your local application to GitHub by running the following commands in your terminal:</p>
<pre><code class="language-sh">&#35; Skip the following three commands if you have built your application&#10;&#35; using C3 or already committed your changes&#10;git init&#10;git add .&#10;git commit -m &quot;Initial commit&quot;&#10;&#10;git branch -M main&#10;git remote add origin https://github.com/&lt;YOUR_GH_USERNAME&gt;/&lt;REPOSITORY_NAME&gt;&#10;git push -u origin main&#10;</code></pre>
<h3 id="create-a-pages-project">Create a Pages project</h3>
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
<table><thead><tr><th>Configuration option</th><th>Value</th></tr></thead><tbody><tr><td>Production branch</td><td><code>main</code></td></tr><tr><td>Build command</td><td><code>npm run build</code></td></tr><tr><td>Build directory</td><td><code>dist</code></td></tr></tbody></table>
<p>Optionally, you can customize the <strong>Project name</strong> field. It defaults to the GitHub repository's name, but it does not need to match. The <strong>Project name</strong> value is assigned as your <code>*.pages.dev</code> subdomain.</p>
<ol start="7">
<li>After completing configuration, select the <strong>Save and Deploy</strong>.</li>
</ol>
<p>Review your first deploy pipeline in progress. Pages installs all dependencies and builds the project as specified. Cloudflare Pages will automatically rebuild your project and deploy it on every new pushed commit.</p>
<p>Additionally, you will have access to <a href="/pages/configuration/preview-deployments/">preview deployments</a>, which repeat the build-and-deploy process for pull requests. With these, you can preview changes to your project with a real URL before deploying your changes to production.</p>
<h2 id="use-bindings-in-your-nuxt-application">Use bindings in your Nuxt application</h2>
<p>A <a href="/pages/functions/bindings/">binding</a> allows your application to interact with Cloudflare developer products, such as <a href="/kv/">KV</a>, <a href="/durable-objects/">Durable Objects</a>, <a href="/r2/">R2</a>, and <a href="/d1/">D1</a>.</p>
<p>If you intend to use bindings in your project, you must first set up your bindings for local and remote development.</p>
<h3 id="set-up-bindings-for-local-development">Set up bindings for local development</h3>
<p>Projects created via C3 come with <code>nitro-cloudflare-dev</code>, a <code>nitro</code> module that simplifies the process of working with bindings during development:</p>
<pre><code class="language-typescript">export default defineNuxtConfig({&#10;	modules: [&quot;nitro-cloudflare-dev&quot;],&#10;});&#10;</code></pre>
<p>This module is powered by the <a href="/workers/wrangler/api#getplatformproxy"><code>getPlatformProxy</code> helper function</a>. <code>getPlatformProxy</code> will automatically detect any bindings defined in your project's Wrangler configuration file and emulate those bindings in local development. Review <a href="/workers/wrangler/configuration/#bindings">Wrangler configuration information on bindings</a> for more information on how to configure bindings in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11036.md")
</aside>
<h3 id="set-up-bindings-for-a-deployed-application">Set up bindings for a deployed application</h3>
<p>In order to access bindings in a deployed application, you will need to <a href="/pages/functions/bindings/">configure your bindings</a> in the Cloudflare dashboard.</p>
<h3 id="add-bindings-to-typescript-projects">Add bindings to TypeScript projects</h3>
<p>To get proper type support, you need to create a new <code>env.d.ts</code> file in the root of your project and declare a <a href="/pages/functions/bindings/">binding</a>. Make sure you have generated Cloudflare runtime types by running <a href="/pages/functions/typescript/"><code>wrangler types</code></a>.</p>
<p>The following is an example of adding a <code>KVNamespace</code> binding:</p>
<pre><code class="language-ts">declare module &quot;h3&quot; {&#10;	interface H3EventContext {&#10;		cf: CfProperties;&#10;		cloudflare: {&#10;			request: Request;&#10;			env: {&#10;				MY_KV: KVNamespace;&#10;			};&#10;			context: ExecutionContext;&#10;		};&#10;	}&#10;}&#10;</code></pre>
<h3 id="access-bindings-in-your-nuxt-application">Access bindings in your Nuxt application</h3>
<p>In Nuxt, add server-side code via <a href="https://nuxt.com/docs/guide/directory-structure/server#server-directory">Server Routes and Middleware</a>. The <code>defineEventHandler()</code> method is used to define your API endpoints in which you can access Cloudflare's context via the provided <code>context</code> field. The <code>context</code> field allows you to access any bindings set for your application.</p>
<p>The following code block shows an example of accessing a KV namespace in Nuxt.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11041.md")
</div></div>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your Nuxt site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
