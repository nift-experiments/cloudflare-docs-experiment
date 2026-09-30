<p>Wrangler commands for creating, developing, deploying, and managing Workers.</p>
<h2 id="init"><code>init</code></h2>
<p>Create a new project via the <a href="/workers/get-started/guide/#1-create-a-new-worker-project">create-cloudflare-cli (C3) tool</a>. A variety of web frameworks are available to choose from as well as templates. Dependencies are installed by default, with the option to deploy your project immediately.</p>
<pre><code class="language-txt">wrangler init [&lt;NAME&gt;] [OPTIONS]&#10;</code></pre>
<ul>
<li><code>NAME</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional (default: name of working directory)</span>
<ul>
<li>The name of the Workers project. This is both the directory name and <code>name</code> property in the generated <a href="/workers/wrangler/configuration/">Wrangler configuration</a>.</li>
</ul>
</li>
<li><code>--yes</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Answer yes to any prompts for new projects.</li>
</ul>
</li>
<li><code>--from-dash</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Fetch a Worker initialized from the dashboard. This is done by passing the flag and the Worker name. <code>wrangler init --from-dash &lt;WORKER_NAME&gt;</code>.</li>
<li>The <code>--from-dash</code> command will not automatically sync changes made to the dashboard after the command is used. Therefore, it is recommended that you continue using the CLI.</li>
</ul>
</li>
</ul>
<p>The following global flags work on every command:</p>
<ul>
<li><code>--help</code> <span class="nb-type">boolean</span>
<ul>
<li>Show help.</li>
</ul>
</li>
<li><code>--config</code> <span class="nb-type">string</span> (not supported by Pages)
<ul>
<li>Path to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ul>
</li>
<li><code>--cwd</code> <span class="nb-type">string</span>
<ul>
<li>Run as if Wrangler was started in the specified directory instead of the current working directory.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="dev"><code>dev</code></h2>
<p>Start a local server for developing your Worker.</p>
<pre><code class="language-txt">wrangler dev [&lt;SCRIPT&gt;] [OPTIONS]&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17424.md")
</aside>
<ul>
<li><code>SCRIPT</code> <span class="nb-type">string</span>
<ul>
<li>The path to an entry point for your Worker. Only required if your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> does not include a <code>main</code> key (for example, <code>main = &quot;index.js&quot;</code>).</li>
</ul>
</li>
<li><code>--name</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Name of the Worker.</li>
</ul>
</li>
<li><code>--config</code>, <code>-c</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Path(s) to <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>. If not provided, Wrangler will use the nearest config file based on your current working directory.</li>
<li>You can provide multiple configuration files to run multiple Workers in one dev session like this: <code>wrangler dev -c ./wrangler.toml -c ../other-worker/wrangler.toml</code>. The first config will be treated as the <em>primary</em> Worker, which will be exposed over HTTP. The remaining config files will only be accessible via a service binding from the primary Worker.</li>
</ul>
</li>
<li><code>--no-bundle</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: false) optional</span>
<ul>
<li>Skip Wrangler's build steps. Particularly useful when using custom builds. Refer to <a href="/workers/wrangler/bundling/">Bundling</a> for more information.</li>
</ul>
</li>
<li><code>--env</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Perform on a specific environment.</li>
</ul>
</li>
<li><code>--compatibility-date</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A date in the form yyyy-mm-dd, which will be used to determine which version of the Workers runtime is used.</li>
</ul>
</li>
<li><code>--compatibility-flags</code>, <code>--compatibility-flag</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Flags to use for compatibility checks.</li>
</ul>
</li>
<li><code>--latest</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: true) optional</span>
<ul>
<li>Use the latest version of the Workers runtime.</li>
</ul>
</li>
<li><code>--ip</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>IP address to listen on, defaults to <code>localhost</code>.</li>
</ul>
</li>
<li><code>--port</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Port to listen on.</li>
</ul>
</li>
<li><code>--inspector-port</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Port for devtools to connect to.</li>
</ul>
</li>
<li><code>--routes</code>, <code>--route</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Routes to upload.</li>
<li>For example: <code>--route example.com/*</code>.</li>
</ul>
</li>
<li><code>--host</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Host to forward requests to, defaults to the zone of project.</li>
</ul>
</li>
<li><code>--local-protocol</code> <span class="nb-type">http'|'https</span> <span class="nb-metainfo">(default: http) optional</span>
<ul>
<li>Protocol to listen to requests on.</li>
</ul>
</li>
<li><code>--https-key-path</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Path to a custom certificate key.</li>
</ul>
</li>
<li><code>--https-cert-path</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Path to a custom certificate.</li>
</ul>
</li>
<li><code>--local-upstream</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Host to act as origin in local mode, defaults to <code>dev.host</code> or route.</li>
</ul>
</li>
<li><code>--infer-origin-from-routes</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: true) optional</span>
<ul>
<li>Use the first configured route to infer the origin (<code>request.url</code> and the <code>Host</code> header) seen by the Worker in local mode. Set to <code>false</code> to preserve the real local origin, for example <code>localhost:8787</code>, so that Host- or Origin-sensitive logic behaves the same as the actual local request. An explicit <code>--host</code>, <code>--local-upstream</code>, or <code>dev.host</code> takes precedence either way.</li>
</ul>
</li>
<li><code>--assets</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional beta</span>
<ul>
<li>Folder of static assets to be served. Replaces <a href="/workers/configuration/sites/">Workers Sites</a>. Visit <a href="/workers/static-assets/">assets</a> for more information.</li>
</ul>
</li>
<li><code>--site</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional deprecated, use <code>--assets</code></span>
<ul>
<li>Folder of static assets for Workers Sites.</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17423.md")
</aside>
- `--site-include` <span class="nb-type">string[]</span> <span class="nb-metainfo">optional deprecated</span>
  - Array of `.gitignore`-style patterns that match file or directory names from the sites directory. Only matched items will be uploaded.
- `--site-exclude` <span class="nb-type">string[]</span> <span class="nb-metainfo">optional deprecated</span>
  - Array of `.gitignore`-style patterns that match file or directory names from the sites directory. Matched items will not be uploaded.
- `--upstream-protocol` <span class="nb-type">http&#x27;|&#x27;https</span> <span class="nb-metainfo">(default: https) optional</span>
  - Protocol to forward requests to host on.
- `--var` <span class="nb-type">key:value\[]</span> <span class="nb-metainfo">optional</span>
  - Array of `key:value` pairs to inject as variables into your code. The value will always be passed as a string to your Worker.
  - For example, `--var "git_hash:'$(git rev-parse HEAD)'" "test:123"` makes the `git_hash` and `test` variables available in your Worker's `env`.
  - This flag is an alternative to defining [`vars`](/workers/wrangler/configuration/#non-inheritable-keys) in your [Wrangler configuration file](/workers/wrangler/configuration/). If defined in both places, this flag's values will be used.
- `--define` <span class="nb-type">key:value\[]</span> <span class="nb-metainfo">optional</span>
  - Array of `key:value` pairs to replace global identifiers in your code.
  - For example, `--define "GIT_HASH:'$(git rev-parse HEAD)'"` will replace all uses of `GIT_HASH` with the actual value at build time.
  - This flag is an alternative to defining [`define`](/workers/wrangler/configuration/#non-inheritable-keys) in your [Wrangler configuration file](/workers/wrangler/configuration/). If defined in both places, this flag's values will be used.
- `--tsconfig` <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
  - Path to a custom `tsconfig.json` file.
- `--minify` <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
  - Minify the Worker.
- `--persist-to` <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
  - Specify directory to use for local persistence.
- `--remote` <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: false) optional</span>
  - Develop against remote resources and data stored on Cloudflare's network.
- `--tunnel` <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: false) optional</span>
  - Expose your local dev server over a Cloudflare Tunnel. For more information, refer to [Share a local dev server](/workers/local-development/local-dev-tunnels/).
- `--tunnel-name` <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
  - Use an existing named Cloudflare Tunnel. Combine with `--tunnel` to open it automatically at startup.
- `--test-scheduled` <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: false) optional</span>
  - Exposes a `/cdn-cgi/local/scheduled` fetch route which will trigger a scheduled event (Cron Trigger) for testing during development. To simulate different cron patterns, a `cron` query parameter can be passed in: `/cdn-cgi/local/scheduled?cron=*+*+*+*+*`.
- `--log-level` <span class="nb-type">debug&#x27;|&#x27;info&#x27;|&#x27;log&#x27;|&#x27;warn&#x27;|&#x27;error|&#x27;none</span> <span class="nb-metainfo">(default: log) optional</span>
  - Specify Wrangler's logging level.
- `--show-interactive-dev-session` <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: true if the terminal supports interactivity) optional</span>
  - Show the interactive dev session.
- `--alias` `Array<string>`
  - Specify modules to alias using [module aliasing](/workers/wrangler/configuration/#module-aliasing).
- `--types` <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: false) optional</span>
  - Generate types from your Worker configuration.
- `--local` <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: false) optional</span>
  - Run in local mode. In this mode:
    - the Worker code is running locally on your machine
    - all [remote bindings](/workers/local-development/#remote-bindings) are disabled, which behaves exactly as if they were configured with `remote: false`.
<p>The following global flags work on every command:</p>
<ul>
<li><code>--help</code> <span class="nb-type">boolean</span>
<ul>
<li>Show help.</li>
</ul>
</li>
<li><code>--config</code> <span class="nb-type">string</span> (not supported by Pages)
<ul>
<li>Path to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ul>
</li>
<li><code>--cwd</code> <span class="nb-type">string</span>
<ul>
<li>Run as if Wrangler was started in the specified directory instead of the current working directory.</li>
</ul>
</li>
</ul>
<p><code>wrangler dev</code> is a way to <a href="/workers/local-development/">locally test</a> your Worker while developing. With <code>wrangler dev</code> running, send HTTP requests to <code>localhost:8787</code> and your Worker should execute as expected. You will also see <code>console.log</code> messages and exceptions appearing in your terminal.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17422.md")
</aside>
<hr />
<h2 id="deploy"><code>deploy</code></h2>
<p>Deploy your Worker to Cloudflare.</p>
<p>When you run <code>wrangler deploy</code> in a project directory without a Wrangler configuration file, Wrangler will <a href="/workers/framework-guides/automatic-configuration/">automatically detect your framework</a> and configure your project for Cloudflare Workers. This command will prompt you to confirm the detected settings before applying changes. Confirm that you would like to proceed, and your project will be configured and deployed.</p>
<p>To deploy from an AI agent or another environment before Cloudflare authentication is available, use <code>wrangler deploy --temporary</code>. This flow requires Wrangler 4.102.0 or later. Wrangler creates or reuses a temporary preview account, deploys to that account, and prints a claim URL. For more information, refer to <a href="/workers/platform/claim-deployments/">Claim deployments</a>.</p>
<p>To configure your project without deploying, use <a href="#setup"><code>wrangler setup</code></a> instead.</p>
<pre><code class="language-txt">wrangler deploy [&lt;PATH&gt;] [OPTIONS]&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17421.md")
</aside>
<ul>
<li>
<p><code>PATH</code> <span class="nb-type">string</span></p>
<ul>
<li>A path specific what needs to be deployed, this can either be:
<ul>
<li>
<p>The path to an entry point for your Worker.</p>
<ul>
<li>Only required if your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> does not include a <code>main</code> key (for example, <code>main = &quot;index.js&quot;</code>).</li>
</ul>
</li>
<li>
<p>Or the path to an assets directory for the deployment of a static site.</p>
<ul>
<li>Visit <a href="/workers/static-assets/">assets</a> for more information.</li>
<li>This overrides the eventual <code>assets</code> configuration in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
<li>This is equivalent to the <code>--assets</code> option listed below.</li>
<li>Note: this option currently only works only in interactive mode (so not in CI systems).</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li>
<p><code>--name</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Name of the Worker.</li>
</ul>
</li>
<li>
<p><code>--no-bundle</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: false) optional</span></p>
<ul>
<li>Skip Wrangler's build steps. Particularly useful when using custom builds. Refer to <a href="/workers/wrangler/bundling/">Bundling</a> for more information.</li>
</ul>
</li>
<li>
<p><code>--env</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Perform on a specific environment.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17420.md")
</aside>
<ul>
<li><code>--outdir</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Path to directory where Wrangler will write the bundled Worker files.</li>
</ul>
</li>
<li><code>--compatibility-date</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>A date in the form yyyy-mm-dd, which will be used to determine which version of the Workers runtime is used.</li>
</ul>
</li>
<li><code>--compatibility-flags</code>, <code>--compatibility-flag</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Flags to use for compatibility checks.</li>
</ul>
</li>
<li><code>--latest</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: true) optional</span>
<ul>
<li>Use the latest version of the Workers runtime.</li>
</ul>
</li>
<li><code>--assets</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional beta</span>
<ul>
<li>Folder of static assets to be served. Replaces <a href="/workers/configuration/sites/">Workers Sites</a>. Visit <a href="/workers/static-assets/">assets</a> for more information.</li>
</ul>
</li>
<li><code>--site</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional deprecated, use <code>--assets</code></span>
<ul>
<li>Folder of static assets for Workers Sites.</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17419.md")
</aside>
- `--site-include` <span class="nb-type">string[]</span> <span class="nb-metainfo">optional deprecated</span>
  - Array of `.gitignore`-style patterns that match file or directory names from the sites directory. Only matched items will be uploaded.
- `--site-exclude` <span class="nb-type">string[]</span> <span class="nb-metainfo">optional deprecated</span>
  - Array of `.gitignore`-style patterns that match file or directory names from the sites directory. Matched items will not be uploaded.
- `--var` <span class="nb-type">key:value\[]</span> <span class="nb-metainfo">optional</span>
  - Array of `key:value` pairs to inject as variables into your code. The value will always be passed as a string to your Worker.
  - For example, `--var git_hash:$(git rev-parse HEAD) test:123` makes the `git_hash` and `test` variables available in your Worker's `env`.
  - This flag is an alternative to defining [`vars`](/workers/wrangler/configuration/#non-inheritable-keys) in your [Wrangler configuration file](/workers/wrangler/configuration/). If defined in both places, this flag's values will be used.
- `--define` <span class="nb-type">key:value\[]</span> <span class="nb-metainfo">optional</span>
  - Array of `key:value` pairs to replace global identifiers in your code.
  - For example, `--define GIT_HASH:$(git rev-parse HEAD)` will replace all uses of `GIT_HASH` with the actual value at build time.
  - This flag is an alternative to defining [`define`](/workers/wrangler/configuration/#non-inheritable-keys) in your [Wrangler configuration file](/workers/wrangler/configuration/). If defined in both places, this flag's values will be used.
- `--triggers`, `--schedule`, `--schedules` <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span>
  - Cron schedules to attach to the deployed Worker. Refer to [Cron Trigger Examples](/workers/configuration/cron-triggers/#examples).
- `--routes`, `--route` string\[] optional
  - Routes where this Worker will be deployed.
  - For example: `--route example.com/*`.
- `--domain` <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span>
  - Custom domains where this Worker will be deployed.
  - For example: `--domain example.com`.
- `--tsconfig` <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
  - Path to a custom `tsconfig.json` file.
- `--minify` <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
  - Minify the bundled Worker before deploying.
- `--dry-run` <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: false) optional</span>
  - Compile a project without actually deploying to live servers. Combined with `--outdir`, this is also useful for testing the output of `npx wrangler deploy`. It also gives developers a chance to upload our generated sourcemap to a service like Sentry, so that errors from the Worker can be mapped against source code, but before the service goes live.
- `--keep-vars` <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: false) optional</span>
  - It is recommended best practice to treat your Wrangler developer environment as a source of truth for your Worker configuration, and avoid making changes via the Cloudflare dashboard.
  - If you change your environment variables in the Cloudflare dashboard, Wrangler will override them the next time you deploy. If you want to disable this behaviour set `keep-vars` to `true`.
  - Secrets are never deleted by a deployment whether this flag is true or false.
- `--secrets-file` <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
  - Path to a file containing secrets to upload alongside the deployment. Accepts JSON or `.env` format — the same formats used by [`wrangler secret bulk`](#secret-bulk). Existing secrets not included in the file are preserved from the previous version. Refer to [Secrets — Upload secrets alongside code](/workers/configuration/secrets/#upload-secrets-alongside-code) for more details.
- `--dispatch-namespace` <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
  - Specify the [Workers for Platforms dispatch namespace](/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dispatch-namespace) to upload this Worker to.
- `--metafile` <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
  - Specify a file to write the build metadata from esbuild to. If flag is used without a path string, this defaults to `bundle-meta.json` inside the directory specified by `--outdir`. This can be useful for understanding the bundle size.
- `--containers-rollout` <span class="nb-type">immediate | gradual | none</span> <span class="nb-metainfo">optional</span>
  - [Rollout](/containers/configuration/rollouts/) mode for Containers on this deploy. `gradual` (default) uses `rollout_step_percentage`. `immediate` uses one 100% step (not a simultaneous restart of every container instance). `none` skips container image and instance updates.
- `--strict` <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: false) optional</span>
  - Turns on strict mode for the deployment command, meaning that the command will be more defensive and prevent deployments which could introduce potential issues. In particular, this mode prevents deployments if the deployment would potentially override remote settings in non-interactive environments.
- `--tag` <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
  - A tag for this Worker version. Matches the behavior of `wrangler versions upload --tag`.
- `--message` <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
  - A descriptive message for this Worker version and deployment. Matches the behavior of `wrangler versions upload --message`. The message is also applied to the deployment.
- `--yes` <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: false) optional</span>
  - Skip confirmation prompts and run [automatic project configuration](/workers/framework-guides/automatic-configuration/) non-interactively using detected settings. Only applicable when no Wrangler configuration file exists in your project.
- `--temporary` <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
  - Deploy with a temporary preview account when no Cloudflare credentials are available. Requires Wrangler 4.102.0 or later. Wrangler prints a claim URL that lets you claim the deployment within 60 minutes. This is intended for AI agents and other first-time deployment flows. If Wrangler can already use OAuth, `CLOUDFLARE_API_TOKEN`, or a global API key, this flag returns an error. For more information, refer to [Claim deployments](/workers/platform/claim-deployments/).
<p>The following global flags work on every command:</p>
<ul>
<li><code>--help</code> <span class="nb-type">boolean</span>
<ul>
<li>Show help.</li>
</ul>
</li>
<li><code>--config</code> <span class="nb-type">string</span> (not supported by Pages)
<ul>
<li>Path to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ul>
</li>
<li><code>--cwd</code> <span class="nb-type">string</span>
<ul>
<li>Run as if Wrangler was started in the specified directory instead of the current working directory.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="delete"><code>delete</code></h2>
<p>Delete your Worker and all associated Cloudflare developer platform resources.</p>
<pre><code class="language-txt">wrangler delete [&lt;SCRIPT&gt;] [OPTIONS]&#10;</code></pre>
<ul>
<li><code>SCRIPT</code> <span class="nb-type">string</span>
<ul>
<li>The path to an entry point for your Worker. Only required if your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> does not include a <code>main</code> key (for example, <code>main = &quot;index.js&quot;</code>).</li>
</ul>
</li>
<li><code>--name</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Name of the Worker.</li>
</ul>
</li>
<li><code>--env</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Perform on a specific environment.</li>
</ul>
</li>
<li><code>--dry-run</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: false) optional</span>
<ul>
<li>Do not actually delete the Worker. This is useful for testing the output of <code>wrangler delete</code>.</li>
</ul>
</li>
</ul>
<p>The following global flags work on every command:</p>
<ul>
<li><code>--help</code> <span class="nb-type">boolean</span>
<ul>
<li>Show help.</li>
</ul>
</li>
<li><code>--config</code> <span class="nb-type">string</span> (not supported by Pages)
<ul>
<li>Path to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ul>
</li>
<li><code>--cwd</code> <span class="nb-type">string</span>
<ul>
<li>Run as if Wrangler was started in the specified directory instead of the current working directory.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="setup">setup</h2><p>🪄 Setup a project to work on Cloudflare</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler setup</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler setup" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler setup</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler setup" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler setup</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler setup" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>--yes</code> <small>boolean, default: False</small><p>Answer &quot;yes&quot; to any prompts for configuring your project</p>
</li><li><code>--build</code> <small>boolean, default: False</small><p>Run your project's build command once it has been configured</p>
</li><li><code>--dry-run</code> <small>boolean</small><p>Runs the command without applying any filesystem modifications</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<p>This command configures your project for Cloudflare Workers without deploying. It performs the same <a href="/workers/framework-guides/automatic-configuration/">automatic project configuration</a> as <code>wrangler deploy</code>, but does not deploy. This is useful when you want to review the generated configuration before deploying.</p>
<hr />
<h2 id="secret"><code>secret</code></h2>
<p>Manage the secret variables for a Worker.</p>
<p>This action creates a new <a href="/workers/versions-and-deployments/#versions">version</a> of the Worker and <a href="/workers/versions-and-deployments/#deployments">deploys</a> it immediately. To only create a new version of the Worker, use the <a href="#versions-secret-put"><code>wrangler versions secret</code></a> commands.</p>
<h3 id="secret-put">secret put</h3><p>Create or update a secret for a Worker</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler secret put [KEY]</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler secret put [KEY]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler secret put [KEY]</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler secret put [KEY]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler secret put [KEY]</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler secret put [KEY]" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>key</code> <small>required, string</small><p>The variable name to be accessible in the Worker</p>
</li><li><code>--name</code> <small>string</small><p>Name of the Worker. If this is not specified, it will default to the name specified in your Wrangler config file.</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<p>When running this command, you will be prompted to input the secret's value:</p>
<pre><code class="language-sh">npx wrangler secret put FOO&#10;</code></pre>
<pre><code class="language-sh">? Enter a secret value: &gt; ***&#10;🌀 Creating the secret for script worker-app&#10;✨ Success! Uploaded secret FOO&#10;</code></pre>
<p>The <code>put</code> command can also receive piped input. For example:</p>
<pre><code class="language-sh">echo &quot;-----BEGIN PRIVATE KEY-----\nM...==\n-----END PRIVATE KEY-----\n&quot; | wrangler secret put PRIVATE_KEY&#10;</code></pre>
<h3 id="secret-delete">secret delete</h3><p>Delete a secret from a Worker</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler secret delete [KEY]</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler secret delete [KEY]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler secret delete [KEY]</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler secret delete [KEY]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler secret delete [KEY]</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler secret delete [KEY]" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>key</code> <small>required, string</small><p>The variable name to be accessible in the Worker</p>
</li><li><code>--name</code> <small>string</small><p>Name of the Worker. If this is not specified, it will default to the name specified in your Wrangler config file.</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<h3 id="secret-list">secret list</h3><p>List all secrets for a Worker</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler secret list</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler secret list" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler secret list</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler secret list" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler secret list</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler secret list" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>--name</code> <small>string</small><p>Name of the Worker. If this is not specified, it will default to the name specified in your Wrangler config file.</p>
</li><li><code>--format</code> <small>default: json</small><p>The format to print the secrets in</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<p>The following is an example of listing the secrets for the current Worker.</p>
<pre><code class="language-sh">npx wrangler secret list&#10;</code></pre>
<pre><code class="language-sh">[&#10;  {&#10;    &quot;name&quot;: &quot;FOO&quot;,&#10;    &quot;type&quot;: &quot;secret_text&quot;&#10;  }&#10;]&#10;</code></pre>
<hr />
<h3 id="secret-bulk">secret bulk</h3><p>Create, update, or delete multiple secrets for a Worker in a single request, with up to 100 secrets per command.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler secret bulk [FILE]</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler secret bulk [FILE]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler secret bulk [FILE]</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler secret bulk [FILE]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler secret bulk [FILE]</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler secret bulk [FILE]" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>file</code> <small>string</small><p>The file of key-value pairs to create, update, or delete, as JSON in form {&quot;key&quot;: &quot;value&quot;, ...} or .env file in the form KEY=VALUE. Set a key to null in the JSON file to delete it. Deletion is not supported with .env files. If omitted, Wrangler expects to receive input from stdin rather than a file.</p>
</li><li><code>--name</code> <small>string</small><p>Name of the Worker. If this is not specified, it will default to the name specified in your Wrangler config file.</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17418.md")
</aside>
<p>The following is an example of creating, updating, and deleting secrets from a JSON file redirected to <code>stdin</code>. Set a key to <code>null</code> to delete it.</p>
<pre><code class="language-json">{&#10;	&quot;secret-name-1&quot;: &quot;secret-value-1&quot;,&#10;	&quot;secret-name-2&quot;: &quot;secret-value-2&quot;,&#10;	&quot;secret-name-3&quot;: null&#10;}&#10;</code></pre>
<pre><code class="language-sh">npx wrangler secret bulk &lt; secrets.json&#10;</code></pre>
<pre><code class="language-sh">🌀 Processing the secrets for the Worker &quot;script-name&quot;&#10;✨ Successfully created secret for key: secret-name-1&#10;✨ Successfully created secret for key: secret-name-2&#10;💥 Successfully deleted secret for key: secret-name-3&#10;&#10;Finished processing secrets file:&#10;✨ 2 secrets successfully created&#10;💥 1 secrets successfully deleted&#10;</code></pre>
<hr />
<h2 id="tail">tail</h2><p>🦚 Start a log tailing session for a Worker</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler tail [WORKER]</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler tail [WORKER]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler tail [WORKER]</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler tail [WORKER]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler tail [WORKER]</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler tail [WORKER]" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>worker</code> <small>string</small><p>Name or route of the worker to tail</p>
</li><li><code>--format</code><p>The format of log entries</p>
</li><li><code>--status</code><p>Filter by invocation status</p>
</li><li><code>--header</code> <small>string</small><p>Filter by HTTP header</p>
</li><li><code>--method</code> <small>string</small><p>Filter by HTTP method</p>
</li><li><code>--sampling-rate</code> <small>number</small><p>Adds a percentage of requests to log sampling rate</p>
</li><li><code>--search</code> <small>string</small><p>Filter by a text match in console.log messages</p>
</li><li><code>--ip</code> <small>string</small><p>Filter by the IP address the request originates from. Use &quot;self&quot; to filter for your own IP</p>
</li><li><code>--version-id</code> <small>string</small><p>Filter by Worker version</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<p>After starting <code>wrangler tail</code>, you will receive a live feed of console and exception logs for each request your Worker receives.</p>
<p>If your Worker has a high volume of traffic, the tail might enter sampling mode. This will cause some of your messages to be dropped and a warning to appear in your tail logs. To prevent messages from being dropped, add the options listed above to filter the volume of tail messages.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17417.md")
</aside>
<p>If sampling persists after using options to filter messages, consider using <a href="/logs/instant-logs/">instant logs</a>.</p>
<hr />
<h2 id="versions"><code>versions</code></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17416.md")
</aside>
<h3 id="versions-upload">versions upload</h3><p>Uploads your Worker code and config as a new Version</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler versions upload [PATH]</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler versions upload [PATH]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler versions upload [PATH]</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler versions upload [PATH]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler versions upload [PATH]</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler versions upload [PATH]" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>path</code> <small>string</small><p>The path to an entry point for your Worker or a directory of static assets</p>
</li><li><code>--name</code> <small>string</small><p>Name of the Worker</p>
</li><li><code>--tag</code> <small>string</small><p>A tag for this Worker Version</p>
</li><li><code>--message</code> <small>string</small><p>A descriptive message for this Worker Version</p>
</li><li><code>--no-bundle</code> <small>boolean, default: False</small><p>Skip internal build steps and directly upload Worker</p>
</li><li><code>--outdir</code> <small>string</small><p>Output directory for the bundled Worker</p>
</li><li><code>--outfile</code> <small>string</small><p>Output file for the bundled worker</p>
</li><li><code>--compatibility-date</code> <small>string</small><p>Date to use for compatibility checks</p>
</li><li><code>--compatibility-flags</code> <small>string</small><p>Flags to use for compatibility checks</p>
</li><li><code>--latest</code> <small>boolean, default: False</small><p>Use the latest compatibility date supported by this version of Wrangler</p>
</li><li><code>--assets</code> <small>string</small><p>Static assets to be served. Replaces Workers Sites.</p>
</li><li><code>--var</code> <small>string</small><p>A key-value pair to be injected into the script as a variable</p>
</li><li><code>--define</code> <small>string</small><p>A key-value pair to be substituted in the script</p>
</li><li><code>--alias</code> <small>string</small><p>A module pair to be substituted in the script</p>
</li><li><code>--jsx-factory</code> <small>string</small><p>The function that is called for each JSX element</p>
</li><li><code>--jsx-fragment</code> <small>string</small><p>The function that is called for each JSX fragment</p>
</li><li><code>--tsconfig</code> <small>string</small><p>Path to a custom tsconfig.json file</p>
</li><li><code>--minify</code> <small>boolean</small><p>Minify the Worker</p>
</li><li><code>--upload-source-maps</code> <small>boolean</small><p>Include source maps when uploading this Worker</p>
</li><li><code>--dry-run</code> <small>boolean</small><p>Compile a project and run checks without actually uploading the Worker</p>
</li><li><code>--secrets-file</code> <small>string</small><p>Path to a file containing secrets to upload with the version (JSON or .env format). Applies additively with secrets from previous deployments - omitted secrets will not be deleted.</p>
</li><li><code>--keep-vars</code> <small>boolean, default: False</small><p>When not used (or set to false), Wrangler will delete all vars before setting those found in the Wrangler configuration.
When used (and set to true), the environment variables are not deleted before the deployment.
If you set variables via the dashboard you probably want to use this flag.
Note that secrets are never deleted by deployments.</p>
</li><li><code>--strict</code> <small>boolean, default: False</small><p>Enables strict mode, which prevents uploads when there are conflicting remote changes.</p>
</li><li><code>--preview-alias</code> <small>string</small><p>Name of an alias for this Worker version</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<h3 id="versions-deploy">versions deploy</h3><p>Safely roll out new Versions of your Worker by splitting traffic between multiple Versions</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler versions deploy [VERSION-SPECS]</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler versions deploy [VERSION-SPECS]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler versions deploy [VERSION-SPECS]</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler versions deploy [VERSION-SPECS]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler versions deploy [VERSION-SPECS]</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler versions deploy [VERSION-SPECS]" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>--name</code> <small>string</small><p>Name of the worker</p>
</li><li><code>--version-id</code> <small>string</small><p>Worker Version ID(s) to deploy</p>
</li><li><code>--percentage</code> <small>number</small><p>Percentage of traffic to split between Worker Version(s) (0-100)</p>
</li><li><code>version-specs</code> <small>string</small><p>Shorthand notation to deploy Worker Version(s) [<version-id>@<percentage>..]. Omitted percentages share the remaining traffic.</p>
</li><li><code>--version-tag</code> <small>string</small><p>Worker Version tag(s) to deploy, resolved to a Version ID against the deployable versions. Supports the shorthand notation [<version-tag>@<percentage>..].</p>
</li><li><code>--message</code> <small>string</small><p>Description of this deployment (optional)</p>
</li><li><code>--yes</code> <small>boolean, default: False</small><p>Automatically accept defaults to prompts</p>
</li><li><code>--dry-run</code> <small>boolean, default: False</small><p>Don't actually deploy</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17415.md")
</aside>
<h3 id="versions-list">versions list</h3><p>List the 10 most recent Versions of your Worker</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler versions list</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler versions list" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler versions list</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler versions list" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler versions list</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler versions list" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>--name</code> <small>string</small><p>Name of the Worker</p>
</li><li><code>--json</code> <small>boolean, default: False</small><p>Display output as JSON</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<h3 id="versions-view">versions view</h3><p>View the details of a specific version of your Worker</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler versions view [VERSION-ID]</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler versions view [VERSION-ID]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler versions view [VERSION-ID]</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler versions view [VERSION-ID]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler versions view [VERSION-ID]</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler versions view [VERSION-ID]" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>version-id</code> <small>required, string</small><p>The Worker Version ID to view</p>
</li><li><code>--name</code> <small>string</small><p>Name of the worker</p>
</li><li><code>--json</code> <small>boolean, default: False</small><p>Display output as JSON</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<h3 id="versions-secret-put">versions secret put</h3><p>Create or update a secret variable for a Worker</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler versions secret put [KEY]</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler versions secret put [KEY]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler versions secret put [KEY]</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler versions secret put [KEY]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler versions secret put [KEY]</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler versions secret put [KEY]" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>key</code> <small>string</small><p>The variable name to be accessible in the Worker</p>
</li><li><code>--name</code> <small>string</small><p>Name of the Worker</p>
</li><li><code>--message</code> <small>string</small><p>Description of this deployment</p>
</li><li><code>--tag</code> <small>string</small><p>A tag for this version</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<h3 id="versions-secret-delete">versions secret delete</h3><p>Delete a secret variable from a Worker</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler versions secret delete [KEY]</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler versions secret delete [KEY]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler versions secret delete [KEY]</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler versions secret delete [KEY]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler versions secret delete [KEY]</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler versions secret delete [KEY]" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>key</code> <small>string</small><p>The variable name to be accessible in the Worker</p>
</li><li><code>--name</code> <small>string</small><p>Name of the Worker</p>
</li><li><code>--message</code> <small>string</small><p>Description of this deployment</p>
</li><li><code>--tag</code> <small>string</small><p>A tag for this version</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<h3 id="versions-secret-bulk">versions secret bulk</h3><p>Create or update a secret variable for a Worker</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler versions secret bulk [FILE]</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler versions secret bulk [FILE]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler versions secret bulk [FILE]</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler versions secret bulk [FILE]" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler versions secret bulk [FILE]</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler versions secret bulk [FILE]" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>file</code> <small>string</small><p>The file of key-value pairs to upload, as JSON in form {&quot;key&quot;: value, ...} or .dev.vars file in the form KEY=VALUE</p>
</li><li><code>--name</code> <small>string</small><p>Name of the Worker</p>
</li><li><code>--message</code> <small>string</small><p>Description of this deployment</p>
</li><li><code>--tag</code> <small>string</small><p>A tag for this version</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<hr />
<h2 id="triggers"><code>triggers</code></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17414.md")
</aside>
<h3 id="triggers-deploy">triggers deploy</h3><p>Apply changes to triggers (Routes or domains and Cron Triggers) when using <code>wrangler versions upload</code></p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler triggers deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler triggers deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler triggers deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler triggers deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler triggers deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler triggers deploy" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>--name</code> <small>string</small><p>Name of the worker</p>
</li><li><code>--triggers</code> <small>string</small><p>cron schedules to attach</p>
</li><li><code>--routes</code> <small>string</small><p>Routes to upload</p>
</li><li><code>--dry-run</code> <small>boolean, default: False</small><p>Don't actually deploy</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<hr />
<h2 id="deployments"><code>deployments</code></h2>
<p><a href="/workers/versions-and-deployments/#deployments">Deployments</a> track the version(s) of your Worker that are actively serving traffic.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17413.md")
</aside>
<h3 id="deployments-list">deployments list</h3><p>Displays the 10 most recent deployments of your Worker</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler deployments list</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler deployments list" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler deployments list</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler deployments list" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler deployments list</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler deployments list" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>--name</code> <small>string</small><p>Name of the Worker</p>
</li><li><code>--json</code> <small>boolean, default: False</small><p>Display output as JSON</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<h3 id="deployments-status">deployments status</h3><p>View the current state of your production</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler deployments status</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler deployments status" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler deployments status</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler deployments status" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler deployments status</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler deployments status" aria-label="Copy to clipboard">Copy</button></div></div><ul><li><code>--name</code> <small>string</small><p>Name of the Worker</p>
</li><li><code>--json</code> <small>boolean, default: False</small><p>Display output as JSON</p>
</li></ul><details><summary>Global flags</summary><ul><li><code>--version</code><p>Show version number</p></li><li><code>--cwd</code><p>Run as if Wrangler was started in the specified directory instead of the current working directory</p></li><li><code>--config</code><p>Path to Wrangler configuration file</p></li><li><code>--env</code><p>Environment to use for operations, and for selecting .env and .dev.vars files</p></li><li><code>--env-file</code><p>Path to an .env file to load; can be specified multiple times; values from earlier files are overridden by values in later files</p></li><li><code>--install-skills</code><p>Install Cloudflare skills for detected AI coding agents before running the command</p></li><li><code>--profile</code><p>Use a specific auth profile</p></li></ul></details>
<h2 id="rollback"><code>rollback</code></h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17412.md")
</aside>
<pre><code class="language-txt">wrangler rollback [&lt;VERSION_ID&gt;] [OPTIONS]&#10;</code></pre>
<ul>
<li><code>VERSION_ID</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>The ID of the version you wish to roll back to. If not supplied, the <code>rollback</code> command defaults to the version uploaded before the latest version.</li>
</ul>
</li>
<li><code>--name</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Perform on a specific Worker rather than inheriting from the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ul>
</li>
<li><code>--message</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Add message for rollback. Accepts empty string. When specified, interactive prompts for rollback confirmation and message are skipped.</li>
</ul>
</li>
</ul>
<p>The following global flags work on every command:</p>
<ul>
<li><code>--help</code> <span class="nb-type">boolean</span>
<ul>
<li>Show help.</li>
</ul>
</li>
<li><code>--config</code> <span class="nb-type">string</span> (not supported by Pages)
<ul>
<li>Path to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ul>
</li>
<li><code>--cwd</code> <span class="nb-type">string</span>
<ul>
<li>Run as if Wrangler was started in the specified directory instead of the current working directory.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="types"><code>types</code></h2>
<p>Generate types based on your Worker configuration, including <code>Env</code> types based on your bindings, module rules, and <a href="/workers/languages/typescript/">runtime types</a> based on the<code>compatibility_date</code> and <code>compatibility_flags</code> in your <a href="/workers/wrangler/configuration/">config file</a>.</p>
<pre><code class="language-txt">wrangler types [&lt;PATH&gt;] [OPTIONS]&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17411.md")
</aside>
<h3 id="multi-environment-support">Multi-environment support</h3>
<p>By default, <code>wrangler types</code> generates types for bindings from <strong>all environments</strong> defined in your configuration file. This ensures your generated <code>Env</code> type includes all bindings that might be used across different deployment environments (such as staging and production), preventing TypeScript errors when accessing environment-specific bindings.</p>
<p>For example, if you have a KV namespace binding only in production and an R2 bucket binding only in staging, both will be included in the generated types as optional properties.</p>
<p>To generate types for only a specific environment, use the <code>--env</code> flag.</p>
<h3 id="options">Options</h3>
<ul>
<li><code>PATH</code> <span class="nb-type">string</span> <span class="nb-metainfo">(default: <code>./worker-configuration.d.ts</code>)</span>
<ul>
<li>The path to where types for your Worker will be written.</li>
<li>The path must have a <code>d.ts</code> extension.</li>
</ul>
</li>
<li><code>--env</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Generate types for bindings in a specific environment only, rather than aggregating bindings from all environments.</li>
</ul>
</li>
<li><code>--env-interface</code> <span class="nb-type">string</span> <span class="nb-metainfo">(default: <code>Env</code>)</span>
<ul>
<li>The name of the interface to generate for the environment object.</li>
<li>Not valid if the Worker uses the Service Worker syntax.</li>
</ul>
</li>
<li><code>--include-runtime</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: true)</span>
<ul>
<li>Whether to generate runtime types based on the<code>compatibility_date</code> and <code>compatibility_flags</code> in your <a href="/workers/wrangler/configuration/">config file</a>.</li>
</ul>
</li>
<li><code>--include-env</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: true)</span>
<ul>
<li>Whether to generate <code>Env</code> types based on your Worker bindings.</li>
</ul>
</li>
<li><code>--strict-vars</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional (default: true)</span>
<ul>
<li>Control the types that Wrangler generates for <code>vars</code> bindings.</li>
<li>If <code>true</code>, (the default) Wrangler generates literal and union types for bindings (e.g. <code>myVar: 'my dev variable' | 'my prod variable'</code>).</li>
<li>If <code>false</code>, Wrangler generates generic types (e.g. <code>myVar: string</code>). This is useful when variables change frequently, especially when working across multiple environments.</li>
</ul>
</li>
<li><code>--check</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Check if the generated types at the specified path are up-to-date without regenerating them.</li>
<li>Exits with code 0 if types are up-to-date, or code 1 if types are out-of-date.</li>
<li>Useful for CI/CD pipelines and pre-commit hooks to ensure types have been regenerated after configuration changes.</li>
</ul>
</li>
<li><code>--config</code>, <code>-c</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span>
<ul>
<li>Path(s) to <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>. If the Worker you are generating types for has service bindings or bindings to Durable Objects, you can also provide the paths to those configuration files so that the generated <code>Env</code> type will include RPC types. For example, given a Worker with a service binding, <code>wrangler types -c wrangler.toml -c ../bound-worker/wrangler.toml</code> will generate an <code>Env</code> type like this:</li>
</ul>
</li>
</ul>
<pre><code class="language-ts">interface Env {&#10;	SERVICE_BINDING: Service&lt;import(&quot;../bound-worker/src/index&quot;).Entrypoint&gt;;&#10;}&#10;</code></pre>
<hr />
<h2 id="check"><code>check</code></h2>
<h3 id="startup"><code>startup</code></h3>
<p>Analyze your Worker's startup phase. Wrangler reports bundle size and a summary of local CPU activity. It also saves a detailed CPU profile.</p>
<pre><code class="language-sh">wrangler check startup&#10;</code></pre>
<pre><code class="language-txt">Bundle: 42.31 KiB / gzip: 11.24 KiB&#10;&#10;Local startup profile:&#10;  Profile window: 25.2 ms&#10;  Sampled time: 24.8 ms&#10;  Active: 18.4 ms (including 1.2 ms garbage collection)&#10;  Idle: 6.4 ms&#10;  Samples: 25&#10;</code></pre>
<p>The local startup profile includes the following metrics:</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Profile window</td>
<td>Elapsed time between the start and end of the profiling session.</td>
</tr>
<tr>
<td>Sampled time</td>
<td>Total time represented by the captured CPU samples.</td>
</tr>
<tr>
<td>Active</td>
<td>Sampled time that the Worker was not idle, including garbage collection.</td>
</tr>
<tr>
<td>Idle</td>
<td>Sampled time that the Worker was idle.</td>
</tr>
<tr>
<td>Samples</td>
<td>Number of CPU samples captured during the profiling session.</td>
</tr>
</tbody>
</table>
<p>Import the generated <code>.cpuprofile</code> file into Chrome DevTools or open it directly in VS Code to view a flamegraph. When a Worker deployment fails with a startup time error, Wrangler also generates this profile automatically.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17410.md")
</aside>
<ul>
<li><code>--args</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>To customise the way <code>wrangler check startup</code> builds your Worker for analysis, provide the exact arguments you use when deploying your Worker with <code>wrangler deploy</code>, or your Pages project with <code>wrangler pages functions build</code>. For instance, if you deploy your Worker with <code>wrangler deploy --no-bundle</code>, you should use <code>wrangler check startup --args=&quot;--no-bundle&quot;</code> to profile the startup phase.</li>
</ul>
</li>
<li><code>--worker</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>
<ul>
<li>If you don't use Wrangler to deploy your Worker, you can use this argument to provide a Worker bundle to analyse. This should be a file path to a serialized multipart upload, with the exact same format as <a href="/api/resources/workers/subresources/scripts/methods/update/">the API expects</a>.</li>
</ul>
</li>
<li><code>--pages</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span>
<ul>
<li>If you don't use a Wrangler config file with your Pages project (i.e. a Wrangler config file containing <code>pages_build_output_dir</code>), use this flag to force <code>wrangler check startup</code> to treat your project as a Pages project.</li>
</ul>
</li>
</ul>
<p>The following global flags work on every command:</p>
<ul>
<li><code>--help</code> <span class="nb-type">boolean</span>
<ul>
<li>Show help.</li>
</ul>
</li>
<li><code>--config</code> <span class="nb-type">string</span> (not supported by Pages)
<ul>
<li>Path to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</li>
</ul>
</li>
<li><code>--cwd</code> <span class="nb-type">string</span>
<ul>
<li>Run as if Wrangler was started in the specified directory instead of the current working directory.</li>
</ul>
</li>
</ul>
