<p>Cloudflare's threat intelligence team crowdsources attack trends and protects users automatically, such as from zero-day vulnerabilities like the <a href="https://blog.cloudflare.com/technical-breakdown-http2-rapid-reset-ddos-attack/">HTTP/2 Rapid Reset attack</a>. However, in some cases, Cloudflare will partner with external entities that have their own feeds which can be shared with eligible Cloudflare users.</p>
<p>With Custom Indicator Feeds, Cloudflare provides a threat intelligence feed based on data received from various Cyber Defense Collaboration groups. The security filtering capabilities are available to eligible public and private sector organizations.</p>
<h2 id="publicly-available-feeds">Publicly available feeds</h2>
<p>Cloudflare provides some feeds to Gateway users without the need to establish a provider relationship.</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Availability</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://www.cloudflare.com/press-releases/2024/us-department-of-treasury-pnnl-finserv-threat-intel-feed/">Treasury Early Indicator Feed</a>, Feed ID 14</td>
<td>Threat data for financial institutions provided by the US Department of Treasury and Pacific Northwest National Laboratory (PNNL). For more information, contact your account team.</td>
<td>Approved financial services organizations</td>
</tr>
<tr>
<td><a href="https://www.ncsc.gov.uk/information/pdns">UK NCSC Public Threat Indicators</a> Feed ID 24</td>
<td>Recursive DNS service supplied by the UK National Cyber Security Centre (NCSC) to block DNS-based malware.</td>
<td>All users</td>
</tr>
<tr>
<td>Cloudforce One - Public Feed Feed ID 34</td>
<td>Feed of indicators.</td>
<td>All users</td>
</tr>
</tbody>
</table>
<h2 id="get-started">Get started</h2>
<p>Cloudflare threat intelligence data consists of a data exchange between providers and subscribers.</p>
<p>A provider is an organization that has a set of data that they are interested in sharing with other Cloudflare organizations. Any organization can be a provider. Examples of current providers are Government Cyber Defense groups.</p>
<p>Subscribers can be any Cloudflare customer that wants to secure their environment further by creating rules based on provider datasets. Subscribers must be authorized by a provider. Authorization is granted using the <a href="/api/resources/intel/subresources/indicator_feeds/subresources/permissions/methods/create/">Grant permission to indicator feed endpoint</a>.</p>
<p>If your organization is interested in becoming a provider or a subscriber, contact your account team.</p>
<h3 id="create-a-custom-indicator-feed">Create a Custom Indicator Feed</h3>
<p>Providers can create and manage a Custom Indicator Feed with the <a href="/api/resources/intel/subresources/indicator_feeds/methods/list/">Custom Indicator Feeds API endpoints</a>:</p>
<ol>
<li>Contact your account team to configure your account as an indicator feed provider.</li>
<li>Create a feed with the <a href="/api/resources/intel/subresources/indicator_feeds/methods/create/">Create new indicator feed endpoint</a>. Make note of the <code>feed_id</code> generated for your feed. For example:</li>
</ol>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/intel/indicator-feeds&quot; \&#10;	&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;	&#45;-header &#x27;X-Auth-Email: &lt;EMAIL&gt;&#x27; \&#10;	&#45;-header &#x27;X-Auth-Key: &lt;API_KEY&gt;&#x27; \&#10;	&#45;-data &#x27;{&#10;	&quot;description&quot;: &quot;Custom indicator feed to detect threats&quot;,&#10;	&quot;name&quot;: &quot;threat_indicator_feed&quot;&#10;}&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: 10,&#10;		&quot;name&quot;: &quot;threat_indicator_feed&quot;,&#10;		&quot;description&quot;: &quot;Custom indicator feed to detect threats&quot;,&#10;		&quot;created_on&quot;: &quot;2024-09-17T21:16:09.412Z&quot;,&#10;		&quot;modified_on&quot;: &quot;2024-09-17T21:16:09.412Z&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<ol start="3">
<li>Upload data to the feed with the <a href="/api/resources/intel/subresources/indicator_feeds/subresources/snapshots/methods/update/">Update indicator feed data endpoint</a>. Uploaded indicator data must be in a <a href="https://oasis-open.github.io/cti-documentation/stix/intro"><code>.stix2</code></a> formatted file. The <a href="/r2/platform/limits/">maximum upload file size</a> is 4.995 GiB.</li>
</ol>
<pre><code class="language-bash">curl --request PUT \&#10;	&quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/intel/indicator-feeds/&lt;FEED_ID&gt;/snapshot&quot; \&#10;	&#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;	&#45;-header &#x27;X-Auth-Email: &lt;EMAIL&gt;&#x27; \&#10;	&#45;-header &#x27;X-Auth-Key: &lt;API_KEY&gt;&#x27; \&#10;	&#45;-form &#x27;source=@/path/to/file&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;file_id&quot;: 1,&#10;		&quot;filename&quot;: &quot;snapshot_file.unified&quot;,&#10;		&quot;status&quot;: &quot;unified&quot;&#10;	},&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;success&quot;: true&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/371.md")
</aside>
<ol start="4">
<li>(Optional) Verify the status of your feed upload with the <a href="/api/resources/intel/subresources/indicator_feeds/methods/data/">Get indicator feed data endpoint</a>. For example:</li>
</ol>
<pre><code class="language-bash">curl --request GET \&#10;	&quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/intel/indicator-feeds/&lt;FEED_ID&gt;/data&quot; \&#10;	&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;	&#45;-header &#x27;X-Auth-Email: &lt;EMAIL&gt;&#x27; \&#10;	&#45;-header &#x27;X-Auth-Key: &lt;API_KEY&gt;&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: 10,&#10;		&quot;name&quot;: &quot;threat_indicator_feed&quot;,&#10;		&quot;description&quot;: &quot;Custom indicator feed to detect threats&quot;,&#10;		&quot;created_on&quot;: &quot;2023-08-01T18:00:26.65715Z&quot;,&#10;		&quot;modified_on&quot;: &quot;2023-08-01T18:00:26.65715Z&quot;,&#10;		&quot;latest_upload_status&quot;: &quot;Complete&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<ol start="5">
<li>Grant access to subscribers with the <a href="/api/resources/intel/subresources/indicator_feeds/subresources/permissions/methods/create/">Grant permission to indicator feed endpoint</a>. You can add subscribers to the feed's allowed subscribers list using their <a href="/fundamentals/account/find-account-and-zone-ids/">account IDs</a>. For example:</li>
</ol>
<pre><code class="language-bash">curl --request PUT \&#10;	&quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/intel/indicator-feeds/&lt;FEED_ID&gt;/snapshot&quot; \&#10;	&#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;	&#45;-header &#x27;X-Auth-Email: &lt;EMAIL&gt;&#x27; \&#10;	&#45;-header &#x27;X-Auth-Key: &lt;API_KEY&gt;&#x27; \&#10;	&#45;-data &#x27;{&#10;	&quot;account_tag&quot;: &quot;823f45f16fd2f7e21e1e054aga4d2859&quot;,&#10;	&quot;feed_id&quot;: 10&#10;}&#x27;&#10;</code></pre>
<h3 id="use-a-feed-in-gateway">Use a feed in Gateway</h3>
<p>Once an account is granted access to a feed, it will be available to match traffic as a <a href="/cloudflare-one/traffic-policies/dns-policies/#indicator-feeds">selector in Gateway DNS policies</a>.</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong>. Select <strong>DNS</strong>.</li>
<li>To create a new DNS policy, select <strong>Add a policy</strong>.</li>
<li>Name your policy.</li>
<li>In <strong>Traffic</strong>, add a condition with the <strong>Indicator Feeds</strong> selector. If your account has been granted access to a Custom Indicator Feed, Gateway will list the feed in <strong>Value</strong>. For example, you can block sites that appear in a feed:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Indicator Feeds</td>
<td>in</td>
<td><em>Threat Intel Feed</em></td>
<td>Block</td>
</tr>
</tbody>
</table>
<ol start="5">
<li>Select <strong>Create policy</strong>.</li>
</ol>
<p>For more information on creating Gateway policies, refer to <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policies</a>.</p>
