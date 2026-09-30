<p>To enable <a href="/ssl/edge-certificates/additional-options/total-tls/">Total TLS</a> - which issues individual certificates for your proxied hostnames - follow these instructions:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14160.md")
</div></div>
<h2 id="aspects-to-consider">Aspects to consider</h2>
<ul>
<li></li>
</ul>
<p>Total TLS certificates follow the Common Name (CN) restriction of 64 characters (<a href="https://www.rfc-editor.org/rfc/rfc5280.html">RFC 5280</a>). If you have a hostname that exceeds this length, you can create an <a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/#create-a-certificate">Advanced Certificate</a> via API to cover it.</p>
