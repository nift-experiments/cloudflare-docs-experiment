<p>This tutorial is intended as an introductory example of how you can leverage Cloudflare's global traffic management.</p>
<p>The following sections will guide you through setting up an <a href="/load-balancing/load-balancers/common-configurations/#active---passive-failover">active-passive failover</a> load balancer with <a href="/pages/">Cloudflare Pages</a> as one of the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/10372.md")
</div>, while also going into details about the Load Balancing dashboard workflow, and some important field values and troubleshooting.
<h2 id="use-cases">Use cases</h2>
<p>This setup can be useful if you are migrating your production website or application to Pages or if you just want to have a backup or a personalized web page for when your primary origin goes down.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Make sure you:</p>
<ul>
<li>Are familiar with the Cloudflare <a href="/load-balancing/understand-basics/load-balancing-components/">Load Balancing components</a>.</li>
<li>Own a domain and use Cloudflare as a <a href="/dns/zone-setups/full-setup/">primary DNS provider</a>.</li>
<li>Have <a href="/pages/get-started/git-integration/">deployed a website or application</a> with Cloudflare Pages.</li>
<li>Have <a href="/load-balancing/get-started/enable-load-balancing/">enabled Load Balancing</a> in your account.</li>
</ul>
<h2 id="create-health-monitor">Create health monitor</h2>
<p>Although you can create all the components in the <strong>Create Load Balancer</strong> workflow, using the <strong>Manage Monitors</strong> and <strong>Manage Pools</strong> sections separately makes it easier to test and troubleshoot the configurations of each of these components before bringing them together in a load balancer.</p>
<p>Monitors define the criteria based on which an endpoint will be considered healthy or not. Start by setting up a monitor as follows.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Load Balancing</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Monitors</strong> tab and then <strong>Create monitor</strong>.</li>
<li>Give the monitor a descriptive name and confirm the other fields are filled in as the following:</li>
</ol>
<table>
<thead>
<tr>
<th>Field</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Type</td>
<td>HTTP</td>
</tr>
<tr>
<td>Path</td>
<td>/</td>
</tr>
<tr>
<td>Port</td>
<td>80</td>
</tr>
</tbody>
</table>
<ol start="4">
<li>
<p>Under <strong>Advanced health check settings</strong>, keep the default values and enable the <strong>Follow Redirects</strong> option.</p>
<p>When you are using a service like Cloudflare Pages, it is possible that requests from the health monitor - as well as the ones from your visitors - are redirected before reaching their destination. Enabling this option prevents the monitor from reporting an unhealthy endpoint when it actually has only been redirected (with a <code>301</code> code, for example).</p>
</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="tip">Tip</h3>
@markup("md", "content/.markup/bodies/10371.md")
</aside>
<ol start="5">
<li>Select <strong>Save</strong> to confirm.</li>
</ol>
<h2 id="create-pools">Create pools</h2>
<p>Pools hold information about where the health monitor requests and your visitors requests will be directed to.</p>
<p>To support the <a href="#use-cases">use cases</a> mentioned above, and assuming you only have one origin server for your production website and one for the Cloudflare Pages instance, create two pools with one endpoint each:</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/10370.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Load Balancing</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select the <strong>Pools</strong> tab and then <strong>Create monitor</strong>.</p>
</li>
<li>
<p>For the first pool, start by filling out the fields:</p>
</li>
</ol>
<ul>
<li>A name for the pool (must be unique). Suggestion: <code>primary</code></li>
<li>A description to provide more details on the name. Suggestion: <code>production website</code></li>
</ul>
<ol start="4">
<li>
<p>Leave the choice for <a href="/load-balancing/understand-basics/traffic-steering/origin-level-steering/"><strong>Endpoint Steering</strong></a> as is. Since each pool will only have one endpoint, this steering method will not interfere in this case.</p>
</li>
<li>
<p>Add your origin server as an endpoint with the following information:</p>
</li>
</ol>
<ul>
<li>A name for the endpoint (must be unique). Suggestion: <code>my-website</code>.</li>
<li>The endpoint IP address or hostname.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10369.md")
</aside>
<ul>
<li>The endpoint <a href="/load-balancing/understand-basics/traffic-steering/origin-level-steering/#weights">weight</a>, which can be set to <code>1</code>. Since each pool will only have one endpoint, the endpoint weight will not make a difference in this case.</li>
<li>A <a href="/load-balancing/additional-options/override-http-host-headers/">hostname</a> by selecting <strong>Add host header</strong>.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10368.md")
</aside>
<ol start="6">
<li>Finish configuring the first pool with the following information:</li>
</ol>
<ul>
<li>Leave the <strong>Health Threshold</strong> set to <code>1</code>. Since each pool will only have one endpoint, this is the only possible value for this field.</li>
<li>Select the <strong>Monitor</strong> configured in the previous step.</li>
<li>Select <strong>Health Check Regions</strong> to choose from which <a href="/load-balancing/monitors/#health-monitor-regions">locations</a> Cloudflare should send monitor requests to periodically test the endpoint health.</li>
</ul>
<ol start="7">
<li>
<p>Select <strong>Save</strong></p>
</li>
<li>
<p>Repeat the process for the second pool using the following values:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Field</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pool name</td>
<td><code>secondary</code></td>
</tr>
<tr>
<td>Description</td>
<td><code>Pages version</code></td>
</tr>
<tr>
<td>Endpoint steering</td>
<td><code>&lt;default&gt;</code></td>
</tr>
<tr>
<td>Endpoint name</td>
<td><code>my-pages-website</code></td>
</tr>
<tr>
<td>Endpoint address</td>
<td><code>&lt;your custom domain or Pages subdomain&gt;</code></td>
</tr>
<tr>
<td>Weight</td>
<td><code>1</code></td>
</tr>
<tr>
<td>Host (<strong>Add host header</strong>)</td>
<td><code>&lt;your custom domain or Pages subdomain&gt;</code></td>
</tr>
<tr>
<td>Health threshold</td>
<td><code>1</code></td>
</tr>
<tr>
<td>Monitor</td>
<td><code>&lt;monitor defined on previous step&gt;</code></td>
</tr>
<tr>
<td>Health check regions</td>
<td><code>&lt;select region of your choice&gt;</code></td>
</tr>
</tbody>
</table>
<h2 id="check-the-endpoints-health-status">Check the endpoints health status</h2>
<p>Before setting up the load balancer:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Load Balancing</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol>
<li>Go to the <strong>Pools</strong> tab.</li>
<li>Find the pools you created in the list and check if their status is <code>Healthy</code>. You might have to refresh the page.</li>
<li>Expand each pool entry to confirm that the health status for endpoints within them is also <code>Healthy</code>.</li>
</ol>
<p>The basic principle is that, if both your production website and your Cloudflare Pages project are live and directly accessible via browser, the monitors should also be able to get a <code>200</code> code as HTTP response.</p>
<p>Revise your pools and monitor configurations to confirm they followed the instructions above. If you still find issues, refer to <a href="/load-balancing/troubleshooting/common-error-codes/">Troubleshooting</a> or <a href="/load-balancing/troubleshooting/load-balancing-faq/#why-is-my-endpoint-or-pool-considered-unhealthy">FAQ</a>.</p>
<h2 id="create-load-balancer">Create load balancer</h2>
<p>After confirming the endpoints and monitors are set up correctly and return the expected health status, create the load balancer:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Load Balancing</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Create load balancer</strong>.</p>
</li>
<li>
<p>On the <strong>Hostname</strong> page, configure the following and select <strong>Next</strong>.</p>
<ul>
<li>Enter a <strong>Hostname</strong>, which is the DNS name at which the load balancer is available. Suggestion: for now, you can just add a temporary hostname such as <code>lb</code> (so the complete field value would look like <code>lb.&lt;your_domain&gt;</code>).</li>
<li>Toggle the orange cloud icon to update the <a href="/load-balancing/understand-basics/proxy-modes/">proxy mode</a>, which affects how traffic is routed and which IP addresses are advertised.</li>
<li>Select your preferred option for <a href="/load-balancing/understand-basics/session-affinity/">session affinity</a> and <a href="/load-balancing/understand-basics/adaptive-routing/">adaptive routing</a>.</li>
</ul>
</li>
<li>
<p>On the <strong>Add a Pool</strong> page, configure the following and select <strong>Next</strong>.</p>
<ul>
<li>Select the first pool you created previously and select <strong>Add Pool</strong>.</li>
<li>Do the same for the second pool and reorder them if needed. For the purposes of this tutorial, your production website pool would be the first (<code>primary</code>) and the Cloudflare Pages pool would be the second (<code>secondary</code>).</li>
<li>If needed, update the <a href="/load-balancing/understand-basics/health-details/#fallback-pools"><strong>Fallback Pool</strong></a>. For the purposes of this tutorial, you can leave this pointing to your secondary pool.</li>
</ul>
</li>
<li>
<p>On the <strong>Monitors</strong> page, review the monitors attached to your pools and the expected health status, and select <strong>Next</strong>.</p>
</li>
<li>
<p>On the <strong>Traffic Steering</strong> page, make sure <strong>Off</strong> is selected. This means the load balancer will follow the order established on the <strong>Add a Pool</strong> section (Step 3 above), achieving an <a href="/load-balancing/load-balancers/common-configurations/#active---passive-failover">Active - Passive Failover</a> configuration.</p>
</li>
<li>
<p>For the purposes of this tutorial, leave the <a href="/load-balancing/additional-options/load-balancing-rules/"><strong>Custom Rules</strong></a> option empty.</p>
</li>
<li>
<p>On the <strong>Review</strong> page, review your configuration and select <strong>Save as Draft</strong>.</p>
</li>
</ol>
<p>A DNS record of the type <code>LB</code> will be created under <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS</strong> &gt; <strong>Records</strong></a> with the hostname you have defined, and a corresponding load balancer will be added to <a href="https://dash.cloudflare.com/?to=/:account/load-balancing"><strong>Load Balancing</strong></a></p>
<h2 id="optional-deploy-on-a-test-hostname">Optional - Deploy on a test hostname</h2>
<p>If you have used a temporary hostname for your load balancer, follow the steps below to deploy and test it.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Load Balancing</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>In the <strong>Load Balancers</strong> list, locate the load balancer you created under a test hostname (such as <code>lb</code>) and enable it.</p>
</li>
<li>
<p>On your browser, request the temporary hostname (<code>lb.example.com</code>). You should see the website or application hosted at your primary origin server.</p>
</li>
<li>
<p>Go back to the <strong>Manage Load Balancers</strong> list, select to expand the test load balancer, and disable the primary pool.</p>
</li>
<li>
<p>On a new incognito window of your browser, request the temporary hostname once again. You should see the website or application hosted at your secondary origin server this time.</p>
<p>If you find issues, revise your pools, monitor, and load balancer configurations to confirm they followed the instructions above. Also refer to <a href="/load-balancing/troubleshooting/common-error-codes/">Troubleshooting</a> or <a href="/load-balancing/troubleshooting/load-balancing-faq/">FAQ</a> if needed.</p>
</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important-1">Important</h3>
@markup("md", "content/.markup/bodies/10367.md")
</aside>
<h2 id="route-production-traffic-to-load-balancer">Route production traffic to load balancer</h2>
<p>Now that you have set up your load balancer and verified everything is working correctly, you can put the load balancer on a live domain or subdomain:</p>
<ol>
<li>
<p>Confirm that your production hostname has the correct <a href="/load-balancing/load-balancers/dns-records/#priority-order">priority order</a> of DNS records and is covered by an <a href="/load-balancing/load-balancers/dns-records/#ssltls-coverage">SSL/TLS certificate</a>.</p>
<p>If you have an Enterprise account, also evaluate your application for any excluded paths. For example, you might not want the load balancer to distribute requests directed at your <code>/admin</code> path. For any exceptions, set up an <a href="/rules/origin-rules/features/#dns-record">Origin rule</a>.</p>
</li>
<li>
<p>Configure your load balancer to receive production traffic by editing the <strong>Hostname</strong> of your existing load balancer.</p>
</li>
</ol>
