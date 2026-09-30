<p>The <strong>queueing method</strong> determines the order that visitors exit an active waiting room and reach your application.</p>
<p>Only certain customers can use queue methods besides First In First Out (FIFO). For more details, refer to <a href="/waiting-room/plans/">Plans</a> page.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note:</h3>
@markup("md", "content/.markup/bodies/15739.md")
</aside>
<h2 id="first-in-first-out-fifo">First In First Out (FIFO)</h2>
<p>Your waiting room orders visitors according to when they entered the waiting room.</p>
<p><img src="/assets/upstream/images/waiting-room/fifo-queueing-method.png" alt="First In First Out flow showing visitors entering the origin by order of arrival to the waiting room" /></p>
<p>Technically, each user receives a <a href="/waiting-room/reference/waiting-room-cookie/">cookie</a> that contains a timestamp of when their request first hit an actively queueing waiting room. Cloudflare uses that timestamp to order visitors and provide the estimated wait time.</p>
<p>Use this method when you want to reward visitors who get in the queue first and wait longer.</p>
<h2 id="random">Random</h2>
<p>When your application has open spots, your waiting room chooses visitors at random to exit the waiting room and enter your application.</p>
<p><img src="/assets/upstream/images/waiting-room/random-queueing-method.png" alt="Random queueing flow showing visitors randomly exiting the waiting room and entering an origin" /></p>
<p>Use this method when you want to distribute products or services more equitably. Earlier users have a better chance of exiting the waiting room before the estimated wait time because they have more chances to be selected.</p>
<h2 id="passthrough">Passthrough</h2>
<p>Allow all traffic to pass immediately through your waiting room and into your application by setting its <code>queueing_method</code> to <strong>passthrough</strong>.</p>
<p>Use this setup when you only want to use your waiting room for events — where you can update the queueing method — and otherwise avoid queueing during low-traffic hours.</p>
<p>Additionally, you can use this queuing method when you want to gather analytics on your traffic but do not want to queue any users. With passthrough on, all traffic will be sent directly to your origin. However, analytics will be gathered on <code>total active users</code>, <code>new users per minute</code> and <code>time on origin</code>. We recommend this as a useful test to gather insights into your traffic patterns to help determine appropriate threshold settings.</p>
<h2 id="reject">Reject</h2>
<p>Prevent any traffic from reaching your application by setting its <code>queueing_method</code> to <strong>reject</strong>. Users will get a static page.</p>
<p>Use this setup for event-only endpoints or to perform application maintenance.</p>
<h2 id="change-queueing-methods">Change queueing methods</h2>
<p>Though you can change your <a href="/waiting-room/reference/queueing-methods/">queueing method</a>, it may affect users if your waiting room is actively queueing:</p>
<ul>
<li><strong>From FIFO to Random</strong>: Users will no longer be ordered based on their cookie timestamp, which may affect the displayed wait time.</li>
<li><strong>From Random to FIFO</strong>: Users will be ordered based on their cookie timestamp, meaning any new users move to the end of the FIFO queue.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15738.md")
</aside>
