<h2 id="the-token-is-not-verified">The token is not verified</h2>
<p>Ensure the token has been verified by running the following <code>curl</code> command and confirming that the response returns <code>&quot;status&quot;: &quot;active&quot;</code>.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/user/tokens/verify&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<pre><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;id&quot;: &quot;f267e341f3dd4697bd3b9f71dd96247f&quot;,&#10;    &quot;status&quot;: &quot;active&quot;,&#10;    &quot;not_before&quot;: &quot;2018-07-01T05:20:00Z&quot;,&#10;    &quot;expires_on&quot;: &quot;2020-01-01T00:00:00Z&quot;&#10;  }&#10;}&#10;</code></pre>
<h2 id="the-token-has-incorrect-permissions">The token has incorrect permissions</h2>
<p>Review the permissions groups for your token in the <a href="https://dash.cloudflare.com/profile/api-tokens">Cloudflare dashboard</a>. Refer to <a href="/fundamentals/api/reference/permissions/">API token permissions</a> for more information.</p>
<h2 id="the-incorrect-syntax-is-used">The incorrect syntax is used</h2>
<p>Occasionally customers will attempt to use an API token with an API key syntax. Ensure you are using the Bearer option rather than the email and API key pair.</p>
<h2 id="you-have-the-incorrect-user-permissions">You have the incorrect user permissions</h2>
<p>You cannot create a token that exceeds the permission granted to you on your account. For example, if you have been granted an <strong>Admin (Read only)</strong> role, you would need your Super Administrator to update your role so that you could create a token for yourself.</p>
