<ol>
<li>
<p>Launch <a href="https://www.gatsbyjs.com/docs/how-to/querying-data/running-queries-with-graphiql/">GraphiQL</a>.</p>
</li>
<li>
<p>Select <strong>Edit HTTP Headers</strong>.
<img src="/assets/upstream/images/analytics/GraphiQL-edit-http-headers.png" alt="Clicking Edit HTTP Headers" />
The <strong>Edit HTTP Headers</strong> window appears.
<img src="/assets/upstream/images/analytics/GraphiQL-edit-http-headers-window.png" alt="Editing HTTP Headers Window" /></p>
</li>
<li>
<p>Select <strong>Add Header</strong> to configure authentication. You can use Cloudflare Analytics API token authentication (recommended) or Cloudflare API key authentication.</p>
<ul>
<li>
<p><strong>Token authentication</strong>:</p>
<p>Enter <strong>Authorization</strong> in the <strong>Header Name</strong> field, and enter <code>Bearer {your-analytics-token}</code> in the <strong>Header value</strong> field, then select <strong>Save</strong>.</p>
</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/analytics/GraphiQL-edit-http-headers-token.png" alt="Editing HTTP Headers" /></p>
<ul>
<li>
<p><strong>Key authentication</strong>:</p>
<p>Enter <code>X-AUTH-EMAIL</code> in the <strong>Header name</strong> field and your email address registered with Cloudflare in the <strong>Header value</strong> field, and select <strong>Save</strong>.<br/></p>
<p>Select <strong>Add Header</strong> to add a second header. Enter <code>X-AUTH-KEY</code> in the <strong>Header Name</strong> field, and paste your Global API Key in the <strong>Header value</strong> field, then select <strong>Save</strong>.<br/></p>
</li>
</ul>
<ol start="4">
<li>
<p>Select anywhere outside the <strong>Edit HTTP Headers</strong> window in GraphiQL to close it and return to the main GraphiQL display.</p>
</li>
<li>
<p>Enter <code>https://api.cloudflare.com/client/v4/graphql</code> in the <strong>GraphQL Endpoint</strong> field.
<img src="/assets/upstream/images/analytics/GraphiQL-response-pane.png" alt="Editing GraphQL Endpoint" /></p>
</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3176.md")
</aside>
<p>Now that you have configured authentication, you are ready to run queries using GraphiQL.</p>
