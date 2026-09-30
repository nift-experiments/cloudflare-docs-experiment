<p class="article-summary">Set multiple Cron Triggers on three different schedules.</p>
<p>If you want to get started quickly, click on the button below.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/multiple-cron-triggers"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16410.md")
</div></div>
<h2 id="test-cron-triggers-using-wrangler">Test Cron Triggers using Wrangler</h2>
<p>The recommended way of testing Cron Triggers is using Wrangler.</p>
<p>Cron Triggers can be tested using Wrangler by passing in the <code>--test-scheduled</code> flag to <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a>. This will expose a <code>/cdn-cgi/local/scheduled</code> route which can be used to test using a HTTP request. To simulate different cron patterns, a <code>cron</code> query parameter can be passed in.</p>
<pre><code class="language-sh">npx wrangler dev --test-scheduled&#10;&#10;curl &quot;http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*&quot; # Python Workers&#10;</code></pre>
