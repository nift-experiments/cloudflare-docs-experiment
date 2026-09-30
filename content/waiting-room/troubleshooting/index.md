<p>Below you will find answers to our most commonly asked questions about the Waiting Room.</p>
<ul>
<li><a href="#configuration">Configuration</a></li>
<li><a href="#features-and-products">Features and products</a></li>
<li><a href="#user-behavior">User behavior</a></li>
<li><a href="#monitor-your-waiting-room">Monitor your waiting room</a></li>
</ul>
<hr />
<h2 id="configuration">Configuration</h2>
<h3 id="can-i-display-my-waiting-room-page-in-another-language">Can I display my waiting room page in another language?</h3>
<p>Yes. For more details, refer to <a href="/waiting-room/how-to/customize-waiting-room/">Customize a waiting room</a>.</p>
<h3 id="why-does-my-waiting-room-look-different-than-how-i-designed-it">Why does my waiting room look different than how I designed it?</h3>
<p>If you have <a href="/waiting-room/how-to/customize-waiting-room">customized your waiting room template</a>:</p>
<ol>
<li>Preview your template before deploying it to production.</li>
<li>If you encounter any issues, check for proper syntax and a closing backslash (/).</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/123.md")
</aside>
<h3 id="what-can-i-update-when-my-waiting-room-is-actively-queueing">What can I update when my waiting room is actively queueing?</h3>
<p>You can update a <a href="/waiting-room/how-to/customize-waiting-room">waiting room's template</a> and those changes will be visible to users in near-real time. We recommend these updates as a way to engage with users and provide updated information or expectations.</p>
<p>You can also update the <a href="/waiting-room/reference/configuration-settings">configuration settings</a> of a waiting room, but only make these changes when necessary. These changes may impact the estimated wait time shown to end users and cause unnecessary confusion.</p>
<h2 id="features-and-products">Features and products</h2>
<h3 id="which-features-are-included-in-my-waiting-room-plan">Which features are included in my Waiting Room plan?</h3>
<p>To check which features are available to different plan types, refer to <a href="/waiting-room/plans/">Plans</a>.</p>
<h3 id="how-does-waiting-room-interact-with-other-cloudflare-products">How does Waiting Room interact with other Cloudflare products?</h3>
<p>Some Cloudflare products run before a waiting room acts on traffic:</p>
<ul>
<li>DDoS Mitigation</li>
<li>Web Application Firewall (WAF)</li>
<li>Bot Management</li>
<li>Page Rules</li>
</ul>
<p>Other Cloudflare products run after a waiting room acts on traffic:</p>
<ul>
<li>Workers</li>
</ul>
<h2 id="user-behavior">User behavior</h2>
<h3 id="what-happens-if-a-user-refreshes-their-tab-when-in-a-waiting-room">What happens if a user refreshes their tab when in a waiting room?</h3>
<p>A manual tab refresh has no effect on a user's position in your waiting room.</p>
<p>However, if they close their tab and then try to access the application again during active queueing, they will lose their spot and have to go to the back of the queue.</p>
<h3 id="what-happens-if-a-queued-user-leaves-the-queue">What happens if a queued user leaves the queue?</h3>
<p>When a user joins the queue, they are placed into a bucket which is their general position in line. When a user leaves the queue (closes the browser or tab), their place in line is held for five minutes after the last refresh. This grace period allows users to keep their position in line if they experience a brief disconnection. After five minutes, the grace period expires and they are no longer counted as waiting in the queue.</p>
<h2 id="monitor-your-waiting-room">Monitor your waiting room</h2>
<h3 id="why-do-i-observe-a-few-users-being-queued-in-the-dashboard">Why do I observe a few users being queued in the dashboard?</h3>
<p>Some users might be queued before your waiting room reaches is limit due to architectural designs. For more details on the behavior and how to fix it, refer to <a href="/waiting-room/how-to/monitor-waiting-room#queueing-activation">​​Queueing activation</a>.</p>
<h3 id="why-are-some-users-not-being-queued-in-my-waiting-room">Why are some users not being queued in my waiting room?</h3>
<p>If you notice users not being queued to your waiting room, make sure the path you defined exactly matches the path of your website.</p>
<p>The path is case-sensitive, so if you have a waiting room set up for <code>/Black-Friday-Sale</code> and users go to <code>/black-friday-sale</code>, they will bypass your waiting room.</p>
<p>For more details, refer to <a href="/waiting-room/reference/best-practices">Best practices</a>.</p>
<h3 id="why-are-users-being-blocked-from-entering-my-waiting-room">Why are users being blocked from entering my waiting room?</h3>
<p>If you have Rate Limiting, check your <a href="/waf/rate-limiting-rules/">rate limiting rules</a>.</p>
<p>The Waiting Room queue page refreshes every 20 seconds by populating the refresh header. If you have a rule set to block requests from a specific IP within 20 seconds, the user in the waiting room will be blocked. Make sure your rules allow at least one request every 20 seconds.</p>
<p>Your user also might not have <a href="/waiting-room/reference/waiting-room-cookie">cookies</a> enabled. If they do not enable cookies and your waiting room is actively queueing traffic, they will not reach your endpoint until the queueing stops.</p>
<h3 id="why-is-the-estimated-wait-time-increasing-for-some-users">Why is the estimated wait time increasing for some users?</h3>
<p>Estimated wait times may increase if the rate of users leaving your site decreases. The estimated wait time is updated upon each page refresh based on the most recently available information about the rate of slots opening up on your site and the number of users ahead of the user in line. To make this increase less likely, you could limit the amount of time users are allowed to spend on your site by disabling session renewal. Be aware that, if you change your traffic settings, estimated wait times will change as well.</p>
<h3 id="why-is-new-users-per-minute-low-when-there-is-capacity-available">Why is <code>new users per minute</code> low when there is capacity available?</h3>
<p>The <code>new users per minute</code> metric tracks how many users were accepted to the origin in the last minute. It is only incremented when a queued user refreshes and is accepted to the origin. If the waiting room queueing method is set to <code>fifo</code>, we will wait until all queued users in a minute-based bucket are accepted before moving to the next bucket. If many of the users in a bucket have abandoned the queue, then the waiting room must wait until their place in line expires before moving on to the next bucket. This can cause <code>new users per minute</code> to be low when only a small percentage of queued users are actually still waiting.</p>
<p>This is often noticed if there is a large amount of automated traffic which does not handle cookies properly. Since bots usually do not persist cookies from one request to the next, they end up counting as multiple inactive users in the queue and prevent full utilization of available slots. For this reason, we recommend leveraging <a href="/bots/">Bots Management</a> products to keep bots out of the queue. Waiting Room Advanced customers can try our <a href="/turnstile/">Turnstile</a> integration, which prevents bots from clogging the line by putting  them in an infinite queue.</p>
<h3 id="why-are-my-waiting-room-analytics-and-google-analytics-not-matching">Why are my Waiting Room analytics and Google analytics not matching?</h3>
<p>Waiting Room relies on a session cookie to count and keep track of active users. The duration for which a user is considered active depends on the waiting room configuration. The key setting involved in this calculation is <a href="/waiting-room/reference/configuration-settings/#session-duration">session duration</a>. By default, Waiting Room considers a user active from the time of their last request made with a session cookie, until the configured session duration elapses. Customers with an advanced Waiting Room setup can modify this behavior by <a href="/waiting-room/how-to/control-user-session/#disable-session-renewal-to-limit-browsing-time">disabling session renewal</a> and/or explicitly <a href="/waiting-room/how-to/control-user-session/#revoke-a-users-session-using-origin-commands">revoking sessions</a> using an origin command.</p>
<p>If the session duration is set to a higher value, a user who makes only a single request will be considered active for longer than they actually were. This can cause the <code>Total Active Users</code> metric to appear higher than the active users metric reported by Google Analytics for the same time period, as Google Analytics only counts users who made requests during that specific period.</p>
<p>For example, if the session duration is set to 30 minutes and you look at the last 10 minutes of active users in Google Analytics, the number of active users reported by Waiting Room will be higher, since it includes users from the last 30 minutes.</p>
<p>Another key difference is that Waiting Room runs on requests made to the origin, while Google Analytics requires a user-agent to run JavaScript (via Google Tag). Waiting Room creates new sessions and tracks user metrics based on the HTTP request path, without requiring any additional JavaScript execution by a user-agent. In contrast, Google Analytics requires user-agents to execute JavaScript and make a secondary request to report details to Google Analytics. If a large portion of the traffic is automated, it may not be captured by Google Analytics. However, Waiting Room analytics will count such traffic as new users and consider them active for the configured session duration.</p>
<h3 id="why-did-my-traffic-exceed-the-new-users-per-minute-threshold">Why did my traffic exceed the New Users Per Minute threshold?</h3>
<p>Waiting Room is a distributed system, and achieving perfect global counting in real time is challenging due to the time required for state propagation across data centers worldwide. The budgeting logic is structured around both data center-specific and global budgets. Data center budgets are allocated based on the historical traffic received by each data center, while global budgets (a portion of the total available budget) are maintained to allow new users to enter from any data center globally.</p>
<p>In the case of a rapid spike — rising to several thousand users within a minute — the global state propagation process takes approximately two minutes, resulting in a delay before all data centers become aware of the spike. If this information is not disseminated quickly enough to other locations, temporary overshooting may occur, particularly when lower limits are in place.</p>
<p>This occurs because the portion of the budget reserved for new users to enter a data center is equally available to all data centers. Until the usage of this budget is synchronized across all data centers, each data center may consume a portion that collectively exceeds 100% of the global budget allocated for new users.</p>
