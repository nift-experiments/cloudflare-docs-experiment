<p>Workflows expose metrics that allow you to inspect and measure Workflow execution, error rates, steps, and total duration across each (and all) of your Workflows.</p>
<p>The metrics displayed in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> charts are queried from Cloudflare’s <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. You can access the metrics <a href="#query-via-the-graphql-api">programmatically</a> via GraphQL or HTTP client.</p>
<h2 id="metrics">Metrics</h2>
<p>Workflows currently export the below metrics within the <code>workflowsAdaptiveGroups</code> GraphQL dataset.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>GraphQL Field Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Read Queries (qps)</td>
<td><code>readQueries</code></td>
<td>The number of read queries issued against a database. This is the raw number of read queries, and is not used for billing.</td>
</tr>
</tbody>
</table>
<p>Metrics can be queried (and are retained) for the past 31 days.</p>
<h3 id="labels-and-dimensions">Labels and dimensions</h3>
<p>The <code>workflowsAdaptiveGroups</code> dataset provides the following dimensions for filtering and grouping query results:</p>
<ul>
<li><code>workflowName</code> - Workflow name - e.g. <code>my-workflow</code></li>
<li><code>instanceId</code> - Instance ID</li>
<li><code>stepName</code> - Step name</li>
<li><code>eventType</code> - Event type (see <a href="#event-types">event types</a>)</li>
<li><code>stepCount</code> - Step number within a given instance</li>
<li><code>date</code> - The date when the Workflow was triggered</li>
<li><code>datetimeFifteenMinutes</code> - The date and time truncated to fifteen minutes</li>
<li><code>datetimeFiveMinutes</code> - The date and time truncated to five minutes</li>
<li><code>datetimeHour</code> - The date and time truncated to the hour</li>
<li><code>datetimeMinute</code> - The date and time truncated to the minute</li>
</ul>
<h3 id="event-types">Event types</h3>
<p>The <code>eventType</code> metric allows you to filter (or groupBy) Workflows and steps based on their last observed status.</p>
<p>The possible values for <code>eventType</code> are documented below:</p>
<h4 id="workflows-level-status-labels">Workflows-level status labels</h4>
<ul>
<li><code>WORKFLOW_QUEUED</code> - the Workflow is queued, but not currently running. This can happen when you are at the <a href="/workflows/reference/limits/">concurrency limit</a> and new instances are waiting for currently running instances to complete.</li>
<li><code>WORKFLOW_START</code> - the Workflow has started and is running.</li>
<li><code>WORKFLOW_SUCCESS</code> - the Workflow finished without errors.</li>
<li><code>WORKFLOW_FAILURE</code> - the Workflow failed due to errors (exhausting retries, errors thrown, etc).</li>
<li><code>WORKFLOW_TERMINATED</code> - the Workflow was explicitly terminated.</li>
<li><code>ROLLBACK_START</code> - the Workflow began executing registered rollback handlers.</li>
<li><code>ROLLBACK_COMPLETE</code> - all rollback handlers that were run completed successfully.</li>
<li><code>ROLLBACK_FAILED</code> - a rollback handler failed and rollback did not finish cleanly.</li>
</ul>
<h4 id="step-level-status-labels">Step-level status labels</h4>
<ul>
<li><code>STEP_START</code> - the step has started and is running.</li>
<li><code>STEP_SUCCESS</code> - the step finished without errors.</li>
<li><code>STEP_FAILURE</code> - the step failed due to an error.</li>
<li><code>SLEEP_START</code> - the step is sleeping.</li>
<li><code>SLEEP_COMPLETE</code> - the step last finished sleeping.</li>
<li><code>ATTEMPT_START</code> - a step is retrying.</li>
<li><code>ATTEMPT_SUCCESS</code> - the retry succeeded.</li>
<li><code>ATTEMPT_FAILURE</code> - the retry attempt failed.</li>
<li><code>ROLLBACK_STEP_START</code> - a rollback handler started running.</li>
<li><code>ROLLBACK_STEP_SUCCESS</code> - a rollback handler finished successfully.</li>
<li><code>ROLLBACK_STEP_FAILURE</code> - a rollback handler failed.</li>
<li><code>ROLLBACK_ATTEMPT_START</code> - a rollback retry attempt started.</li>
<li><code>ROLLBACK_ATTEMPT_SUCCESS</code> - a rollback retry attempt succeeded.</li>
<li><code>ROLLBACK_ATTEMPT_FAILURE</code> - a rollback retry attempt failed.</li>
</ul>
<p>Rollback events let you distinguish forward execution failures from compensation failures when you are querying Workflow health or debugging instance timelines.</p>
<h2 id="view-metrics-in-the-dashboard">View metrics in the dashboard</h2>
<p>Per-Workflow and instance analytics for Workflows are available in the Cloudflare dashboard. To view current and historical metrics for a database:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workflows</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select a Workflow to view its metrics.</li>
</ol>
<p>You can optionally select a time window to query. This defaults to the last 24 hours.</p>
<h2 id="query-via-the-graphql-api">Query via the GraphQL API</h2>
<p>You can programmatically query analytics for your Workflows via the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. This API queries the same datasets as the Cloudflare dashboard, and supports GraphQL <a href="/analytics/graphql-api/features/discovery/introspection/">introspection</a>.</p>
<p>Workflows GraphQL datasets require an <code>accountTag</code> filter with your Cloudflare account ID, and includes the <code>workflowsAdaptiveGroups</code> dataset.</p>
<h3 id="examples">Examples</h3>
<p>To query the count (number of workflow invocations) and sum of <code>wallTime</code> for a given <code>$workflowName</code> between <code>$datetimeStart</code> and <code>$datetimeEnd</code>, grouping by <code>date</code>:</p>
<pre><code class="language-graphql">query WorkflowInvocationsExample(&#10;	$accountTag: string!&#10;	$datetimeStart: Time&#10;	$datetimeEnd: Time&#10;	$workflowName: string&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			wallTime: workflowsAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					datetimeHour_geq: $datetimeStart&#10;					datetimeHour_leq: $datetimeEnd&#10;					workflowName: $workflowName&#10;				}&#10;				orderBy: [count_DESC]&#10;			) {&#10;				count&#10;				sum {&#10;					wallTime&#10;				}&#10;				dimensions {&#10;					date: datetimeHour&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Here we are doing the same for <code>wallTime</code>, <code>instanceRuns</code> and <code>stepCount</code> in the same query:</p>
<pre><code class="language-graphql">query WorkflowInvocationsExample2(&#10;	$accountTag: string!&#10;	$datetimeStart: Time&#10;	$datetimeEnd: Time&#10;	$workflowName: string&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			instanceRuns: workflowsAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					datetimeHour_geq: $datetimeStart&#10;					datetimeHour_leq: $datetimeEnd&#10;					workflowName: $workflowName&#10;					eventType: &quot;WORKFLOW_START&quot;&#10;				}&#10;				orderBy: [count_DESC]&#10;			) {&#10;				count&#10;				dimensions {&#10;					date: datetimeHour&#10;				}&#10;			}&#10;			stepCount: workflowsAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					datetimeHour_geq: $datetimeStart&#10;					datetimeHour_leq: $datetimeEnd&#10;					workflowName: $workflowName&#10;					eventType: &quot;WORKFLOW_START&quot;&#10;				}&#10;				orderBy: [count_DESC]&#10;			) {&#10;				count&#10;				dimensions {&#10;					date: datetimeHour&#10;				}&#10;			}&#10;			wallTime: workflowsAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					datetimeHour_geq: $datetimeStart&#10;					datetimeHour_leq: $datetimeEnd&#10;					workflowName: $workflowName&#10;				}&#10;				orderBy: [count_DESC]&#10;			) {&#10;				count&#10;				sum {&#10;					wallTime&#10;				}&#10;				dimensions {&#10;					date: datetimeHour&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Here lets query <code>workflowsAdaptive</code> for raw data about <code>$instanceId</code> between <code>$datetimeStart</code> and <code>$datetimeEnd</code>:</p>
<pre><code class="language-graphql">query WorkflowsAdaptiveExample(&#10;	$accountTag: string!&#10;	$datetimeStart: Time&#10;	$datetimeEnd: Time&#10;	$instanceId: string&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			workflowsAdaptive(&#10;				limit: 100&#10;				filter: {&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;					instanceId: $instanceId&#10;				}&#10;				orderBy: [datetime_ASC]&#10;			) {&#10;				datetime&#10;				eventType&#10;				workflowName&#10;				instanceId&#10;				stepCount&#10;				wallTime&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h4 id="graphql-query-variables">GraphQL query variables</h4>
<p>Example values for the query variables:</p>
<pre><code class="language-json">{&#10;	&quot;accountTag&quot;: &quot;fedfa729a5b0ecfd623bca1f9000f0a22&quot;,&#10;	&quot;datetimeStart&quot;: &quot;2024-10-20T00:00:00Z&quot;,&#10;	&quot;datetimeEnd&quot;: &quot;2024-10-29T00:00:00Z&quot;,&#10;	&quot;workflowName&quot;: &quot;shoppingCart&quot;,&#10;	&quot;instanceId&quot;: &quot;ecc48200-11c4-22a3-b05f-88a3c1c1db81&quot;&#10;}&#10;</code></pre>
