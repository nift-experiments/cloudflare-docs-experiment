<p>Spectrum logs the entire lifecycle of every client that connects through it. These event logs are available through Logpush as a separate category (dataset type <code>spectrum_events</code>); they are not part of HTTP log events.</p>
<p>For each connection, Spectrum logs a connect event and either a disconnect or error event. Details on status codes can be found below.</p>
<h2 id="configure-logpush">Configure Logpush</h2>
<p>Spectrum <a href="/logs/logpush/logpush-job/datasets/">log events</a> can be configured through the dashboard or API, depending on your preferred <a href="/logs/logpush/logpush-job/enable-destinations/">destination</a>.</p>
<h2 id="status-codes">Status Codes</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="spectrum-status-codes-are-not-http-status-codes">Spectrum status codes are not HTTP status codes</h3>
@markup("md", "content/.markup/bodies/13864.md")
</aside>
<table>
<thead>
<tr>
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>Connection was opened successfully.</td>
</tr>
<tr>
<td>200</td>
<td>Normal connection closure.</td>
</tr>
<tr>
<td>400</td>
<td>The TLS client hello sent during the client/edge TLS handshake contained an invalid SNI.</td>
</tr>
<tr>
<td>403</td>
<td>Connection closed because the client IP matched a firewall rule with deny action.</td>
</tr>
<tr>
<td>443</td>
<td>The client TLS handshake failed.</td>
</tr>
<tr>
<td>444</td>
<td>The origin closed the connection by sending a reset (RST) packet. Not all data may have been sent.</td>
</tr>
<tr>
<td>445</td>
<td>A timeout event (ETIMEDOUT) occurred on an established connection to origin.</td>
</tr>
<tr>
<td>446</td>
<td>Origin keepalive expired (EHOSTUNREACH).</td>
</tr>
<tr>
<td>447</td>
<td>Error while reading from or writing to an established origin connection (ECONNREFUSED).</td>
</tr>
<tr>
<td>448</td>
<td>Origin connection closed due to a broken pipe (EPIPE).</td>
</tr>
<tr>
<td>490</td>
<td>Client TLS error on established connection.</td>
</tr>
<tr>
<td>495</td>
<td>Client connection received an error (ECONNREFUSED).</td>
</tr>
<tr>
<td>496</td>
<td>Client host is unreachable (EHOSTUNREACH).</td>
</tr>
<tr>
<td>497</td>
<td>A timeout event (ETIMEDOUT) occurred on an established connection to client.</td>
</tr>
<tr>
<td>498</td>
<td>Established client connection closed due to broken pipe (EPIPE).</td>
</tr>
<tr>
<td>499</td>
<td>The client closed the connection by sending a reset (RST) packet. Not all data may have been sent.</td>
</tr>
<tr>
<td>500</td>
<td>Internal Cloudflare error.</td>
</tr>
<tr>
<td>503</td>
<td>Error related to performing the TLS handshake with keyless SSL.</td>
</tr>
<tr>
<td>520</td>
<td>Unknown origin connection error.</td>
</tr>
<tr>
<td>521</td>
<td>Origin refused to open the connection (ECONNREFUSED).</td>
</tr>
<tr>
<td>522</td>
<td>Opening a connection to origin failed: ETIMEDOUT</td>
</tr>
<tr>
<td>523</td>
<td>Opening a connection to origin failed: ENETUNREACH</td>
</tr>
<tr>
<td>524</td>
<td>Opening a connection to origin failed due to an internal system error.</td>
</tr>
<tr>
<td>530</td>
<td>Internal error while resolving origin to an IP.</td>
</tr>
<tr>
<td>531</td>
<td>Could not resolve origin to an IP.</td>
</tr>
<tr>
<td>532</td>
<td>The origin connection was not opened because the origin IP is blocked.</td>
</tr>
<tr>
<td>533</td>
<td>Internal error while resolving origin to an IP.</td>
</tr>
<tr>
<td>540</td>
<td>The client/edge TLS handshake failed due to an invalid configuration.</td>
</tr>
<tr>
<td>999</td>
<td>Unknown connection error.</td>
</tr>
</tbody>
</table>
