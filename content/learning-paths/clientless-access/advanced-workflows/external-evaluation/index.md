<p>With Cloudflare Access, you can build infinitely customizable policies using External Evaluation rules. External Evaluation rules allow you to call any API during the evaluation of an Access policy and authenticate users based on custom business logic. Example use cases include:</p>
<ul>
<li>Customize policies based on time of day.</li>
<li>Check IP addresses against external threat feeds.</li>
<li>Call industry-specific user registries.</li>
</ul>
<p>The External Evaluation rule requires two values: an API endpoint to call and a key to verify that any request response is coming from a trusted source. After the user authenticates with your identity provider, all information about the user, device and location is passed to your external API. The API returns a pass or fail response to Access which will then either allow or deny access to the user.</p>
<h2 id="set-up-external-evaluation-rule">Set up External Evaluation rule</h2>
<p>For detailed setup instructions, refer to <a href="/cloudflare-one/access-controls/policies/external-evaluation/">External Evaluation rules</a>.</p>
<p>Example code for the API is available in our <a href="https://github.com/cloudflare/workers-access-external-auth-example">open-source repository</a>.</p>
