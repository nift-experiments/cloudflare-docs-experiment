<p>Security Analytics shows information about all incoming HTTP requests or only about requests mitigated by Cloudflare.</p>
<p>Use Security Analytics as your starting point to understand and analyze traffic patterns, and to create security rules based on the filters you applied.</p>
<p>To access Security Analytics in the new security dashboard, go to the <strong>Analytics</strong> page.</p>
<div class="nb-dash-button"></div>
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/1a426a3ae597ae3935eb97b5f97f106f/iframe?preload=true&amp;letterboxColor=transparent&amp;poster=https%3A%2F%2Fimagedelivery.net%2FxDOJvHcv1KwTQn6S-BGFIw%2Fb8137b46-e0dd-45ab-b24f-4edab0fa0b00%2Fpublic" title="Application Security: Get started guide" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<p>By default, Security Analytics queries filter on <code>requestSource = 'eyeball'</code>, which represents requests from end users. Note that requests from Cloudflare Workers (subrequests) are not visible in Security Analytics.</p>
<h2 id="traffic">Traffic</h2>
<p>The <strong>Traffic</strong> tab displays information about all incoming HTTP requests for your domain, including requests not handled by Cloudflare security products.</p>
<p>In this tab you can perform several tasks:</p>
<ul>
<li>View the traffic distribution for your domain.</li>
<li>Understand which traffic is being mitigated by Cloudflare security products, and where non-mitigated traffic is being served from (Cloudflare global network or <a href="https://www.cloudflare.com/learning/cdn/glossary/origin-server/">origin server</a>).</li>
<li>Analyze suspicious traffic and create tailored custom <a href="/security/rules/">security rules</a> based on applied filters.</li>
<li><a href="/waf/rate-limiting-rules/find-rate-limit/">Find an appropriate rate limit</a> for incoming traffic.</li>
</ul>
<p>For information on how to use the <strong>Traffic</strong> tab, refer to <a href="/waf/analytics/security-analytics/#adjusting-displayed-data">Security Analytics</a>.</p>
<p>If you need to modify existing security-related rules you already configured, consider also using the <a href="#events">Events</a> tab. This tab displays information about requests affected by Cloudflare security products.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/369.md")
</aside>
<h2 id="events">Events</h2>
<p>Use the <strong>Events</strong> tab to review <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/370.md")
</div> and to tailor your security configurations.
<p>The <strong>Events</strong> tab displays information about requests actioned or flagged by Cloudflare security products. Each incoming HTTP request might generate one or more security events. The tab only shows these events, not the HTTP requests themselves. To obtain information on all incoming HTTP requests, use the <a href="#traffic">Traffic</a> tab.</p>
<p>Users on a Free plan can view summarized events by date in sampled logs. Customers on paid plans have access to additional graphs and dashboards that summarize the most relevant information about the current behavior of Cloudflare's security features on your domain.</p>
<p>For more information on the <strong>Events</strong> tab, refer to <a href="/waf/analytics/security-events/">Security Events</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/368.md")
</aside>
