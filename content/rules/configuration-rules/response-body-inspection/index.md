<p>When no enabled feature needs response content, Cloudflare can send data to the client as it arrives. Some features inspect or change response content at the edge.</p>
<p>Inspection can hold part of a response at the edge. This may increase time to first byte (TTFB) or delay incremental delivery. The amount of data held depends on the feature and response.</p>
<h2 id="features-that-inspect-response-bodies">Features that inspect response bodies</h2>
<p>Cloudflare features primarily inspect responses with a <code>Content-Type</code> of <code>text/html</code>. Some features change the body, while others only read it.</p>
<p>The following features can change HTML response bodies when turned on and applicable:</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Body change</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/bots/additional-configurations/ai-labyrinth/">AI Labyrinth</a></td>
<td>Adds invisible links for unauthorized AI crawlers</td>
</tr>
<tr>
<td><a href="/cache/how-to/always-online/">Always Online</a></td>
<td>Adds a banner to archived pages</td>
</tr>
<tr>
<td><a href="/ssl/edge-certificates/additional-options/automatic-https-rewrites/">Automatic HTTPS Rewrites</a></td>
<td>Rewrites eligible HTTP links to HTTPS</td>
</tr>
<tr>
<td><a href="/cloudflare-challenges/">Cloudflare challenge features</a></td>
<td>Injects challenge scripts or returns challenge content</td>
</tr>
<tr>
<td><a href="/speed/optimization/content/fonts/">Cloudflare Fonts</a> and <a href="/automatic-platform-optimization/">Automatic Platform Optimization</a></td>
<td>Rewrites Google Fonts references</td>
</tr>
<tr>
<td><a href="/waf/tools/scrape-shield/email-address-obfuscation/">Email Address Obfuscation</a></td>
<td>Obfuscates email addresses in page content</td>
</tr>
<tr>
<td><a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a></td>
<td>Converts HTML to Markdown for eligible requests</td>
</tr>
<tr>
<td><a href="/waf/tools/replace-insecure-js-libraries/">Replace insecure JavaScript libraries</a></td>
<td>Rewrites supported insecure library URLs</td>
</tr>
<tr>
<td><a href="/speed/optimization/content/rocket-loader/">Rocket Loader</a></td>
<td>Changes script loading behavior</td>
</tr>
<tr>
<td><a href="/web-analytics/">Web Analytics</a></td>
<td>Injects the Real User Monitoring beacon</td>
</tr>
</tbody>
</table>
<p>Security and AI features may also read HTML without changing it. <a href="/speed/optimization/content/prefetch-urls/">Prefetch URLs</a> reads URL manifests served as <code>text/plain</code>.</p>
<p>This list excludes explicit rules that inspect response content. Review each rule separately when troubleshooting.</p>
<h2 id="streaming-considerations">Streaming considerations</h2>
<p>Response body inspection most often affects progressive HTML and plain-text streams. It can affect other responses selected by explicit inspection rules. A client may receive data later or in larger groups than the origin sent it.</p>
<p>Set an accurate <code>Content-Type</code> at your origin. Do not serve streaming API responses as <code>text/html</code> or <code>text/plain</code> unless that media type is required.</p>
<p>The <code>Cache-Control: no-transform</code> response directive prevents body changes by supported features. It does not prevent read-only inspection. Refer to <a href="/cache/concepts/cache-control/#cache-control-directives">Cache-Control directives</a> for other effects of this directive.</p>
<h2 id="isolate-inspection-issues">Isolate inspection issues</h2>
<p>If a response stops streaming after you proxy it through Cloudflare:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13020.md")
</div>
<p>The <strong>None</strong> setting streams the body without inspection. It can prevent security, optimization, and analytics features from working on matching responses. Use the narrowest matching expression possible.</p>
<p>For setting values and API configuration, refer to <a href="/rules/configuration-rules/settings/#response-body-buffering">Response Body Buffering</a>.</p>
