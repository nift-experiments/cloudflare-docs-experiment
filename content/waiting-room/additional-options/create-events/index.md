---
cp9:
  canonical: https://developers.cloudflare.com/waiting-room/additional-options/create-events/
  description: Create scheduled events with custom waiting room settings.
  full_title: Create scheduled events · Cloudflare Waiting Room docs
  head_html: <title>Create scheduled events · Cloudflare Waiting Room docs</title><meta name="generator" content="Nift"><meta name="description" content="Create scheduled events with custom waiting room settings."><link rel="canonical" href="https://developers.cloudflare.com/waiting-room/additional-options/create-events/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waiting-room/additional-options/create-events/index.md"><meta property="og:title" content="Create scheduled events · Cloudflare Waiting Room docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create scheduled events with custom waiting room settings."><meta property="og:url" content="https://developers.cloudflare.com/waiting-room/additional-options/create-events/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Waiting Room"><meta name="algolia_product_filter" content="Waiting Room"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Waiting Room"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waiting-room/additional-options/create-events/#page","headline":"Create scheduled events \u00b7 Cloudflare Waiting Room docs","description":"Create scheduled events with custom waiting room settings.","url":"https://developers.cloudflare.com/waiting-room/additional-options/create-events/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waiting-room/additional-options/create-events/
  schema: 1
