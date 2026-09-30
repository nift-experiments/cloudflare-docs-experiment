<p>The Challenge solve rate (CSR) is the percentage of issued challenges — Non-Interactive Challenge, Managed Challenge, or Interactive Challenge actions — that were solved.</p>
<p>Every challenge involves two separate events:</p>
<ul>
<li><strong>Challenge trigger</strong>: The original request matches a WAF rule with a challenge action. Cloudflare issues a challenge to the visitor's browser.</li>
<li><strong>Challenge solved</strong>: The visitor's browser completes the challenge and sends back a validated response. This event is logged as challenge Solved.</li>
</ul>
<p>Most automated traffic abandons immediately upon encountering the challenge script and never reaches the second event. This is why the count of unsolved challenges is typically very large — those abandonments count as failures in the formula.</p>
<pre><code class="language-txt">CSR = number of challenges solved / number of challenges issued&#10;</code></pre>
<p>CSR indicates the false positive percentage of a rule. A high CSR means a large share of issued challenges were solved by real visitors, which may indicate the rule is matching too much legitimate traffic. Use CSR to evaluate whether your rule's criteria or action needs adjustment.</p>
<p>You can find the CSR of a rule by going to its corresponding dashboard page:</p>
<p>For <a href="/waf/custom-rules/">custom rules</a> or <a href="/waf/rate-limiting-rules/">rate limiting rules</a>, go to your zone &gt; <strong>Security</strong> &gt; <strong>Security rules</strong>.</p>
<hr />
<h2 id="challenge-actions-in-security-events">Challenge actions in Security Events</h2>
<p>If you find a Challenge Solved action, such as <code>[js]challengeSolved</code> or <code>challengeSolved</code>, in your Security Events that does not match the underlying rule criteria, it is because this action refers to the successful mitigation of a previous request — not a re-match of the original rule.</p>
<p>The parameters of the solved request may no longer match the original rule's expression. For example, if a challenge was issued due to a low bot score, the score for the solved request may have already changed to a non-suspicious value upon successful verification.</p>
<p>The Challenge Solved action is an informative signal that a previously issued challenge was answered, allowing the visitor's traffic to proceed.</p>
<hr />
<h2 id="failed-challenges">Failed Challenges</h2>
<p>You will not find a dedicated metric for failed challenges in Security Analytics because Cloudflare calculates failure indirectly, based on the difference between challenges issued and challenges solved.</p>
<p>The system views any issued challenge that does not result in a successful clearance cookie as a failure. This is why the number of failed challenges may appear exceptionally high: the majority of issued challenges are never completed.</p>
<p>The official calculation for failures is:</p>
<pre><code class="language-txt">Failed Challenges = Total Challenges Issued − Total Challenges Solved&#10;</code></pre>
<p>The large number of unmatched challenges is primarily due to automated traffic (bots or scrapers) that abandon the process immediately upon encountering the initial challenge script.</p>
<p>Key reasons a challenge may be issued but never solved:</p>
<ul>
<li>The visitor gives up on the challenge or navigates away from the page.</li>
<li>The visitor attempts to solve the challenge but cannot provide a valid answer.</li>
<li>The system receives an invalid or malformed answer from the client.</li>
<li>The script environment (often a bot's controlled browser) fails to run the necessary client-side checks.</li>
</ul>
