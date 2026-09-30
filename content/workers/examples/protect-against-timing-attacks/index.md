<p class="article-summary">Protect against timing attacks by safely comparing values using `timingSafeEqual`.</p>
<p>If you want to get started quickly, click on the button below.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/protect-against-timing-attacks"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.</p>
<p>The <a href="/workers/runtime-apis/web-crypto/#timingsafeequal"><code>crypto.subtle.timingSafeEqual</code></a> function compares two values using a constant-time algorithm. The time taken is independent of the contents of the values.</p>
<p>When strings are compared using the equality operator (<code>==</code> or <code>===</code>), the comparison will end at the first mismatched character. By using <code>timingSafeEqual</code>, an attacker would not be able to use timing to find where at which point in the two strings there is a difference.</p>
<p>The <code>timingSafeEqual</code> function takes two <code>ArrayBuffer</code> or <code>TypedArray</code> values to compare. These buffers must be of equal length, otherwise an exception is thrown.
Note that this function is not constant time with respect to the length of the parameters and also does not guarantee constant time for the surrounding code.
Handling of secrets should be taken with care to not introduce timing side channels.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16393.md")
</aside>
<p>In order to compare two strings, you must use the <a href="/workers/runtime-apis/encoding/#textencoder"><code>TextEncoder</code></a> API.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16397.md")
</div></div>
