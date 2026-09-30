<h2 id="background">Background</h2>
<p>Connect to databases by configuring connection strings and credentials as <a href="/workers/configuration/secrets/">secrets</a> in your Worker.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="connecting-to-a-regional-database-from-a-worker">Connecting to a regional database from a Worker?</h3>
@markup("md", "content/.markup/bodies/16893.md")
</aside>
<h2 id="database-credentials">Database credentials</h2>
<p>When you rotate or update database credentials, you must update the corresponding <a href="/workers/configuration/secrets/">secrets</a> in your Worker. Use the <a href="/workers/wrangler/commands/general/#secret"><code>wrangler secret put</code></a> command to update secrets securely or update the secret directly in the <a href="https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/settings">Cloudflare dashboard</a>.</p>
<h2 id="database-limits">Database limits</h2>
<p>You can connect to multiple databases by configuring separate sets of secrets for each database connection. Use descriptive secret names to distinguish between different database connections (for example, <code>DATABASE_URL_PROD</code> and <code>DATABASE_URL_STAGING</code>).</p>
<h2 id="popular-providers">Popular providers</h2>
<ul class="directory-listing"><li><a href="/workers/databases/third-party-integrations/neon/">Neon</a></li><li><a href="/workers/databases/third-party-integrations/planetscale/">PlanetScale</a></li><li><a href="/workers/databases/third-party-integrations/supabase/">Supabase</a></li><li><a href="/workers/databases/third-party-integrations/turso/">Turso</a></li><li><a href="/workers/databases/third-party-integrations/upstash/">Upstash</a></li><li><a href="/workers/databases/third-party-integrations/xata/">Xata</a></li></ul>
