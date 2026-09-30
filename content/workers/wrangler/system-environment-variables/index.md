<p>System environment variables are local environment variables that can change Wrangler's behavior. There are three ways to set system environment variables:</p>
<ol>
<li>
<p>Create an <code>.env</code> file in your project directory. Set the values of your environment variables in your <a href="/workers/wrangler/system-environment-variables/#example-env-file"><code>.env</code></a> file. This is the recommended way to set these variables, as it persists the values between Wrangler sessions.</p>
</li>
<li>
<p>Inline the values in your Wrangler command. For example, <code>WRANGLER_LOG=&quot;debug&quot; npx wrangler deploy</code> will set the value of <code>WRANGLER_LOG</code> to <code>&quot;debug&quot;</code> for this execution of the command.</p>
</li>
<li>
<p>Set the values in your shell environment. For example, if you are using Z shell, adding <code>export CLOUDFLARE_API_TOKEN=...</code> to your <code>~/.zshrc</code> file will set this token as part of your shell configuration.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15905.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15904.md")
</aside>
<h2 id="supported-environment-variables">Supported environment variables</h2>
<p>Wrangler supports the following environment variables:</p>
<ul>
<li>
<p><code>CLOUDFLARE_ACCOUNT_ID</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> for the Workers related account.</li>
</ul>
</li>
<li>
<p><code>CLOUDFLARE_API_TOKEN</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The <a href="/fundamentals/api/get-started/create-token/">API token</a> for your Cloudflare account, can be used for authentication for situations like CI/CD, and other automation.</li>
</ul>
</li>
<li>
<p><code>CLOUDFLARE_API_KEY</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The API key for your Cloudflare account, usually used for older authentication method with <code>CLOUDFLARE_EMAIL=</code>.</li>
</ul>
</li>
<li>
<p><code>CLOUDFLARE_EMAIL</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The email address associated with your Cloudflare account, usually used for older authentication method with <code>CLOUDFLARE_API_KEY=</code>.</li>
</ul>
</li>
<li>
<p><code>CLOUDFLARE_ACCESS_CLIENT_ID</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The Client ID of a <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Cloudflare Access Service Token</a>, used to authenticate with Access-protected domains in non-interactive environments such as CI/CD pipelines. Must be set together with <code>CLOUDFLARE_ACCESS_CLIENT_SECRET</code>. When both variables are set, Wrangler authenticates using the service token instead of launching <code>cloudflared access login</code>. For the full Access policy and service token setup, refer to <a href="/workers/local-development/#connect-to-access-protected-workers">Connect to Access-protected Workers</a>.</li>
</ul>
</li>
<li>
<p><code>CLOUDFLARE_ACCESS_CLIENT_SECRET</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The Client Secret of a <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Cloudflare Access Service Token</a>, used together with <code>CLOUDFLARE_ACCESS_CLIENT_ID</code> to authenticate with Access-protected domains in non-interactive environments. For the full Access policy and service token setup, refer to <a href="/workers/local-development/#connect-to-access-protected-workers">Connect to Access-protected Workers</a>.</li>
</ul>
</li>
<li>
<p><code>CLOUDFLARE_AUTH_USE_KEYRING</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Options for this are <code>true</code> and <code>false</code>. Defaults to unset. Overrides the persistent preference set by <code>wrangler login --use-keyring</code> / <code>--no-use-keyring</code> for a single invocation. When <code>true</code>, Wrangler stores OAuth credentials in an encrypted file with the encryption key held in the OS keychain, and exits with an error if the keychain backend is unavailable. When <code>false</code>, Wrangler uses the legacy plaintext TOML file even if the persistent preference is enabled. Refer to <a href="/workers/wrangler/commands/general/#storing-oauth-credentials-in-the-os-keychain">Storing OAuth credentials in the OS keychain</a> for details.</li>
</ul>
</li>
<li>
<p><code>CLOUDFLARE_ENV</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The <a href="/workers/wrangler/environments/">environment</a> to use for Wrangler commands. This allows you to select an environment without using the <code>--env</code> flag. For example, <code>CLOUDFLARE_ENV=production wrangler deploy</code> will deploy to the <code>production</code> environment. The <code>--env</code> command line argument takes precedence over this environment variable.</li>
</ul>
</li>
<li>
<p><code>NODE_ENV</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Sets the value of <code>process.env.NODE_ENV</code> in your Worker code. Defaults to <code>&quot;development&quot;</code> for <code>wrangler dev</code> and <code>&quot;production&quot;</code> for <code>wrangler deploy</code> and <code>wrangler versions upload</code>. Refer to <a href="/workers/wrangler/bundling/#node_env">Bundling</a> for more information.</li>
</ul>
</li>
<li>
<p><code>WRANGLER_SEND_METRICS</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Options for this are <code>true</code> and <code>false</code>. Defaults to <code>true</code>. Controls whether Wrangler can send anonymous usage data to Cloudflare for this project. You can learn more about this in our <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/wrangler/telemetry.md">data policy</a>.</li>
</ul>
</li>
<li>
<p><code>WRANGLER_SEND_ERROR_REPORTS</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Options for this are <code>true</code> and <code>false</code>. Defaults to <code>undefined</code>. Controls whether Wrangler can send non-user error reports to Cloudflare for this project. If <code>undefined</code>, Wrangler will ask the user whether to send an error report each time there is a non-user error.</li>
</ul>
</li>
<li>
<p><code>CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_&lt;BINDING_NAME&gt;</code><span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The <a href="/hyperdrive/configuration/local-development/">local connection string</a> for your database to use in local development with <a href="/hyperdrive/">Hyperdrive</a>. For example, if the binding for your Hyperdrive is named <code>PROD_DB</code>, this would be <code>CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_PROD_DB=&quot;postgres://user:password@127.0.0.1:5432/testdb&quot;</code>. Each Hyperdrive is uniquely distinguished by the binding name.</li>
</ul>
</li>
<li>
<p><code>CLOUDFLARE_API_BASE_URL</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The default value is <code>&quot;https://api.cloudflare.com/client/v4&quot;</code>.</li>
</ul>
</li>
<li>
<p><code>WRANGLER_LOG</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Options for Logging levels are <code>&quot;none&quot;</code>, <code>&quot;error&quot;</code>, <code>&quot;warn&quot;</code>, <code>&quot;info&quot;</code>, <code>&quot;log&quot;</code> and <code>&quot;debug&quot;</code>. Levels are case-insensitive and default to <code>&quot;log&quot;</code>. If an invalid level is specified, Wrangler will fallback to the default. Logs can include requests to Cloudflare's API, any usage data being collected, and more verbose error logs.</li>
</ul>
</li>
<li>
<p><code>WRANGLER_LOG_PATH</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A file or directory path where Wrangler will write debug logs. If the path ends in <code>.log</code>, Wrangler will consider this the path to a file where all logs will be written. Otherwise, Wrangler will treat the path as a directory where it will write one or more log files using a timestamp for the filenames.</li>
</ul>
</li>
<li>
<p><code>WRANGLER_LOG_SANITIZE</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Options for this are <code>true</code> and <code>false</code>. Defaults to <code>true</code>. Controls whether Wrangler will sanitize any sensitive information from logs written to the console or to a log file. Sensitive information includes API tokens, email addresses, account IDs, and more.</li>
</ul>
</li>
<li>
<p><code>FORCE_COLOR</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>By setting this to <code>0</code>, you can disable Wrangler's colorised output, which makes it easier to read with some terminal setups. For example, <code>FORCE_COLOR=0</code>.</li>
</ul>
</li>
<li>
<p><code>WRANGLER_HTTPS_KEY_PATH</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Path to a custom HTTPS certificate key when running <code>wrangler dev</code>, to be used with <code>WRANGLER_HTTPS_CERT_PATH</code>.</li>
</ul>
</li>
<li>
<p><code>WRANGLER_HTTPS_CERT_PATH</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Path to a custom HTTPS certificate when running <code>wrangler dev</code>, to be used with <code>WRANGLER_HTTPS_KEY_PATH</code>.</li>
</ul>
</li>
<li>
<p><code>DOCKER_HOST</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Used for local development of <a href="/containers/guides/local-dev">Containers</a>. Wrangler will attempt to automatically find the correct socket to use to communicate with your container engine. If that does not work (usually surfacing as an <code>internal error</code> when attempting to connect to your Container), you can try setting the socket path using this environment variable.</li>
</ul>
</li>
<li>
<p><code>WRANGLER_R2_SQL_AUTH_TOKEN</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>API token used for executing queries with <a href="/r2-sql">R2 SQL</a>.</li>
</ul>
</li>
<li>
<p><code>WRANGLER_OUTPUT_FILE_PATH</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Specifies a file path where Wrangler will write output data in <a href="https://github.com/ndjson/ndjson-spec">ND-JSON</a> (newline-delimited JSON) format. Each line in the file is a separate JSON object containing information about Wrangler operations such as deployments, version uploads, and errors. This is useful for CI/CD pipelines and automation tools that need to programmatically access deployment information. If both <code>WRANGLER_OUTPUT_FILE_PATH</code> and <code>WRANGLER_OUTPUT_FILE_DIRECTORY</code> are set, <code>WRANGLER_OUTPUT_FILE_PATH</code> takes precedence.</li>
</ul>
</li>
<li>
<p><code>WRANGLER_OUTPUT_FILE_DIRECTORY</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Specifies a directory where Wrangler will create a randomly-named file (format: <code>wrangler-output-&lt;timestamp&gt;-&lt;random&gt;.json</code>) to write output data in <a href="https://github.com/ndjson/ndjson-spec">ND-JSON</a> format. This is useful when you want to keep output files organized in a specific directory but do not need to control the exact filename. If both <code>WRANGLER_OUTPUT_FILE_PATH</code> and <code>WRANGLER_OUTPUT_FILE_DIRECTORY</code> are set, <code>WRANGLER_OUTPUT_FILE_PATH</code> takes precedence.</li>
</ul>
</li>
<li>
<p><code>WRANGLER_CACHE_DIR</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Custom directory for Wrangler's cache files. When set, this overrides the default cache location (<code>node_modules/.cache/wrangler</code>). Useful for environments that do not use a traditional <code>node_modules</code> directory, such as Yarn PnP.</li>
</ul>
</li>
<li>
<p><code>MINIFLARE_CACHE_DIR</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Custom directory for Miniflare's <code>cf.json</code> cache file, used during local development with <code>wrangler dev</code>. When set, this overrides the default cache location (<code>node_modules/.mf</code>). Useful for environments that do not use a traditional <code>node_modules</code> directory, such as Yarn PnP.</li>
</ul>
</li>
<li>
<p><code>CLOUDFLARE_CF_FETCH_ENABLED</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Controls whether <a href="/workers/testing/miniflare/">Miniflare</a> fetches the <code>cf.json</code> file containing <a href="/workers/runtime-apis/request/#the-cf-property-requestinitcfproperties"><code>Request.cf</code></a> properties from Cloudflare during local development. Set to <code>&quot;false&quot;</code> or <code>&quot;0&quot;</code> to disable fetching entirely and use fallback data. No <code>node_modules/.mf/cf.json</code> file will be created when disabled. Defaults to <code>&quot;true&quot;</code>. This is particularly useful for non-JavaScript projects (such as Rust or Go Workers) that do not want a <code>node_modules</code> directory created automatically. The explicit <code>cf</code> option in the <a href="/workers/testing/miniflare/get-started/#requestcf-object">Miniflare API</a> takes precedence over this environment variable.</li>
</ul>
</li>
<li>
<p><code>CLOUDFLARE_CF_FETCH_PATH</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Specifies a custom path for caching the <code>cf.json</code> file, overriding the default <code>node_modules/.mf/cf.json</code> location. This is useful for multi-project setups where you want a shared cache location, or for projects that want to store the cache outside of <code>node_modules</code>. The explicit <code>cf</code> option in the <a href="/workers/testing/miniflare/get-started/#requestcf-object">Miniflare API</a> takes precedence over this environment variable, and <code>CLOUDFLARE_CF_FETCH_ENABLED=false</code> takes precedence over this variable.</li>
</ul>
</li>
</ul>
<h3 id="example-output-file">Example output file</h3>
<p>When these environment variables are set, Wrangler writes one JSON object per line to the output file. Each entry includes a <code>timestamp</code> field and a <code>type</code> field indicating the kind of operation. Here is an example of what the file might contain after running <code>wrangler deploy</code>:</p>
<pre><code class="language-json">{&quot;type&quot;:&quot;wrangler-session&quot;,&quot;version&quot;:1,&quot;wrangler_version&quot;:&quot;3.78.0&quot;,&quot;command_line_args&quot;:[&quot;deploy&quot;],&quot;log_file_path&quot;:&quot;/path/to/logs/wrangler-2024-11-03_12-00-00_abc.log&quot;,&quot;timestamp&quot;:&quot;2024-11-03T12:00:00.000Z&quot;}&#10;{&quot;type&quot;:&quot;deploy&quot;,&quot;version&quot;:1,&quot;worker_name&quot;:&quot;my-worker&quot;,&quot;worker_tag&quot;:&quot;abc123def456&quot;,&quot;version_id&quot;:&quot;v1-abc123&quot;,&quot;targets&quot;:[&quot;https://my-worker.example.workers.dev&quot;],&quot;worker_name_overridden&quot;:false,&quot;wrangler_environment&quot;:&quot;production&quot;,&quot;timestamp&quot;:&quot;2024-11-03T12:00:05.000Z&quot;}&#10;</code></pre>
<p>The <code>wrangler-session</code> entry is written when Wrangler starts and contains information about the command being run. The <code>deploy</code> entry is written when a deployment completes successfully and includes the worker name, version ID, and deployment URLs.</p>
<p>Other entry types include:</p>
<ul>
<li><code>version-upload</code> - Written by <code>wrangler versions upload</code> with version ID and preview URLs</li>
<li><code>version-deploy</code> - Written by <code>wrangler versions deploy</code> with deployment information</li>
<li><code>pages-deploy</code> - Written by <code>wrangler pages deploy</code> with Pages deployment details</li>
<li><code>command-failed</code> - Written when a command fails, including error code and message</li>
</ul>
<h2 id="example-env-file">Example <code>.env</code> file</h2>
<p>The following is an example <code>.env</code> file:</p>
<pre><code class="language-bash">CLOUDFLARE_ACCOUNT_ID=&lt;YOUR_ACCOUNT_ID_VALUE&gt;&#10;CLOUDFLARE_API_TOKEN=&lt;YOUR_API_TOKEN_VALUE&gt;&#10;CLOUDFLARE_EMAIL=&lt;YOUR_EMAIL&gt;&#10;WRANGLER_SEND_METRICS=true&#10;CLOUDFLARE_API_BASE_URL=https://api.cloudflare.com/client/v4&#10;WRANGLER_LOG=debug&#10;WRANGLER_LOG_PATH=../Desktop/my-logs/my-log-file.log&#10;WRANGLER_R2_SQL_AUTH_TOKEN=&lt;YOUR_R2_API_TOKEN_VALUE&gt;&#10;CLOUDFLARE_CF_FETCH_ENABLED=false&#10;</code></pre>
<h2 id="deprecated-global-variables">Deprecated global variables</h2>
<p>The following variables are deprecated. Use the new variables listed above to prevent any issues or unwanted messaging.</p>
<ul>
<li><code>CF_ACCOUNT_ID</code></li>
<li><code>CF_API_TOKEN</code></li>
<li><code>CF_API_KEY</code></li>
<li><code>CF_EMAIL</code></li>
<li><code>CF_API_BASE_URL</code></li>
</ul>
