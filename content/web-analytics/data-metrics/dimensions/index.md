<p>Dimensions are the labels used to describe different types of metrics or data. For example, <strong>Referer</strong> is the data collected from external links referring visits to a page, while <strong>Browser</strong> shows which browsers accessed your website.</p>
<p>Below you can find a list of the different dimensions you can use to filter Web Analytics:</p>
<ul>
<li><strong>Country</strong>: The visitor's country.</li>
<li><strong>Host</strong>: The domain of the site's URL.</li>
<li><strong>Path</strong>: The links within your site referring visits to a page.</li>
<li><strong>Referer</strong>: The external links referring visits to a page. You can access <code>referer host</code> data on the dashboard. Additionally, you can access data for the <code>referer path</code> from the GraphQL API.</li>
<li><strong>Device type</strong>: The device visitors use to access a page (for example, desktop, mobile, or tablet).</li>
<li><strong>Browser</strong>: The web browser (for example, Chrome, Safari) visitors use to access your website.</li>
<li><strong>Operating system</strong>: The operating system visitors use to access a page.</li>
<li><strong>Site</strong>: The website's domain name. Used for high-level segmentation of data. For example, you can use it for a particular zone or gray-clouded website.</li>
<li><strong>Exclude Bots</strong>: Exclude bot traffic from the dataset. With this dimension set to <code>Yes</code>, the resulting dataset will be a closer representation of real user traffic.</li>
<li><strong>Navigation type</strong>: Which method was used to load the HTML document. Refer to <a href="#navigation-types">Navigation types</a> for a breakdown.</li>
</ul>
<p><img src="/assets/upstream/images/web-analytics/dash-web_analytics-dimensions.png" alt="Web Analytics dimensions page" /></p>
<h2 id="navigation-types">Navigation types</h2>
<table>
<thead>
<tr>
<th>Type</th>
<th>Cache hit?</th>
<th>Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td>Navigate</td>
<td>❌</td>
<td>The visitor clicked a link or submitted a form but the document was either not found or stale in the browsers HTTP cache, so a network request was made to load the document.</td>
</tr>
<tr>
<td>Navigate Cache</td>
<td>✅</td>
<td>The visitor clicked a link or submitted a form and the document was found and fresh within the browsers HTTP cache, so no network request was necessary for the document.</td>
</tr>
<tr>
<td>Navigate Prefetch Cache</td>
<td>✅</td>
<td>The visitor clicked a link or submitted a form and the document has been prefetched into the browsers HTTP cache, so no network request was necessary for the document.</td>
</tr>
<tr>
<td>Prerender</td>
<td>✅</td>
<td>The visitor clicked a link or submitted a form but the browser had already prerendered the page, so no network request was necessary for the document.</td>
</tr>
<tr>
<td>Reload</td>
<td>❌</td>
<td>The visitor reloaded the page but the document was either not found or stale in the browsers HTTP cache, so a network request was made to load the document.</td>
</tr>
<tr>
<td>Reload Cache</td>
<td>✅</td>
<td>The visitor reloaded the page and the document was found and fresh within the browsers HTTP cache, so no network request was necessary for the document.</td>
</tr>
<tr>
<td>Back-forward</td>
<td>❌</td>
<td>The visitor used the back/forward buttons/gestures in their browser but the previously-loaded document either not found or stale in the browsers HTTP cache OR a feature was used which prevents using the cache (refer to the explanation in <a href="https://web.dev/articles/bfcache">Back/forward cache</a>), so a network request was made to load the document.</td>
</tr>
<tr>
<td>Back-forward Cache</td>
<td>✅</td>
<td>The visitor used the back/forward buttons/gestures in their browser and the document was found and fresh within the browsers HTTP cache, so no network request was necessary for the document.</td>
</tr>
<tr>
<td>Restore</td>
<td>✅</td>
<td>The browser was able to restore this page, for example when a tab has been paused due to inactivity.</td>
</tr>
<tr>
<td>Soft Navigation</td>
<td>N/A</td>
<td>The visitor clicked a link or submitted a form but JavaScript intercepted the navigation and made a client-side update instead. Measured via <a href="https://developer.chrome.com/docs/web-platform/soft-navigations">the native Soft Navigation API</a>.</td>
</tr>
<tr>
<td>Routing APIs</td>
<td>N/A</td>
<td>The visitor clicked a link or submitted a form but JavaScript intercepted the navigation and made a client-side update instead. Measured via <a href="https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API">the Navigation API</a> or <a href="https://developer.mozilla.org/en-US/docs/Web/API/History_API">the History API</a> when the Soft Navigation API is not supported.</td>
</tr>
</tbody>
</table>
