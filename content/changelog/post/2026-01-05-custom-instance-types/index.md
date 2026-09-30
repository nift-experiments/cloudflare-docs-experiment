<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 5, 2026</time><h2 id="post-title">Custom container instance types now available for all users</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>Custom instance types are now enabled for all <a href="/containers">Cloudflare Containers</a> users. You can now specify specific vCPU, memory, and disk amounts, rather than being limited to pre-defined <a href="/containers/platform/limits/#instance-types">instance types</a>. Previously, only select Enterprise customers were able to customize their instance type.</p>
<p>To use a custom instance type, specify the <code>instance_type</code> property as an object with <code>vcpu</code>, <code>memory_mib</code>, and <code>disk_mb</code> fields in your Wrangler configuration:</p>
<pre><code class="language-toml">[[containers]]&#10;image = &quot;./Dockerfile&quot;&#10;instance_type = { vcpu = 2, memory_mib = 6144, disk_mb = 12000 }&#10;</code></pre>
<p>Individual limits for custom instance types are based on the <code>standard-4</code> instance type (4 vCPU, 12 GiB memory, 20 GB disk). You must allocate at least 1 vCPU for custom instance types. For workloads requiring less than 1 vCPU, use the predefined instance types like <code>lite</code> or <code>basic</code>.</p>
<p>See the <a href="/containers/platform/limits/#custom-instance-types">limits documentation</a> for the full list of constraints on custom instance types.
See the <a href="/containers/get-started/">getting started guide</a> to deploy your first Container,</p>
</div></article></div>
