<p>Google Cloud lets you configure custom DNS servers at the Virtual Private Cloud (VPC) network level using <a href="https://cloud.google.com/dns/docs/server-policies-overview#dns-server-policy-out">outbound server policies</a> in Cloud DNS. When you create an outbound server policy, all resources in that VPC network — including existing virtual machines — use the specified DNS servers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1802.md")
</aside>
<p>To configure 1.1.1.1 for your Google Cloud VPC network:</p>
<ol>
<li>Open the <a href="https://console.cloud.google.com">Google Cloud Console</a>.</li>
<li>Go to <strong>Network Services</strong> &gt; <strong>Cloud DNS</strong> and select <a href="https://console.cloud.google.com/net-services/dns/policies"><strong>DNS Server Policies</strong></a>.</li>
<li>Select <strong>Create Policy</strong>.</li>
<li>Enter a name for your policy (for example, <code>cloudflare-1-1-1-1</code>) and select the VPC networks to apply it to.</li>
<li>Under <strong>Alternate DNS servers</strong>, select <strong>Add Item</strong> and enter:</li>
</ol>
<pre><code class="language-txt">1.1.1.1&#10;1.0.0.1&#10;</code></pre>
<ol start="6">
<li>Select <strong>Create</strong>.</li>
</ol>
<p>DNS requests within the configured VPC networks will now use 1.1.1.1.</p>
