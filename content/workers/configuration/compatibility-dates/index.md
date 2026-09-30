<p>Cloudflare regularly updates the Workers runtime. These updates apply to all Workers globally and should never cause a Worker that is already deployed to stop functioning. Sometimes, though, some changes may be backwards-incompatible. In particular, there might be bugs in the runtime API that existing Workers may inadvertently depend upon. Cloudflare implements bug fixes that new Workers can opt into while existing Workers will continue to see the buggy behavior to prevent breaking deployed Workers.</p>
<p>The compatibility date and flags are how you, as a developer, opt into these runtime changes. <a href="/workers/configuration/compatibility-flags">Compatibility flags</a> will often have a date in which they are enabled by default, and so, by specifying a <code>compatibility_date</code> for your Worker, you can quickly enable all of these various compatibility flags up to, and including, that date.</p>
<h2 id="setting-compatibility-date">Setting compatibility date</h2>
<p>When you start your project, you should always set <code>compatibility_date</code> to the current date. You should occasionally update the <code>compatibility_date</code> field. When updating, you should refer to the <a href="/workers/configuration/compatibility-flags">compatibility flags</a> page to find out what has changed, and you should be careful to test your Worker to see if the changes affect you, updating your code as necessary. The new compatibility date takes effect when you next run the <a href="/workers/wrangler/commands/general/#deploy"><code>npx wrangler deploy</code></a> command.</p>
<p>There is no need to update your <code>compatibility_date</code> if you do not want to. The Workers runtime will support old compatibility dates forever. If, for some reason, Cloudflare finds it is necessary to make a change that will break live Workers, Cloudflare will actively contact affected developers. That said, Cloudflare aims to avoid this if at all possible.</p>
<p>However, even though you do not need to update the <code>compatibility_date</code> field, it is a good practice to do so for two reasons:</p>
<ol>
<li>Sometimes, new features can only be made available to Workers that have a current <code>compatibility_date</code>. To access the latest features, you need to stay up-to-date.</li>
<li>Generally, other than the <a href="/workers/configuration/compatibility-flags">compatibility flags</a> page, the Workers documentation may only describe the current <code>compatibility_date</code>, omitting information about historical behavior. If your Worker uses an old <code>compatibility_date</code>, you will need to continuously refer to the compatibility flags page in order to check if any of the APIs you are using have changed.</li>
</ol>
<h4 id="via-wrangler">Via Wrangler</h4>
<p>The compatibility date can be set in a Worker's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16654.md")
</div>
<h4 id="via-the-cloudflare-dashboard">Via the Cloudflare Dashboard</h4>
<p>When a Worker is created through the Cloudflare Dashboard, the compatibility date is automatically set to the current date.</p>
<p>The compatibility date can be updated in the Workers settings on the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</p>
<h4 id="via-the-cloudflare-api">Via the Cloudflare API</h4>
<p>The compatibility date can be set when uploading a Worker using the <a href="/api/resources/workers/subresources/scripts/methods/update/">Workers Script API</a> or <a href="/api/resources/workers/subresources/scripts/subresources/versions/methods/create/">Workers Versions API</a> in the request body's <code>metadata</code> field.</p>
<p>If a compatibility date is not specified on upload via the API, it defaults to the oldest compatibility date, before any flags took effect (2021-11-02). When creating new Workers, it is highly recommended to set the compatibility date to the current date when uploading via the API.</p>
