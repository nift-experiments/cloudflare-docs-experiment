<p class="article-summary">Set a Cron Trigger for your Worker.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16482.md")
</div></div>
<h2 id="set-cron-triggers-in-wrangler">Set Cron Triggers in Wrangler</h2>
<p>Refer to <a href="/workers/configuration/cron-triggers/">Cron Triggers</a> for more information on how to add a Cron Trigger.</p>
<p>If you are deploying with Wrangler, set the cron syntax (once per hour as shown below) by adding this to your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16483.md")
</div>
<p>You also can set a different Cron Trigger for each <a href="/workers/wrangler/environments/">environment</a> in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>. You need to put the <code>[triggers]</code> table under your chosen environment. For example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16484.md")
</div>
<h2 id="test-cron-triggers-using-wrangler">Test Cron Triggers using Wrangler</h2>
<p>The recommended way of testing Cron Triggers is using Wrangler.</p>
<p>Cron Triggers can be tested using Wrangler by passing in the <code>--test-scheduled</code> flag to <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a>. This will expose a <code>/cdn-cgi/local/scheduled</code> route which can be used to test using a HTTP request. To simulate different cron patterns, a <code>cron</code> query parameter can be passed in.</p>
<pre><code class="language-sh">npx wrangler dev --test-scheduled&#10;&#10;curl &quot;http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*&quot; # Python Workers&#10;</code></pre>
