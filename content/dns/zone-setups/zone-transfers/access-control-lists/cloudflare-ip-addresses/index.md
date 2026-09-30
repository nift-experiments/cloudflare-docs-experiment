<p>Depending on your setup (<a href="#cloudflare-as-primary">Cloudflare as Primary</a> or <a href="#cloudflare-as-secondary">Cloudflare as Secondary</a>), you need to configure slightly different Cloudflare IP addresses at your other DNS provider.</p>
<h2 id="source-ip-addresses">Source IP addresses</h2>
<p>Cloudflare's AXFR/IXFR zone transfer requests and NOTIFY messages originate from the following IP addresses. These need to be allowed at your other DNS servers.</p>
<pre><code class="language-txt">104.30.167.163&#10;104.30.167.173&#10;2a09:bac0:1000:c47::/64&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="action-required-ip-address-migration">Action required: IP address migration</h3>
@markup("md", "content/.markup/bodies/8084.md")
</aside>
<details class="nb-details"><summary>Old source IP addresses (deprecated — removed December 1, 2026)</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8085.md")
</div></details>
<h2 id="cloudflare-as-primary">Cloudflare as Primary</h2>
<p>If you are using Cloudflare for Primary DNS — meaning that you are setting up Cloudflare to send <a href="/dns/zone-setups/zone-transfers/cloudflare-as-primary/">outgoing zone transfers</a> — you need to update the following settings at your secondary DNS provider.</p>
<h3 id="allow-range">Allow range</h3>
<p>Cloudflare's NOTIFY messages originate from the <a href="#source-ip-addresses">source IP addresses</a> listed above. Allow them at your secondary DNS servers.</p>
<h3 id="transfer-ip">Transfer IP</h3>
<p>Cloudflare will listen to AXFR/IXFR zone transfer requests and SOA queries from your Secondary DNS server on this IP address.</p>
<pre><code class="language-txt">172.65.64.6&#10;</code></pre>
<h2 id="cloudflare-as-secondary">Cloudflare as Secondary</h2>
<p>If you are using Cloudflare for Secondary DNS — meaning that you are setting up Cloudflare to receive <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">incoming zone transfers</a> — you need to update the following settings at your primary DNS provider.</p>
<h3 id="allow-range-1">Allow range</h3>
<p>Cloudflare's AXFR/IXFR zone transfer requests originate from the <a href="#source-ip-addresses">source IP addresses</a> listed above. Allow them at your primary DNS servers.</p>
<h3 id="notify-ips">Notify IPs</h3>
<p>Notify IPs are the IP addresses where you notify Cloudflare's Secondary DNS to initiate a pull of new zone information from your Primary DNS servers:</p>
<pre><code class="language-txt">172.65.30.82&#10;172.65.50.145&#10;2606:4700:60:0:317:26ee:3bdf:5774&#10;2606:4700:60:0:35a:4be3:4144:c5ee&#10;</code></pre>
<h3 id="bind-server-configuration">BIND server configuration</h3>
<p>To run a BIND server as a primary, add the following statements to your zone file:</p>
<pre><code class="language-txt">allow-transfer {104.30.167.163;104.30.167.173;2a09:bac0:1000:c47::/64;}&#10;also-notify { 172.65.30.82;172.65.50.145;2606:4700:60:0:317:26ee:3bdf:5774;2606:4700:60:0:35a:4be3:4144:c5ee;}&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8083.md")
</aside>
