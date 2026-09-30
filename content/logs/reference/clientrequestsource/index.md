<p>The possible values for the <code>ClientRequestSource</code> field are the following:</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Request source</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>0</code></td>
<td>unknown</td>
<td>Should never happen.</td>
</tr>
<tr>
<td><code>1</code></td>
<td>eyeball</td>
<td>A request from an end user. If you want to count requests made the Cloudflare Edge, the query should filter on <code>requestSource=eyeball</code>.</td>
</tr>
<tr>
<td><code>2</code></td>
<td>purge</td>
<td>A request made by Cloudflare's purge system.</td>
</tr>
<tr>
<td><code>3</code></td>
<td>alwaysOnline</td>
<td>A request made by Cloudflare's Always Online crawler.</td>
</tr>
<tr>
<td><code>4</code></td>
<td>healthcheck</td>
<td>A request made by Cloudflare's Health Check system.</td>
</tr>
<tr>
<td><code>5</code></td>
<td>edgeWorkerFetch</td>
<td>A fetch request made from an edge Worker.</td>
</tr>
<tr>
<td><code>6</code></td>
<td>edgeWorkerCacheAPI</td>
<td>A cache API call made from an edge Worker.</td>
</tr>
<tr>
<td><code>7</code></td>
<td>edgeWorkerKV</td>
<td>A KV call made from an edge Worker.</td>
</tr>
<tr>
<td><code>8</code></td>
<td>imageResizing</td>
<td>Requests made by Cloudflare's Image Resizing product.</td>
</tr>
<tr>
<td><code>9</code></td>
<td>orangeToOrange</td>
<td>A request that comes from another orange clouded zone.</td>
</tr>
<tr>
<td><code>10</code></td>
<td>sslDetector</td>
<td>A request made by Cloudflare's <a href="https://blog.cloudflare.com/ssl-tls-recommender/">SSL Detector system</a>.</td>
</tr>
<tr>
<td><code>11</code></td>
<td>earlyHintsCache</td>
<td>An <a href="https://blog.cloudflare.com/early-hints/">Early Hint request</a>.</td>
</tr>
<tr>
<td><code>12</code></td>
<td>inBrowserChallenge</td>
<td>An end user request caused by a Cloudflare security product (Challenges, JavaScript Detections). These requests never reach the origin.</td>
</tr>
</tbody>
</table>
