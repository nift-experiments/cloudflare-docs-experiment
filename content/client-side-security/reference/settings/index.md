<h2 id="reporting-endpoint">Reporting endpoint</h2>
<p>When enabled, client-side security's resource monitoring uses a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3972.md")
</div> [report-only HTTP header](/client-side-security/reference/csp-header/) to gather information about all the scripts running on your application.
<p>By default, reports are sent to a Cloudflare-owned endpoint:</p>
<pre><code class="language-txt">https://csp-reporting.cloudflare.com/cdn-cgi/script_monitor/report?&lt;QUERY_STRING&gt;&#10;</code></pre>
<p>Customers with Client-Side Security Advanced can change the reporting endpoint so that the CSP reports are sent to the same hostname:</p>
<pre><code class="language-txt">&lt;YOUR-HOSTNAME&gt;/cdn-cgi/script-monitor/report?&lt;QUERY_STRING&gt;&#10;</code></pre>
<h3 id="prerequisites-for-using-the-same-hostname-for-csp-reports">Prerequisites for using the same hostname for CSP reports</h3>
<p>Using the same hostname for CSP reporting may interfere with other Cloudflare products. Before selecting this option, ensure that your Cloudflare configuration complies with the following:</p>
<ul>
<li>No rate limiting rules match the <code>cdn-cgi/*</code> URL path</li>
<li>No custom rules match the <code>cdn-cgi/*</code> URL path</li>
</ul>
<h3 id="configure-the-reporting-endpoint">Configure the reporting endpoint</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3971.md")
</aside>
<p>To configure the CSP reporting endpoint:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3973.md")
</div>
<h2 id="connection-target-details">Connection target details</h2>
<p>When connection targets are reported to Cloudflare, their URIs can sometimes include sensitive data such as session ID.</p>
<p>By default, client-side security only checks the domain against malicious threat intelligence feeds. You can choose to let Cloudflare use the full URI when analyzing the connections made from your domain's pages. Any sensitive data present in the URI will be logged in clear text, and any user with access to the connection monitor dashboard will be able to view it.</p>
<h3 id="configure-the-connection-target-details-to-use">Configure the connection target details to use</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3974.md")
</div>
<h2 id="turn-off-client-side-resource-monitoring">Turn off client-side resource monitoring</h2>
<p>When you turn off client-side security's resource monitoring, you lose visibility on the scripts running on your zone, the outbound connections made from pages in your domain, and cookies detected in HTTP traffic.</p>
<p>To turn off client-side resource monitoring:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3975.md")
</div>
<p>Turning off client-side security's resource monitoring does not turn off <a href="/client-side-security/rules/">content security rules</a> (previously known as policies). To turn off content security rules:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>(Optional) Filter by <strong>Content security rules</strong>.</li>
<li>For each rule, select the three dots next to it &gt; <strong>Disable</strong>.</li>
</ol>
