<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 19, 2024</time><h2 id="post-title">Regionalized Generic Tiered Cache for higher hit ratios</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now achieve higher cache hit ratios with <a href="/cache/how-to/tiered-cache/#generic-global-tiered-cache">Generic Global Tiered Cache</a>. Regional content hashing routes content consistently to the same upper-tier data centers, eliminating redundant caching and reducing origin load.</p>
<h4 id="how-it-works">How it works</h4>
<p>Regional content hashing groups data centers by region and uses consistent hashing to route content to designated upper-tier caches:</p>
<ul>
<li>Same content always routes to the same upper-tier data center within a region.</li>
<li>Eliminates redundant copies across multiple upper-tier caches.</li>
<li>Increases the likelihood of cache HITs for the same content.</li>
</ul>
<h4 id="example">Example</h4>
<p>A popular image requested from multiple edge locations in a region:</p>
<ul>
<li><strong>Before</strong>: Cached at 3-4 different upper-tier data centers</li>
<li><strong>After</strong>: Cached at 1 designated upper-tier data center</li>
<li><strong>Result</strong>: 3-4x fewer cache MISSes, reducing origin load and improving performance</li>
</ul>
<h4 id="get-started">Get started</h4>
<p>To get started, enable <a href="/cache/how-to/tiered-cache/#generic-global-tiered-cache">Generic Global Tiered Cache</a> on your zone.</p>
</div></article></div>
