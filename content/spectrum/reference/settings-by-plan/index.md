<p>Certain fields in Spectrum request and response bodies require an Enterprise plan. To upgrade your plan, contact your account team.</p>
<p>Spectrum properties requiring an Enterprise plan:</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>origin_dns</code></td>
<td>object</td>
<td>Method and parameters used to discover the origin server address via DNS. Valid record types are <code>A</code>, <code>AAAA</code>, <code>SRV</code> and empty (both <code>A</code> and <code>AAA</code>).<br />A request must contain either an <code>origin_dns</code> parameter or an <code>origin_direct</code> parameter. When both are specified the service returns an <code>HTTP 400 Bad Request</code>.</td>
<td><code>origin_dns: {type: A, name: mqtt.example.com, ttl: 1200}</code></td>
</tr>
<tr>
<td><code>origin_port</code></td>
<td>integer</td>
<td>The destination port at the origin.</td>
<td><code>22</code></td>
</tr>
<tr>
<td><code>proxy_protocol</code></td>
<td>string</td>
<td>Enables Proxy Protocol to the origin. Spectrum supports <code>v1</code>, <code>v2</code>, and <code>simple</code> proxy protocols. Refer to <a href="/spectrum/how-to/enable-proxy-protocol/">Proxy Protocol</a> for more details.</td>
<td><code>off</code></td>
</tr>
<tr>
<td><code>ip_firewall</code></td>
<td>boolean</td>
<td>Enables IP Access rules for this application.</td>
<td><code>true</code></td>
</tr>
<tr>
<td><code>tls</code></td>
<td>string</td>
<td>Type of TLS termination for the application. Options are <code>off</code> (default, also known as Passthrough), <code>flexible</code>, <code>full</code>, and <code>strict</code>. Refer to <a href="/spectrum/reference/configuration-options/">Configuration Options</a> for descriptions of each.</td>
<td><code>full</code></td>
</tr>
<tr>
<td><code>argo_smart_routing</code></td>
<td>boolean</td>
<td>Enables Argo Smart Routing for the application. Note that it is only available for TCP applications with traffic_type set to <code>direct</code>.</td>
<td><code>true</code></td>
</tr>
</tbody>
</table>
<p>Review the <a href="/api/resources/spectrum/subresources/apps/methods/list/">Spectrum API documentation</a> for example API requests.</p>
