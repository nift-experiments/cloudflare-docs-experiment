<p>DEX rules allow you to create and manage testing policies for targeted user groups within your <a href="/cloudflare-one/insights/dex/tests/">fleet</a> (all devices with the Cloudflare One Client installed and connected to your Zero Trust organization). After creating a rule, you can use it to define the scope of a <a href="/cloudflare-one/insights/dex/tests/">test</a> to specific groups such as departments (like finance or sales), devices, and/or users. You can apply and reuse rules on your desired tests.</p>
<p>Use DEX rules to scope a test to a specific group within your fleet for more precise problem detection and resolution.</p>
<h2 id="create-a-rule">Create a rule</h2>
<p>To create a rule:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Insights</strong> &gt; <strong>Digital experience</strong>.</li>
<li>Select the <strong>Rules</strong> tab.</li>
<li>Select <strong>Add a rule</strong>.</li>
<li>Give your rule a name and build your desired expressions.</li>
<li>Select <strong>Create rule</strong> to finalize your rule.</li>
</ol>
<h3 id="selectors">Selectors</h3>
<p>Selectors are required categories in a DEX rule expression that define a group within a fleet. The selector(s) you have defined in a rule will determine which group a test will impact.</p>
<p>Review the available selectors and their scope in the following list.</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>User email</strong></td>
<td>For specifying <a href="/cloudflare-one/traffic-policies/identity-selectors/#user-email">user emails</a>.</td>
</tr>
<tr>
<td><strong>User group emails</strong></td>
<td>For specifying <a href="/cloudflare-one/traffic-policies/identity-selectors/#user-group-email">group emails</a>.</td>
</tr>
<tr>
<td><strong>User group IDs</strong></td>
<td>For specifying <a href="/cloudflare-one/traffic-policies/identity-selectors/#user-group-ids">group IDs</a>.</td>
</tr>
<tr>
<td><strong>User group names</strong></td>
<td>For specifying a <a href="/cloudflare-one/traffic-policies/identity-selectors/#user-group-names">group name</a>.</td>
</tr>
<tr>
<td><strong>Operating systems</strong></td>
<td>For specifying operating systems.</td>
</tr>
<tr>
<td><strong>Operating system version</strong></td>
<td>For specifying an operating system version (use Operator <code>in</code>) or versions (use Operator <code>is</code>).</td>
</tr>
<tr>
<td><strong>Managed network</strong></td>
<td>For specifying users accessing the network from the office (managed network) compared to those accessing remotely.</td>
</tr>
<tr>
<td><strong>SAML attributes</strong></td>
<td>For specifying a value from the <a href="/cloudflare-one/traffic-policies/identity-selectors/#saml-attributes">SAML Attribute Assertion</a>.</td>
</tr>
<tr>
<td><strong>Colos</strong></td>
<td>For specifying a Cloudflare data center (colocation) that users are connected to.</td>
</tr>
</tbody>
</table>
<h2 id="add-a-rule-to-a-test">Add a rule to a test</h2>
<p>After you have created a rule, you can add it to a test. If you do not add a rule to a test, the test will run on your entire device fleet.</p>
<p>To add a rule to a test:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Insights</strong> &gt; <strong>Digital experience</strong>.</li>
<li>Select the <strong>Tests</strong> tab.</li>
<li>Choose an existing test and select <strong>Edit</strong>, or select <strong>Add a test</strong> to make a new test.</li>
<li>Under <strong>Select DEX rules</strong>, select the rule you would like to apply.</li>
<li>Select <strong>Save test</strong> for an existing rule or <strong>Add rule</strong> for the new test.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4968.md")
</aside>
<p>To view which tests a rule is being applied to:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Insights</strong> &gt; <strong>Digital experience</strong>.</li>
<li>Select the <strong>Rules</strong> tab.</li>
<li>Choose a rule and select <strong>Edit</strong>.</li>
<li>Select the <strong>DEX tests</strong> tab and review the list of tests that include your selected rule.</li>
</ol>
<h2 id="create-a-test-using-a-rule">Create a test using a rule</h2>
<p>You can create a new test from the <a href="/cloudflare-one/insights/dex/rules/#add-a-rule-to-a-test">DEX test dashboard as described above</a> or directly from the DEX rules dashboard.</p>
<p>To create a new test using a rule from DEX rules:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Insights</strong> &gt; <strong>Digital experience</strong>.</li>
<li>Select the <strong>Rules</strong> tab.</li>
<li>Select a rule and select <strong>Edit</strong>.</li>
<li>Select the <strong>DEX tests</strong> tab.</li>
<li>You will be able to review all the tests that currently include this rule. To create a new test, select <strong>Create a test using this rule</strong>.</li>
<li>Enter all required information, making sure that the box next to your rule name is checked.</li>
<li>Select <strong>Add test</strong>.</li>
</ol>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/insights/dex/tests/http/">DEX HTTP test</a> - Assess the accessibility of a web application.</li>
<li><a href="/cloudflare-one/insights/dex/tests/traceroute/">DEX Traceroute test</a> - Measure the network path of an IP packet from an end-user device to a server.</li>
</ul>
