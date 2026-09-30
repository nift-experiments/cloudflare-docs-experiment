<p>Having access to Cloudflare’s provisioning capabilities allows you to more easily create and manage Cloudflare accounts. The following steps will get you started on making API calls to provision accounts, users, and services.</p>
<h2 id="before-you-begin">Before you begin</h2>
<h3 id="channel-and-alliance-partner-account-setup">Channel and Alliance partner account setup</h3>
<p>Before using the Tenant API, you need to <a href="/fundamentals/account/create-account/">create an account</a>, <a href="/fundamentals/user-profiles/verify-email-address/">verify your email address</a>, and <a href="/billing/get-started/create-billing-profile/">add your billing information</a>.</p>
<p>After you sign your partner agreement with Cloudflare, Cloudflare will add <a href="/tenant/structure/">certain entitlements</a> to your account that allow you to provision and manage custom accounts. If you have signed your partner agreement and your account has not yet been enabled, MSP partners should contact <code>partners@cloudflare.com</code> and Agency Partners should contact <code>agency@cloudflare.com</code>.</p>
<h3 id="api-access">API access</h3>
<p>You also need to <a href="/fundamentals/api/get-started/keys/#view-your-global-api-key">retrieve your API key</a> to authenticate your requests to the Tenant API.</p>
<p>For more details on using the Cloudflare API, refer to our <a href="/fundamentals/api/">API overview</a>.</p>
<h2 id="step-1-create-an-account">Step 1 - Create an account</h2>
<p>Each customer or team that uses Cloudflare should have their own account. This ensures proper security and access of resources. Each account acts as a container of zones and other resources. Depending on your needs, you may even provision multiple accounts for a single customer or team.</p>
<p>When you create an account with the Tenant API, your Cloudflare user owns that account from creation, ongoing management, and finally deletion.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/259.md")
</div></div>
<h2 id="step-2-grant-user-access">Step 2 - Grant user access</h2>
<p>Now that you have created an account, you need to either give your customer direct access to Cloudflare or build an interface for them to interact with.</p>
<p>The first method gives customers control over all aspects of Cloudflare, while the latter allows you to integrate your customer's Cloudflare experience into a dashboard that you control and that they may already be familiar with.</p>
<h3 id="option-1-direct-access-to-cloudflare">Option 1 - Direct access to Cloudflare</h3>
<p>When you grant user access to an account, Cloudflare will send an invitation to the user so they can get access to the account. If they do not already have a Cloudflare user, Cloudflare will take them through the process of creating one. Once created, they will be given access to the account and any zones already created.</p>
<h4 id="using-the-dashboard">Using the dashboard</h4>
<p>If you want to give customers access to their individual accounts, it is the same as if you were <a href="/fundamentals/manage-members/manage/#add-account-members">inviting a teammate</a> to help manage your account.</p>
<h4 id="using-the-api">Using the API</h4>
<p>You can also grant access to the Cloudflare dashboard by using the API.</p>
<pre><code class="language-bash">curl &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;CUSTOMER_ACCOUNT_ID&gt;/members&#x27; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;email&quot;: &quot;&lt;CUSTOMER_EMAIL&gt;&quot;,&#10;  &quot;roles&quot;: [&quot;&lt;USER_ROLE&gt;&quot;]&#10;}&#x27;&#10;</code></pre>
<p>In most cases, you will want to create new users with a role of <code>Administrator</code> which always has the ID <code>05784afa30c1afe1440e79d9351c7430</code>.</p>
<p>If your customer is on an Enterprise plan, they have access to a broader set of user roles. To get a full list of available roles, send a <a href="/api/resources/accounts/subresources/roles/methods/list/"><code>GET</code></a> request to the API.</p>
<h3 id="option-2-access-via-an-interface">Option 2 - Access via an interface</h3>
<p>If you want greater control over how customers use Cloudflare or if you want your customers to use an existing dashboard of yours that they already know, use the Cloudflare API to build this experience.</p>
<p>This means that you will be making API calls to Cloudflare on behalf of your customers. To avoid getting <a href="/fundamentals/api/reference/limits/">rate limited</a> by our API, Cloudflare recommend that you create accounts and users for each of your customers. Changes made by customer <code>A</code> should go through user <code>A</code> and changes made by customer <code>B</code> should go through user <code>B</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/256.md")
</aside>
<p>To grant access via an interface, you need to create a service user, as no one will log in to the dashboard with them. If you are planning to use this method, Cloudflare will enable you to see the API key in order to make API calls as this user.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/users&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;email&quot;: &quot;&lt;ID@example.com&gt;&quot;&#10;}&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;60758bd48392a06215ae817bc35084b6&quot;,&#10;		&quot;email&quot;: &quot;&lt;ID@example.com&gt;&quot;,&#10;		&quot;first_name&quot;: null,&#10;		&quot;last_name&quot;: null,&#10;		&quot;username&quot;: &quot;17bd2796b374cec14976ac3bced85c05&quot;,&#10;		&quot;telephone&quot;: null,&#10;		&quot;country&quot;: null,&#10;		&quot;created_on&quot;: &quot;2019-02-21T23:20:28.645256Z&quot;,&#10;		&quot;modified_on&quot;: &quot;2019-02-21T23:20:28.645256Z&quot;,&#10;		&quot;two_factor_authentication&quot;: {&#10;			&quot;enabled&quot;: false,&#10;			&quot;locked&quot;: false&#10;		},&#10;		&quot;api_key&quot;: &quot;xxx&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="step-3-create-a-zone">Step 3 - Create a zone</h2>
<p>Now that you have a customer account and customer users (or service users), you need to create a zone.</p>
<p>To do this, send a <a href="/api/resources/zones/methods/create/"><code>POST</code></a> request to the <code>/zones</code> endpoint (including the customer account ID you received in <a href="#step-1---create-an-account">Step 1</a>).</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;example.com&quot;,&#10;  &quot;account&quot;: {&#10;    &quot;id&quot;: &quot;&lt;CUSTOMER_ACCOUNT_ID&gt;&quot;&#10;  }&#10;}&#x27;&#10;</code></pre>
<h2 id="step-4-create-a-zone-plan-subscription">Step 4 - Create a zone plan subscription</h2>
<p>Now that you have a zone provisioned for the customer, you can add the appropriate zone plan based on your reseller agreement.</p>
<p>To create a zone subscription, typically used to upgrade a zone's plan from <code>PARTNERS_FREE</code> to a paid <a href="/tenant/reference/subscriptions/#zone-plans">Zone plan</a>, send a <a href="/api/resources/zones/subresources/subscriptions/methods/create/">POST</a> request to the <code>/zones/{zone_id}/subscription</code> endpoint and include the following values:</p>
<ul>
<li>
<p><code>rate_plan</code> object</p>
<ul>
<li>Contains the zone plan corresponding to what customers would order in the dashboard. For a list of available values, refer to <a href="/tenant/reference/subscriptions/#zone-plans">Zone subscriptions</a>.</li>
</ul>
</li>
<li>
<p><code>component_values</code> array</p>
<ul>
<li>Additional services depending on your reseller agreement, such as additional <code>page_rules</code>.</li>
</ul>
</li>
<li>
<p><code>frequency</code> string</p>
<ul>
<li>How often the subscription is renewed automatically (defaults to <code>&quot;monthly&quot;</code>).</li>
</ul>
</li>
</ul>
<pre><code class="language-bash">curl &#x27;https://api.cloudflare.com/client/v4/zones/{zone_id}/subscription&#x27; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;rate_plan&quot;: {&#10;    &quot;id&quot;: &quot;&lt;RATE_PLAN&gt;&quot;&#10;  },&#10;  &quot;frequency&quot;: &quot;annual&quot;&#10;}&#x27;&#10;</code></pre>
<pre><code class="language-bash">curl &#x27;https://api.cloudflare.com/client/v4/zones/{zone_id}/subscription&#x27; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;rate_plan&quot;: {&#10;    &quot;id&quot;: &quot;PARTNERS_BIZ&quot;&#10;  },&#10;  &quot;component_values&quot;: [&#10;    {&#10;      &quot;name&quot;: &quot;page_rules&quot;,&#10;      &quot;value&quot;: 50&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<h2 id="step-5-create-other-subscriptions">Step 5 - Create other subscriptions</h2>
<p>Depending on your agreement, you may be allowed to resell other add-on services. These are provisioned as account-level subscriptions.</p>
<p>To create an account subscription, send a <a href="/api/resources/accounts/subresources/subscriptions/methods/create/">POST</a> request to the <code>/accounts/{account_id}/subscriptions</code> endpoint and include the following values:</p>
<ul>
<li>
<p><code>rate_plan</code> object</p>
<ul>
<li>Contains the account subscription corresponding to a specific add-on service. For a list of available values, refer to <a href="/tenant/reference/subscriptions/">Available subscriptions</a>.</li>
</ul>
</li>
<li>
<p><code>component_values</code> array</p>
<ul>
<li>Additional services depending on your reseller agreement, such as additional endpoints for load balancing or additional seats for Cloudflare Zero Trust. If not included, the subscription includes the default values associated with each purchase.</li>
</ul>
</li>
<li>
<p><code>frequency</code> string</p>
<ul>
<li>How often the subscription is renewed automatically (defaults to <code>&quot;monthly&quot;</code>).</li>
</ul>
</li>
</ul>
<pre><code class="language-bash">curl &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/subscriptions&#x27; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;rate_plan&quot;: {&#10;    &quot;id&quot;: &quot;&lt;RATE_PLAN_NAME&gt;&quot;&#10;  }&#10;}&#x27;&#10;</code></pre>
<h2 id="step-6-configure-zone-and-services">Step 6 - Configure zone and services</h2>
<p>Once you have added the necessary subscriptions, you or your customer can move on to configuring various services and fine-tuning account and zone settings.</p>
<p>Configuration can be done by anyone with access to the account (as well as the correct user permissions). This process does not differ from configuring any other Cloudflare account. For additional guidance, refer to our <a href="/">Product docs</a>.</p>
