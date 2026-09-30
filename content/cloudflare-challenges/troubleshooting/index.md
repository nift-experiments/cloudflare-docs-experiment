<h2 id="common-issues">Common issues</h2>
<h3 id="proxied-hostnames">Proxied hostnames</h3>
<p>If your hostname is proxied through Cloudflare, visitors may experience challenges on your webpages.</p>
<p>Cloudflare issues challenges through the <a href="/cloudflare-challenges/">Challenge Platform</a>, which is the same underlying technology powering <a href="/turnstile/">Turnstile</a>.</p>
<p>In contrast to our Challenge page offerings, Turnstile allows you to run challenges anywhere on your site in a less-intrusive way without requiring the use of Cloudflare's CDN.</p>
<h3 id="deprecated-browser-support">Deprecated browser support</h3>
<p>Challenges are not supported by Microsoft Internet Explorer. If you are currently using Internet Explorer, try using another modern web browser (Chrome, Safari, Firefox). If you are already using a modern web browser, make sure it is using the latest version.</p>
<h3 id="referer-header">Referer header</h3>
<p>Your visitor's HTTP request contains a referer header set to the website that they came from. When they encounter and solve a Challenge Page, the request with the referer is sent to the origin, and the response to the request is served to the user. The JavaScript on the response page may read the value of <code>document.referer</code>, but it will not be accurate.</p>
<p>For example, a visitor coming from a given website is challenged by a <a href="/waf/custom-rules/">WAF rule</a> via an interstitial Challenge Page served by your domain. Once the visitor loads the website's home page, the <code>document.referer</code> value is your domain, not the origin website.</p>
<p>This affects tools like Google Analytics, which reads the referer from JavaScript, since it replaces the previous website that visitors came from.</p>
<p>You can add tracking scripts, such as the Google Tag Manager Javascript, within an existing <a href="/rules/custom-errors/">Challenge Page</a> to capture the correct referer header on the initial request.</p>
<pre><code class="language-js">&lt;script&gt;&#10;    (function () {&#10;      const gaIds = {&#10;        &quot;&lt;YOUR_DOMAIN&gt;&quot;: &quot;&lt;GA_TRACKING_ID&gt;&quot;,&#10;      };&#10;&#10;      const gaId = gaIds[window.location.hostname];&#10;&#10;      if (gaId) {&#10;        const src = &quot;https://www.googletagmanager.com/gtag/js?id=&quot;;&#10;&#10;        const gaScript = document.createElement(&quot;script&quot;);&#10;        gaScript.src = src.concat(gaId);&#10;        document.body.appendChild(gaScript);&#10;&#10;        window.dataLayer = window.dataLayer || [];&#10;        function gtag() {&#10;          dataLayer.push(arguments);&#10;        }&#10;        gtag(&quot;js&quot;, new Date());&#10;        gtag(&quot;config&quot;, gaId);&#10;      } else {&#10;        console.warn(&#10;          &quot;Google Analytics ID not found for host:&quot;,&#10;          window.location.hostname,&#10;        );&#10;      }&#10;    })();&#10;  &lt;/script&gt;&#10;&lt;/body&gt;&#10;</code></pre>
<h3 id="cross-origin-resource-sharing-cors-preflight-requests">Cross-origin resource sharing (CORS) preflight requests</h3>
<p>Cross-origin resource sharing (CORS) preflight requests, or <code>OPTIONS</code>, exclude user credentials that include cookies. As a result, the <code>cf_clearance</code> cookie will not be sent with the request, causing it to fail to bypass a Challenge Page (Non-interactive, Managed, or Interactive Challenge).</p>
<h3 id="challenges-on-cloudflare-protected-sites">Challenges on Cloudflare-protected sites</h3>
<p>Cloudflare issues challenges to website visitors to protect against malicious activity, such as bot attacks and DDoS attempts. If a legitimate human visitor is unexpectedly challenged, the reason typically stems from a security feature flagging their request.</p>
<table>
<thead>
<tr>
<th>Source</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>High threat score</td>
<td>IP addresses with a high-risk score trigger Challenges.</td>
</tr>
<tr>
<td>IP reputation</td>
<td>If your IP has a history of suspicious activity, it may be flagged.</td>
</tr>
<tr>
<td>Bot detection</td>
<td>Automated traffic resembling bots is filtered by Cloudflare.</td>
</tr>
<tr>
<td>Web Application Firewall (WAF) custom rules</td>
<td>Site owners may set rules targeting specific regions or user agents.</td>
</tr>
<tr>
<td>Browser Integrity Check</td>
<td>Cloudflare verifies that browsers meet certain standards.</td>
</tr>
<tr>
<td>Challenge Passage</td>
<td>Technologies like Privacy Pass reduce the frequency of repeated Challenges.</td>
</tr>
</tbody>
</table>
<p>To avoid repeated challenges, visitors can take the following steps to ensure their environment does not trigger security checks:</p>
<ul>
<li>Ensure your web browser is updated to the latest stable version for full compatibility with modern challenge technologies.</li>
<li>Temporarily disable browser extensions, such as ad blockers or privacy tools, that may block standard browser headers or the necessary challenge scripts.</li>
<li>If your IP address has a poor reputation (often seen with shared VPNs or corporate proxies), try switching to a different, trusted network connection.</li>
</ul>
<h3 id="allowlist-traffic-from-mitigation-actions">Allowlist traffic from mitigation actions</h3>
<p>If you need to prevent a <strong>Block</strong> or <strong>Challenge</strong> action from being applied to specific requests, such as known search engine crawlers, monitoring services, or internal APIs, you must configure an exclusion using <a href="/waf/custom-rules/">WAF custom rules</a>.</p>
<p>Cloudflare supports two primary methods for creating these exclusions:</p>
<h4 id="1-use-a-skip-rule-recommended"><ol>
<li>Use a Skip rule (recommended)</li>
</ol></h4>
<p>The most robust method for creating an exception is to create a custom rule with the <strong>Skip</strong> action. This allows matching requests to bypass certain security features, including Bot Management and other WAF rules.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4021.md")
</aside>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4022.md")
</div></details>
<h4 id="2-modify-the-rule-expression"><ol start="2">
<li>Modify the Rule Expression</li>
</ol></h4>
<p>You can refine the expression of a <strong>Block</strong> or <strong>Challenge</strong> rule to directly exclude known good traffic by using the logical not operator with an exclusion list, such as an IP list, country code, or ASN.</p>
<p>This approach is useful for simple exclusions but can make complex rules more difficult to maintain than separate <strong>Skip</strong> rules.</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4023.md")
</div></details>
