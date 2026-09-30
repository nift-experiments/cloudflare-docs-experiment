---
cp9:
  canonical: https://developers.cloudflare.com/waiting-room/reference/configuration-settings/
  description: Available configuration settings for waiting rooms.
  full_title: Configuration settings · Cloudflare Waiting Room docs
  head_html: <title>Configuration settings · Cloudflare Waiting Room docs</title><meta name="generator" content="Nift"><meta name="description" content="Available configuration settings for waiting rooms."><link rel="canonical" href="https://developers.cloudflare.com/waiting-room/reference/configuration-settings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waiting-room/reference/configuration-settings/index.md"><meta property="og:title" content="Configuration settings · Cloudflare Waiting Room docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Available configuration settings for waiting rooms."><meta property="og:url" content="https://developers.cloudflare.com/waiting-room/reference/configuration-settings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Waiting Room"><meta name="algolia_product_filter" content="Waiting Room"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Waiting Room"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waiting-room/reference/configuration-settings/#page","headline":"Configuration settings \u00b7 Cloudflare Waiting Room docs","description":"Available configuration settings for waiting rooms.","url":"https://developers.cloudflare.com/waiting-room/reference/configuration-settings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waiting-room/reference/configuration-settings/
  schema: 1
---
<p>You can customize a variety of options for your waiting rooms.</p>
<p><a class="nb-link-button" href="#dashboard-settings">Dashboard settings</a><a class="nb-link-button" href="#additional-details">Additional details</a></p>
<h2 id="dashboard-settings">Dashboard settings</h2>
<table style="width:100%">
<thead>
<tr>
<td colspan="2" style="width:30%">
        <strong>Settings</strong>
</td>
<td colspan="2" style="width:70%">
        <strong>Notes</strong>
</td>
</tr>
<tr>
<td style="width:15%">
        <strong>Dashboard Setting</strong>
</td>
<td style="width:15%">
        <strong>API parameter</strong>
</td>
<td style="width:15%">
        <strong>Required?</strong>
</td>
<td style="width:30%">
        <strong>Description</strong>
</td>
<td style="width:25%">
        <strong>Best practices</strong>
</td>
</tr>
</thead>
<tbody>
<tr>
<td>Name</td>
<td>
        <code>name</code>
</td>
<td>Yes</td>
<td>Unique waiting room name.</td>
<td></td>
</tr>
<tr>
<td>Hostname</td>
<td>
        <code>host</code>
</td>
<td>Yes</td>
<td>Hostname for which the waiting room will be applied (no wildcards).</td>
<td>
        Do not include <code>http://</code> or <code>https://</code>.
</td>
</tr>
<tr>
<td>Path</td>
<td>
        <code>path</code>
</td>
<td>No</td>
<td>
        Case-sensitive path of the waiting room. The waiting room will be enabled for all subpaths.
        Wildcards and query parameters are not supported.
</td>
<td>
        If your server does not allow letter casing, use numbers in your <code>path</code>.
</td>
</tr>
<tr>
<td>Additional Hostnames and Paths</td>
<td>
        <code>additional_routes</code>
</td>
<td>No</td>
<td>
        Add additional hostnames and/or paths to your waiting room coverage.
</td>
<td>
        Additional hostnames must be within the same zone. Hostname and path combinations must be unique per waiting room.
</td>
<td></td>
</tr>
<tr>
<td>Custom Cookie Suffix</td>
<td>
        <code>cookie_suffix</code>
</td>
<td>Required when using <code>additional_routes</code>.</td>
<td>
        Customize the suffix of your waiting room cookie. Suffix will be added to <code>_cfwaitingroom</code>.
</td>
<td>
       Ensure your cookie name is compliant. Do not change this often.
</td>
<td></td>
</tr>
<tr>
<td>Total active users</td>
<td>
        <code>total_active_users</code>
</td>
<td>Yes</td>
<td>
        The maximum number of active sessions allowed in <code>host/path</code> at a given time
        (must be greater than 200).
</td>
<td>
        Set to 75% of origin traffic capacity and adjust as needed. Adjustments may affect estimated
        wait time shown to end users.
</td>
</tr>
<tr>
<td>New users per minute</td>
<td>
        <code>new_users_per_minute</code>
</td>
<td>Yes</td>
<td>
        A <a href="#new-users-per-minute">threshold</a> of users per minute that can be allowed into <code>host/path</code>, greater than 200 and less than or equal to <strong>total active users</strong>.
