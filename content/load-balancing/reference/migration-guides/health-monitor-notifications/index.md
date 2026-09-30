<p>Cloudflare is migrating the notifications used by load balancing <a href="/load-balancing/monitors/">health monitors</a> to use Cloudflare's centralized <a href="/notifications/">Notifications Service</a>.</p>
<h2 id="what-is-changing-and-why">What is changing and why?</h2>
<p>Cloudflare’s account-level <a href="/notifications/">Notifications Service</a> is now the centralized location for most Cloudflare services. This change promotes consistency and streamlined administration, as well as gives you more options for notification delivery such as configuring webhooks or associating multiple pools with the same notification. These new notifications will also be managed at the account level instead of the zone level.</p>
<p>We strongly encourage all customers to migrate existing Health Monitor notifications to Cloudflare’s centralized Notifications Service to avoid lapses in alerts.</p>
<h2 id="migration-guide">Migration guide</h2>
<p>You should use this guide to migrate over <strong>all</strong> your existing health monitor notifications.</p>
<h3 id="step-1-find-existing-notifications">Step 1 - Find existing notifications</h3>
<p>First you should determine which pools are using notifications. It's often easier if you use the Cloudflare API to list all your pools and look for the <code>notification_email</code> parameter.</p>
<details class="nb-details"><summary>With code</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10441.md")
</div></details>
<details class="nb-details"><summary>No code</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10442.md")
</div></details>
<h3 id="step-2-create-new-notifications">Step 2 - Create new notifications</h3>
<p>In this step, you should create new notifications to replace all of your existing legacy notifications.</p>
<details class="nb-details"><summary>With code</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10443.md")
</div></details>
<details class="nb-details"><summary>No code</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10444.md")
</div></details>
<h3 id="step-3-remove-deprecated-notifications">Step 3 - Remove deprecated notifications</h3>
<p>As the final step in the migration process, you need to remove all emails from your legacy notifications to ensure that you no longer receive deprecation emails moving forward.</p>
<p>Though you can perform these steps in the dashboard, Cloudflare recommends you use our new API endpoint for added convenience.</p>
<details class="nb-details"><summary>With code</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10445.md")
</div></details>
<p>If needed, you can remove legacy notifications by using the dashboard.</p>
<details class="nb-details"><summary>No code</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10446.md")
</div></details>
<p>If you do not complete this step (removing all notification emails from all pools), your migration will not be considered complete and you will continue to receive additional emails about this deprecation.</p>
