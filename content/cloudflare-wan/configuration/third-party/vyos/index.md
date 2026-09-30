<p>This tutorial provides configuration information and a sample template for using a VyOS device with an IPsec configuration.</p>
<h2 id="notes">Notes</h2>
<ul>
<li><code>vti &lt;NAME_OF_VTI_INTERFACE&gt;</code> - Specifies the virtual tunnel interface of the IPsec tunnel.</li>
<li><code>esp-group &lt;NAME_OF_ESP_GROUP&gt;</code> - Encrypts traffic through the tunnel using a particular ESP policy or profile.</li>
<li><code>ike-group &lt;NAME_OF_IKE_GROUP&gt;</code> - Exchanges keys using a particular IKE policy or profile.</li>
<li>The IP addresses of the IPsec tunnel interfaces on both ends of the tunnel should be a pair of private IP addresses (RFC 1918) on the same <code>/31</code> or <code>/30</code> subnet, specifying a point-to-point link.</li>
<li>The IPsec tunnel endpoint on this VyOS router is the <code>&lt;IP_ADDR_OF_UPLINK_INTF_TO_INTERNET/WAN&gt;</code>.</li>
<li>The IP address of the IPsec tunnel endpoint on the Cloudflare side is one of the anycast IP addresses assigned to your account, available in <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space">Leased IPs</a>.</li>
<li>This router is configured to initiate the IPsec tunnel connection.</li>
</ul>
<h2 id="configuration-parameters">Configuration parameters</h2>
<h3 id="phase-1">Phase 1</h3>
<ul>
<li>
<p><strong>Encryption</strong></p>
<ul>
<li>AES-GCM with 128-bit or 256-bit key length</li>
</ul>
</li>
<li>
<p><strong>Integrity</strong></p>
<ul>
<li>SHA512</li>
</ul>
</li>
</ul>
<h3 id="phase-2">Phase 2</h3>
<ul>
<li>
<p><strong>Encryption</strong></p>
<ul>
<li>AES-GCM with 128-bit or 256-bit key length</li>
</ul>
</li>
<li>
<p><strong>Integrity</strong></p>
<ul>
<li>SHA512</li>
</ul>
</li>
<li>
<p><strong>PFS group</strong></p>
<ul>
<li>DH group 20 (348-bit random ECP group)</li>
</ul>
</li>
</ul>
<h2 id="configuration-template">Configuration template</h2>
<pre><code class="language-bash">set interfaces vti &lt;name of the vti interface&gt; address&#10;&#x27;&lt;PRIVATE_IP_ADDRESS_OF_IPSEC_TUNNEL_INTERFACE&gt;&#x27;&#10;set vpn ipsec esp-group &lt;NAME_OF_ESP_GROUP&gt; compression &#x27;disable&#x27;&#10;set vpn ipsec esp-group &lt;NAME_OF_ESP_GROUP&gt; lifetime &#x27;86400&#x27;&#10;set vpn ipsec esp-group &lt;NAME_OF_ESP_GROUP&gt; mode &#x27;tunnel&#x27;&#10;set vpn ipsec esp-group &lt;NAME_OF_ESP_GROUP&gt; pfs &#x27;enable&#x27;&#10;set vpn ipsec esp-group &lt;NAME_OF_ESP_GROUP&gt; proposal 1 encryption &#x27;aes256gcm128&#x27;&#10;set vpn ipsec esp-group &lt;NAME_OF_ESP_GROUP&gt; proposal 1 hash &#x27;sha512&#x27;&#10;set vpn ipsec ike-group &lt;NAME_OF_IKE_GROUP&gt; close-action &#x27;none&#x27;&#10;set vpn ipsec ike-group &lt;NAME_OF_IKE_GROUP&gt; dead-peer-detection action &#x27;restart&#x27;&#10;set vpn ipsec ike-group &lt;NAME_OF_IKE_GROUP&gt; dead-peer-detection interval &#x27;30&#x27;&#10;set vpn ipsec ike-group &lt;NAME_OF_IKE_GROUP&gt; dead-peer-detection timeout &#x27;120&#x27;&#10;set vpn ipsec ike-group &lt;NAME_OF_IKE_GROUP&gt; ikev2-reauth &#x27;no&#x27;&#10;set vpn ipsec ike-group &lt;NAME_OF_IKE_GROUP&gt; key-exchange &#x27;ikev2&#x27;&#10;set vpn ipsec ike-group &lt;NAME_OF_IKE_GROUP&gt; lifetime &#x27;28800&#x27;&#10;set vpn ipsec ike-group &lt;NAME_OF_IKE_GROUP&gt; mobike &#x27;disable&#x27;&#10;set vpn ipsec ike-group &lt;NAME_OF_IKE_GROUP&gt; proposal 1 dh-group &#x27;20&#x27;&#10;set vpn ipsec ike-group &lt;NAME_OF_IKE_GROUP&gt; proposal 1 encryption &#x27;aes256gcm128&#x27;&#10;set vpn ipsec ike-group &lt;NAME_OF_IKE_GROUP&gt; proposal 1 hash &#x27;sha512&#x27;&#10;set vpn ipsec ipsec-interfaces interface &#x27;&lt;UPLINK_INTF_TO_INTERNET/WAN&gt;&#x27;&#10;set vpn ipsec logging log-level &#x27;2&#x27;&#10;set vpn ipsec options disable-route-autoinstall&#10;set vpn ipsec site-to-site peer &lt;CF_ANYCAST_IP&gt; authentication id &#x27;&lt;IPSEC_ID_STRING_IN_RESULT_OF_PSK_KEY-GEN_VIA_CF_API&gt;&#x27;&#10;set vpn ipsec site-to-site peer &lt;CF_ANYCAST_IP&gt; authentication pre-shared-secret &#x27;&lt;PSK_KEY_STRING_GENERATED_VIA_CF_API&gt;&#x27;&#10;set vpn ipsec site-to-site peer &lt;CF_ANYCAST_IP&gt; authentication remote-id &#x27;&lt;CF_ANYCAST_IP&gt;&#x27;&#10;set vpn ipsec site-to-site peer &lt;CF_ANYCAST_IP&gt; connection-type &#x27;initiate&#x27;&#10;set vpn ipsec site-to-site peer &lt;CF_ANYCAST_IP&gt; ike-group &#x27;&lt;NAME_OF_IKE_GROUP&gt;&#x27;&#10;set vpn ipsec site-to-site peer &lt;CF_ANYCAST_IP&gt; ikev2-reauth &#x27;no&#x27;&#10;set vpn ipsec site-to-site peer &lt;CF_ANYCAST_IP&gt; local-address &#x27;&lt;IP_ADDR_OF_UPLINK_INTF_TO_INTERNET/WAN&gt;&#x27;&#10;set vpn ipsec site-to-site peer &lt;CF_ANYCAST_IP&gt; vti bind &#x27;&lt;NAME_OF_VTI_INTERFACE&gt;&#x27;&#10;set vpn ipsec site-to-site peer &lt;CF_ANYCAST_IP&gt; vti esp-group &#x27;&lt;NAME_OF_ESP_GROUP&gt;&#x27;&#10;</code></pre>
