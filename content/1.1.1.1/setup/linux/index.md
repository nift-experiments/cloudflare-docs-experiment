<p>Before you begin, take note of any DNS addresses you might have set up, and save them in a safe place in case you need to use them later.</p>
<p>You can configure 1.1.1.1 using the <a href="#use-command-line-interface-cli">command line</a> or a <a href="#use-graphical-user-interface-gui">graphical interface</a>.</p>
<h2 id="use-command-line-interface-cli">Use command line interface (CLI)</h2>
<p>If you want to use 1.1.1.1 for Families instead of the standard resolver, replace <code>1.1.1.1</code> in the examples below with the corresponding <a href="/1.1.1.1/ip-addresses/">IPv4 or IPv6 address</a>.</p>
<h3 id="resolv-conf"><code>resolv.conf</code></h3>
<p>On most Linux distributions, <code>/etc/resolv.conf</code> controls which DNS resolver the system uses.</p>
<p>To set <code>1.1.1.1</code> as your DNS resolver with <code>1.0.0.1</code> as a backup:</p>
<pre><code class="language-sh">echo -e &quot;nameserver 1.1.1.1\nnameserver 1.0.0.1&quot; | sudo tee /etc/resolv.conf&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/1773.md")
</aside>
<p>You can also edit <code>/etc/resolv.conf</code> manually with a text editor like <code>nano</code> or <code>vim</code>.</p>
<h3 id="systemd-resolved"><code>systemd-resolved</code></h3>
<p>If your system uses <code>systemd-resolved</code> to manage DNS, edit the configuration file at <code>/etc/systemd/resolved.conf</code>:</p>
<ol>
<li>Run the following command, replacing <code>&lt;EDITOR&gt;</code> with your preferred editor.</li>
</ol>
<pre><code class="language-sh">sudo &lt;EDITOR&gt; /etc/systemd/resolved.conf&#10;</code></pre>
<ol start="2">
<li>In the editor, add or edit the following lines:</li>
</ol>
<pre><code class="language-txt">[Resolve]&#10;DNS=1.1.1.1&#10;</code></pre>
<p>To use DNS over TLS, append <code>#one.one.one.one</code> after the IP address (this tells <code>systemd-resolved</code> which hostname to use for TLS verification) and set <code>DNSOverTLS</code> to <code>yes</code>:</p>
<pre><code class="language-txt">[Resolve]&#10;DNS=1.1.1.1#one.one.one.one&#10;DNSOverTLS=yes&#10;</code></pre>
<h2 id="use-graphical-user-interface-gui">Use graphical user interface (GUI)</h2>
<h3 id="gnome">GNOME</h3>
<ol>
<li>Go to <strong>Show Applications</strong> &gt; <strong>Settings</strong> &gt; <strong>Network</strong>.</li>
<li>Select the adapter you want to configure — such as your Ethernet adapter or Wi-Fi card — and select the <strong>Settings</strong> button.</li>
<li>On the <strong>IPv4</strong> tab &gt; <strong>DNS</strong> section, disable the <strong>Automatic</strong> toggle.</li>
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv4:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1774.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1775.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1776.md")
</div></details>
<ol start="5">
<li>Go to <strong>IPv6</strong>.</li>
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv6:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1777.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1778.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1779.md")
</div></details>
<ol start="7">
<li>Select <strong>Apply</strong>.</li>
</ol>
<h3 id="kde-plasma">KDE Plasma</h3>
<ol>
<li>Go to <strong>System Settings</strong> &gt; <strong>Wi-Fi &amp; Internet</strong> &gt; <strong>Wi-Fi &amp; Networking</strong>. (or <strong>Connections</strong>, if on Plasma 5)</li>
<li>Select the connection you want to configure - like your current connected network.</li>
<li>On the <strong>IPv4</strong> tab, select the <strong>Method</strong> drop-down menu &gt; <em>Automatic (Only addresses)</em>.</li>
<li>Select the text box next to <strong>DNS servers</strong>.</li>
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv4:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1780.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1781.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1782.md")
</div></details>
<ol start="6">
<li>On the <strong>IPv6</strong> tab, select the <strong>Method</strong> drop-down menu &gt; <em>Automatic (Only addresses)</em>.</li>
<li>Select the text box next to <strong>DNS servers</strong>.</li>
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv6:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1783.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1784.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1785.md")
</div></details>
<ol start="9">
<li>Select <strong>Apply</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1772.md")
</aside>
