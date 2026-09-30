<p>If you initially set up <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/">incoming zone transfers (Cloudflare as secondary)</a>, you can later convert your zone to use a <a href="/dns/zone-setups/full-setup/">primary setup</a> (also know as full setup).</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="subdomain-setup">Subdomain setup</h3>
@markup("md", "content/.markup/bodies/7969.md")
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
<h2 id="2-prepare-for-the-conversion"><ol start="2">
<li>Prepare for the conversion</li>
</ol></h2>
<ol>
<li>Plan for <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/">DNSSEC settings</a>. If you were previously using <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/#set-up-pre-signed-dnssec">Pre-signed DNSSEC</a>, consider disabling DNSSEC before starting the conversion.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7968.md")
</aside>
<ol start="2">
<li>
<p>Make sure the <a href="/dns/proxy-status/">proxy statuses</a> of your DNS records are consistently set:</p>
<ul>
<li>If you have <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/proxy-traffic/">Secondary DNS override</a>, confirm each record has the appropriate setting (<strong>Proxied</strong> or <strong>DNS only</strong>).</li>
<li>If <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/proxy-traffic/">Secondary DNS override</a> is disabled, make sure all of your DNS records are listed as <strong>DNS only</strong>.</li>
</ul>
</li>
<li>
<p>(Optional) For consistency, use the <a href="/api/resources/dns/subresources/settings/subresources/zone/methods/edit/">Update DNS Settings</a> endpoint to specify SOA record fields according to your needs. Once Cloudflare automatically generates an SOA record for your zone on primary setup (full), the field overrides will be considered.</p>
</li>
</ol>
<h2 id="3-convert-your-zone"><ol start="3">
<li>Convert your zone</li>
</ol></h2>
<ol>
<li>Use the <a href="/api/resources/zones/methods/edit/">Edit Zone endpoint</a> with <code>type</code> set to <code>full</code> to convert the zone type. Existing DNS records will not be affected.</li>
<li>Go to the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page and take note of your new <strong>Cloudflare Nameservers</strong>.</li>
<li>At your domain registrar (or parent zone), <a href="/dns/nameservers/update-nameservers/">update your nameservers</a>. Replace the nameservers ending in <code>secondary.cloudflare.com</code> by the ones ending in <code>ns.cloudflare.com</code>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7967.md")
</aside>
<ol start="4">
<li>Delete the previous SOA record to make sure Cloudflare generates a new one.</li>
<li>(Optional) If Cloudflare was previously not signing your records and you wish to use DNSSEC, follow the steps to <a href="/dns/dnssec/#enable-dnssec">Enable DNSSEC</a>.</li>
</ol>
