<h1 id="changelog">Changelog</h1>

<h2 id="new-snippets-code-editor"><a href="/changelog/post/2025-01-29-snippets-code-editor/">New Snippets Code Editor</a></h2>
<p><em>2025-01-29</em></p>
<p>The new <a href="/rules/snippets/">Snippets</a> code editor lets you edit Snippet code and rule in one place, making it easier to test and deploy changes without switching between pages.</p>
<p><img src="/assets/upstream/images/changelog/rules/snippets-new-editor.png" alt="New Snippets code editor" /></p>
<p>What’s new:</p>
<ul>
<li><strong>Single-page editing for code and rule</strong> – No need to jump between screens.</li>
<li><strong>Auto-complete &amp; syntax highlighting</strong> – Get suggestions and avoid mistakes.</li>
<li><strong>Code formatting &amp; refactoring</strong> – Write cleaner, more readable code.</li>
</ul>
<p>Try it now in <a href="https://dash.cloudflare.com/?to=/:account/:zone/rules/snippets">Rules &gt; Snippets</a>.</p>


<h2 id="new-rules-overview-interface"><a href="/changelog/post/2025-01-09-rules-overview/">New Rules Overview Interface</a></h2>
<p><em>2025-01-09</em></p>
<p><strong>Rules Overview</strong> gives you a single page to manage all your <a href="/rules/">Cloudflare Rules</a>.</p>
<p>What you can do:</p>
<ul>
<li><strong>See all your rules in one place</strong> – No more clicking around.</li>
<li><strong>Find rules faster</strong> – Search by name.</li>
<li><strong>Understand execution order</strong> – See how rules run in sequence.</li>
<li><strong>Debug easily</strong> – Use <a href="/rules/trace-request/">Trace</a> without switching tabs.</li>
</ul>
<p>Check it out in <a href="https://dash.cloudflare.com/?to=/:account/:zone/rules/overview">Rules &gt; Overview</a>.</p>


<h2 id="troubleshoot-tunnels-with-diagnostic-logs"><a href="/changelog/post/2024-12-19-diagnostic-logs/">Troubleshoot tunnels with diagnostic logs</a></h2>
<p><em>2024-12-19</em></p>
<p>The latest <code>cloudflared</code> build <a href="https://github.com/cloudflare/cloudflared/releases/tag/2024.12.2">2024.12.2</a> introduces the ability to collect all the diagnostic logs needed to troubleshoot a <code>cloudflared</code> instance.</p>
<p>A diagnostic report collects data from a single instance of <code>cloudflared</code> running on the local machine and outputs it to a <code>cloudflared-diag</code> file.</p>
<p>For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/">Diagnostic logs</a>.</p>


<h2 id="establish-bgp-peering-over-direct-cni-circuits"><a href="/changelog/post/2024-12-17-bgp-support-cni/">Establish BGP peering over Direct CNI circuits</a></h2>
<p><em>2024-12-17</em></p>
<p>Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using a Direct CNI on-ramp.</p>
<p>Using BGP peering allows customers to:</p>
<ul>
<li>Automate the process of adding or removing networks and subnets.</li>
<li>Take advantage of failure detection and session recovery features.</li>
</ul>
<p>With this functionality, customers can:</p>
<ul>
<li>Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via CNI.</li>
<li>Secure the session by MD5 authentication to prevent misconfigurations.</li>
<li>Exchange routes dynamically between their devices and their Magic routing table.</li>
</ul>
<p>Refer to <a href="/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes">Magic WAN BGP peering</a> or <a href="/magic-transit/how-to/configure-routes/#configure-bgp-routes">Magic Transit BGP peering</a> to learn more about this feature and how to set it up.</p>


