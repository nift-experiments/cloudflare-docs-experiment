<p>These steps configure 1.1.1.1 as the DNS resolver for an Azure Virtual Network (VNet). This applies to all resources in the VNet, including virtual machines.</p>
<ol>
<li>Log in to your Azure portal.</li>
<li>From the Azure portal side menu, select <strong>Virtual Networks</strong>.</li>
<li>Select the virtual network you want to configure.</li>
<li>Select <strong>DNS Servers</strong> &gt; <strong>Custom</strong>, and add two entries:</li>
</ol>
<pre><code class="language-txt">1.1.1.1&#10;1.0.0.1&#10;</code></pre>
<ol start="5">
<li>Select <strong>Save</strong>.</li>
</ol>
