<p>R-U-Dead-Yet (R.U.D.Y.) attacks accomplish denial of service (DoS) by submitting long form fields. Use custom rules to stop these attacks by blocking requests that do not have a legitimate session cookie.</p>
<p>This example combines three expressions to target HTTP <code>POST</code> requests that do not contain a legitimate authenticated session cookie:</p>
<ul>
<li>The first expression uses the <a href="/ruleset-engine/rules-language/fields/reference/http.request.uri.path/"><code>http.request.uri.path</code></a> field to target the paths to secure from R.U.D.Y.:</li>
</ul>
<pre><code class="language-txt">http.request.uri.path matches &quot;(comment|conversation|event|poll)/create&quot;&#10;</code></pre>
<ul>
<li>The second uses a regular expression to match the format of a legitimate <code>auth_session</code> cookie. The <code>not</code> operator targets requests where that cookie is not formatted correctly:</li>
</ul>
<pre><code class="language-txt">not http.cookie matches &quot;auth_session=[0-9a-zA-Z]{32}-[0-9]{10}-[0-9a-z]{6}&quot;&#10;</code></pre>
<ul>
<li>The third expression targets HTTP <code>POST</code> requests:</li>
</ul>
<pre><code class="language-txt">http.request.method eq &quot;POST&quot;&#10;</code></pre>
<p>To generate the final <a href="/waf/custom-rules/create-dashboard/">custom rule</a> expression for this example, the three expressions are combined into a compound expression using the <code>and</code> operator. When an HTTP <code>POST</code> request to any of the specified URIs does not contain a properly formatted <code>auth_session</code> cookie, Cloudflare blocks the request:</p>
<ul>
<li>
<p><strong>When incoming requests match</strong>:</p>
<p>Use the expression editor:<br/>
<code>(http.request.method eq &quot;POST&quot; and http.request.uri.path matches &quot;(comment|conversation|event|poll)/create&quot; and not http.cookie matches &quot;auth_session=[0-9a-zA-Z]{32}-[0-9]{10}-[0-9a-z]{6}&quot;)</code></p>
</li>
<li>
<p><strong>Then take action</strong>: <em>Block</em></p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15455.md")
</aside>
