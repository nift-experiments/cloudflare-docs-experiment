<h2 id="background">Background</h2>
<p>You can add environment variables, which are a type of binding, to attach text strings or JSON values to your Worker. Environment variables are available on the <a href="/workers/runtime-apis/handlers/fetch/#parameters"><code>env</code> parameter</a> passed to your Worker's <a href="/workers/runtime-apis/handlers/fetch/"><code>fetch</code> event handler</a>.</p>
<p>Text strings and JSON values are not encrypted and are useful for storing application configuration.</p>
<h2 id="add-environment-variables-via-wrangler">Add environment variables via Wrangler</h2>
<p>To add env variables using Wrangler, define text and JSON via the <code>[vars]</code> configuration in your Wrangler file. In the following example, <code>API_HOST</code> and <code>API_ACCOUNT_ID</code> are text values and <code>SERVICE_X_DATA</code> is a JSON value.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16629.md")
</div>
<p>Refer to the following example on how to access the <code>API_HOST</code> environment variable in your Worker code:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16633.md")
</div></div>
<h3 id="import-env-for-global-access">Import <code>env</code> for global access</h3>
<p>You can also import <code>env</code> from <a href="/workers/runtime-apis/bindings/#importing-env-as-a-global"><code>cloudflare:workers</code></a> to access environment variables from anywhere in your code, including outside of request handlers:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16634.md")
</div>
<p>This approach is useful when you need to:</p>
<ul>
<li>Initialize configuration or API clients at the top level of your Worker.</li>
<li>Access environment variables from deeply nested functions without passing <code>env</code> through every function call.</li>
</ul>
<p>For more details, refer to <a href="/workers/runtime-apis/bindings/#importing-env-as-a-global">Importing <code>env</code> as a global</a>.</p>
<h3 id="configuring-different-environments-in-wrangler">Configuring different environments in Wrangler</h3>
<p><a href="/workers/wrangler/environments">Environments in Wrangler</a> let you specify different configurations for the same Worker, including different values for <code>vars</code> in each environment.
As <code>vars</code> is a <a href="/workers/wrangler/configuration/#non-inheritable-keys">non-inheritable key</a>, they are not inherited by environments and must be specified for each environment.</p>
<p>The example below sets up two environments, <code>staging</code> and <code>production</code>, with different values for <code>API_HOST</code>.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16635.md")
</div>
<p>To run Wrangler commands in specific environments, you can pass in the <code>--env</code> or <code>-e</code> flag. For example, you can develop the Worker in an environment called <code>staging</code> by running <code>npx wrangler dev --env staging</code>, and deploy it with <code>npx wrangler deploy --env staging</code>.</p>
<p>Learn about <a href="/workers/wrangler/environments">environments in Wrangler</a>.</p>
<h2 id="add-environment-variables-via-the-dashboard">Add environment variables via the dashboard</h2>
<p>To add environment variables via the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Overview</strong>, select your Worker.</li>
<li>Select <strong>Settings</strong>.</li>
<li>Under <strong>Variables and Secrets</strong>, select <strong>Add</strong>.</li>
<li>Select a <strong>Type</strong>, input a <strong>Variable name</strong>, and input its <strong>Value</strong>. This variable will be made available to your Worker.</li>
<li>(Optional) To add multiple environment variables, select <strong>Add variable</strong>.</li>
<li>Select <strong>Deploy</strong> to implement your changes.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="plaintext-strings-and-secrets">Plaintext strings and secrets</h3>
@markup("md", "content/.markup/bodies/16628.md")
</aside>
<h2 id="compare-secrets-and-environment-variables">Compare secrets and environment variables</h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="use-secrets-for-sensitive-information">Use secrets for sensitive information</h3>
@markup("md", "content/.markup/bodies/16627.md")
</aside>
<p><a href="/workers/configuration/secrets/">Secrets</a> are <a href="/workers/configuration/environment-variables/">environment variables</a>. The difference is secret values are not visible within Wrangler or Cloudflare dashboard after you define them. This means that sensitive data, including passwords or API tokens, should always be encrypted to prevent data leaks. To your Worker, there is no difference between an environment variable and a secret. The secret's value is passed through as defined.</p>
<h3 id="local-development-with-secrets">Local development with secrets</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16626.md")
</aside>
<p>Put secrets for use in local development in either a <code>.dev.vars</code> file or a <code>.env</code> file, in the same directory as the Wrangler configuration file.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16625.md")
</aside>
<aside class="nb-aside info">
@markup("md", "content/.markup/bodies/16624.md")
</aside>
<p>These files should be formatted using the <a href="https://hexdocs.pm/dotenvy/dotenv-file-format.html">dotenv</a> syntax. For example:</p>
<pre><code class="language-bash">SECRET_KEY=&quot;value&quot;&#10;API_TOKEN=&quot;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9&quot;&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="do-not-commit-secrets-to-git">Do not commit secrets to git</h3>
@markup("md", "content/.markup/bodies/16623.md")
</aside>
<p>To set different secrets for each Cloudflare environment, create files named <code>.dev.vars.&lt;environment-name&gt;</code> or <code>.env.&lt;environment-name&gt;</code>.</p>
<p>When you select a Cloudflare environment in your local development, the corresponding environment-specific file will be loaded ahead of the generic <code>.dev.vars</code> (or <code>.env</code>) file.</p>
<ul>
<li>When using <code>.dev.vars.&lt;environment-name&gt;</code> files, all secrets must be defined per environment. If <code>.dev.vars.&lt;environment-name&gt;</code> exists then only this will be loaded; the <code>.dev.vars</code> file will not be loaded.</li>
<li>In contrast, all matching <code>.env</code> files are loaded and the values are merged. For each variable, the value from the most specific file is used, with the following precedence:
<ul>
<li><code>.env.&lt;environment-name&gt;.local</code> (most specific)</li>
<li><code>.env.local</code></li>
<li><code>.env.&lt;environment-name&gt;</code></li>
<li><code>.env</code> (least specific)</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="controlling-env-handling">Controlling `.env` handling</h3>
@markup("md", "content/.markup/bodies/16622.md")
</aside>
<h2 id="environment-variables-and-node-js-compatibility">Environment variables and Node.js compatibility</h2>
<p>When you enable <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code></a> and the <a href="/workers/configuration/compatibility-flags/#nodejs_compat_populate_process_env"><code>nodejs_compat_populate_process_env</code></a> compatibility flag (enabled by default for compatibility dates on or after 2025-04-01), environment variables are available via the global <code>process.env</code>.</p>
<p>The <code>process.env</code> will be populated lazily the first time that <code>process</code> is accessed
in the worker.</p>
<p>Text variable values are exposed directly.</p>
<p>JSON variable values that evaluate to string values are exposed as the parsed value.</p>
<p>JSON variable values that do not evaluate to string values are exposed as the raw
JSON string.</p>
<p>For example, imagine a Worker with three environment variables, two text values, and
one JSON value:</p>
<pre><code>[vars]&#10;FOO =  &quot;abc&quot;&#10;BAR =  &quot;abc&quot;&#10;BAZ = { &quot;a&quot;: 123 }&#10;</code></pre>
<p>Environment variables can be added using either the <code>wrangler.{json|jsonc|toml}</code> file or via the Cloudflare
dashboard UI.</p>
<p>The values of <code>process.env.FOO</code> and <code>process.env.BAR</code> will each be the
JavaScript string <code>&quot;abc&quot;</code>.</p>
<p>The value of <code>process.env.BAZ</code> will be the JSON-encoded string <code>&quot;{ \&quot;a\&quot;: 123 }&quot;</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16621.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>Migrating environment variables from <a href="/workers/reference/migrate-to-module-workers/#environment-variables">Service Worker format to ES modules syntax</a>.</li>
</ul>
