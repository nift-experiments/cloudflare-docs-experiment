<p>Generate new API tokens on the fly via the API. Before you can do this, you must create an API token in the Cloudflare dashboard that can create subsequent tokens.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8992.md")
</aside>
<h2 id="generating-the-initial-token">Generating the initial token</h2>
<p>Before you can use the API, you need to <a href="/fundamentals/api/get-started/create-token/">generate an initial token</a> via the Cloudflare dashboard. The required permission depends on the API operation. To grant users access to an account as members, create a token with <strong>Account</strong> &gt; <strong>Account Settings</strong> &gt; <strong>Edit</strong>. To create account-owned API tokens, create a token with <strong>Account</strong> &gt; <strong>Account API Tokens</strong> &gt; <strong>Edit</strong>. To create user-owned API tokens, use the <strong>Create additional tokens</strong> template.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/8991.md")
</aside>
<h3 id="recommendations">Recommendations</h3>
<p>When using the <strong>Create additional tokens</strong> template, Cloudflare highly recommends that you do not grant other permissions to the token. Make sure you safeguard the new token because it can create tokens with access to any of a user's resources.</p>
<p>Cloudflare also recommends limiting the use of the token via client IP address filtering or TTL to reduce the potential for abuse in the event that the token is compromised. Refer to <a href="/fundamentals/api/how-to/restrict-tokens/">Restrict token use</a> for more information.</p>
<h2 id="creating-api-tokens-with-the-api">Creating API tokens with the API</h2>
<p>You can create a user owned token or account owned token to use with the API. Refer to the <a href="/api/resources/user/subresources/tokens/methods/create/">user owned token</a> or the <a href="/api/resources/accounts/subresources/tokens/methods/create/">account owned token</a> API schema docs for more information.</p>
<p>To create a token:</p>
<ol>
<li>Define the policy.</li>
<li>Define the restrictions.</li>
<li>Create the token.</li>
</ol>
<h3 id="1-define-the-access-policy"><ol>
<li>Define the Access Policy</li>
</ol></h3>
<p>An Access Policy defines what resources the token can act on and what permissions the token has to those resources. This process is similar to how you <a href="/fundamentals/api/get-started/create-token/">create tokens in the Cloudflare dashboard</a>.</p>
<p>Each token can contain multiple policies.</p>
<pre><code class="language-json">[&#10;	{&#10;		&quot;id&quot;: &quot;f267e341f3dd4697bd3b9f71dd96247f&quot;,&#10;		&quot;effect&quot;: &quot;allow&quot;,&#10;		&quot;resources&quot;: {&#10;			&quot;com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4&quot;: &quot;*&quot;,&#10;			&quot;com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43&quot;: &quot;*&quot;&#10;		},&#10;		&quot;permission_groups&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;c8fed203ed3043cba015a93ad1616f1f&quot;,&#10;				&quot;name&quot;: &quot;Zone Read&quot;&#10;			},&#10;			{&#10;				&quot;id&quot;: &quot;82e64a83756745bbbb1c9c2701bf816b&quot;,&#10;				&quot;name&quot;: &quot;DNS Read&quot;&#10;			}&#10;		]&#10;	}&#10;]&#10;</code></pre>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>id</code></td>
<td>Unique read-only identifier for the policy generated after creation.</td>
</tr>
<tr>
<td><code>effect</code></td>
<td>Defines whether this policy is allowing or denying access. If only creating one policy, use <code>allow</code>. The evaluation order for policies is as follows: 1. Explicit <code>DENY</code> Policies; 2. Explicit <code>ALLOW</code> Policies; 3. Implicit <code>DENY ALL</code>.</td>
</tr>
<tr>
<td><code>resources</code></td>
<td>Defines what resources are allowed to be configured.</td>
</tr>
<tr>
<td><code>permission_groups</code></td>
<td>Defines what permissions the policy grants to the included resources.</td>
</tr>
</tbody>
</table>
<h4 id="resources">Resources</h4>
<p>API token policies support three resource types: <code>User</code>, <code>Account</code>, and <code>Zone</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8990.md")
</aside>
<h5 id="account">Account</h5>
<p>Include a single account or all accounts in a token policy.</p>
<ul>
<li>A <strong>single account</strong> is denoted as:<code>&quot;com.cloudflare.api.account.&lt;ACCOUNT_ID&gt;&quot;: &quot;*&quot;</code>.</li>
<li><strong>All accounts</strong> is denoted as:<code>&quot;com.cloudflare.api.account.*&quot;: &quot;*&quot;</code></li>
</ul>
<h5 id="zone">Zone</h5>
<p>Include a <strong>single zone</strong>, <strong>all zones in an account</strong>, or <strong>all zones in all accounts</strong> in a token policy.</p>
<ul>
<li>A <strong>single zone</strong> is denoted as:<code>&quot;com.cloudflare.api.account.zone.&lt;ZONE_ID&gt;&quot;: &quot;*&quot;</code></li>
<li><strong>All Zones in an account</strong> are denoted as:<code>&quot;com.cloudflare.api.account.&lt;ACCOUNT_ID&gt;&quot;: {&quot;com.cloudflare.api.account.zone.*&quot;: &quot;*&quot;}</code></li>
<li><strong>All zones in all accounts</strong> is denoted as:<code>&quot;com.cloudflare.api.account.zone.*&quot;: &quot;*&quot;</code></li>
</ul>
<h5 id="user">User</h5>
<p>For user resources, you can only reference yourself, which is denoted as:<code>&quot;com.cloudflare.api.user.&lt;USER_TAG&gt;&quot;: &quot;*&quot;</code></p>
<h4 id="permission-groups">Permission groups</h4>
<p>Add permission groups to the API token by specifying their <code>id</code> values. We recommend using <code>id</code> as the key for interacting with Cloudflare APIs; the permission <code>name</code> is cosmetic and subject to change. Permission groups are scoped to specific resources (user, account, or zone), so a permission group in a policy will only apply to the resource type it is scoped for.</p>
<p>To fetch all available permission groups and their IDs, use the <a href="/api/resources/user/subresources/tokens/subresources/permission_groups/methods/list/">List permission groups</a> endpoint:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/user/tokens/permission_groups \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;  &quot;result&quot;: [&#10;    {&#10;      &quot;id&quot;: &quot;19637fbb73d242c0a92845d8db0b95b1&quot;,&#10;      &quot;name&quot;: &quot;AI Crawl Control Read&quot;,&#10;      &quot;description&quot;: &quot;Grants access to reading AI Crawl Control&quot;,&#10;      &quot;scopes&quot;: [&#10;        &quot;com.cloudflare.api.account.zone&quot;&#10;      ]&#10;    },&#10;    {&#10;      &quot;id&quot;: &quot;1ba6ab4cacdb454b913bbb93e1b8cb8c&quot;,&#10;      &quot;name&quot;: &quot;AI Crawl Control Write&quot;,&#10;      &quot;description&quot;: &quot;Grants access to reading and editing AI Crawl Control&quot;,&#10;      &quot;scopes&quot;: [&#10;        &quot;com.cloudflare.api.account.zone&quot;&#10;      ]&#10;    },&#10;    // (...)&#10;	]&#10;}&#10;</code></pre>
<h3 id="2-define-the-restrictions"><ol start="2">
<li>Define the restrictions</li>
</ol></h3>
<p>Set up any limitations on how the token can be used. API tokens allow restrictions for client IP address filtering and TTLs. Refer to <a href="/fundamentals/api/how-to/restrict-tokens/">Restrict token use</a> for more information.</p>
<p>When defining TTLs, you can set the time at which a token becomes active with <code>not_before</code> and the time when it expires with <code>expires_on</code>. Both of these fields take UTC timestamps in the following format: <code>&quot;2018-07-01T05:20:00Z&quot;</code>.</p>
<p>Limit usage of a token by client IP address filters with the following object:</p>
<pre><code class="language-json">{&#10;	&quot;request.ip&quot;: {&#10;		&quot;in&quot;: [&quot;199.27.128.0/21&quot;, &quot;2400:cb00::/32&quot;],&#10;		&quot;not_in&quot;: [&quot;199.27.128.0/21&quot;, &quot;2400:cb00::/32&quot;]&#10;	}&#10;}&#10;</code></pre>
<p>Each parameter in the <code>in</code> and <code>not_in</code> objects must be in CIDR notation. For example, use <code>192.168.0.1/32</code> to specify a single IP address.</p>
<h3 id="3-create-the-token"><ol start="3">
<li>Create the token</li>
</ol></h3>
<p>Combine the previous information to create a token as in the following example:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8995.md")
</div></div>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/user/tokens&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;readonly token&quot;,&#10;  &quot;policies&quot;: [&#10;    {&#10;      &quot;effect&quot;: &quot;allow&quot;,&#10;      &quot;resources&quot;: {&#10;        &quot;com.cloudflare.api.account.zone.eb78d65290b24279ba6f44721b3ea3c4&quot;: &quot;*&quot;,&#10;        &quot;com.cloudflare.api.account.zone.22b1de5f1c0e4b3ea97bb1e963b06a43&quot;: &quot;*&quot;&#10;      },&#10;      &quot;permission_groups&quot;: [&#10;        {&#10;          &quot;id&quot;: &quot;c8fed203ed3043cba015a93ad1616f1f&quot;,&#10;          &quot;name&quot;: &quot;Zone Read&quot;&#10;        },&#10;        {&#10;          &quot;id&quot;: &quot;82e64a83756745bbbb1c9c2701bf816b&quot;,&#10;          &quot;name&quot;: &quot;DNS Read&quot;&#10;        }&#10;      ]&#10;    }&#10;  ],&#10;  &quot;not_before&quot;: &quot;2020-04-01T05:20:00Z&quot;,&#10;  &quot;expires_on&quot;: &quot;2020-04-10T00:00:00Z&quot;,&#10;  &quot;condition&quot;: {&#10;    &quot;request.ip&quot;: {&#10;      &quot;in&quot;: [&#10;        &quot;199.27.128.0/21&quot;,&#10;        &quot;2400:cb00::/32&quot;&#10;      ],&#10;      &quot;not_in&quot;: [&#10;        &quot;199.27.128.1/32&quot;&#10;      ]&#10;    }&#10;  }&#10;}&#x27;&#10;</code></pre>
