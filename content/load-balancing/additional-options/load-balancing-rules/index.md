<p>Custom load balancing rules let you customize the behavior of your load balancer based on the characteristics of a request.</p>
<p>For example, you can use URL-based routing, or create a rule that selects a pool based on the URI path of an HTTP request.</p>
<h2 id="how-custom-rules-work">How custom rules work</h2>
<p>As with <a href="/waf/custom-rules/">WAF custom rules</a>, each load balancing custom rule is a combination of two elements: an <a href="/load-balancing/additional-options/load-balancing-rules/expressions/">expression</a> and an <a href="/load-balancing/additional-options/load-balancing-rules/actions/">action</a>. Expressions define the criteria for an HTTP request to trigger an action. The action tells Cloudflare how to handle the request.</p>
<p>You can <a href="/load-balancing/additional-options/load-balancing-rules/create-rules/">create Load Balancing rules</a> whenever you create or edit a load balancer in <strong>Load Balancing</strong>.</p>
<p>When building expressions for Load Balancing rules, refer to <a href="/load-balancing/additional-options/load-balancing-rules/reference/">Supported fields and operators</a> for definitions and usage.</p>
<h2 id="availability">Availability</h2>
<p>By default, non-Enterprise customers have <strong>one</strong> Load Balancing rule <strong>per load balancer hostname</strong>. For more rules, upgrade to <a href="https://www.cloudflare.com/enterprise/">Enterprise</a>.</p>
<h2 id="limitations">Limitations</h2>
<p>At the moment, you cannot use Load Balancing rules with <a href="/spectrum/about/load-balancer/">Cloudflare Spectrum</a>.</p>
<p>Custom rules can override <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/">Geo steering</a> pool mappings for matched requests. Specify different region, country, or data center pools in the rule. Changing only the steering policy does not disable Geo steering. Cloudflare still resolves pools from the configured topology before applying that policy.</p>
<p>Custom rules do work alongside <a href="/load-balancing/understand-basics/traffic-steering/pool-sets/">pool sets</a>. Cloudflare evaluates pool sets first, then applies custom rule overrides on top of the result. A pool set that returns a fixed response is the complete response, so custom rules are not evaluated for that request.</p>
