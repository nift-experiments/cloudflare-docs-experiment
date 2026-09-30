<p>Cloudflare API credentials use a prefixed, scannable format that makes them identifiable by credential scanning tools. Each credential type has a distinct prefix followed by 40 characters and a checksum.</p>
<table>
<thead>
<tr>
<th>Credential type</th>
<th>Description</th>
<th>Format</th>
</tr>
</thead>
<tbody>
<tr>
<td>Global API Key</td>
<td>Global key tied to your user account (full access)</td>
<td><code>cfk_[40 characters][checksum]</code></td>
</tr>
<tr>
<td>User API Token</td>
<td>Scoped token you create for specific permissions</td>
<td><code>cfut_[40 characters][checksum]</code></td>
</tr>
<tr>
<td>Account API Token</td>
<td>Token owned by the account, not tied to a specific user</td>
<td><code>cfat_[40 characters][checksum]</code></td>
</tr>
</tbody>
</table>
<p>Existing tokens continue to work. Every new token you create or <a href="/fundamentals/api/how-to/roll-token/">roll</a> uses the scannable format automatically.</p>
<h2 id="leaked-token-detection">Leaked token detection</h2>
<p>The prefixed format and checksum allow credential scanning tools to detect leaked Cloudflare tokens with high confidence. Cloudflare partners with credential scanning providers to proactively find your leaked tokens and revoke them before they can be used maliciously.</p>
<h3 id="github-secret-scanning">GitHub Secret Scanning</h3>
<p>Cloudflare participates in <a href="https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning">GitHub's Secret Scanning program</a>. GitHub scans every commit for Cloudflare API credentials in both public and private repositories.</p>
<ul>
<li><strong>Public repositories</strong> — When GitHub detects a leaked Cloudflare token, it verifies the token using the checksum and sends Cloudflare a webhook. Cloudflare automatically revokes the token and notifies you by email so you can generate a replacement.</li>
<li><strong>Private repositories</strong> — GitHub notifies you about any leaked Cloudflare tokens so you can rotate them.</li>
</ul>
<h2 id="pre-2026-formats">Pre-2026 formats</h2>
<p>Tokens created before the scannable format was introduced use unprefixed strings. These tokens continue to work. Cloudflare scans for and revokes leaked tokens in both the old and new formats.</p>
<table>
<thead>
<tr>
<th>Credential type</th>
<th>Old format</th>
</tr>
</thead>
<tbody>
<tr>
<td>Global API Key</td>
<td>37–45 character lowercase hex string</td>
</tr>
<tr>
<td>User API Token</td>
<td>40-character alphanumeric string</td>
</tr>
<tr>
<td>Account API Token</td>
<td>40-character alphanumeric string</td>
</tr>
</tbody>
</table>
