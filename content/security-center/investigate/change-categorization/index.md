<p>Cloudflare sorts domains into categories based on their content and security type. You can request categorization changes via the <a href="#via-the-cloudflare-dashboard">dashboard</a>, <a href="#via-cloudflare-radar">Cloudflare Radar</a>, or the <a href="#via-the-api">API</a>.</p>
<p>For a detailed list of categories, refer to <a href="/cloudflare-one/traffic-policies/domain-categories/">Domain categories</a>.</p>
<h2 id="via-the-cloudflare-dashboard">Via the Cloudflare dashboard</h2>
<p>To request a categorization change via the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Investigate</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Search for the domain you want to change.</p>
</li>
<li>
<p>In <strong>Domain overview</strong>, select <strong>Request to change categorization</strong>.</p>
</li>
<li>
<p>Choose whether to change a <a href="/cloudflare-one/traffic-policies/domain-categories/#security-categories">security category</a> or a <a href="/cloudflare-one/traffic-policies/domain-categories/#content-categories">content category</a>.</p>
</li>
<li>
<p>Choose which categories you want to add or remove from the domain.</p>
</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="content-category-limit">Content category limit</h3>
@markup("md", "content/.markup/bodies/13811.md")
</aside>
<ol start="6">
<li>Select <strong>Submit</strong> to submit your request for review.</li>
</ol>
<p>Requesting a security category change will trigger a deeper investigation by Cloudflare to confirm that the submission is valid. Requesting a content category change also requires Cloudflare validation, but the turnaround time for these submissions is usually shorter as it requires less investigation.</p>
<p>Your category change requests will be revised by the Cloudflare team depending on the type of change. If your requests have been reviewed and applied by the Cloudflare team, the new categories will be visible in the Cloudflare dashboard in <strong>Security Center</strong> &gt; <strong>Investigate</strong>, as well as in <a href="https://radar.cloudflare.com/">Cloudflare Radar</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13810.md")
</aside>
<h2 id="via-cloudflare-radar">Via Cloudflare Radar</h2>
<p>To request recategorization via Cloudflare Radar, submit feedback in <a href="https://radar.cloudflare.com/domains/feedback">Radar Domain Categorization</a>.</p>
<h2 id="via-the-api">Via the API</h2>
<p>To request a categorization change via the API:</p>
<ol>
<li><a href="/fundamentals/api/get-started/create-token/">Create an API token</a> with permission to edit your Intel account.</li>
</ol>
<table>
<thead>
<tr>
<th><strong>Permissions</strong></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Account</td>
<td>Intel</td>
<td>Edit</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th><strong>Account Resources</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Include</td>
<td>All accounts</td>
</tr>
</tbody>
</table>
<ol start="2">
<li>Make a call to the <a href="/api/resources/intel/subresources/miscategorizations/methods/create/">miscategorization endpoint</a> including the domain name and any categories you would like to add or remove. For example:</li>
</ol>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/intel/miscategorization \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;content_adds&quot;: [&#10;    82&#10;  ],&#10;  &quot;content_removes&quot;: [&#10;    155&#10;  ],&#10;  &quot;indicator_type&quot;: &quot;domain&quot;,&#10;  &quot;ip&quot;: null,&#10;  &quot;security_adds&quot;: [&#10;    117,&#10;    131&#10;  ],&#10;  &quot;security_removes&quot;: [&#10;    83&#10;  ],&#10;  &quot;url&quot;: &quot;example.com&quot;&#10;}&#x27;&#10;</code></pre>
