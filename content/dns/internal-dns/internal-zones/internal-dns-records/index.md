<p>Internal zones can contain the same <a href="/dns/manage-dns-records/reference/dns-record-types/">DNS record types</a> that Cloudflare supports for public zones.</p>
<p>You can manage internal DNS records in the same way as you would manage public DNS records, with the difference that <a href="/dns/proxy-status/">proxy status</a> does not apply to internal DNS records.</p>
<p>Refer to <a href="/dns/manage-dns-records/how-to/create-dns-records/">Manage DNS records</a> or to the <a href="/api/resources/dns/subresources/records/">API documentation</a> for further guidance.</p>
<h2 id="cname-flattening-in-internal-dns">CNAME flattening in Internal DNS</h2>
<p>With <a href="/dns/cname-flattening/">CNAME flattening</a>, Cloudflare finds the final target content that a CNAME points to and then returns this content instead of a CNAME record. With Internal DNS, CNAME flattening is applied by default and cannot be turned off.</p>
<p>Cloudflare will try to flatten the CNAME record considering both the specified <a href="/dns/internal-dns/dns-views/">DNS view</a> and any existing <a href="/dns/internal-dns/internal-zones/reference-zones/">reference zones</a>. If the reference zone then has another CNAME, the record will again be considered from the perspective of the original view.</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7760.md")
</div></details>
<p>If it is not possible to flatten the CNAME record, the following will happen:</p>
<ol>
<li>The CNAME record is returned to <a href="/dns/internal-dns/#architecture-overview">Gateway resolver</a> as-is.</li>
<li>Gateway resolver will process the returned record, depending on the <strong>Fallback through public DNS</strong> configuration:
<ul>
<li>On: Gateway will try to resolve the query by sending it to Cloudflare's public DNS resolver (<a href="/1.1.1.1/">1.1.1.1</a>).</li>
<li>Off: Gateway will return the response as-is to the client.</li>
</ul>
</li>
</ol>
