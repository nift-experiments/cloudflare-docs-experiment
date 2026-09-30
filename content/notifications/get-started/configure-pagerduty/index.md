<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10856.md")
</aside>
<p>Cloudflare’s Notification service supports routing notifications to PagerDuty. By sending notifications to PagerDuty you can leverage the same service definitions and escalation paths that you would for other third-party services that you connect to PagerDuty.</p>
<p>When a configuration that you have previously set up triggers a notification for PagerDuty, Cloudflare will send the notification to PagerDuty on your behalf. All of the PagerDuty services configured for the notification will receive the notification. PagerDuty will follow the service’s configuration to handle the notification appropriately. Actions like de-duping and rate limiting depend on the notification type.</p>
<p>To use PagerDuty as a connected service, you must <a href="https://www.pagerduty.com/sign-up/">sign up for a PagerDuty account</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10855.md")
</aside>
<h2 id="connect-pagerduty-to-a-cloudflare-account">Connect PagerDuty to a Cloudflare account</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Go to **Destinations**.
3. In the **Connected notification services** card, select **Connect**.
4. Log in to your [PagerDuty account](https://www.pagerduty.com/) to connect it to your Cloudflare account.
5. Choose the services you want to use and select **Connect**.
6. The browser will navigate back to your Cloudflare dashboard. Select **Continue**.
<p>Your new connected PagerDuty will appear in the <strong>Connected notification services</strong> card.</p>
<h2 id="edit-a-pagerduty-connected-service">Edit a PagerDuty connected service</h2>
<p>To edit which PagerDuty services are connected to your Cloudflare account, you must first disconnect PagerDuty from Cloudflare, make any changes you need in PagerDuty, and then reconnect it.</p>
<p>Disconnecting PagerDuty will disable any notifications being sent to PagerDuty where they are currently configured. If PagerDuty was the only configured destination, disconnecting PagerDuty may result in a notification with no destination.</p>
<p>If other delivery destinations were selected, then those notifications will still be routed as configured.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Go to **Destinations**.
3. In the **Connected notification services** card, select **View** on the PagerDuty service you want to disconnect.
4. Select **Disconnect** > **Confirm**.
5. Log in to your [PagerDuty account](https://www.pagerduty.com/) and make the required changes.
6. [Reconnect PagerDuty to Cloudflare](/notifications/get-started/configure-pagerduty/).
