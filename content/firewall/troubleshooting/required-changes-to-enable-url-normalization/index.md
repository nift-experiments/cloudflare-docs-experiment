<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/8691.md")
</aside>
<p>On 2021-04-08, Cloudflare announced <a href="/rules/normalization/">URL normalization</a>, a feature that protects zones by normalizing HTTP request URI paths.</p>
<p>Malicious users can craft specific URIs that could be interpreted differently by firewall systems and origin systems. When you enable <strong>Normalize incoming URLs</strong>, all rules filtering on the URI path will receive the URL in a canonical form, which provides an extra layer of protection against these malicious users.</p>
<p>Cloudflare gradually enabled URL normalization for all Cloudflare zones except for those that could be impacted by this change. We determined the impacted zones by analyzing all firewall rules, looking for patterns in HTTP fields that would no longer match when using URL normalization techniques.</p>
<p>These fields are the following:</p>
<ul>
<li><code>http.request.uri.path</code></li>
<li><code>http.request.full_uri</code></li>
<li><code>http.request.uri</code></li>
</ul>
<p>Cloudflare did not enable URL normalization automatically for zones that would be impacted by these changes to prevent any change in behavior of your existing firewall rules.</p>
<h2 id="why-url-normalization-is-important">Why URL normalization is important</h2>
<p>Cloudflare strongly recommends that you enable <strong>Normalize incoming URLs</strong> in <strong>Rules</strong> &gt; <strong>Overview</strong> &gt; <strong>URL Normalization</strong> to strengthen your zone's security posture. Not doing so leaves your zone at greater risk of a successful attack. Malicious parties could craft the URL in a way that the rules are not accounting for.</p>
<p>For example, a firewall rule with an expression such as <code>http.request.uri.path contains &quot;/login&quot;</code> could be bypassed if the malicious actor has encoded the <code>l</code> character as <code>%6C</code>. In this scenario, and with URL normalization disabled, traffic would not be matched by the firewall rule.</p>
<p>Refer to <a href="/rules/normalization/how-it-works/">How URL normalization works</a> for more information and additional examples.</p>
<hr />
<h2 id="recommended-procedure">Recommended procedure</h2>
<p>It is recommended that you:</p>
<ol>
<li>Update any firewall rules impacted by the URL normalization changes.</li>
<li>Enable URL normalization.</li>
</ol>
<p>These steps will ensure a stronger security posture on your zone(s).</p>
<h3 id="1-review-and-update-firewall-rules"><ol>
<li>Review and update firewall rules</li>
</ol></h3>
<p>Before enabling URL normalization, you should review the affected firewall rules on your zone(s) and take one of the following approaches:</p>
<ul>
<li>
<p>Edit these firewall rules to remove the parts which will no longer trigger once normalized — for example, any rules that look for <code>//</code> or <code>../</code> in URL paths. Administrators previously created these rules to perform a limited URL normalization, and these rules can now be safely disabled and then deleted.</p>
</li>
<li>
<p>If you wish to identify visitors with non-normalized URI paths with these firewall rules, you should update them to use the original (or raw) non-normalized fields. These fields are the following:</p>
<ul>
<li><code>raw.http.request.uri.path</code></li>
<li><code>raw.http.request.full_uri</code></li>
<li><code>raw.http.request.uri</code></li>
</ul>
</li>
</ul>
<h3 id="2-enable-url-normalization"><ol start="2">
<li>Enable URL normalization</li>
</ol></h3>
<p>Once you have updated the affected firewall rules, enable URL normalization in <strong>Rules</strong> &gt; <strong>Overview</strong> &gt; <strong>URL Normalization</strong>.</p>
<p>A Cloudflare user must have the <a href="/fundamentals/manage-members/roles/">Firewall role</a> or one of the Administrator roles to access URL normalization settings in the dashboard.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/rules/normalization/">URL normalization</a></li>
<li><a href="/rules/transform/">Transform Rules</a></li>
</ul>
