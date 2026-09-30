<p>With custom ingest domains, you can configure your RTMPS feeds to use an ingest URL that you specify instead of using <code>live.cloudflare.com.</code></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14404.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Live inputs</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Settings</strong>, above the list. The <strong>Custom Input Domains</strong> page displays.</li>
<li>Under <strong>Domain</strong>, add your domain and select <strong>Add domain</strong>.</li>
<li>At your DNS provider, add a CNAME record that points to <code>live.cloudflare.com</code>. If your DNS provider is Cloudflare, this step is done automatically.</li>
</ol>
<p>If you are using Cloudflare for DNS, ensure the <a href="/dns/proxy-status/"><strong>Proxy status</strong></a> of your ingest domain is <strong>DNS only</strong> (grey-clouded).</p>
<h2 id="delete-a-custom-domain">Delete a custom domain</h2>
<ol>
<li>From the <strong>Custom Input Domains</strong> page under <strong>Hostnames</strong>, locate the domain.</li>
<li>Select the menu icon under <strong>Action</strong>. Select <strong>Delete</strong>.</li>
</ol>
