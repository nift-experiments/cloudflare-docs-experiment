<p>Cipher suites are a combination of ciphers used to negotiate security settings during the <a href="https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/">SSL/TLS handshake</a> (and therefore separate from the <a href="/ssl/reference/protocols/">SSL/TLS protocol</a>).</p>
<br />
<p>This section covers cipher suites used in connections between visitors and the Cloudflare network. Cipher suites used between Cloudflare and your origin server are configured separately — refer to <a href="/ssl/origin-configuration/cipher-suites/">Origin server &gt; Cipher suites</a>.</p>
<p><a href="/ssl/edge-certificates/additional-options/cipher-suites/compliance-status/">Compliance standards</a> such as PCI DSS may require specific cipher suites or prohibit older ones, and security testing tools like Qualys SSL Labs may flag Cloudflare's <a href="/ssl/edge-certificates/additional-options/cipher-suites/recommendations/#legacy-default">default configuration</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14167.md")
</aside>
<h2 id="cipher-suites-and-edge-certificates">Cipher suites and edge certificates</h2>
<p>Cloudflare's default cipher suites (<a href="/ssl/edge-certificates/additional-options/cipher-suites/recommendations/">Legacy</a>) balance security and compatibility, which means they include older algorithms that security testing tools may flag.</p>
<p>If the default configuration does not meet your requirements, you can <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/acm/">purchase the Advanced Certificate Manager add-on</a> to <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/">specify more secure cipher suites</a>.</p>
<p>Cipher suite customization is a hostname-level setting. Once specified, the configuration applies to all edge certificates serving that hostname, regardless of <a href="/ssl/edge-certificates/">certificate type</a> (universal, advanced, or custom).</p>
<h2 id="related-ssl-tls-settings">Related SSL/TLS settings</h2>
<p>Although configured independently, cipher suites interact with other SSL/TLS settings.</p>
<h3 id="minimum-tls-version">Minimum TLS Version</h3>
<p>You can specify a <a href="/ssl/edge-certificates/additional-options/minimum-tls/">minimum TLS version</a> that is required for a client to connect to your website or application.</p>
<p>For example, if TLS 1.1 is selected as the minimum, visitors attempting to connect using TLS 1.0 will be rejected while visitors attempting to connect using TLS 1.1, 1.2, or 1.3 (if enabled) will be allowed.</p>
<p>Certain cipher suites are only available in specific TLS versions. If you restrict cipher suites to a <a href="/ssl/edge-certificates/additional-options/cipher-suites/recommendations/">higher security level</a> that excludes older algorithms, you should also adjust your minimum TLS version to match.</p>
<p><a href="/ssl/edge-certificates/additional-options/cipher-suites/compliance-status/">Compliance standards</a> may also require you to increase the minimum TLS version accepted in connections to your website or application.</p>
<h3 id="tls-1-3">TLS 1.3</h3>
<div class="nb-data-component" data-cf-component="Render"></div>
<p>Cloudflare may return the following names for TLS 1.3 cipher suites. This is how they map to <a href="https://www.rfc-editor.org/rfc/rfc8446.html">RFC 8446</a> names:</p>
<table>
<thead>
<tr>
<th>Cloudflare</th>
<th>RFC 8446</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>AEAD-AES128-GCM-SHA256</code></td>
<td><code>TLS_AES_128_GCM_SHA256</code></td>
</tr>
<tr>
<td><code>AEAD-AES256-GCM-SHA384</code></td>
<td><code>TLS_AES_256_GCM_SHA384</code></td>
</tr>
<tr>
<td><code>AEAD-CHACHA20-POLY1305-SHA256</code></td>
<td><code>TLS_CHACHA20_POLY1305_SHA256</code></td>
</tr>
</tbody>
</table>
<h2 id="resources">Resources</h2>
<ul class="directory-listing"><li><a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/">Customize cipher suites</a></li><li><a href="/ssl/edge-certificates/additional-options/cipher-suites/recommendations/">Security levels</a></li><li><a href="/ssl/edge-certificates/additional-options/cipher-suites/compliance-status/">Compliance standards</a></li><li><a href="/ssl/edge-certificates/additional-options/cipher-suites/supported-cipher-suites/">Supported cipher suites</a></li><li><a href="/ssl/edge-certificates/additional-options/cipher-suites/troubleshooting/">Troubleshooting</a></li></ul>
<h2 id="limitations">Limitations</h2>
<p>It is not possible to configure cipher suites for <a href="/pages/">Cloudflare Pages</a> hostnames.</p>
