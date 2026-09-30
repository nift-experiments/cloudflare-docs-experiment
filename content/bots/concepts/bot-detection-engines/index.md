<p>Cloudflare uses multiple detection engines because different bot types require different detection strategies. Simple bots can be caught by pattern matching against known signatures, while sophisticated bots require machine learning and behavioral analysis.</p>
<p>The engines available to your domain depend on your plan.</p>
<h2 id="heuristics">Heuristics</h2>
<p>The <strong>Heuristics</strong> engine processes all requests. Cloudflare conducts a number of heuristic checks to identify automated traffic, and requests are matched against a growing database of malicious fingerprints.</p>
<h2 id="javascript-detections">JavaScript detections</h2>
<p>The <a href="/bots/additional-configurations/javascript-detections/"><strong>JavaScript Detections (JSD)</strong></a> engine identifies headless browsers and other malicious fingerprints. This engine performs a lightweight, invisible JavaScript injection on the client side of any request while honoring our <a href="https://www.cloudflare.com/privacypolicy/">strict privacy standards</a>. We do not collect any personally identifiable information during the process. The JSD engine either blocks, challenges, or passes requests to other engines.</p>
<p>JSD is completely optional. To adjust your settings, configure Super Bot Fight Mode from <strong>Security</strong> &gt; <strong>Bots</strong>.</p>
<h2 id="machine-learning-business-and-enterprise">Machine Learning (Business and Enterprise)</h2>
<p>The <strong>Machine Learning (ML)</strong> engine accounts for the majority of all detections, distinguishing between human and bot traffic. This approach leverages our global network, which proxies billions of requests daily, to identify both automated and human traffic.</p>
<p>The ML system uses a supervised machine learning methodology to determine the final Bot Score (1–99).</p>
<p>The core model relies on the following process:</p>
<ul>
<li>Input Variables (X): Various request features (headers, session characteristics, and browser signals) collected from traffic across the Cloudflare network.</li>
<li>Output Variable (Y): The predicted probability that a client is human (such as the probability of successfully solving a Challenge). This probability is mapped to the final 1–99 Bot Score.</li>
</ul>
<p>We constantly train the ML engine on a periodic basis using vast, anonymized data to ensure it remains accurate and adapts to new threats. Customers can analyze the request features used by these models via their own logs, such as Cloudflare <a href="/logs/logpull/">Logpull</a> or <a href="/logs/logpush/">Logpush</a>.</p>
<p>The ML engine identifies <em>likely automated</em> traffic.</p>
<h2 id="anomaly-detection-enterprise">Anomaly detection (Enterprise)</h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/3522.md")
</aside>
<p>The <strong>Anomaly Detection (AD)</strong> engine is an optional detection engine that uses a form of unsupervised learning. Cloudflare records a baseline of your domain's traffic and uses the baseline to intelligently detect outlier requests. This approach is user agent-agnostic and can be turned on or off by your account team.</p>
<p>Cloudflare does not recommend AD for domains that use <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/">Cloudflare for SaaS</a> or expect large amounts of API traffic. The AD engine immediately gives automated requests a score of one.</p>
<h2 id="notes-on-detection">Notes on detection</h2>
<p>Cloudflare uses the <code>__cf_bm</code> cookie to smooth out the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3523.md")
</div> and reduce false positives for actual user sessions.
<p>The Bot Management cookie measures a single user's request pattern and applies it to the machine learning data to generate a reliable bot score for all of that user's requests.</p>
<p>For more details, refer to <a href="/fundamentals/reference/policies-compliances/cloudflare-cookies/">Cloudflare Cookies</a>.</p>
<p>You can disable the <code>__cf_bm</code> cookie using the <code>bm_cookie_enabled</code> field <a href="/api/resources/bot_management/methods/update/">via the API</a>.</p>
