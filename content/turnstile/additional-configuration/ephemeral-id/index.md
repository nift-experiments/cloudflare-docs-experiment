<p>Ephemeral IDs are short-lived device identifiers that Turnstile generates for each visitor interaction. Unlike IP-based detection, Ephemeral IDs link visitor behavior to a specific client device without relying on cookies or client-side storage. This makes them effective against attackers who change IP addresses between requests.</p>
<h2 id="how-ephemeral-ids-work">How Ephemeral IDs work</h2>
<p>Ephemeral IDs are dynamically generated for each Turnstile solve attempt. No cookies or local storage is required.</p>
<p>Ephemeral IDs are scoped to your Cloudflare account and cannot be shared across accounts. IDs expire within a few days and cannot be used to identify individual users.</p>
<p>This approach is particularly effective against credential stuffing and fake account creation attacks, where attackers rotate IP addresses to evade detection.</p>
<p>Refer to the <a href="https://blog.cloudflare.com/turnstile-ephemeral-ids-for-fraud-detection/">blog post</a> for more information.</p>
<hr />
<h2 id="implementation">Implementation</h2>
<h3 id="enable-ephemeral-ids">Enable Ephemeral IDs</h3>
<ol>
<li>Contact your Cloudflare account team to enable Ephemeral ID entitlement for your account. This feature requires Enterprise-level access and cannot be self-activated.</li>
<li>After entitlement is enabled, activate Ephemeral IDs for specific widgets using the Cloudflare API.</li>
</ol>
<pre><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/challenges/widgets/$WIDGET_ID&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;ephemeral_id&quot;: true&#10;  }&#x27;&#10;</code></pre>
<ol start="3">
<li>Confirm Ephemeral IDs are active by checking your widget configuration.</li>
</ol>
<pre><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/challenges/widgets/$WIDGET_ID&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<h3 id="access-ephemeral-ids">Access Ephemeral IDs</h3>
<p>Once enabled, Ephemeral IDs are included in Siteverify API responses.</p>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;challenge_ts&quot;: &quot;2022-02-28T15:14:30.096Z&quot;,&#10;	&quot;hostname&quot;: &quot;example.com&quot;,&#10;	&quot;error-codes&quot;: [],&#10;	&quot;action&quot;: &quot;login&quot;,&#10;	&quot;cdata&quot;: &quot;sessionid-123456789&quot;,&#10;	&quot;metadata&quot;: {&#10;		&quot;ephemeral_id&quot;: &quot;x:9f78e0ed210960d7693b167e&quot;&#10;	}&#10;}&#10;</code></pre>
<hr />
<h2 id="availability">Availability</h2>
<p>Ephemeral IDs are available to Enterprise Bot Management customers with the Enterprise Turnstile add-on or standalone Enterprise Turnstile customers. Contact your account team for access to Ephemeral IDs.</p>
