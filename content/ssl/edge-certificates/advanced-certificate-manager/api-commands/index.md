<p>Use the following API commands to manage advanced certificates. If you are using our API for the first time, review our <a href="/fundamentals/api/">API documentation</a>.</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Method</th>
<th>Endpoint</th>
<th>Additional notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/api/resources/ssl/subresources/certificate_packs/methods/create/">Order advanced certificate</a></td>
<td><code>POST</code></td>
<td><code>zones/&lt;&lt;ZONE_ID&gt;&gt;/ssl/certificate_packs/order</code></td>
<td></td>
</tr>
<tr>
<td><a href="/api/resources/ssl/subresources/certificate_packs/methods/edit/">Restart certificate validation</a></td>
<td><code>PATCH</code></td>
<td><code>zones/&lt;&lt;ZONE_ID&gt;&gt;/ssl/certificate_packs/&lt;&lt;ID&gt;&gt;</code></td>
<td>For a Certificate Pack in a <code>validation_timed_out</code> status.</td>
</tr>
<tr>
<td><a href="/api/resources/ssl/subresources/certificate_packs/methods/delete/">Delete certificate pack</a></td>
<td><code>DELETE</code></td>
<td><code>zones/&lt;&lt;ZONE_ID&gt;&gt;/ssl/certificate_packs/&lt;&lt;ID&gt;&gt;</code></td>
<td></td>
</tr>
<tr>
<td><a href="/api/resources/ssl/subresources/certificate_packs/methods/list/">List certificate packs in a zone</a></td>
<td><code>GET</code></td>
<td><code>zones/&lt;&lt;ZONE_ID&gt;&gt;/ssl/certificate_packs?status=all</code></td>
<td>This API call returns all certificate packs for a domain (Universal, Custom, and Advanced).</td>
</tr>
<tr>
<td>List Cipher Suite settings: <a href="/api/resources/zones/subresources/settings/methods/get/">Get zone setting</a> with <code>ciphers</code> as the setting name in the URI path</td>
<td><code>GET</code></td>
<td><code>zones/&lt;&lt;ZONE_ID&gt;&gt;/settings/ciphers</code></td>
<td></td>
</tr>
<tr>
<td>Change Cipher Suite settings: <a href="/api/resources/zones/subresources/settings/methods/edit/">Edit zone setting</a> with <code>ciphers</code> as the setting name in the URI path</td>
<td><code>PATCH</code></td>
<td><code>zones/&lt;&lt;ZONE_ID&gt;&gt;/settings/ciphers</code></td>
<td>To restore default settings, send a blank array in the <code>value</code> parameter.</td>
</tr>
</tbody>
</table>
