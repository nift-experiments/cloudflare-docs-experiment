<p>A root ruleset is the top-level container that holds all your firewall policies. You can check for an existing root ruleset from the dashboard or via the <a href="/api/resources/rulesets/methods/list/">Account rulesets API</a>. If you are a new Magic Transit customer, you may not have a root ruleset created for your account. To view examples for root rulesets, review the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/magic_firewall_ruleset">Cloudflare Network Firewall Terraform documentation</a>.</p>
<p>By default, you can create a maximum of 200 policies. Contact your account team to request a higher limit if needed. We recommend you create lists of IP addresses to reference within policies to streamline policy management.</p>
<h2 id="add-a-policy">Add a policy</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and go to <strong>Networking</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>Select <strong>Add a policy</strong>.</li>
<li>Fill out the information for your new policy. All existing policies apply to IPv4 traffic only. You can use a <a href="/waf/tools/lists/managed-lists/#managed-ip-lists">Managed IP List</a> when populating the <strong>Value</strong>.</li>
<li>When you are done, select <strong>Add new policy</strong>.</li>
</ol>
<h2 id="create-a-disabled-policy">Create a disabled policy</h2>
<p>When you add a new policy, the policy is <strong>Enabled</strong> by default.</p>
<p>To create a <strong>Disabled</strong> policy, follow the steps in <a href="#add-a-policy">Add a policy</a> above and toggle <strong>Enabled</strong> to off. When a policy is in the disabled state, the policy will not perform the action until it is set to <strong>Enabled</strong>.</p>
<p>To disable an existing policy, from the <strong>Custom policies</strong> tab, set the <strong>Enabled</strong> toggle to off.</p>
<h2 id="update-a-policy">Update a policy</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and go to <strong>Networking</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>Locate the policy you want to edit and select the three dots &gt; <strong>Edit</strong>.</li>
<li>Update the policy with your changes and select <strong>Save</strong>.</li>
</ol>
<h2 id="delete-an-existing-policy">Delete an existing policy</h2>
<ol>
<li>Locate the policy you want to delete in the list.</li>
<li>From the end of the row, select <strong>Delete</strong>.</li>
<li>Select <strong>Delete</strong> again to confirm the deletion.</li>
</ol>
<h2 id="api">API</h2>
<p>Below, you can find examples of how to use the API to perform certain actions.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/6420.md")
</aside>
<h3 id="skip-action">Skip action</h3>
<p>A skip action tells the firewall to stop evaluating the current ruleset for matching traffic, effectively allowing it through. Rules in a ruleset evaluate in order from top to bottom. In the example below, the skip rule must appear before the block rule so that matching traffic (port <code>8080</code>) is allowed through before the catch-all block applies.</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;Example ruleset&quot;,&#10;  &quot;kind&quot;: &quot;root&quot;,&#10;  &quot;phase&quot;: &quot;magic_transit&quot;,&#10;  &quot;description&quot;: &quot;Example ruleset description&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;skip&quot;,&#10;      &quot;action_parameters&quot;: { &quot;ruleset&quot;: &quot;current&quot; },&#10;      &quot;expression&quot;: &quot;tcp.dstport in { 8080 } &quot;,&#10;      &quot;description&quot;: &quot;Allow port 8080&quot;&#10;    },&#10;    {&#10;      &quot;action&quot;: &quot;block&quot;,&#10;      &quot;expression&quot;: &quot;tcp.dstport in { 1..65535 }&quot;,&#10;      &quot;description&quot;: &quot;Block all TCP ports&quot;&#10;    }&#10;  ]&#10;}&#x27;&#10;</code></pre>
<h3 id="block-a-country">Block a country</h3>
<p>The example below blocks all packets with a source or destination IP address coming from Brazil by using its 2-letter country code in <a href="https://www.iso.org/obp/ui/#search/code/">ISO 3166-1 Alpha 2</a> format.</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;Example ruleset&quot;,&#10;  &quot;kind&quot;: &quot;root&quot;,&#10;  &quot;phase&quot;: &quot;magic_transit&quot;,&#10;  &quot;description&quot;: &quot;Example ruleset description&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;block&quot;,&#10;      &quot;expression&quot;: &quot;ip.src.country == \&quot;BR\&quot;&quot;,&#10;      &quot;description&quot;: &quot;Block traffic from Brazil&quot;&#10;    }&#10;  ]&#10;}&#x27;&#10;</code></pre>
<h3 id="use-an-ip-list">Use an IP list</h3>
<p>Cloudflare Network Firewall supports <a href="/waf/tools/lists/use-in-expressions/">using lists in expressions</a> for the <code>ip.src</code> and <code>ip.dst</code> fields. The supported lists are:</p>
<ul>
<li><code>$cf.anonymizer</code> - Anonymizer proxies</li>
<li><code>$cf.botnetcc</code> - Botnet command and control channel</li>
<li><code>$cf.malware</code> - Sources of malware</li>
<li><code>$&lt;IP_LIST_NAME&gt;</code> - The name of an account-level IP list</li>
</ul>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;Example ruleset&quot;,&#10;  &quot;kind&quot;: &quot;root&quot;,&#10;  &quot;phase&quot;: &quot;magic_transit&quot;,&#10;  &quot;description&quot;: &quot;Example ruleset description&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;block&quot;,&#10;      &quot;expression&quot;: &quot;ip.src in $cf.anonymizer&quot;,&#10;      &quot;description&quot;: &quot;Block traffic from anonymizer proxies&quot;&#10;    }&#10;  ]&#10;}&#x27;&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p>Refer to <a href="/cloudflare-one/traffic-policies/packet-filtering/form-expressions/">Form expressions</a> for more information on how to write rule expressions.</p>
