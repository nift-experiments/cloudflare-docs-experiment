<h2 id="minimal-configuration">Minimal configuration</h2>
<p>The minimum required configuration for using Sandbox SDK:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13528.md")
</div>
<h2 id="required-settings">Required settings</h2>
<p>The Sandbox SDK is built on Cloudflare Containers. Your configuration requires three sections:</p>
<ol>
<li><strong>containers</strong> - Define the container image (your runtime environment)</li>
<li><strong>durable_objects.bindings</strong> - Bind the Sandbox Durable Object to your Worker</li>
<li><strong>migrations</strong> - Initialize the Durable Object class</li>
</ol>
<p>The minimal configuration shown above includes all required settings. For detailed configuration options, refer to the <a href="/workers/wrangler/configuration/#containers">Containers configuration documentation</a>.</p>
<h2 id="backup-storage">Backup storage</h2>
<p>To use the <a href="/sandbox/api/backups/">backup and restore API</a>, you need an R2 bucket binding and presigned URL credentials. The container uploads and downloads backup archives directly to/from R2 using presigned URLs, which requires R2 API token credentials.</p>
<h3 id="1-create-the-r2-bucket"><ol>
<li>Create the R2 bucket</li>
</ol></h3>
<pre><code class="language-sh">npx wrangler r2 bucket create my-backup-bucket&#10;</code></pre>
<h3 id="2-add-the-binding-and-environment-variables"><ol start="2">
<li>Add the binding and environment variables</li>
</ol></h3>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13529.md")
</div>
<h3 id="3-set-r2-api-credentials-as-secrets"><ol start="3">
<li>Set R2 API credentials as secrets</li>
</ol></h3>
<pre><code class="language-sh">npx wrangler secret put R2_ACCESS_KEY_ID&#10;npx wrangler secret put R2_SECRET_ACCESS_KEY&#10;</code></pre>
<p>Create an R2 API token in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> under <strong>R2</strong> &gt; <strong>Overview</strong> &gt; <strong>Manage R2 API Tokens</strong>. The token needs <strong>Object Read &amp; Write</strong> permissions for your backup bucket.</p>
<p>The SDK uses these credentials to generate presigned URLs that allow the container to transfer backup archives directly to and from R2. For a complete setup walkthrough, refer to the <a href="/sandbox/guides/backup-restore/">backup and restore guide</a>.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="binding-not-found">Binding not found</h3>
<p><strong>Error</strong>: <code>TypeError: env.Sandbox is undefined</code></p>
<p><strong>Solution</strong>: Ensure your <code>wrangler.jsonc</code> includes the Durable Objects binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13530.md")
</div>
<h3 id="missing-migrations">Missing migrations</h3>
<p><strong>Error</strong>: Durable Object not initialized</p>
<p><strong>Solution</strong>: Add migrations for the Sandbox class:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13531.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/guides/deploy/">Deploy a Sandbox application</a> - Deploy and keep package and image aligned</li>
<li><a href="/containers/guides/deploy/">Deploy Containers</a> - Containers deploy path</li>
<li><a href="/sandbox/configuration/transport/">Transport modes</a> - Configure HTTP, WebSocket, and RPC transport</li>
<li><a href="/workers/wrangler/">Wrangler documentation</a> - Complete Wrangler reference</li>
<li><a href="/durable-objects/get-started/">Durable Objects setup</a> - DO-specific configuration</li>
<li><a href="/sandbox/configuration/dockerfile/">Dockerfile reference</a> - Custom container images</li>
<li><a href="/sandbox/configuration/environment-variables/">Environment variables</a> - Passing configuration to sandboxes</li>
<li><a href="/sandbox/get-started/">Get Started guide</a> - Initial setup walkthrough</li>
</ul>
