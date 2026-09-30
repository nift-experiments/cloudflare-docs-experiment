<p><a href="https://github.com/salesforce/ja3"><strong>JA3</strong></a> and <a href="https://github.com/FoxIO-LLC/ja4"><strong>JA4</strong></a> <strong>fingerprints</strong> identify TLS clients based on how they initiate connections. Each client type (browser, bot, or application) has distinct connection characteristics, so the resulting fingerprint acts as a stable identifier across different destination IPs, ports, and certificates.</p>
<p>JA4 improves on JA3 by sorting ClientHello extensions, which reduces the number of unique fingerprints for modern browsers and makes grouping easier.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3544.md")
</aside>
<p>If you want to use JA4 fingerprints and Signals Intelligence, your Workers script should be able to handle missing fields when Bot Management isn't able to calculate or populate JA4 Signals (for example, non-TLS traffic or when Bot Management is skipped). For Orange-to-Orange (O2O) scenarios where Bot Management is in effect, JA4 Signals correspond to the eyeball (end-user) connection and are preserved through the O2O chain, including O2O zone requests and any corresponding subrequests.</p>
<ul>
<li>The possibility that the JA4 fingerprint could be missing.</li>
<li>The possibility that the <code>ja4Signals</code> array could be missing (for example, if JA4 isn't available for the request).</li>
<li>Results with <code>NaN</code> or <code>Infinity</code> values will be excluded from the array.</li>
</ul>
<pre><code class="language-json">&#10;{&#10;  &quot;ja4Signals&quot;: {&#10;    &quot;h2h3_ratio_1h&quot;: 0.98826485872269,&#10;    &quot;heuristic_ratio_1h&quot;: 7.288895722013e-05,&#10;    &quot;reqs_quantile_1h&quot;: 0.99905741214752,&#10;    &quot;uas_rank_1h&quot;: 901,&#10;    &quot;browser_ratio_1h&quot;: 0.93640440702438,&#10;    &quot;paths_rank_1h&quot;: 655,&#10;    &quot;reqs_rank_1h&quot;: 850,&#10;    &quot;cache_ratio_1h&quot;: 0.18918327987194,&#10;    &quot;ips_rank_1h&quot;: 662,&#10;    &quot;ips_quantile_1h&quot;: 0.99926590919495&#10;  },&#10;  &quot;jaSignalsParsed&quot;: {&#10;    &quot;ratios&quot;: {&#10;      &quot;h2h3_ratio_1h&quot;: 0.98826485872269,&#10;      &quot;heuristic_ratio_1h&quot;: 7.288895722013e-05,&#10;      &quot;browser_ratio_1h&quot;: 0.93640440702438,&#10;      &quot;cache_ratio_1h&quot;: 0.18918327987194&#10;    },&#10;    &quot;ranks&quot;: {&#10;      &quot;uas_rank_1h&quot;: 901,&#10;      &quot;paths_rank_1h&quot;: 655,&#10;      &quot;reqs_rank_1h&quot;: 850,&#10;      &quot;ips_rank_1h&quot;: 662&#10;    },&#10;    &quot;quantiles&quot;: {&#10;      &quot;reqs_quantile_1h&quot;: 0.99905741214752,&#10;      &quot;ips_quantile_1h&quot;: 0.99926590919495&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>When JA4 Signals are missing, the output appears as follows:</p>
<pre><code class="language-json">{&#10;  &quot;ja4Signals&quot;: {},&#10;  &quot;jaSignalsParsed&quot;: {&#10;    &quot;ratios&quot;: {},&#10;    &quot;ranks&quot;: {},&#10;    &quot;quantiles&quot;: {}&#10;  }&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3543.md")
</aside>
<p>The JA3 or JA4 fingerprint is an SSL/TLS-based identifier and can be null or empty in logs under specific circumstances:</p>
<ul>
<li>Since JA3 and JA4 are calculated during the TLS (SSL) handshake, they will not be present for non-encrypted HTTP traffic.</li>
<li>The field may be empty when a <a href="/workers/">Worker</a> sends a request to a zone that is either internal to Cloudflare's network (for example, non-proxied/internal O2O) or to a third-party origin, or when a Worker is routing traffic to the target zone.</li>
<li>The fingerprints may be absent when Bot Management itself is skipped for a request, as the feature is responsible for calculating and populating these values.</li>
<li>With <a href="https://blog.cloudflare.com/tls-session-resumption-full-speed-and-secure/">TLS Session Resumption</a>, once the initial TLS handshake is successfully completed, subsequent connections will be streamlined. This results in no further fingerprint calculation.</li>
</ul>
<p>In <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/">Orange-to-Orange (O2O)</a> scenarios where Bot Management is in effect, JA3/JA4 fingerprints are preserved through the O2O chain and represent the eyeball (end-user) connection. This includes requests on the O2O zone and any corresponding subrequests.</p>
<h2 id="analytics">Analytics</h2>
<p>To get more information about potential bot requests, use these JA3 and JA4 fingerprints in:</p>
<ul>
<li><a href="/bots/bot-analytics/#enterprise-bot-management">Bot Analytics</a></li>
<li><a href="/waf/analytics/security-events/">Security Events</a> and <a href="/waf/analytics/security-analytics/">Security Analytics</a></li>
<li><a href="/analytics/graphql-api/">Analytics GraphQL API</a>, specifically the <strong>HTTP Requests</strong> dataset</li>
<li><a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">Logs</a></li>
</ul>
<h2 id="actions">Actions</h2>
<p>To adjust how your application responds to specific fingerprints, use them with:</p>
<ul>
<li><a href="/waf/custom-rules/">WAF custom rules</a></li>
<li><a href="/rules/transform/">Transform Rules</a></li>
<li><a href="/workers/runtime-apis/request/#incomingrequestcfproperties">Cloudflare Workers</a></li>
</ul>
<h2 id="use-cases">Use cases</h2>
<h3 id="block-or-allow-certain-traffic">Block or allow certain traffic</h3>
<p>A group of similar requests may share the same JA3 fingerprint. For this reason, JA3 may be useful in blocking an incoming threat. For example, if you notice that a bot attack is not caught by existing defenses, create a <a href="/waf/custom-rules/">custom rule</a> that blocks or challenges the JA3 used for the attack.</p>
<p>Alternatively, if existing defenses are blocking traffic that is actually legitimate, create a <a href="/waf/custom-rules/">custom rule</a> with the <em>Skip</em> action allowing the JA3 seen across good requests.</p>
<p>JA3 may also be useful if you want to immediately remedy false positives or false negatives with Bot Management.</p>
<h3 id="allow-mobile-traffic">Allow mobile traffic</h3>
<p>Often, mobile application traffic will produce the same JA3 fingerprint across devices and users. This means you can identify your mobile application traffic by its JA3 fingerprint.</p>
<p>Use the JA3 fingerprint to <a href="/waf/custom-rules/use-cases/challenge-bad-bots/#adjust-for-mobile-traffic">allow traffic</a> from your mobile application, but block or challenge remaining traffic.</p>
