<p><a href="/client-side-security/rules/">Content security rules</a> support most <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3967.md")
</div> directives, covering both monitored and unmonitored resources. You can use a content security rule to control other types of resources besides scripts and their connections, even though Cloudflare is not monitoring these resources.
<p>Each CSP directive can contain multiple values, including:</p>
<ul>
<li>Schemes</li>
<li>Hostnames</li>
<li>URIs</li>
<li>Special keywords between single quotes (for example, <code>'none'</code>)</li>
<li>Hashes between single quotes (for example, <code>'sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC'</code>)</li>
</ul>
<p>Hostname and URI values support a <code>*</code> wildcard for the leftmost subdomain.</p>
<p>The following table lists the supported CSP directives and special values you can use in content security rules:</p>
<table>
<thead>
<tr>
<th>Directive</th>
<th>Name in the dashboard</th>
<th>Supported special values</th>
<th>Monitored</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>script-src</code></td>
<td>Scripts</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td><a href="/client-side-security/detection/monitor-connections-scripts/">Yes</a></td>
</tr>
<tr>
<td><code>connect-src</code></td>
<td>Connections</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td><a href="/client-side-security/detection/monitor-connections-scripts/">Yes</a></td>
</tr>
<tr>
<td><code>default-src</code></td>
<td>Default</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>img-src</code></td>
<td>Images</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>style-src</code></td>
<td>Styles</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>font-src</code></td>
<td>Fonts</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>object-src</code></td>
<td>Objects</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>media-src</code></td>
<td>Media</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>child-src</code></td>
<td>Child</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>form-action</code></td>
<td>Form actions</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>worker-src</code></td>
<td>Workers</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>base-uri</code></td>
<td>Base URI</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>manifest-src</code></td>
<td>Manifests</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>frame-src</code></td>
<td>Frames</td>
<td><code>'none'</code><br/><code>'self'</code><br/><code>'unsafe-inline'</code><br/><code>'unsafe-eval'</code><br/><code>'&lt;HASH&gt;'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>frame-ancestors</code></td>
<td>Frame ancestors</td>
<td><code>'none'</code><br/><code>'self'</code></td>
<td>No</td>
</tr>
<tr>
<td><code>upgrade-insecure-requests</code></td>
<td>Upgrade insecure requests</td>
<td>N/A</td>
<td>No</td>
</tr>
</tbody>
</table>
<h2 id="more-resources">More resources</h2>
<p>For more information on CSP directives and their values, refer to the following resources in the MDN documentation:</p>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy">Content-Security-Policy response header</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP">CSP guide</a></li>
</ul>
