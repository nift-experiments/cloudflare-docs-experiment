<p>Scraping behavioral detection IDs allow you to better protect your website from volumetric scraping attacks by identifying anomalous behavior. The detection IDs below are specifically designed to catch suspicious scraping activity at the zone level.</p>
<table>
<thead>
<tr>
<th><span style="width:100px">Detection ID</span></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>50331648</code></td>
<td>Observes patterns of requests sent to your zone, dynamically analyzing behavior by ASN.</td>
</tr>
<tr>
<td><code>50331649</code></td>
<td>Observes patterns of requests sent to your zone, dynamically analyzing behavior by JA4 fingerprint.</td>
</tr>
</tbody>
</table>
<h2 id="challenges-for-scraping-detections">Challenges for scraping detections</h2>
<p>Cloudflare's <a href="/cloudflare-challenges/challenge-types/challenge-pages/#managed-challenge">Managed Challenge</a> can limit scraping attacks on your website.</p>
<p>To access scraping detections:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3547.md")
</div>
<pre><code class="language-js">&#10;(any(cf.bot_management.detection_ids[*] in {50331648 50331649}) and not cf.bot_management.verified_bot)&#10;</code></pre>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="best-practice">Best practice</h3>
@markup("md", "content/.markup/bodies/3546.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3545.md")
</aside>
