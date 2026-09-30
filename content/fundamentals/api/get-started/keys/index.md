<p>Global API key is the previous authorization scheme for interacting with the Cloudflare API. When possible, use <a href="/fundamentals/api/get-started/create-token/">API tokens</a> instead of Global API key.</p>
<p>New and rolled Global API Keys use the <code>cfk_</code> prefixed <a href="/fundamentals/api/get-started/token-formats/">scannable format</a>, which allows credential scanning tools to detect leaked keys.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8999.md")
</aside>
<h2 id="limitations">Limitations</h2>
<p>Global API key has multiple limitations when compared to API tokens:</p>
<ul>
<li>
<p><strong>Access to all Cloudflare resources</strong> - Global API key has access to all of a user's resources. This makes it impossible to safely use Global API key to access non-production resources when a user also has access to production resources.</p>
</li>
<li>
<p><strong>Full permissions</strong> - Similarly, Global API key has the exact same permissions as the user, which means if the user can delete zones or change DNS records, so can the Global API key.</p>
</li>
<li>
<p><strong>Limited to one per user</strong> - Only one Global API key can be provisioned per user. This complicates using Cloudflare's API in production systems where maintaining two secrets for accessing the API is important in the case one needs to be rolled.</p>
</li>
<li>
<p><strong>Lack of advanced limits on usage</strong> - API tokens can be limited to specific time windows and expire or be limited to use from specific IP ranges.</p>
</li>
</ul>
<p>For these reasons, Global API key is not recommended for new customers. Current customers using Global API key are encouraged to migrate and use API tokens instead.</p>
<h2 id="view-your-global-api-key">View your Global API key</h2>
<p>To retrieve your Global API key:</p>
<ol>
<li>In the Cloudflare dashboard and select <strong>User Profile</strong> &gt; <strong>API Tokens</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In the <strong>API Keys</strong> section, click <code>View</code> button of <strong>Global API Key</strong>.</li>
</ol>
<h2 id="change-your-global-api-key">Change your Global API key</h2>
<p>If your API key might be compromised, change your API key:</p>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong>.</li>
<li>In the <strong>API Keys</strong> section, find your key.</li>
<li>Select <strong>Change</strong>.</li>
</ol>
