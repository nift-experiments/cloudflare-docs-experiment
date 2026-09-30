<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecated">Deprecated</h3>
@markup("md", "content/.markup/bodies/9003.md")
</aside>
<p>Origin CA keys are often used as the value of header <code>X-AUTH-USER-SERVICE-KEY</code> when interacting with <a href="/ssl/origin-configuration/origin-ca/">Origin CA certificates</a> API. It is also used by <a href="/ssl/keyless-ssl/">Keyless SSL</a> key server.</p>
<p>The key value always starts with <code>v1.0-</code>.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Changing the Origin CA key is not recorded by <a href="/fundamentals/account/account-security/review-audit-logs/">Audit Logs</a>.</li>
<li>Each time you view the Origin CA key, it will be presented as a different value. All these different values are <strong>simultaneously valid</strong> until you click the <code>Change</code> button, which immediately invalidates all previously generated values.</li>
<li>Origin CA keys have access to every account the user has access to.</li>
</ul>
<h2 id="view-change-your-origin-ca-keys">View/Change your Origin CA keys</h2>
<p>To retrieve your Origin CA keys:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>User Profile</strong> &gt; <strong>API Tokens</strong>.</li>
<li>In the <strong>API Keys</strong> section, select <code>Origin CA Key</code>.</li>
</ol>
