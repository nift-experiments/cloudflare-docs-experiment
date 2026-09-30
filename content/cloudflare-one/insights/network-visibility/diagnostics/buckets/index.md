<p>Before you can begin a full <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5014.md")
</div> capture, you must configure a cloud storage bucket where Cloudflare can write the captured traffic data. Setting up a bucket is not required for sample packet captures, which complete immediately and can be downloaded directly from the API.
<p>You can configure an Amazon S3 or Google Cloud Platform bucket to use as a target. You can also <a href="#r2">use R2</a> as a target using the API.</p>
<h2 id="set-up-a-bucket">Set up a bucket</h2>
<p>Learn how to set up a bucket for use with full packet captures.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5017.md")
</div></div>
<p>Next, validate the bucket and confirm ownership.</p>
<h2 id="validate-a-bucket">Validate a bucket</h2>
<p>After the initial bucket setup, you need to confirm you have access to the bucket via an ownership challenge. This verification prevents Cloudflare from writing capture data to a bucket you do not control. After you validate your bucket, you can begin using it to collect full packet captures.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5020.md")
</div></div>
<p>The bucket status displays one of the following options:</p>
<ul>
<li><strong>Success:</strong> The bucket is fully verified and ready to use.</li>
<li><strong>Pending:</strong> The challenge response was initiated but is pending verification. Bucket verification can take five to ten minutes to finish processing.</li>
<li><strong>Failed:</strong> The bucket could not be validated. If this occurs, verify that Cloudflare has write access to your bucket and that you submitted the correct contents of the ownership challenge file.</li>
</ul>
<h2 id="list-configured-buckets">List configured buckets</h2>
<p>View a list of all buckets configured on your account.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5023.md")
</div></div>
<p>To learn how to collect packet captures, refer to <a href="/cloudflare-network-firewall/packet-captures/collect-pcaps/">Collect packet captures</a>.</p>
<h2 id="r2">R2</h2>
<p>You can also use <a href="/r2/">Cloudflare R2</a> as a storage destination for packet captures. R2 bucket configuration is available through the API only.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5013.md")
</aside>
<h3 id="create-bucket-and-api-token">Create bucket and API token</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create bucket</strong>.</li>
<li>Give your bucket a name &gt; <strong>Create bucket</strong>.</li>
<li>Go to the R2 Overview page, and select <strong>Manage R2 API Tokens</strong>.</li>
<li>Select <strong>Create API Token</strong>.</li>
<li>In <strong>Permissions</strong>, choose <strong>Object Read &amp; Write</strong>. Make sure you also select <strong>Apply to specific buckets only</strong>, and select the bucket you have created for PCAPs from the drop-down menu.</li>
<li>Select <strong>Create API Token</strong>.</li>
<li>Make sure you copy the <strong>Secret Access Key</strong> and <strong>Access Key ID</strong> values, as you will need them for the next step.</li>
</ol>
<h3 id="create-initial-request">Create initial request</h3>
<p>Create your initial request to R2:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/pcaps/ownership \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;destination_conf&quot;: &quot;r2://&lt;BUCKET_NAME&gt;?account-id=&lt;ACCOUNT_ID&gt;&amp;access-key-id=&lt;R2_ACCESS_KEY_ID&gt;&amp;secret-access-key=&lt;R2_SECRET_ACCESS_KEY&gt;&quot;&#10;}&#x27;&#10;</code></pre>
<p>The <a href="/api/resources/magic_transit/subresources/pcaps/subresources/ownership/methods/create/">response</a> has a <code>&quot;filename&quot;</code> parameter with the name of a file that Cloudflare wrote to your R2 bucket. You need to download it for the next step. Example:</p>
<pre><code class="language-json">{&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [],&#10;	&quot;result&quot;: {&#10;		&quot;destination_conf&quot;: &quot;&lt;YOUR_R2_BUCKET&gt;&quot;,&#10;		&quot;filename&quot;: &quot;ownership-challenge-9883874ecac311ec8475433579a6bf5f.txt&quot;,&#10;		&quot;id&quot;: &quot;9883874ecac311ec8475433579a6bf5f&quot;,&#10;		&quot;status&quot;: &quot;success&quot;,&#10;		&quot;submitted&quot;: &quot;2020-01-01T08:00:00Z&quot;,&#10;		&quot;validated&quot;: &quot;2020-01-01T08:00:00Z&quot;&#10;	},&#10;	&quot;success&quot;: true&#10;}&#10;</code></pre>
<h3 id="validate-bucket-ownership">Validate bucket ownership</h3>
<p>Refer to the <a href="#validate-a-bucket">Validate a bucket</a> API instructions for more details on the entire process to <a href="/api/resources/magic_transit/subresources/pcaps/subresources/ownership/methods/validate/">validate your R2 bucket</a>. When specifying the R2 destination for this validation, exclude the secret and access keys from the URL.</p>
