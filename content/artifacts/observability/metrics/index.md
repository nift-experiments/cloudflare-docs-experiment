<p>Artifacts exposes analytics that let you inspect repo activity, errors, and operation duration across your account.</p>
<p>Artifacts metrics are available through Cloudflare's <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. You can use them to answer questions like which repos are busiest, where errors cluster, and how long operations take.</p>
<h2 id="metrics">Metrics</h2>
<p>Artifacts currently exports the <code>artifactsEventsAdaptiveGroups</code> GraphQL dataset.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>GraphQL field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Operations</td>
<td><code>count</code></td>
<td>Total number of Artifacts events that match the query filter. This includes successful actions and errors.</td>
</tr>
<tr>
<td>Total duration</td>
<td><code>sum.durationMs</code></td>
<td>Total time spent handling matching Artifacts operations, in milliseconds.</td>
</tr>
<tr>
<td>Average duration</td>
<td><code>avg.durationMs</code></td>
<td>Average time per matching operation, in milliseconds.</td>
</tr>
<tr>
<td>Duration p25</td>
<td><code>quantiles.durationMsP25</code></td>
<td>25th percentile operation duration, in milliseconds.</td>
</tr>
<tr>
<td>Duration p50</td>
<td><code>quantiles.durationMsP50</code></td>
<td>Median operation duration, in milliseconds.</td>
</tr>
<tr>
<td>Duration p75</td>
<td><code>quantiles.durationMsP75</code></td>
<td>75th percentile operation duration, in milliseconds.</td>
</tr>
<tr>
<td>Duration p90</td>
<td><code>quantiles.durationMsP90</code></td>
<td>90th percentile operation duration, in milliseconds.</td>
</tr>
<tr>
<td>Duration p95</td>
<td><code>quantiles.durationMsP95</code></td>
<td>95th percentile operation duration, in milliseconds.</td>
</tr>
<tr>
<td>Duration p99</td>
<td><code>quantiles.durationMsP99</code></td>
<td>99th percentile operation duration, in milliseconds.</td>
</tr>
<tr>
<td>Duration p999</td>
<td><code>quantiles.durationMsP999</code></td>
<td>99.9th percentile operation duration, in milliseconds.</td>
</tr>
</tbody>
</table>
<p>Metrics can be queried for the past 31 days. Queries require an <code>accountTag</code> filter with your Cloudflare account ID.</p>
<h2 id="dimensions">Dimensions</h2>
<p>Use these dimensions to filter or group results:</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>repository</code></td>
<td>Fully qualified repo path in the form <code>namespace/name</code>.</td>
</tr>
<tr>
<td><code>repositoryNamespace</code></td>
<td>Namespace that contains the repo.</td>
</tr>
<tr>
<td><code>repositoryName</code></td>
<td>Repo name inside the namespace.</td>
</tr>
<tr>
<td><code>eventKind</code></td>
<td>Top-level event category. Use <code>action</code> for successful operations and <code>error</code> for failures.</td>
</tr>
<tr>
<td><code>eventType</code></td>
<td>Specific operation or error type.</td>
</tr>
<tr>
<td><code>errorMessage</code></td>
<td>Error message for failed operations.</td>
</tr>
<tr>
<td><code>date</code></td>
<td>Calendar date of the event.</td>
</tr>
<tr>
<td><code>datetime</code></td>
<td>Exact event timestamp.</td>
</tr>
<tr>
<td><code>datetimeMinute</code></td>
<td>Event time truncated to the minute.</td>
</tr>
<tr>
<td><code>datetimeFiveMinutes</code></td>
<td>Event time truncated to five-minute windows.</td>
</tr>
<tr>
<td><code>datetimeFifteenMinutes</code></td>
<td>Event time truncated to fifteen-minute windows.</td>
</tr>
<tr>
<td><code>datetimeHour</code></td>
<td>Event time truncated to the hour.</td>
</tr>
<tr>
<td><code>datetimeSixHours</code></td>
<td>Event time truncated to six-hour windows.</td>
</tr>
</tbody>
</table>
<h2 id="event-types">Event types</h2>
<p>Artifacts currently emits these values in <code>eventType</code>:</p>
<table>
<thead>
<tr>
<th>Event type</th>
<th>Kind</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>create</code></td>
<td><code>action</code></td>
<td>A repo was created.</td>
</tr>
<tr>
<td><code>fork</code></td>
<td><code>action</code></td>
<td>A repo was forked.</td>
</tr>
<tr>
<td><code>push</code></td>
<td><code>action</code></td>
<td>A client pushed data to a repo.</td>
</tr>
<tr>
<td><code>pull</code></td>
<td><code>action</code></td>
<td>A client fetched or cloned data from a repo.</td>
</tr>
<tr>
<td><code>delete</code></td>
<td><code>action</code></td>
<td>A repo was deleted.</td>
</tr>
<tr>
<td><code>storageLimitReached</code></td>
<td><code>error</code></td>
<td>An operation hit a storage limit condition.</td>
</tr>
<tr>
<td><code>serverError</code></td>
<td><code>error</code></td>
<td>The service failed while handling the request.</td>
</tr>
<tr>
<td><code>clientError</code></td>
<td><code>error</code></td>
<td>The client sent an invalid or unsupported request.</td>
</tr>
<tr>
<td><code>rateLimited</code></td>
<td><code>error</code></td>
<td>The request was rejected by a rate limiter.</td>
</tr>
</tbody>
</table>
<h2 id="example-graphql-queries">Example GraphQL queries</h2>
<p>You can query Artifacts analytics with the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. All examples on this page use the <code>artifactsEventsAdaptiveGroups</code> dataset.</p>
<h3 id="operations-by-repo-within-a-namespace">Operations by repo within a namespace</h3>
<p>Use this query to find the busiest repos in one namespace over a time range. It also returns average operation duration so you can compare activity and latency together.</p>
<pre><code class="language-graphql">query ArtifactsOperationsByRepo(&#10;	$accountTag: String!&#10;	$datetimeStart: Time&#10;	$datetimeEnd: Time&#10;	$repositoryNamespace: String!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			artifactsEventsAdaptiveGroups(&#10;				limit: 100&#10;				filter: {&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;					repositoryNamespace: $repositoryNamespace&#10;					eventKind: &quot;action&quot;&#10;				}&#10;				orderBy: [count_DESC]&#10;			) {&#10;				count&#10;				avg {&#10;					durationMs&#10;				}&#10;				dimensions {&#10;					repositoryName&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="errors-by-repo-descending">Errors by repo, descending</h3>
<p>Use this query to rank repos by error volume. It helps you spot which repos fail most often and which error types are driving those failures.</p>
<pre><code class="language-graphql">query ArtifactsErrorsByRepo(&#10;	$accountTag: String!&#10;	$datetimeStart: Time&#10;	$datetimeEnd: Time&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			artifactsEventsAdaptiveGroups(&#10;				limit: 100&#10;				filter: {&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;					eventKind: &quot;error&quot;&#10;				}&#10;				orderBy: [count_DESC]&#10;			) {&#10;				count&#10;				dimensions {&#10;					repository&#10;					eventType&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="repos-by-pushes-descending">Repos by pushes, descending</h3>
<p>Use this query to see which repos receive the most pushes in a time window. It is useful for identifying active write-heavy repos across an account.</p>
<pre><code class="language-graphql">query ArtifactsPushesByRepo(&#10;	$accountTag: String!&#10;	$datetimeStart: Time&#10;	$datetimeEnd: Time&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			artifactsEventsAdaptiveGroups(&#10;				limit: 100&#10;				filter: {&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;					eventKind: &quot;action&quot;&#10;					eventType: &quot;push&quot;&#10;				}&#10;				orderBy: [count_DESC]&#10;			) {&#10;				count&#10;				dimensions {&#10;					repository&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
