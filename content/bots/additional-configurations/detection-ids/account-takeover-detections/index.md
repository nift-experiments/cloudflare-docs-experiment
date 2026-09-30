<p>Using the detection IDs below, you can detect and mitigate account takeover attacks. You can monitor the number of login requests for a given software and network combination, as well as the percentage of login errors. When it reaches a suspicious level, you can prevent these attacks by using <a href="/waf/custom-rules/">custom rules</a>, <a href="/waf/rate-limiting-rules/">rate limiting rules</a>, and <a href="/workers/">Workers</a>.</p>
<table>
<thead>
<tr>
<th><span style="width:100px">Detection ID</span></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>201326592</code></td>
<td>Matches traffic that is making a suspicious amount of login failures to the zone.</td>
</tr>
<tr>
<td><code>201326593</code></td>
<td>Matches traffic that is making a suspicious amount of login attempts to the zone.</td>
</tr>
<tr>
<td><code>201326598</code></td>
<td>Sets a dynamic threshold based on the normal traffic that is unique to the zone.<br /><br /> When the ID matches a login failure, Bot Management sets the <a href="/bots/concepts/bot-score/">bot score</a> to 29 and uses <a href="/bots/concepts/bot-detection-engines/#anomaly-detection-enterprise">anomaly detection</a> as its score source.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="login-endpoints">Login endpoints</h3>
@markup("md", "content/.markup/bodies/3557.md")
</aside>
<h2 id="challenges-for-account-takeover-detections">Challenges for account takeover detections</h2>
<p>Cloudflare's <a href="/cloudflare-challenges/challenge-types/challenge-pages/#managed-challenge">Managed Challenge</a> can limit brute-force attacks on your login endpoints.</p>
<p>To access account takeover detections:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3558.md")
</div>
<pre><code class="language-js">&#10;(any(cf.bot_management.detection_ids[*] eq 201326593))&#10;</code></pre>
<h2 id="limit-logins-with-account-takeover-detections">Limit logins with account takeover detections</h2>
<p>Rate limiting rules can limit the number of logins from a particular IP, JA4 fingerprint, or country.</p>
<p>To use rate limiting rules with account takeover detections:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3559.md")
</div>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="enhanced-with-leaked-credential-detections">Enhanced with leaked credential detections</h3>
@markup("md", "content/.markup/bodies/3556.md")
</aside>
