<p>Cloudflare separates service configuration by zone. When there are multiple accounts, each with many zones, it is important to restrict GraphQL Analytics API access to only those account and zone resources that are relevant for the task at hand.</p>
<p>To secure access to your GraphQL Analytics data, use a Cloudflare API key or token to authenticate an API request.</p>
<p>This table outlines the differences between Cloudflare API keys and tokens:</p>
<table>
<thead>
<tr>
<th>Authentication Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href='/fundamentals/api/get-started/create-token/'>API Tokens</a></td>
<td>Cloudflare recommends API Tokens as the preferred way to interact with Cloudflare APIs. You can configure the scope of tokens to limit access to account and zone resources, and you can define the Cloudflare APIs to which the token authorizes access.</td>
</tr>
<tr>
<td><a href='/fundamentals/api/get-started/keys/'>API Keys</a></td>
<td><p>Unique to each Cloudflare user and used only for authentication. API keys do not authorize access to accounts or zones.</p>
        <p>Use the Global API Key for authentication.</p></td>
</tr>
</tbody>
</table>
<p>To create and configure GraphQL Analytics API tokens, refer to <a href="/analytics/graphql-api/getting-started/authentication/api-token-auth/">Configure an Analytics API token</a>.</p>
<p>To find and retrieve API keys, as well as edit HTTP headers for authentication in GraphiQL, refer to <a href="/analytics/graphql-api/getting-started/authentication/api-key-auth/">Authenticate with a Cloudflare API key</a>.</p>
