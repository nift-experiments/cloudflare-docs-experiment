<p><a href="https://vitejs.dev">Vite</a> is a next-generation build tool for front-end developers. With <a href="https://vitejs.dev/blog/announcing-vite3.html">the release of Vite 3</a>, developers can make use of new command line (CLI) improvements, starter templates, and <a href="https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#300-2022-07-13">more</a> to help build their front-end applications.</p>
<p>Cloudflare Pages has native support for Vite 3 projects. Refer to the blog post on <a href="https://blog.cloudflare.com/cloudflare-pages-build-improvements/">improvements to the Pages build process</a>, including sub-second build initialization, for more information on using Vite 3 and Cloudflare Pages to optimize your application's build tooling.</p>
<p>In this guide, you will learn how to start a new project using Vite 3, and deploy it to Cloudflare Pages.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create vite@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create vite@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create vite</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create vite" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create vite@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create vite@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<pre><code class="language-sh">✔ Project name: … vite-on-pages&#10;✔ Select a framework: › vue&#10;✔ Select a variant: › vue&#10;&#10;Scaffolding project in ~/src/vite-on-pages...&#10;&#10;Done. Now run:&#10;&#10;  cd vite-on-pages&#10;  npm install&#10;  npm run dev&#10;</code></pre>
<p>You will now create a new GitHub repository, and push your code using <a href="https://cli.github.com">GitHub's <code>gh</code> command line (CLI)</a>:</p>
<pre><code class="language-sh">git init&#10;</code></pre>
<pre><code class="language-sh">Initialized empty Git repository in ~/vite-vue3-on-pages/.git/&#10;</code></pre>
<pre><code class="language-sh">git add .&#10;git commit -m &quot;Initial commit&quot;                                           vite-vue3-on-pages/git/main +&#10;</code></pre>
<pre><code class="language-sh">[main (root-commit) dad4177] Initial commit&#10; 14 files changed, 1452 insertions(+)&#10;</code></pre>
<pre><code class="language-sh">gh repo create&#10;</code></pre>
<pre><code class="language-sh">✓ Created repository kristianfreeman/vite-vue3-on-pages on GitHub&#10;✓ Added remote git@github.com:kristianfreeman/vite-vue3-on-pages.git&#10;</code></pre>
<pre><code class="language-sh">git push&#10;</code></pre>
<p>To deploy your site to Pages:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Create application** > **Pages** > **Import from an existing Git repository**.
3. Select your new GitHub repository.
4. In the **Set up builds and deployments**, set `npm run build` as the **Build command**, and `dist` as the **Build output directory**.
<p>After completing configuration, select <strong>Save and Deploy</strong>.</p>
<p>You will see your first deploy pipeline in progress. Pages installs all dependencies and builds the project as specified. After you have deployed your project, it will be available at the <code>&lt;YOUR_PROJECT_NAME&gt;.pages.dev</code> subdomain. Find your project's subdomain in <strong>Workers &amp; Pages</strong> &gt; select your Pages project &gt; <strong>Deployments</strong>.</p>
<p>Cloudflare Pages will automatically rebuild your project and deploy it on every new pushed commit.</p>
<p>Additionally, you will have access to <a href="/pages/configuration/preview-deployments/">preview deployments</a>, which repeat the build-and-deploy process for pull requests. With these, you can preview changes to your project with a real URL before deploying them to production.</p>
<h2 id="learn-more">Learn more</h2>
<p>By completing this guide, you have successfully deployed your Vite 3 site to Cloudflare Pages. To get started with other frameworks, <a href="/pages/framework-guides/">refer to the list of Framework guides</a>.</p>
