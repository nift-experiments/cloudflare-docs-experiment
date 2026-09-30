<p>By default, the GraphQL Analytics API applies rate limits per user or per API
token. As you grow — adding more zones and accounts — all of your analytics
traffic competes for that single per-credential quota.</p>
<p><strong>Account-based rate limiting</strong> applies limits per account and per zone instead.
Each account and zone gets its own independent budget, so a single user or token
can query many resources at once without exhausting one shared quota. This is the
recommended model if you query analytics across multiple zones or accounts.</p>
<h2 id="benefits">Benefits</h2>
<ul>
<li><strong>Scales with your footprint.</strong> Throughput grows with the number of accounts
and zones you query, instead of being capped by a single per-credential limit.</li>
<li><strong>Higher quotas for Enterprise.</strong> Enterprise customers receive higher default
per-account (15 rps) and per-zone (10 rps) quotas.</li>
<li><strong>Easy limit increases.</strong> Need more headroom? Get in touch, we can accommodate needed increases to your limits.</li>
</ul>
<h2 id="enable-account-based-rate-limiting">Enable account-based rate limiting</h2>
<p>Send the following HTTP header with your requests to the existing GraphQL API
endpoint (<code>https://api.cloudflare.com/client/v4/graphql</code>):</p>
<pre><code class="language-txt">X-Rate-Limit-Type: account-based&#10;</code></pre>
<p>Your endpoint URL and credentials stay the same. Requests without this header
continue to use the default per-user / per-token limits, so you can adopt this
gradually.</p>
<h2 id="limits">Limits</h2>
<table>
<thead>
<tr>
<th>Scope</th>
<th>Default limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Each account</td>
<td>1 request per second (300 requests per 5-minute window)</td>
</tr>
<tr>
<td>Each zone</td>
<td>1 request per second (300 requests per 5-minute window)</td>
</tr>
</tbody>
</table>
<p>A single <code>accounts</code> block counts one request against the referenced account. A
single <code>zones</code> block counts one request against the referenced zone; if the
<code>zones</code> block is nested inside an <code>accounts</code> block, it counts against that
account instead.</p>
<p>Because limits apply per resource, the total throughput available to one user or
token scales with the number of distinct accounts and zones you query.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3129.md")
</aside>
<h2 id="query-requirements">Query requirements</h2>
<p>Most queries work unchanged. Only queries that select a <strong>list</strong> or <strong>range</strong> of
zones at the top (<code>viewer</code>) level need adjusting: nest those zones inside a
single <code>accounts</code> block. The adjusted queries are valid under <strong>both</strong> rate
limiting models.</p>
<p>Querying a single zone — no change:</p>
<pre><code class="language-graphql">{&#10;  viewer {&#10;    zones(filter: { zoneTag: &quot;&lt;ZONE_TAG&gt;&quot; }) {&#10;      &#35; ...&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Querying a single account — no change:</p>
<pre><code class="language-graphql">{&#10;  viewer {&#10;    accounts(filter: { accountTag: &quot;&lt;ACCOUNT_TAG&gt;&quot; }) {&#10;      &#35; ...&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Querying a list or range of zones — nest inside the owning account:</p>
<pre><code class="language-graphql">&#35; Not supported: a list of zones at the viewer level&#10;{&#10;  viewer {&#10;    zones(filter: { zoneTag_in: [&quot;&lt;ZONE_A&gt;&quot;, &quot;&lt;ZONE_B&gt;&quot;] }) {&#10;      &#35; ...&#10;    }&#10;  }&#10;}&#10;&#10;&#35; Supported: the same zones nested inside their account&#10;{&#10;  viewer {&#10;    accounts(filter: { accountTag: &quot;&lt;ACCOUNT_TAG&gt;&quot; }) {&#10;      zones(filter: { zoneTag_in: [&quot;&lt;ZONE_A&gt;&quot;, &quot;&lt;ZONE_B&gt;&quot;] }) {&#10;        &#35; ...&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>The same applies to range filters such as <code>zoneTag_gt</code>. The query semantics are
identical — you only need the account tag that owns the zones, which you already
have.</p>
<h2 id="request-higher-limits">Request higher limits</h2>
<p>If you need more than the default per-account or per-zone throughput, contact
your Cloudflare account team to request an increase for the specific accounts and
zones you query. Increases under this model are applied per resource and take
effect quickly, without an engineering release.</p>
<h2 id="rate-limit-errors">Rate limit errors</h2>
<p>When a limit is exceeded, the API returns an error with <code>extensions.code</code> set to
<code>budget</code>, naming the account or zone that was throttled:</p>
<pre><code class="language-json">{&#10;  &quot;data&quot;: null,&#10;  &quot;errors&quot;: [&#10;    {&#10;      &quot;extensions&quot;: { &quot;code&quot;: &quot;budget&quot;, &quot;timestamp&quot;: &quot;2026-01-01T01:01:01Z&quot; },&#10;      &quot;message&quot;: &quot;Account &lt;ACCOUNT_TAG&gt; has exceeded its rate limit. Please try again after 5 minutes. Refer to this page for more details about rate limits: https://developers.cloudflare.com/analytics/graphql-api/limits/&quot;,&#10;      &quot;path&quot;: null&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>The equivalent zone error reports <code>Zone &lt;ZONE_TAG&gt; has exceeded its rate limit</code>.
Retry after the 5-minute window, spread traffic across resources, or
<a href="#request-higher-limits">request a higher limit</a>.</p>
