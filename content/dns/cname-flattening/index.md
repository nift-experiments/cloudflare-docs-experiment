<p>CNAME flattening speeds up CNAME resolution and allows you to use a <a href="/dns/manage-dns-records/reference/dns-record-types/#cname">CNAME record</a> at your <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7719.md")
</div> (`example.com`).
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7718.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>With CNAME flattening, Cloudflare finds the IP address that a CNAME points to. This process could involve a single lookup or multiple (if your CNAME points to another CNAME). Cloudflare then returns the final IP address instead of a CNAME record, helping DNS queries resolve faster.</p>
<p>For more details on the steps involved in CNAME flattening, review the <a href="/dns/cname-flattening/cname-flattening-diagram/">CNAME flattening diagram</a> and refer to the <a href="https://blog.cloudflare.com/introducing-cname-flattening-rfc-compliant-cnames-at-a-domains-root/">Cloudflare blog post</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7717.md")
</aside>
<h2 id="aspects-to-keep-in-mind">Aspects to keep in mind</h2>
<ul>
<li>CNAME flattening happens by default in some cases. Refer to <a href="/dns/cname-flattening/set-up-cname-flattening/">Setup</a> for details.</li>
<li>CNAME to a different Cloudflare account is prohibited and will result in <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1014/">Error 1014: CNAME Cross-User Banned</a></li>
<li></li>
</ul>
<p>If a CNAME target is being used to verify a domain for a third-party service, turning on <a href="/dns/cname-flattening/set-up-cname-flattening/#for-all-cname-records">CNAME flattening for all CNAME records</a> may cause the verification to fail since the CNAME record itself will not be returned directly.</p>
<ul>
<li>If the final CNAME target has no A/AAAA records (a dangling CNAME), CNAME flattening returns an empty response (NODATA) because there is no IP address to flatten to. This can make it appear as if the DNS record is not propagating. Ensure your CNAME targets resolve to valid A/AAAA records.</li>
</ul>
