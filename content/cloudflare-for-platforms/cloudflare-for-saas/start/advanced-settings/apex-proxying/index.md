<p>Apex proxying allows your customers to use their apex domains (<code>example.com</code>) with your SaaS application.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4187.md")
</aside>
<h2 id="benefits">Benefits</h2>
<p>In a normal Cloudflare for SaaS <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">setup</a>, your customers route traffic to your hostname by creating a <code>CNAME</code> record pointing to your CNAME target.</p>
<p>However, most DNS providers do not allow <code>CNAME</code> records at the zone's root<sup><a href="#footnote-1">1</a></sup>. This means that your customers have to use a subdomain as a vanity domain (<code>shop.example.com</code>) instead of their domain apex (<code>example.com</code>).</p>
<p>This limitation does not apply with apex proxying. Cloudflare assigns a set of <a href="/byoip/concepts/static-ips/">Static IP prefixes</a> - cost associated, reach out to your account team - to your account (or uses your own if you have <a href="/byoip/">BYOIP</a>).
This means then that customers can create a standard <code>A</code> record to route traffic to your domain, which can support the domain apex.</p>
<h2 id="setup">Setup</h2>
<ul>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/setup/">Set up Apex Proxying</a></li>
</ul>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Cloudflare offers this functionality through [CNAME flattening](/dns/cname-flattening/).</li></ol></section>
