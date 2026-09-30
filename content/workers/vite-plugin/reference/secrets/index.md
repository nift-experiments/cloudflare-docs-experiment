<p><a href="/workers/configuration/secrets/">Secrets</a> are typically used for storing sensitive information such as API keys and auth tokens.
For deployed Workers, they are set via the dashboard or Wrangler CLI.</p>
<p>In local development, secrets can be provided to your Worker by using a <a href="/workers/configuration/secrets/#local-development-with-secrets"><code>.dev.vars</code></a> file.
If you are using <a href="/workers/vite-plugin/reference/cloudflare-environments/">Cloudflare Environments</a> then the relevant <code>.dev.vars</code> file will be selected.
For example, <code>CLOUDFLARE_ENV=staging vite dev</code> will load <code>.dev.vars.staging</code> if it exists and fall back to <code>.dev.vars</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17386.md")
</aside>
