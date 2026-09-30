<hr />
<h2 id="before-you-begin">Before you begin</h2>
<p>Before you start this tutorial, make sure you have:</p>
<ul>
<li>Reviewed the <a href="/waiting-room/about/">About</a> Waiting Room page.).</li>
<li>Reviewed your <a href="/waf/rate-limiting-rules/">rate limiting rules</a> to make sure they allow at least one request every 20 seconds (required for automatic page refreshes).</li>
</ul>
<hr />
<h2 id="step-1-plan-out-your-waiting-room">Step 1 — Plan out your waiting room</h2>
<p>Before you create your waiting room, think about how you want it to appear and operate.</p>
<h3 id="location">Location</h3>
<p>Which page will you cover with a waiting room? You can only have one waiting room per page, so you need to identify the high-traffic areas of your website.</p>
<p>Specify the URL for your page by setting the <code>hostname</code> and <code>path</code> in your <a href="/waiting-room/reference/configuration-settings/">configuration settings</a>.</p>
<p>Advanced Waiting Room customers can also <a href="/waiting-room/how-to/place-waiting-room/">specify multiple hostname and path combinations</a> for the same zone.</p>
<h3 id="access-method">Access method</h3>
<p>You can direct visitors to your high-traffic page:</p>
<ul>
<li>Directly (via URL)</li>
<li>Indirectly (via <a href="/rules/url-forwarding/bulk-redirects/">a redirect</a>)</li>
</ul>
<h3 id="queue-activation">Queue activation</h3>
<p>When you <a href="#step-3--activate-your-waiting-room">activate your waiting room</a>, choose whether:</p>
<ul>
<li><a href="#queue-all-visitors"><strong>All visitors</strong></a> to be queued, in preparation for a product release or other time-based event.</li>
<li>Only <a href="#queue-some-visitors"><strong>some visitors</strong></a> to be queued, as traffic reaches the thresholds defined in <code>Total active users</code> and <code>New users per minute</code>.</li>
</ul>
<h2 id="step-2-create-your-waiting-room">Step 2 — Create your waiting room</h2>
<p>Create your waiting room by:</p>
<ul>
<li>Using the <a href="/waiting-room/how-to/create-waiting-room/">dashboard</a>.</li>
<li>Using the <a href="/waiting-room/how-to/create-waiting-room/">API</a>.</li>
</ul>
<h3 id="appearance-optional">Appearance (optional)</h3>
<p>Some customers can <a href="/waiting-room/how-to/customize-waiting-room/">customize the design</a> of their waiting room by editing the page's HTML and CSS.</p>
<p>If you have this ability, think about how you want the page to appear.</p>
<h3 id="prepare-your-waiting-room-for-mobile-application-traffic">Prepare your waiting room for mobile application traffic</h3>
<p>If you need to manage traffic in a non-browser environment such as a mobile app or web app, use a <a href="/waiting-room/how-to/json-response/">JSON-friendly waiting room</a> that can be consumed via your API endpoints. Note that if you have a mobile app or web app that depends on resources that would be protected by a waiting room, you will need to update those clients to handle Waiting Room appropriately.</p>
<h2 id="step-3-activate-your-waiting-room">Step 3 — Activate your waiting room</h2>
<p>Depending on your <a href="#queue-activation">queue activation</a>, you may deploy your waiting room differently.</p>
<h3 id="queue-some-visitors">Queue some visitors</h3>
<p>To queue visitors only when necessary:</p>
<ol>
<li>Go to <strong>Traffic</strong> &gt; <strong>Waiting Room</strong>.</li>
<li>On a waiting room, set <strong>Enabled</strong> to <strong>On</strong>.</li>
<li>Your waiting room will begin queueing visitors once it approaches the target traffic thresholds defined in <a href="/waiting-room/reference/configuration-settings/"><strong>Total active users</strong></a> and in <a href="/waiting-room/reference/configuration-settings/"><strong>New users per minute</strong></a>.</li>
</ol>
<h3 id="queue-all-visitors">Queue all visitors</h3>
<p>To queue all visitors prior to a time-based offering, set up a pre-queue as part of a <a href="/waiting-room/additional-options/create-events/#create-an-event-from-the-dashboard">waiting room event</a>.</p>
<p>To start queueing all new visitors without a scheduled event:</p>
<ol>
<li>Go to <strong>Traffic</strong> &gt; <strong>Waiting Room</strong>.</li>
<li>On a waiting room:
<ol>
<li>Ensure <strong>Enabled</strong> is set to <strong>On</strong>.</li>
<li>Set <strong>Queue-all</strong> to <strong>On</strong>.</li>
</ol>
</li>
<li>Your waiting room will begin queueing all new visitors and will not allow any new visitors to the path protected by your waiting room. Queue-all will override all other waiting room settings, including event settings.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/136.md")
</aside>
<ol start="4">
<li>To begin allowing visitors to the path protected by your waiting room, set <strong>Queue-all</strong> to <strong>Off</strong>.</li>
</ol>
<h2 id="step-4-next-steps">Step 4 — Next steps</h2>
<p>After you have created and deployed your first waiting room, you might also want to:</p>
<ul>
<li><a href="/waiting-room/additional-options/test-waiting-room/">Test your waiting room</a> before it goes live.</li>
<li><a href="/waiting-room/how-to/monitor-waiting-room/">Monitor your traffic</a> in real time.</li>
<li><a href="/waiting-room/troubleshooting/">Troubleshoot</a> potential issues.</li>
</ul>
