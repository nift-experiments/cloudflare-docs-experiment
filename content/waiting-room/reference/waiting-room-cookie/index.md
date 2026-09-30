<p>A waiting room only uses the <code>__cfwaitingroom</code> cookie when a visitor requests access to a host and path combination with an enabled and associated waiting room. When the waiting room is suspended, traffic goes to the origin and the <code>__cfwaitingroom</code> cookie is not created. The <code>__cfwaitingroom</code> cookie is encrypted to prevent modification by users. You may append a <a href="#customize-cookie-name">custom suffix</a> to your waiting room cookie to customize the name of your waiting room cookie.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important:</h3>
@markup("md", "content/.markup/bodies/15737.md")
</aside>
<h2 id="cookie-function">Cookie function</h2>
<p>The <code>__cfwaitingroom</code> cookie is used to:</p>
<ul>
<li>Track a user's position in the waiting room queue and serve them in the correct order.</li>
<li>Monitor each visitor's duration in the application to provide an <a href="#estimated-wait-time-fifo-queueing-method">accurate entry time</a> to visitors queueing in the waiting room.</li>
<li>To allow re-entry for a period of time (specified by <a href="/waiting-room/reference/configuration-settings/#session-duration">session_duration</a>) without going back in the waiting room.</li>
</ul>
<h2 id="cookie-expiration-time">Cookie expiration time</h2>
<ul>
<li>While a visitor stays in a waiting room, <code>__cfwaitingroom</code> cookie expiration is always set to five minutes, but renews every 20 seconds automatically as long as the visitor does not close the tab or leaves your application.</li>
<li>When the visitor accesses the application, the <code>__cfwaitingroom</code> cookie expires after an interval (specified by <a href="/waiting-room/reference/configuration-settings/#session-duration">session_duration</a>).</li>
</ul>
<h2 id="customize-cookie-name">Customize cookie name</h2>
<p>You can customize the name of your waiting room cookie by adding a custom suffix to the end of <code>__cfwaitingroom</code>.</p>
<p>To do this via the UI, complete the Custom cookie field in the <a href="/waiting-room/how-to/create-waiting-room/">Create</a> or <a href="/waiting-room/how-to/edit-delete-waiting-room/">Edit</a> workflow. To do this via the API, enter a value for <code>cookie_suffix</code> when creating or editing a waiting room. The cookie suffix is a required field when <a href="/waiting-room/how-to/place-waiting-room/">using additional hostnames</a> and paths for a single waiting room. Ensure your cookie is compliant with any applicable policies.</p>
<h2 id="estimated-wait-time-fifo-queueing-method">Estimated wait time (FIFO queueing method)</h2>
<p>When a visitor first enters the host and path combination for your waiting room, they receive the <code>__cfwaitingroom</code> cookie. That cookie contains a unique group ID, which corresponds to the minute your visitor entered the waiting room. Using this value, we can tell how many visitors are in front of a specific group.</p>
<p>Each cookie also contains a value for <code>acceptedAt</code>, which corresponds to the minute your visitor entered your application. This value lets us know how many visitors per minute are leaving the waiting room to enter your application.</p>
<pre><code class="language-txt">visitorsAhead ÷ activeUsersToWebApplication = estimatedWaitTime&#10;</code></pre>
<p>We combine these pieces of information to calculate estimated wait time for each group of visitors.</p>
<p>For more details about the technical implementation of Cloudflare Waiting Room, refer to the <a href="https://blog.cloudflare.com/building-waiting-room-on-workers-and-durable-objects/">blog post</a>.</p>
