<p class="article-summary">Verify a signed request using the HMAC and SHA-256 algorithms or return a 403.</p>
<p>If you want to get started quickly, click on the button below.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/signing-requests"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16341.md")
</aside>
<p>You can both verify and generate signed requests from within a Worker using the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Crypto/subtle">Web Crypto APIs</a>.</p>
<p>The following Worker will:</p>
<ul>
<li>
<p>For request URLs beginning with <code>/generate/</code>, replace <code>/generate/</code> with <code>/</code>, sign the resulting path with its timestamp, and return the full, signed URL in the response body.</p>
</li>
<li>
<p>For all other request URLs, verify the signed URL and allow the request through.</p>
</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16346.md")
</div></div>
<h2 id="validate-signed-requests-using-the-waf">Validate signed requests using the WAF</h2>
<p>The provided example code for signing requests is compatible with the <a href="/ruleset-engine/rules-language/functions/#hmac-validation"><code>is_timed_hmac_valid_v0()</code></a> Rules language function. This means that you can verify requests signed by the Worker script using a <a href="/waf/custom-rules/use-cases/configure-token-authentication/#option-2-configure-using-custom-rules">custom rule</a>.</p>
