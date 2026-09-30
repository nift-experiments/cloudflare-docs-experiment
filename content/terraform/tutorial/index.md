<p>Before you begin, <a href="/terraform/installing/">install Terraform</a>. Each tutorial builds on the previous, so you should complete the tutorials in the order shown below.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14760.md")
</aside>
<h2 id="1-initialize-terraform-terraform-tutorial-initialize-terraform"><a href="/terraform/tutorial/initialize-terraform/">1 – Initialize Terraform</a></h2>
<ul>
<li>Brief introduction.</li>
<li>Introduction of <code>terraform init</code>, <code>plan</code>, <code>apply</code>, and <code>show</code>.</li>
<li>Resource covered: <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/dns_record"><code>cloudflare_dns_record</code></a> (DNS record).</li>
</ul>
<h2 id="2-track-your-history-terraform-tutorial-track-history"><a href="/terraform/tutorial/track-history/">2 – Track your history</a></h2>
<ul>
<li>Store Cloudflare configuration in source control.</li>
</ul>
<h2 id="3-configure-https-settings-terraform-tutorial-configure-https-settings"><a href="/terraform/tutorial/configure-https-settings/">3 – Configure HTTPS settings</a></h2>
<ul>
<li>Modify zone settings.</li>
<li>Resource covered: <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zone_setting"><code>cloudflare_zone_setting</code></a>.</li>
</ul>
<h2 id="4-improve-performance-and-reliability-terraform-tutorial-use-load-balancing"><a href="/terraform/tutorial/use-load-balancing/">4 – Improve performance and reliability</a></h2>
<ul>
<li>Add load balancing rules.</li>
<li>Resources covered:
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/load_balancer"><code>cloudflare_load_balancer</code></a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/load_balancer_pool"><code>cloudflare_load_balancer_pool</code></a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/load_balancer_monitor"><code>cloudflare_load_balancer_monitor</code></a></li>
</ul>
</li>
</ul>
<h2 id="5-add-exceptions-with-page-rules-terraform-tutorial-add-page-rules"><a href="/terraform/tutorial/add-page-rules/">5 – Add exceptions with page rules</a></h2>
<ul>
<li>Add page rule.</li>
<li>Resource covered: <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/page_rule"><code>cloudflare_page_rule</code></a>.</li>
<li>Increase security level for a specific URL: <code>/expensive-db-call</code>.</li>
<li>Add a redirect (URL forward) with a <code>301</code> status code from <code>/old-location.php</code> to <code>/expensive-db-call</code>.</li>
</ul>
<h2 id="6-revert-configuration-terraform-tutorial-revert-configuration"><a href="/terraform/tutorial/revert-configuration/">6 – Revert configuration</a></h2>
<ul>
<li>Review change history.</li>
<li>Roll back changes.</li>
</ul>
