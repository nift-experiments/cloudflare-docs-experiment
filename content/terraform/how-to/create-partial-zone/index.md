<p>A <a href="/dns/zone-setups/partial-setup/">partial zone</a> lets you use Cloudflare for a subdomain while keeping your existing authoritative DNS provider for the parent domain. This guide shows how to automate the setup using the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14765.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Terraform installed. Refer to <a href="/terraform/installing/">Get started</a>.</li>
<li>Your Cloudflare account ID and a configured provider block. Refer to <a href="/terraform/tutorial/initialize-terraform/">Initialize Terraform</a>.</li>
</ul>
<h2 id="create-the-zone">Create the zone</h2>
<p>Add the zone configuration and apply the change to create the zone:</p>
<pre><code class="language-hcl">resource &quot;cloudflare_zone&quot; &quot;subdomain_example_com&quot; {&#10;  account = {&#10;    id = var.cloudflare_account_id&#10;  }&#10;  name = &quot;subdomain.example.com&quot;&#10;}&#10;</code></pre>
<p>Then, in a new Terraform plan and apply cycle, upgrade the zone to a Business plan or higher:</p>
<pre><code class="language-hcl">resource &quot;cloudflare_zone_subscription&quot; &quot;example_zone_subscription&quot; {&#10;  zone_id = cloudflare_zone.subdomain_example_com.id&#10;  frequency = &quot;monthly&quot;&#10;  rate_plan = {&#10;    id = &quot;business&quot;&#10;    currency = &quot;USD&quot;&#10;  }&#10;}&#10;</code></pre>
<p>Then, again in a new Terraform plan and apply cycle, update your Terraform configuration to add <code>type = &quot;partial&quot;</code> to the zone:</p>
<pre><code class="language-hcl">resource &quot;cloudflare_zone&quot; &quot;subdomain_example_com&quot; {&#10;  account = {&#10;    id = var.cloudflare_account_id&#10;  }&#10;  name = &quot;subdomain.example.com&quot;&#10;  type = &quot;partial&quot;&#10;}&#10;</code></pre>
<p>Terraform places the zone in a <strong>Pending</strong> state. You must add the necessary DNS records and verify domain ownership before Cloudflare activates it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14764.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/dns/zone-setups/partial-setup/">Partial zone setup</a></li>
<li><a href="/dns/zone-setups/conversions/convert-full-to-partial/">Convert a full zone to partial</a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zone"><code>cloudflare_zone</code> resource</a></li>
</ul>
