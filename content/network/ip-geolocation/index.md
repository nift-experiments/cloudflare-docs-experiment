<p>IP geolocation adds the <a href="/fundamentals/reference/http-headers/#cf-ipcountry"><code>CF-IPCountry</code> header</a> to all requests to your origin server.</p>
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
<h2 id="add-ip-geolocation-information">Add IP geolocation information</h2>
<p>The recommended procedure to enable IP geolocation information is to <a href="/rules/transform/managed-transforms/reference/#add-visitor-location-headers">enable the <strong>Add visitor location headers</strong> Managed Transform</a>. This Managed Transform adds HTTP request headers with location information for the visitor's IP address, such as city, country, continent, longitude, and latitude.</p>
<p>If you only want the request header for the visitor's country, you can enable <strong>IP Geolocation</strong>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/685.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/682.md")
</aside>
<hr />
<h2 id="accuracy-and-limitations">Accuracy and limitations</h2>
<p>IP geolocation is an estimate, not an exact science. There is nothing that inherently binds an IP address to a physical location or country. Because IP addresses rotate and ownership can change, the data is dynamic and may shift over time.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/681.md")
</aside>
<p>Here is what you can expect regarding data accuracy and updates:</p>
<ul>
<li><strong>Update frequency</strong>: Cloudflare automatically updates its IP geolocation database multiple times per week.</li>
<li><strong>Processing time</strong>: Cloudflare reviews correction requests, which may or may not result in a change. Confirmed changes generally take effect within a few business days.</li>
<li><strong>Accuracy</strong>: Due to the dynamic nature of IP address allocation, Cloudflare cannot guarantee that its IP geolocation will align with other providers. Cloudflare does not provide SLAs for IP geolocation accuracy or the timing of updates.</li>
</ul>
<hr />
<h2 id="report-an-incorrect-ip-location">Report an incorrect IP location</h2>
<p>If you find an IP address with a location that you believe is incorrect, fill in the <a href="https://www.cloudflare.com/lp/ip-corrections/">data correction form</a> with the relevant IP address range(s) along with the correct information as applicable (country, state/province, city name, and ZIP code).</p>
<p>If the data is confirmed, Cloudflare will make the necessary changes, generally within a few business days.</p>
<p>If Cloudflare cannot confirm the submitted location, the correction does not result in a change.</p>
<p>If an end user's IP address rotates frequently, for example on mobile or CGNAT networks, the address may change again before the correction completes.</p>
