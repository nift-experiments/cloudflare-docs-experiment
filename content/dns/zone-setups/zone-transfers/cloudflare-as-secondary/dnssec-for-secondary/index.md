<p><a href="https://www.cloudflare.com/learning/dns/dns-security/">DNS Security Extensions (DNSSEC)</a> increase security by adding cryptographic signatures to DNS records. When you use multiple providers and Cloudflare is secondary, you have a few options to enable DNSSEC for records served by Cloudflare.</p>
<ul>
<li><strong><a href="/dns/dnssec/multi-signer-dnssec/setup/">Multi-signer DNSSEC</a></strong>: Both Cloudflare and your primary DNS provider know the signing keys of each other and perform their own live-signing of DNS records, in accordance with <a href="https://www.rfc-editor.org/rfc/rfc8901.html">RFC 8901</a>.</li>
<li><strong><a href="#set-up-live-signing-dnssec">Live signing</a></strong>: If your domain is not delegated to your primary provider's nameservers and Cloudflare secondary nameservers are the only nameservers authoritatively responding to DNS queries (hidden primary setup), you can choose this option to allow Cloudflare to perform live-signing of your DNS records.</li>
<li><strong><a href="#set-up-pre-signed-dnssec">Pre-signed</a></strong>: Your primary DNS provider signs records and transfers out the signatures. Cloudflare then serves these records and signatures as is, without doing any signing. By default, Cloudflare uses <a href="https://www.cloudflare.com/dns/dnssec/how-dnssec-works/">NSEC records</a> and not NSEC3 - refer to <a href="/dns/dnssec/enable-nsec3/">NSEC3 support</a> if needed. Also, Pre-signed DNSSEC does not support <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/proxy-traffic/">Secondary DNS Overrides</a> nor <a href="/load-balancing/">Load Balancing</a>.</li>
</ul>
<hr />
<h2 id="set-up-multi-signer-dnssec">Set up multi-signer DNSSEC</h2>
<p>Refer to <a href="/dns/dnssec/multi-signer-dnssec/setup/">Set up multi-signer DNSSEC</a> and follow the instructions, considering the note about Cloudflare as Secondary.</p>
<hr />
<h2 id="set-up-live-signing-dnssec">Set up live signing DNSSEC</h2>
<p>If you use Cloudflare secondary nameservers as the only nameservers authoritatively responding to DNS queries (hidden primary setup), you can enable live signing DNSSEC to have Cloudflare sign the records for your zone.</p>
<p>In this setup, DNSSEC on your primary DNS provider does not need to be enabled.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8053.md")
</div></div>
<hr />
<h2 id="set-up-pre-signed-dnssec">Set up pre-signed DNSSEC</h2>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li>Your secondary zone in Cloudflare already exists and zone transfers from your primary DNS provider are working correctly.</li>
<li>You have considered whether your primary DNS provider uses NSEC or NSEC3, and have enabled <a href="/dns/dnssec/enable-nsec3/">NSEC3 support</a> if needed.</li>
<li>Your primary DNS provider transfers out DNSSEC related records, such as RRSIG, DNSKEY, and NSEC.</li>
</ul>
<h3 id="steps">Steps</h3>
<ol>
<li>Enable DNSSEC at your primary DNS provider.</li>
<li>Enable DNSSEC for your zone at Cloudflare, using either the Dashboard or the API.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8048.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8056.md")
</div></div>
<ol start="3">
<li>
<p>Make sure Cloudflare nameservers are added at your registrar. You can see your Cloudflare nameservers on the dashboard by going to the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page.</p>
</li>
<li>
<p>Make sure there is a DS record added at your registrar. The DS record is obtained from your primary DNS provider (the signer of the zone) and is what indicates to DNS resolvers that your zone has DNSSEC enabled.</p>
</li>
</ol>
