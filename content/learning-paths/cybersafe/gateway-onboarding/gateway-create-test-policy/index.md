<p>To ensure a smooth deployment, we recommend testing a simple policy before deploying DNS filtering to your organization.</p>
<h2 id="test-a-policy-in-the-browser">Test a policy in the browser</h2>
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>Create a policy to block all security categories:</li>
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
<ol start="3">
<li>In the browser, go to <code>malware.testcategory.com</code>. You should see a generic Gateway block page.</li>
<li>In <strong>Logs</strong> &gt; <strong>Gateway</strong> &gt; <strong>DNS</strong>, verify that you see the blocked domain.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9713.md")
</aside>
<p>You have now validated DNS filtering!</p>
