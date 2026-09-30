---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/status-codes/custom-hostnames/
  description: HTTP status codes for custom hostname API endpoints.
  full_title: Status codes - Custom hostnames · Cloudflare for Platforms docs
  head_html: <title>Status codes - Custom hostnames · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="HTTP status codes for custom hostname API endpoints."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/status-codes/custom-hostnames/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/status-codes/custom-hostnames/index.md"><meta property="og:title" content="Status codes - Custom hostnames · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="HTTP status codes for custom hostname API endpoints."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/status-codes/custom-hostnames/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare for SaaS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/status-codes/custom-hostnames/#page","headline":"Status codes - Custom hostnames \u00b7 Cloudflare for Platforms docs","description":"HTTP status codes for custom hostname API endpoints.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/status-codes/custom-hostnames/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/cloudflare-for-saas/reference/status-codes/custom-hostnames/
  schema: 1
---
<hr />
<h2 id="success-codes">Success codes</h2>
<table>
<thead>
<tr>
<th>Endpoint</th>
<th>Method</th>
<th>Code</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/v4/zones/:zone_id/custom_hostnames</code></td>
<td>POST</td>
<td>201 Created</td>
</tr>
<tr>
<td><code>/v4/zones/:zone_id/custom_hostnames/:custom_hostname_id</code></td>
<td>GET</td>
<td>200 OK</td>
</tr>
<tr>
<td><code>/v4/zones/:zone_id/custom_hostnames</code></td>
<td>GET</td>
<td>200 OK</td>
</tr>
<tr>
<td><code>/v4/zones/:zone_id/custom_hostnames/:custom_hostname_id</code></td>
<td>DELETE</td>
<td>200 OK</td>
</tr>
<tr>
<td><code>/v4/zones/:zone_id/custom_hostnames/:custom_hostname_id</code></td>
<td>PATCH</td>
<td>202 Accepted</td>
</tr>
</tbody>
</table>
<hr />
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
<td>Unable to encode the Custom Metadata as JSON. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1402</td>
<td>Zone ID is required. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1403</td>
<td>The request has no Authorization header. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1407</td>
<td>Invalid custom hostname. Custom hostnames have to be smaller than 256 characters in length, cannot be IP addresses, cannot contain any special characters such as ``~`!@#$%^&amp;*()=+{}[]\</td>
</tr>
<tr>
<td>400</td>
<td>1408</td>
<td>Custom hostnames with non-ASCII characters are not supported. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1409</td>
<td>Reserved top domain custom hostnames, such as 'test', 'example', 'invalid' or 'localhost', is not supported. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1410</td>
<td>Unable to parse custom hostname - <code>:reason</code>. Check your input and try again. <br/> <strong>Reasons:</strong> <br/> publicsuffix: cannot derive eTLD+1 for domain <code>:domain</code> <br/> publicsuffix: invalid public suffix <code>:suffix</code> for domain <code>:domain</code></td>
</tr>
<tr>
<td>400</td>
<td>1411</td>
<td>Custom hostnames ending in example.com, example.net, or example.org are prohibited. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1412</td>
<td>Custom metadata for wildcard custom hostnames is not supported. Check your input and try again. <br/> <strong>Note:</strong> <br/> This message is only presented to customers who have opted out of wildcard support for custom metadata.</td>
</tr>
<tr>
<td>400</td>
<td>1415</td>
<td>Invalid custom origin hostname. Custom origin hostnames have to be smaller than 256 characters in length, cannot be IP addresses, cannot contain any special characters such as <del>``</del>`!@#$%^&amp;*()=+{}[]\</td>
</tr>
<tr>
<td>400</td>
<td>1416</td>
<td>Custom origin hostnames with non-ASCII characters are not supported. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1417</td>
<td>Reserved top domain custom origin hostnames, such as 'test', 'example', 'invalid' or 'localhost', is not supported. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1418</td>
<td>Unable to parse custom origin hostname - <code>:reason</code>. Check your input and try again. <br/> <strong>Reasons:</strong> <br/> publicsuffix: cannot derive eTLD+1 for domain <code>:domain</code><br/> publicsuffix: invalid public suffix<code>:suffix</code>for domain<code>:domain</code></td>
</tr>
<tr>
<td>400</td>
<td>1419</td>
<td>Custom origin hostnames ending in example.com, example.net, or example.org are prohibited. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1420</td>
<td>Wildcard custom origin hostnames are not supported. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1421</td>
<td>The custom origin hostname you specified does not exist on Cloudflare as a DNS record (A, AAAA or CNAME) in your zone:<code>:zone\_tag</code>. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1422</td>
<td>Invalid <code>http2</code>setting. Only 'on' or 'off' is accepted. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1423</td>
<td>Invalid<code>tls\_1\_2\_only</code>setting. Only 'on' or 'off' is accepted. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1424</td>
<td>Invalid<code>tls\_1\_3</code>setting. Only 'on' or 'off' is accepted. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1425</td>
<td>Invalid<code>min\_tls\_version</code>setting. Only '1.0','1.1','1.2' or '1.3' is accepted. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1426</td>
<td>The certificate that you uploaded cannot be parsed. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1427</td>
<td>The certificate that you uploaded is empty. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1428</td>
<td>The private key you uploaded cannot be parsed. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1429</td>
<td>The private key you uploaded does not match the certificate. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1430</td>
<td>The custom CSR ID is invalid. Check your input and try again.</td>
</tr>
<tr>
<td>404</td>
<td>1431</td>
<td>The custom CSR was not found.</td>
</tr>
<tr>
<td>400</td>
<td>1432</td>
<td>The validation method is not supported. Only<code>http</code>, <code>email</code>, or <code>txt</code> are accepted. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1433</td>
<td>The validation type is not supported. Only 'dv' is accepted. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1434</td>
<td>The SSL attribute is invalid. Refer to the API documentation, check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1435</td>
<td>The custom hostname ID is invalid. Check your input and try again.</td>
</tr>
<tr>
<td>404</td>
<td>1436</td>
<td>The custom hostname was not found.</td>
</tr>
<tr>
<td>400</td>
<td>1437</td>
<td>Invalid hostname.contain query parameter. The hostname.contain query parameter has to be smaller than 256 characters in length, cannot be IP addresses, cannot contain any special characters such as ``~`!@#$%^&amp;*()=+{}[]\</td>
</tr>
<tr>
<td>400</td>
<td>1438</td>
<td>Cannot specify other filter parameters in addition to <code>id</code>. Only one must be specified. Check your input and try again.</td>
</tr>
<tr>
<td>409</td>
<td>1439</td>
<td>Modifying the custom hostname is not supported. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1440</td>
<td>Both validation type and validation method are required. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1441</td>
<td>The certificate that you uploaded is having trouble bundling against the public trust store. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1442</td>
<td>Invalid <code>ciphers</code> setting. Refer to the documentation for the list of accepted cipher suites. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1443</td>
<td>Cipher suite selection is not supported for a minimum TLS version of 1.3. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1444</td>
<td>The certificate chain that you uploaded has multiple leaf certificates. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1445</td>
<td>The certificate chain that you uploaded has no leaf certificates. Check your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1446</td>
<td>The certificate that you uploaded does not include the custom hostname - <code>:custom_hostname</code>. Review your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1447</td>
<td>The certificate that you uploaded does not use a supported signature algorithm. Only SHA-256/ECDSA, SHA-256/RSA, and SHA-1/RSA signature algorithms are supported. Review your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1448</td>
<td>Custom hostnames with wildcards are not supported for certificates managed by Cloudflare. Review your input and try again.</td>
</tr>
<tr>
<td>400</td>
<td>1449</td>
<td>The request input <code>bundle_method</code> must be one of: ubiquitous, optimal, force.</td>
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
<td>1404</td>
<td>No quota has been allocated for this zone. If you are already a paid Cloudflare for SaaS customer, contact your account team for additional provisioning. If you are not yet enrolled, <a href="https://www.cloudflare.com/plans/enterprise/contact/">fill out this contact form</a> and our sales team will reach out to you.</td>
</tr>
<tr>
<td>403</td>
<td>1405</td>
<td>Quota exceeded. If you are already a paid Cloudflare for SaaS customer, contact your account team for additional provisioning. If you are not yet enrolled, <a href="https://www.cloudflare.com/plans/enterprise/contact/">fill out this contact form</a> and our sales team will reach out to you.</td>
</tr>
<tr>
<td>403</td>
<td>1413</td>
<td>No <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/">custom metadata</a> access has been allocated for this zone. If you are already a paid  customer, contact your account team for additional provisioning. If you are not yet enrolled, <a href="https://www.cloudflare.com/plans/enterprise/contact/">fill out this contact form</a> and our sales team will reach out to you.</td>
</tr>
<tr>
<td>403</td>
<td>1414</td>
<td>Access to setting a custom origin server has not been granted for this zone. If you are already a paid Cloudflare for SaaS customer, contact your account team for additional provisioning. If you are not yet enrolled, <a href="https://www.cloudflare.com/plans/enterprise/contact/">fill out this contact form</a> and our sales team will reach out to you.</td>
</tr>
<tr>
<td>409</td>
<td>1406</td>
<td>Duplicate custom hostname found.</td>
</tr>
<tr>
<td>500</td>
<td>1500</td>
<td>Internal Server Error</td>
</tr>
</tbody>
</table>
