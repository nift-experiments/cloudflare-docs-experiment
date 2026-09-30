<p>The following tables list the <a href="/ruleset-engine/about/phases/">phases</a> of Cloudflare products powered by the Ruleset Engine, in the order those phases are executed. Some products such as the Cloudflare Web Application Firewall have more than one associated phase.</p>
<h2 id="network-layer">Network layer</h2>
<p><a href="https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/">Network-layer</a> phases apply to packets received on the Cloudflare global network.</p>
<table>
<thead>
<tr>
<th>Phase name</th>
<th>Used in product/feature</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ddos_l4</code></td>
<td><a href="/ddos-protection/managed-rulesets/network/network-overrides/configure-api/">Network-layer DDoS Attack Protection</a></td>
</tr>
<tr>
<td><code>magic_transit</code></td>
<td><a href="/cloudflare-one/traffic-policies/packet-filtering/add-policies/">Cloudflare Network Firewall</a></td>
</tr>
<tr>
<td><code>magic_transit_managed</code></td>
<td><a href="/cloudflare-network-firewall/how-to/enable-managed-rulesets/">Cloudflare Network Firewall managed rulesets</a></td>
</tr>
<tr>
<td><code>magic_transit_ratelimit</code></td>
<td><a href="/cloudflare-network-firewall/how-to/create-rate-limiting-policies/">Cloudflare Network Firewall rate limiting policies</a></td>
</tr>
<tr>
<td><code>magic_transit_ids_managed</code></td>
<td><a href="/cloudflare-network-firewall/about/ids/">Cloudflare Network Firewall Intrusion Detection System (IDS)</a></td>
</tr>
</tbody>
</table>
<h2 id="application-layer">Application layer</h2>
<p><a href="https://www.cloudflare.com/learning/ddos/what-is-layer-7/">Application-layer</a> phases apply to requests received on the Cloudflare global network.</p>
<h3 id="request-phases">Request phases</h3>
<p>The phases execute in the order they appear in the table.</p>
<table>
<thead>
<tr>
<th>Phase name</th>
<th>Used in product/feature</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>http_request_dynamic_redirect</code></td>
<td><a href="/rules/url-forwarding/single-redirects/">Single Redirects</a></td>
</tr>
<tr>
<td><code>http_request_sanitize</code></td>
<td><a href="/rules/normalization/">URL normalization</a></td>
</tr>
<tr>
<td><code>http_request_transform</code></td>
<td><a href="/rules/transform/url-rewrite/">URL Rewrite Rules</a></td>
</tr>
<tr>
<td><em>N/A</em> (internal phase)</td>
<td><a href="/waiting-room/additional-options/waiting-room-rules/">Waiting Room Rules</a></td>
</tr>
<tr>
<td><code>http_request_api_gateway_early</code>*</td>
<td><a href="/api-shield/">API Shield</a></td>
</tr>
<tr>
<td><code>http_config_settings</code></td>
<td><a href="/rules/configuration-rules/">Configuration Rules</a></td>
</tr>
<tr>
<td><code>http_request_origin</code></td>
<td><a href="/rules/origin-rules/">Origin Rules</a></td>
</tr>
<tr>
<td><code>ddos_l7</code>*</td>
<td><a href="/ddos-protection/managed-rulesets/http/">HTTP DDoS Attack Protection</a></td>
</tr>
<tr>
<td><code>http_request_firewall_custom</code></td>
<td><a href="/waf/custom-rules/">Custom rules (Web Application Firewall)</a></td>
</tr>
<tr>
<td><code>http_ratelimit</code></td>
<td><a href="/waf/rate-limiting-rules/">Rate limiting rules (WAF)</a></td>
</tr>
<tr>
<td><code>http_request_api_gateway_late</code></td>
<td><a href="/api-shield/">API Shield</a></td>
</tr>
<tr>
<td><code>http_request_firewall_managed</code></td>
<td><a href="/waf/managed-rules/">WAF Managed Rules</a></td>
</tr>
<tr>
<td><code>http_request_sbfm</code></td>
<td><a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a></td>
</tr>
<tr>
<td><em>N/A</em> (internal phase)</td>
<td><a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> application check</td>
</tr>
<tr>
<td><code>http_request_redirect</code></td>
<td><a href="/rules/url-forwarding/bulk-redirects/">Bulk Redirects</a></td>
</tr>
<tr>
<td><em>N/A</em> (internal phase)</td>
<td><a href="/rules/transform/managed-transforms/">Managed Transforms</a></td>
</tr>
<tr>
<td><code>http_request_late_transform</code></td>
<td><a href="/rules/transform/request-header-modification/">Request Header Transform Rules</a></td>
</tr>
<tr>
<td><code>http_request_cache_settings</code></td>
<td><a href="/cache/how-to/cache-rules/">Cache Rules</a></td>
</tr>
<tr>
<td><code>http_request_snippets</code></td>
<td><a href="/rules/snippets/">Snippets</a></td>
</tr>
<tr>
<td><code>http_request_cloud_connector</code></td>
<td><a href="/rules/cloud-connector/">Cloud Connector</a></td>
</tr>
</tbody>
</table>
<p>* <em>This phase is for configuration purposes only — the corresponding rules will not be executed at this stage in the request handling process.</em></p>
<p>For Cloudflare Access, the <code>Cloudflare Access</code> row refers to Access application checking. Access enforcement and handling run in later internal phases, after Bulk Redirects.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="change-notice-for-super-bot-fight-mode-rulesets">Change notice for Super Bot Fight Mode rulesets</h3>
@markup("md", "content/.markup/bodies/13271.md")
</aside>
<h3 id="response-phases">Response phases</h3>
<p>The phases execute in the order they appear in the table.</p>
<table>
<thead>
<tr>
<th>Phase name</th>
<th>Used in product/feature</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>http_custom_errors</code></td>
<td><a href="/rules/custom-errors/">Custom Errors</a></td>
</tr>
<tr>
<td><em>N/A</em> (internal phase)</td>
<td><a href="/rules/transform/managed-transforms/">Managed Transforms</a></td>
</tr>
<tr>
<td><code>http_response_headers_transform</code></td>
<td><a href="/rules/transform/response-header-modification/">Response Header Transform Rules</a></td>
</tr>
<tr>
<td><code>http_ratelimit</code></td>
<td><a href="/waf/rate-limiting-rules/">Rate limiting rules</a> (when they use response information)</td>
</tr>
<tr>
<td><code>http_response_compression</code></td>
<td><a href="/rules/compression-rules/">Compression Rules</a></td>
</tr>
<tr>
<td><code>http_response_firewall_managed</code></td>
<td><a href="/waf/managed-rules/">Cloudflare Sensitive Data Detection</a> (Data Loss Prevention)</td>
</tr>
<tr>
<td><code>http_log_custom_fields</code></td>
<td><a href="/logs/logpush/logpush-job/custom-fields/">Logpush custom fields</a></td>
</tr>
</tbody>
</table>
