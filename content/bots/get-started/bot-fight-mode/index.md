<p>Bot Fight Mode is a simple, free product that helps detect and mitigate bot traffic on your domain. When enabled, the product:</p>
<ul>
<li>Identifies traffic matching patterns of known bots</li>
<li>Issues computationally expensive challenges that force the requesting client to perform CPU-intensive calculations, increasing the cost for bots to send automated requests</li>
<li>Notifies <a href="https://cloudflare.com/bandwidth-alliance/">Bandwidth Alliance</a> partners (if applicable) to disable bots</li>
</ul>
<h2 id="considerations">Considerations</h2>
<p>Bot Fight Mode and Super Bot Fight Mode use the same underlying technology that powers our <a href="https://www.cloudflare.com/products/bot-management/">Bot Management</a> product. Specifically, these products:</p>
<ul>
<li>Protect entire domains without endpoint restrictions</li>
<li>Cannot be customized, adjusted, or reconfigured via WAF custom rules</li>
</ul>
<p>Although these products are designed to fight malicious actors on the Internet, they may challenge API or mobile app traffic. For more granular control, upgrade to <a href="/bots/plans/bm-subscription/">Bot Management for Enterprise</a>.</p>
<h2 id="interaction-with-other-app-security-features">Interaction with other app security features</h2>
<p>If you are using several app security features like custom rules, Managed Rules, and Bot Fight Mode, it is important to understand how these features interact and the order in which they execute. Refer to <a href="/waf/feature-interoperability/">Security features interoperability</a> for more information.</p>
<hr />
<h2 id="enable-bot-fight-mode">Enable Bot Fight Mode</h2>
<p>To start using Bot Fight Mode:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3506.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3505.md")
</aside>
<hr />
<h2 id="disable-bot-fight-mode">Disable Bot Fight Mode</h2>
<p>If you find that <strong>Bot Fight Mode</strong> is causing problems with your application traffic, you may want to disable it.</p>
<p>To disable Bot Fight Mode:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3507.md")
</div>
<hr />
<h2 id="block-ai-bots">Block AI bots</h2>
<p>Refer to <a href="/bots/additional-configurations/block-ai-bots/">Block AI bots</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3504.md")
</aside>
<hr />
<h2 id="visibility">Visibility</h2>
<p>You can see bot-related actions by going to <strong>Security</strong> &gt; <strong>Analytics</strong> and selecting the <strong>Events</strong> tab. Any requests challenged by this product will be labeled <strong>Bot Fight Mode</strong> in the <strong>Service</strong> field. This allows you to observe, analyze, and follow trends in your bot traffic over time.</p>
<hr />
<h2 id="limitations">Limitations</h2>
<h3 id="rules">Rules</h3>
<p>You cannot bypass or skip Bot Fight Mode using WAF custom rules or Page Rules. This is because Bot Fight Mode does not run on the <a href="/ruleset-engine/">Ruleset Engine</a> — it operates in a separate evaluation pipeline where <em>Skip</em>, <em>Bypass</em>, and <em>Allow</em> actions have no effect.</p>
<p>If you need to create exceptions for specific traffic (for example, your own API clients or monitoring tools), use <a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a> instead. Super Bot Fight Mode runs on the Ruleset Engine and supports Skip rules.</p>
<p>Bot Fight Mode can still trigger if you have <a href="/waf/tools/ip-access-rules/">IP Access rules</a>, but it will not trigger if an IP Access rule matches the request first.</p>
<h3 id="javascript-detections">JavaScript Detections</h3>
<p>For Bot Fight Mode customers, <a href="/cloudflare-challenges/challenge-types/javascript-detections/">JavaScript Detections</a> is automatically enabled and cannot be disabled.</p>
<p>If you have a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3508.md")
</div>, you need to take additional steps to implement JavaScript Detections:
<ul>
<li>Ensure that anything under <code>/cdn-cgi/challenge-platform/</code> is allowed. Your CSP should allow scripts served from your origin domain (<code>script-src self</code>).</li>
<li>For <code>nonce</code> script tags:
<ul>
<li>
<p>If your CSP uses a <code>nonce</code> for script tags, Cloudflare will add these nonces to the scripts it injects by parsing your CSP response header.</p>
</li>
<li>
<p>If your CSP does not use <code>nonce</code> for script tags and <strong>JavaScript Detections</strong> is enabled, you may see a console error such as <code>Refused to execute inline script because it violates the following Content Security Policy directive: &quot;script-src 'self'&quot;. Either the 'unsafe-inline' keyword, a hash ('sha256-b123b8a70+4jEj+d6gWI9U6IilUJIrlnRJbRR/uQl2Jc='), or a nonce ('nonce-...') is required to enable inline execution.</code> We highly discourage the use of <code>unsafe-inline</code> and instead recommend the use CSP <code>nonces</code> in script tags which we parse and support in our CDN.</p>
</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/3503.md")
</aside>
