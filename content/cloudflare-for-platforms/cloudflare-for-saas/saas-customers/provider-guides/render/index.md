<p>Cloudflare partners with <a href="https://render.com">Render</a> to provide Render customers’ web services and static sites with Cloudflare’s performance and security benefits.</p>
<p>If you use Render and also have a Cloudflare plan, you can use your own Cloudflare zone to proxy web traffic to your zone first, then Render's (the SaaS Provider) zone second. This configuration option is called <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/">O2O</a>.</p>
<h2 id="benefits">Benefits</h2>
<p>O2O's benefits include applying your own Cloudflare zone's services and settings — such as <a href="/waf/">WAF</a>, <a href="/bots/plans/bm-subscription/">Bot Management</a>, <a href="/waiting-room/">Waiting Room</a>, and more — on the traffic destined for your Render services.</p>
<h2 id="how-it-works">How it works</h2>
<p>For additional detail about how traffic routes when O2O is enabled, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/">How O2O works</a>.</p>
<h2 id="enable">Enable</h2>
<p>Render customers can enable O2O on any Cloudflare zone plan. Cloudflare support for O2O setups is only available for Enterprise customers.</p>
<p>To enable O2O for a specific hostname within a Cloudflare zone, <a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">create</a> a Proxied <code>CNAME</code> DNS record with your Render site name as the target. Render's domain addition setup will walk you through other validation steps.</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>Target</th>
<th>Proxy status</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CNAME</code></td>
<td><code>&lt;YOUR_HOSTNAME&gt;</code></td>
<td><code>&lt;RENDER_SUBDOMAIN&gt;</code> (for example, <code>example.onrender.com</code>)</td>
<td>Proxied</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4126.md")
</aside>
<h3 id="additional-requirements-for-wildcard-subdomains">Additional requirements for wildcard subdomains</h3>
<p>With O2O enabled, adding a wildcard subdomain to a Render service requires that the corresponding root domain is also routed to Render. If the root domain is routed elsewhere, wildcard routing will fail.</p>
<p>If your root domain needs to route somewhere besides Render, add individual subdomains to your Render service instead of a wildcard.</p>
<h2 id="product-compatibility">Product compatibility</h2>
<p>When a hostname within your Cloudflare zone has O2O enabled, you assume additional responsibility for the traffic on that hostname because you can now configure various Cloudflare products to affect that traffic. Some of the Cloudflare products compatible with O2O are:</p>
<ul>
<li><a href="/cache/">Caching</a></li>
<li><a href="/workers/">Workers</a></li>
<li><a href="/rules/">Rules</a></li>
</ul>
<p>For a full list of compatible products and potential limitations, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/product-compatibility/">Product compatibility</a>.</p>
<h2 id="zone-hold">Zone hold</h2>
<p>If your own Cloudflare zone is on the Enterprise plan, you have access to the <a href="/fundamentals/account/account-security/zone-holds/">zone hold feature</a>, which is a toggle that prevents your domain name from being created as a zone in a different Cloudflare account. Additionally, if the zone hold is enabled, it prevents the activation of custom hostnames onboarded to Render. Render would receive the following error message for your custom hostname: <code>The hostname is associated with a held zone. Please contact the owner of this domain to have the hold removed.</code></p>
<p>To successfully activate the custom hostname on Render, the owner of the zone needs to <a href="/fundamentals/account/account-security/zone-holds/#release-zone-holds">temporarily release the hold</a>. If you are only onboarding a subdomain as a custom hostname to Render, only the subfeature titled <strong>Also prevent Subdomains</strong> needs to be temporarily disabled.</p>
<p>Once the zone hold is temporarily disabled, follow Render's instructions to refresh the custom hostname and it should activate.</p>
<h2 id="additional-support">Additional support</h2>
<p>If you are a Render customer and have set up your own Cloudflare zone with O2O enabled on specific hostnames, contact your Cloudflare Account Team or <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> for help resolving issues in your own zone.</p>
<p>Cloudflare will consult Render if there are technical issues that Cloudflare cannot resolve.</p>
<h3 id="resolving-ssl-errors">Resolving SSL errors</h3>
<p>If you encounter SSL errors, check if you have a <code>CAA</code> record.</p>
<p>If you have a <code>CAA</code> record, verify that it permits SSL certificates to be issued by Google Trust Services (<code>pki.goog</code>).</p>
<p>For more details, refer to <a href="/ssl/edge-certificates/caa-records/">CAA records</a>.</p>
