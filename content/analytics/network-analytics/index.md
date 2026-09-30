<p>Cloudflare Network Analytics (version 2) provides near real-time visibility into network and transport-layer traffic patterns and DDoS attacks. Network Analytics visualizes packet and bit-level data, the same data available via the Network Analytics dataset of the GraphQL Analytics API.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="requirements">Requirements</h3>
@markup("md", "content/.markup/bodies/3126.md")
</aside>
<p>For a technical deep-dive into Network Analytics, refer to our <a href="https://blog.cloudflare.com/building-network-analytics-v2/">blog post</a>.</p>
<h2 id="remarks">Remarks</h2>
<ul>
<li>
<p>The Network Analytics logs refer to IP traffic of Magic Transit customer prefixes/leased IP addresses or Spectrum applications. These logs are not directly associated with the <a href="/fundamentals/concepts/accounts-and-zones/#zones">zones</a> in your Cloudflare account.</p>
</li>
<li>
<p>The data retention for Network Analytics is 16 weeks. Additionally, data older than eight weeks might have lower resolution when using narrow time frames.</p>
</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/analytics/graphql-api/">Cloudflare GraphQL API</a></li>
<li><a href="/logs/logpush/">Cloudflare Logpush</a></li>
<li><a href="/analytics/graphql-api/migration-guides/network-analytics-v2/">Migrating from Network Analytics v1 to Network Analytics v2</a></li>
</ul>
