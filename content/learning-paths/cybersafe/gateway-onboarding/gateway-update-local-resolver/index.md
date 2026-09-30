<p>With a Gateway location created, you have the ability to send traffic to your environment. You can test without risk by changing your DNS resolvers in your browser or network settings.</p>
<h2 id="change-dns-resolver-at-the-network-level">Change DNS resolver at the network level</h2>
<p>To configure your device to send traffic to Gateway:</p>
<details class="nb-details"><summary>macOS</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9701.md")
</div></details>
<details class="nb-details"><summary>Windows</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9702.md")
</div></details>
<details class="nb-details"><summary>Linux</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9703.md")
</div></details>
<details class="nb-details"><summary>iPhone</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9704.md")
</div></details>
<details class="nb-details"><summary>Android</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9705.md")
</div></details>
<h2 id="change-dns-resolver-in-the-browser">Change DNS resolver in the browser</h2>
<p>To configure your browser to send traffic to Gateway:</p>
<ol>
<li>
<p>Obtain your DNS over HTTPS (DoH) address:</p>
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>DNS locations</strong>.</li>
<li>Select the default location.</li>
<li>Copy your <strong>DNS over HTTPS</strong> hostname: <code>https://&lt;YOUR_DOH_SUBDOMAIN&gt;.cloudflare-gateway.com/dns-query</code></li>
</ol>
</li>
<li>
<p>Follow the configuration instructions for your browser:</p>
</li>
</ol>
<details class="nb-details"><summary>Mozilla Firefox</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9706.md")
</div></details>
<details class="nb-details"><summary>Google Chrome</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9707.md")
</div></details>
<details class="nb-details"><summary>Microsoft Edge</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9708.md")
</div></details>
<details class="nb-details"><summary>Brave</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9709.md")
</div></details>
<details class="nb-details"><summary>Safari</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/9710.md")
</div></details>
<ol start="3">
<li>Verify that third-party firewall or TLS decryption software does not inspect or block traffic to the DoH endpoint: <code>https://&lt;YOUR_DOH_SUBDOMAIN&gt;.cloudflare-gateway.com/dns-query</code>.</li>
</ol>
<h2 id="more-locations">More locations</h2>
<p>To configure your router or OS, or to add additional DNS endpoints, refer to <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">DNS locations</a>.</p>
