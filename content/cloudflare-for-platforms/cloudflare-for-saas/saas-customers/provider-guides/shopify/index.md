<p>Cloudflare partners with Shopify to provide Shopify customers’ websites with Cloudflare’s performance and security benefits.</p>
<p>If you use Shopify and also have a Cloudflare plan, you can use your own Cloudflare zone to proxy web traffic to your zone first, then Shopify's (the SaaS Provider) zone second. This configuration option is called <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/">O2O</a>.</p>
<h2 id="benefits">Benefits</h2>
<p>O2O routing also enables you to take advantage of Cloudflare zones specifically customized for Shopify traffic.</p>
<h2 id="how-it-works">How it works</h2>
<p>For more details about how O2O is different than other Cloudflare setups, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/">How O2O works</a>.</p>
<p>When you <a href="#enable">set up O2O routing for your Shopify website</a>, Cloudflare enables specific configurations for this SaaS provider. Currently, this includes the following:</p>
<ul>
<li>Workers and Snippets are disabled on the <code>/checkout</code> URI path.</li>
</ul>
<h2 id="enable">Enable</h2>
<p>You can enable O2O on any Cloudflare zone plan.</p>
<p>To enable O2O on your account, <a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">create</a> a <code>CNAME</code> DNS record.</p>
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
<td><code>&lt;YOUR_SHOP_DOMAIN&gt;</code></td>
<td><code>shops.myshopify.com</code></td>
<td>Proxied</td>
</tr>
</tbody>
</table>
<p>Once you save the new DNS record, the Cloudflare dashboard will show a Shopify icon next to the CNAME record value. For example:</p>
<p><img src="/assets/upstream/images/cloudflare-for-platforms/provider-guides/shopify-dns-entry.png" alt="Cloudflare dashboard showing a CNAME DNS entry for Shopify with a specific Shopify icon" /></p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="do-not-use-always-use-https">Do not use Always Use HTTPS</h3>
@markup("md", "content/.markup/bodies/4122.md")
</aside>
<p>For questions about Shopify setup, refer to their <a href="https://help.shopify.com/en/manual/domains/add-a-domain/connecting-domains/connect-domain-manual">support guide</a>.</p>
<h2 id="product-compatibility">Product compatibility</h2>
<p>When a hostname within your Cloudflare zone has O2O enabled, you assume additional responsibility for the traffic on that hostname because you can now configure various Cloudflare products to affect that traffic. Some of the Cloudflare products compatible with O2O are:</p>
<ul>
<li><a href="/cache/">Caching</a></li>
<li><a href="/workers/">Workers</a></li>
<li><a href="/rules/">Rules</a></li>
</ul>
<p>For a full list of compatible products and potential limitations, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/product-compatibility/">Product compatibility</a>.</p>
<h2 id="zone-hold">Zone hold</h2>
<p>If your own Cloudflare zone is on the Enterprise plan, you have access to the <a href="/fundamentals/account/account-security/zone-holds/">zone hold feature</a>, which is a toggle that prevents your domain name from being created as a zone in a different Cloudflare account. Additionally, if the zone hold is enabled, it prevents the activation of custom hostnames onboarded to Shopify. Shopify would receive the following error message for your custom hostname: <code>The hostname is associated with a held zone. Please contact the owner of this domain to have the hold removed.</code></p>
<p>To successfully activate the custom hostname on Shopify, the owner of the zone needs to <a href="/fundamentals/account/account-security/zone-holds/#release-zone-holds">temporarily release the hold</a>. If you are only onboarding a subdomain as a custom hostname to Shopify, only the subfeature titled <strong>Also prevent Subdomains</strong> needs to be temporarily disabled.</p>
<p>Once the zone hold is temporarily disabled, follow Shopify's instructions to refresh the custom hostname and it should activate.</p>
<h2 id="additional-support">Additional support</h2>
<p>If you are a Shopify customer and have set up your own Cloudflare zone with O2O enabled on specific hostnames, contact your Cloudflare Account Team or <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> for help resolving issues in your own zone.</p>
<p>Cloudflare will consult Shopify if there are technical issues that Cloudflare cannot resolve.</p>
<h3 id="dns-caa-records">DNS CAA records</h3>
<p>For details about <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/4123.md")
</div> refer to the [Shopify documentation](https://help.shopify.com/manual/domains/add-a-domain/connecting-domains/considerations).