<h2 id="terraform-support-for-snippets"><a href="/changelog/post/2024-12-11-terraform-snippets/">Terraform Support for Snippets</a></h2>
<p><em>2024-12-11</em></p>
<p>Now, you can manage <a href="/rules/snippets/">Cloudflare Snippets</a> with <a href="/terraform/">Terraform</a>. Use infrastructure-as-code to deploy and update Snippet code and rules without manual changes in the dashboard.</p>
<p>Example Terraform configuration:</p>
<pre><code class="language-tf">resource &quot;cloudflare_snippet&quot; &quot;my_snippet&quot; {&#10;	zone_id  = &quot;&lt;ZONE_ID&gt;&quot;&#10;	name = &quot;my_test_snippet_1&quot;&#10;	main_module = &quot;file1.js&quot;&#10;	files {&#10;		name = &quot;file1.js&quot;&#10;		content = file(&quot;file1.js&quot;)&#10;	}&#10;}&#10;&#10;resource &quot;cloudflare_snippet_rules&quot; &quot;cookie_snippet_rule&quot; {&#10;	zone_id  = &quot;&lt;ZONE_ID&gt;&quot;&#10;	rules {&#10;		enabled = true&#10;		expression = &quot;http.cookie eq \&quot;a=b\&quot;&quot;&#10;		description = &quot;Trigger snippet on specific cookie&quot;&#10;		snippet_name = &quot;my_test_snippet_1&quot;&#10;	}&#10;	depends_on = [cloudflare_snippet.my_snippet]&#10;}&#10;</code></pre>
<p>Learn more in the <a href="/rules/snippets/create-terraform/">Configure Snippets using Terraform</a> documentation.</p>


<h2 id="generate-customized-terraform-files-for-building-cloud-network-on-ramps"><a href="/changelog/post/2024-12-05-cloud-onramp-terraform/">Generate customized terraform files for building cloud network on-ramps</a></h2>
<p><em>2024-12-05</em></p>
<p>You can now generate customized terraform files for building cloud network on-ramps to <a href="/cloudflare-wan/">Magic WAN</a>.</p>
<p><a href="/multi-cloud-networking/">Magic Cloud</a> can scan and discover existing network resources and generate the required terraform files to automate cloud resource deployment using their existing infrastructure-as-code workflows for cloud automation.</p>
<p>You might want to do this to:</p>
<ul>
<li>Review the proposed configuration for an on-ramp before deploying it with Cloudflare.</li>
<li>Deploy the on-ramp using your own infrastructure-as-code pipeline instead of deploying it with Cloudflare.</li>
</ul>
<p>For more details, refer to <a href="/multi-cloud-networking/cloud-on-ramps/#set-up-with-terraform">Set up with Terraform</a>.</p>


<h2 id="cloud-connector-now-supports-r2"><a href="/changelog/post/2024-11-22-cloud-connector-r2/">Cloud Connector Now Supports R2</a></h2>
<p><em>2024-11-22</em></p>
<p>Now, you can use <a href="/rules/cloud-connector/">Cloud Connector</a> to route traffic to your <a href="/r2/">R2 buckets</a> based on URLs, headers, geolocation, and more.</p>
<p>Example setup:</p>
<pre><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/cloud_connector/rules&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;[&#10;  {&#10;    &quot;expression&quot;: &quot;http.request.uri.path wildcard \&quot;/images/*\&quot;&quot;,&#10;    &quot;provider&quot;: &quot;cloudflare_r2&quot;,&#10;    &quot;description&quot;: &quot;Connect to R2 bucket containing images&quot;,&#10;    &quot;parameters&quot;: {&#10;      &quot;host&quot;: &quot;mybucketcustomdomain.example.com&quot;&#10;    }&#10;  }&#10;]&#x27;&#10;</code></pre>
<p>Get started using <a href="/rules/cloud-connector/">Cloud Connector</a> documentation.</p>


<h2 id="simplified-ui-for-url-rewrites"><a href="/changelog/post/2024-10-23-url-rewrites-wildcard/">Simplified UI for URL Rewrites</a></h2>
<p><em>2024-10-23</em></p>
<p>It’s now easy to create <strong>wildcard-based <a href="/rules/transform/url-rewrite/">URL Rewrites</a></strong>. No need for complex functions—just define your patterns and go.</p>
<p><img src="/assets/upstream/images/rules/transform/create-url-rewrite-rule.png" alt="Rules Overview Interface" /></p>
<p>What’s improved:</p>
<ul>
<li><strong>Full wildcard support</strong> – Create rewrite patterns using intuitive interface.</li>
<li><strong>Simplified rule creation</strong> – No need for complex functions.</li>
</ul>
<p>Try it via <a href="/rules/transform/url-rewrite/create-dashboard/#wildcard-pattern-parameters">creating a Rewrite URL rule in the dashboard</a>.</p>


<h2 id="search-for-custom-rules-using-rule-name-and-or-id"><a href="/changelog/post/2024-10-02-custom-rule-search/">Search for custom rules using rule name and/or ID</a></h2>
<p><em>2024-10-02</em></p>
<p>The Magic Firewall dashboard now allows you to search custom rules using the rule name and/or ID.</p>
<ol>
<li>Log into the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>Analytics &amp; Logs</strong> &gt; <strong>Network Analytics</strong>.</li>
<li>Select <strong>Magic Firewall</strong>.</li>
<li>Add a filter for <strong>Rule ID</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/changelog/cloudflare-network-firewall/search-with-rule-id.png" alt="Search for firewall rules with rule IDs" /></p>
<p>Additionally, the rule ID URL link has been added to Network Analytics.</p>


<h2 id="try-out-magic-network-monitoring"><a href="/changelog/post/2024-09-24-magic-network-monitoring/">Try out Magic Network Monitoring</a></h2>
<p><em>2024-09-24</em></p>
<p>The free version of Magic Network Monitoring (MNM) is now available to everyone with a Cloudflare account by default.</p>
<ol>
<li>Log in to your <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>, and select your account.</li>
<li>Go to <strong>Analytics &amp; Logs</strong> &gt; <strong>Magic Monitoring</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/changelog/network-flow/get-started.png" alt="Try out the free version of Magic Network Monitoring" /></p>
<p>For more details, refer to the <a href="/network-flow/get-started/">Get started guide</a>.</p>


<h2 id="new-rules-templates-for-one-click-rule-creation"><a href="/changelog/post/2024-09-05-rules-templates/">New Rules Templates for One-Click Rule Creation</a></h2>
<p><em>2024-09-05</em></p>
<p>Now, you can create <strong>common rule configurations</strong> in just <strong>one click</strong> using Rules Templates.</p>
<p><img src="/assets/upstream/images/changelog/rules/rules-templates.gif" alt="Rules Templates" /></p>
<p>What you can do:</p>
<ul>
<li><strong>Pick a pre-built rule</strong> – Choose from a library of templates.</li>
<li><strong>One-click setup</strong> – Deploy best practices instantly.</li>
<li><strong>Customize as needed</strong> – Adjust templates to fit your setup.</li>
</ul>
<p>Template cards are now also available directly in the rule builder for each product.</p>
<p>Need more ideas? Check out the <a href="/rules/examples/">Examples gallery</a> in our documentation.</p>


<h2 id="explore-product-updates-for-cloudflare-one"><a href="/changelog/post/2024-06-16-cloudflare-one/">Explore product updates for Cloudflare One</a></h2>
<p><em>2024-06-16</em></p>
<p>Welcome to your new home for product updates on <a href="/cloudflare-one/">Cloudflare One</a>.</p>
<p>Our <a href="/changelog/">new changelog</a> lets you read about changes in much more depth, offering in-depth examples, images, code samples, and even gifs.</p>
<p>If you are looking for older product updates, refer to the following locations.</p>
<details class="nb-details" open><summary>Older product updates</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17707.md")</div></details>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/network-security/3/">Previous</a><span>Page 4 of 4</span></nav>
