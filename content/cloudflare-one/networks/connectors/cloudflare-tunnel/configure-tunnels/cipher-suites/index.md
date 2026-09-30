<p>Cloudflare Tunnel connections use the cipher suites supported by <code>cloudflared</code>, which relies on the Go TLS library for its TLS implementation. These cipher suites apply to both the TLS connection between Cloudflare's network and <code>cloudflared</code>, and the HTTPS connection between <code>cloudflared</code> and your origin. In both cases, <code>cloudflared</code> negotiates the most secure cipher suite supported by both sides. All tunnel connections use TLS 1.3 and post-quantum encryption by default.</p>
<p>The following table lists the cipher suites supported by <code>cloudflared</code>:</p>
<table>
<thead>
<tr>
<th>Protocol support</th>
<th>Cipher suites</th>
</tr>
</thead>
<tbody>
<tr>
<td>TLS 1.3 only</td>
<td><code>TLS_AES_128_GCM_SHA256</code><br /><code>TLS_AES_256_GCM_SHA384</code><br /><code>TLS_CHACHA20_POLY1305_SHA256</code></td>
</tr>
<tr>
<td>TLS 1.2 only</td>
<td><code>TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256</code><br /><code>TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384</code><br /><code>TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256</code><br /><code>TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384</code><br /><code>TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256</code><br /><code>TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256</code></td>
</tr>
<tr>
<td>Up to and including TLS 1.2</td>
<td><code>TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA</code><br /><code>TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA</code><br /><code>TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA</code><br /><code>TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA</code></td>
</tr>
</tbody>
</table>
