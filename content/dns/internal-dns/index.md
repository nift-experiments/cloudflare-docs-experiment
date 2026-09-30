<div class="nb-description">
@markup("md", "content/.markup/bodies/7625.md")
</div>
<div class="nb-plan">
<p>Enterprise-only</p>
</div>
<p>Manage DNS records that should only be accessible within your private network. Internal DNS <a href="/dns/internal-dns/internal-zones/">zones</a> and <a href="/dns/internal-dns/dns-views/">views</a> pair up with <a href="/cloudflare-one/traffic-policies/resolver-policies/">Gateway resolver policies</a> so that you can control how a DNS query should be responded to according to query context, such as query source IP.</p>
<p>Internal DNS is included with <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> for Enterprise customers. There is no additional SKU or separate subscription required.</p>
<h2 id="architecture-overview">Architecture overview</h2>
<p>You can use different <a href="/dns/internal-dns/connectivity/">connectivity options</a> to on-ramp your traffic to Cloudflare. Then, Cloudflare Gateway resolver acts as an interface between the DNS client and internal DNS zones.</p>
<p>Internal DNS zones do not get assigned Cloudflare nameservers and can only be queried via Cloudflare Gateway resolver.</p>
<pre><code class="language-mermaid">flowchart LR&#10;        accTitle: Internal DNS query overview&#10;        accDescr: Diagram comparing internal DNS query with public DNS&#10;        A[Client]&#10;        subgraph Cloudflare account&#10;        subgraph Gateway&#10;				B[Default 1.1.1.1 resolver]&#10;        X[Resolver policy selecting an internal DNS view]&#10;        end&#10;        subgraph Authoritative DNS&#10;        Y[(Public DNS)]&#10;				Z[(Internal DNS)]&#10;        end&#10;        end&#10;&#10;			  C[Public resolver]&#10;&#10;        B --Query--&gt; Y&#10;        X --Query + View ID--&gt; Z&#10;        A --Query--&gt; B&#10;				A --Query--&gt; X&#10;				C --Query--&gt; Y&#10;</code></pre>
<p>Internal DNS zones are grouped into DNS views, which are selected by the resolver policy you define. Views are usually logical groupings relevant to your organization, such as different geographical locations.</p>
<pre><code class="language-mermaid">flowchart LR&#10;        accTitle: Internal DNS views and zones&#10;        accDescr: Diagram exemplifying Internal DNS views and zones relationship&#10;        subgraph Internal DNS&#10;        subgraph View 111 - London&#10;        Y[Zone 600 &lt;br /&gt; example.local]&#10;				Z[Zone 601 &lt;br /&gt; local]&#10;        end&#10;        subgraph View 110 - San Francisco&#10;        X[Zone 101 &lt;br /&gt; example.com]&#10;				B[Zone 100 &lt;br /&gt; example.local]&#10;				S[Zone 102 &lt;br /&gt; com]&#10;        end&#10;				W[Zone 701 &lt;br /&gt; net]&#10;				end&#10;</code></pre>
<p>Internal DNS zones contain the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7626.md")
</div> that should be used to resolve an internal DNS query. Also, if no internal record is found within a matching internal zone, Cloudflare will check if the matching internal zone is [referencing another internal zone](/dns/internal-dns/internal-zones/reference-zones/).
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/7627.md")
</div>
<h2 id="resources">Resources</h2>
<ul class="directory-listing"><li><a href="/dns/internal-dns/get-started/">Get started</a></li><li><a href="/dns/internal-dns/internal-zones/">Internal zones</a></li><li><a href="/dns/internal-dns/dns-views/">Manage DNS views</a></li><li><a href="/dns/internal-dns/connectivity/">Connect to Gateway resolver</a></li><li><a href="/dns/internal-dns/analytics/">Analytics and logs</a></li></ul>
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/7628.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/7629.md")
</div>
