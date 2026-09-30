<p>The hardware version of Cloudflare One Appliance (formerly Magic WAN Connector) includes two <a href="https://en.wikipedia.org/wiki/Small_Form-factor_Pluggable">SFP+ ports</a> that support 10G throughput. These ports can be configured as either a WAN or a LAN port, like all of the 1G RJ45 ports in the machine. Because a 10G WAN uplink will often be bottlenecked by IPsec tunnel speeds, the SFP+ ports are most useful for configuring high speed LANs, and for using fiber connections.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="virtual-appliance-and-sfp-ports">Virtual Appliance and SFP+ ports</h3>
@markup("md", "content/.markup/bodies/5762.md")
</aside>
<h2 id="port-configuration">Port configuration</h2>
<p>SFP+ ports are next to the regular LAN ports. They are represented as follows in the dashboard:</p>
<ul>
<li>SFP+ <strong>port 1</strong> is represented by <strong>port 7</strong> in the dashboard</li>
<li>SFP+ <strong>port 2</strong> is represented by <strong>port 8</strong> in the dashboard</li>
</ul>
<p><img src="/assets/upstream/images/cloudflare-wan/connector/sfp-ports.png" alt="The left port, SFP+ 1, is port 7. The right port, SFP+ 2, is port 8." /></p>
<p><em>The left port, SFP+ 1, is port 7. The right port, SFP+ 2, is port 8.</em></p>
<h2 id="sfp-module-compatibility">SFP+ module compatibility</h2>
<p>Cloudflare One Appliance only supports 10Gbps SFP+ modules, including RJ45, DAC, and fiber, among others. Many 1 Gbps modules are incompatible with the Intel driver used internally, and thus are not supported.</p>
<p>Cloudflare supports the following SFP+ inputs:</p>
<ul>
<li>10 Gbps Intel-compatible optics using 10GBase-SR, LR, ER. This includes Intel-compatible active optical cables (AOC) cables at 10 Gbps.</li>
<li>10 Gbps DAC Twinax cables, compatible with SFF-8431 v4.1 and SFF-8472 v10.4</li>
<li>10GBASE-T RJ45 converter modules</li>
</ul>
<p>Cloudflare successfully deployed commonly available 10G modules that are also compatible across many vendors:</p>
<ul>
<li>StarTech Dell EMC Twinax SFP+ DAC</li>
<li>Ubiquiti multi-mode, duplex, 10 Gbps fiber transceiver modules</li>
</ul>
<p>Keep in mind that SFP+ modules/cables have to be compatible at both ends, that is, both sides of the connection should be 10 Gbps, and it should really be the same module/cable that is compatible with both hardware stacks. The choice of module/optic/cable ultimately depends on your specific interoperability needs, and it is much less of a &quot;plug and play&quot; situation as one expects from RJ45.</p>
<h2 id="recover-from-unsupported-sfp-inputs">Recover from unsupported SFP+ inputs</h2>
<p>SFP+ modules should be installed and tested prior to deploying Cloudflare One Appliance into production usage.</p>
<p>An unsupported SFP+ input is indicated by the interface failing to come up (that is, the Cloudflare One Appliance has no status lights), and also by the port (7 or 8) going offline until the hardware is rebooted.</p>
<p>When an unsupported module is plugged, the module should be removed and then the Cloudflare One Appliance rebooted by removing power for five seconds. The module should not remain plugged during reboot, or the Cloudflare One Appliance will have to be rebooted again after the module is removed.</p>
