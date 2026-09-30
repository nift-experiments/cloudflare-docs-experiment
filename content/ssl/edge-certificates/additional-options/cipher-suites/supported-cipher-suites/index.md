<p>Cloudflare supports the following cipher suites by default. If needed, you can <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/">restrict your website or application</a> to only use specific cipher suites.</p>
<table>
<thead>
<tr>
<th>Cipher name</th>
<th>Minimum protocol</th>
<th><a href="/ssl/edge-certificates/additional-options/cipher-suites/recommendations/">Security recommendation</a></th>
<th>Cipher suite</th>
<th>IANA name</th>
</tr>
</thead>
<tbody>
<tr>
<td>ECDHE-ECDSA-AES128-GCM-SHA256</td>
<td>TLS 1.2</td>
<td>Modern, Compatible, Legacy</td>
<td>[0xc02b]</td>
<td>TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256</td>
</tr>
<tr>
<td>ECDHE-ECDSA-CHACHA20-POLY1305</td>
<td>TLS 1.2</td>
<td>Modern, Compatible, Legacy</td>
<td>[0xcca9]</td>
<td>TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256</td>
</tr>
<tr>
<td>ECDHE-RSA-AES128-GCM-SHA256</td>
<td>TLS 1.2</td>
<td>Modern, Compatible, Legacy</td>
<td>[0xc02f]</td>
<td>TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256</td>
</tr>
<tr>
<td>ECDHE-RSA-CHACHA20-POLY1305</td>
<td>TLS 1.2</td>
<td>Modern, Compatible, Legacy</td>
<td>[0xcca8]</td>
<td>TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256</td>
</tr>
<tr>
<td>ECDHE-ECDSA-AES128-SHA256</td>
<td>TLS 1.2</td>
<td>Compatible, Legacy</td>
<td>[0xc023]</td>
<td>TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256</td>
</tr>
<tr>
<td>ECDHE-ECDSA-AES128-SHA</td>
<td>TLS 1.0</td>
<td>Legacy</td>
<td>[0xc009]</td>
<td>TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA</td>
</tr>
<tr>
<td>ECDHE-RSA-AES128-SHA256</td>
<td>TLS 1.2</td>
<td>Compatible, Legacy</td>
<td>[0xc027]</td>
<td>TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256</td>
</tr>
<tr>
<td>ECDHE-RSA-AES128-SHA</td>
<td>TLS 1.0</td>
<td>Legacy</td>
<td>[0xc013]</td>
<td>TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA</td>
</tr>
<tr>
<td>AES128-GCM-SHA256</td>
<td>TLS 1.2</td>
<td>Legacy</td>
<td>[0x9c]</td>
<td>TLS_RSA_WITH_AES_128_GCM_SHA256</td>
</tr>
<tr>
<td>AES128-SHA256</td>
<td>TLS 1.2</td>
<td>Legacy</td>
<td>[0x3c]</td>
<td>TLS_RSA_WITH_AES_128_CBC_SHA256</td>
</tr>
<tr>
<td>AES128-SHA</td>
<td>TLS 1.0</td>
<td>Legacy</td>
<td>[0x2f]</td>
<td>TLS_RSA_WITH_AES_128_CBC_SHA</td>
</tr>
<tr>
<td>ECDHE-ECDSA-AES256-GCM-SHA384</td>
<td>TLS 1.2</td>
<td>Modern, Compatible, Legacy</td>
<td>[0xc02c]</td>
<td>TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384</td>
</tr>
<tr>
<td>ECDHE-ECDSA-AES256-SHA384</td>
<td>TLS 1.2</td>
<td>Compatible, Legacy</td>
<td>[0xc024]</td>
<td>TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384</td>
</tr>
<tr>
<td>ECDHE-RSA-AES256-GCM-SHA384</td>
<td>TLS 1.2</td>
<td>Modern, Compatible, Legacy</td>
<td>[0xc030]</td>
<td>TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384</td>
</tr>
<tr>
<td>ECDHE-RSA-AES256-SHA384</td>
<td>TLS 1.2</td>
<td>Compatible, Legacy</td>
<td>[0xc028]</td>
<td>TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384</td>
</tr>
<tr>
<td>ECDHE-RSA-AES256-SHA</td>
<td>TLS 1.0</td>
<td>Legacy</td>
<td>[0xc014]</td>
<td>TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA</td>
</tr>
<tr>
<td>AES256-GCM-SHA384</td>
<td>TLS 1.2</td>
<td>Legacy</td>
<td>[0x9d]</td>
<td>TLS_RSA_WITH_AES_256_GCM_SHA384</td>
</tr>
<tr>
<td>AES256-SHA256</td>
<td>TLS 1.2</td>
<td>Legacy</td>
<td>[0x3d]</td>
<td>TLS_RSA_WITH_AES_256_CBC_SHA256</td>
</tr>
<tr>
<td>AES256-SHA</td>
<td>TLS 1.0</td>
<td>Legacy</td>
<td>[0x35]</td>
<td>TLS_RSA_WITH_AES_256_CBC_SHA</td>
</tr>
<tr>
<td>DES-CBC3-SHA</td>
<td>TLS 1.0</td>
<td>Legacy</td>
<td>[0x0a]</td>
<td>TLS_RSA_WITH_3DES_EDE_CBC_SHA</td>
</tr>
<tr>
<td>AEAD-AES128-GCM-SHA256 *</td>
<td>TLS 1.3</td>
<td>Modern, Compatible, Legacy</td>
<td>{0x13,0x01}</td>
<td>TLS_AES_128_GCM_SHA256</td>
</tr>
<tr>
<td>AEAD-AES256-GCM-SHA384 *</td>
<td>TLS 1.3</td>
<td>Modern, Compatible, Legacy</td>
<td>{0x13,0x02}</td>
<td>TLS_AES_256_GCM_SHA384</td>
</tr>
<tr>
<td>AEAD-CHACHA20-POLY1305-SHA256 *</td>
<td>TLS 1.3</td>
<td>Modern, Compatible, Legacy</td>
<td>{0x13,0x03}</td>
<td>TLS_CHACHA20_POLY1305_SHA256</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="tls-1-3-minimum-protocol">* TLS 1.3 minimum protocol</h3>
@markup("md", "content/.markup/bodies/14162.md")
</aside>
