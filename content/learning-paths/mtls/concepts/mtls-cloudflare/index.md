<p>In this implementation guide we will be focusing on the L7 / Application Layer security for HTTP/S requests targeting <a href="/dns/proxy-status/">proxied</a> hostnames, including the <a href="/ssl/origin-configuration/ssl-modes/">first connection</a> between client and Cloudflare.</p>
<p>Some common mTLS use cases are:</p>
<ul>
<li>Protect and verify legitimate API traffic by verifying Client Certificates provided during TLS/SSL handshakes.</li>
<li>Check IoT devices' identity by verifying Client Certificates they provide during TLS/SSL handshakes.</li>
</ul>
<p>There are two main ways to use mTLS at Cloudflare, either by using the Application Security offering (optionally including <a href="/api-shield/">API Shield</a>) or <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a>. Below is a non-exhaustive overview table of their differences:</p>
<table>
<thead>
<tr>
<th align="left">Feature</th>
<th align="left">Application Security (Client Certificate + WAF)</th>
<th align="left">Cloudflare Access (mTLS)</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mainly used for</td>
<td align="left">External Authentication (that is, APIs)</td>
<td align="left">Internal Authentication (that is, employees)</td>
</tr>
<tr>
<td align="left">Availability</td>
<td align="left">By default, 100 Client Certificates per Zone are included for free. For more certificates or <a href="/api-shield/">API Shield features</a>, contact your account team.</td>
<td align="left">Zero Trust Enterprise only feature.</td>
</tr>
<tr>
<td align="left"><a href="/ssl/concepts/#certificate-authority-ca">Certificate Authority (CA)</a></td>
<td align="left">Cloudflare-managed or customer-uploaded (BYO CA). There's a soft-limit of up to <a href="/ssl/client-certificates/byo-ca/#availability">five customer-uploaded CAs</a>.</td>
<td align="left">Customer-uploaded only (BYO CA). There's a soft-limit of up to <a href="/cloudflare-one/account-limits/#access">50 CAs</a>.</td>
</tr>
<tr>
<td align="left">Client Certificate Details</td>
<td align="left">Forwarded to the origin server via <a href="/ssl/client-certificates/forward-a-client-certificate/#cloudflare-api">Cloudflare API</a>, <a href="/ssl/client-certificates/forward-a-client-certificate/#cloudflare-workers">Cloudflare Workers</a>, and <a href="/ssl/client-certificates/forward-a-client-certificate/#managed-transforms">Managed Transforms</a>.</td>
<td align="left">Forwarded to the origin server via <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#cloudflare-api">Cloudflare API</a>, <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#cloudflare-workers">Cloudflare Workers</a>, and <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#managed-transforms">Managed Transforms</a>. Client Certificate headers and <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/">Cf-Access-Jwt-Assertion</a> JWT header can be forwarded to the origin server.</td>
</tr>
<tr>
<td align="left">Client Certificates Revocation</td>
<td align="left">Use the WAF <a href="/waf/custom-rules/">Custom Rules</a> to check for <a href="/ssl/client-certificates/revoke-client-certificate/"><em>cf.tls_client_auth.cert_revoked</em></a>, which only applies to Cloudflare-managed CA. <br /><br /> For BYO CAs, it would be the same approach as with Cloudflare Access.</td>
<td align="left">Generate a <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#create-a-crl">Certificate Revocation List (CRL)</a> and enforce the revocation in a Cloudflare Worker.</td>
</tr>
</tbody>
</table>
