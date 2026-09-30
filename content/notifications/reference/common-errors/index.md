<p>Refer to the information below for more details on common notification errors and how to troubleshoot them.</p>
<h2 id="webhook-test-failed-with-status-code-400-400-bad-request">Webhook test failed with status code 400 400 Bad Request</h2>
<p>This error can occur when you try to configure a webhook that is not currently supported, such as setting up a PagerDuty webhook.</p>
<p>PagerDuty needs to be configured under <a href="/notifications/get-started/configure-pagerduty/">connected notification services</a>.</p>
<h2 id="deleted-users-are-still-receiving-notifications">Deleted users are still receiving notifications</h2>
<p>When you remove a user from your account via <strong>Manage Account</strong> &gt; <strong>Members</strong> in the Cloudflare dashboard, their email address is not removed from existing notifications.</p>
<p>You need to remove the email address from the configuration of the notifications by <a href="/notifications/get-started/#edit-a-notification">editing the notification recipient</a>.</p>
