<p>If you initially set up <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/">incoming zone transfers (Cloudflare as secondary)</a>, you can later convert your zone to use a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7964.md")
</div>.
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="subdomain-setup">Subdomain setup</h3>
@markup("md", "content/.markup/bodies/7963.md")
</aside>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-dns-conversion-subdomain-setup-callout-mdx-1">Meaning you have one or more subdomains (`sub.example.com`) added to Cloudflare as their own zone, separate from your apex domain (`example.com`).</li></ol></section>
<p>Follow the steps below to achieve this conversion.</p>
<h2 id="1-stop-transferring-the-zone"><ol>
<li>Stop transferring the zone</li>
</ol></h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>DNS Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Under <strong>DNS Zone Transfers</strong>, and select <strong>Manage linked peers</strong>.</li>
<li>Unlink the peer and select <strong>Save</strong>.</li>
</ol>
<p>At this point, your zone will be read-only.</p>
<h2 id="2-configure-your-authoritative-dns-provider"><ol start="2">
<li>Configure your authoritative DNS provider</li>
</ol></h2>
<ol>
<li>
<p>(Optional) If you are also migrating to a new authoritative DNS provider, export a zone file from the previous provider and import it into the new one.</p>
</li>
<li>
<p>At your authoritative DNS provider, create <code>CNAME</code> records pointing to <code>{your-hostname}.cdn.cloudflare.net</code> for every hostname you wish to proxy through Cloudflare.</p>
<details class="nb-details"><summary>Example CNAME record at authoritative DNS provider</summary><div class="nb-details-body">
</li>
</ol>
@markup("md", "content/.markup/bodies/7965.md")
</div></details>
<ol start="3">
<li>At your authoritative DNS provider, remove any previously existing <code>A</code>, <code>AAAA</code>, or <code>CNAME</code> records referencing the hostnames you want to proxy through Cloudflare. For these hostnames, leave only the records pointing to <code>{your-hostname}.cdn.cloudflare.net</code>.</li>
</ol>
<h2 id="3-convert-your-cloudflare-zone"><ol start="3">
<li>Convert your Cloudflare zone</li>
</ol></h2>
<ol>
<li>
<p>Back at your Cloudflare zone, confirm that you have all the <code>A</code>, <code>AAAA</code>, or <code>CNAME</code> <a href="/dns/manage-dns-records/how-to/create-dns-records/">DNS records</a> needed for the hostnames you pointed to <code>{your-hostname}.cdn.cloudflare.net</code> in the previous step. You can also delete any DNS records that have a different type, as they will no longer resolve once you convert your zone to a CNAME setup (partial).</p>
</li>
<li>
<p>Use the <a href="/api/resources/zones/methods/edit/">Edit Zone endpoint</a> with <code>type</code> set to <code>partial</code> to convert the zone type. Existing DNS records will not be affected.</p>
</li>
<li>
<p>On the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page, get the <strong>Verification TXT Record</strong> and add it at your authoritative DNS provider.</p>
<details class="nb-details"><summary>Example verification record</summary><div class="nb-details-body">
</li>
</ol>
@markup("md", "content/.markup/bodies/7966.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7962.md")
</aside>
<h2 id="4-update-nameservers"><ol start="4">
<li>Update nameservers</li>
</ol></h2>
<p>At your domain registrar (or parent zone), <a href="/dns/nameservers/update-nameservers/">update the nameservers</a>. In a CNAME setup (partial), only the nameservers of your external DNS provider should be listed.</p>
<pre><code>- Remove any `secondary.cloudflare.com` nameservers if you used to have them.&#10;- If you are also migrating to a new authoritative DNS provider, add your new nameservers.&#10;</code></pre>
