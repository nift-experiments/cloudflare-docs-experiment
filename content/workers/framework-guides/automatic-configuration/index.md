<p>Wrangler can automatically detect your framework and configure your project for Cloudflare Workers. This allows you to deploy existing projects with a single command, without manually setting up configuration files or installing adapters.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16305.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>When you run <code>wrangler deploy</code> or <code>wrangler setup</code> in a project directory without a Wrangler configuration file, Wrangler will:</p>
<ol>
<li><strong>Detect your framework</strong> - Analyzes your project to identify the framework you're using</li>
<li><strong>Prompt for confirmation</strong> - Shows the detected settings and asks you to confirm before making changes</li>
<li><strong>Install adapters</strong> - Installs any required Cloudflare adapters for your framework</li>
<li><strong>Generate configuration</strong> - Creates a <code>wrangler.jsonc</code> file with appropriate settings</li>
<li><strong>Update package.json</strong> - Adds helpful scripts like <code>deploy</code>, <code>preview</code>, and <code>cf-typegen</code></li>
<li><strong>Configure git</strong> - Adds Wrangler-specific entries to <code>.gitignore</code></li>
</ol>
<h2 id="supported-frameworks">Supported frameworks</h2>
<p>Automatic configuration supports the following frameworks:</p>
<table>
<thead>
<tr>
<th>Framework</th>
<th>Adapter/Tool</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/workers/framework-guides/web-apps/nextjs/">Next.js</a></td>
<td><code>vinext</code></td>
<td>Configures vinext for Cloudflare Workers and adds the required Vite and Wrangler configuration.</td>
</tr>
<tr>
<td><a href="/workers/framework-guides/web-apps/astro/">Astro</a></td>
<td><code>@astrojs/cloudflare</code></td>
<td>Runs <code>astro add cloudflare</code> automatically</td>
</tr>
<tr>
<td><a href="/workers/framework-guides/web-apps/sveltekit/">SvelteKit</a></td>
<td><code>@sveltejs/adapter-cloudflare</code></td>
<td>Runs <code>sv add sveltekit-adapter</code> automatically</td>
</tr>
<tr>
<td><a href="/workers/framework-guides/web-apps/more-web-frameworks/nuxt/">Nuxt</a></td>
<td>Built-in Cloudflare preset</td>
<td></td>
</tr>
<tr>
<td><a href="/workers/framework-guides/web-apps/react-router/">React Router</a></td>
<td>Cloudflare Vite plugin</td>
<td></td>
</tr>
<tr>
<td><a href="/workers/framework-guides/web-apps/more-web-frameworks/solid/">Solid Start</a></td>
<td>Built-in Cloudflare preset</td>
<td></td>
</tr>
<tr>
<td><a href="/workers/framework-guides/web-apps/tanstack-start/">TanStack Start</a></td>
<td>Cloudflare Vite plugin</td>
<td></td>
</tr>
<tr>
<td><a href="/workers/framework-guides/web-apps/more-web-frameworks/angular/">Angular</a></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="/workers/framework-guides/web-apps/more-web-frameworks/analog/">Analog</a></td>
<td>Built-in Cloudflare preset</td>
<td></td>
</tr>
<tr>
<td><a href="/workers/vite-plugin/">Vite</a></td>
<td>Cloudflare Vite plugin</td>
<td></td>
</tr>
<tr>
<td><a href="/workers/framework-guides/web-apps/vike/">Vike</a></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="/workers/framework-guides/web-apps/more-web-frameworks/waku/">Waku</a></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Static sites</td>
<td>None</td>
<td>Any directory with an <code>index.html</code></td>
</tr>
</tbody>
</table>
<p>Automatic configuration may also work with other projects, such as React or Vue SPAs. Try running <code>wrangler deploy</code> or <code>wrangler setup</code> to see if your project is detected.</p>
<h2 id="files-created-and-modified">Files created and modified</h2>
<p>When automatic configuration runs, the following files may be created or modified:</p>
<h3 id="wrangler-jsonc"><code>wrangler.jsonc</code></h3>
<p>A new Wrangler configuration file is created with settings appropriate for your framework:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16306.md")
</div>
<p>The exact configuration varies based on your framework.</p>
<h3 id="package-json"><code>package.json</code></h3>
<p>New scripts are added to your <code>package.json</code>:</p>
<pre><code class="language-json">{&#10;	&quot;scripts&quot;: {&#10;		&quot;deploy&quot;: &quot;npm run build &amp;&amp; wrangler deploy&quot;,&#10;		&quot;preview&quot;: &quot;npm run build &amp;&amp; wrangler dev&quot;,&#10;		&quot;cf-typegen&quot;: &quot;wrangler types&quot;&#10;	}&#10;}&#10;</code></pre>
<h3 id="gitignore"><code>.gitignore</code></h3>
<p>Wrangler-specific entries are added:</p>
<pre><code class="language-txt">&#35; wrangler files&#10;.wrangler&#10;.dev.vars*&#10;!.dev.vars.example&#10;</code></pre>
<h3 id="assetsignore"><code>.assetsignore</code></h3>
<p>For frameworks that generate worker files in the output directory, an <code>.assetsignore</code> file is created to exclude them from static asset uploads:</p>
<pre><code class="language-txt">_worker.js&#10;_routes.json&#10;</code></pre>
<h2 id="using-automatic-configuration">Using automatic configuration</h2>
<h3 id="deploy-with-automatic-configuration">Deploy with automatic configuration</h3>
<p>To deploy an existing project, run <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a> in your project directory:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler deploy" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Wrangler will detect your framework, show the configuration it will apply, and prompt you to confirm before making changes and deploying.</p>
<h3 id="configure-without-deploying">Configure without deploying</h3>
<p>To configure your project without deploying, use <a href="/workers/wrangler/commands/general/#setup"><code>wrangler setup</code></a>:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler setup</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler setup" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler setup</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler setup" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler setup</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler setup" aria-label="Copy to clipboard">Copy</button></div></div>
<p>This is useful when you want to review the generated configuration before deploying.</p>
<h3 id="preview-changes-with-dry-run">Preview changes with dry run</h3>
<p>To see what changes would be made without actually modifying any files:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler setup --dry-run</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler setup --dry-run" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler setup --dry-run</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler setup --dry-run" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler setup --dry-run</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler setup --dry-run" aria-label="Copy to clipboard">Copy</button></div></div>
<p>This outputs a summary of the configuration that would be generated.</p>
<h2 id="non-interactive-mode">Non-interactive mode</h2>
<p>To skip the confirmation prompts, use the <a href="/workers/wrangler/commands/general/#deploy"><code>--yes</code> flag</a>:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler deploy --yes</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler deploy --yes" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler deploy --yes</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler deploy --yes" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler deploy --yes</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler deploy --yes" aria-label="Copy to clipboard">Copy</button></div></div>
<p>This applies the configuration automatically using sensible defaults. This is useful in CI/CD environments or when you want to accept the detected settings without reviewing them.</p>
<h2 id="importing-a-repository-from-the-dashboard">Importing a repository from the dashboard</h2>
<p>When you import a GitHub or GitLab repository via the Cloudflare dashboard, autoconfig runs non-interactively. If your repository does not have a Wrangler configuration file, <a href="/workers/ci-cd/builds/">Workers Builds</a> will create a pull request with the necessary configuration.</p>
<p>The PR includes all the configuration changes described above. A preview deployment is generated so you can test the changes before merging. Once merged, your project is ready for deployment.</p>
<p>For more details, refer to <a href="/workers/ci-cd/builds/automatic-prs/">Automatic pull requests</a>.</p>
<h2 id="skipping-automatic-configuration">Skipping automatic configuration</h2>
<p>If you do not want automatic configuration to run, ensure you have a valid Wrangler configuration file (<code>wrangler.toml</code>, <code>wrangler.json</code>, or <code>wrangler.jsonc</code>) in your project before running <code>wrangler deploy</code>.</p>
<p>You can also manually configure your project by following the framework-specific guides in the <a href="/workers/framework-guides/">Framework guides</a>.</p>
<h2 id="next-js-configuration">Next.js configuration</h2>
<p>For Next.js projects, automatic configuration uses <a href="/workers/framework-guides/web-apps/nextjs/">vinext</a> as the default deployment path for Cloudflare Workers. The generated configuration adds the vinext and Vite dependencies, creates the Cloudflare Workers configuration, and adds package scripts for development, builds, and deployment.</p>
<p>vinext supports Next.js caching features such as Incremental Static Regeneration (ISR), <code>&quot;use cache&quot;</code>, and <code>unstable_cache</code>. For production applications, configure the generated Workers project with the cache backend your application requires. For more information, refer to <a href="https://github.com/cloudflare/vinext#caching">vinext caching</a>.</p>
<p>If you need the OpenNext adapter instead of vinext, configure it manually by following the <a href="/workers/framework-guides/web-apps/opennext/">OpenNext adapter guide</a>.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="multiple-frameworks-detected">Multiple frameworks detected</h3>
<p>When you import a repository via <a href="/workers/ci-cd/builds/">Workers Builds</a> in the Cloudflare dashboard, automatic configuration will fail if your project contains multiple frameworks. To resolve this, set the <a href="/workers/ci-cd/builds/configuration/#build-settings">root directory</a> to the path containing only one framework. For monorepos, refer to <a href="/workers/ci-cd/builds/advanced-setups/#monorepos">monorepo setup</a>.</p>
<p>When running <code>wrangler deploy</code> or <code>wrangler setup</code> locally, Wrangler will prompt you to select which framework to use if multiple frameworks are detected.</p>
<h3 id="framework-not-detected">Framework not detected</h3>
<p>If your framework is not detected, ensure your <code>package.json</code> includes the framework as a dependency.</p>
<h3 id="configuration-already-exists">Configuration already exists</h3>
<p>If a Wrangler configuration file already exists, automatic configuration will not run. To reconfigure your project, delete the existing configuration file and run <code>wrangler deploy</code> or <code>wrangler setup</code> again.</p>
<h3 id="workspaces">Workspaces</h3>
<p>Support for monorepos and npm/yarn/pnpm workspaces is currently limited. Wrangler analyzes the project directory where you run the command, but does not detect dependencies installed at the workspace root. This can cause framework detection to fail if the framework is listed as a dependency in the workspace's root <code>package.json</code> rather than in the individual project's <code>package.json</code>.</p>
<p>If you encounter issues, report them in the <a href="https://github.com/cloudflare/workers-sdk/issues/new/choose">Wrangler GitHub repository</a>.</p>
