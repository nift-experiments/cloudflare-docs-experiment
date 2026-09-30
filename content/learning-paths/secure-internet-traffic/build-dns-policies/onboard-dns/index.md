<p>The fastest way to start filtering DNS queries is to change your DNS resolver to use a specific Gateway endpoint. You can make this change at the browser, OS, or router level.</p>
<p>Choose this option if:</p>
<ul>
<li>You want to try out DNS filtering without installing software.</li>
<li>You do not need to filter by user identity.</li>
<li>You want to apply blanket DNS policies to all devices in a physical location, such as a retail store or office.</li>
</ul>
<h2 id="change-dns-resolver-in-browser">Change DNS resolver in browser</h2>
<p>To configure your browser to send traffic to Gateway:</p>
<ol>
<li>
<p>Obtain your DNS over HTTPS (DoH) address:</p>
<ol>
<li>Go to <strong>Gateway</strong> &gt; <strong>DNS locations</strong>.</li>
<li>Select <strong>Add a location</strong>.</li>
<li>Enter a name for the location.</li>
<li>Turn on <strong>Set as Default DNS Location</strong>.</li>
<li>Select <strong>Add location</strong>.</li>
<li>Copy your <strong>DNS over HTTPS</strong> hostname: <code>https://&lt;YOUR_DOH_SUBDOMAIN&gt;.cloudflare-gateway.com/dns-query</code></li>
</ol>
</li>
<li>
<p>Follow the configuration instructions for your browser:</p>
</li>
</ol>
<details class="nb-details"><summary>Mozilla Firefox</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10259.md")
</div></details>
<details class="nb-details"><summary>Google Chrome</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10260.md")
</div></details>
<details class="nb-details"><summary>Microsoft Edge</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10261.md")
</div></details>
<details class="nb-details"><summary>Brave</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10262.md")
</div></details>
<details class="nb-details"><summary>Safari</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10263.md")
</div></details>
<ol start="3">
<li>Verify that third-party firewall or TLS decryption software does not inspect or block traffic to the DoH endpoint: <code>https://&lt;YOUR_DOH_SUBDOMAIN&gt;.cloudflare-gateway.com/dns-query</code>.</li>
</ol>
<p>DNS filtering is now turned on for this browser.</p>
<p>To configure your router or OS, or to add additional DNS endpoints, refer to <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">DNS locations</a>.</p>
