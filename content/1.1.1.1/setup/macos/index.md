<p>These steps configure 1.1.1.1 as the DNS resolver for a specific network service (such as Wi-Fi or Ethernet) on your Mac.</p>
<p>Take note of any DNS addresses you might have set up, and save them in a safe place in case you need to use them later.</p>
<ol>
<li>Go to <strong>System Settings</strong>. You can find it by pressing <code>CMD + Space</code> on your keyboard and typing <code>System Settings</code>.</li>
<li>Go to <strong>Network</strong>.</li>
<li>Select a network service.</li>
<li>Select <strong>Details</strong>.</li>
<li>Go to <strong>DNS</strong>.</li>
<li>Under <strong>DNS Servers</strong>, select <strong>Add</strong>.</li>
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv4:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1766.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1767.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1768.md")
</div></details>
<ol start="8">
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv6:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1769.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1770.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1771.md")
</div></details>
<ol start="9">
<li>Select <strong>OK</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1765.md")
</aside>
<h2 id="encrypt-your-dns-queries">Encrypt your DNS queries</h2>
<p>1.1.1.1 supports DNS over TLS (DoT) and DNS over HTTPS (DoH), two standards developed for encrypting plaintext DNS traffic. This prevents untrustworthy entities from interpreting and manipulating your queries. For more information on how to encrypt your DNS queries, please refer to the <a href="/1.1.1.1/encryption/">Encrypted DNS documentation</a>.</p>
