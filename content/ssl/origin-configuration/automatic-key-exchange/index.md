<p>Automatic key exchange allows Cloudflare to establish faster connections to origin servers by predicting which key agreements origins support. When establishing a TLS 1.3 connection to the origin, Cloudflare sends a key share for the predicted key agreement in the initial ClientHello, which can remove one network round trip by avoiding a <a href="https://www.rfc-editor.org/rfc/rfc8446.html#section-4.1.4">HelloRetryRequest</a>.</p>
<p>This feature is separate from your <a href="/ssl/origin-configuration/ssl-modes/">SSL/TLS encryption mode</a>. The encryption mode controls whether Cloudflare uses HTTPS and validates your origin certificate. Automatic key exchange controls the <a href="https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.8">key shares</a> sent when starting an HTTPS connection. The same preference is applied for all of a zone's origins.</p>
<h2 id="requirements-and-scope">Requirements and scope</h2>
<p>Automatic key exchange applies when the connection meets these requirements:</p>
<ul>
<li>Your zone uses <strong>Full</strong>, <strong>Full (strict)</strong>, or <strong>Strict (SSL-Only Origin Pull)</strong> mode.</li>
<li>Your origin negotiates TLS 1.3 with Cloudflare.</li>
<li>Your zone does not connect through Cloudflare Tunnel.</li>
</ul>
<p>Automatic key exchange is available on all plans. It only affects new TLS connections. Requests that reuse an existing connection do not perform another key exchange.</p>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> uses a separate post-quantum connection between <code>cloudflared</code> and Cloudflare.</p>
<p>The setting applies to all outbound connections for the zone, including <code>fetch()</code> requests from <a href="/workers/">Workers</a>. If the zone has multiple active origins, Cloudflare derives one preference from their traffic-weighted results.</p>
<h2 id="how-automatic-selection-works">How automatic selection works</h2>
<p>Cloudflare scans active origins approximately every 24 hours. The scan checks the TLS key agreements that each origin supports and prefers.</p>
<p>When an origin supports both classical and post-quantum key agreements, Cloudflare prefers a post-quantum key agreement.</p>
<p>Cloudflare then applies the selected preference in stages:</p>
<ol>
<li>Cloudflare sends the selected key share to 1% of traffic.</li>
<li>Cloudflare monitors connection failures and HelloRetryRequest rates.</li>
<li>A healthy change increases through 10%, 25%, 50%, 75%, and 100% of traffic.</li>
<li>An unhealthy change rolls back to the previous setting.</li>
</ol>
<p>For each connection, Cloudflare sends the preferred key share first. Cloudflare also advertises the other key agreements allowed by your compliance requirements. An origin can request another advertised key share with a HelloRetryRequest. This adds one round trip but does not break the connection.</p>
<p>After a successful rollout, Cloudflare keeps the preference until a later scan finds a better option. Cloudflare selects <code>X25519MLKEM768</code> when the origin supports it and compliance requirements allow it. Otherwise, Cloudflare selects a supported classical key agreement.</p>
<p>Cloudflare uses standardized <code>X25519MLKEM768</code> for automatic post-quantum selection.</p>
<h2 id="configuration-options">Configuration options</h2>
<p>To configure automatic key exchange in the dashboard:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/14001.md")
</div>
<p>The settings provide two separate controls. <strong>Automatic key exchange</strong> controls whether Cloudflare scans and reorders preferred key agreements. <strong>Compliance requirements</strong> control which key agreements Cloudflare may use for automatic selection on TLS 1.3 connections.</p>
<h3 id="automatic-key-exchange">Automatic key exchange</h3>
<p>Automatic key exchange is on for all existing zones and on by default for new zones.</p>
<p>The setting has these options:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>On</td>
<td>Cloudflare scans your origins and sends the zone's preferred key share.</td>
</tr>
<tr>
<td>Off</td>
<td>Cloudflare does not scan or reorder key shares. It uses the default order for your selected compliance requirements.</td>
</tr>
</tbody>
</table>
<p>Turning off automatic key exchange does not change your compliance requirements.</p>
<h3 id="compliance-requirements">Compliance requirements</h3>
<p>Compliance requirements apply only to TLS 1.3 connections. They filter the key agreements that Cloudflare can advertise or select. Automatic key exchange never selects an algorithm outside this allowed set.</p>
<p>The available selections are:</p>
<table>
<thead>
<tr>
<th>Selection</th>
<th>API value</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>No selection</td>
<td><code>[]</code></td>
<td>Allows supported classical and post-quantum key agreements.</td>
</tr>
<tr>
<td>Post-quantum hybrid</td>
<td><code>[&quot;pqh&quot;]</code></td>
<td>Allows only hybrid post-quantum key agreements.</td>
</tr>
<tr>
<td>Federal Information Processing Standards (FIPS)</td>
<td><code>[&quot;fips&quot;]</code></td>
<td>Allows only key agreements that meet FIPS requirements.</td>
</tr>
<tr>
<td>Post-quantum hybrid and FIPS</td>
<td><code>[&quot;pqh&quot;, &quot;fips&quot;]</code></td>
<td>Allows only key agreements that satisfy both requirements.</td>
</tr>
</tbody>
</table>
<p>Cloudflare rejects a combination if the selected requirements have no key agreement in common. Changing a compliance requirement stops any active rollout. A later scan selects from the new allowed set.</p>
<h2 id="origin-post-quantum-encryption-api">Origin Post-Quantum Encryption API</h2>
<p>The <a href="/api/resources/origin_post_quantum_encryption/methods/update/">Origin Post-Quantum Encryption API</a> remains available. Requests to this API are no-ops and do not change a zone's post-quantum key agreement behavior. Cloudflare plans to deprecate this API, but a deprecation date has not been established.</p>
<p>Use <strong>Automatic key exchange</strong> and <strong>Compliance requirements</strong> to configure post-quantum key agreement behavior.</p>
