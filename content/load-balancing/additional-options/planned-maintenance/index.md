<p>When you change application settings or add new assets, you will likely want to make these changes on one endpoint at a time. Going endpoint by endpoint reduces the risk of changes and ensures a more consistent user experience.</p>
<p>To take endpoints out of rotation gradually (important for session-based load balancing), <a href="#gradual-rotation">enable endpoint drain</a> on your load balancer. This option is only available for <a href="/load-balancing/understand-basics/proxy-modes/">proxied load balancers (orange-clouded)</a>.</p>
<p>To direct traffic away from your endpoint immediately, <a href="#immediate-rotation">adjust settings on the pool or monitor</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10427.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="existing-connections-are-not-terminated">Existing connections are not terminated</h3>
@markup("md", "content/.markup/bodies/10426.md")
</aside>
<h2 id="before-you-begin">Before you begin</h2>
<p>Before disabling any endpoint, review the settings for any affected load balancers and pools.</p>
<p>If a pool falls below its <strong>Health Threshold</strong>, it will be considered <strong>Unhealthy</strong> and — depending on the load balancer setup and steering policy — a load balancer may begin routing traffic away from that pool.</p>
<h2 id="gradual-rotation">Gradual rotation</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10425.md")
</aside>
<p>With <a href="/load-balancing/understand-basics/session-affinity/">session-based load balancing</a>, it is important to direct all requests from a particular end user to a specific endpoint. Otherwise, information about the user session — such as items in their shopping cart — may be lost and lead to negative business outcomes.</p>
<p>To remove an endpoint from rotation while still preserving session continuity, set up <strong>Endpoint drain</strong> on a load balancer:</p>
<ol>
<li>On a new or existing load balancer, go to the <strong>Hostname</strong> step.</li>
<li>Make sure you have enabled <strong>Session Affinity</strong>.</li>
<li>For <strong>Endpoint drain duration</strong>, enter a time in seconds. If this value is less than the <strong>Session TTL</strong> value, you will affect existing sessions.
<img src="/assets/upstream/images/load-balancing/session-affinity-3.png" alt="Example configuration of session affinity with endpoint drain" /></li>
<li>Save your changes to the load balancer.</li>
<li>Click <strong>Manage Pools</strong>.</li>
<li>Disable an endpoint. Your load balancer will gradually drain sessions from that endpoint.</li>
<li>On your load balancer, expand your pools to find the disabled endpoint. You will see the estimated <strong>Drain Time</strong> counting down.
<img src="/assets/upstream/images/load-balancing/session-affinity-4.png" alt="Example showing load balancer draining in progress" /></li>
<li>When a drain is <strong>Complete</strong>, there are no longer any connections to that endpoint.
<img src="/assets/upstream/images/load-balancing/session-affinity-5.png" alt="Example showing load balancer draining complete" /></li>
<li>Perform your required maintenance or upgrades.</li>
<li>To bring your endpoint back online, re-enable the endpoint.</li>
</ol>
<h2 id="immediate-rotation">Immediate rotation</h2>
<p>To direct traffic away from an endpoint immediately:</p>
<ol>
<li>Do one of the following actions:
<ul>
<li>On the endpoint's <a href="/load-balancing/monitors/">monitor</a>, update the monitor settings so the endpoint will fail health monitor requests, such as putting an incorrect value for the <strong>Response Body</strong> or <strong>Response Code</strong>.</li>
<li>On the pool, disable the endpoint.</li>
<li>On the pool, set the <a href="/load-balancing/understand-basics/traffic-steering/origin-level-steering/#weights">endpoint weight</a> to <code>0</code> (though traffic may still reach the endpoint if it is included in multiple pools).</li>
</ul>
</li>
<li>Monitor <a href="/load-balancing/reference/load-balancing-analytics/">Load Balancing Analytics</a> to make sure no requests are reaching the pool.
<ul>
<li>If you are using <a href="/load-balancing/understand-basics/proxy-modes/">DNS-only load balancing (gray-clouded)</a>, changes may be delayed due to DNS resolver caching.</li>
</ul>
</li>
<li>Perform your required maintenance or upgrades.</li>
<li>Undo the changes you made in <strong>Step 1</strong>.</li>
</ol>
