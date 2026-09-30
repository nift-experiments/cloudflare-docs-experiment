<h2 id="windows-10">Windows 10</h2>
<p>Take note of any DNS addresses you might have set up, and save them in a safe place in case you need to use them later.</p>
<ol>
<li>Select the <strong>Start menu</strong> &gt; <strong>Settings</strong>.</li>
<li>On <strong>Network and Internet</strong>, select <strong>Change Adapter Options</strong>.</li>
<li>Right-click on the Ethernet or Wi-Fi network you are connected to and select <strong>Properties</strong>.</li>
<li>Select <strong>Internet Protocol Version 4</strong>.</li>
<li>Select <strong>Properties</strong> &gt; <strong>Use the following DNS server addresses</strong>.</li>
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv4:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1747.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1748.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1749.md")
</div></details>
<ol start="7">
<li>Select <strong>OK</strong>.</li>
<li>Select <strong>Internet Protocol Version 6</strong>.</li>
<li>Select <strong>Properties</strong> &gt; <strong>Use the following DNS server addresses</strong>.</li>
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv6:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1750.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1751.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1752.md")
</div></details>
<ol start="11">
<li>Select <strong>OK</strong>.</li>
</ol>
<h2 id="windows-11">Windows 11</h2>
<p>Take note of any DNS addresses you might have set up, and save them in a safe place in case you need to use them later.</p>
<ol>
<li>Select the <strong>Start menu</strong> &gt; <strong>Settings</strong>.</li>
<li>On <strong>Network and Internet</strong>, select the adapter you want to configure — such as your Ethernet adapter or Wi-Fi card.</li>
<li>Scroll to <strong>DNS server assignment</strong> and select <strong>Edit</strong>.</li>
<li>Select the <strong>Automatic (DHCP)</strong> drop-down menu &gt; <strong>Manual</strong>.</li>
<li>Select the <strong>IPv4</strong> toggle to turn it on.</li>
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv4:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1753.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1754.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1755.md")
</div></details>
<ol start="7">
<li>Select the <strong>IPv6</strong> toggle.</li>
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv6:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1756.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1757.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1758.md")
</div></details>
<ol start="9">
<li>Select <strong>Save</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1746.md")
</aside>
<h2 id="encrypt-your-dns-queries">Encrypt your DNS queries</h2>
<p>1.1.1.1 supports DNS over TLS (DoT) and DNS over HTTPS (DoH), two standards developed for encrypting plaintext DNS traffic. This prevents untrustworthy entities from interpreting and manipulating your queries. For more information on how to encrypt your DNS queries, please refer to the <a href="/1.1.1.1/encryption/">Encrypted DNS documentation</a>.</p>
