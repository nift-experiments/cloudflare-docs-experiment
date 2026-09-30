<p><a href="https://www.chromium.org/updates/same-site">Google Chrome enforces SameSite cookie behavior</a> to protect against marketing cookies that track users and Cross-site Request Forgery (CSRF) that allows attackers to steal or manipulate your cookies.</p>
<p>The <code>SameSite</code> cookie attribute has three different modes:</p>
<ul>
<li><strong>Strict</strong>: Cookies are created by the first party (the visited domain). For example, a first-party cookie is set by Cloudflare when visiting <code>cloudflare.com</code>.</li>
<li><strong>Lax</strong>: Cookies are only sent to the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/15316.md")
</div> domain (such as `example.com`). For example, if someone (`blog.example.net`) hotlinked an image (`img.example.com/bar.png`), the client does not send a cookie to `img.example.com` since it is neither the first-party nor apex context.
- **None**: Cookies are sent with all requests.
<p><code>SameSite</code> settings for <a href="/fundamentals/reference/policies-compliances/cloudflare-cookies/">Cloudflare cookies</a> include:</p>
<table>
<thead>
<tr>
<th>Cloudflare cookie</th>
<th>SameSite setting</th>
<th>HTTPS Only</th>
<th>Partitioned (CHIPS)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>__cf_bm</code></td>
<td><code>SameSite=None; Secure</code></td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td><code>cf_clearance</code></td>
<td><code>SameSite=None; Secure</code></td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td><code>__cflb</code></td>
<td><code>SameSite=Lax</code></td>
<td>No</td>
<td>No</td>
</tr>
</tbody>
</table>
<h2 id="samesite-attribute-in-session-affinity-cookies">SameSite attribute in session affinity cookies</h2>
<p>Currently, to configure the <code>SameSite</code> attribute on <a href="/load-balancing/understand-basics/session-affinity/">session affinity cookies</a> you must use the Cloudflare API (for example, the <a href="/api/resources/load_balancers/methods/create/">Create Load Balancer</a> operation).</p>
<p>To configure the value of the <code>SameSite</code> cookie attribute, include the <code>samesite</code> and <code>secure</code> JSON attributes in your HTTP request, inside the <code>session_affinity_attributes</code> object.</p>
<p>The available values for these two attributes are the following:</p>
<p><strong><code>samesite</code> attribute:</strong></p>
<ul>
<li>Valid values: <code>Auto</code> (default), <code>Lax</code>, <code>None</code>, <code>Strict</code>.</li>
</ul>
<p><strong><code>secure</code> attribute:</strong></p>
<ul>
<li>Valid values: <code>Auto</code> (default), <code>Always</code>, <code>Never</code>.</li>
</ul>
<p>The <code>Auto</code> value for the <code>samesite</code> attribute will have the following behavior:</p>
<ul>
<li>If <a href="/ssl/edge-certificates/additional-options/always-use-https/"><strong>Always Use HTTPS</strong></a> is enabled, session affinity cookies will use the <code>Lax</code> SameSite mode.</li>
<li>If <strong>Always Use HTTPS</strong> is disabled, session affinity cookies will use the <code>None</code> SameSite mode.</li>
</ul>
<p>The <code>Auto</code> value for the <code>secure</code> attribute will have the following behavior:</p>
<ul>
<li>If <strong>Always Use HTTPS</strong> is enabled, session affinity cookies will include <code>Secure</code> in the SameSite attribute.</li>
<li>If <strong>Always Use HTTPS</strong> is disabled, session affinity cookies will not include <code>Secure</code> in the SameSite attribute.</li>
</ul>
<p>If you set <code>samesite</code> to <code>None</code> in your API request, you cannot set <code>secure</code> to <code>Never</code>.</p>
<p>If you require a specific <code>SameSite</code> configuration in your session affinity cookies, Cloudflare recommends that you provide values for <code>samesite</code> and <code>secure</code> different from <code>Auto</code>, instead of relying on the default behavior. This way, the value of the <code>SameSite</code> cookie attribute will not change due to configuration changes (namely <a href="/ssl/edge-certificates/additional-options/always-use-https/"><strong>Always Use HTTPS</strong></a>).</p>
<hr />
<h2 id="known-issues-with-samesite-and-cf-clearance-cookies">Known issues with SameSite and <code>cf_clearance</code> cookies</h2>
<p>When a visitor solves a <a href="/cloudflare-challenges/">challenge</a> presented due to a <a href="/waf/custom-rules/">custom rule</a> or an <a href="/waf/tools/ip-access-rules/">IP access rule</a>, a <code>cf_clearance</code> cookie is set in the visitor's browser. The <code>cf_clearance</code> cookie has a default lifetime of 30 minutes, which you can configure via <a href="/cloudflare-challenges/challenge-types/challenge-pages/challenge-passage/">Challenge Passage</a>.</p>
<p>Cloudflare uses <code>SameSite=None</code> in the <code>cf_clearance</code> cookie so that visitor requests from different hostnames are not met with later challenges or errors. When <code>SameSite=None</code> is used, it must be set in conjunction with the <code>Secure</code> flag.</p>
<p>Using the <code>Secure</code> flag requires sending the cookie via an HTTPS connection. If you use HTTP on any part of your website, the <code>cf_clearance</code> cookie defaults to <code>SameSite=Lax</code>, which may cause your website not to function properly.</p>
<p>To resolve the issue, move your website traffic to HTTPS. Cloudflare offers two features for this purpose:</p>
<ul>
<li><a href="/ssl/edge-certificates/additional-options/automatic-https-rewrites/">Automatic HTTPS Rewrites</a></li>
<li><a href="/ssl/edge-certificates/additional-options/always-use-https/">Always Use HTTPS</a></li>
</ul>
<hr />
<h2 id="partitioned-cookies-chips-and-cf-clearance">Partitioned cookies (CHIPS) and <code>cf_clearance</code></h2>
<p>Cloudflare sets the <code>Partitioned</code> attribute on the <code>cf_clearance</code> cookie (and on the internal <code>cf_chl_*</code> cookies used by the Challenge Platform) to comply with <a href="https://developers.google.com/privacy-sandbox/cookies/chips">Cookies Having Independent Partitioned State (CHIPS) ↗</a>.</p>
<p>With CHIPS, a cookie set in a third-party context (for example, inside an iframe or from a cross-site subresource) is stored in a partition keyed to the top-level site, rather than being shared across all sites that embed the third party. On Chromium-based browsers that block third-party cookies, this preserves challenge state for cross-site embeds that would otherwise be broken. On browsers that do not implement CHIPS, the <code>Partitioned</code> attribute is ignored and behavior is unchanged.</p>
<p>The <code>Partitioned</code> attribute is not applied to <code>__cf_bm</code>.</p>
<h3 id="impact-on-embedded-challenges">Impact on embedded challenges</h3>
<p>Because <code>cf_clearance</code> is partitioned, a clearance obtained in one top-level context is not reused in a different top-level context. A visitor who passes a challenge while browsing a site directly will not automatically carry that clearance into another site that embeds it, and vice versa. This is the intended behavior under CHIPS.</p>
<h3 id="partitioned-requires-samesite-none-secure"><code>Partitioned</code> requires <code>SameSite=None; Secure</code></h3>
<p>The <code>Partitioned</code> attribute only takes effect on cookies that are also set with <code>SameSite=None; Secure</code>. If your site does not serve all traffic over HTTPS, the <code>cf_clearance</code> cookie falls back to <code>SameSite=Lax</code> (refer to <a href="#known-issues-with-samesite-and-cf_clearance-cookies">Known issues with SameSite and <code>cf_clearance</code> cookies</a>), and the <code>Partitioned</code> attribute has no effect.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://web.dev/samesite-cookies-explained/">SameSite cookies explained</a></li>
<li><a href="/fundamentals/reference/policies-compliances/cloudflare-cookies/">Cloudflare Cookies</a></li>
<li><a href="/ssl/faq/">Cloudflare SSL FAQ</a></li>
<li><a href="/ssl/edge-certificates/additional-options/automatic-https-rewrites/">Automatic HTTPS Rewrites</a></li>
<li><a href="/ssl/edge-certificates/additional-options/always-use-https/">Always Use HTTPS</a></li>
</ul>
