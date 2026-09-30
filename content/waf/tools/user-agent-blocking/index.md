<p>User Agent Blocking allows you to block specific browser or web application <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent"><code>User-Agent</code> request headers</a>. User agent rules apply to the entire domain instead of individual subdomains.</p>
<p>User agent rules are applied after <a href="/waf/tools/zone-lockdown/">zone lockdown rules</a>. If you allow an IP address via Zone Lockdown, it will skip any user agent rules.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15331.md")
</aside>
<h2 id="availability">Availability</h2>
<p>Cloudflare User Agent Blocking is available on all plans. The <strong>User agent rules</strong> option appears only if you have configured at least one user agent rule.</p>
<p>The number of available user agent rules depends on your Cloudflare plan.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Number of rules</td>
<td>10</td>
<td>50</td>
<td>250</td>
<td>1,000</td>
</tr>
</tbody>
</table>
<h2 id="create-a-user-agent-blocking-rule">Create a User Agent Blocking rule</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashNewNav"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15335.md")
</div></div>
<h2 id="challenge-actions">Challenge actions</h2>
<p>When a User Agent Blocking rule uses a challenge action such as <em>Managed Challenge</em>, the visitor must pass a challenge page. After passing the challenge, a <code>cf_clearance</code> cookie is set. The duration of this cookie is controlled by the <a href="/cloudflare-challenges/challenge-types/challenge-pages/challenge-passage/">Challenge Passage</a> setting.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/learning-paths/application-security/account-security/">Secure your application</a></li>
<li><a href="/waf/tools/zone-lockdown/">Cloudflare Zone Lockdown</a></li>
</ul>
