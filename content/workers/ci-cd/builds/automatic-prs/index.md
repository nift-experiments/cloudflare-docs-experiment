<p>Workers Builds can automatically create pull requests in your repository to configure your project or resolve deployment issues.</p>
<h2 id="configuration-pr">Configuration PR</h2>
<p>When you connect a repository that does not have a Wrangler configuration file, Workers Builds runs <code>wrangler deploy</code> which triggers <a href="/workers/framework-guides/automatic-configuration/">automatic project configuration</a>. Instead of failing, it creates a pull request with the necessary configuration for your detected framework.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16784.md")
</aside>
<h3 id="why-you-should-merge-the-pr">Why you should merge the PR</h3>
<p>Without the configuration in your repository, every build has to run autoconfig first, which means your project gets built twice - once during autoconfig to generate the configuration, and again for the actual deployment. Merging the PR commits the configuration to your repository, so future builds skip autoconfig and go straight to building and deploying. This results in faster deployments and version-controlled settings.</p>
<h3 id="what-the-pr-includes">What the PR includes</h3>
<p><img src="/assets/upstream/images/workers/ci-cd/builds/automatic-pr.png" alt="Example of an automatic configuration pull request created by Workers Builds" /></p>
<p>The configuration PR may contain changes to the following files, depending on your framework:</p>
<ul>
<li><strong><code>wrangler.jsonc</code></strong> - Wrangler configuration file with your Worker settings</li>
<li><strong>Framework adapter</strong> - Any required Cloudflare adapter for your framework (for example, <code>@astrojs/cloudflare</code> for Astro)</li>
<li><strong>Framework configuration</strong> - Updates to framework config files (for example, <code>astro.config.mjs</code> for Astro or <code>svelte.config.js</code> for SvelteKit)</li>
<li><strong><code>package.json</code></strong> - New scripts like <code>deploy</code>, <code>preview</code>, and <code>cf-typegen</code>, plus required dependencies</li>
<li><strong><code>package-lock.json</code></strong> / <strong><code>yarn.lock</code></strong> / <strong><code>pnpm-lock.yaml</code></strong> - Updated lock file with new dependencies</li>
<li><strong><code>.gitignore</code></strong> - Entries for <code>.wrangler</code> and <code>.dev.vars*</code> files</li>
<li><strong><code>.assetsignore</code></strong> - For frameworks that generate worker files in the output directory</li>
</ul>
<h3 id="pr-description">PR description</h3>
<p>The PR description includes:</p>
<ul>
<li><strong>Detected settings</strong> - Framework, build command, deploy command, and version command</li>
<li><strong>Preview link</strong> - A working preview generated using the detected settings</li>
<li><strong>Next steps</strong> - Links to documentation for adding bindings, custom domains, and more</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16783.md")
</aside>
<h2 id="name-conflict-pr">Name conflict PR</h2>
<p>If Workers Builds detects a mismatch between your Worker name in the Cloudflare dashboard and the <code>name</code> field in your Wrangler configuration file, it will create a pull request to fix the conflict.</p>
<p>This can happen when:</p>
<ul>
<li>You rename your Worker in the dashboard but not in your config file</li>
<li>You connect a repository that was previously used with a different Worker</li>
<li>The <code>name</code> field in your config does not match the connected Worker</li>
</ul>
<p>The PR will update the <code>name</code> field in your Wrangler configuration to match the Worker name in the dashboard.</p>
<p>For more details, refer to the <a href="/changelog/2025-02-20-builds-name-conflict/">name conflict changelog</a>.</p>
<h2 id="reviewing-prs">Reviewing PRs</h2>
<p>When you receive a PR from Workers Builds:</p>
<ol>
<li><strong>Review the changes</strong> - Check that the configuration matches your project requirements</li>
<li><strong>Test the preview</strong> - Use the preview link in the PR description to verify everything works</li>
<li><strong>Merge when ready</strong> - Once satisfied, merge the PR to enable faster deployments</li>
</ol>
