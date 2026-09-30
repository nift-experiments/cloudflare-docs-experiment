<p>Gateway follows a specific order of enforcement as traffic travels through the Cloudflare global network to the Internet:</p>
<pre><code class="language-mermaid">flowchart TB&#10;    %% Accessibility&#10;    accTitle: Gateway order of enforcement&#10;    accDescr: Flowchart describing the order of enforcement for Gateway policies.&#10;&#10; subgraph Resolution[&quot;Resolution&quot;]&#10;        dns2[&quot;1.1.1.1&quot;]&#10;        dns4[&quot;Custom resolver&quot;]&#10;        dns3[&quot;Resolver policies &lt;br&gt;(Enterprise users only)&quot;]&#10;        internal[&quot;Internal DNS&quot;]&#10;  end&#10; subgraph DNS[&quot;DNS&quot;]&#10;        dns1[&quot;DNS policies&quot;]&#10;        Resolution&#10;  end&#10; subgraph HTTP[&quot;HTTP policies&quot;]&#10;        http1{{&quot;Do Not Inspect policies&quot;}}&#10;        http2[&quot;Isolate policies  &lt;br&gt;(with Browser Isolation add-on)&quot;]&#10;        http3[&quot;Allow, Block, Do Not Scan, Quarantine, and Redirect policies, DLP, and anti-virus scanning&quot;]&#10;        https[&quot;HTTP or HTTPS?&quot;]&#10;  end&#10; subgraph Proxy[&quot;Proxy&quot;]&#10;        HTTP&#10;        network1[&quot;Network policies&quot;]&#10;        nonhttp[&quot;Non-HTTP(S) traffic&quot;]&#10;  end&#10; subgraph Egress[&quot;Egress&quot;]&#10;        egress1[&quot;Egress policies &lt;br&gt;(Enterprise users only)&quot;]&#10;  end&#10;    start([&quot;Traffic&quot;]) --&gt; dns0[/&quot;DNS query&quot;/] &amp; http0[&quot;Network connections&quot;]&#10;    dns0 ----&gt; dns1&#10;    dns1 -- Resolved by --&gt; dns2&#10;    dns1 --&gt; dns3&#10;    dns3 -- Resolved by --&gt; dns4&#10;    dns2 -----&gt; internet([&quot;Internet&quot;])&#10;    dns4 -----&gt; internet&#10;    dns4 ---&gt; cloudflare[&quot;Private network services &lt;br&gt;(Cloudflare Tunnel, Cloudflare WAN, Cloudflare Mesh)&quot;]&#10;    http1 -- Do Not Inspect --&gt; internet&#10;    http1 -- Inspect --&gt; http2&#10;    http2 --&gt; http3&#10;    http0 --&gt; magic[&quot;Cloudflare Network Firewall (Enterprise users only)&quot;]&#10;    magic --&gt; egress1&#10;    egress1 --&gt; tcp[&quot;Check for origin availability (TCP SYN)&quot;]&#10;    tcp --&gt; network1&#10;    http3 --&gt; internet&#10;    https -- HTTPS --&gt; http1&#10;    https -- HTTP --&gt; http2&#10;    network1 --&gt; https &amp; nonhttp&#10;    dns3 -- Resolved by --&gt; internal &amp; dns2&#10;    nonhttp -----&gt; internet&#10;&#10;    https@{ shape: hex}&#10;    http0@{ shape: lean-r}&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="order-of-enforcement-change-on-2025-07-14">Order of enforcement change on 2025-07-14</h3>
@markup("md", "content/.markup/bodies/10028.md")
</aside>
<h2 id="connection-establishment">Connection establishment</h2>
<p>When a user connects to a server with Gateway, Gateway first establishes a TCP connection with the destination server on the port the user requested. Because TCP traffic is proxied by Cloudflare, the connection Gateway establishes with the origin is independent from the connection users establish with Gateway. This means Gateway assigns a new source IP and port to the user's connection and no details from the user's TCP handshake are included in the TCP handshake with the origin server.</p>
<p>If the TCP connection to the destination server is successful, Gateway will apply policies. If Gateway policies allow the connection, Gateway will connect the user to the destination server. If Gateway policies block the connection, Gateway will end the connection and will not send any data between the user and the destination server. If the TCP connection to the destination server is unsuccessful, Gateway will not run any policies and retry TCP connections from the user to the server.</p>
<pre><code class="language-mermaid">flowchart TD&#10;    %% Accessibility&#10;    accTitle: How Gateway proxy works&#10;    accDescr: Flowchart describing how the Gateway proxy uses the Happy Eyeballs algorithm to establish TCP connections and proxy user traffic.&#10;&#10;    %% Flowchart&#10;    A[User&#x27;s device sends TCP SYN to Gateway] --&gt; B[Gateway sends TCP SYN to origin server]&#10;    B --&gt; C{{Origin server responds with TCP SYN-ACK?}}&#10;    C --&gt;|Yes| E[TCP handshakes completed]&#10;    C --&gt;|No| D[Connection fails]&#10;    E --&gt; F{{Connection allowed?}}&#10;    F --&gt;|Allow policy| G[Gateway proxies traffic bidirectionally]&#10;    F --&gt;|Block policy| H[Connection blocked by firewall policies]&#10;&#10;    %% Styling&#10;    style D stroke:#D50000&#10;    style G stroke:#00C853&#10;    style H stroke:#D50000&#10;</code></pre>
<p>Connections to Zero Trust will always appear in your <a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust network session logs</a> regardless of connection success. Because Gateway does not inspect failed connections, they will not appear in your <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway activity logs</a>.</p>
<h3 id="filter-tcp-syn-packets-with-cloudflare-network-firewall">Filter TCP SYN packets with Cloudflare Network Firewall</h3>
<p>Because Gateway sends a TCP SYN to the destination server before evaluating policies, Gateway Network or HTTP Block policies do not prevent the initial TCP SYN from reaching the destination server. If you need to prevent TCP SYN packets from being sent to specific destination IP addresses, you can create a <a href="/cloudflare-one/traffic-policies/packet-filtering/">Cloudflare Network Firewall</a> rule to block traffic at the packet level. As shown in the <a href="#order-of-enforcement">enforcement flowchart</a>, Cloudflare Network Firewall evaluates traffic before Gateway checks for origin availability.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10026.md")
</aside>
<p>To block TCP SYN packets to a specific destination:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Firewall policies</strong> &gt; <strong>Custom policies</strong>.</li>
<li>Select <strong>Add a policy</strong>.</li>
<li>Create a rule with the destination IP address or CIDR range you want to block. For example, to block all traffic to <code>10.0.0.0/8</code>, use the expression <code>ip.dst in {10.0.0.0/8}</code> with a <strong>Block</strong> action.</li>
<li>Select <strong>Add new policy</strong>.</li>
</ol>
<p>For more information on creating packet filtering rules, refer to <a href="/cloudflare-one/traffic-policies/packet-filtering/add-policies/">Add policies</a>.</p>
<h2 id="priority-between-policy-builders">Priority between policy builders</h2>
<p>Gateway applies your policies in the following order:</p>
<ol>
<li>DNS policies with selectors evaluated before resolution</li>
<li>Resolver policies (if applicable)</li>
<li>DNS policies with selectors evaluated after resolution</li>
<li>Egress policies (if applicable)</li>
<li>Network policies</li>
<li>HTTP policies</li>
</ol>
<p>DNS and resolver policies are standalone. For example, if you block a site with a DNS policy but do not create a corresponding HTTP policy, users can still access the site if they know its IP address.</p>
<h3 id="http-3-traffic">HTTP/3 traffic</h3>
<p>For proxied <a href="/cloudflare-one/traffic-policies/http-policies/http3/">HTTP/3 traffic</a>, Gateway applies your policies in the following order:</p>
<ol>
<li>DNS policies</li>
<li>Network policies</li>
<li>HTTP policies</li>
</ol>
<h2 id="priority-within-a-policy-builder">Priority within a policy builder</h2>
<h3 id="dns-policies">DNS policies</h3>
<p>Gateway evaluates DNS policies first in order of DNS resolution, then in <a href="#order-of-precedence">order of precedence</a>.</p>
<p>When DNS queries are received, Gateway evaluates policies with pre-resolution selectors, resolves the DNS query, then evaluates policies with post-resolution selectors. This means policies with selectors evaluated before DNS resolution take precedence. For example, the following set of policies will block <code>example.com</code>:</p>
<table>
<thead>
<tr>
<th>Precedence</th>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Resolved Country IP Geolocation</td>
<td>is</td>
<td>United States</td>
<td>Allow</td>
</tr>
<tr>
<td>2</td>
<td>Domain</td>
<td>is</td>
<td><code>example.com</code></td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>Despite an explicit Allow policy ordered first, policy 2 takes precedence because the <em>Domain</em> selector is evaluated before DNS resolution.</p>
<p>If a policy contains both pre-resolution and post-resolution selectors, Gateway will evaluate the entire policy after DNS resolution. For information on when each selector is evaluated, refer to the <a href="/cloudflare-one/traffic-policies/dns-policies/#selectors">list of DNS selectors</a>.</p>
<h3 id="network-policies">Network policies</h3>
<p>Gateway evaluates network policies in <a href="#order-of-precedence">order of precedence</a>.</p>
<h3 id="http-policies">HTTP policies</h3>
<p>Gateway applies HTTP policies based on a combination of <a href="/cloudflare-one/traffic-policies/http-policies/#actions">action type</a> and <a href="#order-of-precedence">order of precedence</a>:</p>
<ol>
<li>All Do Not Inspect policies are evaluated first, in order of precedence.</li>
<li>If no policies match, all Isolate policies are evaluated in order of precedence.</li>
<li>All Allow, Block and Do Not Scan policies are evaluated in order of precedence.</li>
<li>The body of the HTTP request, including Data Loss Prevention (DLP), AV scanning, and file sandboxing, is evaluated.</li>
</ol>
<p>This order of enforcement allows Gateway to first determine whether decryption should occur. If a site matches a Do Not Inspect policy, it is automatically allowed through Gateway and bypasses all other HTTP policies.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10025.md")
</aside>
<p>Next, Gateway checks decrypted traffic against your Isolate policies. When a user makes a request which triggers an Isolate policy, the request will be rerouted to a <a href="/cloudflare-one/remote-browser-isolation/">remote browser</a>.</p>
<p>Next, Gateway evaluates all Allow, Block, and Do Not Scan policies. These policies apply to both isolated and non-isolated traffic. For example, if <code>example.com</code> is isolated and <code>example.com/subpage</code> is blocked, Gateway will block the subpage (<code>example.com/subpage</code>) inside of the remote browser.</p>
<p>Lastly, Gateway inspects the body of the HTTP request by evaluating it against DLP policies, and running anti-virus scanning and file sandboxing. If DLP Block policies are present, the action Gateway ultimately takes may not match the action it initially logs. For more information, refer to <a href="#dlp-policy-precedence">DLP policy precedence</a>.</p>
<h3 id="resolver-policies">Resolver policies</h3>
<p>When <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policies</a> are present, Gateway first evaluates any DNS policies with pre-resolution selectors, then routes any DNS queries according to the <a href="#order-of-precedence">order of precedence</a> of your resolver policies, and lastly evaluates any DNS policies with post-resolution selectors.</p>
<h3 id="default-behavior-when-no-policy-matches">Default behavior when no policy matches</h3>
<p>If traffic does not match any explicit Allow or Block policy, Gateway applies the following defaults:</p>
<table>
<thead>
<tr>
<th>Policy type</th>
<th>Default action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>DNS</td>
<td>Allow</td>
<td>DNS queries resolve normally through the configured resolver.</td>
</tr>
<tr>
<td>Network</td>
<td>Allow</td>
<td>TCP and UDP connections are allowed through the Gateway proxy.</td>
</tr>
<tr>
<td>HTTP</td>
<td>Allow</td>
<td>HTTP and HTTPS requests are allowed. However, if you have configured a default Block action in your <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policy settings</a>, unmatched traffic is blocked instead.</td>
</tr>
</tbody>
</table>
<p>Because the default is to allow unmatched traffic, Gateway follows a permissive model. To switch to a restrictive model (block by default, allow by exception), create a catch-all Block policy at the lowest precedence in the relevant policy builder and add specific Allow policies above it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10024.md")
</aside>
<h3 id="order-of-precedence">Order of precedence</h3>
<p>Order of precedence refers to the priority of individual policies within the DNS, network, or HTTP policy builder. Gateway evaluates policies in ascending order beginning with the lowest value.</p>
<p>The order of precedence follows the first match principle. Once traffic matches an Allow or Block policy, evaluation stops and no subsequent policies can override the decision. Therefore, Cloudflare recommends assigning the most specific policies and exceptions with the highest precedence and the most general policies with the lowest precedence.</p>
<h4 id="cloudflare-dashboard">Cloudflare dashboard</h4>
<p>In the Cloudflare dashboard, policies are in order of precedence from top to bottom of the list. Policies begin with precedence <code>1</code> and count upward. You can modify the order of precedence by dragging and dropping individual policies in the dashboard.</p>
<h4 id="cloudflare-api">Cloudflare API</h4>
<p>To update the precedence of a policy with the Cloudflare API, use the <a href="/api/resources/zero_trust/subresources/gateway/subresources/rules/methods/update/">Update a Zero Trust Gateway rule</a> endpoint to update the <code>precedence</code> field.</p>
<h4 id="dlp-policy-precedence">DLP policy precedence</h4>
<p>For Gateway configurations with DLP policies, Gateway will filter and log traffic based on first match, then scan the body of the HTTP request for matching content. Because of the first match principle, Gateway may perform and log a decision for traffic, then perform a contradicting decision. For example, if traffic is first allowed with an Allow HTTP policy, then blocked with a DLP Block policy, Gateway will log the initial Allow action despite ultimately blocking the request.</p>
<h4 id="access-applications">Access applications</h4>
<p>If Gateway traffic is headed to a private IP address protected as an Access application, that traffic will still be evaluated by the destination application's Access policies, even if a Gateway Allow policy matched first. Gateway Block policies that match traffic will terminate any other policy evaluation. This is expected behavior. A Gateway Allow policy does not override or bypass Access policies.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="terraform-provider-v4-precedence-limitation">Terraform provider v4 precedence limitation</h3>
@markup("md", "content/.markup/bodies/10023.md")
</aside>
<h2 id="example">Example</h2>
<p>Suppose you have a list of policies arranged in the following order of precedence:</p>
<ul>
<li>DNS policies:</li>
</ul>
<table>
<thead>
<tr>
<th>Precedence</th>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Host</td>
<td>is</td>
<td><code>example.com</code></td>
<td>Block</td>
</tr>
<tr>
<td>2</td>
<td>Host</td>
<td>is</td>
<td><code>test.example.com</code></td>
<td>Allow</td>
</tr>
<tr>
<td>3</td>
<td>Domain</td>
<td>matches regex</td>
<td><code>.\</code></td>
<td>Block</td>
</tr>
</tbody>
</table>
<ul>
<li>HTTP policies:</li>
</ul>
<table>
<thead>
<tr>
<th>Precedence</th>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Host</td>
<td>is</td>
<td><code>example.com</code></td>
<td>Block</td>
</tr>
<tr>
<td>2</td>
<td>Host</td>
<td>is</td>
<td><code>test2.example.com</code></td>
<td>Do Not Inspect</td>
</tr>
</tbody>
</table>
<ul>
<li>Network policies:</li>
</ul>
<table>
<thead>
<tr>
<th>Precedence</th>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Destination Port</td>
<td>is</td>
<td><code>80</code></td>
<td>Block</td>
</tr>
<tr>
<td>2</td>
<td>Destination port</td>
<td>is</td>
<td><code>443</code></td>
<td>Allow</td>
</tr>
<tr>
<td>3</td>
<td>SNI Domain</td>
<td>is</td>
<td><code>test.example.com</code></td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>When a user goes to <code>https://test.example.com</code>, Gateway performs the following operations:</p>
<ol>
<li>
<p>Evaluate DNS request against DNS policies:</p>
<ol>
<li>Policy #1 does not match <code>test.example.com</code> — move on to check Policy #2.</li>
<li>Policy #2 matches, so DNS resolution is allowed.</li>
<li>Policy #3 is not evaluated because there has already been an explicit match.</li>
</ol>
</li>
<li>
<p>Evaluate HTTPS request against network policies:</p>
<ol>
<li>Policy #1 does not match because port 80 is used for standard HTTP, not HTTPS.</li>
<li>Policy #2 matches, so the request is allowed and proxied to the upstream server.</li>
<li>Policy #3 is not evaluated because there has already been an explicit match.</li>
</ol>
</li>
<li>
<p>Evaluate HTTPS request against HTTP policies:</p>
<ol>
<li>Policy #2 is evaluated first because Do Not Inspect <a href="#http-policies">always takes precedence</a> over Allow and Block. Since there is no match, move on to check Policy #1.</li>
<li>Policy #1 does not match <code>test.example.com</code>. Since there are no matching Block policies, the request passes the HTTP filter.</li>
</ol>
</li>
</ol>
<p>Therefore, the user is able to connect to <code>https://test.example.com</code>.</p>
<h2 id="precedence-calculations">Precedence calculations</h2>
<p>When arranging policies in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, Gateway automatically calculates the precedence for rearranged policies.</p>
<p>When using the API to create a policy, unless the precedence is explicitly defined in the policy, Gateway will assign precedence to policies starting at <code>1000</code>. Every time a new policy is added to the bottom of the order, Gateway will calculate the current highest precedence in the account and add a random integer between 1 and 100 to <code>1000</code> so that it now claims the maximum precedence in the account. To manually update a policy's precedence, use the <a href="/api/resources/zero_trust/subresources/gateway/subresources/rules/methods/update/">Update a Zero Trust Gateway rule</a> endpoint. You can set a policy's precedence to any value that is not already in use.</p>
<p>Changing the order within the Cloudflare dashboard or API may result in configuration issues when using <a href="#manage-precedence-with-terraform">Terraform</a>.</p>
<h2 id="manage-precedence-with-terraform">Manage precedence with Terraform</h2>
<p>You can manage the order of execution of your Gateway policies using Terraform. With version 5 of the Terraform Cloudflare provider, Gateway users can list their policies in a Terraform file with any desired integer precedence value. Cloudflare recommends starting with a precedence of <code>1000</code> and adding extra space between each policy's precedence for any future policies. For example:</p>
<pre><code class="language-tf">resource &quot;cloudflare_zero_trust_gateway_policy&quot; &quot;policy_1&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  &#35; other attributes...&#10;  precedence = 1000&#10;}&#10;&#10;resource &quot;cloudflare_zero_trust_gateway_policy&quot; &quot;policy_2&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  &#35; other attributes...&#10;  precedence = 2000&#10;}&#10;&#10;resource &quot;cloudflare_zero_trust_gateway_policy&quot; &quot;policy_3&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  &#35; other attributes...&#10;  precedence = 3000&#10;}&#10;</code></pre>
<p>To avoid precedence calculation errors when reordering policies with Terraform, you should move one policy at a time before running <code>terraform plan</code> and <code>terraform apply</code>. If you use both Terraform and the Cloudflare dashboard or API, sync your polices with <code>terraform refresh</code> before reordering policies in Terraform. Alternatively, you can set your account to <a href="/cloudflare-one/api-terraform/#set-dashboard-to-read-only">read-only in the Cloudflare dashboard</a>, only allowing changes using the API or Terraform.</p>
