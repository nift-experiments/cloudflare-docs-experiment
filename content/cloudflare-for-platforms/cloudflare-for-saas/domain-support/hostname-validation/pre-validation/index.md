<p>Pre-validation methods help verify domain ownership before your customer's traffic is proxying through Cloudflare.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="not-supported-for-o2o-custom-hostnames">Not supported for O2O custom hostnames</h3>
@markup("md", "content/.markup/bodies/4118.md")
</aside>
<h2 id="use-when">Use when</h2>
<p>Use pre-validation methods when your customers cannot tolerate any downtime, which often occurs with production domains.</p>
<p>The downside is that these methods require an additional setup step for your customers. Especially if you already need them to add something to their domain for <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/">certificate validation</a>, pre-validation might make their onboarding more complicated.</p>
<p>If your customers can tolerate a bit of downtime and you want their setup to be simpler, review our <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/realtime-validation/">real-time validation methods</a>.</p>
<h2 id="how-to">How to</h2>
<h3 id="txt-records">TXT records</h3>
<p>TXT validation is when your customer adds a <code>TXT</code> record to their authoritative DNS to verify domain ownership.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4117.md")
</aside>
<p>To set up <code>TXT</code> validation:</p>
<ol>
<li>When you <a href="/api/resources/custom_hostnames/methods/create/">create a custom hostname</a>, save the <code>ownership_verification</code> information.</li>
</ol>
<pre><code class="language-json">{&#10;&quot;result&quot;: [&#10;    {&#10;    &quot;id&quot;: &quot;3537a672-e4d8-4d89-aab9-26cb622918a1&quot;,&#10;    &quot;hostname&quot;: &quot;app.example.com&quot;,&#10;    // ...&#10;    &quot;status&quot;: &quot;pending&quot;,&#10;    &quot;verification_errors&quot;: [&quot;custom hostname does not CNAME to this zone.&quot;],&#10;    &quot;ownership_verification&quot;: {&#10;        &quot;type&quot;: &quot;txt&quot;,&#10;        &quot;name&quot;: &quot;_cf-custom-hostname.app.example.com&quot;,&#10;        &quot;value&quot;: &quot;0e2d5a7f-1548-4f27-8c05-b577cb14f4ec&quot;&#10;    },&#10;    &quot;created_at&quot;: &quot;2020-03-04T19:04:02.705068Z&quot;&#10;    }&#10;]&#10;}&#10;</code></pre>
<ol start="2">
<li>
<p>Have your customer add a <code>TXT</code> record with that <code>name</code> and <code>value</code> at their authoritative DNS provider.</p>
</li>
<li>
<p>After a few minutes, you will see the hostname status become <strong>Active</strong> in the UI.</p>
</li>
<li>
<p>Once you activate the custom hostname, your customer can remove the <code>TXT</code> record.</p>
</li>
</ol>
<h3 id="http-tokens">HTTP tokens</h3>
<p>HTTP validation is when you or your customer places an HTTP token on their origin server to verify domain ownership.</p>
<p>To set up HTTP validation:</p>
<p>When you <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/issue-certificates/">create a custom hostname</a> using the API, Cloudflare provides an HTTP <code>ownership_verification</code> record in the response.</p>
<p>To get and use the <code>ownership_verification</code> record:</p>
<ol>
<li>
<p>Make an API call to <a href="/api/resources/custom_hostnames/methods/create/">create a Custom Hostname</a>.</p>
</li>
<li>
<p>In the response, copy the <code>http_url</code> and <code>http_body</code> from the <code>ownership_verification_http</code> object:</p>
</li>
</ol>
<pre><code class="language-json">{&#10;  &quot;result&quot;: [&#10;    {&#10;      &quot;id&quot;: &quot;24c8c68e-bec2-49b6-868e-f06373780630&quot;,&#10;      &quot;hostname&quot;: &quot;app.example.com&quot;,&#10;      // ...&#10;      &quot;ownership_verification_http&quot;: {&#10;          &quot;http_url&quot;: &quot;http://app.example.com/.well-known/cf-custom-hostname-challenge/24c8c68e-bec2-49b6-868e-f06373780630&quot;,&#10;          &quot;http_body&quot;: &quot;48b409f6-c886-406b-8cbc-0fbf59983555&quot;&#10;      },&#10;      &quot;created_at&quot;: &quot;2020-03-04T20:06:04.117122Z&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<ol start="3">
<li>Have your customer place the <code>http_url</code> and <code>http_body</code> on their origin web server.</li>
</ol>
<pre><code class="language-txt">location &quot;/.well-known/cf-custom-hostname-challenge/24c8c68e-bec2-49b6-868e-f06373780630&quot; {&#10;    return 200 &quot;48b409f6-c886-406b-8cbc-0fbf59983555\n&quot;;&#10;}&#10;</code></pre>
<p>Cloudflare will access this token by sending <code>GET</code> requests to the <code>http_url</code> using <code>User-Agent: Cloudflare Custom Hostname Verification</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4116.md")
</aside>
<ol start="4">
<li>
<p>After a few minutes, you will see the hostname status become <strong>Active</strong> in the UI.</p>
</li>
<li>
<p>Once the hostname is active, your customer can remove the token from their origin server.</p>
</li>
</ol>
<h2 id="zero-downtime-migration-with-http-dcv">Zero-downtime migration with HTTP DCV</h2>
<p>When onboarding a customer whose hostname is already live with another provider, you can use pre-validation combined with manual HTTP DCV to achieve zero-downtime migration:</p>
<ol>
<li>Create the custom hostname with <code>&quot;ssl&quot;: {&quot;method&quot;: &quot;http&quot;, &quot;type&quot;: &quot;dv&quot;}</code>.</li>
<li>Complete <a href="#pre-validate-with-a-txt-record">hostname ownership pre-validation</a> using a TXT record so the hostname reaches <code>status: active</code>.</li>
<li>Wait for the <code>ssl.validation_records</code> to populate with the HTTP DCV token (an <code>http_url</code> and <code>http_body</code> pair).</li>
<li>Ask your customer to serve the DCV token at the <code>http_url</code> path on their current live origin. The certificate authority will validate it against the current DNS target.</li>
<li>Once <code>ssl.status</code> reaches <code>active</code>, the hostname and certificate are both ready.</li>
<li>Your customer can now update their DNS CNAME to point to your SaaS target with no interruption — the certificate is already issued.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4115.md")
</aside>
