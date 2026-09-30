<p>If you initially set up a <a href="/dns/zone-setups/partial-setup/">partial zone (CNAME setup)</a> on Cloudflare, you can later convert it to use a <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">secondary setup</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="subdomain-setup">Subdomain setup</h3>
@markup("md", "content/.markup/bodies/7973.md")
</aside>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-dns-conversion-subdomain-setup-callout-mdx-1">Meaning you have one or more subdomains (`sub.example.com`) added to Cloudflare as their own zone, separate from your apex domain (`example.com`).</li></ol></section>
<p>This page will guide you through this conversion using <a href="/dns/manage-dns-records/how-to/import-and-export/">export and import</a> and API calls.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Make sure you consider the following:</p>
<ul>
<li>Proxying traffic with secondary zones requires a setting that is not turned on by default. Refer to <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/proxy-traffic/">Secondary DNS override</a> to learn more. The steps below include enabling this setting.</li>
<li>There are a few options for <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/">DNSSEC with incoming zone transfers</a>. If you want to use DNSSEC, plan for which option you will configure and confirm that your other DNS provider(s) support the setup.</li>
<li>You can prepare SSL/TLS in advance by either ordering an <a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/">advanced certificate</a> or <a href="/ssl/edge-certificates/custom-certificates/uploading/">uploading a custom certificate</a>. You should confirm that the certificate covers all your proxied hostnames and that the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates">status of your SSL certificate</a> is <strong>Active</strong>.</li>
</ul>
<h2 id="1-prepare-a-zone-file"><ol>
<li>Prepare a zone file</li>
</ol></h2>
<ol>
<li>Export a zone file from the authoritative DNS provider you were using with your CNAME setup (partial).</li>
<li>Edit the zone file to remove any occurrences of the <code>cdn.cloudflare.net</code> suffix.</li>
</ol>
<ul>
<li>If the <code>CNAME</code> target is only appending the Cloudflare suffix to the same hostname at which it is created, replace it by the records on the Cloudflare partial zone.</li>
</ul>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7974.md")
</div></details>
<ul>
<li>If the <code>CNAME</code> record points to a different hostname, keep this record but remove the <code>cdn.cloudflare.net</code> suffix, and also bring the records from the Cloudflare partial zone.</li>
</ul>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7975.md")
</div></details>
<h2 id="2-configure-the-cloudflare-zone"><ol start="2">
<li>Configure the Cloudflare zone</li>
</ol></h2>
<ol>
<li>Use the <a href="/api/resources/dns/subresources/records/methods/import/">Import DNS Records endpoint</a> with a properly <a href="/dns/manage-dns-records/how-to/import-and-export/#format-your-zone-file">formatted zone file</a> to import the records into your partial zone.</li>
</ol>
<p>The zone file size limit is 256 KiB (262144 bytes).
Existing and already
proxied records will not be overwritten by the import.</p>
<ol start="2">
<li>Use the <a href="/api/resources/dns/subresources/settings/subresources/zone/methods/edit/">Update DNS Settings endpoint</a> with <code>secondary_overrides</code> set to <code>true</code>, to enable Secondary DNS Override.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7972.md")
</aside>
<ol start="3">
<li>
<p>Use the <a href="/api/resources/zones/methods/edit/">Edit Zone endpoint</a> with <code>type</code> set to <code>secondary</code>, to convert the zone type.</p>
<p>You can verify if it answers as expected by querying the new assigned secondary nameservers. You can find your nameservers on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page, and they should follow a format like <code>ns0123.secondary.cloudflare.com</code>.</p>
</li>
</ol>
<pre><code class="language-bash">&#35; Replace ns0123 with your actual Cloudflare nameservers&#10;dig example.com @ns0123.secondary.cloudflare.com&#10;</code></pre>
<ol start="4">
<li>At your registrar, <a href="/dns/nameservers/update-nameservers/">update your nameservers</a> to point to the Cloudflare nameservers.</li>
</ol>
<p>Once the time to live (TTL) of previous <code>NS</code> records is expired and this information is evicted from resolvers' cache, your zone will be properly delegated to Cloudflare. In order to update DNS records, you must configure <a href="/dns/zone-setups/zone-transfers/">zone transfers</a> in the next steps.</p>
<h2 id="3-configure-the-zone-transfers"><ol start="3">
<li>Configure the zone transfers</li>
</ol></h2>
<ol>
<li>Remove all references to <code>cdn.cloudflare.net</code> from your primary DNS provider. You can do this by importing the same zone file you prepared in <a href="#1-prepare-a-zone-file">Step 1</a> onto your primary zone.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7971.md")
</aside>
<ol start="2">
<li>Enable outgoing zone transfers at your primary provider and create a peer DNS server on your Cloudflare account.</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7978.md")
</div></div>
<ol start="3">
<li>Link your Cloudflare zone to the peer DNS server you just created.</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7981.md")
</div></div>
<ol start="4">
<li>On the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/settings"><strong>DNS Settings</strong></a> page, confirm the linked peer is listed under <strong>DNS Zone Transfers</strong>, and select <strong>Initiate zone transfer</strong>. Alternatively, you can use the <a href="/api/resources/dns/subresources/zone_transfers/subresources/force_axfr/methods/create/">Force AXFR endpoint</a>.</li>
</ol>
