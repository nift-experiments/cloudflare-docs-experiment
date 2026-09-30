<p>Use this guide to resolve common issues when analyzing <a href="https://www.cloudflare.com/products/cloudflare-logs/">Cloudflare Logs</a> through the <a href="/analytics/analytics-integrations/splunk/">Cloudflare App for Splunk</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="support-scope">Support scope</h3>
@markup("md", "content/.markup/bodies/3150.md")
</aside>
<h2 id="firewall-events-carry-incorrect-time-values">Firewall Events carry incorrect <code>_time</code> values</h2>
<p>Events under the <code>cloudflare:json</code> sourcetype for the Firewall Events dataset carry <code>_time</code> values that do not match the event's actual time, and <code>splunkd.log</code> shows entries similar to:</p>
<pre><code class="language-txt">WARN DateParserVerbose - Failed to parse timestamp.&#10;Defaulting to timestamp of previous event.&#10;</code></pre>
<p><strong>Cause:</strong> In older versions of the Cloudflare App for Splunk, the <code>cloudflare:json</code> sourcetype extracts <code>_time</code> from the <code>EdgeStartTimestamp</code> JSON key, which only exists in HTTP requests logs. Firewall Events use a different key (<code>Datetime</code>), so timestamp extraction fails and Splunk silently falls back to the timestamp of the most recently indexed event.</p>
<p><strong>Fix:</strong> Upgrade to the latest version of the <a href="https://splunkbase.splunk.com/app/4501/">Cloudflare App for Splunk</a>. The current release parses both <code>EdgeStartTimestamp</code> and <code>Datetime</code> under the <code>cloudflare:json</code> sourcetype.</p>
<p>If you cannot upgrade immediately, or if you maintain a customized <code>props.conf</code>, update the <code>cloudflare:json</code> stanza on your indexer or heavy forwarder to match both keys, then restart the Splunk service:</p>
<pre><code class="language-conf">[cloudflare:json]&#10;TRUNCATE = 100000&#10;TIME_PREFIX = &quot;(?:EdgeStartTimestamp|Datetime)&quot;\s*:\s*&quot;&#10;TIME_FORMAT = %Y-%m-%dT%H:%M:%SZ&#10;MAX_TIMESTAMP_LOOKAHEAD = 150&#10;</code></pre>
<p><strong>Verify:</strong> Newly indexed Firewall Events carry accurate <code>_time</code> values, and <code>DateParserVerbose</code> warnings no longer appear in <code>splunkd.log</code>. Events indexed before the fix retain their original <code>_time</code> values unless they are re-indexed.</p>
<h2 id="the-cloudflare-security-waf-dashboard-is-empty">The Cloudflare Security (WAF) dashboard is empty</h2>
<p>The <code>Cloudflare – Security (WAF)</code> dashboard in the Cloudflare App for Splunk loads without errors, but all panels are empty. Other dashboards (Overview, Performance, Reliability) populate normally, and running the WAF panels' underlying SPL directly in the search bar also returns zero results — even when WAF and security events are confirmed present in the target index.</p>
<p><strong>Cause:</strong> In older versions of the Cloudflare App for Splunk, the WAF dashboard SPL references Cloudflare log fields that were <a href="/logs/reference/change-notices/2023-02-01-security-fields-updates/#http-requests-dataset-changes">removed from the HTTP Requests dataset</a>:</p>
<table>
<thead>
<tr>
<th align="left">Deprecated field</th>
<th align="left">Current field</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>FirewallMatchesRuleIDs{}</code></td>
<td align="left"><code>SecurityRuleIDs</code></td>
</tr>
<tr>
<td align="left"><code>WAFRuleMessage</code></td>
<td align="left"><code>SecurityRuleDescription</code></td>
</tr>
</tbody>
</table>
<p>Splunk does not raise an error when a search references a field that is absent from all indexed events — it completes the search and returns zero results, leaving every dashboard panel empty.</p>
<p><strong>Fix:</strong> Upgrade to the latest version of the <a href="https://splunkbase.splunk.com/app/4501/">Cloudflare App for Splunk</a>. The current release references <code>SecurityRuleIDs</code> and <code>SecurityRuleDescription</code> throughout the WAF dashboard, saved searches, and macros.</p>
<p>If you maintain a customized fork of the app, replace all references to <code>FirewallMatchesRuleIDs{}</code> and <code>WAFRuleMessage</code> in your dashboard XML, saved searches, and macros with <code>SecurityRuleIDs</code> and <code>SecurityRuleDescription</code>, respectively.</p>
<p><strong>Verify:</strong> Reload the <code>Cloudflare – Security (WAF)</code> dashboard. Panels should populate with recent WAF and security events. A direct search such as <code>index=&lt;your-index&gt; sourcetype=cloudflare:json SecurityRuleIDs=*</code> should also return matching events.</p>
<h2 id="still-not-resolved">Still not resolved</h2>
<p>If your issue is not covered here:</p>
<ul>
<li>Consult the <a href="https://splunkbase.splunk.com/app/4501/">Cloudflare App for Splunk page</a> on Splunkbase for the latest version and release notes.</li>
<li>Review the <a href="/logs/reference/change-notices/">Cloudflare Logs change notices</a> for recent schema changes that may affect your searches or dashboards.</li>
<li><a href="/support/contacting-cloudflare-support/">Contact Cloudflare Support</a> for issues involving Cloudflare-side log delivery.</li>
<li>Contact your Splunk representative or your integration partner for issues within your Splunk environment.</li>
</ul>
