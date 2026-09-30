<p>When HTTP/HTTPS traffic is <a href="/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-reverse-proxy">proxied through Cloudflare</a>, there are often two established <a href="/fundamentals/reference/tcp-connections/">TCP connections</a>: the first is between the requesting client to Cloudflare and the second is between Cloudflare and the origin server. Each connection has their own set of TCP and HTTP limits, which are documented below.</p>
<h2 id="between-client-and-cloudflare">Between client and Cloudflare</h2>
<table>
<thead>
<tr>
<th>Type</th>
<th>Limit (seconds)</th>
<th>HTTP status code at limit</th>
<th>Configurable</th>
</tr>
</thead>
<tbody>
<tr>
<td>Connection Keep-Alive HTTP/1.1</td>
<td>400</td>
<td>TCP connection closed</td>
<td>No</td>
</tr>
<tr>
<td>Connection Idle HTTP/2</td>
<td>400</td>
<td>TCP connection closed</td>
<td>No</td>
</tr>
</tbody>
</table>
<h2 id="between-cloudflare-and-origin-server">Between Cloudflare and origin server</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8798.md")
</aside>
<table>
<thead>
<tr>
<th>Type</th>
<th>Limit (seconds)</th>
<th>HTTP status code at limit</th>
<th><a href="/fundamentals/reference/connection-limits/#configurable-limits">Configurable</a></th>
</tr>
</thead>
<tbody>
<tr>
<td><span class="nb-interactive-component" data-cf-component="GlossaryTooltip"></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
@markup("md", "content/.markup/bodies/8799.md")
</div> | 19              | [522](/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/)                | No                                                                             |
| <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/8800.md")
</div> Timeout               | 90              | [522](/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/)                | No                                                                             |
| <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/8801.md")
</div> Interval          | 30              | [520](/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-520/)                | No                                                                             |
| <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/8802.md")
</div> Timeout              | 900             | [520](/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-520/)                | No                                                                             |
| <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/8803.md")
</div>           | 125             | [524](/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/)                | [Yes, for Enterprise zones](/api/resources/zones/subresources/settings/methods/edit/)                       |
| <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/8804.md")
</div>         | 30              | [524](/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/)                | No                                                                             |
| HTTP/2 Pings to Origin                                                                    | Off             | -                                                                                                                                      | Yes                                                                            |
| <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/8805.md")
</div>          | 900             | No                                                                                                                                     | No                                                                             |
<h2 id="configurable-limits">Configurable limits</h2>
<p>Some TCP connections can be customized for Enterprise customers. Reach out to your account team for more details.</p>
<h2 id="keep-alives">Keep-Alives</h2>
<p>Cloudflare maintains keep-alive connections to improve performance and reduce cost of recurring TCP connects in the request transaction as Cloudflare proxies customer traffic from its global network to the site's origin server.</p>
<p>Ensure HTTP keep-alive connections are enabled on your origin. Cloudflare reuses open TCP connections up to the <code>Proxy Idle Timeout</code> limit after the last HTTP request. Origin web servers close TCP connections if too many are open. HTTP keep-alive helps avoid connection resets for requests proxied by Cloudflare.</p>
<h2 id="request-limits">Request limits</h2>
<p>URLs have a limit of 16 KB. Request headers have a total limit of 128 KB.</p>
<h2 id="response-limits">Response limits</h2>
<p>Response headers observe a total limit of 128 KB.</p>
<h2 id="cache-limits">Cache limits</h2>
<p>Refer to the <a href="/cache/concepts/default-cache-behavior/#customization-options-and-limits">Cache documentation</a> for more details about the max upload size and the cacheable file size limits.</p>
