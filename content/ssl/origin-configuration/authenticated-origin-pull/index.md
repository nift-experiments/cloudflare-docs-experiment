<p>Authenticated Origin Pulls (AOP) helps ensure requests to your origin server come from the Cloudflare network, which provides an additional layer of security on top of <a href="/ssl/origin-configuration/ssl-modes/full/">Full</a> or <a href="/ssl/origin-configuration/ssl-modes/full-strict/">Full (strict)</a> encryption modes.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="check-your-encryption-mode">Check your encryption mode</h3>
@markup("md", "content/.markup/bodies/14283.md")
</aside>
<p>Without AOP, anyone who discovers your origin server's IP address can send requests directly, bypassing Cloudflare and all its protections. When you combine AOP with the <a href="/waf/">Cloudflare Web Application Firewall (WAF)</a>, your origin only accepts requests that have passed through Cloudflare, which means every request is evaluated by the WAF before reaching your server.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="not-compatible-with-cloudflare-tunnel">Not compatible with Cloudflare Tunnel</h3>
@markup("md", "content/.markup/bodies/14282.md")
</aside>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="configuration-levels">Configuration levels</h2>
<p>AOP has three independent configuration levels. Each uses its own certificate and enablement setting, and each requires configuration on your origin server. Refer to the specific setup guides for details.</p>
<ul>
<li>
<p><a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/global/">Global</a>: Uses a Cloudflare-provided certificate that is shared across all Cloudflare accounts. Applies to all proxied traffic on the zone. This is the simplest setup but only guarantees that a request is coming from the Cloudflare network.</p>
</li>
<li>
<p><a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/">Zone-level</a>: Uses a certificate that you upload. Applies to all proxied traffic on the zone. Provides stricter security because the certificate is exclusive to your account. Zone-level certificates take precedence over global certificates.</p>
</li>
<li>
<p><a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/">Per-hostname</a>: Uses a certificate that you upload, applied to specific hostnames. Per-hostname certificates take precedence over zone-level and global certificates for the specified hostname.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14281.md")
</aside>
<h2 id="when-to-use-your-own-certificate">When to use your own certificate</h2>
<p>Global AOP uses a Cloudflare-provided certificate shared across all accounts, so it only proves a request came from the Cloudflare network — not from your account specifically. If you need to guarantee requests come from your account, set up <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/">zone-level</a> or <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/">per-hostname</a> AOP with your own certificate.</p>
<p>Using your own certificate is also required for <a href="https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards">FIPS</a> compliance. For broader origin protection guidance, refer to <a href="/fundamentals/security/protect-your-origin-server/">Protect your origin server</a>.</p>
<h2 id="post-quantum-certificates">Post-quantum certificates</h2>
<p>Zone-level and per-hostname AOP support ML-DSA (FIPS 204) post-quantum client certificates. Refer to <a href="/ssl/post-quantum-cryptography/pqc-to-origin/#post-quantum-signatures">Post-quantum signatures</a> for certificate generation and upload guidance.</p>
<h2 id="related-topics">Related topics</h2>
<ul>
<li><a href="/ssl/origin-configuration/ssl-modes/">SSL/TLS Encryption Modes</a></li>
</ul>
