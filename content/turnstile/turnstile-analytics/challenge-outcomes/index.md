<p>When a visitor encounters Turnstile, it assesses whether they are human or bot-like based on various signals. These outcomes help you evaluate how effectively Turnstile is protecting your application.</p>
<h2 id="metrics">Metrics</h2>
<p>A &quot;solved&quot; Turnstile challenge does not automatically confirm the visitor is human. You must <a href="#call-siteverify">call the Siteverify API</a> to validate the token and proceed only if the response returns <code>success:true</code>.</p>
<p>For example, the challenge outcome values in your analytics may look like this:</p>
<p><img src="/assets/upstream/images/turnstile/challenge-outcomes.png" alt="Challenge outcome example values" title="Challenge outcome example" /></p>
<ul>
<li><strong>Challenges issued</strong>: The total number of challenges presented to visitors within a specific timeframe.</li>
<li><strong>Challenges solved</strong>: The number of challenges successfully completed by visitors in that period.</li>
<li><strong>Challenges unsolved</strong>: Challenges that were abandoned or failed in that period.</li>
<li><strong>Likely human</strong>: The total number of challenges solved or the total number of challenges issued.</li>
<li><strong>Likely bot</strong>: The total number of challenges unsolved or the total number challenges issued.</li>
</ul>
<p>By analyzing these metrics, you can identify trends such as high failure rates in specific regions, device types, or traffic sources, which may indicate bot activity or misconfigurations.</p>
<h3 id="call-siteverify">Call Siteverify</h3>
<p>It is important to <a href="/turnstile/get-started/server-side-validation/">call the Siteverify API</a>. Without calling Siteverify API to validate the tokens, your website or application is not protected. Skipping token validation means you cannot confirm the visitor's legitimacy.</p>
<ul>
<li>Tokens can only be redeemed once. Even valid tokens will return <code>success:false</code> if they are reused, preventing token theft and replay attacks.</li>
<li>Tokens expire after five minutes. Validation must occur within this window to be effective.</li>
<li>Tokens can be invalid. Bots might complete challenges, but Cloudflare can detect bot-like signals and mark the token as invalid.</li>
</ul>
<h2 id="solve-rates">Solve rates</h2>
<p>Turnstile's solve rate indicates how many visitors pass a challenge. Solve rates can be broken down into the total number of challenges solved and whether they are interactive, non-interactive, or pre-clearance solves.</p>
<p>If you are using <a href="/turnstile/concepts/widget/#managed-mode-recommended">managed mode</a>, you can monitor how many of your visitors were prompted to interact with the checkbox on the widget (interactive solves) and how many were verified without any disruptions to their experience (non-interactive solves).</p>
<p>For example, the solve rate values in your analytics may look like this:</p>
<p><img src="/assets/upstream/images/turnstile/solve-rates.png" alt="Solve rate example values" title="Solve rate example" /></p>
<h3 id="metrics-1">Metrics</h3>
<ul>
<li><strong>Non-interactive solves</strong>: Challenges solved without requiring the visitor to click a checkbox.</li>
<li><strong>Interactive solves</strong>: Challenges solved that required visitor interaction to be solved.</li>
<li><a href="/cloudflare-challenges/concepts/clearance/#pre-clearance-support-in-turnstile"><strong>Pre-clearance solves</strong></a>: Challenges solved that issued the <code>cf_clearance</code> cookie along with the Turnstile token.</li>
</ul>
<p>A low solve rate might indicate increased bot activity attempting to bypass Turnstile or anomalous traffic patterns that require further investigation.</p>