</td>
<td>Set to 100% of peak traffic to ensure users are only queued when necessary</td>
</tr>
<tr>
<td>Session duration</td>
<td>
        <code>session_duration</code>
</td>
<td>No</td>
<td>
        The amount of time in minutes (between 1 and 30) that a user who left <code>host/path</code> can come <a href="#session-duration">directly back</a> without having to go into the waiting room. Defaults to 5 minutes.
</td>
<td></td>
</tr>
<tr>
<td>Session Revocation</td>
<td>
        <code></code>
</td>
<td>No</td>
<td>
        Revoke a user's session when they perform a specific action by sending a command to the waiting room using an HTTP header on the response from your origin.
</td>
<td>Enable this setting in the dashboard and add the `Cf-Waiting-Room-Command: revoke` HTTP header to the response from your origin.</td>
</tr>
<tr>
<td>Description</td>
<td>
        <code>description</code>
</td>
<td>No</td>
<td>Description of the waiting room.</td>
<td></td>
</tr>
<tr>
<td>Disable session renewal</td>
<td>
        <code>disable_session_renewal</code>
</td>
<td>No</td>
<td>
        Only available to Enterprise customers with purchase. If true, users only have <code>session duration</code> minutes to browse your site. If false, a user's session cookie is renewed on every request.
</td>
<td></td>
</tr>
<tr>
<td>JSON response</td>
<td>
        <code>json_response_enabled</code>
</td>
<td>No, defaults to false.</td>
<td>
        Send JSON body when receiving an <code>Accept: application/json</code> header, commonly used with native mobile applications.
</td>
<td>
        Set to <code>true</code> when using a waiting room for non-browser traffic. Follow <a href="/waiting-room/how-to/json-response/">this documentation</a> for additional steps.
</td>
<td></td>
</tr>
<tr>
<td>Queueing status code</td>
<td>
        <code>queueing_status_code</code>
</td>
<td>No, defaults <code>200</code> (OK).</td>
<td>
        HTTP status code to be returned while a user is queuing.
</td>
<td>
</td>
<td></td>
</tr>
<tr>
<td>Turnstile Widget Mode</td>
<td>
        <code>turnstile_mode</code>
</td>
<td>Yes, defaults <code>invisible</code>.</td>
<td>
        The type of Turnstile widget to use - refer to the [Turnstile documentation](/turnstile/concepts/widget/#widget-modes) for details. Valid values are <code>off</code>, <code>invisible</code>, <code>visible_non_interactive</code>, and <code>visible_managed</code>. Setting this to <code>off</code> will completely disable the Turnstile integration.
</td>
<td>
        Setting this to <code>invisible</code> makes sense for most rooms, unless you would like end users to be aware the challenge is running.
</td>
<td></td>
</tr>
<tr>
<td>Turnstile Fail Action</td>
<td>
        <code>turnstile_action</code>
</td>
<td>Yes, defaults to <code>log</code>.</td>
<td>
        The action to take when an end user fails a Turnstile challenge. Valid values are <code>log</code> and <code>infinite_queue</code>.
</td>
<td>
        Setting this to <code>log</code> makes sense for most rooms, unless you wish to aggressively block bots using an infinite queue.
</td>
<td></td>
</tr>
</tbody>
</table>
<h2 id="additional-details">Additional details</h2>
<h3 id="new-users-per-minute">New users per minute</h3>
<p>When you configure <code>new users per minute</code>, this value <strong>is not</strong> the number of users added per minute.</p>
<p>Instead, it is the threshold of users allowed per minute (less than or equal to the number of <code>total active users</code>). You should set this value at 100% of your expected peak traffic to ensure users are only queued when necessary.</p>
<h3 id="session-duration">Session duration</h3>
<p>Session duration improves user experience in two ways.</p>
<p>First, it prevents visitors from having to pass through a waiting room twice for the same transaction. For example, a visitor might want to make a purchase at <code>example.com</code>. There's a lot of traffic at <code>example.com</code>, so they queue in the waiting room before entering the online store. After a period of time, they leave the waiting room and enter the online store. They make a purchase and leave the online store.</p>
<p>However, they forgot to add a note to the order or request a receipt. As long as their <a href="/waiting-room/reference/waiting-room-cookie/">session cookie</a> is still valid (for the length of time specified by the <code>session duration</code>), they can re-enter your application without having to re-queue in the waiting room.</p>
<p>Second, session duration lets your waiting room create a dynamic outflow from your application (in addition to dynamic inflow). A user's session cookie expires after a period of inactivity, meaning that new spots can open up as soon as space becomes available and estimated wait times are lower and more accurate.</p>
