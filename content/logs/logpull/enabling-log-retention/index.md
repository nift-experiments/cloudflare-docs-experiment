<p>By default, your HTTP request logs are not retained. When using the Logpull API for the first time, you will need to enable retention. You can also turn off retention at any time. Note that after retention is turned off, previously saved logs will be available until the retention period expires (refer to <a href="/logs/logpull/understanding-the-basics/#data-retention-period">Data retention period</a>).</p>
<h2 id="endpoints">Endpoints</h2>
<p>There are two endpoints for managing log retention:</p>
<ul>
<li><code>GET /logs/control/retention/flag</code> - returns the current status of retention</li>
<li><code>POST /logs/control/retention/flag</code> - turns retention on or off</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/10480.md")
</aside>
<h2 id="example-api-requests-using-curl">Example API requests using cURL</h2>
<h3 id="check-log-retention-status">Check log retention status</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10484.md")
</div></div>
<p>If the zone has log retention <a href="/logs/logpull/enabling-log-retention/#enabled-response">enabled</a> you get the value <code>true</code>, whereas a value of <code>false</code> is returned when it is <a href="/logs/logpull/enabling-log-retention/#disabled-response">disabled</a>.</p>
<h3 id="turn-on-log-retention">Turn on log retention</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10488.md")
</div></div>
<h4 id="enabled-response">Enabled response</h4>
<pre><code class="language-json">{&#10;	&quot;flag&quot;: true&#10;}&#10;</code></pre>
<h3 id="turn-off-log-retention">Turn off log retention</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10492.md")
</div></div>
<h4 id="disabled-response">Disabled response</h4>
<pre><code class="language-json">{&#10;	&quot;flag&quot;: false&#10;}&#10;</code></pre>
<h2 id="audit">Audit</h2>
<p>Turning log retention on or off is recorded in <a href="/fundamentals/account/account-security/review-audit-logs/#access-audit-logs">Cloudflare Audit Logs</a>.</p>
