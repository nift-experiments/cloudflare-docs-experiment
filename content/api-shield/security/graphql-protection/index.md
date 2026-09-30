<p>GraphQL is a query language for APIs. In addition to protecting RESTful APIs, Cloudflare can also protect GraphQL APIs.</p>
<p>GraphQL malicious query protection scans your GraphQL traffic for queries that could overload your origin and result in a denial of service. You can build rules that limit the query depth and size of incoming GraphQL queries in order to block suspiciously large or complex queries.</p>
<h2 id="availability">Availability</h2>
<p>GraphQL malicious query protection is available for all API Shield customers. Enterprise customers who have not purchased API Shield can preview <a href="https://dash.cloudflare.com/?to=/:account/:zone/security/api-shield">API Shield as a non-contract service</a> in the Cloudflare dashboard or by contacting your account team.</p>
<h2 id="limitations">Limitations</h2>
<p>The following limitations apply:</p>
<ul>
<li>Parsing is limited to GraphQL <code>POST</code> bodies smaller than 20 KB. This limit will be raised in a future release.</li>
<li>Only <code>POST</code> requests with content types of <code>application/json</code> or <code>application/graphql</code> are inspected.</li>
<li>Queries containing fragments or multiple operations are not supported.</li>
<li>Parsing and rules are limited to paths ending in <code>/graphql</code>.</li>
</ul>
