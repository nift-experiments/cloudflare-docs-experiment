<p>Your load balancer should be receiving production traffic (and you can confirm this by reviewing the <a href="/load-balancing/reference/load-balancing-analytics/">analytics</a>).</p>
<p>Though your product is officially set up, you may want to consider the following suggestions.</p>
<h2 id="usage-based-notifications">Usage-based notifications</h2>
<p>Since this is a service with <a href="/billing/understand/usage-based-billing/">usage-based billing</a>, Cloudflare recommends that you set up usage-based billing notifications to avoid unexpected bills.</p>
<p>To set up those notifications:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>On <strong>Alert Type</strong> of <strong>Usage Based Billing</strong>, click <strong>Select</strong>.</p>
</li>
<li>
<p>Fill out the following information:</p>
<ul>
<li><strong>Name</strong></li>
<li><strong>Product</strong></li>
<li><strong>Notification limit</strong> (exact metric will vary based on product)</li>
<li><strong>Notification email</strong></li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9799.md")
</aside>
<ol start="4">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="additional-configuration-options">Additional configuration options</h2>
<p>You may want to further customize how your load balancer routes traffic or integrate your load balancer with other Cloudflare products:</p>
<ul class="directory-listing"><li><a href="/load-balancing/additional-options/cloudflare-tunnel/">Cloudflare Tunnel (published applications)</a></li><li><a href="/load-balancing/additional-options/spectrum/">Spectrum</a></li><li><a href="/load-balancing/additional-options/planned-maintenance/">Perform planned maintenance</a></li><li><a href="/load-balancing/additional-options/load-shedding/">Load shedding</a></li><li><a href="/load-balancing/additional-options/dns-persistence/">DNS persistence</a></li><li><a href="/load-balancing/additional-options/load-balancing-china/">Load Balancing with the China Network</a></li><li><a href="/load-balancing/additional-options/override-http-host-headers/">Override HTTP Host headers</a></li><li><a href="/load-balancing/additional-options/cname-flattening/">CNAME flattening for endpoints</a></li><li><a href="/load-balancing/additional-options/load-balancing-rules/">Custom load balancing rules</a></li><li><a href="/load-balancing/additional-options/pagerduty-integration/">Integrate with PagerDuty</a></li><li><a href="/load-balancing/additional-options/additional-dns-records/">Additional DNS records</a></li></ul>
