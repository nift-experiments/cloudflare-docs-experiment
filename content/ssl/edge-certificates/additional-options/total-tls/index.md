<p>Total TLS allows Cloudflare to issue individual certificates for your proxied hostnames. These certificates will protect proxied hostnames not covered by <a href="/ssl/edge-certificates/universal-ssl/">Universal certificates</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14156.md")
</aside>
<p>When issued, these certificates will have a type of <strong>Advanced - Total TLS</strong>, and their default validity period is 90 days.</p>
<h2 id="reference">Reference</h2>
<ul class="directory-listing"><li><a href="/ssl/edge-certificates/additional-options/total-tls/enable/">Enable</a></li><li><a href="/ssl/edge-certificates/additional-options/total-tls/error-messages/">Error messages</a></li></ul>
<h2 id="availability">Availability</h2>
<p>Total TLS is available for domains that have purchased <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a> and are currently using a <a href="/dns/zone-setups/full-setup/">full DNS setup</a>.</p>
<h2 id="limitations">Limitations</h2>
<h3 id="hostnames-used-with-other-cloudflare-products">Hostnames used with other Cloudflare products</h3>
<p>Total TLS does not issue certificates for any hostnames used with:</p>
<ul>
<li><a href="/load-balancing/">Cloudflare Load Balancing</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">Cloudflare Tunnel</a></li>
<li><a href="/spectrum/">Cloudflare Spectrum</a></li>
</ul>
<p>You can use other types of certificates or manually <a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/#create-a-certificate">order advanced certificates</a> for these hostnames.</p>
<h3 id="deleting-certificates">Deleting certificates</h3>
<p>Once you <a href="/ssl/edge-certificates/additional-options/total-tls/enable/">enable Total TLS</a>, be careful deleting any Total TLS certificates associated with proxied hostnames.</p>
<p>If you do, our system assumes you want to opt that hostname out of Total TLS certificate and will not order new certificates for the hostname in the future. This behavior applies even if you delete and re-create the hostname's DNS record.</p>
