<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prerequisite">Prerequisite</h3>
@markup("md", "content/.markup/bodies/9002.md")
</aside>
<div class="video-frame"><img class="video-poster" src="https://imagedelivery.net/xDOJvHcv1KwTQn6S-BGFIw/d1f88307-30b6-40e3-c38e-7cec03e5ed00/public" alt="Create an API token"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/4e92423fc9126a22af2b0c37825d4195/iframe?preload=true&amp;letterboxColor=transparent" title="Create an API token" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<ol>
<li>Determine if you want a user token or an <a href="/fundamentals/api/get-started/account-owned-tokens/">Account API token</a>. Use Account API tokens if you prefer service tokens that are not associated with users and your <a href="/fundamentals/api/get-started/account-owned-tokens/#compatibility-matrix">desired API endpoints are compatible</a>.</li>
<li>From the <a href="https://dash.cloudflare.com/profile/api-tokens/">Cloudflare dashboard</a>, go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong> for user tokens. For Account Tokens, go to <strong>Manage Account</strong> &gt; <strong>API Tokens</strong>.</li>
<li>Select <strong>Create Token</strong>.</li>
<li>Select a template from the available <a href="/fundamentals/api/reference/template/">API token templates</a> or create a custom token. The following example uses the <strong>Edit zone DNS</strong> template.</li>
<li>Add or edit the token name to describe why or how the token is used. Templates are prefilled with a token name and permissions.</li>
</ol>
<p><img src="/assets/upstream/images/fundamentals/api/template-customize.png" alt="Token template overview screen" /></p>
<ol start="6">
<li>Modify the token's permissions. After selecting a permissions group (<em>Account</em>, <em>User</em>, or <em>Zone</em>), choose what level of access to grant the token. Most groups offer <code>Edit</code> or <code>Read</code> options. <code>Edit</code> is full CRUDL (create, read, update, delete, list) access, while <code>Read</code> is the read permission and list where appropriate. Refer to the <a href="/fundamentals/api/reference/permissions/">available token permissions</a> for more information.</li>
<li>Select which resources the token is authorized to access. For example, granting <code>Zone DNS Read</code> access to a zone <code>example.com</code> will allow the token to read DNS records only for that specific zone. Any other zone will return an error for DNS record reads operations. Any other operation on that zone will also return an error.</li>
<li>(Optional) Restrict how a token is used in the <strong>Client IP Address Filtering</strong> and <strong>TTL (time to live)</strong> fields.</li>
<li>Select <strong>Continue to summary</strong>.</li>
<li>Review the token summary. Select <strong>Edit token</strong> to make adjustments. You can also edit a token after creation.</li>
</ol>
<p><img src="/assets/upstream/images/fundamentals/api/token-summary.png" alt="Token summary screen displaying the resources and permissions selected" /></p>
<ol start="11">
<li>Select <strong>Create Token</strong> to generate the token's secret.</li>
<li>Copy the secret to a secure place.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/9001.md")
</aside>
<p><img src="/assets/upstream/images/fundamentals/api/token-complete.png" alt="Token creation completion screen displaying your API token and the curl command to test your token" /></p>
<p>The token secret page also includes an example command to test the token. Use the <code>/user/tokens/verify</code> endpoint to fetch the current status of the given token.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/user/tokens/verify&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>The result:</p>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;100bf38cc8393103870917dd535e0628&quot;,&#10;		&quot;status&quot;: &quot;active&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [&#10;		{&#10;			&quot;code&quot;: 10000,&#10;			&quot;message&quot;: &quot;This API Token is valid and active&quot;,&#10;			&quot;type&quot;: null&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>New API tokens use the <code>cfut_</code> prefixed <a href="/fundamentals/api/get-started/token-formats/">scannable format</a>, which allows credential scanning tools to detect leaked tokens.</p>
<p>With this you have successfully created an API token and can start working with the Cloudflare API. After creating your first API token, you can create additional API tokens <a href="/fundamentals/api/how-to/create-via-api/">via the API</a>.</p>
