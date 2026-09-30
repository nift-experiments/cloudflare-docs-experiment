<p>The domain name system (DNS) translates domain names into numeric Internet addresses. However, DNS is a fundamentally insecure protocol. It does not guarantee where DNS records come from and accepts any requests given to it.</p>
<p><a href="/dns/dnssec/">DNSSEC</a> creates a secure layer to the domain name system by adding cryptographic signatures to DNS records. By doing so, your request can check the signature to verify that the record you need comes from the authoritative nameserver and was not altered along the way.</p>
<h2 id="enable-or-disable-dnssec">Enable or disable DNSSEC</h2>
<p>Cloudflare Registrar offers one-click DNSSEC activation for free to all customers:</p>
<ol>
<li>In Cloudflare dashboard, go to the <strong>Manage Domains</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Find the domain that you want to activate DNSSEC and select <strong>Manage</strong>.</li>
<li>Select <strong>Configuration</strong> &gt; <strong>Enable DNSSEC</strong>. If DNSSEC was previously activated, select <strong>Disable DNSSEC</strong> to disable it.</li>
</ol>
<p>Cloudflare publishes delegation signer (DS) records in the form of <a href="https://www.cloudflare.com/dns/dnssec/how-dnssec-works/">CDS and CDNSKEY records</a> for a domain delegated to Cloudflare. Cloudflare Registrar scans those records at regular intervals, gathers those details and sends them to your domain's registry.</p>
<p>This process can take one to two days after you first enable DNSSEC.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12755.md")
</aside>
<h2 id="confirming-dnssec">Confirming DNSSEC</h2>
<p>When DNSSEC has been successfully applied to your domain, Cloudflare shows you a confirmed status. Go to <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/settings"><strong>DNS</strong> &gt; <strong>Settings</strong></a> in the Cloudflare dashboard, and scroll down to <strong>DNSSEC</strong>.</p>
<p>You can also confirm this by reviewing the <a href="https://lookup.icann.org/">WHOIS information</a> for your domain. Domains with DNSSEC will read <code>signedDelegation</code> in the DNSSEC field.</p>
