<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 19, 2025</time><h2 id="post-title">Account-level DNS analytics now available via GraphQL Analytics API</h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><p>Authoritative DNS analytics are now available on the <strong>account level</strong> via the <a href="/analytics/graphql-api/">Cloudflare GraphQL Analytics API</a>.</p>
<p>This allows users to query DNS analytics across multiple zones in their account, by using the <code>accounts</code> filter.</p>
<p>Here is an example to retrieve the most recent DNS queries across all zones in your account that resulted in an <code>NXDOMAIN</code> response over a given time frame. Please replace <code>a30f822fcd7c401984bf85d8f2a5111c</code> with your actual account ID.</p>
<pre><code class="language-graphql">query GetLatestNXDOMAINResponses {&#10;	viewer {&#10;		accounts(filter: { accountTag: &quot;a30f822fcd7c401984bf85d8f2a5111c&quot; }) {&#10;			dnsAnalyticsAdaptive(&#10;				filter: {&#10;					date_geq: &quot;2025-06-16&quot;&#10;					date_leq: &quot;2025-06-18&quot;&#10;					responseCode: &quot;NXDOMAIN&quot;&#10;				}&#10;				limit: 10000&#10;				orderBy: [datetime_DESC]&#10;			) {&#10;				zoneTag&#10;				queryName&#10;				responseCode&#10;				queryType&#10;				datetime&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>To learn more and get started, refer to the <a href="/dns/additional-options/analytics/#analytics">DNS Analytics documentation</a>.</p>
</div></article></div>
