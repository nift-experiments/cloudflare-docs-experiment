<p>When <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/#4-update-registrar">updating your registrar</a> with the Cloudflare secondary nameservers (<code>nsXXXX.secondary.cloudflare.com</code>), you get an error.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7891.md")
</aside>
<p>Upon contacting your registrar, their services confirm that the Cloudflare nameservers cannot be added at this time.</p>
<hr />
<h2 id="cause">Cause</h2>
<p>This issue may arise when one of the Cloudflare nameservers used for secondary setup is removed from the Verisign side.</p>
<hr />
<h2 id="solution">Solution</h2>
<p>The Cloudflare engineering team needs to be engaged <a href="/support/contacting-cloudflare-support/">through Support</a> to make sure the nameserver gets registered again manually at Verisign.</p>
