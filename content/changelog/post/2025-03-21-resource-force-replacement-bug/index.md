<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 21, 2025</time><h2 id="post-title">Dozens of Cloudflare Terraform Provider resources now have proper drift detection</h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>In <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare Terraform Provider</a> versions 5.2.0 and above, dozens of resources now have proper drift detection. Before this fix, these resources would indicate they needed to be updated or replaced — even if there was no real change. Now, you can rely on your <code>terraform plan</code> to only show what resources are expected to change.</p>
<p>This issue affected <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">resources</a> related to these products and features:</p>
<ul>
<li>API Shield</li>
<li>Argo Smart Routing</li>
<li>Argo Tiered Caching</li>
<li>Bot Management</li>
<li>BYOIP</li>
<li>D1</li>
<li>DNS</li>
<li>Email Routing</li>
<li>Hyperdrive</li>
<li>Observatory</li>
<li>Pages</li>
<li>R2</li>
<li>Rules</li>
<li>SSL/TLS</li>
<li>Waiting Room</li>
<li>Workers</li>
<li>Zero Trust</li>
</ul>
</div></article></div>
