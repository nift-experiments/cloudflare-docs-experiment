<p>Using <a href="https://developer.chrome.com/docs/devtools">Chrome DevTools</a>, you can capture the queries running behind the Cloudflare Dashboard analytics. In this example, we will focus on the Network Analytics dataset, but the same process can be applied to any other analytics available in your dashboard.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Network Analytics</strong> page or any other analytics dashboard you are interested in seeing the GraphQL queries in.</li>
</ol>
<div class="nb-dash-button"></div>
<p><img src="/assets/upstream/images/analytics/analytics-tab.png" alt="Analytics tab" /></p>
<ol start="2">
<li>Open the <a href="https://developer.chrome.com/docs/devtools">Chrome Developer Tools</a> and select <strong>Inspect</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/analytics/chrome-developer-tools.png" alt="Chrome developer tools" /></p>
<ol start="3">
<li>Select the <strong>Network</strong> tab in the Developer Tools panel.</li>
<li>In the filter bar, type <code>graphql</code> to filter out the GraphQL requests. If no requests appear, try reloading the page. As the page reloads, several network requests will populate the <strong>Network</strong> tab. Look for requests that contain <code>graphql</code> in the name.</li>
</ol>
<p><img src="/assets/upstream/images/analytics/search-field.png" alt="Type graphql in the search field" /></p>
<ol start="5">
<li>Select one of the GraphQL requests to open its details and go to the <strong>Payload</strong> tab. There you will find the GraphQL query. Select the query line and then <strong>Copy value</strong> to capture the query.</li>
</ol>
<p><img src="/assets/upstream/images/analytics/copy-value.png" alt="Copy query value" /></p>
<ol start="6">
<li>If you want to capture a new query, adjust the filters in the <strong>Network analytics</strong> dashboard and a new query will appear in the GraphQL requests.</li>
</ol>
<p><img src="/assets/upstream/images/analytics/new-query.png" alt="Create a new query" /></p>
<p>You can now use this query as the basis for your API call. Refer to the <a href="/analytics/graphql-api/getting-started/">Get started</a> section for more information.</p>
