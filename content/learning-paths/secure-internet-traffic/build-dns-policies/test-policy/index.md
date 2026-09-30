<p>It is common for a misconfigured Gateway policy to accidentally block traffic to benign sites. To ensure a smooth deployment, we recommend testing a simple policy before deploying DNS filtering to your organization.</p>
<h2 id="test-a-policy-in-the-browser">Test a policy in the browser</h2>
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>Turn off all existing DNS policies.</li>
<li>Turn on any existing security policies or create a policy to block all security categories:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Security Categories</td>
<td>in</td>
<td><em>All security risks</em></td>
<td>Block</td>
</tr>
</tbody>
</table>
<ol start="4">
<li>Ensure that your browser is not configured to use an alternate DNS resolver. For example, Chrome has a <strong>Use secure DNS</strong> setting that will cause the browser to send requests to 1.1.1.1 and bypass your DNS policies.</li>
<li>In the browser, go to <code>malware.testcategory.com</code>. Your browser will display:
<ul>
<li>The Gateway block page, if your device is connected through the Cloudflare One Client in Traffic and DNS mode.</li>
<li>A generic error page, if your device is connected through another method, such as DNS only mode.</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10215.md")
</aside>
<ol start="6">
<li>In <strong>Logs</strong> &gt; <strong>Gateway</strong> &gt; <strong>DNS</strong>, verify that you see the blocked domain.</li>
<li>Slowly turn on or add other policies to your configuration.</li>
<li>When testing against frequently-visited sites, you may need to <a href="/cloudflare-one/traffic-policies/dns-policies/test-dns-filtering/#clear-dns-cache">clear the DNS cache</a> in your browser or OS. Otherwise, the DNS lookup will return the locally-cached IP address and bypass your DNS policies.</li>
</ol>
<p>You have now validated DNS filtering on a test device.</p>
