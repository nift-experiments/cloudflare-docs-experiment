<p>Page Rules trigger certain actions whenever a request matches one of the URL patterns you define. You can define a page rule to trigger one or more actions whenever a certain URL pattern is matched. Refer to <a href="/rules/page-rules/">Page Rules</a> to learn more about configuring Page Rules.</p>
<h2 id="page-rules-with-workers">Page Rules with Workers</h2>
<p>Cloudflare acts as a <a href="https://www.cloudflare.com/learning/what-is-cloudflare/">reverse proxy</a> to provide services, like Page Rules, to Internet properties. Your application's traffic will pass through a Cloudflare data center that is closest to the visitor. There are hundreds of these around the world, each of which are capable of running services like Workers and Page Rules. If your application is built on Workers and/or Pages, the <a href="https://www.cloudflare.com/learning/serverless/glossary/what-is-edge-computing/">Cloudflare global network</a> acts as your origin server and responds to requests directly from the Cloudflare global network.</p>
<p>When using Page Rules with Workers, the following workflow is applied.</p>
<ol>
<li>Request arrives at Cloudflare data center.</li>
<li>Cloudflare decides if this request is a Worker route. Because this is a Worker route, Cloudflare evaluates and disabled a number of features, including some that would be set by Page Rules.</li>
<li>Page Rules run as part of normal request processing with some features now disabled.</li>
<li>Worker executes.</li>
<li>Worker makes a same-zone or other-zone subrequest. Because this is a Worker route, Cloudflare disables a number of features, including some that would be set by Page Rules.</li>
</ol>
<p>Page Rules are evaluated both at the client-to-Worker request stage (step 2) and the Worker subrequest stage (step 5).</p>
<p>If you are experiencing Page Rule errors when running Workers, contact your Cloudflare account team or <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>.</p>
<h2 id="affected-page-rules">Affected Page Rules</h2>
<p>The following Page Rules may not work as expected when an incoming request is matched to a Worker route:</p>
<ul>
<li>Always Online</li>
<li><a href="/workers/configuration/workers-with-page-rules/#always-use-https">Always Use HTTPS</a></li>
<li><a href="/workers/configuration/workers-with-page-rules/#automatic-https-rewrites">Automatic HTTPS Rewrites</a></li>
<li><a href="/workers/configuration/workers-with-page-rules/#browser-cache-ttl">Browser Cache TTL</a></li>
<li><a href="/workers/configuration/workers-with-page-rules/#browser-integrity-check">Browser Integrity Check</a></li>
<li><a href="/workers/configuration/workers-with-page-rules/#cache-deception-armor">Cache Deception Armor</a></li>
<li><a href="/workers/configuration/workers-with-page-rules/#cache-level">Cache Level</a></li>
<li>Disable Apps</li>
<li><a href="/workers/configuration/workers-with-page-rules/#disable-zaraz">Disable Zaraz</a></li>
<li><a href="/workers/configuration/workers-with-page-rules/#edge-cache-ttl">Edge Cache TTL</a></li>
<li><a href="/workers/configuration/workers-with-page-rules/#email-obfuscation">Email Obfuscation</a></li>
<li><a href="/workers/configuration/workers-with-page-rules/#forwarding-url">Forwarding URL</a></li>
<li>Host Header Override</li>
<li><a href="/workers/configuration/workers-with-page-rules/#ip-geolocation-header">IP Geolocation Header</a></li>
<li><a href="/workers/configuration/workers-with-page-rules/#origin-cache-control">Origin Cache Control</a></li>
<li><a href="/workers/configuration/workers-with-page-rules/#rocket-loader">Rocket Loader</a></li>
<li><a href="/workers/configuration/workers-with-page-rules/#security-level">Security Level</a></li>
<li><a href="/workers/configuration/workers-with-page-rules/#ssl">SSL</a></li>
</ul>
<p>This is because the default setting of these Page Rules will be disabled when Cloudflare recognizes that the request is headed to a Worker.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="testing">Testing</h3>
@markup("md", "content/.markup/bodies/16593.md")
</aside>
<p>To learn what these Page Rules do, refer to <a href="/rules/page-rules/">Page Rules</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="same-zone-versus-other-zone">Same zone versus other zone</h3>
@markup("md", "content/.markup/bodies/16592.md")
</aside>
<h3 id="always-use-https">Always Use HTTPS</h3>
<table>
<thead>
<tr>
<th>Source</th>
<th>Target</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>Worker</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Same Zone</td>
<td>Rule Ignored</td>
</tr>
<tr>
<td>Worker</td>
<td>Other Zone</td>
<td>Rule Ignored</td>
</tr>
</tbody>
</table>
<h3 id="automatic-https-rewrites">Automatic HTTPS Rewrites</h3>
<table>
<thead>
<tr>
<th>Source</th>
<th>Target</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>Worker</td>
<td>Rule Ignored</td>
</tr>
<tr>
<td>Worker</td>
<td>Same Zone</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Other Zone</td>
<td>Rule Ignored</td>
</tr>
</tbody>
</table>
<h3 id="browser-cache-ttl">Browser Cache TTL</h3>
<table>
<thead>
<tr>
<th>Source</th>
<th>Target</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>Worker</td>
<td>Rule Ignored</td>
</tr>
<tr>
<td>Worker</td>
<td>Same Zone</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Other Zone</td>
<td>Rule Ignored</td>
</tr>
</tbody>
</table>
<h3 id="browser-integrity-check">Browser Integrity Check</h3>
<table>
<thead>
<tr>
<th>Source</th>
<th>Target</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>Worker</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Same Zone</td>
<td>Rule Ignored</td>
</tr>
<tr>
<td>Worker</td>
<td>Other Zone</td>
<td>Rule Ignored</td>
</tr>
</tbody>
</table>
<h3 id="cache-deception-armor">Cache Deception Armor</h3>
<table>
<thead>
<tr>
<th>Source</th>
<th>Target</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>Worker</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Same Zone</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Other Zone</td>
<td>Rule Ignored</td>
</tr>
</tbody>
</table>
<h3 id="cache-level">Cache Level</h3>
<table>
<thead>
<tr>
<th>Source</th>
<th>Target</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>Worker</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Same Zone</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Other Zone</td>
<td>Rule Ignored</td>
</tr>
</tbody>
</table>
<h3 id="disable-zaraz">Disable Zaraz</h3>
<table>
<thead>
<tr>
<th>Source</th>
<th>Target</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>Worker</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Same Zone</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Other Zone</td>
<td>Rule Ignored</td>
</tr>
</tbody>
</table>
<h3 id="edge-cache-ttl">Edge Cache TTL</h3>
<table>
<thead>
<tr>
<th>Source</th>
<th>Target</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>Worker</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Same Zone</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Other Zone</td>
<td>Rule Ignored</td>
</tr>
</tbody>
</table>
<h3 id="email-obfuscation">Email Obfuscation</h3>
<table>
<thead>
<tr>
<th>Source</th>
<th>Target</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>Worker</td>
<td>Rule Ignored</td>
</tr>
<tr>
<td>Worker</td>
<td>Same Zone</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Other Zone</td>
<td>Rule Ignored</td>
</tr>
</tbody>
</table>
<h3 id="forwarding-url">Forwarding URL</h3>
<table>
<thead>
<tr>
<th>Source</th>
<th>Target</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>Worker</td>
<td>Rule Ignored</td>
</tr>
<tr>
<td>Worker</td>
<td>Same Zone</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Other Zone</td>
<td>Rule Ignored</td>
</tr>
</tbody>
</table>
<h3 id="ip-geolocation-header">IP Geolocation Header</h3>
<table>
<thead>
<tr>
<th>Source</th>
<th>Target</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>Worker</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Same Zone</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Other Zone</td>
<td>Rule Ignored</td>
</tr>
</tbody>
</table>
<h3 id="origin-cache-control">Origin Cache Control</h3>
<table>
<thead>
<tr>
<th>Source</th>
<th>Target</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>Worker</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Same Zone</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Other Zone</td>
<td>Rule Ignored</td>
</tr>
</tbody>
</table>
<h3 id="rocket-loader">Rocket Loader</h3>
<table>
<thead>
<tr>
<th>Source</th>
<th>Target</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>Worker</td>
<td>Rule Ignored</td>
</tr>
<tr>
<td>Worker</td>
<td>Same Zone</td>
<td>Rule Ignored</td>
</tr>
<tr>
<td>Worker</td>
<td>Other Zone</td>
<td>Rule Ignored</td>
</tr>
</tbody>
</table>
<h3 id="security-level">Security Level</h3>
<table>
<thead>
<tr>
<th>Source</th>
<th>Target</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>Worker</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Same Zone</td>
<td>Rule Ignored</td>
</tr>
<tr>
<td>Worker</td>
<td>Other Zone</td>
<td>Rule Ignored</td>
</tr>
</tbody>
</table>
<h3 id="ssl">SSL</h3>
<table>
<thead>
<tr>
<th>Source</th>
<th>Target</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Client</td>
<td>Worker</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Same Zone</td>
<td>Rule Respected</td>
</tr>
<tr>
<td>Worker</td>
<td>Other Zone</td>
<td>Rule Ignored</td>
</tr>
</tbody>
</table>
