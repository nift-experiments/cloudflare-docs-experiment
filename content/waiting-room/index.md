<div class="nb-description">
@markup("md", "content/.markup/bodies/126.md")
</div>
<div class="nb-plan">
<p>Business and above</p>
</div>
<p>Cloudflare Waiting Room allows you to route excess users of your website to a customized waiting room, helping preserve customer experience and protect origin servers from being overwhelmed with requests.</p>
<hr />
<h2 id="benefits">Benefits</h2>
<p>Waiting Room protects your origin server by preventing surges in legitimate traffic that may overload your origin.</p>
<p>Waiting Room also benefits your visitors by:</p>
<ul>
<li>Keeping your application online and preventing them from reaching error pages.</li>
<li>Showing estimated wait times that are continuously updated.</li>
<li>Opening up new spots more quickly by tracking dynamic inflow and <a href="/waiting-room/reference/configuration-settings/#session-duration">outflow</a>.</li>
<li>Remembering each visitor's status to prevent someone from losing their place in line or having to re-queue if they leave your site.</li>
<li>Appearing in your own <a href="/waiting-room/how-to/customize-waiting-room/">branding and style</a>, which enhances trust and lets you provide additional information as needed.</li>
</ul>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/127.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/128.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/129.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/130.md")
</div>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/131.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/132.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/133.md")
</div>
<hr />
<h2 id="availability">Availability</h2>
<p>The following customers have access to Cloudflare Waiting Room:</p>
<ul>
<li>Those qualified under <a href="https://www.cloudflare.com/fair-shot/">Project Fair Shot</a></li>
<li>Customers on a Business or Enterprise plan</li>
</ul>
<p>Access to certain features depends on a customer's <a href="/waiting-room/plans/">plan type</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/125.md")
</aside>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li><a href="/cache/">Cloudflare’s CDN</a> is required to use the Waiting Room feature.</li>
<li>Configure a <a href="/dns/manage-dns-records/how-to/create-dns-records/">proxied DNS record</a> or a <a href="/load-balancing/understand-basics/proxy-modes/">proxied load balancer</a> for the waiting room’s hostname. A DNS record is not auto-configured after a waiting room is created.</li>
<li>Visitors must enable cookies. Refer to <a href="/waiting-room/reference/waiting-room-cookie/">Waiting Room cookies</a> for information on how cookies are used in Cloudflare Waiting Room.</li>
</ul>
<hr />
<h2 id="more-resources">More resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/135.md")
</div>
