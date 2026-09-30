<p>Waiting Room Analytics gives you historical insights into the traffic going through your waiting room compared to your waiting room settings. Data is stored for the past 30 days.</p>
<p>Using Waiting Room Analytics, you can:</p>
<ul>
<li>Evaluate peak traffic flow through your waiting room and onto your site.</li>
<li>Determine how long users spent in the waiting room.</li>
<li>Use analytics to help calibrate your waiting room settings.</li>
</ul>
<h2 id="dashboard-analytics">​Dashboard Analytics</h2>
<p>To access your waiting room’s analytics in the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Waiting Room</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Expand the waiting room you would like to review metrics for, to display a preview of your waiting room analytics. The preview gives you insights into peak traffic through your waiting room over the last 24 hours including: Maximum active users, Maximum queued users and Typical time in queue for queued users.</li>
<li>Select <strong>View More</strong> under the Waiting Room Analytics section to get more historical analytics for your waiting room.</li>
<li>The time range for all of the metrics displayed defaults to the last 24 hours. To change the time range, select from the drop down. You can select any time range from the last 30 days that is a minimum of 30 minutes.</li>
</ol>
<h2 id="event-analytics">Event Analytics</h2>
<p>If your waiting room has a completed scheduled event, you can quickly access the event’s analytics by expanding the row for the waiting room you are interested in and selecting the event time. The link opens the analytics view for that waiting room, including information from the pre-queueing period to the end of the event.</p>
<p>To save this event information, you can either select <strong>Download data</strong> or <strong>Print report</strong>. If you delete the event, the time period link will no longer appear in your dashboard. If you edit the timing of the event, the time period link will update as well.</p>
<p>If you do not get a link to your event’s analytics, one of the following may have happened:</p>
<ul>
<li>Your event has not happened yet.</li>
<li>Your event started more than 30 days ago.</li>
</ul>
<h2 id="metrics">Metrics</h2>
<p>These are metrics available in the Analytics dashboard and how they are calculated.</p>
<h3 id="time-in-queue">Time in queue</h3>
<p>Time in queue summary values give you an insight into the user experience by indicating how long queued users spent waiting to enter your application. It displays the time waited for the typical user, as well as for those who waited the longest, for the time period you have selected. These values are an indicator of the impact your waiting room settings combined with the traffic to your waiting room had on wait times.</p>
<p>If wait times are higher than you would like, and you feel comfortable doing so, you could consider taking any or all of the following actions:</p>
<ul>
<li>Increase <code>total_active_users</code> configured value.</li>
<li>Increase <code>new_users_per_minute</code> configured value.</li>
<li>Decrease <code>session_duration</code>.</li>
<li>Disable session renewal.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/119.md")
</aside>
<h3 id="time-on-origin">Time on origin</h3>
<p>Time on origin summary values estimate how long users spent on the pages covered by your waiting room before leaving. For the time period selected, you will have access to the estimated time spent on origin for the typical user, as well as the time on origin for those who spend the most time on your site. Keep in mind that if your session renewal is disabled and there is no active queueing, users are issued a new waiting room session every <code>session_duration</code> minutes.  Therefore, these users may be staying for multiple sessions.  The time on origin for these users restarts each time a session expires.</p>
<p>The following are some takeaways you could have depending on the time on origin values.</p>
<p>You may want to increase session duration, giving users more time to make subrequests, and/or enable session renewal if:</p>
<ul>
<li>You have session renewal disabled.</li>
<li>You have frequent, active queueing with long wait times.</li>
<li>The typical time on origin is around 70% of your configured session duration.</li>
</ul>
<p>These may be indicators that users need more time to complete their desired tasks on your site.</p>
<p>You may want to decrease session duration and/or disable session renewal if:</p>
<ul>
<li>Your top 5% time on origin is less than 70% of your configured session duration.</li>
<li>You are seeing high queue times and do not want to increase traffic limits.</li>
</ul>
<p>These may be indicators that users do not need as much time on your site and are taking up spots on your origin.</p>
<h3 id="active-users-vs-queued-users">Active users vs. queued users</h3>
<p>The Active users chart is a time series chart that displays the maximum active users on any URLs covered by your waiting room as well as maximum queued users. These values are shown compared to your configured active user target threshold.</p>
<p>A new user is a novel request made to any URLs covered by the waiting room. Waiting Room counts the request as new if no waiting room cookie is tied to the request. Once the request is made, a waiting room cookie is issued. If there is an active queue, the user will be considered a queued user. Once that user makes it through the queue and onto the site, they are now an active user and remain active as long as they keep making HTTP requests to waiting room URLs at least once every <code>session_duration</code> minutes.</p>
<p>To identify and hone in on peak traffic, select a longer time period, such as 30 days. Then, drag your cursor to the left and right of any time period you would like to check with more granularity to zoom in. You can zoom in until each bar represents a one minute interval. All other metrics on the page will update automatically to reflect the data behind the time period selected.</p>
<p>To check for more details about a particular moment in time, hover over a bar on the graph. This displays a tooltip which will indicate the following for the time period that bar represents:</p>
<ul>
<li>Maximum active users reached</li>
<li>Maximum queued users reached</li>
<li>Configured active user target values</li>
</ul>
<p>Queueing may occur below your configured limits, and active users may sometimes exceed your configured limits. Refer to the <a href="/waiting-room/how-to/monitor-waiting-room/#queueing-activation">Queuing activation</a> section for more information.</p>
<h3 id="new-users-per-minute">New users per minute</h3>
<p>The New users per minute chart shows how many new users per minute passed through the waiting room to your origin compared to your configured New users per minute target threshold. Like the Active users chart, you can zoom in by highlighting to the left and right of the time period you are interested in, which will update the other chart as well as summary values. As you zoom out, each data point is averaged. Therefore, as you zoom in, values may fluctuate.</p>
<h3 id="turnstile-widget-traffic">Turnstile Widget Traffic</h3>
<p>The Turnstile widget traffic chart shows the number of challenges issued per minute and the distribution of traffic seen with these challenges. Traffic is categorized into three main categories:</p>
<ul>
<li>Likely Human - This represents the number of challenges that were successfully solved.</li>
<li>Likely Bots - This represents the number of unsolved challenges.</li>
<li>Bots - This represents the number of failed challenges.</li>
</ul>
<p>If your waiting room has the infinite queue option enabled, you will see a line on the graph representing the number of refresh requests from bots in the infinite queue.</p>
<h2 id="graphql-analytics">​​GraphQL Analytics</h2>
<p>You can query your Waiting Room analytics data via GraphQL API. Waiting Room analytics provides near real-time visibility into your Waiting Room, allowing you to visualize the traffic to your application and how it is managed respecting the configured limits.</p>
<p>Here are some query examples to get started:</p>
<details class="nb-details"><summary>Fetch values for total active users and new users per minute over a certain period.</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/120.md")
</div></details>
<details class="nb-details"><summary>Find the average of total active users and new users per minute over a certain period, and aggregate this data over a period of 15 minutes.</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/121.md")
</div></details>
<details class="nb-details"><summary>Find the weighted averages of time on origin (50th percentile) and total time waited (90th percentile) for a certain period and aggregate this data over one hour.</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/122.md")
</div></details>
<h2 id="why-is-there-no-data-for-my-waiting-room">Why is there no data for my waiting room?</h2>
<p>If you are not seeing any historical data for your waiting room, one or more of the following may be true:</p>
<ul>
<li>Your waiting room was not receiving any traffic for the time period you are inspecting.</li>
<li>Your waiting room was not enabled for the time period you are inspecting.</li>
</ul>
