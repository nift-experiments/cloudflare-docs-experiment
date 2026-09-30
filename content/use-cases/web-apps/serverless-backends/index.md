<p>Running backend code on traditional servers requires provisioning capacity, managing scaling, and accepting cold starts. Cloudflare Workers runs your server-side code at the edge with fast startup, automatic scaling, and global distribution across 300+ locations.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="workers">Workers</h3>
<p>Build and deploy serverless applications on Cloudflare's global network. <a href="/workers/">Learn more about Workers</a>.</p>
<ul>
<li><strong>Global deployment</strong> - Code runs at the Cloudflare location nearest to each user automatically</li>
<li><strong>Fast startup</strong> - V8 isolates start in milliseconds with no warm-up period, avoiding the cold start delays of container-based platforms</li>
<li><strong>Auto-scaling</strong> - Handle traffic spikes without provisioning or configuration</li>
</ul>
<h3 id="cron-triggers">Cron Triggers</h3>
<p>Schedule Workers to run on a recurring basis. <a href="/workers/configuration/cron-triggers/">Learn more about Cron Triggers</a>.</p>
<ul>
<li><strong>Scheduled tasks</strong> - Run Workers on a fixed schedule for background jobs and periodic tasks</li>
</ul>
<h3 id="queues">Queues</h3>
<p>Reliable message queuing and background processing for Workers. <a href="/queues/">Learn more about Queues</a>.</p>
<ul>
<li><strong>Async processing</strong> - Reliably process background jobs and webhooks without blocking request handling</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/workers/get-started/">Workers get started</a></li>
<li><a href="/workers/configuration/cron-triggers/">Configure Cron Triggers</a></li>
<li><a href="/queues/get-started/">Queues get started</a></li>
</ol>
