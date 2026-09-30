<div class="nb-glossary-definition"><p>A monitor issues health monitor requests at regular intervals to evaluate the health of each endpoint within a <a href="/load-balancing/pools/">pool</a>.</p>
<p>When a pool <a href="/load-balancing/understand-basics/health-details/">becomes unhealthy</a>, your load balancer takes that pool out of the endpoint rotation.</p></div>
<p>For more details about monitors, refer to <a href="/load-balancing/monitors/">Monitors</a>.</p>
<hr />
<h2 id="retry-timing">Retry timing</h2>
<p>When a health check times out, Cloudflare sends retries immediately — they do not wait for the next interval. The <code>retries</code> setting defines the number of additional attempts after the initial check. For example, with five retries:</p>
<ul>
<li>Total attempts: 1 (initial) + 5 (retries) = <strong>6</strong></li>
<li>With a 20 s timeout: Cloudflare marks the endpoint unhealthy after approximately 120 s (6 × 20 s)</li>
<li>The configured interval (for example, 60 s) only applies between <strong>successful</strong> probe cycles, not between retries</li>
</ul>
<hr />
<h2 id="create-a-monitor">Create a monitor</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10381.md")
</div></div>
<hr />
<h2 id="edit-a-monitor">Edit a monitor</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10384.md")
</div></div>
<hr />
<h2 id="delete-a-monitor">Delete a monitor</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10387.md")
</div></div>
