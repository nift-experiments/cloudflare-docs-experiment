<h1 id="changelog">Changelog</h1>

<h2 id="cloud-connector-now-supports-r2"><a href="/changelog/post/2024-11-22-cloud-connector-r2/">Cloud Connector Now Supports R2</a></h2>
<p><em>2024-11-22</em></p>
<p>Now, you can use <a href="/rules/cloud-connector/">Cloud Connector</a> to route traffic to your <a href="/r2/">R2 buckets</a> based on URLs, headers, geolocation, and more.</p>
<p>Example setup:</p>
<pre><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/cloud_connector/rules&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;[&#10;  {&#10;    &quot;expression&quot;: &quot;http.request.uri.path wildcard \&quot;/images/*\&quot;&quot;,&#10;    &quot;provider&quot;: &quot;cloudflare_r2&quot;,&#10;    &quot;description&quot;: &quot;Connect to R2 bucket containing images&quot;,&#10;    &quot;parameters&quot;: {&#10;      &quot;host&quot;: &quot;mybucketcustomdomain.example.com&quot;&#10;    }&#10;  }&#10;]&#x27;&#10;</code></pre>
<p>Get started using <a href="/rules/cloud-connector/">Cloud Connector</a> documentation.</p>


<h2 id="simplified-ui-for-url-rewrites"><a href="/changelog/post/2024-10-23-url-rewrites-wildcard/">Simplified UI for URL Rewrites</a></h2>
<p><em>2024-10-23</em></p>
<p>It’s now easy to create <strong>wildcard-based <a href="/rules/transform/url-rewrite/">URL Rewrites</a></strong>. No need for complex functions—just define your patterns and go.</p>
<p><img src="/assets/upstream/images/rules/transform/create-url-rewrite-rule.png" alt="Rules Overview Interface" /></p>
<p>What’s improved:</p>
<ul>
<li><strong>Full wildcard support</strong> – Create rewrite patterns using intuitive interface.</li>
<li><strong>Simplified rule creation</strong> – No need for complex functions.</li>
</ul>
<p>Try it via <a href="/rules/transform/url-rewrite/create-dashboard/#wildcard-pattern-parameters">creating a Rewrite URL rule in the dashboard</a>.</p>


<h2 id="new-rules-templates-for-one-click-rule-creation"><a href="/changelog/post/2024-09-05-rules-templates/">New Rules Templates for One-Click Rule Creation</a></h2>
<p><em>2024-09-05</em></p>
<p>Now, you can create <strong>common rule configurations</strong> in just <strong>one click</strong> using Rules Templates.</p>
<p><img src="/assets/upstream/images/changelog/rules/rules-templates.gif" alt="Rules Templates" /></p>
<p>What you can do:</p>
<ul>
<li><strong>Pick a pre-built rule</strong> – Choose from a library of templates.</li>
<li><strong>One-click setup</strong> – Deploy best practices instantly.</li>
<li><strong>Customize as needed</strong> – Adjust templates to fit your setup.</li>
</ul>
<p>Template cards are now also available directly in the rule builder for each product.</p>
<p>Need more ideas? Check out the <a href="/rules/examples/">Examples gallery</a> in our documentation.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/application-security/8/">Previous</a><span>Page 9 of 9</span></nav>
