<p>You need to enable DMARC Management to allow Cloudflare to process DMARC reports on your behalf. DMARC Management only works with <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/1142.md")
</div> (for example, `example.com`, not `blog.example.com`) and not domains in [subdomain setups](/dns/zone-setups/subdomain-setup/).
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="a-warning-on-dmarc-management-and-spf-records">A warning on DMARC Management and SPF records</h3>
@markup("md", "content/.markup/bodies/1141.md")
</aside>
<p>To enable DMARC Management:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select your account and domain.</li>
<li>Go to <strong>Email</strong> &gt; <strong>DMARC Management</strong>.</li>
<li>Select <strong>Enable DMARC Management</strong>.</li>
<li>DMARC Management will scan your zone for DMARC records, and will present you with two outcomes:
<ul>
<li>If no DMARC record is found, Cloudflare will automatically invite you to add one that you can edit later. Select <strong>Add</strong> to continue.</li>
<li>If a DMARC record is found in your zone, Cloudflare will add another <code>rua</code> (Reporting URI for Aggregate data) entry to it. The <code>rua</code> tag specifies the URI (typically a <code>mailto:</code> address) where aggregate DMARC reports are sent. This additional entry uses a Cloudflare email address so that Cloudflare can receive and process DMARC reports on your behalf. Select <strong>Next</strong> to continue.</li>
</ul>
</li>
</ol>
<p>DMARC Management (beta) is now active. However, it may take up to 24 hours to receive your first DMARC report and to display this information in DMARC Management.</p>
