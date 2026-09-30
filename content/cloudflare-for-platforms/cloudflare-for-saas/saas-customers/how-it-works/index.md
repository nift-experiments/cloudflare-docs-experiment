<p>O2O is a specific traffic routing configuration where traffic routes through two Cloudflare zones: the first Cloudflare zone is owned by customer 1 and the second Cloudflare zone is owned by customer 2, who is considered a SaaS provider.</p>
<p>If one or more hostnames are onboarded to a SaaS Provider that uses Cloudflare products as part of their platform - specifically the <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS product</a> - those hostnames will be created as <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/">custom hostnames</a> in the SaaS Provider's zone.</p>
<p>To give the SaaS provider permission to route traffic through their zone, any custom hostname must be activated by you (the SaaS customer) by placing a <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#3-have-customer-create-cname-record">CNAME record</a> on your authoritative DNS. If your authoritative DNS is Cloudflare, you have the option to <a href="/fundamentals/concepts/how-cloudflare-works/#application-services">proxy</a> your CNAME record, achieving an O2O setup.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>O2O only applies when the two zones are part of different Cloudflare accounts.</li>
<li>Since O2O is based on CNAME, it does not apply when an A record is used to point to the SaaS provider's (<a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/">apex proxying</a>).</li>
</ul>
<h2 id="with-o2o">With O2O</h2>
<p>If you have your own Cloudflare zone (<code>example.com</code>) and your zone contains a <a href="/dns/proxy-status/">proxied DNS record</a> matching the custom hostname (<code>mystore.example.com</code>) with a <strong>CNAME</strong> target defined by the SaaS Provider, then O2O will be enabled.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/4090.md")
</div>
<p>With O2O enabled, the settings configured in your Cloudflare zone will be applied to the traffic first, and then the settings configured in the SaaS provider's zone will be applied to the traffic second. In the SaaS provider-owned zone, a HTTP header will be set to <code>cf-connecting-o2o: 1</code>.</p>
<pre><code class="language-mermaid">flowchart TD&#10;accTitle: O2O-enabled traffic flow diagram&#10;&#10;A[Website visitor]&#10;&#10;subgraph Cloudflare&#10;  B[Customer-owned zone]&#10;  C[SaaS Provider-owned zone]&#10;end&#10;&#10;D[SaaS Provider Origin]&#10;&#10;A --&gt; B&#10;B --&gt; C&#10;C --&gt; D&#10;</code></pre>
<h2 id="detect-o2o-traffic">Detect O2O traffic</h2>
<p>When traffic flows through an O2O configuration, Cloudflare sets the HTTP header <code>cf-connecting-o2o: 1</code> on requests entering the SaaS provider's zone. There is no API field or zone setting that indicates whether O2O is active — it is a per-request routing behavior determined by the customer's DNS configuration.</p>
<p>You can check for this header in your origin server or in a <a href="/workers/">Cloudflare Worker</a> to identify O2O traffic and apply specific logic.</p>
<h2 id="without-o2o">Without O2O</h2>
<p>If you do not have your own Cloudflare zone and have only onboarded one or more of your hostnames to a SaaS Provider, then O2O will not be enabled.</p>
<p>Without O2O enabled, the settings configured in the SaaS Provider's zone will be applied to the traffic.</p>
<pre><code class="language-mermaid">flowchart TD&#10;accTitle: Your zone using a SaaS provider, but without O2O&#10;&#10;A[Website visitor]&#10;&#10;subgraph Cloudflare&#10;    B[SaaS Provider-owned zone]&#10;end&#10;&#10;C[SaaS Provider Origin]&#10;&#10;A --&gt; B&#10;B --&gt; C&#10;</code></pre>
