<p>Configuring 1.1.1.1 on your router applies the DNS setting to every device on your network. You do not need to change DNS settings on individual phones, computers, or other devices.</p>
<ol>
<li>
<p>Go to the <strong>IP address</strong> used to access your router's admin console in your browser.</p>
<ul>
<li>Linksys and Asus routers typically use <code>http://192.168.1.1</code> or <code>http://router.asus.com</code> (for ASUS).</li>
<li>Netgear routers typically use <code>http://192.168.1.1</code> or <code>http://routerlogin.net</code>.</li>
<li>D-Link routers typically use <code>http://192.168.0.1</code>.</li>
<li>Ubiquiti routers typically use <code>http://unifi.ubnt.com</code>.</li>
<li>MikroTik routers typically use <code>http://192.168.88.1</code>.</li>
</ul>
</li>
<li>
<p>Enter the router credentials. For consumer routers, the default credentials for the admin console are often found under or behind the device.</p>
</li>
<li>
<p>In the admin console, locate the section where <strong>DNS settings</strong> are configured. This may be contained within categories such as <strong>WAN</strong> and <strong>IPv6</strong> (Asus routers), <strong>IP</strong> (MikroTik routers), or <strong>Internet</strong> (Netgear routers). Consult your router's documentation for details.</p>
</li>
<li>
<p>Take note of any DNS addresses that are currently set and save them in a safe place in case you need to use them later.</p>
</li>
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv4:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1759.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1760.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1761.md")
</div></details>
<ol start="6">
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv6:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1762.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1763.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1764.md")
</div></details>
<ol start="7">
<li>Save the updated settings.</li>
</ol>
<h2 id="use-dns-over-tls-on-openwrt">Use DNS over TLS on OpenWrt</h2>
<p>If your router runs OpenWrt, you can encrypt DNS traffic using DNS over TLS. For setup instructions, refer to <a href="https://blog.cloudflare.com/dns-over-tls-for-openwrt/">Adding DNS-Over-TLS support to OpenWrt (LEDE) with Unbound</a>.</p>
<h2 id="fritz-box">FRITZ!Box</h2>
<p>Starting with <a href="https://en.avm.de/press/press-releases/2020/07/fritzos-720-more-performance-convenience-security/">FRITZ!OS 7.20</a>, DNS over TLS is supported. Refer to <a href="https://en.avm.de/service/knowledge-base/dok/FRITZ-Box-7590/165_Configuring-different-DNS-servers-in-the-FRITZ-Box/">Configuring different DNS servers in the FRITZ!Box</a>.</p>
