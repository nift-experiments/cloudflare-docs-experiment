<p><a href="/cloudflare-challenges/concepts/clearance/#pre-clearance-support-in-turnstile">Pre-clearance</a> allows Turnstile to issue clearance cookies that can be used across your Cloudflare-protected domains. This feature requires specific hostname configuration for proper functionality.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>For pre-clearance to work correctly, you must:</p>
<ol>
<li>
<p>Use a registered Cloudflare zone.</p>
<p>The hostname must be a zone registered in your Cloudflare account. When configuring your widget via the dashboard, you can select from existing zones.</p>
</li>
<li>
<p>Select the registered Cloudflare zone with intended WAF rule to set pre-clearance.</p>
<p>The zone you select must contain the WAF rule you wish to set pre-clearance through Turnstile.</p>
<p>For example, if you have <code>example.com</code> and <code>app.example.com</code> as registered zones and you want to have Turnstile issue pre-clearance for <code>app.example.com</code>, you must select <code>app.example.com</code>.</p>
</li>
</ol>
<h2 id="validation">Validation</h2>
<p>The clearance cookie <code>cf_clearance</code> will only be accepted on domains that match the widget's configured hostnames, are registered as zones in your Cloudflare account, and have challenges enabled through Cloudflare's security settings.</p>
<p>If pre-clearance is configured incorrectly, clearance cookies may become invalid and lead to additional challenge requests.</p>
