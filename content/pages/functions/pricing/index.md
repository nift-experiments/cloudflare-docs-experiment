<p>Requests to your Functions are billed as Cloudflare Workers requests. Workers plans and pricing can be found <a href="/workers/platform/pricing/">in the Workers documentation</a>.</p>
<h2 id="paid-plans">Paid Plans</h2>
<p>Requests to your Pages functions count towards your quota for Workers Paid plans, including requests from your Function to KV or Durable Object bindings.</p>
<p>Pages supports the <a href="/workers/platform/pricing/#example-pricing-standard-usage-model">Standard usage model</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10949.md")
</aside>
<h3 id="static-asset-requests">Static asset requests</h3>
<p>On both free and paid plans, requests to static assets are free and unlimited. A request is considered static when it does not invoke Functions. Refer to <a href="/pages/functions/routing/#functions-invocation-routes">Functions invocation routes</a> to learn more about when Functions are invoked.</p>
<h2 id="free-plan">Free Plan</h2>
<p>Requests to your Pages Functions count towards your quota for the Workers Free plan. For example, you could use 50,000 Functions requests and 50,000 Workers requests to use your full 100,000 daily request usage. The free plan daily request limit resets at midnight UTC.</p>
