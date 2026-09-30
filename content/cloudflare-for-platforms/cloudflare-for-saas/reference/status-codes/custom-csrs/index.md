<h2 id="success-codes">Success codes</h2>
<table>
<thead>
<tr>
<th>Endpoint</th>
<th>Method</th>
<th>HTTP Status Code</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/api/v4/zones/:zone_id/custom_csrs</code></td>
<td>POST</td>
<td>201 Created</td>
</tr>
<tr>
<td><code>/api/v4/zones/:zone_id/custom_csrs</code></td>
<td>GET</td>
<td>200 OK</td>
</tr>
<tr>
<td><code>/api/v4/zones/:zone_id/custom_csrs/:custom_csr_id</code></td>
<td>GET</td>
<td>200 OK</td>
</tr>
<tr>
<td><code>/api/v4/zones/:zone_id/custom_csrs/:custom_csr_id</code></td>
<td>DELETE</td>
<td>200 OK</td>
</tr>
</tbody>
</table>
<h2 id="error-codes">Error codes</h2>
<table>
<thead>
<tr>
<th>HTTP Status Code</th>
<th>API Error Code</th>
<th>Error Message</th>
</tr>
</thead>
<tbody>
<tr>
<td>400</td>
<td>1400</td>
<td>Unable to decode the JSON request body. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1401</td>
<td>Zone ID is required. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1402</td>
<td>The request has no Authorization header. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1405</td>
<td>Country field is required. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1406</td>
<td>State field is required. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1407</td>
<td>Locality field is required. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1408</td>
<td>Organization field is required. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1409</td>
<td>Common Name field is required. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1410</td>
<td>The specified Common Name is too long. Maximum allowed length is %d characters. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1411</td>
<td>At least one subject alternative name (SAN) is required. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1412</td>
<td>Invalid subject alternative name(s) (SAN). SANs have to be smaller than 256 characters in length, cannot be IP addresses, cannot contain any special characters such as ~`!@#$%^&amp;*()=+{}[]</td>
</tr>
<tr>
<td>400</td>
<td>1413</td>
<td>Subject Alternative Names (SANs) with non-ASCII characters are not supported. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1414</td>
<td>Reserved top domain subject alternative names (SAN), such as 'test', 'example', 'invalid' or 'localhost', is not supported. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1415</td>
<td>Unable to parse subject alternative name(s) (SAN) - :reason. Check your input and try again. Reasons: publicsuffix: cannot derive eTLD+1 for domain %q; publicsuffix: invalid public suffix %q for domain %q;</td>
</tr>
<tr>
<td>400</td>
<td>1416</td>
<td>Subject Alternative Names (SANs) ending in example.com, example.net, or example.org are prohibited. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1417</td>
<td>Invalid key type. Only 'rsa2048' or 'p256v1' is accepted. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1418</td>
<td>The custom CSR ID is invalid. Check your input and try again.</td>
</tr>
<tr>
<td>401</td>
<td>1000</td>
<td>Unable to extract bearer token</td>
</tr>
<tr>
<td>401</td>
<td>1001</td>
<td>Unable to parse JWT token</td>
</tr>
<tr>
<td>401</td>
<td>1002</td>
<td>Bad JWT header</td>
</tr>
<tr>
<td>401</td>
<td>1003</td>
<td>Failed to verify JWT token</td>
</tr>
<tr>
<td>401</td>
<td>1004</td>
<td>Failed to get claims from JWT token</td>
</tr>
<tr>
<td>401</td>
<td>1005</td>
<td>JWT token does not have required claims</td>
</tr>
<tr>
<td>403</td>
<td>1403</td>
<td>No quota has been allocated for this zone. If you are already a paid Cloudflare for SaaS customer, contact your account team for additional provisioning. If you are not yet enrolled, <a href="https://www.cloudflare.com/plans/enterprise/contact/">fill out this contact form</a> and our sales team will contact you.</td>
</tr>
<tr>
<td>403</td>
<td>1404</td>
<td>Access to generating CSRs has not been granted for this zone. If you are already a paid Cloudflare for SaaS customer, contact your account team for additional provisioning. If you are not yet enrolled, <a href="https://www.cloudflare.com/plans/enterprise/contact/">fill out this contact form</a> and our sales team will contact you.</td>
</tr>
<tr>
<td>404</td>
<td>1419</td>
<td>The custom CSR was not found.</td>
</tr>
<tr>
<td>409</td>
<td>1420</td>
<td>The custom CSR is associated with an active certificate pack. You will need to delete all associated active certificate packs before you can delete the custom CSR.</td>
</tr>
<tr>
<td>500</td>
<td>1500</td>
<td>Internal Server Error</td>
</tr>
</tbody>
</table>
