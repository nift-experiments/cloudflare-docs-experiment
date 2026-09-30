<p>Security Center scans your Cloudflare account configuration and identifies potential security risks, misconfigurations, and vulnerabilities across your domains. This guide covers the initial setup.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A Cloudflare account.</li>
<li>At least one <a href="/fundamentals/concepts/accounts-and-zones/#zones">zone</a> (domain or subdomain) added to your Cloudflare account.</li>
</ul>
<h2 id="turn-security-insights-on-or-off">Turn Security Insights on or off</h2>
<p>Security Insights scans are enabled by default. Security Insights will scan your Cloudflare environment and provide you with a list of detected <a href="/security/security-insights/">insights</a>. Refer to <a href="/security/security-insights/how-it-works/">How it works</a> to learn more about how Security Insights perform a scan.</p>
<p>The initial scan time depends on the number of IT assets in all the domains of your Cloudflare account. When the scan is complete, the status of the page will change from <strong>Scan in Progress</strong> to <strong>Last scan performed on: <code>&lt;DATE_TIME&gt;</code></strong>.</p>
<p>You can decide to stop a scan, and restart a scan later.</p>
<p>To disable scans:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security Insights</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Disable Security Center scans</strong>, select <strong>Disable scans</strong>.</li>
</ol>
<p>To restart a scan:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security Insights</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Scan now</strong>.</li>
</ol>
<h3 id="start-a-new-scan">Start a new scan</h3>
<p>To manually start a scan:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security insights</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Scan now</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/373.md")
</aside>
<h3 id="scan-frequency">Scan frequency</h3>
<p>Cloudflare performs scans automatically for all accounts and zones by default. On-demand scans are available on all plans:</p>
<table>
<thead>
<tr>
<th>Plan</th>
<th>Scan Frequency</th>
<th>On-Demand</th>
</tr>
</thead>
<tbody>
<tr>
<td>Free</td>
<td>Every 7 days</td>
<td>Yes</td>
</tr>
<tr>
<td>Pro and Business</td>
<td>Every 3 days</td>
<td>Yes</td>
</tr>
<tr>
<td>Enterprise</td>
<td>Daily</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<p>For more details, refer to <a href="/security/security-insights/how-it-works/#scan-frequency">How it works</a>.</p>
