<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 21, 2025</time><h2 id="post-title">Cloudflare Terraform Provider now properly redacts sensitive values</h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>In the <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare Terraform Provider</a> versions 5.2.0 and above, sensitive properties of resources are redacted in logs. Sensitive properties in <a href="https://raw.githubusercontent.com/cloudflare/api-schemas/refs/heads/main/openapi.yaml">Cloudflare's OpenAPI Schema</a> are now annotated with <code>x-sensitive: true</code>. This results in proper auto-generation of the corresponding Terraform resources, and prevents sensitive values from being shown when you run Terraform commands.</p>
<p>This issue affected <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">resources</a> related to these products and features:</p>
<ul>
<li>Alerts and Audit Logs</li>
<li>Device API</li>
<li>DLP</li>
<li>DNS</li>
<li>Magic Visibility</li>
<li>Magic WAN</li>
<li>TLS Certs and Hostnames</li>
<li>Tunnels</li>
<li>Turnstile</li>
<li>Workers</li>
<li>Zaraz</li>
</ul>
</div></article></div>
