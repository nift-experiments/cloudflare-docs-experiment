<p>Challenges can be issued in three primary ways depending on which Cloudflare products or features are in use. Each method is designed to balance security with seamless visitor experience.</p>
<table>
<thead>
<tr>
<th>Product</th>
<th>Challenge type(s)</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/waf/">WAF</a> (<a href="/waf/custom-rules/">custom rules</a>, <a href="/waf/rate-limiting-rules/">rate limiting rules</a>, <a href="/waf/tools/ip-access-rules/">IP access rules</a>)</td>
<td><a href="/cloudflare-challenges/challenge-types/challenge-pages/">Interstitial Challenge Page</a></td>
</tr>
<tr>
<td><a href="/bots/get-started/bot-management/">Bot Management</a></td>
<td><a href="/bots/additional-configurations/javascript-detections/">JavaScript Detections</a></td>
</tr>
<tr>
<td><a href="/bots/get-started/bot-fight-mode/">Bot Fight Mode</a>, <a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a></td>
<td><a href="/cloudflare-challenges/challenge-types/challenge-pages/">Interstitial Challenge Page</a></td>
</tr>
<tr>
<td><a href="/turnstile/">Turnstile</a></td>
<td>Embedded widget</td>
</tr>
<tr>
<td><a href="/ddos-protection/managed-rulesets/http/">HTTP DDoS attack protection</a></td>
<td>Any Challenge</td>
</tr>
<tr>
<td><a href="/fundamentals/reference/under-attack-mode/">Under Attack Mode</a></td>
<td><a href="/cloudflare-challenges/challenge-types/challenge-pages/#managed-challenge">Managed Challenge</a></td>
</tr>
</tbody>
</table>
<p>Challenge Pages and Turnstile rely on the same underlying mechanism to issue challenges to your website or application's visitors.</p>
<p>JavaScript Detections is an optional feature within <a href="/bots/get-started/bot-management/">Bot Management</a>. When enabled, Cloudflare injects a JavaScript snippet into HTML responses to gather client-side signals. Unlike Challenge Pages, JavaScript Detections runs on every HTML request without pausing or interrupting the visitor. It populates a pass/fail result (<code>cf.bot_management.js_detection.passed</code>) that you can then act on using a <a href="/waf/custom-rules/">WAF custom rule</a>.</p>
<p>For session-level detection that informs when challenges should be applied, refer to <a href="/cloudflare-challenges/precursor/">Precursor</a>.</p>
<hr />
<h2 id="available-challenges">Available challenges</h2>
<p>Refer to the following pages for more information on the different challenge types:</p>
<ul>
<li><a href="/cloudflare-challenges/challenge-types/challenge-pages/">Interstitial Challenge Pages</a></li>
<li><a href="/cloudflare-challenges/challenge-types/turnstile/">Turnstile</a></li>
<li><a href="/cloudflare-challenges/challenge-types/javascript-detections/">JavaScript Detections</a></li>
<li><a href="/cloudflare-challenges/precursor/">Precursor</a></li>
</ul>
<hr />
<h2 id="limitations">Limitations</h2>
<p>Cloudflare Challenges cannot support the following:</p>
<ul>
<li><a href="/cloudflare-challenges/reference/supported-browsers/#browser-extensions">Browser extensions</a> that modify the browser's <code>User-Agent</code> value or Web APIs such as <code>Canvas</code> and <code>WebGL</code>.</li>
<li>Implementations where a domain serves a challenge page originally requested for another domain.</li>
<li>Challenge Pages cannot be embedded in cross-origin iframes.</li>
<li>Client software where the solve request of a Managed Challenge comes from a different IP than the original IP a Challenge request was issued to. For example, if you receive the Challenge from one IP and solve it using another IP, the solve is not valid and you may encounter a Challenge loop.</li>
</ul>
