<p>When you connect your domain to Cloudflare, the <a href="/dns/zone-setups/reference/dns-quick-scan/">DNS records quick scan</a> may automatically add several records to your zone.</p>
<p>If you realize most of them are not applicable and want to bulk delete DNS records, follow the steps below. This method assumes you are familiar with <a href="/fundamentals/api/">API calls fundamentals</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="bulk-deletion-available-in-the-dashboard">Bulk deletion available in the dashboard</h3>
@markup("md", "content/.markup/bodies/7900.md")
</aside>
<ol>
<li>Make sure you have <a href="/fundamentals/api/get-started/create-token/">an API token</a> that allows you to edit DNS for your zone.</li>
<li>Get your <a href="/fundamentals/account/find-account-and-zone-ids/">zone ID</a>.</li>
<li>Run the following script, replacing <code>&lt;ZONE_ID&gt;</code> and <code>&lt;API_TOKEN&gt;</code> with the values you got from the previous steps.</li>
</ol>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/7901.md")
</div>
