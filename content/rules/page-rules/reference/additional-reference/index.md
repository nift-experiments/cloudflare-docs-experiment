<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13118.md")
</aside>
<h2 id="bypass-cache-on-cookie-setting">Bypass Cache on Cookie setting</h2>
<p>This setting is available to Business and Enterprise customers.</p>
<p>The <strong>Bypass Cache on Cookie</strong> setting supports basic regular expressions (regex) as follows:</p>
<ul>
<li>A pipe operator (represented by <code>|</code>) to match multiple cookies using <em>OR</em> boolean logic. For example, <code>bypass=.*|PHPSESSID=.*</code> would bypass the cache if either a cookie called <code>bypass</code> or <code>PHPSESSID</code> were set, regardless of the cookie's value.</li>
<li>The wildcard operator (represented by <code>.*</code>), such that a rule value of <code>t.*st=</code> would match both a cookie called <code>test</code> and one called <code>teeest</code>.</li>
</ul>
<p>Limitations include:</p>
<ul>
<li>150 characters per cookie regex</li>
<li>12 wildcards per cookie regex</li>
<li>1 wildcard in between each <code>|</code> in the cookie regex</li>
</ul>
<p>To learn how to configure <strong>Bypass Cache on Cookie</strong> with a cache rule, refer to <a href="/cache/how-to/cache-rules/examples/bypass-cache-on-cookie/">Bypass Cache on Cookie</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13117.md")
</aside>
<h2 id="zone-name-occurrences-must-end-with-a-slash">Zone name occurrences must end with a slash</h2>
<p>When saving a page rule, Cloudflare will ensure that there is a slash after each occurrence of the current zone name in the <strong>If the URL matches</strong> field. For example, if the current zone name is <code>example.com</code>, then:</p>
<ul>
<li><code>example.com</code> will be saved as <code>example.com/</code></li>
<li><code>example.com/path/example.com</code> will be saved as <code>example.com/path/example.com/</code></li>
</ul>
<p>Note that <code>example.com/some-path/cloudflare.com</code> will be saved <em>without</em> a final slash, since the zone name is not <code>cloudflare.com</code>.</p>
<h2 id="network-ports-supported-by-page-rules">Network ports supported by Page Rules</h2>
<p>If you specify a port in the <strong>If the URL matches</strong> field of a page rule, it must be one of the following:</p>
<ul>
<li>One of the HTTP/HTTPS ports <a href="/fundamentals/reference/network-ports/#network-ports-compatible-with-cloudflares-proxy">compatible with Cloudflare’s proxy</a>.</li>
<li>A custom port of a <a href="/spectrum/">Cloudflare Spectrum</a> HTTPS application.</li>
</ul>
<h2 id="using-page-rules-with-workers">Using Page Rules with Workers</h2>
<p>If the URL of the current request matches both a page rule and a <a href="/workers/configuration/routing/routes/">Workers custom route</a>, some Pages Rules settings will not be applied. For more details, refer to <a href="/workers/configuration/workers-with-page-rules/">Page Rules</a>.</p>
<h2 id="page-rules-are-case-insensitive">Page Rules are case-insensitive</h2>
<p>The pattern entered under <strong>If the URL matches</strong> will not consider upper and lower case differences — <code>example.com/path</code>, <code>example.com/Path</code>, and <code>example.com/PATH</code> will be triggered the same way.</p>
<p>If you need your rules to consider case sensitivity, you might want to use alternative <a href="/rules/">Rules</a> options instead.</p>
