<p>Use <a href="/waf/custom-rules/">Custom rules</a> to allow you to control incoming traffic by filtering requests to a zone. They work as customized web application firewall (WAF) rules that you can use to perform actions like Block or Managed Challenge on incoming requests.</p>
<p>Use WAF <a href="/waf/managed-rules/">Managed Rules</a> to apply custom criteria for all incoming HTTP requests.</p>
<h2 id="understand-hosting-plan-limits">Understand hosting plan limits</h2>
<p>Cloudflare offsets most of the load to your website via caching and request filtering, but some traffic will still pass through to your origin. Knowing the limits of your hosting plan can help prevent a bottleneck from your host.</p>
<p>Once you are aware of your plan limits, you can use <a href="/waf/rate-limiting-rules/">Rate Limiting</a> to restrict how many times a requesting entity can make a request to your website.</p>
<p>To help you define the best rate limiting setting for your use case, refer to <a href="/waf/rate-limiting-rules/request-rate/">How Cloudflare determines the request rate</a>.</p>
<h2 id="security-models">Security models</h2>
<ul>
<li>Positive Security policy: Allow specific requests and deny everything else.</li>
<li>Negative Security policy: Block specific requests and allow everything else.</li>
</ul>
<h2 id="actions">Actions</h2>
<ul>
<li>Log: Test rule effectiveness before committing to a more severe action.</li>
<li>Allow: Allow matching requests to access the site.</li>
<li>Block: Block matching requests from accessing the site.</li>
<li>Non-Interactive Challenge: Visitors will be shown a non-interactive challenge before proceeding.</li>
<li>Interactive Challenge: Visitors will be shown an interactive challenge before proceeding.</li>
</ul>
