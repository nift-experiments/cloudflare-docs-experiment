<aside class="nb-aside note">
<h3 class="nb-aside-title" id="smart-shield">Smart Shield</h3>
@markup("md", "content/.markup/bodies/1523.md")
</aside>
<p>Argo Smart Routing speeds up your global traffic by routing requests across the fastest network paths available.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1526.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1522.md")
</aside>
<h2 id="billing">Billing</h2>
<p>If Cloudflare mitigates attacks on your site - whether through DDoS protection, the WAF, or other mechanisms - that traffic will not be included in any charges for Argo Smart Routing.</p>
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
@markup("md", "content/.markup/bodies/1521.md")
</aside>
<ol start="4">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="enable-tiered-cache">Enable Tiered Cache</h2>
<p><a href="/cache/">Cache</a> works by storing a copy of website content at Cloudflare's data centers. <a href="/cache/how-to/tiered-cache/">Tiered Cache</a> organizes these data centers into a hierarchy based on location. This behavior allows Cloudflare to deliver content from data centers closest to your visitor.</p>
<p>When used together, Argo Smart Routing optimizes the network path between Cloudflare data centers and your origin, while Tiered Cache reduces the number of requests that reach your origin. For more information, refer to <a href="/cache/how-to/tiered-cache/">Tiered Cache</a>.</p>
