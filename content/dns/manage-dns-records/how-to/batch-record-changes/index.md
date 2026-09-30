<p>Cloudflare allows you to apply several changes to your zone records in just one action. You can <a href="#use-the-dashboard">use the dashboard</a> to delete DNS records or update their <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7860.md")
</div> in bulk, or [use the API](#use-the-api) to perform further batched operations.
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="propagation-through-the-cloudflare-network">Propagation through the Cloudflare network</h3>
@markup("md", "content/.markup/bodies/7859.md")
</aside>
<h2 id="availability-and-limits">Availability and limits</h2>
<p>Batch DNS record changes is available on all plans.</p>
<p>The number of records that you can operate with in one action depends on your zone plan:</p>
<ul>
<li>Free: 200</li>
<li>Pro: 3,500</li>
<li>Business: 3,500</li>
<li>Enterprise: 3,500</li>
</ul>
<hr />
<h2 id="use-the-dashboard">Use the dashboard</h2>
<h3 id="edit-proxy-status-in-bulk">Edit proxy status in bulk</h3>
<p><code>A</code>,<code>AAAA</code>, and <code>CNAME</code> records can be <a href="/dns/proxy-status/">proxied</a>. The <strong>Proxy status</strong> of a DNS record affects <a href="/fundamentals/concepts/how-cloudflare-works/">how Cloudflare responds to DNS queries</a> to that record.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7858.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>DNS Records</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the DNS records you want to set the proxy status for. Note that only <code>A</code>, <code>AAAA</code>, and <code>CNAME</code> records can be proxied.</li>
<li>Select <strong>Edit records</strong>.</li>
<li>Choose the proxy status you want to apply to the selected records.</li>
<li>Select <strong>Save</strong> to confirm.</li>
</ol>
<p>You can only set records to either <strong>Proxied</strong> or <strong>DNS only</strong> in bulk. This means that if your selection includes both proxied and DNS-only records, some of them will have the proxy status updated while others will keep their original value:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/7861.md")
</div>
<h3 id="delete-records-in-bulk">Delete records in bulk</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7857.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>DNS Records</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the DNS records you want to delete.</li>
<li>Select <strong>Delete records</strong>.</li>
<li>In the <strong>Delete DNS records</strong> prompt, type in <code>DELETE</code> and select <strong>Delete</strong> to confirm.</li>
</ol>
<h2 id="use-the-api">Use the API</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7856.md")
</aside>
<p>The <a href="/api/resources/dns/subresources/records/methods/batch/">Batched DNS record changes</a> endpoint allows you to trigger the execution of <code>DELETES</code>, <code>PATCHES</code>, <code>PUTS</code>, and <code>POSTS</code> in a single request.</p>
<p><a href="/dns/manage-dns-records/reference/record-attributes/">Tags and comments</a> are also supported with batch changes.</p>
<p>The operations you specify within the <code>/batch</code> request body are always executed in the following order:</p>
<ol>
<li>Deletes</li>
<li>Patches</li>
<li>Puts</li>
<li>Posts</li>
</ol>
<p>Within each of these four lists, each individual action is executed following the DNS records order you provide. If any of the individual action fails, no changes are applied and the API returns the first error it encountered.</p>
<h3 id="aspects-to-consider">Aspects to consider</h3>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="propagation-through-the-cloudflare-network-1">Propagation through the Cloudflare network</h3>
@markup("md", "content/.markup/bodies/7855.md")
</aside>
<p>For each operation that you list in the <code>/batch</code> request body, consider the required information and how unspecified fields will behave:</p>
<ul>
<li><strong><code>deletes</code></strong>: only the <code>id</code> is required for each record object. You can keep additional parameters such as <code>name</code> for readability, but any other fields aside from <code>id</code> will be ignored in this case.</li>
<li><strong><code>patches</code></strong>: aside from each record <code>id</code>, you should specify the fields you want to update. All unspecified fields will remain as they are.</li>
<li><strong><code>puts</code></strong>: you must specify each record <code>id</code>, <code>content</code>, <code>name</code>, and <code>type</code>. You should also specify any other fields you want to set to a value that is not the default. Any unspecified fields will assume their default value for each <a href="/dns/manage-dns-records/reference/dns-record-types/">record type</a>. This operation works as an overwrite, so all fields in a given record are always affected.</li>
<li><strong><code>posts</code></strong>: since you are creating a new record, <code>id</code> is not required. For field definitions, refer to the <a href="/api/resources/dns/subresources/records/methods/create/">Create DNS Record</a> endpoint and select the desired record type under the request body specification.</li>
</ul>
<h3 id="example-request">Example request</h3>
<p>In this example, the <code>proxied</code> field for the first record listed under <code>&quot;puts&quot;</code> will assume the default value (<code>false</code>).</p>
<pre><code class="language-bash">{&#10;    &quot;deletes&quot;: [&#10;        {&#10;            &quot;id&quot;: &quot;2bff0ebc4df64beaa44b0dca93e37a28&quot;&#10;        },&#10;        {&#10;            &quot;id&quot;: &quot;31d1d6e79ce04b8d93cbc5a13401d728&quot;&#10;        }&#10;    ],&#10;    &quot;patches&quot;: [&#10;        {&#10;            &quot;id&quot;: &quot;62276440f783445380480484648c1017&quot;,&#10;            &quot;content&quot;: &quot;192.0.2.46&quot;&#10;        },&#10;        {&#10;            &quot;id&quot;: &quot;c942d948dc2343b9b97aed78479c9fb9&quot;,&#10;            &quot;name&quot;: &quot;update.example.com&quot;,&#10;            &quot;proxied&quot;: true&#10;        }&#10;    ],&#10;    &quot;puts&quot;: [&#10;        {&#10;            &quot;id&quot;: &quot;a50364543094428abde0f14061d42b0e&quot;,&#10;            &quot;content&quot;: &quot;192.0.2.50&quot;,&#10;            &quot;name&quot;: &quot;change.example.com&quot;,&#10;						&quot;type&quot;: &quot;A&quot;,&#10;            &quot;ttl:&quot;: 1&#10;        },&#10;        {&#10;            &quot;id&quot;: &quot;3bce0920f19d43949498bd067b05dfa9&quot;,&#10;            &quot;content&quot;: &quot;192.0.2.45&quot;,&#10;            &quot;name&quot;: &quot;no-change.example.com&quot;,&#10;						&quot;type&quot;: &quot;A&quot;,&#10;            &quot;proxied&quot;: false,&#10;            &quot;ttl:&quot;: 3000&#10;        }&#10;    ],&#10;    &quot;posts&quot;: [&#10;        {&#10;            &quot;name&quot;: &quot;@&quot;,&#10;            &quot;type&quot;: &quot;A&quot;,&#10;            &quot;content&quot;: &quot;192.0.2.41&quot;,&#10;            &quot;proxied&quot;: false,&#10;            &quot;ttl&quot;: 3000&#10;        },&#10;        {&#10;            &quot;name&quot;: &quot;a.example.com&quot;,&#10;            &quot;type&quot;: &quot;A&quot;,&#10;            &quot;content&quot;: &quot;192.0.2.42&quot;,&#10;            &quot;proxied&quot;: true&#10;        }&#10;    ]&#10;}&#10;</code></pre>
