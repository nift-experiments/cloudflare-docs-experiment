<p>The <strong>Zaraz Monitoring API</strong> allows users to retrieve detailed data on Zaraz events through the <strong>GraphQL Analytics API</strong>. Using this API, you can monitor events, pageviews, triggers, actions, and server-side request statuses, including any errors and successes. The data available through the API mirrors what is shown on the Zaraz Monitoring page in the dashboard, but with the API, you can query it programmatically to create alerts and notifications for unexpected deviations.</p>
<p>To get started, you'll need to generate an Analytics API token by following the <a href="/analytics/graphql-api/getting-started/authentication/api-token-auth/">API token authentication guide</a>.</p>
<h2 id="key-entities">Key Entities</h2>
<p>The Monitoring API includes the following core entities, which each provide distinct insights:</p>
<ul>
<li><strong>zarazTrackAdaptiveGroups</strong>: Contains data on Zaraz events, such as event counts and timestamps.</li>
<li><strong>zarazActionsAdaptiveGroups</strong>: Provides information on Zaraz Actions.</li>
<li><strong>zarazTriggersAdaptiveGroups</strong>: Tracks data on Zaraz Triggers.</li>
<li><strong>zarazFetchAdaptiveGroups</strong>: Captures server-side request data, including URLs and returning status codes for third-party requests made by Zaraz.</li>
</ul>
<h2 id="example-graphql-queries">Example GraphQL Queries</h2>
<p>You can construct any query you'd like using the above datasets, but here are some example queries you can use.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="GQLExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17603.md")
</div></div>
<h3 id="variables-example">Variables Example</h3>
<pre><code class="language-json">{&#10;	&quot;zoneTag&quot;: &quot;d6dfdf32c704a77ac227243a5eb5ca61&quot;,&#10;	&quot;start&quot;: &quot;2025-01-01T00:00:00Z&quot;,&#10;	&quot;end&quot;: &quot;2025-01-30T00:00:00Z&quot;,&#10;	&quot;limit&quot;: 10000,&#10;	&quot;orderBy&quot;: &quot;datetimeHour_ASC&quot;&#10;}&#10;</code></pre>
<p>Be sure to customize the zoneTag to match your specific zone, along with setting the desired start and end dates</p>
<h3 id="explanation-of-parameters">Explanation of Parameters</h3>
<ul>
<li><strong>zoneTag</strong>: Unique identifier of your Cloudflare zone.</li>
<li><strong>limit</strong>: Maximum number of results to return.</li>
<li><strong>start</strong> and <strong>end</strong>: Define the date range for the query in ISO 8601 format.</li>
<li><strong>orderBy</strong>: Determines the sorting order, such as by ascending or descending datetime.</li>
</ul>
<h2 id="example-curl-request">Example <code>curl</code> Request</h2>
<p>Use this <code>curl</code> command to query the Zaraz Monitoring API for the number of events processed by Zaraz. Replace <code>$TOKEN</code> with your API token, <code>$ZONE_TAG</code> with your zone tag, and adjust the start and end dates as needed.</p>
<pre><code class="language-bash">curl -X POST https://api.cloudflare.com/client/v4/graphql \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer $TOKEN&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;query&quot;: &quot;query AllEvents($zoneTag: String!, $limit: Int!, $start: Date, $end: Date, $orderBy: [ZoneZarazTriggersAdaptiveGroupsOrderBy!]) { viewer { zones(filter: { zoneTag: $zoneTag }) { data: zarazTrackAdaptiveGroups( limit: $limit filter: { datetimeHour_geq: $start datetimeHour_leq: $end } orderBy: [$orderBy] ) { count dimensions { ts: datetimeHour } } } } }&quot;,&#10;    &quot;variables&quot;: {&#10;      &quot;zoneTag&quot;: &quot;$ZONE_TAG&quot;,&#10;      &quot;start&quot;: &quot;2025-01-01T00:00:00Z&quot;,&#10;      &quot;end&quot;: &quot;2025-01-30T00:00:00Z&quot;,&#10;      &quot;limit&quot;: 10000,&#10;      &quot;orderBy&quot;: &quot;datetimeHour_ASC&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h3 id="explanation-of-the-curl-components">Explanation of the <code>curl</code> Components</h3>
<ul>
<li><strong>Authorization</strong>: The <code>Authorization</code> header requires a Bearer token. Replace <code>$TOKEN</code> with your actual API token.</li>
<li><strong>Content-Type</strong>: Set <code>application/json</code> to indicate a JSON payload.</li>
<li><strong>Data Payload</strong>: This payload includes the GraphQL query and variable parameters, such as <code>zoneTag</code>, <code>start</code>, <code>end</code>, <code>limit</code>, and <code>orderBy</code>.</li>
</ul>
<p>This <code>curl</code> example will return a JSON response containing event counts and timestamps within the specified date range. Modify the <code>variables</code> values as needed for your use case.</p>
<h2 id="additional-resources">Additional Resources</h2>
<p>Refer to the <a href="/analytics/graphql-api/">full GraphQL Analytics API documentation</a> for more details on available fields, filters, and further customization options for Zaraz Monitoring API queries.</p>
