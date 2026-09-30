<p>When creating a Spectrum application, Cloudflare normally assigns an arbitrary IP from Cloudflare’s IP pool to your application. If you want to be explicit in your network setup or use your own IP addresses, BYOIP with Spectrum allows you to do just that.</p>
<p>BYOIP stands for <a href="/byoip/">Bring Your Own IP</a>. If you own an IP prefix you can migrate it to Cloudflare. After migration, Cloudflare broadcasts your IP prefix and traffic is routed to the global Cloudflare network. However, without configuration, Cloudflare will not know how to handle this traffic. The last step is to add Spectrum applications for all applications that you wish to protect with the IP addresses you want associated with them.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13880.md")
</aside>
<p>The smallest prefixes that Cloudflare currently supports is /24 for IPv4 and /48 for IPv6.</p>
<p>BYOIP does not come standard with Spectrum. To enable it, contact your account team.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="udp-applications">UDP applications</h3>
@markup("md", "content/.markup/bodies/13879.md")
</aside>
<h2 id="assign-an-ip-address">Assign an IP address</h2>
<p>To use an IP, it must be assigned to a Spectrum app to create the appropriate A (IPv4) or AAAA (IPv6) records. This is done by specifying one or more IP addresses when creating an application through the API. Any change to the application's properties also needs to be done via API. In addition, you must update the DNS <code>&quot;type&quot;</code> field to <code>&quot;ADDRESS&quot;</code> to create a Spectrum app using BYOIP.</p>
<pre><code class="language-json">{&#10;  &quot;id&quot;: &quot;4590376cf2994d72cee36828ec4eff19&quot;,&#10;  &quot;protocol&quot;: &quot;tcp/22&quot;,&#10;  &quot;dns&quot;: {&#10;    &quot;type&quot;: &quot;ADDRESS&quot;,&#10;    &quot;name&quot;: &quot;ssh.example.com&quot;&#10;  },&#10;  &quot;origin_direct&quot;: [&quot;tcp://192.0.2.1:22&quot;],&#10;  &quot;ip_firewall&quot;: true,&#10;  &quot;proxy_protocol&quot;: false,&#10;  &quot;spp&quot;: false,&#10;  &quot;tls&quot;: &quot;off&quot;,&#10;  &quot;traffic_type&quot;: &quot;direct&quot;,&#10;  &quot;edge_ips&quot;: {&#10;    &quot;type&quot;: &quot;static&quot;,&#10;    &quot;ips&quot;: [&quot;198.51.100.10&quot;, &quot;2001:DB8::1&quot;]&#10;  }&#10;}&#10;</code></pre>
<h2 id="example">Example</h2>
<p>In the example below, the application routes traffic through Cloudflare’s HTTP pipeline, including WAF, Workers and CDN functionality.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/spectrum/apps \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;protocol&quot;: &quot;tcp/80&quot;,&#10;  &quot;dns&quot;: {&#10;    &quot;type&quot;: &quot;ADDRESS&quot;,&#10;    &quot;name&quot;: &quot;www.example.com&quot;&#10;  },&#10;  &quot;origin_direct&quot;: [&#10;    &quot;tcp://192.0.2.1:80&quot;&#10;  ],&#10;  &quot;tls&quot;: &quot;off&quot;,&#10;  &quot;traffic_type&quot;: &quot;http&quot;,&#10;  &quot;edge_ips&quot;: {&#10;    &quot;type&quot;: &quot;static&quot;,&#10;    &quot;ips&quot;: [&#10;      &quot;198.51.100.10&quot;,&#10;      &quot;2001:DB8::1&quot;&#10;    ]&#10;  }&#10;}&#x27;</code></pre>
