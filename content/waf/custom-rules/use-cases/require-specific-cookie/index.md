<p>To secure a sensitive area such as a development area, you can share a cookie with trusted individuals and then filter requests so that only users with that cookie can access your site.</p>
<p>Use the <a href="/ruleset-engine/rules-language/fields/reference/http.cookie/"><code>http.cookie</code></a> field to target requests based on the presence of a specific cookie.</p>
<p>This example comprises two <a href="/waf/custom-rules/create-dashboard/">custom rules</a>:</p>
<ul>
<li>Rule #1 targets requests to <code>dev.www.example.com</code> that have a specific cookie key, <code>devaccess</code>. As long as the value of the cookie key contains one of three authorized users — <code>james</code>, <code>matt</code>, or <code>michael</code> — the expression matches and the request is allowed, skipping all other custom rules.</li>
<li>Rule #2 blocks all access to <code>dev.www.example.com</code>.</li>
</ul>
<p>Since custom rules are evaluated in order, Cloudflare grants access to requests that satisfy rule 1 and blocks all other requests to <code>dev.www.example.com</code>:</p>
<p><strong>Rule #1:</strong></p>
<ul>
<li>
<p><strong>When incoming requests match</strong>:</p>
<p>Use the expression editor:<br/>
<code>(http.cookie contains &quot;devaccess=james&quot; or http.cookie contains &quot;devaccess=matt&quot; or http.cookie contains &quot;devaccess=michael&quot;) and http.host eq &quot;dev.www.example.com&quot;</code></p>
</li>
<li>
<p><strong>Then take action</strong>: <em>Skip:</em></p>
<ul>
<li><em>All remaining custom rules</em></li>
</ul>
</li>
</ul>
<p><strong>Rule #2:</strong></p>
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hostname</td>
<td><code>equals</code></td>
<td><code>dev.www.example.com</code></td>
</tr>
</tbody>
</table>
<p>If using the expression editor:<br/>
<code>(http.host eq &quot;dev.www.example.com&quot;)</code></p>
<ul>
<li><strong>Then take action</strong>: <em>Block</em></li>
</ul>