---
<p>When you want to customize the behavior of a waiting room for a specific period of time — such as changing the queueing method or increasing the total active users — set up a <strong>scheduled event</strong>. You can do this from the dashboard or via the API.</p>
<p>Any properties set on the event will override the default property on the waiting room for the duration of the event.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15763.md")
</aside>
<h2 id="create-an-event-from-the-dashboard">Create an event from the dashboard</h2>
<ol>
<li>
<p>Within your application, go to <strong>Traffic</strong> &gt; <strong>Waiting Room</strong>.</p>
</li>
<li>
<p>Expand a waiting room  and select <strong>Schedule event</strong>.</p>
</li>
<li>
<p>Customize the details for your event: name the event, add a description (optional), and select a Start Date Time and an End Date Time.</p>
</li>
<li>
<p>You can also enable the pre-queueing — in this case you need to define a pre-queueing time. And you can also select <strong>Shuffle at event start</strong> and all users in the pre-queue will be randomly admitted at event start.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15762.md")
</aside>
<ol start="5">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>In the <strong>Settings</strong> section, you can define new values for your Total active users, New users per minute, Session duration, Session Renewal, and Queueing Method. For each of these settings you also have the option to always inherit the values defined in your waiting room. With this option, if you change the settings of your base waiting room, the corresponding Event setting will update as well.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15761.md")
</aside>
<ol start="7">
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>In the customization section, you can select Always inherit your waiting room’s template (default) or you can override it with a Custom Event Template. In this case, you need to import your own template. Make sure to preview the result before continuing.</p>
</li>
<li>
<p>Select <strong>Next</strong> and review your Event details and settings.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15760.md")
</aside>
<p>In your waiting room page, in the <strong>Next Event</strong> column you can visualize the date of the next event scheduled. This columns will read <code>N/A</code> in case there is no event scheduled for that waiting room. You can always suspend, edit or delete your event.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15759.md")
</aside>
<h2 id="create-an-event-via-api">Create an event via API</h2>
<p>To create an event, make a <a href="/api/resources/waiting_rooms/subresources/events/methods/create/">POST request</a> including <a href="#parameters">required and optional parameters</a>. Any properties set on the event will override the default property on the waiting room for the duration of the event.</p>
<p>If you are using a <a href="/waiting-room/how-to/customize-waiting-room/#custom-waiting-room">custom template</a>, you may want to add <a href="/api/resources/waiting_rooms/methods/update/">relevant variables</a> to your template (listed under the <code>json_response_enabled</code> parameter).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15758.md")
</aside>
<h3 id="parameters">Parameters</h3>
<p>Though most parameters are identical to those in a regular waiting room, there are a few unique to creating an event. For a complete list of event settings, please refer to <a href="/api/resources/waiting_rooms/subresources/events/methods/create/">Create an Event</a>.</p>
<ul>
<li><code>name</code> (required): Unique name with alphanumeric characters, hyphens, and underscores.</li>
<li><code>event_start_time</code> (required): ISO 8601 timestamp that marks the start of the event. At this time, queued users will be processed with the event's configuration. Must occur at least 1 minute before <code>event_end_time</code>.</li>
<li><code>event_end_time</code> (required): ISO 8601 timestamp that marks the end of the event.</li>
<li><code>shuffle_at_event_start</code>: If <strong>true</strong> and <code>prequeue_start_time</code> is not null, users in the prequeue will be shuffled randomly at the <code>event_start_time</code>. Commonly used to ensure fairness if your event is using a <a href="#set-up-a-lottery"><strong>FIFO</strong> queueing method</a>.</li>
<li><code>prequeue_start_time</code>: ISO 8601 timestamp that marks when to begin queueing all users before the event starts. Must occur at least <strong>5 minutes before</strong> <code>event_start_time</code>.</li>
<li><code>description</code>: A text description providing more detail about the event.</li>
<li><code>suspended</code>: If <strong>true</strong>, the event is ignored and traffic is handled based on the waiting room's typical configuration.</li>
</ul>
<h3 id="queueing-methods">Queueing methods</h3>
<p>When setting up events, you may want to also adjust the default queueing methods for your waiting room.</p>
<p>Set the waiting room's queueing method to <a href="/waiting-room/reference/queueing-methods/#passthrough"><strong>Passthrough</strong></a> when you want to allow traffic normally, but then restrict traffic during a scheduled event.</p>
<p>Set the waiting room's queueing method to <a href="/waiting-room/reference/queueing-methods/#reject"><strong>Reject</strong></a> when you want to block all traffic normally, but then allow traffic during special events like signups or ticket sales.</p>
<h2 id="set-up-a-lottery">Set up a &quot;lottery&quot;</h2>
<p>Set up a &quot;lottery&quot; system to reward all users who enter into the queue prior to your event start time.</p>
<p>Users who reach your application <strong>during the prequeue period</strong> are <a href="/waiting-room/reference/queueing-methods/#random">randomly assigned</a> a place in line when the event starts. If the event uses <a href="/waiting-room/reference/queueing-methods/#first-in-first-out-fifo">FIFO ordering</a>, users who reach your application <strong>after the prequeue period</strong> are assigned places after users from the prequeue.</p>
<p>To set up a &quot;lottery&quot;, include the <a href="#parameters">following parameters</a> in your API request:</p>
<ul>
<li><code>prequeue_start_time</code></li>
<li><code>shuffle_at_event_start</code></li>
</ul>
<h2 id="preview-an-event-configuration">Preview an event configuration</h2>
<p>Since some properties set on an event will override the default property of a waiting room for the duration of an event, you should use the API to <a href="/api/resources/waiting_rooms/subresources/events/subresources/details/methods/get/">preview an event configuration</a> before it begins.</p>
<p>This command shows you the event's configuration as if it were active, meaning that inherited fields from the waiting room will display their current values.</p>
<h2 id="edit-an-event">Edit an event</h2>
<p>To edit an event, use a <a href="/api/resources/waiting_rooms/subresources/events/methods/edit/">PATCH request</a>.</p>
<h2 id="disable-events">Disable events</h2>
<p>You can disable an event by setting its <code>suspended</code> parameter to <code>true</code>.</p>
<p>Additionally, events will not become active if a waiting room itself is <strong>Disabled</strong>.</p>
<h2 id="schedule-a-maintenance-page">Schedule a maintenance page</h2>
<p>Follow these steps if you would like to deploy a scheduled maintenance page, with no queueing before or after the maintenance window.</p>
<ol>
<li><a href="/waiting-room/how-to/create-waiting-room/">Create a waiting room</a> with <a href="/waiting-room/reference/queueing-methods/#passthrough">Passthrough</a> queueing method enabled.</li>
<li>Create a waiting room event for this room with <a href="/waiting-room/reference/queueing-methods/#reject">Reject</a> queueing method enabled.</li>
</ol>
<p>After the scheduled event has ended, users will have access to your site.  You can end the maintenance window before the scheduled event is over by setting the event to disabled.</p>
<h2 id="other-api-commands">Other API commands</h2>
<table>
<thead>
<tr>
<th>Function</th>
<th>Command</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/api/resources/waiting_rooms/subresources/events/methods/get/">Get event details</a></td>
<td><code>GET</code></td>
</tr>
<tr>
<td><a href="/api/resources/waiting_rooms/subresources/events/methods/list/">List scheduled events</a></td>
<td><code>GET</code></td>
</tr>
<tr>
<td><a href="/api/resources/waiting_rooms/subresources/events/methods/delete/">Delete event</a></td>
<td><code>DELETE</code></td>
</tr>
</tbody>
</table>
