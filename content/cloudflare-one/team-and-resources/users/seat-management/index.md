<p>Cloudflare One subscriptions consist of seats that active users in your account consume. Active users are added to Cloudflare One through any <a href="#authentication-events">authentication event</a>.</p>
<p>The amount of seats available in your Cloudflare One account depends on the amount of users you purchase. If you want to increase the number of seats available, you will have to purchase more users. Learn more about adding and removing seats from your account in the <a href="/cloudflare-one/faq/getting-started-faq/#how-do-i-change-my-subscription-plan">Cloudflare One FAQ</a>.</p>
<h2 id="authentication-events">Authentication events</h2>
<p>A user consumes a seat when they perform an authentication event. For Access, this is any Cloudflare Access authentication event, such as a login to the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a> or an application. For Gateway, this is when any devices associated with the user connect to Cloudflare One within the <a href="#enable-seat-expiration">specified period</a>.</p>
<p>If either one of these events occurs, that user's identity is added as an Active user to Cloudflare One and consumes one seat from your plan. The user will occupy and consume a single seat regardless of the number of applications accessed or login events from their user account. Once the total amount of seats in the subscription has been consumed, additional users who attempt to log in are blocked.</p>
<p>A user who authenticates will hold their seat until you <a href="#remove-a-user">remove the user</a> from your account. By default, inactive users will not be <a href="#enable-seat-expiration">automatically removed</a> from your account. You can remove a single user or all users at any time, and those users will immediately stop counting against the seat count defined in your subscription.</p>
<p>If you notice a number of accounts greater than the number of your users, you may need to configure an Access <a href="/cloudflare-one/access-controls/policies/#bypass">bypass policy</a>. Alternatively, you can use Access <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service tokens</a> to allow access to applications without consuming seats.</p>
<h2 id="seat-management-and-device-registrations">Seat management and device registrations</h2>
<p><a href="/cloudflare-one/team-and-resources/users/seat-management/#remove-a-user">Removing a user</a> determines whether that user consumes a billable seat, but does not <a href="/cloudflare-one/team-and-resources/devices/device-registration/#remove-user-access">prevent users from accessing resources</a> behind Cloudflare Access.</p>
<p>Removing a user will delete all device registrations associated with the user. For more information about managing device registrations, refer to <a href="/cloudflare-one/team-and-resources/devices/device-registration/">Device registration</a>.</p>
<h2 id="manage-users">Manage users</h2>
<h3 id="check-number-of-seats-used">Check number of seats used</h3>
<p>To check the number of seats consumed by active users in your organization, log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and go to <strong>Zero Trust</strong>. <strong>Cloudflare One overview</strong> will display the amount of seats consumed and the remaining amount available. For more details on your users, go to <strong>Team &amp; Resources</strong> &gt; <strong>Users</strong>.</p>
<h3 id="revoke-a-user">Revoke a user</h3>
<p>When you revoke a user, this action will terminate active sessions, but will not remove the user's consumption of an active seat.</p>
<p>To revoke a user from your Zero Trust Organization:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Users</strong>.</li>
<li>Select the checkbox next to a user with an <strong>Active</strong> status in the <strong>Seat usage</strong> column.</li>
<li>Select <strong>Action</strong> &gt; <strong>Revoke</strong>.</li>
<li>Select <strong>Revoke sessions</strong>.</li>
</ol>
<p>Revoked users can still log in if your policies allow them. To prevent a user from authenticating, you must remove them from your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/">device enrollment policies</a> or from your Identity Provider (IdP).</p>
<h3 id="remove-a-user">Remove a user</h3>
<p>Removing a user from your Zero Trust Organization will free up the seat the user consumed. The user will still appear in your list of users.</p>
<p>To remove a user from your Zero Trust Organization:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Users</strong>.</li>
<li>Select the checkbox next to a user with an <strong>Active</strong> status in the <strong>Seat usage</strong> column.</li>
<li>Select <strong>Action</strong> &gt; <strong>Remove users</strong>.</li>
<li>Select <strong>Remove</strong>.</li>
</ol>
<p>The user will now show as <strong>Inactive</strong> and will no longer occupy a seat. If a user is removed but authenticates later, they will consume a seat again. To prevent a user from authenticating, you must remove them from your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/">device enrollment policies</a> or from your Identity Provider (IdP).</p>
<p>To automate the removal of users who have not logged in or triggered a device enrollment in a specific amount of time, turn on <a href="/cloudflare-one/team-and-resources/users/seat-management/#enable-seat-expiration">seat expiration</a> or utilize <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM</a> to remove users when they are deactivated in your identity provider.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="user-record-persistence">User record persistence</h3>
@markup("md", "content/.markup/bodies/5953.md")
</aside>
<h3 id="enable-seat-expiration">Enable seat expiration</h3>
<p>Cloudflare One can automatically remove any user who does not log in to an Access application or whose device does not show any Gateway activity for the specified period (between one month and one year). To determine if a user will be removed, Cloudflare looks for any authentication events and checks the <strong>Last seen</strong> value for all of the user's devices. If both of those are outside the expiration window, the user will be removed and will no longer count against your number of seats. This process occurs once daily for an account.</p>
<p>To enable user seat expiration:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Settings</strong> &gt; <strong>Admin controls</strong>.</li>
<li>In <strong>Remove inactive users from seats</strong>, select <strong>Edit</strong>.</li>
<li>Select an inactivity time from the dropdown menu.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>If a user is removed but authenticates later, they will consume a seat again.</p>
<p>For more information about removing a user for Access and Gateway, refer to the <a href="/cloudflare-one/faq/getting-started-faq/#removing-users">FAQ</a>.</p>
