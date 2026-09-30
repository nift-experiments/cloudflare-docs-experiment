<p>Route Leak Detection protects your routes on the Internet by notifying you when your traffic is routed somewhere it should not go, which could indicate a possible attack. Route Leak Detection also reduces the amount of time needed to mitigate leaks by providing you with timely notifications.</p>
<p>Cloudflare detects route leaks by using several sources of routing data to create a synthesis of how the Internet sees routes to BYOIP users. Cloudflare then watches these views to track any sudden changes that occur on the Internet. If the changes can be correlated to actions Cloudflare has taken, no further action is required. However, if changes have not been made, Cloudflare notifies you to inform you that your routes and users may be at risk.</p>
<h2 id="enable-route-leak-detection">Enable Route Leak Detection</h2>
<details><summary>Route Leak Detection Alert</summary><strong>Who is it for?</strong><p><a href="/byoip/">BYOIP customers</a> who want to receive a notification when their prefixes are advertised in places they should not be.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of BYOIP.</p>
<strong>What should you do if you receive one?</strong><p>Confirm your traffic is healthy. Reach out to your transit providers to ensure you are behaving as expected and ask them to follow up with any providers accepting the unauthorized routes.</p>
</details>
<p>You must be a user who has brought your own IP address to Cloudflare, which includes Magic Transit, Spectrum, and WAF users. Only prefixes advertised by Cloudflare qualify for Route Leak Detection.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add</strong>.</li>
<li>Locate <strong>Route Leak Detection</strong> from the list &gt; <strong>Select</strong>.</li>
<li>Enter a name and description for the notification.</li>
<li>Enter one or more email addresses to receive the notifications.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
