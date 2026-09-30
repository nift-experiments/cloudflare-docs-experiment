<p>Stream provides analytics about both live video and video uploaded to Stream, via the GraphQL API described below, as well as on the Stream <strong>Analytics</strong> page of the Cloudflare dashboard.</p>
<div class="nb-dash-button"></div>
<p>The Stream Analytics API uses the Cloudflare GraphQL Analytics API, which can be used across many Cloudflare products. For more about GraphQL, rate limits, filters, and sorting, refer to the <a href="/analytics/graphql-api">Cloudflare GraphQL Analytics API docs</a>.</p>
<h2 id="getting-started">Getting started</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account API tokens</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Generate an API token with the <strong>Account Analytics</strong> permission.</li>
<li>Use a GraphQL client of your choice to make your first query. <a href="https://www.postman.com/">Postman</a> has a built-in GraphQL client which can help you run your first query and introspect the GraphQL schema to understand what is possible.</li>
</ol>
<p>Refer to the sections below for available metrics, dimensions, fields, and example queries.</p>
<h2 id="server-side-analytics">Server side analytics</h2>
<p>Stream collects data about the number of minutes of video delivered to viewers for all live and on-demand videos played via HLS or DASH, regardless of whether or not you use the <a href="/stream/viewing-videos/using-the-stream-player/">Stream Player</a>.</p>
<h3 id="filters-and-dimensions">Filters and Dimensions</h3>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>date</code></td>
<td>Date</td>
</tr>
<tr>
<td><code>datetime</code></td>
<td>DateTime</td>
</tr>
<tr>
<td><code>uid</code></td>
<td>UID of the video</td>
</tr>
<tr>
<td><code>clientCountryName</code></td>
<td>ISO 3166 alpha2 country code from the client who viewed the video</td>
</tr>
<tr>
<td><code>creator</code></td>
<td>The <a href="/stream/manage-video-library/creator-id/">Creator ID</a> associated with individual videos, if present</td>
</tr>
</tbody>
</table>
<p>Some filters, like <code>date</code>, can be used with operators, such as <code>gt</code> (greater than) and <code>lt</code> (less than), as shown in the example query below. For more advanced filtering options, refer to <a href="/analytics/graphql-api/features/filtering/">filtering</a>.</p>
<h3 id="metrics">Metrics</h3>
<table>
<thead>
<tr>
<th>Node</th>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>streamMinutesViewedAdaptiveGroups</code></td>
<td><code>minutesViewed</code></td>
<td>Minutes of video delivered</td>
</tr>
</tbody>
</table>
<h3 id="example">Example</h3>
<h4 id="get-minutes-viewed-by-country">Get minutes viewed by country</h4>
<pre><code class="language-graphql">query StreamGetMinutesExample($accountTag: string!, $start: Date, $end: Date) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			streamMinutesViewedAdaptiveGroups(&#10;				filter: { date_geq: $start, date_lt: $end }&#10;				orderBy: [sum_minutesViewed_DESC]&#10;				limit: 100&#10;			) {&#10;				sum {&#10;					minutesViewed&#10;				}&#10;				dimensions {&#10;					uid&#10;					clientCountryName&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;data&quot;: {&#10;		&quot;viewer&quot;: {&#10;			&quot;accounts&quot;: [&#10;				{&#10;					&quot;streamMinutesViewedAdaptiveGroups&quot;: [&#10;						{&#10;							&quot;dimensions&quot;: {&#10;								&quot;clientCountryName&quot;: &quot;US&quot;,&#10;								&quot;uid&quot;: &quot;73c514082b154945a753d0011e9d7525&quot;&#10;							},&#10;							&quot;sum&quot;: {&#10;								&quot;minutesViewed&quot;: 2234&#10;							}&#10;						},&#10;						{&#10;							&quot;dimensions&quot;: {&#10;								&quot;clientCountryName&quot;: &quot;CN&quot;,&#10;								&quot;uid&quot;: &quot;73c514082b154945a753d0011e9d7525&quot;&#10;							},&#10;							&quot;sum&quot;: {&#10;								&quot;minutesViewed&quot;: 700&#10;							}&#10;						},&#10;						{&#10;							&quot;dimensions&quot;: {&#10;								&quot;clientCountryName&quot;: &quot;IN&quot;,&#10;								&quot;uid&quot;: &quot;73c514082b154945a753d0011e9d7525&quot;&#10;							},&#10;							&quot;sum&quot;: {&#10;								&quot;minutesViewed&quot;: 553&#10;							}&#10;						}&#10;					]&#10;				}&#10;			]&#10;		}&#10;	},&#10;	&quot;errors&quot;: null&#10;}&#10;</code></pre>
<h2 id="pagination">Pagination</h2>
<p>GraphQL API supports seek pagination: using filters, you can specify the last video UID so the response only includes data for videos after the last video UID.</p>
<p>The query below will return data for 2 videos that follow video UID <code>5646153f8dea17f44d542a42e76cfd</code>:</p>
<pre><code class="language-graphql">query StreamPaginationExample(&#10;	$accountTag: string!&#10;	$start: Date&#10;	$end: Date&#10;	$uId: string&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			videoPlaybackEventsAdaptiveGroups(&#10;				filter: { date_geq: $start, date_lt: $end, uid_gt: $uId }&#10;				orderBy: [uid_ASC]&#10;				limit: 2&#10;			) {&#10;				count&#10;				sum {&#10;					timeViewedMinutes&#10;				}&#10;				dimensions {&#10;					uid&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Here are the steps to implementing pagination:</p>
<ol>
<li>Call the first query without uid_gt filter to get the first set of videos</li>
<li>Grab the last video UID from the response from the first query</li>
<li>Call next query by specifying uid_gt property and set it to the last video UID. This will return the next set of videos</li>
</ol>
<p>For more on pagination, refer to the <a href="/analytics/graphql-api/features/pagination/">Cloudflare GraphQL Analytics API docs</a>.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>The maximum query interval in a single query is 31 days</li>
<li>The maximum data retention period is 90 days</li>
</ul>
