<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 11, 2025</time><h2 id="post-title">NSEC3 support for DNSSEC</h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><p>Enterprise customers can now select NSEC3 as method for proof of non-existence on their zones.</p>
<p>What's new:</p>
<ul>
<li>
<p><strong>NSEC3 support for live-signed zones</strong> – For both primary and secondary zones that are configured to be live-signed (also known as &quot;on-the-fly signing&quot;), NSEC3 can now be selected as proof of non-existence.</p>
</li>
<li>
<p><strong>NSEC3 support for pre-signed zones</strong> – Secondary zones that are transferred to Cloudflare in a <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/#set-up-pre-signed-dnssec">pre-signed setup</a> now also support NSEC3 as proof of non-existence.</p>
</li>
</ul>
<p>For more information and how to enable NSEC3, refer to the <a href="/dns/dnssec/enable-nsec3/">NSEC3 documentation</a>.</p>
</div></article></div>
