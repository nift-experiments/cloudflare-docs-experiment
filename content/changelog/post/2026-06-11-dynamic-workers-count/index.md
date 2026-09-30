<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 11, 2026</time><h2 id="post-title">Track Dynamic Workers usage from the dashboard and GraphQL API</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/workers/changelog/dynamic-workers-count.png" alt="Dynamic Workers usage on the Workers overview page" /></p>
<p>Customers can now view the number of <a href="/dynamic-workers/">Dynamic Workers</a> invoked during their billing period from the Workers overview page in the Cloudflare dashboard.</p>
<p>This count reflects the number of Dynamic Workers that Cloudflare would bill for during the selected billing period. Dynamic Workers usage data only goes back to June 1, 2026.</p>
<p>You can also query this count through the <a href="/analytics/graphql-api/">GraphQL Analytics API</a> by using <code>workersInvocationsByOwnerAndScriptGroups</code> and selecting <code>distinctDynamicWorkerCount</code>:</p>
<pre><code class="language-graphql">query getDynamicWorkersCount(&#10;	$accountTag: string!&#10;	$filter: AccountWorkersInvocationsByOwnerAndScriptGroupsFilter_InputObject&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			workersInvocationsByOwnerAndScriptGroups(limit: 10000, filter: $filter) {&#10;				uniq {&#10;					distinctDynamicWorkerCount&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Use variables to set the account and billing-period date range:</p>
<pre><code class="language-json">{&#10;	&quot;accountTag&quot;: &quot;&lt;ACCOUNT_ID&gt;&quot;,&#10;	&quot;filter&quot;: {&#10;		&quot;date_geq&quot;: &quot;2026-06-01&quot;,&#10;		&quot;date_leq&quot;: &quot;2026-06-30&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For more information, refer to <a href="/dynamic-workers/pricing/">Dynamic Workers pricing</a>.</p>
</div></article></div>
