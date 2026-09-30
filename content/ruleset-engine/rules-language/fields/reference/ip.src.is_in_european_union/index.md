<h1 id="ip-src-is-in-european-union">ip.src.is_in_european_union</h1>

**Data type:** Boolean

<p>Whether the request originates from a country in the European Union (EU).</p>

<p>Requires a Cloudflare Business or Enterprise plan.</p>
<p>Countries in the EU (from geolocation data):</p>
<table>
<thead>
<tr>
<th>Country code</th>
<th>Country name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>AT</code></td>
<td>Austria</td>
</tr>
<tr>
<td><code>AX</code></td>
<td>Åland Islands</td>
</tr>
<tr>
<td><code>BE</code></td>
<td>Belgium</td>
</tr>
<tr>
<td><code>BG</code></td>
<td>Bulgaria</td>
</tr>
<tr>
<td><code>CY</code></td>
<td>Cyprus</td>
</tr>
<tr>
<td><code>CZ</code></td>
<td>Czechia</td>
</tr>
<tr>
<td><code>DE</code></td>
<td>Germany</td>
</tr>
<tr>
<td><code>DK</code></td>
<td>Denmark</td>
</tr>
<tr>
<td><code>EE</code></td>
<td>Estonia</td>
</tr>
<tr>
<td><code>ES</code></td>
<td>Spain</td>
</tr>
<tr>
<td><code>FI</code></td>
<td>Finland</td>
</tr>
<tr>
<td><code>FR</code></td>
<td>France</td>
</tr>
<tr>
<td><code>GF</code></td>
<td>French Guiana</td>
</tr>
<tr>
<td><code>GP</code></td>
<td>Guadeloupe</td>
</tr>
<tr>
<td><code>GR</code></td>
<td>Greece</td>
</tr>
<tr>
<td><code>HR</code></td>
<td>Croatia</td>
</tr>
<tr>
<td><code>HU</code></td>
<td>Hungary</td>
</tr>
<tr>
<td><code>IE</code></td>
<td>Ireland</td>
</tr>
<tr>
<td><code>IT</code></td>
<td>Italy</td>
</tr>
<tr>
<td><code>LT</code></td>
<td>Lithuania</td>
</tr>
<tr>
<td><code>LU</code></td>
<td>Luxembourg</td>
</tr>
<tr>
<td><code>LV</code></td>
<td>Latvia</td>
</tr>
<tr>
<td><code>MF</code></td>
<td>Saint Martin</td>
</tr>
<tr>
<td><code>MQ</code></td>
<td>Martinique</td>
</tr>
<tr>
<td><code>MT</code></td>
<td>Malta</td>
</tr>
<tr>
<td><code>NL</code></td>
<td>The Netherlands</td>
</tr>
<tr>
<td><code>PL</code></td>
<td>Poland</td>
</tr>
<tr>
<td><code>PT</code></td>
<td>Portugal</td>
</tr>
<tr>
<td><code>RE</code></td>
<td>Réunion</td>
</tr>
<tr>
<td><code>RO</code></td>
<td>Romania</td>
</tr>
<tr>
<td><code>SE</code></td>
<td>Sweden</td>
</tr>
<tr>
<td><code>SI</code></td>
<td>Slovenia</td>
</tr>
<tr>
<td><code>SK</code></td>
<td>Slovakia</td>
</tr>
<tr>
<td><code>YT</code></td>
<td>Mayotte</td>
</tr>
</tbody>
</table>
<p>This field has the same value as the <code>ip.geoip.is_in_european_union</code> field, which is deprecated. The <code>ip.geoip.is_in_european_union</code> field is still available for new and existing rules, but you should use the <code>ip.src.is_in_european_union</code> field instead.</p>
<p><em>GeoIP is the registered trademark of MaxMind, Inc.</em></p>

<h2 id="categories">Categories</h2>

- Request
- Geolocation

**Keywords:** request, location, geolocation, ip.geoip.is_in_european_union, country, client, visitor

