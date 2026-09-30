<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 20, 2026</time><h2 id="post-title">Budget alerts now on by default for Pay-as-you-go accounts</h2>
<div class="changelog-badges"><span>billing</span><span>workers</span></div><div class="changelog-body"><p>We are turning on budget alerts by default for eligible Pay-as-you-go accounts. If your account does not already have a budget alert, Cloudflare will create one for you with a $10 account-level threshold. Your default alert will enable at the turn of your next billing cycle, so it will not fire based on usage you have already incurred.</p>
<p>We are rolling this out in cohorts over the coming weeks, so eligible accounts may see their default alert appear at different times.</p>
<p>The default alert behaves exactly like an alert you would create yourself. When your cumulative usage-based spend this cycle reaches the threshold, you receive an email notification. The alert is informational only. It does not cap your usage or impact your account in any way.</p>
<p>Usage is processed once per day for the prior day's activity, so budget alerts fire the day after the threshold is reached rather than in real time.</p>
<p>Budget alerts only consider spend on usage-based products. Recurring subscription fees, such as the Workers Paid plan fee or other monthly plan charges, are not included in the threshold calculation.</p>
<p>You can change the threshold, add additional alerts, or remove the default alert entirely from <strong>Manage Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Billable Usage</strong>, or from your Notifications settings. If you already configured your own budget alert, nothing changes.</p>
<p>Enterprise contract accounts are not in scope.</p>
<p>For more information, refer to the <a href="/billing/manage/budget-alerts/">Budget alerts documentation</a>.</p>
</div></article></div>
