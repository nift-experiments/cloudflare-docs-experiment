<p>API Shield Routing allows you to expose a single external API that routes requests to different back-end services, even when those services use different paths or hostnames than your zone.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3231.md")
</aside>
<h2 id="process">Process</h2>
<p>You must add Source Endpoints to Endpoint Management through established methods, including <a href="/api-shield/security/schema-validation/#add-validation-by-uploading-a-schema">uploading a schema</a>, via <a href="/api-shield/security/api-discovery/">API Discovery</a>, or by <a href="/api-shield/management-and-monitoring/#add-endpoints-manually">adding manually</a>, before creating a route.</p>
<p>To create a route, you will need the operation ID of the Source Endpoint. To find the operation ID in the dashboard:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3232.md")
</div>
<p>Once your Source Endpoints are added to Endpoint Management, use the following steps to create and verify routes on any given operation ID:</p>
<h3 id="create-a-route">Create a route</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3233.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3230.md")
</aside>
<p>You can also edit or delete a route by selecting <strong>Edit route</strong> on an existing route.</p>
<h3 id="test-a-route">Test a route</h3>
<p>After sending a request to your Source Endpoint, you should see the contents of the back-end service as if you called the Target Endpoint directly.</p>
<p>If API Shield returns unexpected results, check your Source Endpoint host, method, and path and <a href="/api-shield/management-and-monitoring/api-routing/#verify-a-route">verify the Route</a> to ensure the Target Endpoint value is correct.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3229.md")
</aside>
<h2 id="availability">Availability</h2>
<p>API Shield Routing is currently in an open beta and is only available for Enterprise customers subscribed to API Shield. Enterprise customers who have not purchased API Shield can preview <a href="https://dash.cloudflare.com/?to=/:account/:zone/security/api-shield">API Shield as a non-contract service</a> in the Cloudflare dashboard or by contacting your account team.</p>
<h2 id="limitations">Limitations</h2>
<p>The Target Endpoint cannot be routed to a Worker if the route is to the same zone.</p>
<p>You cannot change the method of a request. For example, a <code>GET</code> Source Endpoint will always send a <code>GET</code> request to the Target Endpoint.</p>
<p>You must use all of the variables in the Target Endpoint that appear in the Source Endpoint. For example, routing <code>/api/{var1}/users/{var2}</code> to <code>/api/users/{var2}</code> is not allowed and will result in an error since <code>{var1}</code> is present in the Source Endpoint but not in the Target Endpoint.</p>
