<p>Hyperdrive can be used when developing and testing your Workers locally. <a href="/workers/wrangler/install-and-update/">Wrangler</a>, the command-line interface for Workers, provides two options for local development:</p>
<ul>
<li><strong><code>wrangler dev</code></strong> (default): Runs your Worker code locally on your machine. You configure a <code>localConnectionString</code> to connect directly to a database (either local or remote). Hyperdrive query caching does not take effect in this mode.</li>
<li><strong><code>wrangler dev --remote</code></strong>: Runs your Worker on Cloudflare's using your deployed Hyperdrive configuration. This is useful for testing with Hyperdrive's connection pooling and query caching enabled.</li>
</ul>
<h2 id="use-wrangler-dev">Use <code>wrangler dev</code></h2>
<p>By default, <code>wrangler dev</code> runs your Worker code locally on your machine. To connect to a database during local development, configure a <code>localConnectionString</code> that points directly to your database.</p>
<p>The <code>localConnectionString</code> works with both local and remote databases:</p>
<ul>
<li><strong>Local databases</strong>: Connect to a database instance running on your machine (for example, <code>postgres://user:password@localhost:5432/database</code>)</li>
<li><strong>Remote databases</strong>: Connect directly to remote databases over TLS (for example, <code>postgres://user:password@remote-host.example.com:5432/database?sslmode=require</code> or <code>mysql://user:password@remote-host.example.com:3306/database?sslMode=required</code>). You must specify the SSL/TLS mode if required.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9048.md")
</aside>
<h3 id="configure-with-environment-variable">Configure with environment variable</h3>
<p>The recommended approach is to use an environment variable to avoid committing credentials to source control:</p>
<pre><code class="language-sh">&#35; Your configured Hyperdrive binding is &quot;HYPERDRIVE&quot;&#10;export CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_HYPERDRIVE=&quot;postgres://user:password@your-database-host:5432/database&quot;&#10;npx wrangler dev&#10;</code></pre>
<p>The environment variable format is <code>CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_&lt;BINDING_NAME&gt;</code>, where <code>&lt;BINDING_NAME&gt;</code> is the name of the binding assigned to your Hyperdrive in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<p>To unset an environment variable: <code>unset CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_&lt;BINDING_NAME&gt;</code></p>
<p>For example, to set the connection string for a local database:</p>
<pre><code class="language-sh">export CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_HYPERDRIVE=&quot;postgres://user:password@localhost:5432/databasename&quot;&#10;npx wrangler dev&#10;</code></pre>
<h3 id="configure-in-wrangler-configuration-file">Configure in Wrangler configuration file</h3>
<p>Alternatively, you can set <code>localConnectionString</code> in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9049.md")
</div>
<p>If both an environment variable and <code>localConnectionString</code> in the Wrangler configuration file are set, the environment variable takes precedence.</p>
<h2 id="use-wrangler-dev-remote">Use <code>wrangler dev --remote</code></h2>
<p>When you run <code>wrangler dev --remote</code>, your Worker runs in Cloudflare's network and uses your deployed Hyperdrive configuration. This means:</p>
<ul>
<li>Your Worker code executes in Cloudflare's production environment, not locally</li>
<li>Hyperdrive's connection pooling and query caching are active</li>
<li>You connect to the database configured in your Hyperdrive configuration (created with <code>wrangler hyperdrive create</code>)</li>
<li>Changes made during the session interact with remote resources</li>
</ul>
<p>This mode is useful for testing how your Worker behaves with Hyperdrive's features enabled before deploying.</p>
<p>Configure your Hyperdrive binding in <code>wrangler.jsonc</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9050.md")
</div>
<p>To start a remote development session:</p>
<pre><code class="language-sh">npx wrangler dev --remote&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9047.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/9046.md")
</aside>
<p>Refer to the <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code> documentation</a> to learn more about how to configure a local development session.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>Use <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> to run your Worker and Hyperdrive locally and debug issues before deploying.</li>
<li>Learn <a href="/hyperdrive/concepts/how-hyperdrive-works/">how Hyperdrive works</a>.</li>
<li>Understand how to <a href="/hyperdrive/concepts/query-caching/">configure query caching in Hyperdrive</a>.</li>
</ul>
