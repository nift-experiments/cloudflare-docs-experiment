<p>Rate limiting controls the traffic that reaches your application, which prevents expensive bills and suspicious activity.</p>
<h2 id="parameters">Parameters</h2>
<p>You can define rate limits as the number of requests that get sent in a specific time frame. For example, you can limit your application to 100 requests per 60 seconds.</p>
<p>You can also select if you would like a <strong>fixed</strong> or <strong>sliding</strong> rate limiting technique. With rate limiting, we allow a certain number of requests within a window of time. For example, if it is a fixed rate, the window is based on time, so there would be no more than <code>x</code> requests in a ten minute window. If it is a sliding rate, there would be no more than <code>x</code> requests in the last ten minutes.</p>
<p>To illustrate this, let us say you had a limit of ten requests per ten minutes, starting at 12:00. So the fixed window is 12:00-12:10, 12:10-12:20, and so on. If you sent ten requests at 12:09 and ten requests at 12:11, all 20 requests would be successful in a fixed window strategy. However, they would fail in a sliding window strategy since there were more than ten requests in the last ten minutes.</p>
<h2 id="handling-rate-limits">Handling rate limits</h2>
<p>When your requests exceed the allowed rate, you will encounter rate limiting. This means the server will respond with a <code>429 Too Many Requests</code> status code and your request will not be processed.</p>
<h2 id="default-configuration">Default configuration</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/2826.md")
</div></div>
<p>This rate limiting behavior will be uniformly applied to all requests for that gateway.</p>
