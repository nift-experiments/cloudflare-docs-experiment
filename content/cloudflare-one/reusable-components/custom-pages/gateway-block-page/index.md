<p>When Gateway blocks traffic with a <a href="/cloudflare-one/traffic-policies/dns-policies/#block">DNS</a> or <a href="/cloudflare-one/traffic-policies/http-policies/#block">HTTP Block policy</a>, you can configure a block page to display in your users' browsers. You can provide a descriptive reason for blocking traffic and contact information, or you can redirect your users' browsers to another page. You can apply these customizations globally for every Block policy, or override the settings on a per-policy basis.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>In order to display the block page as the URL of the blocked domain, your organization's devices must have a <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/manual-deployment/">Cloudflare certificate</a> installed. Enterprise users can also <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/custom-certificate/">deploy their own root CA certificate</a>. If you do not install a certificate, the block page <a href="#certificate-error">will not display correctly</a>.</p>
<h2 id="configure-the-block-page">Configure the block page</h2>
<p>Gateway will display a global block page in the browser of any user whose traffic is blocked. By default, Gateway will display the block page for any DNS Block policies you turn it on for and all HTTP Block policies. You can <a href="#configure-policy-block-behavior">turn on or override the global setting</a> on a per-policy basis.</p>
<p>To configure the global block page:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Reusable components</strong> &gt; <strong>Custom pages</strong>.</li>
<li>Under <strong>Account Gateway block page</strong>, Gateway will display the current block page setting. Select <strong>Manage</strong>.</li>
<li>Choose whether to use the <a href="#use-the-default-block-page">default Gateway block page</a>, a <a href="#redirect-to-a-block-page">URL redirect</a>, or a <a href="#customize-the-block-page">custom Gateway block page</a>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h3 id="use-the-default-block-page">Use the default block page</h3>
<p>When you choose <strong>Default Gateway block page</strong>, Gateway will display a <a href="https://blocked.teams.cloudflare.com/">block page hosted by Cloudflare</a>. This is the default option for all traffic blocked by Gateway.</p>
<h3 id="redirect-to-a-block-page">Redirect to a block page</h3>
<p>Instead of displaying the Cloudflare block page, you can configure Gateway to return a <code>307</code> (Temporary Redirect) HTTP response code and redirect to a custom URL.</p>
<p>To redirect users to a non-Cloudflare block page:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com">Cloudflare One</a>, go to <strong>Reusable components</strong> &gt; <strong>Custom pages</strong>.</li>
<li>Under <strong>Account Gateway block page</strong>, select <strong>Manage</strong>.</li>
<li>Choose <strong>URL redirect</strong>.</li>
<li>Enter the URL you want to redirect blocked traffic to.</li>
<li>(Optional) Turn on <strong>Send policy context</strong> to send <a href="#policy-context">additional policy context</a> to the redirected URL.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>Gateway will now redirect users to a custom page when user traffic matches a Block policy with the block page configured.</p>
<p>To create an HTTP policy to redirect URLs, refer to the <a href="/cloudflare-one/traffic-policies/http-policies/#redirect">Redirect action</a>.</p>
<h4 id="policy-context">Policy context</h4>
<p>When you turn on <strong>Send policy context</strong>, Gateway will append details of the matching request to the redirected URL as a query string. Not every context field will be included. Potential policy context fields include:</p>
<details class="nb-details"><summary>Policy context fields</summary><div class="nb-details-body">
@input("content/.markup/bodies/5895.md")
</div></details>
<h4 id="redirect-precedence">Redirect precedence</h4>
<p>Paths and queries in the redirect URL take precedence over the original URL. When you turn on <strong>Send policy context</strong>, Gateway will append context to the end of the redirected URL. For example, if the original URL is <code>example.com/path/to/page?querystring=X&amp;k=1</code> and the redirect URL is <code>cloudflare.com/redirect-path?querystring=Y</code>, Gateway will redirect requests to:</p>
<pre><code class="language-txt">cloudflare.com/redirect-path?querystring=Y&amp;cf_user_email=user@example.com&#10;</code></pre>
<h3 id="customize-the-block-page">Customize the block page</h3>
<p>You can customize the Cloudflare-hosted block page by making global changes that Gateway will display every time a user reaches your block page. Customizations will apply regardless of the type of policy (DNS or HTTP) that blocks the traffic.</p>
<p>To customize your block page:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5898.md")
</div></div>
<p>Gateway will now display a custom Gateway block page when your users visit a blocked website.</p>
<h4 id="add-a-logo-image">Add a logo image</h4>
<p>You can include an external logo image to display on your custom block page. The block page resizes all images to 146x146 pixels. The URL must be valid and no longer than 2048 characters. Accepted file types include SVG, PNG, JPEG, and GIF.</p>
<h4 id="allow-users-to-email-an-administrator">Allow users to email an administrator</h4>
<p>You can add a Mailto link to your custom block page, which allows users to directly email you about the blocked site. When users select <strong>Contact your Administrator</strong> on your block page, an email template opens with the email address and subject line you configure, as well as the following diagnostic information:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Site URL</td>
<td>The URL of the blocked page.</td>
</tr>
<tr>
<td>Rule ID</td>
<td>The ID of the Gateway policy that blocked the page.</td>
</tr>
<tr>
<td>Source IP</td>
<td>The public source IP of the user device.</td>
</tr>
<tr>
<td>Account ID</td>
<td>The Cloudflare account associated with the block policy.</td>
</tr>
<tr>
<td>User ID</td>
<td>The ID of the user who visited the page. Currently, User IDs are not surfaced in the dashboard and can only be viewed by calling the <a href="/api/resources/zero_trust/subresources/access/subresources/users/methods/list/">API</a>.</td>
</tr>
<tr>
<td>Device ID</td>
<td>The ID of the device that visited the page. This is generated by the Cloudflare One Client.</td>
</tr>
<tr>
<td>Block Reason</td>
<td>Your policy-specific block message.</td>
</tr>
</tbody>
</table>
<h2 id="configure-policy-block-behavior">Configure policy block behavior</h2>
<p>For DNS Block policies, you will need to turn on the block page for each policy you want to display it. For HTTP Block policies, Gateway automatically displays your global block page setting by default. You can override your global block page setting for both policy types within each policy's settings.</p>
<p>To turn on the block page or override your global block page setting for an individual policy:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5901.md")
</div></div>
<h2 id="limitations">Limitations</h2>
<h3 id="certificate-error">Certificate error</h3>
<p>If your users receive a security risk warning in their browser when visiting a blocked page, check that you have correctly <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/manual-deployment/">installed a certificate</a> on their devices. If a certificate is not installed or the installed certificate is invalid or expired, your user's browser may:</p>
<ul>
<li>Display an <strong>HTTP Response Code: 526</strong> error page, indicating an insecure upstream.</li>
<li>Close the connection and fail to display any pages.</li>
</ul>
<p>For more information on fixing certificate issues, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/common-issues/#browser-and-certificate-issues">Troubleshooting</a>.</p>
<h3 id="incompatible-dns-record-types">Incompatible DNS record types</h3>
<p>To block the resolution of queries for DNS records with types other than <code>A</code> or <code>AAAA</code>, Gateway will respond with the <code>REFUSED (RCODE:5)</code> DNS return code. Gateway will block the request but will not display a block page.</p>
<h3 id="third-party-filtering-conflict">Third-party filtering conflict</h3>
<p>Gateway will not properly filter traffic sent through third-party VPNs or other Internet filtering software, such as <a href="https://support.apple.com/102602">iCloud Private Relay</a> or <a href="https://github.com/GoogleChrome/ip-protection#ip-protection">Google Chrome IP Protection</a>. To ensure your DNS policies apply to your traffic, Cloudflare recommends turning off software that may interfere with Gateway.</p>
<p>To turn off iCloud Private Relay, refer to the Apple user guides for <a href="https://support.apple.com/guide/mac-help/use-icloud-private-relay-mchlecadabe0/">macOS</a> or <a href="https://support.apple.com/guide/iphone/protect-web-browsing-icloud-private-relay-iph499d287c2/">iOS</a>.</p>
<h3 id="data-center-and-ip-address-matching">Data center and IP address matching</h3>
<p>If an HTTP request that matches a block policy does not arrive at the same Cloudflare data center as its DNS query, Gateway will display the default block page instead of your custom block page.</p>
<p>This applies to DNS queries sent to any Gateway resolver endpoint, including those over IPv4, IPv6, and encrypted protocols like DoH (DNS over HTTPS) and DoT (DNS over TLS). If a DNS query is routed to a different Cloudflare data center than the corresponding HTTP request (for example, if DoH traffic is sent outside the WARP tunnel), Gateway cannot correlate the two requests and will display the default block page instead of your custom block page.</p>
<p>If the HTTP request comes from a different IP address than the DNS request, Gateway may not display the rule ID, custom message, or other fields on the block page. This can happen when a recursive DNS resolver's source IP address differs from the user device's IP address.</p>
<h3 id="dual-stack-networks">Dual-stack networks</h3>
<p>On dual-stack networks, the source IP address of the DNS query and the block page connection may differ. The DNS query may go over IPv4 while the browser connects to the block page over IPv6, or the other way around. When this happens, the block page may fail to load. It may also display without policy context (rule ID, block reason, or custom redirect parameters).</p>
<p>To resolve this issue, configure a <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/#dedicated-dns-resolver-ip">dedicated DNS resolver IP address</a> for your DNS location. With dedicated IP addresses, the block server can identify the account based on the destination IP address regardless of the source address.</p>
