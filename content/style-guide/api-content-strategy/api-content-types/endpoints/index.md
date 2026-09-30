<h2 id="purpose">Purpose</h2>
<p>An endpoint is used to make HTTPS requests, and the <code>GET</code>, <code>POST</code>, <code>PUT</code>, <code>PATCH</code>, and <code>DELETE</code> methods dictate how to interact with the resource.</p>
<h2 id="structure">Structure</h2>
<h3 id="required-components">Required Components</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14613.md")
</aside>
<p><strong>Title</strong>: Title of the endpoint using sentence casing (first word capitalized). The titles do not use punctuation marks at the end of the title. Simple cases usually take one of the following forms:</p>
<p>Endpoints that act on/return a single item: verb + indefinite article + singular resource name.</p>
<ul>
<li>Example: Get a list item</li>
</ul>
<p>Endpoints that act on/return a collection of items: verb + plural resource name.</p>
<ul>
<li>Example: Get list items</li>
</ul>
<p><strong>Description</strong>: Describes what the endpoint does or how it should be used. Use punctuation at the end of the description.</p>
<p><strong>Plan availability</strong>: Lists the plan required to use the endpoint, such as Free, Pro, Business, or Enterprise.</p>
<p><strong>Method</strong>: Includes the type of method, such as <code>GET</code>, <code>POST</code>, <code>PUT</code>, <code>PATCH</code>, or <code>DELETE</code>.</p>
<p><strong>Endpoint</strong>: Lists the endpoint and should be stylized as code snippet.</p>
<p>When an endpoint will be deprecated in a specified timeframe but is still available, add a note to the endpoint description about the upcoming deprecation (&quot;<code>&lt;name of endpoint&gt;</code> will be deprecated on <code>&lt;full month name, date, year&gt;</code>. Use the <code>&lt;alternative endpoint&gt;</code> instead&quot;). Refer to <a href="/style-guide/api-content-strategy/api-content-types/deprecated-apis/">Deprecated APIs</a> for more information.</p>
<h3 id="optional-components">Optional components</h3>
<p><strong>Required permissions</strong>: Additional permissions at the user level that are required to use the endpoint.</p>
<h2 id="writing-guidelines">Writing guidelines</h2>
<p>When writing the titles and descriptions, keep our voice and tone in mind. Be concise and remember our users come from a variety of technical levels. Also, write in the active voice as much as possible to avoid sounding robotic and to make the information easier to understand.</p>
<p>Below are some examples of endpoint titles and descriptions for reference:</p>
<ul>
<li><strong>Get domain</strong>: Fetches a single domain.</li>
<li><strong>List workers</strong>: Fetches a list of uploaded workers.</li>
<li><strong>List pools</strong>: Lists configured pools.</li>
<li><strong>Create waiting room</strong>: Creates a new waiting room.</li>
<li><strong>Update health check</strong>: Updates configured health checks.</li>
</ul>
<h2 id="example">Example</h2>
<p><strong>Title</strong>: Get user audit logs</p>
<p><strong>Description</strong>: Gets a list of audit logs for a user account.</p>
<p><strong>Plan availability</strong>: Free, Pro, Business, Enterprise</p>
<p><strong>Method</strong>: <code>GET</code></p>
<p><strong>Endpoint</strong>: user/audit_logs</p>
