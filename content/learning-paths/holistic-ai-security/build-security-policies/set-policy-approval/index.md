<p>If you use specific AI tools within your organization, you may want to create policies to explicitly allow the usage of those tools while continuing to evaluate additional usage within your organization.</p>
<h2 id="create-a-gateway-policy-for-monitoring-and-evaluating-all-ai-tool-usage">Create a Gateway policy for monitoring and evaluating all AI tool usage</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>In the <strong>HTTP</strong> tab, select <strong>Add a policy</strong>.</li>
<li>Name the policy.</li>
<li>Under <strong>Traffic</strong>, build a logical expression that defines the traffic you want to allow for AI at your organization.</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Application</td>
<td>in</td>
<td><em>Artificial Intelligence</em></td>
</tr>
</tbody>
</table>
<ol start="5">
<li>For <strong>Action</strong>, select <strong>Allow</strong>.</li>
<li>Select <strong>Create policy</strong>.</li>
</ol>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/common-policies/#block-unauthorized-applications">Block unauthorized applications</a>.</p>
<h2 id="create-a-gateway-policy-to-redirect-users-towards-approved-ai-tools">Create a Gateway policy to redirect users towards approved AI tools</h2>
<p>Conversely, you can build policies that take specific actions based on an AI tool's approval status. For example, if you want to redirect users from unapproved applications to approved applications, you can create custom status pages to provide user coaching.</p>
<p>User coaching is a valuable tool for encouraging employees to change their behavior. By redirecting users to a status page, you can help them understand the risks of using unsanctioned AI tools and educate them on the dangers of inputting sensitive data.</p>
<p>Cloudflare Workers are an easy method to stand up custom user coaching pages. The customs status pages can be handled dynamically based on the information that Gateway sends about a blocked request. In the appendix of this document, you can find sample code for a Cloudflare Worker built for this purpose that you can test and adopt if desired.</p>
<h2 id="redirect-users-towards-approved-ai-tools">Redirect users towards approved AI tools</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>In the <strong>HTTP</strong> tab, select <strong>Add a policy</strong>.</li>
<li>Name the policy.</li>
<li>Under <strong>Traffic</strong>, build a logical expression that defines the traffic you want to allow for AI at your organization.</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Application</td>
<td>in</td>
<td><em>Artificial Intelligence</em></td>
</tr>
</tbody>
</table>
<ol start="5">
<li>For <strong>Action</strong>, select <strong>Block</strong>.</li>
<li>To <strong>Modify the Gateway block behavior</strong>, determine how you want to redirect your users.
<ul>
<li>Redirect users to a custom block page to coach the user:
<ol>
<li>Select <strong>Use account-level block setting</strong>.</li>
<li>Check <strong>Add an additional message to your custom block page when traffic matches</strong> this policy and enter your custom message.</li>
</ol>
</li>
<li>Redirect users to an approved AI tool automatically:
<ol>
<li>Select <strong>Override account setting with URL redirect</strong>.</li>
<li>Enter the URL to the approved application you want to redirect the user to use instead.</li>
</ol>
</li>
</ul>
</li>
<li>Select <strong>Create policy</strong>.</li>
</ol>
<p>For more information, refer to <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/#configure-policy-block-behavior">Configure policy block behavior</a>.</p>
<h2 id="capture-prompts-to-prevent-data-loss">Capture prompts to prevent data loss</h2>
<p>You can build policies that enable Prompt Capture for AI applications in specific, complex scenarios. This gives you the flexibility to apply advanced functionality to certain applications, tool types, or user groups, such as contractors or new employees, especially if they pose a higher risk for using unsanctioned applications due to lack of awareness or training.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>In the <strong>HTTP</strong> tab, select <strong>Add a policy</strong>.</li>
<li>Name the policy.</li>
<li>Under <strong>Traffic</strong>, build a logical expression that defines the traffic you want to allow for AI at your organization.</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Application</td>
<td>in</td>
<td><em>Artificial Intelligence</em></td>
</tr>
</tbody>
</table>
<ol start="5">
<li>Under <strong>Identity</strong>, build a logical express that defines the user identity you want to capture and log their prompts to review for data loss prevention.</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>API Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Application</td>
<td>in</td>
<td><code>any(identity.groups.name[*] in {\&quot;contractors\&quot; \&quot;cohort-224\&quot;})</code></td>
</tr>
</tbody>
</table>
<ol start="6">
<li>For <strong>Action</strong>, select <strong>Allow</strong>.</li>
<li>Select <strong>Create policy</strong>.</li>
</ol>
<h2 id="configure-gateway-to-use-chatgpt-workspace-header">Configure Gateway to use ChatGPT workspace header</h2>
<p>If your organization uses <a href="https://chatgpt.com/business/">ChatGPT Business</a>, you can configure a Gateway policy to enforce the use of your organization's workspace ID, ensuring all traffic to ChatGPT is correctly associated with your account. This will implement Gateway <a href="/cloudflare-one/traffic-policies/http-policies/tenant-control/">tenant control</a>, which lets you manage how users interact with specific applications.</p>
<p>To create this policy, you will add a custom HTTP header to your Gateway policy. This header, <code>Chatgpt-Allowed-Workspace-Id</code>, ensures that only requests with your organization's unique workspace ID are permitted.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>In the <strong>HTTP</strong> tab, select <strong>Add a policy</strong>.</li>
<li>Name the policy.</li>
<li>Under <strong>Traffic</strong>, build a logical expression that defines the traffic you want to allow.</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Application</td>
<td>in</td>
<td><em>ChatGPT</em></td>
</tr>
</tbody>
</table>
<ol start="5">
<li>In <strong>Action</strong>, choose <em>Allow</em>.</li>
<li>In <strong>Untrusted certificate action</strong>, choose <em>Block</em>.</li>
<li>Under <strong>Add headers to matched requests</strong>, select <strong>Add a header</strong>.</li>
<li>Add the following values to each field:
<ul>
<li><strong>Custom header name</strong>: <code>Chatgpt-Allowed-Workspace-Id</code></li>
<li><strong>Custom header value</strong>: Your organization's workspace ID</li>
</ul>
</li>
<li>Select <strong>Create policy</strong>.</li>
</ol>
<p>For more information, refer to the <a href="https://help.openai.com/articles/8798594-what-is-a-workspace-how-do-i-access-my-chatgpt-business-workspace">OpenAI documentation</a>.</p>
<h2 id="order-your-policies-for-specific-inspection-and-enforcement">Order your policies for specific inspection and enforcement</h2>
<p>In most scenarios, Gateway evaluates HTTP policies in <a href="/learning-paths/secure-internet-traffic/understand-policies/order-of-enforcement/">top-down order</a>.
Therefore, you can capture prompts in specific scenarios to gain visibility without disrupting your users' work, all while holistically protecting against sensitive data loss.</p>
<p>For example, if you want to prevent sensitive data being shared with AI but want to allow all users to use AI but capture the prompts for specific identity-defined user groups, you would need to order your policies in the following way.</p>
<ol>
<li>The policy that blocks sensitive data being shared would need to be ordered first in this policy group. This will allow it to be enforced before the next policy in the policy group.</li>
</ol>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td>Application</td>
<td>in</td>
<td><em>Artificial Intelligence</em></td>
<td></td>
</tr>
<tr>
<td>And</td>
<td>DLP Profile</td>
<td>in</td>
<td><em>my-sensitive-data</em></td>
<td>Block</td>
</tr>
</tbody>
</table>
<ol start="2">
<li>Next, create the policy that allows the use of AI and specifies the prompt capture for specific user groups.</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Application</td>
<td>in</td>
<td><em>Artificial Intelligence</em></td>
</tr>
</tbody>
</table>
<ol start="3">
<li>Under <strong>Traffic</strong>:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Application</td>
<td>in</td>
<td><em>Artificial Intelligence</em></td>
</tr>
</tbody>
</table>
<ol start="4">
<li>Under <strong>Identity</strong>:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>API Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>User Group Names</td>
<td>in</td>
<td><code>any(identity.groups.name[*] in {\&quot;contractors\&quot; \&quot;cohort-224\&quot;})</code></td>
<td>Allow</td>
</tr>
</tbody>
</table>
<p>By structuring your policies in this way, you ensure that any instance of sensitive data is blocked from AI applications, no matter which user group is involved. If Cloudflare does not detect sensitive data, it will allow the prompt while capturing it for the targeted user groups – in this case, users belonging to the <code>contractors</code> and <code>cohort-224</code> groups. If that same user group were to then use sensitive data in a prompt, it would be detected and blocked.</p>
