<p>TLS 1.3 enables the latest version of the TLS protocol (when supported) for improved security and performance.</p>
<h2 id="what-is-tls-1-3">What is TLS 1.3?</h2>
<p>TLS 1.3 is the newest, fastest, and most secure version of the <a href="/ssl/reference/protocols/">TLS protocol</a>.</p>
<p>By turning on the TLS 1.3 feature, traffic to and from your website will be served over the TLS 1.3 protocol when supported by clients. TLS 1.3 protocol has improved latency over older versions, has several new features, and is currently supported in all updated major browsers.</p>
<h2 id="availability">Availability</h2>
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
</tbody>
</table>
<h2 id="enable-tls-1-3">Enable TLS 1.3</h2>
<p>TLS 1.3 can be activated in the Cloudflare dashboard or through the API:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14125.md")
</div></div>
<h3 id="troubleshooting">Troubleshooting</h3>
<p>Since TLS 1.3 implementations are relatively new, some failures may occur. If you experience errors, submit a Cloudflare Support ticket with the following information:</p>
<ul>
<li>Steps to replicate the issue (if possible)</li>
<li>Client build version</li>
<li>Client diagnostic information</li>
<li>Packet captures</li>
</ul>
<p>Chrome users should submit a <a href="https://dev.chromium.org/for-testers/providing-network-details">net-internals trace</a> to Google. Firefox users should <a href="https://bugzilla.mozilla.org/home">report bugs to Mozilla</a>.</p>
<h2 id="limitations">Limitations</h2>
<div class="nb-data-component" data-cf-component="Render"></div>
