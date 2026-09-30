<h2 id="ruleset-engine-fields">Ruleset Engine fields</h2>
<p>Bot Management provides access to several <a href="/ruleset-engine/rules-language/fields/reference/?field-category=Bots">fields</a> within the expression builder of Ruleset Engine-based products such as <a href="/waf/custom-rules/">WAF custom rules</a> and <a href="/cache/how-to/cache-rules/">Cache Rules</a>.</p>
<ul>
<li>
<p><strong>Bot Score</strong> (<code>cf.bot_management.score</code>): An integer between 1-99 that indicates <a href="/bots/concepts/bot-score/">Cloudflare's level of certainty</a> that a request comes from a bot.</p>
</li>
<li>
<p><strong>Verified Bot</strong> (<code>cf.bot_management.verified_bot</code>): A boolean value that indicates whether a request originates from a Cloudflare allowed bot.</p>
<p>Cloudflare maintains a large allowlist of good, automated bots (such as Google Search Engine and Pingdom) that perform beneficial tasks. Cloudflare identifies and verifies these bots primarily through reverse DNS validation, ensuring the source IP matches the requesting service.</p>
<p>We also use additional validation methods, including checking ASN blocks and public lists. If these methods are unavailable, Cloudflare utilizes internal data and machine learning to identify and verify legitimate IP addresses from good bots. Most customers choose to <a href="/ruleset-engine/rules-language/fields/reference/cf.bot_management.verified_bot/">allow this traffic</a>.</p>
</li>
<li>
<p><strong>Serves Static Resource</strong> (<code>cf.bot_management.static_resource</code>): An identifier that matches <a href="/bots/additional-configurations/static-resources/">file extensions</a> for many types of static resources. Use this variable if you send emails that retrieve static images.</p>
</li>
<li>
<p><strong>ja3Hash</strong> (<code>cf.bot_management.ja3_hash</code>) and <strong>ja4</strong> (<code>cf.bot_management.ja4</code>): A <a href="/bots/additional-configurations/ja3-ja4-fingerprint/"><strong>JA3/JA4 fingerprint</strong></a> helps you profile specific SSL/TLS clients across different destination IPs, Ports, and X509 certificates.</p>
</li>
<li>
<p><strong>Bot Detection IDs</strong> (<code>cf.bot_management.detection_ids</code>): List of IDs that correlate to the Bot Management heuristic detections made on a request (you can have multiple heuristic detections on the same request).</p>
</li>
<li>
<p><strong>Bot Tags</strong> (<code>cf.bot_management.tags</code>): A list of tags associated with bot traffic.</p>
</li>
<li>
<p><strong>Signed Agent</strong> (<code>cf.bot_management.signed_agent</code>): A boolean value that indicates whether the request originated from a known agent that self-identifies with Web Bot Auth. Such agents are now classified as <a href="/bots/concepts/bot/verified-bots/">verified bots and agents</a> labeled as intermediary.</p>
</li>
<li>
<p><strong>Verified Bot Categories</strong> (<code>cf.verified_bot_category</code>): A string that allows you to segment your verified bot traffic by its <a href="/bots/concepts/bot/verified-bots/#legacy-categories">type and purpose</a>.</p>
</li>
</ul>
<h2 id="workers-variables">Workers variables</h2>
<p>These variables are also available as part of the <a href="/workers/runtime-apis/request/#incomingrequestcfproperties">request.cf</a> object via Cloudflare Workers:</p>
<ul>
<li><code>request.cf.botManagement.score</code></li>
<li><code>request.cf.botManagement.verifiedBot</code></li>
<li><code>request.cf.botManagement.staticResource</code></li>
<li><code>request.cf.botManagement.ja3Hash</code></li>
<li><code>request.cf.botManagement.ja4</code></li>
<li><code>request.cf.botManagement.jsDetection.passed</code></li>
<li><code>request.cf.botManagement.detectionIds</code></li>
<li><code>request.cf.botManagement.signedAgent</code></li>
<li><code>request.cf.verifiedBotCategory</code></li>
</ul>
<h2 id="o2o-and-subrequests">O2O and subrequests</h2>
<p>For Orange-to-Orange (O2O) traffic and any related subrequests where Bot Management is in effect, Bot Management fields (including bot score, verified bot, and JA3/JA4) represent the eyeball (end-user) connection to your platform.</p>
<p>Eyeball signals are preserved through the O2O chain, so the fields must be present regardless of which O2O request path you reach.</p>
<h2 id="corporate-proxy">Corporate Proxy</h2>
<p>The Bot Management Corporate Proxy field contains identified cloud-based corporate proxies and secure web gateways that are Enterprise-only, and provide outbound security services to their clients.</p>
<p>You can access the Corporate Proxy field in <a href="/waf/custom-rules/">WAF custom rules</a>, <a href="/waf/rate-limiting-rules/">Rate limiting rules</a>, or <a href="/workers/">Workers</a> to provide different security rules for traffic from these sources. You can also exempt them from rules using Bot Management scores.</p>
<pre><code class="language-txt">not cf.bot_management.verified_bot&#10;and not cf.bot_management.static_resource&#10;and not  cf.bot_management.corporate_proxy&#10;and cf.bot_management.score lt 30&#10;</code></pre>
<h2 id="log-fields">Log fields</h2>
<p>Once you enable Bot Management, Cloudflare also surfaces bot information in its <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP requests log fields</a>:</p>
<ul>
<li>BotDetectionIDs</li>
<li>BotScore</li>
<li>BotScoreSrc</li>
<li>BotTags</li>
</ul>
<h2 id="ephemeral-ids">Ephemeral IDs</h2>
<p><a href="/turnstile/additional-configuration/ephemeral-id/">Ephemeral IDs</a> are short-lived device identifiers returned in the <a href="/turnstile/get-started/server-side-validation/">Turnstile Siteverify API</a> response under <code>metadata.ephemeral_id</code>. They are not Ruleset Engine fields and cannot be used in WAF custom rules or Workers directly.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3468.md")
</aside>
<p>Refer to <a href="/turnstile/additional-configuration/ephemeral-id/">Ephemeral IDs</a> for implementation details and the full enablement process.</p>
