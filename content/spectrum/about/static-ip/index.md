<p>When you create a Spectrum application, you are assigned an IP. These IPs are normally dynamic, meaning that they will change over time. But, for instance, if you want to set up WAF custom rules for specific IPs, you may want to use static IPs.</p>
<p>A static IP, like a physical street address can tell other computers or servers on the Internet where a specific computer is located or connected. This makes the device easier to find on the network, since the IP will not change.</p>
<p>With static IPs, Cloudflare commits to never changing the IP address of a client's domain resolved at the Cloudflare global network. For example, <code>www.example.com</code> will always resolve and accept traffic sent to <code>198.51.100.10</code>. No other customer will be hosted on that IP.</p>
<p>Importantly, the static IP is associated with the DNS name, not with each individual Spectrum application. This means that all Spectrum apps using the same hostname will share the same static IP.</p>
<h2 id="use-static-ips-with-spectrum">Use static IPs with Spectrum</h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/13875.md")
</aside>
<p>Once you get your static IP from Cloudflare, you can use it via API, just like <a href="/byoip/">BYOIP</a>. For the moment, there is still no UI available for this feature.</p>
<p>When creating a Spectrum application through the API, specify the static IPs that you have been provided. See, for instance, the API example below that creates an application routing traffic through Cloudflare’s HTTP pipeline.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/spectrum/apps \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;protocol&quot;: &quot;tcp/80&quot;,&#10;  &quot;dns&quot;: {&#10;    &quot;type&quot;: &quot;ADDRESS&quot;,&#10;    &quot;name&quot;: &quot;www.example.com&quot;&#10;  },&#10;  &quot;origin_direct&quot;: [&#10;    &quot;tcp://192.0.2.1:80&quot;&#10;  ],&#10;  &quot;tls&quot;: &quot;off&quot;,&#10;  &quot;traffic_type&quot;: &quot;http&quot;,&#10;  &quot;edge_ips&quot;: {&#10;    &quot;type&quot;: &quot;static&quot;,&#10;    &quot;ips&quot;: [&#10;      &quot;198.51.100.10&quot;,&#10;      &quot;2001:DB8::1&quot;&#10;    ]&#10;  }&#10;}&#x27;</code></pre>
<h2 id="check-your-static-ips">Check your static IPs</h2>
<p>You can find your leased static IPs for Spectrum on the dashboard under <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space"><strong>Address space</strong> &gt; <strong>Leased IPs</strong></a>.</p>
