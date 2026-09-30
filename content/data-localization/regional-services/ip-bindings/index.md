<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7422.md")
</aside>
<p>Regionalized IP Bindings let you regionalize traffic at the IP layer for prefixes you bring to Cloudflare through <a href="/byoip/">Bring Your Own IP (BYOIP)</a>. You bind a CIDR from one of your prefixes to a region, and Cloudflare processes traffic destined for those IP addresses only within the data centers in that region.</p>
<p>This complements the other ways to use <a href="/data-localization/regional-services/">Regional Services</a>: where <a href="/data-localization/regional-services/regional-hostnames/">Regional Hostnames</a> regionalize traffic by hostname, Regionalized IP Bindings regionalize traffic by IP prefix — ideal for address-map deployments and any service you address by IP rather than hostname. Because bindings are managed entirely through the API, you can regionalize broad configurations yourself once your entitlements are enabled, without per-zone setup from your account team.</p>
<h2 id="how-it-works">How it works</h2>
<p>A prefix binding maps a CIDR (within a BYOIP prefix you own) to a <a href="#list-available-regions">region key</a> (for example, <code>us</code> or <code>eu</code>). After Cloudflare provisions the binding, traffic to addresses in that CIDR terminates TLS and is processed only inside the configured region, following the same in-region processing model described in <a href="/data-localization/regional-services/">Regional Services</a>.</p>
<p>Bindings are managed through the Data Localization Suite API under <code>/accounts/{account_id}/dls/</code>.</p>
<h2 id="choose-which-cidr-to-bind">Choose which CIDR to bind</h2>
<p>A binding covers a range of addresses within a prefix, not just a single address — you do <strong>not</strong> need to create one binding per IP address. The <code>cidr</code> you bind must:</p>
<ul>
<li>Fall within the prefix identified by <code>prefix_id</code>.</li>
<li>Contain only unused IP addresses. Binding IP addresses that are already in use interrupts their traffic while the change propagates.</li>
<li>Be <strong>more specific than the prefix itself</strong> — a sub-range within it. For example, within a <code>/24</code> prefix you can bind any range from a <code>/25</code> down to a single address (a <code>/32</code> for IPv4, or a <code>/128</code> for IPv6). Binding the entire prefix (the full <code>/24</code>) is rejected with a <a href="#handle-a-conflict-error">conflict error</a>, because the whole prefix range is already in use once Cloudflare advertises it.</li>
</ul>
<p>How you choose the CIDR depends on how you want to split the prefix across regions:</p>
<ul>
<li><strong>One region for the whole prefix</strong> — cover the prefix with sub-ranges that all point to the same region. For example, bind both <code>203.0.113.0/25</code> and <code>203.0.113.128/25</code> to <code>eu</code> to regionalize every address in a <code>/24</code>.</li>
<li><strong>Different regions for different addresses</strong> — bind each range to the region you want (for example, <code>203.0.113.0/25</code> to <code>eu</code> and <code>203.0.113.128/25</code> to <code>us</code>). Cloudflare applies the most specific binding that matches a given address, so a narrower binding takes precedence over a broader one that overlaps it.</li>
</ul>
<p>A conflict occurs only when you try to create two bindings for the exact same CIDR. Bindings with overlapping but different CIDRs can coexist, and Cloudflare applies the most specific matching binding. To change the region for an existing CIDR, <a href="#update-the-region-for-a-binding">update its binding</a> instead of creating another one.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you create a binding, make sure that:</p>
<ul>
<li>Your account has both the <strong>Regional Services</strong> and <strong>Regional Services for BYOIP</strong> entitlements enabled. Contact your account team to enable them.</li>
<li>You have <a href="/byoip/">onboarded a BYOIP prefix</a> to Cloudflare and know its prefix ID.</li>
<li>The region you want to use exists for your account. Refer to <a href="#list-available-regions">List available regions</a>.</li>
<li>Your <a href="/fundamentals/api/get-started/create-token/">API token</a> has the required permissions. Refer to <a href="#required-api-token-permissions">Required API token permissions</a>.</li>
</ul>
<h2 id="required-api-token-permissions">Required API token permissions</h2>
<p>These endpoints are authorized at the account level. The permissions you need depend on the operation:</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Required token permissions</th>
</tr>
</thead>
<tbody>
<tr>
<td>List regions, get a region, list or get bindings</td>
<td><strong>DLS: Read</strong></td>
</tr>
<tr>
<td>Create, update, or delete a prefix binding</td>
<td><strong>DLS: Write</strong> <em>and</em> <strong>IP Prefixes: Write</strong></td>
</tr>
</tbody>
</table>
<p>Write operations require <strong>IP Prefixes: Write</strong> in addition to <strong>DLS: Write</strong> because the binding is created against a BYOIP prefix that you own in <a href="/byoip/">Addressing</a> — Cloudflare verifies that you have permission to modify that prefix. A token with only <strong>DLS: Write</strong> can read regions and bindings but will be rejected when it tries to create or change a binding.</p>
<p>The <strong>Super Administrator</strong> and <strong>Administrator</strong> roles include all of these permissions. A custom role works as long as it includes the permission groups above.</p>
<h2 id="list-available-regions">List available regions</h2>
<p>Each binding references a region by its <code>region_key</code> (for example, <code>us</code> or <code>eu</code>). List the regions available to your account to find a valid key.</p>
<pre><code class="language-bash">curl --request GET --url https://api.cloudflare.com/client/v4/accounts/{account_id}/dls/regions</code></pre>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;a1b2c3d4-e5f6-7890-abcd-ef1234567890&quot;,&#10;			&quot;name&quot;: &quot;Europe&quot;,&#10;			&quot;region_key&quot;: &quot;eu&quot;,&#10;			&quot;created_on&quot;: &quot;2026-01-13T23:59:45.276558Z&quot;,&#10;			&quot;modified_on&quot;: &quot;2026-01-13T23:59:45.276558Z&quot;,&#10;			&quot;version&quot;: 1,&#10;			&quot;version_created_on&quot;: &quot;2026-01-13T23:59:45.276558Z&quot;&#10;		}&#10;	],&#10;	&quot;result_info&quot;: {&#10;		&quot;count&quot;: 1,&#10;		&quot;per_page&quot;: 25,&#10;		&quot;cursor&quot;: &quot;&quot;&#10;	}&#10;}&#10;</code></pre>
<p>Use the <code>type</code> query parameter (<code>managed</code> or <code>custom</code>) to filter the results by <a href="/data-localization/region-support/#region-types">region type</a>. Results are paginated — pass the <code>cursor</code> value from a response to fetch the next page.</p>
<details class="nb-details"><summary>Get a single region</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7423.md")
</div></details>
<h2 id="create-a-prefix-binding">Create a prefix binding</h2>
<p>Bind a CIDR from one of your BYOIP prefixes to a region. The <code>cidr</code> must fall within the prefix identified by <code>prefix_id</code> and be <a href="#choose-which-cidr-to-bind">more specific than the prefix itself</a>.</p>
<pre><code class="language-bash">curl --request POST --url https://api.cloudflare.com/client/v4/accounts/{account_id}/dls/regional_services/prefix_bindings</code></pre>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;f0e1d2c3-b4a5-6789-0abc-def123456789&quot;,&#10;		&quot;prefix_id&quot;: &quot;a1b2c3d4-e5f6-7890-abcd-ef1234567890&quot;,&#10;		&quot;cidr&quot;: &quot;203.0.113.0/25&quot;,&#10;		&quot;region_key&quot;: &quot;eu&quot;&#10;	}&#10;}&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="always-bind-unused-ip-addresses">Always bind unused IP addresses</h3>
@markup("md", "content/.markup/bodies/7421.md")
</aside>
<h3 id="check-binding-status">Check binding status</h3>
<p>Use the binding ID returned by the create request to call the <a href="/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/get/">Get service binding</a> endpoint. The Regionalized IP Bindings API and Service Bindings API use the same binding ID.</p>
<pre><code class="language-bash">curl --request GET --url https://api.cloudflare.com/client/v4/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}</code></pre>
<p>The binding is ready when <code>result.provisioning.state</code> is <code>active</code>:</p>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;f0e1d2c3-b4a5-6789-0abc-def123456789&quot;,&#10;		&quot;cidr&quot;: &quot;203.0.113.0/25&quot;,&#10;		&quot;provisioning&quot;: {&#10;			&quot;state&quot;: &quot;active&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="handle-a-conflict-error">Handle a conflict error</h3>
<p>Because <a href="#choose-which-cidr-to-bind">each CIDR can have only one binding</a>, a create request for a CIDR that is already bound fails with an HTTP <code>409</code> conflict:</p>
<pre><code class="language-json">{&#10;	&quot;result&quot;: null,&#10;	&quot;success&quot;: false,&#10;	&quot;errors&quot;: [&#10;		{&#10;			&quot;code&quot;: 1108,&#10;			&quot;message&quot;: &quot;conflict: binding already exists for CIDR 203.0.113.0/24&quot;&#10;		}&#10;	],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>You get this error in two cases:</p>
<ul>
<li><strong>You tried to bind the entire prefix.</strong> The full prefix range (for example, the whole <code>/24</code>) is already in use once Cloudflare advertises your prefix, so it cannot be bound to a region directly. Bind a more specific range within the prefix instead — a <code>/25</code> down to a single <code>/32</code> — and cover the prefix with several sub-ranges if you need to regionalize all of its addresses.</li>
<li><strong>The CIDR is already bound.</strong> A binding for that exact range already exists, for example from an earlier request that succeeded.</li>
</ul>
<p>To resolve it:</p>
<ul>
<li><a href="#list-prefix-bindings">List your existing bindings</a> to see what is already configured.</li>
<li>To move an existing binding to a different region, <a href="#update-the-region-for-a-binding">update it</a> rather than creating a new one.</li>
<li>To bind a different range, choose a CIDR that is not already bound. To replace an existing binding with a different CIDR, <a href="#delete-a-binding">delete it</a> first, then create the new one.</li>
</ul>
<h2 id="list-prefix-bindings">List prefix bindings</h2>
<pre><code class="language-bash">curl --request GET --url https://api.cloudflare.com/client/v4/accounts/{account_id}/dls/regional_services/prefix_bindings</code></pre>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;f0e1d2c3-b4a5-6789-0abc-def123456789&quot;,&#10;			&quot;prefix_id&quot;: &quot;a1b2c3d4-e5f6-7890-abcd-ef1234567890&quot;,&#10;			&quot;cidr&quot;: &quot;203.0.113.0/25&quot;,&#10;			&quot;region_key&quot;: &quot;eu&quot;&#10;		}&#10;	],&#10;	&quot;result_info&quot;: {&#10;		&quot;count&quot;: 1,&#10;		&quot;per_page&quot;: 25,&#10;		&quot;cursor&quot;: &quot;&quot;&#10;	}&#10;}&#10;</code></pre>
<details class="nb-details"><summary>Get a single binding</summary><div class="nb-details-body">
@input("content/.markup/bodies/7424.md")
</div></details>
<h2 id="update-the-region-for-a-binding">Update the region for a binding</h2>
<p>Change the region a binding points to. Only the <code>region_key</code> can be updated. To change the CIDR, delete the binding and create a new one.</p>
<pre><code class="language-bash">curl --request PATCH --url https://api.cloudflare.com/client/v4/accounts/{account_id}/dls/regional_services/prefix_bindings/{binding_id}</code></pre>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;f0e1d2c3-b4a5-6789-0abc-def123456789&quot;,&#10;		&quot;prefix_id&quot;: &quot;a1b2c3d4-e5f6-7890-abcd-ef1234567890&quot;,&#10;		&quot;cidr&quot;: &quot;203.0.113.0/25&quot;,&#10;		&quot;region_key&quot;: &quot;us&quot;&#10;	}&#10;}&#10;</code></pre>
<h2 id="delete-a-binding">Delete a binding</h2>
<p>Remove a binding to stop regionalizing traffic for its CIDR.</p>
<pre><code class="language-bash">curl --request DELETE --url https://api.cloudflare.com/client/v4/accounts/{account_id}/dls/regional_services/prefix_bindings/{binding_id}</code></pre>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result&quot;: null&#10;}&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/data-localization/regional-services/">Regional Services</a> — overview and in-region processing model.</li>
<li><a href="/data-localization/region-support/">Available regions and product support</a> — the full list of regions and their definitions.</li>
<li><a href="/byoip/">Bring Your Own IP (BYOIP)</a> — onboard your own IP prefixes to Cloudflare.</li>
</ul>
