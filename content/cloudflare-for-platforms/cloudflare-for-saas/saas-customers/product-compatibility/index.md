<p>As a general rule, settings on the customer zone will override settings on the SaaS zone. In addition, <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/">O2O</a> does not permit traffic directed to a custom hostname zone into another custom hostname zone.</p>
<p>The following table provides a list of compatibility guidelines for various Cloudflare products and features.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4089.md")
</aside>
<table>
<thead>
<tr>
<th>Product</th>
<th>Customer zone</th>
<th>SaaS provider zone</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-for-platforms/cloudflare-for-saas/security/secure-with-access/">Access</a></td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td><a href="/cache/how-to/always-online/">Always Online</a></td>
<td>No</td>
<td>No</td>
<td>In an O2O setup, Always Online does not trigger on the eyeball zone because the upstream SaaS provider zone is still reachable. Enabling it on the SaaS provider zone is not recommended because the eyeball zone may cache Internet Archive responses.</td>
</tr>
<tr>
<td><a href="/api-shield/">API Shield</a></td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td><a href="/argo-smart-routing/">Argo Smart Routing</a></td>
<td>No</td>
<td>Yes</td>
<td>Customer zones can still use Smart Routing for non-O2O traffic.</td>
</tr>
<tr>
<td><a href="/bots/plans/bm-subscription/">Bot Management</a></td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td><a href="/waf/tools/browser-integrity-check/">Browser Integrity Check</a></td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td><a href="/cache/">Cache</a></td>
<td>Yes*</td>
<td>Yes</td>
<td>Though caching is possible on a customer zone, it is generally discouraged (especially for HTML).<br/><br/>Your SaaS provider likely performs its own caching outside of Cloudflare and caching on your zone might lead to out-of-sync or stale cache states.<br/><br/>Customer zones can still cache content that are not routed through a SaaS provider's zone.</td>
</tr>
<tr>
<td><a href="/china-network/">China Network</a></td>
<td>No</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td><a href="/dns/">DNS</a></td>
<td>Yes*</td>
<td>Yes</td>
<td>As a SaaS customer, do not remove the records related to your Cloudflare for SaaS setup.<br/><br/>Otherwise, your traffic will begin routing away from your SaaS provider.</td>
</tr>
<tr>
<td><a href="https://blog.cloudflare.com/better-http-2-prioritization-for-a-faster-web/">HTTP/2 prioritization</a></td>
<td>Yes</td>
<td>Yes*</td>
<td>This feature must be enabled on the customer zone to function.</td>
</tr>
<tr>
<td><a href="/images/optimization/transformations/overview/">Image resizing</a></td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td>IPv6</td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td><a href="/network/ipv6-compatibility/">IPv6 Compatibility</a></td>
<td>Yes</td>
<td>Yes*</td>
<td>If the customer zone has <strong>IPv6 Compatibility</strong> enabled, generally the SaaS zone should as well.<br/><br/>If not, make sure the SaaS zone enables <a href="/network/pseudo-ipv4/">Pseudo IPv4</a>.</td>
</tr>
<tr>
<td><a href="/load-balancing/">Load Balancing</a></td>
<td>No</td>
<td>Yes</td>
<td>Customer zones can still use Load Balancing for non-O2O traffic.</td>
</tr>
<tr>
<td><a href="/rules/page-rules/">Page Rules</a></td>
<td>Yes*</td>
<td>Yes</td>
<td>Page Rules that match the subdomain used for O2O may block or interfere with the flow of visitors to your website.</td>
</tr>
<tr>
<td><a href="/rules/origin-rules/">Origin Rules</a></td>
<td>No</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td><a href="/client-side-security/">Client-side security</a> (formerly Page Shield)</td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td><a href="/images/polish/">Polish</a></td>
<td>Yes*</td>
<td>Yes</td>
<td>Polish only runs on cached assets. If the customer zone is bypassing cache for SaaS zone destined traffic, then images optimized by Polish will not be loaded from origin.</td>
</tr>
<tr>
<td><a href="/waf/rate-limiting-rules/">Rate Limiting</a></td>
<td>Yes*</td>
<td>Yes</td>
<td>Rate Limiting rules that match the subdomain used for O2O may block or interfere with the flow of visitors to your website.</td>
</tr>
<tr>
<td><a href="/speed/optimization/content/rocket-loader/">Rocket Loader</a></td>
<td>No</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td><a href="/waf/tools/security-level/">Security Level</a></td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td><a href="/spectrum/">Spectrum</a></td>
<td>No</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td><a href="/rules/transform/">Transform Rules</a></td>
<td>Yes*</td>
<td>Yes</td>
<td>Transform Rules that match the subdomain used for O2O may block or interfere with the flow of visitors to your website.</td>
</tr>
<tr>
<td><a href="/waf/custom-rules/">WAF custom rules</a></td>
<td>Yes</td>
<td>Yes</td>
<td>WAF custom rules that match the subdomain used for O2O may block or interfere with the flow of visitors to your website.</td>
</tr>
<tr>
<td><a href="/waf/managed-rules/">WAF managed rules</a></td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td><a href="/waiting-room/">Waiting Room</a></td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td><a href="/network/websockets/">WebSockets</a></td>
<td>No</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td><a href="/workers/">Workers</a></td>
<td>Yes*</td>
<td>Yes</td>
<td>Similar to Page Rules, Workers that match the subdomain used for O2O may block or interfere with the flow of visitors to your website.</td>
</tr>
<tr>
<td><a href="/zaraz/">Zaraz</a></td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
</tbody>
</table>
