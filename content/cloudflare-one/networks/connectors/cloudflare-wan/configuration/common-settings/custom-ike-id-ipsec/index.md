<p>Cloudflare WAN (formerly Magic WAN) customers can configure a custom IKE ID for their IPsec tunnels. Customers that are using Cloudflare WAN and a VeloCloud SD-WAN device together should utilize this option to create a high availability configuration.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5703.md")
</aside>
<p>VeloCloud has a high availability mechanism that allows customers to specify one set of IKE parameters (like IKE ID) and multiple remote IPs. Customers create an IKE ID, and then assign the same custom IKE ID to their primary IPsec tunnel and their backup IPsec tunnel. FQDN is the only supported type for custom IKE IDs.</p>
<p>Cloudflare WAN customers can set a custom IKE ID for an IPsec tunnel using the following API call. Customers will need to fill in the appropriate values for <code>&lt;account_id&gt;</code>, <code>&lt;tunnel_id&gt;</code>, and the FQDN wildcard before running the API call.</p>
<pre><code class="language-bash">curl --request PATCH --url https://api.cloudflare.com/client/v4/accounts/ACCOUNT_ID/ipsec_tunnels/TUNNEL_ID</code></pre>
