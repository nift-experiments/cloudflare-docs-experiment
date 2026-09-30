<p>The list of notifications available depends on the type of account you have. Refer to <a href="/notifications/notification-available/">Available Notifications</a> to learn more about what each notification does and what do to when receiving one.</p>
<p>You can check the <a href="/notifications/notification-history/">Notification History</a> using the API to view notifications that have been generated for your account.</p>
<h2 id="permissions">Permissions</h2>
<p>To create a notification via the Cloudflare dashboard, you will need to have the Super Administrator or Administrator role.</p>
<p>You can also create a notification if you have the account edit role, which allows you create any type of notification.</p>
<p>An API token needs to have the <a href="https://developers.cloudflare.com/fundamentals/api/reference/permissions/">Notifications Read/Write permission</a> to create a notification,</p>
<p>Some notifications can only be created if you have a Professional, Business or Enterprise account or if you are using a particular Cloudflare product.</p>
<h2 id="configure-notifications">Configure notifications</h2>
<p>This guide will help you create, edit, test, or delete notifications using the Cloudflare dashboard.</p>
<h3 id="create-a-notification">Create a notification</h3>
<p>You can create a notification via the Cloudflare dashboard.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Add**.
3. On the notification you want to create, choose **Select**.
4. Name the notification.
5. Enter an email address to receive the notifications.
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10852.md")
</aside>
<ol start="6">
<li>(Optional) Specify any additional options for the notification, if required. For example, some notifications require that you select one or more domains or services.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
<p>The browser will navigate back to the list of notifications, where the new notification will appear as <strong>Enabled</strong>.</p>
<h3 id="edit-a-notification">Edit a notification</h3>
<p>You can edit existing Notifications via the Cloudflare dashboard.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. On the notification that you want to modify, select **Edit**.
3. Make your changes as needed and select **Save**.
<p>The browser will navigate back to the list of notifications.</p>
<h3 id="disable-or-delete-a-notification">Disable or delete a notification</h3>
<p>You can delete or disable existing Notifications via the Cloudflare dashboard.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. On the notification that you want to disable, select the **Enabled** toggle. To delete it, select **Delete**.
<h3 id="mute-a-notification">Mute a notification</h3>
<p>You can temporarily mute a notification to stop receiving alerts for a set period of time. Muted notifications create a silence that automatically expires after the specified duration.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. On the notification that you want to mute, select **Mute**.
3. Select a duration preset (**1h**, **12h**, or **24h**), or set a custom time range using the **Start Time** and **End Time** fields.
4. Select **Save**.
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10851.md")
</aside>
<h3 id="manage-silences">Manage silences</h3>
<p>You can view, edit, or delete existing silences from the <strong>Silences</strong> tab.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select the **Silences** tab.
3. To create a new silence, select **Add**. To modify an existing silence, select **Edit**. To remove a silence before it expires, select **Delete**.
<h3 id="test-a-notification">Test a notification</h3>
<p>To verify that notifications will be sent to the correct location or to view which details are available, you can test a notification by selecting <strong>Test</strong> on any enabled notification.</p>
<p>This action sends a notification with fake data.</p>
