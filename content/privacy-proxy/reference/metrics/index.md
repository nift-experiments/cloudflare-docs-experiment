<p>Privacy Proxy provides two methods for accessing metrics and monitoring your proxy deployment. We recommend getting started with GraphQL as the default method for observability.</p>
<ul class="directory-listing"><li><a href="/privacy-proxy/reference/metrics/graphql/">GraphQL Analytics API</a></li><li><a href="/privacy-proxy/reference/metrics/opentelemetry/">OpenTelemetry</a></li></ul>
<h2 id="data-privacy">Data privacy</h2>
<p>Regardless of whether you use the GraphQL Analytics API or OpenTelemetry, Privacy Proxy observability data does not include:</p>
<ul>
<li>User IP addresses</li>
<li>Request content or headers (beyond what is needed for metrics)</li>
<li>Destination URLs or hostnames (aggregated only)</li>
<li>Authentication tokens or credentials</li>
</ul>
<p>Both methods export only operational metrics that help you monitor service health without compromising user privacy.</p>
