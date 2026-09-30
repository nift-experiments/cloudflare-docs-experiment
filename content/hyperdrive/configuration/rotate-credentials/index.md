<p>You can change the connection information and credentials of your Hyperdrive configuration in one of two ways:</p>
<ol>
<li>Create a new Hyperdrive configuration with the new connection information, and update your Worker to use the new Hyperdrive configuration.</li>
<li>Update the existing Hyperdrive configuration with the new connection information and credentials.</li>
</ol>
<h2 id="use-a-new-hyperdrive-configuration">Use a new Hyperdrive configuration</h2>
<p>Creating a new Hyperdrive configuration to update your database credentials allows you to keep your existing Hyperdrive configuration unchanged, gradually migrate your Worker to the new Hyperdrive configuration, and easily roll back to the previous configuration if needed.</p>
<p>To create a Hyperdrive configuration that connects to an existing PostgreSQL or MySQL database, use the <a href="/workers/wrangler/install-and-update/">Wrangler</a> CLI or the <a href="https://dash.cloudflare.com/?to=/:account/workers/hyperdrive">Cloudflare dashboard</a>.</p>
<pre><code class="language-sh">&#35; wrangler v3.11 and above required&#10;npx wrangler hyperdrive create my-updated-hyperdrive --connection-string=&quot;&lt;YOUR_CONNECTION_STRING&gt;&quot;&#10;</code></pre>
<p>The command above will output the ID of your Hyperdrive. Set this ID in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> for your Workers project:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9045.md")
</div>
<p>To update your Worker to use the new Hyperdrive configuration, redeploy your Worker or use <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployments</a>.</p>
<h2 id="update-the-existing-hyperdrive-configuration">Update the existing Hyperdrive configuration</h2>
<p>You can update the configuration of an existing Hyperdrive configuration using the <a href="/workers/wrangler/install-and-update/">wrangler CLI</a>.</p>
<pre><code class="language-sh">&#35; wrangler v3.11 and above required&#10;npx wrangler hyperdrive update &lt;HYPERDRIVE_CONFIG_ID&gt; --origin-host &lt;YOUR_ORIGIN_HOST&gt; --origin-password &lt;YOUR_ORIGIN_PASSWORD&gt; --origin-user &lt;YOUR_ORIGIN_USERNAME&gt; --database &lt;YOUR_DATABASE&gt; --origin-port &lt;YOUR_ORIGIN_PORT&gt;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9044.md")
</aside>
