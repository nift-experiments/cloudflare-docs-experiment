<p>When Email security detects a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8574.md")
</div> email, the metadata of the detection can be sent directly to KnowBe4. For this tutorial, you will need a working KnowBe4 account with the SecurityCoach add-on. You will also need to create an organization key to use in Email security. This organization key will let you integrate KnowBe4 with Email security. Refer to [KnowBe4 documentation](https://support.knowbe4.com/hc/articles/13129840202643) for more information on this subject.
<p>After creating your organization key and authorizing Email security:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>Go to <strong>Email Configuration</strong> &gt; <strong>Domains &amp; Routing</strong> &gt; <strong>Alert Webhooks</strong>.</li>
<li>Select <strong>New Webhook</strong>.</li>
<li>In <strong>App Type</strong>, select <strong>SIEM</strong>.</li>
<li>Choose <em>KnowBe4</em> from the dropdown, and paste your organization key into the <strong>Auth Code</strong> section.</li>
<li>In <strong>Target</strong>, paste the URL that suits your organization. KnowBe4 has different URLs for different regions:</li>
</ol>
<table>
<thead>
<tr>
<th>KnowBe4 instance</th>
<th>URL</th>
</tr>
</thead>
<tbody>
<tr>
<td>United States</td>
<td><code>https://area1.vendor.training.knowbe4.com/v1</code></td>
</tr>
<tr>
<td>European Union</td>
<td><code>https://area1.vendor.eu.knowbe4.com/v1</code></td>
</tr>
<tr>
<td>Canada</td>
<td><code>https://area1.vendor.ca.knowbe4.com/v1</code></td>
</tr>
<tr>
<td>United Kingdom</td>
<td><code>https://area1.vendor.uk.knowbe4.com/v1</code></td>
</tr>
<tr>
<td>Germany</td>
<td><code>https://area1.vendor.da.knowbe4.com/v1</code></td>
</tr>
</tbody>
</table>
8. Select _Expanded_ from the drop-down menu for **Malicious Style**, **Suspicious Style**, and **Spoof Style**.
9. Select **Publish Webhook**.
