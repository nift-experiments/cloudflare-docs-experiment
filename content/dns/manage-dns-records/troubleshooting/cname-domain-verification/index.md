<p>When configuring services from external providers - such as email services, for example - it is possible that they require you to verify your domain by placing a CNAME record at your zone, similar to the following:</p>
<pre><code class="language-txt">&lt;value&gt;._domainkey.example.com CNAME &lt;hostname&gt;.&lt;service provider domain&gt;&#10;</code></pre>
<p>Consider the sections below if this is not working correctly for you.</p>
<h2 id="causes">Causes</h2>
<p>You may find issues if you have one of the following:</p>
<ul>
<li>The CNAME record you created for domain verification is set to <a href="/dns/proxy-status/"><strong>Proxied</strong></a>.</li>
<li>The CNAME record is correctly set to DNS only (not proxied) but, in your <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/settings">zone settings</a>, <a href="/dns/cname-flattening/set-up-cname-flattening/#for-all-cname-records"><strong>CNAME flattening for all CNAME records</strong></a> is on.</li>
<li>The CNAME record is correctly set to DNS only (not proxied) but CNAME flattening is set <a href="/dns/cname-flattening/set-up-cname-flattening/#per-record">for that record specifically</a>.</li>
<li>An <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/">NS record</a> exists, causing a different DNS provider to be authoritative for the subdomain.</li>
</ul>
<h2 id="solution">Solution</h2>
<p>Make sure that:</p>
<ul>
<li>In your zone DNS settings: <a href="/dns/cname-flattening/"><strong>CNAME flattening for all CNAME records</strong></a> is turned off.</li>
<li>On the DNS records table: you have filled in the CNAME record fields correctly, proxy status is set to <strong>DNS only</strong>, and <strong>Flatten</strong> is turned off.</li>
<li>You have the correct NS configuration, and either:
<ul>
<li>Make sure that the CNAME record is set as expected with the DNS provider that the NS record points to.</li>
<li>Review your configuration for other DNS records that may be affected by the NS record. Once you are aware of any consequences or have made any necessary adjustments, remove the NS record so that the CNAME is resolved to the target you configured on Cloudflare.</li>
</ul>
</li>
</ul>
