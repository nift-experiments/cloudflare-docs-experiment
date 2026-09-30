<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 5, 2025</time><h2 id="post-title">Increased WAF payload limit for all plans</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>Cloudflare WAF now inspects request-payload size of up to 1 MB across all plans to enhance our detection capabilities for React RCE (CVE-2025-55182).</p>
<p><strong>Key Findings</strong></p>
<p>React payloads commonly have a default maximum size of 1 MB. Cloudflare WAF previously inspected up to 128 KB on Enterprise plans, with even lower limits on other plans.</p>
<p><strong>Update:</strong> We later reinstated the maximum request-payload size the Cloudflare WAF inspects. Refer to <a href="/changelog/2025-12-05-waf-max-payload-size-change/">Updating the WAF maximum payload values</a> for details.</p>
</div></article></div>
