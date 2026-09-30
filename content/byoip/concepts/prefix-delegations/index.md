<p>Prefix delegations allow a prefix owner (Account A) to grant another Cloudflare account (Account B) permission to use all or part of their BYOIP prefix. The original prefix remains managed by Account A, but Account B can use the delegated IPs with CDN services (including Cloudflare for SaaS) or Spectrum. Refer to <a href="/byoip/service-bindings/">service bindings</a> for more information on the services an IP can be bound to.</p>
<h2 id="cdn">CDN</h2>
<p>CDN delegations allow you to use the IP(s) with <a href="/byoip/address-maps/">Address Maps</a> or <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> customers.</p>
<p>Address Maps allows you to assign IPs either at the account level or zone level.</p>
<p>In the Cloudflare for SaaS example, Account A is using BYOIP + CDN and Cloudflare for SaaS. Account A can validate and serve traffic for a custom hostname on any of the IPs in its prefix. If Account A delegates some or all of the prefix to Account B, Account B may also validate and serve traffic for custom hostnames on those IPs as well. This is very useful if you use Cloudflare for SaaS but manage different configurations in different accounts. All the accounts can use the IPs through a delegation.</p>
<h2 id="spectrum">Spectrum</h2>
<p>If Account A delegates use of part or all of a prefix to Account B via a prefix delegation, Account B can also use the <a href="/spectrum/about/byoip/">Spectrum API</a> with the IPs it was delegated access to.</p>
<p><strong>Example:</strong> Account A is the primary owner of prefix 1.2.3.0/24. Account A delegates the use of 1.2.3.0/32 to Account B. Account B can now use the Spectrum API to create a Spectrum app with 1.2.3.0/32.</p>
<h2 id="api-calls-for-prefix-delegations">API calls for prefix delegations</h2>
<p>API calls for delegations can be found at <a href="/api/resources/addressing/subresources/prefixes/subresources/delegations/methods/list/">Prefix Delegations</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3772.md")
</aside>
<h2 id="configure-prefix-delegations">Configure prefix delegations</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>IP Addresses</strong> &gt; <strong>BYOIP Prefixes</strong>.</li>
<li>Select <strong>Edit</strong> to modify a prefix. <strong>Edit IP Prefixes</strong> displays.</li>
<li>At the bottom of the page, select <strong>Add Delegation</strong>. Other accounts that your user is a part of will auto-load when you create the delegation.</li>
<li>Select <strong>Save</strong>.</li>
<li>Bind IPs to a service via the <a href="/api/resources/addressing/subresources/prefixes/subresources/service_bindings/">Service Bindings API</a> as needed.</li>
</ol>
