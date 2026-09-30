<p>The <code>PublicStats</code> component allows you to reference specific values about Cloudflare's network without maintaining those values in multiple files.</p>
<p>Refer to the examples below for more information.</p>
<pre><code class="language-mdx">import { PublicStats } from &quot;~/components&quot;;&#10;&#10;Cloudflare has data centers in &lt;PublicStats id=&quot;data_center_cities&quot; /&gt;.&#10;&#10;Our network has &lt;PublicStats id=&quot;total_bandwidth&quot; /&gt;.&#10;&#10;Cloudflare also has &lt;PublicStats id=&quot;network_peers&quot; /&gt;.&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14636.md")
</aside>
<h2 id="associated-content-types">Associated content types</h2>
<p>The <code>PublicStats</code> component is commonly used on the following type of pages:</p>
<ul>
<li><a href="/style-guide/documentation-content-strategy/content-types/overview/">Overview</a></li>
<li><a href="/style-guide/documentation-content-strategy/content-types/reference-architecture/">Reference Architecture</a></li>
<li><a href="/style-guide/documentation-content-strategy/content-types/reference-architecture/#reference-architecture-diagrams">Reference Architecture Diagrams</a></li>
</ul>
