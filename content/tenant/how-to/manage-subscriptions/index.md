<p>Once your customer has a zone provisioned, you can add zone and account-level subscriptions.</p>
<h2 id="zone-subscriptions">Zone subscriptions</h2>
<h3 id="create-zone-subscription">Create zone subscription</h3>
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
<h3 id="get-zone-subscription-details">Get zone subscription details</h3>
<p>To get the details of a zone subscription, send a <a href="/api/resources/zones/subresources/subscriptions/methods/get/"><code>GET</code></a> request to the <code>/zones/&lt;ZONE_ID&gt;/subscription</code> endpoint.</p>
<h3 id="update-zone-subscription">Update zone subscription</h3>
<p>To update a subscription on a zone, typically used to update an existing subscription's 'component_values' or to downgrade a zone's subscription, send a <a href="/api/resources/zones/subresources/subscriptions/methods/update/"><code>PUT</code></a> request to the <code>/zones/&lt;ZONE_ID&gt;/subscription</code> endpoint.</p>
<hr />
<h2 id="account-subscriptions">Account subscriptions</h2>
<p>Depending on your agreement, you may be allowed to resell other add-on services. These are provisioned as account-level subscriptions.</p>
<h3 id="create-account-subscription">Create account subscription</h3>
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
<h3 id="get-account-subscription-details">Get account subscription details</h3>
<p>To get all subscriptions for an account, send a <a href="/api/resources/accounts/subresources/subscriptions/methods/get/"><code>GET</code></a> request to the <code>/accounts/&lt;ACCOUNT_ID&gt;/subscriptions</code> endpoint.</p>
<h3 id="update-account-subscription">Update account subscription</h3>
<p>To update a subscription on an account, send a <a href="/api/resources/accounts/subresources/subscriptions/methods/update/"><code>PUT</code></a> request to the <code>/accounts/&lt;ACCOUNT_ID&gt;/subscriptions/&lt;SUBSCRIPTION_ID&gt;</code> endpoint.</p>
<h3 id="delete-account-subscription">Delete account subscription</h3>
<p>To delete a subscription on an account, send a <a href="/api/resources/accounts/subresources/subscriptions/methods/delete/"><code>DELETE</code></a> request to the <code>/accounts/&lt;ACCOUNT_ID&gt;/subscriptions/&lt;SUBSCRIPTION_ID&gt;</code> endpoint.</p>
