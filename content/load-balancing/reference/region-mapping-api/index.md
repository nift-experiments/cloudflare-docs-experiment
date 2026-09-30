<p>Cloudflare’s Load Balancing Regions API has several uses:</p>
<ul>
<li>Identify which countries/areas (states/provinces in the case of the U.S. and Canada) are part of a specific Cloudflare Load Balancer region.</li>
<li>Identify the Cloudflare Load Balancer region for a particular country/area (states/provinces in the case of the U.S. and Canada).</li>
</ul>
<p>The Region API uses 2-letter <a href="https://www.iso.org/iso-3166-country-codes.html">ISO-3166-1 alpha-2 codes</a> for countries/areas and, in the case of the U.S. and Canada, ISO-3166-2 subdivision codes for states/provinces. Only the U.S. and Canada are provided with these subdivisions.</p>
<p>There are two main optional parameters for the Region API:</p>
<ul>
<li>country_code is a string containing a two-letter alpha-2 country code per ISO 3166-1. For example: /load_balancers/regions?country_code=US</li>
<li>subdivision_code is a string containing a two-letter subdivision code for the U.S. and Canada per ISO 3166-2. For example: /load_balancers/regions?subdivision_code=CA</li>
</ul>
<p>For additional details and examples on using the Region Mapping API, see <a href="/api/resources/load_balancers/subresources/regions/methods/list/">Cloudflare’s API documentation</a>.</p>
<h2 id="list-of-load-balancer-regions">List of Load Balancer regions</h2>
<table>
<thead>
<tr>
<th>Region code</th>
<th>Region name</th>
</tr>
</thead>
<tbody>
<tr>
<td>EEU</td>
<td>Eastern Europe</td>
</tr>
<tr>
<td>ENAM</td>
<td>Eastern North America</td>
</tr>
<tr>
<td>ME</td>
<td>Middle East</td>
</tr>
<tr>
<td>NAF</td>
<td>Northern Africa</td>
</tr>
<tr>
<td>NEAS</td>
<td>Northeast Asia</td>
</tr>
<tr>
<td>NSAM</td>
<td>Northern South America</td>
</tr>
<tr>
<td>OC</td>
<td>Oceania</td>
</tr>
<tr>
<td>SAF</td>
<td>Southern Africa</td>
</tr>
<tr>
<td>SAS</td>
<td>Southern Asia</td>
</tr>
<tr>
<td>SEAS</td>
<td>Southeast Asia</td>
</tr>
<tr>
<td>SSAM</td>
<td>Southern South America</td>
</tr>
<tr>
<td>WEU</td>
<td>Western Europe</td>
</tr>
<tr>
<td>WNAM</td>
<td>Western North America</td>
</tr>
</tbody>
</table>
