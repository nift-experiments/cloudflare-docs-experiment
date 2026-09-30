<div class="nb-glossary-definition"><p>Address map is a data structure enabling customers with BYOIP prefixes or account-level static IPs to specify which IP addresses should be mapped to DNS records when they are proxied through Cloudflare.</p></div>
<p>By default, Cloudflare responds to DNS queries for proxied hostnames with Cloudflare-owned <a href="/fundamentals/concepts/cloudflare-ip-addresses/">anycast IP addresses</a>. Address maps allow you to override this behavior — when a zone or account is associated with an address map, Cloudflare responds with the IP addresses you specify instead.</p>
<p>To use address maps, you must first have <a href="/byoip/">BYOIP</a> prefixes or <a href="/byoip/concepts/static-ips/">static IPs</a> configured on your account. You can <a href="/fundamentals/concepts/cloudflare-ip-addresses/#customize-cloudflare-ip-addresses">customize the IPs Cloudflare uses</a> through either approach. If you are interested in address maps but do not yet have BYOIP or static IPs, contact your account manager.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3787.md")
</aside>
<hr />
<h2 id="how-address-maps-works">How Address Maps works</h2>
<p>For zones using <a href="/dns/">Cloudflare's authoritative DNS</a>, Cloudflare typically responds to DNS queries for proxied hostnames with <a href="/fundamentals/concepts/cloudflare-ip-addresses/">anycast IPs</a>. However, if you <a href="/fundamentals/concepts/cloudflare-ip-addresses/#customize-cloudflare-ip-addresses">customize the IPs Cloudflare uses</a> and use Address Maps, Cloudflare will respond with the IP address(es) on the address map.</p>
<p>Address maps do not change <a href="/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-reverse-proxy">how Cloudflare reaches the configured origin</a>. The IP addresses defined on your zone's <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records">DNS Records</a> continue to instruct Cloudflare how to reach the origin.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3786.md")
</aside>
<h3 id="static-ips-or-byoip">Static IPs or BYOIP</h3>
<p>Leased static IPs allow you to use a set of specifically assigned Cloudflare IPs to ensure they do not change. Cloudflare creates an address map with your static IPs that you may edit. You cannot create another map using your static IPs.</p>
<p>With BYOIP, you use your IPs by bringing an address space that you lease or own and creating an address map.</p>
<hr />
<h2 id="immutable-address-maps">Immutable address maps</h2>
<p>Some customers may only proxy zones through BYOIP addresses, and are prohibited from using Cloudflare IP addresses for proxied DNS names. In this case, Cloudflare will create an immutable, account-wide address map to ensure all zones in your account receive BYOIP addresses as a fallback. These address maps cannot be deleted.</p>
<p>It is still possible to create more specific zone-level address maps with specific BYOIPs, but DNS will fall back to the account-wide address map without one.</p>
<p>To specify different addresses for certain zones, <a href="/byoip/address-maps/setup/">create a new address map</a>.</p>
<hr />
<h2 id="spectrum-compatibility">Spectrum compatibility</h2>
<p>You can use address maps to set up <a href="/byoip/address-maps/setup/#spectrum-https-applications">non-SNI support</a> for Spectrum HTTPS applications.</p>
<p>However, to control what IP address Cloudflare will use when responding to requests for your Spectrum applications, you should first refer to their respective configuration and set the <code>edge_ips</code> field as <code>static</code>, e.g.:</p>
<pre><code class="language-json">&quot;edge_ips&quot;: {&#10;  &quot;type&quot;: &quot;static&quot;,&#10;  &quot;ips&quot;: [&quot;1.2.3.4&quot;]&#10;}&#10;</code></pre>
<p>For details, refer to the <a href="/api/resources/spectrum#%28resource%29%20spectrum%20%3E%20%28model%29%20edge_ips%20%3E%20%28schema%29%20%3E%20%28variant%29%201">Spectrum API</a>.</p>
