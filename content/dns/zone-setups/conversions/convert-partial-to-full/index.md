<p>If you initially set up a partial domain on Cloudflare, you can later migrate it to a <a href="/dns/zone-setups/full-setup/">primary setup</a> (also know as full setup).</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="subdomain-setup">Subdomain setup</h3>
@markup("md", "content/.markup/bodies/7985.md")
</aside>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-dns-conversion-subdomain-setup-callout-mdx-1">Meaning you have one or more subdomains (`sub.example.com`) added to Cloudflare as their own zone, separate from your apex domain (`example.com`).</li></ol></section>
<h2 id="1-prepare-cloudflare-ssl-tls"><ol>
<li>Prepare Cloudflare SSL/TLS</li>
</ol></h2>
<p>In the Cloudflare dashboard, either order an <a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/">advanced certificate</a> or <a href="/ssl/edge-certificates/custom-certificates/uploading/">upload a custom SSL certificate</a> for your website or application.</p>
<p>You should also verify that the <a href="/ssl/reference/certificate-statuses/">status</a> of your SSL certificate is <strong>Active</strong>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7984.md")
</aside>
<h2 id="2-update-settings-in-authoritative-dns"><ol start="2">
<li>Update settings in authoritative DNS</li>
</ol></h2>
<p>At least 24 hours prior to converting your zone, disable DNSSEC at your authoritative DNS provider.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7983.md")
</aside>
<h2 id="3-convert-to-full-setup"><ol start="3">
<li>Convert to full setup</li>
</ol></h2>
<p>In the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, select your partial zone (CNAME setup) and go to the <strong>DNS Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Convert to Primary DNS</strong> (this will not affect how your traffic is proxied).</li>
<li>Import your records into Cloudflare DNS and verify that they have been configured correctly. Usually, you will want to import <a href="/dns/proxy-status/">unproxied records</a>.</li>
</ol>
<h2 id="4-activate-full-setup"><ol start="4">
<li>Activate full setup</li>
</ol></h2>
<p>Get your assigned Cloudflare nameservers from the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page and <a href="/dns/nameservers/update-nameservers/">update your nameservers</a> at your registrar.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7982.md")
</aside>
<p>Cloudflare recommends that you also <a href="/dns/dnssec/">enable DNSSEC</a> from the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/settings"><strong>DNS Settings</strong></a> page
and add the DS record to your registrar.</p>
<p>Once all the DNS TTLs expire, all your DNS queries will be answered by the Cloudflare global network.</p>
<p>Start proxying additional hostnames by enabling the <a href="/dns/proxy-status/">proxy status</a> (also known as orange-clouding) for specific DNS records. Previously proxied subdomains will continue to be proxied without any interruption.</p>
