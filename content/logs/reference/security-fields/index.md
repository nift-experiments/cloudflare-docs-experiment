<p>The Security fields contain rules to block requests that contain specific types of content.</p>
<h2 id="securityactions">SecurityActions</h2>
<table>
<thead>
<tr>
<th>Value</th>
<th>Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>unknown</code></td>
<td>Unknown</td>
<td>Take no other action.</td>
</tr>
<tr>
<td><code>allow</code></td>
<td>Allow</td>
<td>Bypass all subsequent rules.</td>
</tr>
<tr>
<td><code>block</code></td>
<td>Drop</td>
<td>Block with an HTTP status code of 403, 429, or any other <a href="/support/troubleshooting/http-status-codes/4xx-client-error/">4XX</a> status code.</td>
</tr>
<tr>
<td><code>challenge</code></td>
<td>Challenge Drop</td>
<td>Issue an interactive challenge.</td>
</tr>
<tr>
<td><code>jschallenge</code></td>
<td>Challenge Drop</td>
<td>Issue a non-interactive challenge.</td>
</tr>
<tr>
<td><code>log</code></td>
<td>Log</td>
<td>Take no action other than logging the event.</td>
</tr>
<tr>
<td><code>connectionClose</code></td>
<td>Close</td>
<td>Close connection.</td>
</tr>
<tr>
<td><code>challengeSolved</code></td>
<td>Allow</td>
<td>Allow once interactive challenge solved.</td>
</tr>
<tr>
<td><code>challengeBypassed</code></td>
<td>Allow</td>
<td>Interactive challenge is not issued again because the visitor had previously passed an interactive challenge and a valid <code>cf_clearance</code> cookie is present.</td>
</tr>
<tr>
<td><code>jschallengeSolved</code></td>
<td>Allow</td>
<td>Allow once non-interactive challenge solved.</td>
</tr>
<tr>
<td><code>jschallengeBypassed</code></td>
<td>Allow</td>
<td>Non-interactive challenge not issued because the visitor had previously passed a non-interactive or interactive challenge.</td>
</tr>
<tr>
<td><code>bypass</code></td>
<td>Allow</td>
<td>Bypass all subsequent firewall rules.</td>
</tr>
<tr>
<td><code>managedChallenge</code></td>
<td>Challenge Drop</td>
<td>Issue managed challenge.</td>
</tr>
<tr>
<td><code>managedChallengeNonInteractiveSolved</code></td>
<td>Allow</td>
<td>Allow once the managed challenge is solved via non-interactive interstitial page.</td>
</tr>
<tr>
<td><code>managedChallengeInteractiveSolved</code></td>
<td>Allow</td>
<td>Allow once the managed challenged is solved via interactive interstitial page.</td>
</tr>
<tr>
<td><code>managedChallengeBypassed</code></td>
<td>Allow</td>
<td>Challenge was not presented because visitor had clearance from previous challenge.</td>
</tr>
</tbody>
</table>
<h2 id="securitysources">SecuritySources</h2>
<table>
<thead>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>unknown</code></td>
<td>Used if an event is received from a new source but the logging system has not been updated.</td>
</tr>
<tr>
<td><code>asn</code></td>
<td>Allow or block based on autonomous system number.</td>
</tr>
<tr>
<td><code>country</code></td>
<td>Allow or block based on country.</td>
</tr>
<tr>
<td><code>ip</code></td>
<td>Allow or block based on IP address.</td>
</tr>
<tr>
<td><code>ipRange</code></td>
<td>Allow or block based on range of IP addresses.</td>
</tr>
<tr>
<td><code>securityLevel</code></td>
<td>Allow or block based on requester's security level.</td>
</tr>
<tr>
<td><code>zoneLockdown</code></td>
<td>Restrict all access to a specific zone.</td>
</tr>
<tr>
<td><code>waf</code></td>
<td>Allow or block based on the WAF product settings. This is the WAF/managed rules system that is being phased out.</td>
</tr>
<tr>
<td><code>firewallRules</code></td>
<td>Allow or block based on a zone's firewall rules configuration (deprecated).</td>
</tr>
<tr>
<td><code>uaBlock</code></td>
<td>Allow or block based on the Cloudflare User Agent Blocking product settings.</td>
</tr>
<tr>
<td><code>rateLimit</code></td>
<td>Allow or block based on a rate limiting rule, whether set by you or by Cloudflare.</td>
</tr>
<tr>
<td><code>bic</code></td>
<td>Allow or block based on the Browser Integrity Check product settings.</td>
</tr>
<tr>
<td><code>hot</code></td>
<td>Allow or block based on the Hotlink Protection product settings.</td>
</tr>
<tr>
<td><code>l7ddos</code></td>
<td>Allow or block based on the L7 DDoS product settings.</td>
</tr>
<tr>
<td><code>validation</code></td>
<td>Allow or block based on a request that is invalid (cannot be customized.)</td>
</tr>
<tr>
<td><code>botFight</code></td>
<td>Allow or block based on the Bot Fight Mode (classic) product settings.</td>
</tr>
<tr>
<td><code>botManagement</code></td>
<td>Allow or block based on the Bot Management product settings.</td>
</tr>
<tr>
<td><code>dlp</code></td>
<td>Allow or block based on the Data Loss Prevention product settings.</td>
</tr>
<tr>
<td><code>firewallManaged</code></td>
<td>Allow or block based on WAF Managed Rules' settings.</td>
</tr>
<tr>
<td><code>firewallCustom</code></td>
<td>Allow or block based on a rule configured in WAF custom rules.</td>
</tr>
</tbody>
</table>
