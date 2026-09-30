<p>After a visitor successfully completes a Turnstile challenge, a token is generated and validated via the Siteverify API. Token validation data shows how many tokens your server validated successfully versus how many failed. A high rate of invalid tokens may indicate bot activity, expired tokens, or implementation issues.</p>
<p>For example, the token validation values in your analytics may look like this:</p>
<p><img src="/assets/upstream/images/turnstile/token-validation.png" alt="Token validation example values" title="Token validation example" /></p>
<h2 id="metrics">Metrics</h2>
<ul>
<li><strong>Siteverify requests</strong>: The total number of requests made to the Siteverify API in the given timeframe.</li>
<li><strong>Valid tokens</strong>: The number of Siteverify requests with <code>success:true</code> responses.</li>
<li><strong>Invalid tokens</strong>: The number of Siteverify requests with <code>success:false</code> responses.</li>
</ul>
<h3 id="call-siteverify">Call Siteverify</h3>
<p>It is important to <a href="/turnstile/get-started/server-side-validation/">call the Siteverify API</a>. Without calling Siteverify API to validate the tokens, your website or application is not protected. Skipping token validation means you cannot confirm the visitor's legitimacy.</p>
<ul>
<li>Tokens can only be redeemed once. Even valid tokens will return <code>success:false</code> if they are reused, preventing token theft and replay attacks.</li>
<li>Tokens expire after five minutes. Validation must occur within this window to be effective.</li>
<li>Tokens can be invalid. Bots might complete challenges, but Cloudflare can detect bot-like signals and mark the token as invalid.</li>
</ul>
