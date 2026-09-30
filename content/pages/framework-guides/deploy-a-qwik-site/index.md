<p><a href="https://github.com/builderio/qwik">Qwik</a> is an open-source, DOM-centric, resumable web application framework designed for best possible time to interactive by focusing on <a href="https://qwik.builder.io/docs/concepts/resumable/">resumability</a>, server-side rendering of HTML and <a href="https://qwik.builder.io/docs/concepts/progressive/#lazy-loading">fine-grained lazy-loading</a> of code.</p>
<p>In this guide, you will create a new Qwik application implemented via <a href="https://qwik.builder.io/qwikcity/overview/">Qwik City</a> (Qwik's meta-framework) and deploy it using Cloudflare Pages.</p>
<h2 id="creating-a-new-project">Creating a new project</h2>
<p>Use the <a href="https://www.npmjs.com/package/create-cloudflare"><code>create-cloudflare</code></a> CLI (C3) to create a new project. C3 will create a new project directory, initiate Qwik's official setup tool, and provide the option to deploy instantly.</p>
<p>To use <code>create-cloudflare</code> to create a new Qwik project, run the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- my-qwik-app --framework=qwik --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-qwik-app --framework=qwik --platform=pages" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare my-qwik-app --framework=qwik --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-qwik-app --framework=qwik --platform=pages" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest my-qwik-app --framework=qwik --platform=pages</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-qwik-app --framework=qwik --platform=pages" aria-label="Copy to clipboard">Copy</button></div></div>
<p><code>create-cloudflare</code> will install additional dependencies, including the <a href="/workers/wrangler/install-and-update/#check-your-wrangler-version">Wrangler CLI</a> and any necessary adapters, and ask you setup questions.</p>
<p>As part of the <code>cloudflare-pages</code> adapter installation, a <code>functions/[[path]].ts</code> file will be created. The <code>[[path]]</code> filename indicates that this file will handle requests to all incoming URLs. Refer to <a href="/pages/functions/routing/#dynamic-routes">Path segments</a> to learn more.</p>
<p>After selecting your server option, change the directory to your project and render your project by running the following command:</p>
<pre><code class="language-sh">npm start&#10;</code></pre>
<h2 id="before-you-continue">Before you continue</h2>
<p>All of the framework guides assume you already have a fundamental understanding of <a href="https://git-scm.com/">Git</a>. If you are new to Git, refer to this <a href="https://guides.github.com/introduction/git-handbook/">summarized Git handbook</a> on how to set up Git on your local machine.</p>
<p>If you clone with SSH, you must <a href="https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">generate SSH keys</a> on each computer you use to push or pull from GitHub.</p>
<p>Refer to the <a href="https://guides.github.com/introduction/git-handbook/">GitHub documentation</a> and <a href="https://git-scm.com/book/en/v2">Git documentation</a> for more information.</p>
<h2 id="create-a-github-repository">Create a GitHub repository</h2>
<p>Create a new GitHub repository by visiting <a href="https://repo.new">repo.new</a>. After creating a new repository, go to your newly created project directory to prepare and push your local application to GitHub by running the following commands in your terminal:</p>
<pre><code class="language-sh">git init&#10;git remote add origin https://github.com/&lt;your-gh-username&gt;/&lt;repository-name&gt;&#10;git add .&#10;git commit -m &quot;Initial commit&quot;&#10;git branch -M main&#10;git push -u origin main&#10;</code></pre>
<h2 id="deploy-with-cloudflare-pages">Deploy with Cloudflare Pages</h2>
<h3 id="deploy-via-the-create-cloudflare-cli-c3">Deploy via the <code>create-cloudflare</code> CLI (C3)</h3>
<p>If you use <a href="https://www.npmjs.com/package/create-cloudflare"><code>create-cloudflare</code>(C3)</a> to create your new Qwik project, C3 will install all dependencies needed for your project and prompt you to deploy your project via the CLI. If you deploy, your site will be live and you will be provided with a deployment URL.</p>
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
<table><thead><tr><th>Configuration option</th><th>Value</th></tr></thead><tbody><tr><td>Production branch</td><td><code>main</code></td></tr><tr><td>Build command</td><td><code>npm run build</code></td></tr><tr><td>Build directory</td><td><code>dist</code></td></tr></tbody></table>
<p>After configuring your site, you can begin your first deploy. You should see Cloudflare Pages installing <code>npm</code>, your project dependencies, and building your site before deploying it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11033.md")
</aside>
<p>After deploying your site, you will receive a unique subdomain for your project on <code>*.pages.dev</code>.
Every time you commit new code to your Qwik site, Cloudflare Pages will automatically rebuild your project and deploy it. You will also get access to <a href="/pages/configuration/preview-deployments/">preview deployments</a> on new pull requests, to preview how changes look to your site before deploying them to production.</p>
<h2 id="use-bindings-in-your-qwik-application">Use bindings in your Qwik application</h2>
<p>A <a href="/pages/functions/bindings/">binding</a> allows your application to interact with Cloudflare developer products, such as <a href="/kv/concepts/how-kv-works/">KV</a>, <a href="/durable-objects/">Durable Object</a>, <a href="/r2/">R2</a>, and <a href="https://blog.cloudflare.com/introducing-d1/">D1</a>.</p>
<p>In QwikCity, add server-side code via <a href="https://qwik.builder.io/qwikcity/route-loader/">routeLoaders</a> and <a href="https://qwik.builder.io/qwikcity/action/">actions</a>. Then access bindings set for your application via the <code>platform</code> object provided by the framework.</p>
<p>The following code block shows an example of accessing a KV namespace in QwikCity.</p>
<pre><code class="language-typescript">// ...&#10;&#10;export const useGetServerTime = routeLoader$(({ platform }) =&gt; {&#10;  // the type `KVNamespace` comes from runtime types generated by running `wrangler types`&#10;  const { MY_KV } = (platform.env as { MY_KV: KVNamespace }));&#10;&#10;  return {&#10;    // ....&#10;  }&#10;});&#10;</code></pre>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your Qwik site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
