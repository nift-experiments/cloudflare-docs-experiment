<p>SvelteKit is the official framework for building modern web applications with <a href="https://svelte.dev">Svelte</a>, an increasingly popular open-source tool for creating user interfaces. Unlike most frameworks, SvelteKit uses Svelte, a compiler that transforms your component code into efficient JavaScript, enabling SvelteKit to deliver fast, reactive applications that update the DOM surgically as the application state changes.</p>
<p>In this guide, you will create a new SvelteKit application and deploy it using Cloudflare Pages.
You will use <a href="https://kit.svelte.dev/"><code>SvelteKit</code></a>, the official Svelte framework for building web applications of all sizes.</p>
<h2 id="setting-up-a-new-project">Setting up a new project</h2>
<p>Use the <a href="https://www.npmjs.com/package/create-cloudflare"><code>create-cloudflare</code></a> CLI (C3) to set up a new project. C3 will create a new project directory, initiate SvelteKit's official setup tool, and provide the option to deploy instantly.</p>
<p>To use <code>create-cloudflare</code> to create a new SvelteKit project, run the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- my-svelte-app --framework=svelte --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-svelte-app --framework=svelte --platform=pages" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare my-svelte-app --framework=svelte --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-svelte-app --framework=svelte --platform=pages" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest my-svelte-app --framework=svelte --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-svelte-app --framework=svelte --platform=pages" aria-label="Copy to clipboard">Copy</button></div></div>
<p>SvelteKit will prompt you for customization choices. For the template option, choose one of the application/project options. The remaining answers will not affect the rest of this guide. Choose the options that suit your project.</p>
<p><code>create-cloudflare</code> will then install dependencies, including the <a href="/workers/wrangler/install-and-update/#check-your-wrangler-version">Wrangler</a> CLI and the SvelteKit <code>@sveltejs/adapter-cloudflare</code> adapter, and ask you setup questions.</p>
<p>After you have installed your project dependencies, start your application:</p>
<pre><code class="language-sh">npm run dev&#10;</code></pre>
<h2 id="before-you-continue">Before you continue</h2>
<p>All of the framework guides assume you already have a fundamental understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to this <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<p>If you clone with SSH, you must <a href="https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generate SSH keys</a> on each computer you use to push or pull from GitHub.</p>
<p>Refer to the <a href="https://guides.github.com/introduction/git-handbook/">GitHub documentation</a> and <a href="https://git-scm.com/book/en/v2">Git documentation</a> for more information.</p>
<h2 id="create-a-github-repository">Create a GitHub repository</h2>
<p>Create a new GitHub repository by visiting <a href="https://repo.new">repo.new</a>. After creating a new repository, go to your newly created project directory to prepare and push your local application to GitHub by running the following commands in your terminal:</p>
<pre><code class="language-sh">git init&#10;git remote add origin https://github.com/&lt;your-gh-username&gt;/&lt;repository-name&gt;&#10;git add .&#10;git commit -m &quot;Initial commit&quot;&#10;git branch -M main&#10;git push -u origin main&#10;</code></pre>
<h2 id="sveltekit-cloudflare-configuration">SvelteKit Cloudflare configuration</h2>
<p>To use SvelteKit with Cloudflare Pages, you need to add the <a href="https://kit.svelte.dev/docs/adapter-cloudflare">Cloudflare adapter</a> to your application.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11026.md")
</aside>
<ol>
<li>Install the Cloudflare Adapter by running <code>npm i --save-dev @sveltejs/adapter-cloudflare</code> in your terminal.</li>
<li>Include the adapter in <code>svelte.config.js</code>:</li>
</ol>
<pre><code class="language-diff">&#45; import adapter from &#x27;@sveltejs/adapter-auto&#x27;;&#10;&#43; import adapter from &#x27;@sveltejs/adapter-cloudflare&#x27;;&#10;&#10;/** @type {import(&#x27;@sveltejs/kit&#x27;).Config} */&#10;const config = {&#10;  kit: {&#10;    adapter: adapter(),&#10;    // ... truncated ...&#10;  }&#10;};&#10;&#10;export default config;&#10;</code></pre>
<ol start="3">
<li>(Needed if you are using TypeScript) Include support for environment variables. The <code>env</code> object, containing KV namespaces and other storage objects, is passed to SvelteKit via the platform property along with context and caches, meaning you can access it in hooks and endpoints. For example:</li>
</ol>
<pre><code class="language-diff">declare namespace App {&#10;    interface Locals {}&#10;&#10;&#43;   interface Platform {&#10;&#43;       env: {&#10;&#43;           COUNTER: DurableObjectNamespace;&#10;&#43;       };&#10;&#43;       context: {&#10;&#43;           waitUntil(promise: Promise&lt;any&gt;): void;&#10;&#43;       };&#10;&#43;       caches: CacheStorage &amp; { default: Cache }&#10;&#43;   }&#10;&#10;    interface Session {}&#10;&#10;    interface Stuff {}&#10;}&#10;</code></pre>
<ol start="4">
<li>Access the added KV or Durable objects (or generally any <a href="/pages/functions/bindings/">binding</a>) in your endpoint with <code>env</code>:</li>
</ol>
<pre><code class="language-js">export async function post(context) {&#10;	const counter = context.platform.env.COUNTER.idFromName(&quot;A&quot;);&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11025.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11024.md")
</aside>
<h2 id="deploy-with-cloudflare-pages">Deploy with Cloudflare Pages</h2>
<h3 id="deploy-via-the-create-cloudflare-cli-c3">Deploy via the <code>create-cloudflare</code> CLI (C3)</h3>
<p>If you use <a href="https://www.npmjs.com/package/create-cloudflare"><code>create-cloudflare</code>(C3)</a> to create your new Svelte project, C3 will install all dependencies needed for your project and prompt you to deploy your project via the CLI. If you deploy, your site will be live and you will be provided with a deployment URL.</p>
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
6. In the **Build settings** section, select _SvelteKit_ as your **Framework preset**. Your selection will provide the following information:
<div>
<table><thead><tr><th>Configuration option</th><th>Value</th></tr></thead><tbody><tr><td>Production branch</td><td><code>main</code></td></tr><tr><td>Build command</td><td><code>npm run build</code></td></tr><tr><td>Build directory</td><td><code>.svelte-kit/cloudflare</code></td></tr></tbody></table>
</div>
<p>Optionally, you can customize the <strong>Project name</strong> field. It defaults to the GitHub repository's name, but it does not need to match. The <strong>Project name</strong> value is assigned as your <code>*.pages.dev</code> subdomain.</p>
<p>After completing configuration, click the <strong>Save and Deploy</strong> button.</p>
<p>You will see your first deploy pipeline in progress. Pages installs all dependencies and builds the project as specified.</p>
<p>Cloudflare Pages will automatically rebuild your SvelteKit project and deploy it on every new pushed commit.</p>
<p>Additionally, you will have access to <a href="/pages/configuration/preview-deployments/">preview deployments</a>, which repeat the build-and-deploy process for pull requests. With these, you can preview changes to your project with a real URL before deploying them to production.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11023.md")
</aside>
<h2 id="functions-setup">Functions setup</h2>
<p>In SvelteKit, functions are written as endpoints. Functions contained in the <code>/functions</code> directory at the project's root will not be included in the deployment, which compiles to a single <code>_worker.js</code> file.</p>
<p>To have the functionality equivalent to Pages Functions <a href="/pages/functions/api-reference/#onrequests"><code>onRequests</code></a>, you need to write standard request handlers in SvelteKit. For example, the following TypeScript file behaves like an <code>onRequestGet</code>:</p>
<pre><code class="language-ts">import type { RequestHandler } from &quot;./$types&quot;;&#10;&#10;export const GET = (({ url }) =&gt; {&#10;	return new Response(String(Math.random()));&#10;}) satisfies RequestHandler;&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="sveltekit-api-routes">SvelteKit API Routes</h3>
@markup("md", "content/.markup/bodies/11022.md")
</aside>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your Svelte site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
