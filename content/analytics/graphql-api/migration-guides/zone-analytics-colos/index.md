<p>This guide shows how you might migrate from the deprecated (and soon to be sunset) zone analytics API to the GraphQL API. It provides an example for a plausible use-case of the colos endpoint, then shows how that use-case is translated to the GraphQL API. It also explores features of the GraphQL API that make it more powerful than the API it replaces.</p>
<p>In this example, we want to calculate the number of requests for a particular colo, broken down by the hour in which the requests occurred. Referring to the zone analytics colos endpoint, we can construct a curl which retrieves the data from the API.</p>
<pre><code class="language-bash">curl -H &quot;Authorization: Bearer $API_TOKEN&quot; &quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID/analytics/colos?since=2020-12-10T00:00:00Z&quot;  &gt; colos_endpoint_output.json&#10;</code></pre>
<p>This query says:</p>
<ul>
<li>Given an <code>API_TOKEN</code> which has Analytics Read access to <code>ZONE_ID</code>.</li>
<li>Fetch colos analytics for <code>ZONE_ID</code> with a time range that starts on
<code>2020-12-10T00:00:00Z</code> (<code>since</code> parameter) to now.</li>
</ul>
<p>The question that we want to answer is: &quot;What is the number of requests for ZHR per hour?&quot; Using the colos endpoint response data and some wrangling by jq we can answer that question with this command:</p>
<pre><code class="language-bash">cat colos_endpoint_output.json | jq  -c &#x27;.result[] | {colo_id: .colo_id, timeseries: .timeseries[]} | {colo_id: .colo_id, timeslot: .timeseries.since, requests: .timeseries.requests.all, bandwidth: .timeseries.bandwidth.all} | select(.requests &gt; 0) | select(.colo_id == &quot;ZRH&quot;) &#x27;&#10;</code></pre>
<p>This jq command is complex, so we can break it down:</p>
<pre><code class="language-bash">.result[]&#10;</code></pre>
<p>This means that the result array is split into individual json lines.</p>
<pre><code class="language-bash">{colo_id: .colo_id, timeseries: .timeseries[]}&#10;</code></pre>
<p>This breaks each json line into multiple json lines. Each resulting line contains a <code>colo_id</code> and one element of the <code>timeseries</code> array.</p>
<pre><code class="language-bash">{colo_id: .colo_id, timeslot: .timeseries.since, requests: .timeseries.requests.all, bandwidth: .timeseries.bandwidth.all}&#10;</code></pre>
<p>This flattens out the data we are interested in that is inside the timeseries
object of each line.</p>
<pre><code class="language-bash">select(.requests &gt; 0) | select(.colo_id == &quot;ZRH&quot;)&#10;</code></pre>
<p>This selects only lines that contain more than 0 requests and the <code>colo_id</code> is ZRH.</p>
<p>The final data we get looks like the following response:</p>
<details class="nb-details"><summary>Response</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3167.md")
</div></details>
<p>How do we get the same result using the GraphQL API?</p>
<p>The GraphQL API allows us to be much more specific about the data that we want to retrieve. While the colos endpoint forces us to retrieve all the information about the breakdown of requests and bandwidth per colo, using the GraphQL API allows us to fetch only the information we are interested in.</p>
<p>The data we want is about HTTP requests. Hence, we use the canonical source for HTTP request data, also known as <code>httpRequestsAdaptiveGroups</code>. This node in GraphQL API allows you to filter and group by almost any dimension of an HTTP request imaginable. It is <a href="/analytics/network-analytics/understand/concepts/#adaptive-bit-rate-sampling">Adaptive</a> so responses will be fast since it is driven by our <a href="https://blog.cloudflare.com/explaining-cloudflares-abr-analytics/">ABR technology</a>.</p>
<p>The following is a GraphQL API query to retrieve the data we need to answer the question: &quot;What is the number of requests for ZHR per hour?&quot;</p>
<pre><code class="language-txt">{&#10;  viewer {&#10;    zones(filter: {zoneTag:&quot;$ZONE_TAG&quot;}) {&#10;      httpRequestsAdaptiveGroups(filter: {datetime_gt: &quot;2020-12-10T00:00:00Z&quot;, coloCode:&quot;ZRH&quot;}, limit:10000, orderBy: [datetimeHour_ASC]) {&#10;        count&#10;        sum {&#10;          edgeResponseBytes&#10;        }&#10;        avg {&#10;          sampleInterval&#10;        }&#10;        count&#10;        dimensions {&#10;          datetimeHour&#10;          coloCode&#10;        }&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Then we can run it with curl:</p>
<pre><code class="language-bash">curl -X POST -H &quot;Authorization: Bearer $API_TOKEN&quot;  https://api.cloudflare.com/client/v4/graphql -d &quot;@./coloGroups.json&quot; &gt; graphqlColoGroupsResponse.json&#10;</code></pre>
<p>We can answer our question in the same way as before using jq:</p>
<pre><code class="language-bash">cat graphqlColoGroupsResponse.json| jq -c &#x27;.data.viewer.zones[] | .httpRequestsAdaptiveGroups[] | {colo_id: .dimensions.coloCode, timeslot: .dimensions.datetimeHour, requests: .count, bandwidth: .sum.edgeResponseBytes}&#x27;&#10;</code></pre>
<p>This command is much simpler than what we had before, because the data returned by the GraphQL API is more specific than what is returned by the colos endpoint.</p>
<p>Still, it is worth explaining the command since it will help to understand some of the concepts underlying the GraphQL API.</p>
<pre><code class="language-bash">.data.viewer.zones[]&#10;</code></pre>
<p>The format of a GraphQL response is very similar to the query. A successful response always contains a <code>data</code> object which wraps the data in the response. A query will always have a <code>viewer</code> object which represents your user. Then, we unwrap the zones objects, one per line. Our query only has one zone (since this is how we chose to do it). But a query could have multiple zones as well.</p>
<pre><code class="language-bash">.httpRequestsAdaptiveGroups[]&#10;</code></pre>
<p>The <code>httpRequestsAdaptiveGroups</code> field is a list, where each datapoint in the list represents a combination of the dimensions that were selected, along with the aggregation that was selected for that combination of the dimensions. Here, we unwrap each of the datapoints, one per row.</p>
<pre><code class="language-bash">{colo_id: .dimensions.coloCode, timeslot: .dimensions.datetimeHour, requests: .count, bandwidth: .sum.edgeResponseBytes}&#10;</code></pre>
<p>This is straightforward: it just selects the attributes of each datapoint that we are interested in, in the format which we used previously in the colos endpoint.</p>
<p>The GraphQL API is a very powerful tool, as you can filter and group the data by many dimensions. This feature is totally absent from the colos endpoint in the Zone Analytics API.</p>
