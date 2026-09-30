<p>A <a href="/dns/zone-setups/subdomain-setup/">subdomain zone</a> lets you manage a subdomain in a separate Cloudflare zone from the parent domain. This is useful for access control and team management. This guide shows how to automate the setup using the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider</a>. It is only available for Enterprise accounts</p>
<blockquote>
<p>NOTE: subdomain setup is only available for Enterprise accounts</p>
</blockquote>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Terraform installed. Refer to <a href="/terraform/installing/">Get started</a>.</li>
<li>Your Cloudflare account ID and a configured provider block. Refer to <a href="/terraform/tutorial/initialize-terraform/">Initialize Terraform</a>.</li>
</ul>
<h2 id="create-the-zone">Create the zone</h2>
<p>Create a <code>cloudflare_zone</code> resource for the subdomain zone. The following example creates a zone for <code>subdomain.example.com</code>:</p>
<pre><code class="language-hcl">resource &quot;cloudflare_zone&quot; &quot;subdomain_example_com&quot; {&#10;  account = {&#10;    id = var.cloudflare_account_id&#10;  }&#10;  name = &quot;subdomain.example.com&quot;&#10;  type = &quot;full&quot;&#10;}&#10;</code></pre>
<p>Terraform creates the zone in a <strong>Pending</strong> state. You must add NS delegation records to the parent zone before Cloudflare activates it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14763.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/dns/zone-setups/subdomain-setup/">Subdomain setup</a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zone"><code>cloudflare_zone</code> resource</a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/dns_record"><code>cloudflare_dns_record</code> resource</a></li>
</ul>
