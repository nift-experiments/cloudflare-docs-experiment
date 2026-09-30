<p>Cloudflare recommends API tokens as the preferred authentication method with Cloudflare APIs. This article walks through creating API tokens for authentication to the GraphQL Analytics API.</p>
<p>For more details on API tokens and the full range of supported options, refer to <a href="/fundamentals/api/get-started/create-token/">Creating API tokens</a>.</p>
<p>To create an API token for authentication to the GraphQL Analytics API, use this workflow:</p>
<ul>
<li><a href="#access-the-create-api-token-page">Access the Create API Token page</a></li>
<li><a href="#configure-a-custom-api-token">Configure a custom API token</a></li>
<li><a href="#review-and-create-your-api-token">Review and create your API token</a></li>
<li><a href="#copy-and-test-your-api-token">Copy and test your API token</a></li>
</ul>
<h2 id="access-the-create-api-token-page">Access the Create API Token page</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account API tokens</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create Token</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/analytics/user-profile-api-tokens-tab.png" alt="API Tokens tab" /></p>
<p>The <strong>Create API Token</strong> page displays.</p>
<p><img src="/assets/upstream/images/analytics/create-api-token-page-display.png" alt="Clicking Get started in the Create API Token page" /></p>
<p>The next section of this walkthrough shows you how to configure a custom token for access to the GraphQL Analytics API.</p>
<h2 id="configure-a-custom-api-token">Configure a custom API token</h2>
<p>To configure a custom token, follow these steps:</p>
<ol>
<li>Select <strong>Get started</strong> in the <strong>Custom token</strong> section of the <strong>Create API Token</strong> page:</li>
</ol>
<p><img src="/assets/upstream/images/analytics/create-api-token-get-started.png" alt="Clicking Get started in the Create API Token page" /></p>
<p>The <strong>Create Custom Token</strong> page displays:</p>
<p><img src="/assets/upstream/images/analytics/create-custom-api-token.png" alt="Create Custom Token page" /></p>
<ol start="2">
<li>
<p>Enter a descriptive name for your token in the <strong>Token name</strong> text input field.</p>
</li>
<li>
<p>To configure access to the GraphQL Analytics API, use the <strong>Permissions</strong> drop-down lists.</p>
</li>
<li>
<p>To set permissions for the GraphQL Analytics API, select <em>Account</em> in the first drop-down list, <em>Account Analytics</em> from the second drop-down list, and <em>Read</em> from the third.</p>
</li>
</ol>
<p>This example scopes account-level permissions for read access to the Analytics API:</p>
<p><img src="/assets/upstream/images/analytics/create-custom-token-permissions.png" alt="Permissions configuration page" /></p>
<ol start="5">
<li>To configure the specific zones to which the token grants access, use the <strong>Zone Resources</strong> drop-down lists. In this example, the token is set to grant access to all zones:</li>
</ol>
<p><img src="/assets/upstream/images/analytics/create-custom-token-zone-resources.png" alt="Resources configuration page" /></p>
<ol start="6">
<li>To restrict the API token to specific IP addresses, use the <strong>Client IP Address Filtering</strong> controls.</li>
</ol>
<p><img src="/assets/upstream/images/analytics/create-custom-token-ip-address-filtering.png" alt="IP Address Filtering configuration page" /></p>
<ol start="7">
<li>To define how long the token is valid, select the <strong>TTL</strong> (time-to-live) start/end date.</li>
</ol>
<p><img src="/assets/upstream/images/analytics/create-custom-token-ttl.png" alt="TTL configuration page" /></p>
<ol start="8">
<li>Select <strong>Continue to summary</strong>.</li>
</ol>
<p>The next section of this walkthrough covers how to review and test your API token.</p>
<h2 id="review-and-create-your-api-token">Review and create your API token</h2>
<p>Once you select <strong>Continue to summary</strong>, the <strong>API Token Summary</strong> page displays.</p>
<p>Use the <strong>API Token Summary</strong> to confirm that you have scoped the API Token to the desired permissions and resources before creating it.</p>
<p><img src="/assets/upstream/images/analytics/api-token-summary.png" alt="API Token Summary page" /></p>
<p>Once you have validated your API token configuration, select <strong>Create Token</strong>.</p>
<h2 id="copy-and-test-your-api-token">Copy and test your API token</h2>
<p>When you create a new token, a confirmation page displays that includes your token and a custom <code>curl</code> command.</p>
<p><img src="/assets/upstream/images/fundamentals/api/token-complete.png" alt="Page displaying your API token and the curl command to test your token" /></p>
<p>To copy the token to your device's clipboard, select the <strong>Copy</strong> button.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/3177.md")
</aside>
<p>To test your token, copy the <code>curl</code> command and paste it into a terminal.</p>
<p>When you have finished, select <strong>View all API tokens</strong>.</p>
