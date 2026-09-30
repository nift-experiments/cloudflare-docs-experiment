<h1 id="changelog">Changelog</h1>

<h2 id="increased-http-header-size-limit-to-128-kb"><a href="/changelog/post/2025-10-16-header-limit-increase/">Increased HTTP header size limit to 128 KB</a></h2>
<p><em>2025-10-16</em></p>
<h4 id="2025-10-16-header-limit-increase-cdn-now-supports-128-kb-request-and-response-headers">CDN now supports 128 KB request and response headers 🚀</h4>
<p>We're excited to announce a significant increase in the maximum header size supported by Cloudflare's Content Delivery Network (CDN). Cloudflare now supports up to <strong>128 KB</strong> for both <strong>request and response headers</strong>.</p>
<p>Previously, customers were limited to a total of 32 KB for request or response headers, with a maximum of 16 KB per individual header. Larger headers could cause requests to fail with <code>HTTP 413</code> (Request Header Fields Too Large) errors.</p>
<hr />
<h4 id="2025-10-16-header-limit-increase-what-s-new">What's new?</h4>
<ul>
<li><strong>Support for large headers:</strong> You can now utilize much larger headers, whether as a single large header up to 128 KB or split over multiple headers.</li>
<li><strong>Reduces <code>413</code> and <code>520</code> HTTP errors:</strong> This change drastically reduces the likelihood of customers encountering <code>HTTP 413</code> errors from large request headers or <code>HTTP 520</code> errors caused by oversized response headers, improving the overall reliability of your web applications.</li>
<li><strong>Enhanced functionality:</strong> This is especially beneficial for applications that rely on:
<ul>
<li>A large number of cookies.</li>
<li>Large Content-Security-Policy (CSP) response headers.</li>
<li>Advanced use cases with Cloudflare Workers that generate large response headers.</li>
</ul>
</li>
</ul>
<p>This enhancement improves compatibility with Cloudflare's CDN, enabling more use cases that previously failed due to header size limits.</p>
<hr />
<p>To learn more and get started, refer to the <a href="/fundamentals/reference/connection-limits/#request-limits">Cloudflare Fundamentals documentation</a>.</p>


<h2 id="single-sign-on-now-manageable-in-the-user-experience"><a href="/changelog/post/2025-10-14-sso-self-service-ux/">Single sign-on now manageable in the user experience</a></h2>
<p><em>2025-10-14</em></p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-14-sso-configuration-ux.png" alt="Screenshot of new user experience for managing SSO" /></p>
<p>During Birthday Week, we announced that <a href="https://blog.cloudflare.com/enterprise-grade-features-for-all/">single sign-on (SSO) is available for free</a> to everyone who signs in with a custom email domain and maintains a compatible <a href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/">identity provider</a>. SSO minimizes user friction around login and provides the strongest security posture available. At the time, this could only be configured using the API.</p>
<p>Today, we are launching a new user experience which allows users to manage their SSO configuration from within the Cloudflare dashboard. You can access this by going to <strong>Manage account</strong> &gt; <strong>Members</strong> &gt; <strong>Settings</strong>.</p>
<h4 id="2025-10-14-sso-self-service-ux-for-more-information">For more information</h4>
<ul>
<li><a href="/fundamentals/manage-members/dashboard-sso/">Cloudflare dashboard SSO</a></li>
</ul>


<h2 id="automated-reminders-for-backup-codes"><a href="/changelog/post/2025-10-07-recovery-codes/">Automated reminders for backup codes</a></h2>
<p><em>2025-10-07</em></p>
<p>The most common reason users contact Cloudflare support is lost two-factor authentication (2FA) credentials. Cloudflare supports both app-based and hardware keys for 2FA, but you could lose access to your account if you lose these. Over the past few weeks, we have been rolling out email and in-product reminders that remind you to also download backup codes (sometimes called recovery keys) that can get you back into your account in the event you lose your 2FA credentials. Download your backup codes now by logging into Cloudflare, then navigating to <strong>Profile</strong> &gt; <strong>Security &amp; Authentication</strong> &gt; <strong>Backup codes</strong>.</p>
<h4 id="2025-10-07-recovery-codes-sign-in-security-best-practices">Sign-in security best practices</h4>
<p>Cloudflare is critical infrastructure, and you should protect it as such. Please review the following best practices and make sure you are doing your part to secure your account.</p>
<ul>
<li>Use a unique password for every website, including Cloudflare, and store it in a password manager like 1Password or Keeper. These services are cross-platform and simplify the process of managing secure passwords.</li>
<li>Use 2FA to make it harder for an attacker to get into your account in the event your password is leaked</li>
<li>Store your backup codes securely. A password manager is the best place since it keeps the backup codes encrypted, but you can also print them and put them somewhere safe in your home.</li>
<li>If you use an app to manage your 2FA keys, enable cloud backup, so that you don't lose your keys in the event you lose your phone.</li>
<li>If you use a custom email domain to sign in, <a href="https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/">configure SSO</a>.</li>
<li>If you use a public email domain like Gmail or Hotmail, you can also use social login with Apple, GitHub, or Google to sign in.</li>
<li>If you manage a Cloudflare account for work:
<ul>
<li>Have at least two administrators in case one of them unexpectedly leaves your company</li>
<li>Use SCIM to automate permissions management for members in your Cloudflare account</li>
</ul>
</li>
</ul>


<h2 id="fine-grained-permissioning-for-access-for-apps-idps-targets-now-in-public-beta"><a href="/changelog/post/2025-10-01-fine-grained-permissioning-beta/">Fine-grained Permissioning for Access for Apps, IdPs, & Targets now in Public Beta</a></h2>
<p><em>2025-10-02</em></p>
<p>Fine-grained permissions for <strong>Access Applications, Identity Providers (IdPs), and Targets</strong> is now available in Public Beta. This expands our RBAC model beyond account &amp; zone-scoped roles, enabling administrators to grant permissions scoped to individual resources.</p>
<h4 id="2025-10-01-fine-grained-permissioning-beta-what-s-new">What's New</h4>
- **[Access Applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/)**: Grant admin permissions to specific Access Applications.
- **[Identity Providers](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/)**: Grant admin permissions to individual Identity Providers.
- **[Targets](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#1-add-a-target)**: Grant admin rights to specific Targets
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-01-fine-grained-permissioning-ux.png" alt="Updated Permissions Policy UX" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17728.md")</aside>
<p>For more info:</p>
<ul>
<li><a href="/fundamentals/manage-members/roles/">Get started with Cloudflare Permissioning</a></li>
<li><a href="/fundamentals/manage-members/manage">Manage Member Permissioning via the UI &amp; API</a></li>
</ul>


<h2 id="return-markdown"><a href="/changelog/post/2025-10-01-md-returned/">Return markdown</a></h2>
<p><em>2025-10-01</em></p>
<p>Users can now specify that they want to retrieve Cloudflare documentation as markdown rather than the previous HTML default. This can significantly reduce token consumption when used alongside Large Language Model (LLM) tools.</p>
<pre><code class="language-sh">curl https://developers.cloudflare.com/workers/ -H &#x27;Accept: text/markdown&#x27;  -v&#10;</code></pre>
<p>If you maintain your own site and want to adopt this practice using Cloudflare Workers for your own users you can follow the example <a href="https://github.com/cloudflare/cloudflare-docs/pull/25493">here</a>.</p>


<h2 id="sign-in-with-github"><a href="/changelog/post/2025-09-25-sign-in-with-github/">Sign in with GitHub</a></h2>
<p><em>2025-09-25</em></p>
<p>Cloudflare has launched sign in with GitHub as a log in option. This feature is available to all users with a verified email address who are not using SSO. To use it, simply click on the <code>Sign in with GitHub</code> button on the dashboard login page. You will be logged in with your primary GitHub email address.</p>
<h4 id="2025-09-25-sign-in-with-github-for-more-information">For more information</h4>
- [Log in to Cloudflare](/fundamentals/user-profiles/login/)


<h2 id="sso-for-all"><a href="/changelog/post/2025-09-25-sso-for-all/">SSO for all</a></h2>
<p><em>2025-09-25</em></p>
<p>Single sign-on (SSO) streamlines the process of logging into Cloudflare for Enterprise customers who manage a custom email domain and manage their own identity provider. Instead of managing a password and two-factor authentication credentials directly for Cloudflare, SSO lets you reuse your existing login infrastructure to seamlessly log in. SSO also provides additional security opportunities such as device health checks which are not available natively within Cloudflare.</p>
<p>Historically, SSO was only available for Enterprise accounts. Today, we are announcing that we are making SSO available to all users for free. We have also added the ability to directly manage SSO configurations using the API. This removes the previous requirement to contact support to configure SSO.</p>
<h4 id="2025-09-25-sso-for-all-for-more-information">For more information</h4>
<ul>
<li><a href="https://blog.cloudflare.com/enterprise-grade-features-for-all/">Every Cloudflare feature, available to all</a></li>
<li><a href="/fundamentals/manage-members/dashboard-sso/">Configure Dashboard SSO</a></li>
</ul>


<h2 id="reminders-about-two-factor-authentication-backup-codes"><a href="/changelog/post/2025-09-08-reminders-about-two-factor-authentication-backup-codes/">Reminders about two-factor authentication backup codes</a></h2>
<p><em>2025-09-08</em></p>
<p>Two-factor authentication is the best way to help protect your account from account takeovers, but if you lose your second factor, you could be locked out of your account. Lock outs are one of the top reasons customers contact Cloudflare support, and our policies often don't allow us to bypass two-factor authentication for customers that are locked out. Today we are releasing an improvement where Cloudflare will periodically remind you to securely save your backup codes so you don't get locked out in the future.</p>
<h4 id="2025-09-08-reminders-about-two-factor-authentication-backup-codes-for-more-information">For more information</h4>
- [Two-factor authentication](/fundamentals/user-profiles/2fa/)


<h2 id="introducing-new-headers-for-rate-limiting-on-cloudflare-s-api"><a href="/changelog/post/2025-09-03-rate-limiting-improvement/">Introducing new headers for rate limiting on Cloudflare's API</a></h2>
<p><em>2025-09-03</em></p>
<p>Cloudflare's API now supports rate limiting headers using the pattern developed by the <a href="https://ietf-wg-httpapi.github.io/ratelimit-headers/draft-ietf-httpapi-ratelimit-headers.html">IETF draft on rate limiting</a>. This allows API consumers to know how many more calls are left until the rate limit is reached, as well as how long you will need to wait until more capacity is available.</p>
<p>Our SDKs automatically work with these new headers, backing off when rate limits are approached. There is no action required for users of the latest Cloudflare SDKs to take advantage of this.</p>
<p>As always, if you need any help with rate limits, please contact Support.</p>
<h4 id="2025-09-03-rate-limiting-improvement-changes">Changes</h4>
<h4 id="2025-09-03-rate-limiting-improvement-new-headers">New Headers</h4>
<p><strong>Headers that are always returned:</strong></p>
<ul>
<li><code>Ratelimit</code>: List of service limit items, composed of the limit name, the remaining quota (<code>r</code>) and the time next window resets (<code>t</code>). For example: <code>&quot;default&quot;;r=50;t=30</code></li>
<li><code>Ratelimit-Policy</code>: List of quota policy items, composed of the policy name, the total quota (<code>q</code>) and the time window the quota applies to (<code>w</code>). For example: <code>&quot;burst&quot;;q=100;w=60</code></li>
</ul>
<p><strong>Returned only when a rate limit has been reached (error code: 429):</strong></p>
<ul>
<li>Retry-After: Number of Seconds until more capacity is available, rounded up</li>
</ul>
<h4 id="2025-09-03-rate-limiting-improvement-sdk-back-offs">SDK Back offs</h4>
- All of Cloudflare's latest SDKs will automatically respond to the headers, instituting a backoff when limits are approached. 
<h4 id="2025-09-03-rate-limiting-improvement-graphql-and-edge-apis">GraphQL and Edge APIs</h4>
These new headers and back offs are only available for Cloudflare REST APIs, and will not affect GraphQL. 
<h4 id="2025-09-03-rate-limiting-improvement-for-more-information">For more information</h4>
* [Rate limits at Cloudflare](https://developers.cloudflare.com/fundamentals/api/reference/limits/)


<h2 id="terraform-v5-9-now-available"><a href="/changelog/post/2025-08-29-terrform-v5.9-provider/">Terraform v5.9 now available</a></h2>
<p><em>2025-08-29</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a 2 week cadence to ensure its stability and reliability, including the v5.9 release. We have also pivoted from an issue-to-issue approach to a resource-per-resource approach - we will be focusing on specific resources for every release, stabilizing the release, and closing all associated bugs with that resource before moving onto resolving migration issues.</p>
<p>Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.</p>
<p>This release includes a new resource, <code>cloudflare_snippet</code>, which replaces <code>cloudflare_snippets</code>. <code>cloudflare_snippet</code> is now considered deprecated but can still be used. Please utilize <code>cloudflare_snippet</code> as soon as possible.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-changes">Changes</h4>
- Resources stabilized:
  - `cloudflare_zone_setting`
  - `cloudflare_worker_script`
  - `cloudflare_worker_route`
  - `tiered_cache`
- **NEW** resource `cloudflare_snippet` which should be used in place of `cloudflare_snippets`. `cloudflare_snippets` is now deprecated. This enables the management of Cloudflare's snippet functionality through Terraform.
- DNS Record Improvements: Enhanced handling of DNS record drift detection
- Load Balancer Fixes: Resolved `created_on` field inconsistencies and improved pool configuration handling
- Bot Management: Enhanced auto-update model state consistency and fight mode configurations
- Other bug fixes
<p>For a more detailed look at all of the changes, refer to the
<a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.9.0">changelog</a> in GitHub.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-issues-closed">Issues Closed</h4>
- [#5921: In cloudflare_ruleset removing an existing rule causes recreation of later rules](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5921)
- [#5904: cloudflare_zero_trust_access_application is not idempotent](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5904)
- [#5898: (cloudflare_workers_script) Durable Object migrations not applied](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5898)
- [#5892: cloudflare_workers_script secret_text environment variable gets replaced on every deploy](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5892)
- [#5891: cloudflare_zone suddenly started showing drift](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5891)
- [#5882: cloudflare_zero_trust_list always marked for change due to read only attributes](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5882)
- [#5879: cloudflare_zero_trust_gateway_certificate unable to manage resource (cant mark as active/inactive)](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5879)
- [#5858: cloudflare_dns_records is always updated in-place](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5858)
- [#5839: Recurring change on cloudflare_zero_trust_gateway_policy after upgrade to V5 provider & also setting expiration fails](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5839)
- [#5811: Reusable policies are imported as inline type for cloudflare_zero_trust_access_application](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5811)
- [#5795: cloudflare_zone_setting inconsistent value of "editable" upon apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5795)
- [#5789: Pagination issue fetching all policies in "cloudflare_zero_trust_access_policies" data source](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5789)
- [#5770: cloudflare_zero_trust_access_application type warp diff on every apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5770)
- [#5765: V5 / cloudflare_zone_dnssec fails with HTTP/400 "Malformed request body"](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5765)
- [#5755: Unable to manage Cloudflare managed WAF rules via Terraform](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5755)
- [#5738: v4 to v5 upgrade failing Error: no schema available AND Unable to Read Previously Saved State for UpgradeResourceState](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5738)
- [#5727: cloudflare_ruleset http_request_cache_settings bypass mismatch between dashboard and terraform](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5727)
- [#5700: cloudflare_account_member invalid type 'string' for field 'roles'](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5700)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new issue if one does not already exist for what you are experiencing.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-upgrading">Upgrading</h4>
<p>We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized.</p>
<p>If you'd like more information on migrating from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition. These do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test
your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
<li><a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub Repository</a></li>
</ul>


<h2 id="terraform-v5-8-4-now-available"><a href="/changelog/post/2025-08-15-terraform-v5.8.4-provider/">Terraform v5.8.4 now available</a></h2>
<p><em>2025-08-15</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare Community related to the v5 release. We have committed to releasing improvements on a two week cadence to ensure stability and reliability.</p>
<p>One key change we adopted in recent weeks is a pivot to more comprehensive, test-driven development. We are still evaluating individual issues, but are also investing in much deeper testing to drive our stabilization efforts. We will subsequently be investing in comprehensive migration scripts. As a result, you will see several of the highest traffic APIs have been stabilized in the most recent release, and are supported by comprehensive acceptance tests.</p>
<p>Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.</p>
<h4 id="2025-08-15-terraform-v5.8.4-provider-changes">Changes</h4>
- Resources stabilized:
  - `cloudflare_argo_smart_routing`
  - `cloudflare_bot_management`
  - `cloudflare_list`
  - `cloudflare_list_item`
  - `cloudflare_load_balancer`
  - `cloudflare_load_balancer_monitor`
  - `cloudflare_load_balancer_pool`
  - `cloudflare_spectrum_application`
  - `cloudflare_managed_transforms`
  - `cloudflare_url_normalization_settings`
  - `cloudflare_snippet`
  - `cloudflare_snippet_rules`
  - `cloudflare_zero_trust_access_application`
  - `cloudflare_zero_trust_access_group`
  - `cloudflare_zero_trust_access_identity_provider`
  - `cloudflare_zero_trust_access_mtls_certificate`
  - `cloudflare_zero_trust_access_mtls_hostname_settings`
  - `cloudflare_zero_trust_access_policy`
  - `cloudflare_zone`
- Multipart handling restored for `cloudflare_snippet`
- `cloudflare_bot_management` diff issues resolves when running `terraform plan` and `terraform apply`
- Other bug fixes
<p>For a more detailed look at all of the changes, refer to the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.8.4">changelog</a> in GitHub.</p>
<h4 id="2025-08-15-terraform-v5.8.4-provider-issues-closed">Issues Closed</h4>
- [#5017: 'Uncaught Error: No such module' using cloudflare_snippets](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5017)
- [#5701: cloudflare_workers_script migrations for Durable Objects not recorded in tfstate; cannot be upgraded between versions](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5701)
- [#5640: cloudflare_argo_smart_routing importing doesn't read the actual value](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5640)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already exist for what you are experiencing.</p>
<h4 id="2025-08-15-terraform-v5.8.4-provider-upgrading">Upgrading</h4>
<p>We suggest holding off on migration to v5 while we work on stabilization. This will help you avoid any blocking issues while the Terraform resources are actively being stabilized.</p>
<p>If you'd like more information on migrating to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition. These migration scripts do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-08-15-terraform-v5.8.4-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="terraform-v5-8-2-now-available"><a href="/changelog/post/2025-08-01-terraform-v5.8.2-provider/">Terraform v5.8.2 now available</a></h2>
<p><em>2025-08-01</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a 2 week cadeance to ensure it's stability and reliability. We have also pivoted from an issue-to-issue approach to a resource-per-resource approach - we will be focusing on specific resources for every release, stabilizing the release and closing all associated bugs with that resource before moving onto resolving migration issues.</p>
<p>Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.</p>
<h4 id="2025-08-01-terraform-v5.8.2-provider-changes">Changes</h4>
- Resources stabilized:
  - `cloudflare_custom_pages`
  - `cloudflare_page_rule`
  - `cloudflare_dns_record`
  - `cloudflare_argo_tiered_caching`
- Addressed chronic drift issues in `cloudflare_logpush_job`, `cloudflare_zero_trust_dns_location`, `cloudflare_ruleset` & `cloudflare_api_token`
- `cloudflare_zone_subscription` returns expected values `rate_plan.id` from former versions
- `cloudflare_workers_script` can now successfully be destroyed with bindings & migration for Durable Objects now recorded in tfstate 
- Ability to configure `add_headers` under `cloudflare_zero_trust_gateway_policy` 
- Other bug fixes
<p>For a more detailed look at all of the changes, see the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.8.2">changelog</a> in GitHub.</p>
<h4 id="2025-08-01-terraform-v5.8.2-provider-issues-closed">Issues Closed</h4>
- [#5666: cloudflare_ruleset example lists id which is a read-only field](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5666)
- [#5578: cloudflare_logpush_job plan always suggests changes](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5578)
- [#5552: 5.4.0: Since provider update, existing cloudflare_list_item would be recreated "created" state](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5552)
- [#5670: cloudflare_zone_subscription: uses wrong ID field in Read/Update](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5670)
- [#5548: cloudflare_api_token resource always shows changes (drift)](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5548)
- [#5634: cloudflare_workers_script with bindings fails to be destroyed](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5634)
- [#5616: cloudflare_workers_script Unable to deploy worker assets](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5616)
- [#5331: cloudflare_workers_script 500 internal server error when uploading python](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5331)
- [#5701: cloudflare_workers_script migrations for Durable Objects not recorded in tfstate; cannot be upgraded between versions](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5701)
- [#5704: cloudflare_workers_script randomly fails to deploy when changing compatibility_date](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5704)
- [#5439: cloudflare_workers_script (v5.2.0) ignoring content and bindings properties](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5439)
- [#5522: cloudflare_workers_script always detects changes after apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5522)
- [#5693: cloudflare_zero_trust_access_identity_provider gives recurring change on OTP pin login](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5693)
- [#5567: cloudflare_r2_custom_domain doesn't roundtrip jurisdiction properly](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5567)
- [#5179: Bad request with when creating cloudflare_api_shield_schema resource](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5179)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already exist for what you are experiencing.</p>
<h4 id="2025-08-01-terraform-v5.8.2-provider-upgrading">Upgrading</h4>
<p>We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized.</p>
<p>If you'd like more information on migrating from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-08-01-terraform-v5.8.2-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="terraform-v5-7-0-now-available"><a href="/changelog/post/2025-07-11-terraform-v5.7.0-provider/">Terraform v5.7.0 now available</a></h2>
<p><em>2025-07-14</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare community related to the v5 release, with 13.5% of resources impacted. We have committed to releasing improvements on a 2 week cadeance to ensure it's stability and relability, including the v5.7 release.</p>
<p>Thank you for continuing to raise issues and please keep an eye on this changelog for more information about upcoming releases.</p>
<h4 id="2025-07-11-terraform-v5.7.0-provider-changes">Changes</h4>
- Addressed permanent diff bug on Cloudflare Tunnel config
- State is now saved correctly for Zero Trust Access applications
- Exact match is now working as expected within `data.cloudflare_zero_trust_access_applications`
- `cloudflare_zero_trust_access_policy` now supports OIDC claims & diff issues resolved
- Self hosted applications with private IPs no longer require a public domain for `cloudflare_zero_trust_access_application`.
- New resource:
  - `cloudflare_zero_trust_tunnel_warp_connector`
- Other bug fixes
<p>For a more detailed look at all of the changes, see the
<a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.7.0">changelog</a> in GitHub.</p>
<h4 id="2025-07-11-terraform-v5.7.0-provider-issues-closed">Issues Closed</h4>
- [#5563: cloudflare_logpull_retention is missing import](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5563)
- [#5608: cloudflare_zero_trust_access_policy in 5.5.0 provider gives error upon apply unexpected new value: .app_count: was cty.NumberIntVal(0), but now cty.NumberIntVal(1)](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5608)
- [#5612: data.cloudflare_zero_trust_access_applications does not exact match](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5612)
- [#5532: cloudflare_zero_trust_access_identity_provider detects changes on every plan](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5532)
- [#5662: cloudflare_zero_trust_access_policy does not support OIDC claims](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5662)
- [#5565: Running Terraform with the cloudflare_zero_trust_access_policy resource results in updates on every apply, even when no changes are made - breaks idempotency](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5565)
- [#5529: cloudflare_zero_trust_access_application: self hosted applications with private ips require public domain ](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5529)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already exist for what you are experiencing.</p>
<h4 id="2025-07-11-terraform-v5.7.0-provider-upgrading">Upgrading</h4>
<p>We suggest holding on migration to v5 while we work on stabilization of the v5 provider. This will ensure Cloudflare can work ahead and avoid any blocking issues.</p>
<p>If you'd like more information on migrating from v4 to v5, please make use of the
<a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have
provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which
use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test
your changes before applying, and let us know if you encounter any additional issues by reporting to our
<a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-07-11-terraform-v5.7.0-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="cloudflare-user-groups-scim-user-groups-are-now-in-ga"><a href="/changelog/post/2025-06-23-user-groups-ga/">Cloudflare User Groups & SCIM User Groups are now in GA</a></h2>
<p><em>2025-06-23</em></p>
<p>We're announcing the GA of <strong>User Groups for Cloudflare Dashboard</strong> and <strong>System for Cross Domain Identity Management (SCIM) User Groups</strong>, strengthening our RBAC capabilities with stable, production-ready primitives for managing access at scale.</p>
<p><strong>What's New</strong></p>
<p><strong>User Groups [GA]</strong>: <a href="/fundamentals/manage-members/user-groups/">User Groups</a> are a new Cloudflare IAM primitive that enable administrators to create collections of account members that are treated equally from an access control perspective. User Groups can be assigned permission policies, with individual members in the group inheriting all permissions granted to the User Group. User Groups can be created manually or via our APIs.</p>
<p><strong>SCIM User Groups [GA]</strong>: Centralize &amp; simplify your user and group management at scale by syncing memberships directly from your upstream identity provider (like Okta or Entra ID) to the Cloudflare Platform. This ensures Cloudflare stays in sync with your identity provider, letting you apply Permission Policies to those synced groups directly within the Cloudflare Dashboard.</p>
<p><strong>Stability &amp; Scale</strong>:
These features have undergone extensive testing during the Public Beta period and are now ready for production use across enterprises of all sizes.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17727.md")</aside>
<p>For more info:</p>
<ul>
<li><a href="/fundamentals/manage-members/user-groups/">Get started with User Groups</a></li>
<li><a href="/fundamentals/account/account-security/scim-setup/">Explore our SCIM integration guide</a></li>
</ul>


<h2 id="terraform-v5-6-0-now-available"><a href="/changelog/post/2025-06-17-terraform-v5.6.0-provider/">Terraform v5.6.0 now available</a></h2>
<p><em>2025-06-17</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>.
Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since
launch, we have seen an unexpectedly high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a>
reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address
these issues across the company, and have released the v5.6.0 release which includes a number of bug fixes. Please keep an
eye on this changelog for more information about upcoming releases.</p>
<h4 id="2025-06-17-terraform-v5.6.0-provider-changes">Changes</h4>
<ul>
<li>Broad fixes across resources with recurring diffs, including, but not limited to:
<ul>
<li><code>cloudflare_zero_trust_access_identity_provider</code>
<ul>
<li><code>cloudflare_zone</code></li>
</ul>
</li>
</ul>
</li>
<li><code>cloudflare_page_rules</code> runtime panic when setting <code>cache_level</code> to <code>cache_ttl_by_status</code></li>
<li>Failure to serialize requests in <code>cloudflare_zero_trust_tunnel_cloudflared_config</code></li>
<li>Undocumented field 'priority' on <code>zone_lockdown</code> resource</li>
<li>Missing importability for <code>cloudflare_zero_trust_device_default_profile_local_domain_fallback</code> and <code>cloudflare_account_subscription</code></li>
<li>New resources:
<ul>
<li><code>cloudflare_schema_validation_operation_settings</code></li>
<li><code>cloudflare_schema_validation_schemas</code></li>
<li><code>cloudflare_schema_validation_settings</code></li>
<li><code>cloudflare_zero_trust_device_settings</code></li>
</ul>
</li>
<li>Other bug fixes</li>
</ul>
<p>For a more detailed look at all of the changes, see the
<a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.6.0">changelog</a> in GitHub.</p>
<h4 id="2025-06-17-terraform-v5.6.0-provider-issues-closed">Issues Closed</h4>
- [#5098: 500 Server Error on updating 'zero_trust_tunnel_cloudflared_virtual_network' Terraform resource](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5098)
- [#5148: cloudflare_user_agent_blocking_rule doesn’t actually support user agents](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5148)
- [#5472: cloudflare_zone showing changes in plan after following upgrade steps](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5472)
- [#5508: cloudflare_zero_trust_tunnel_cloudflared_config failed to serialize http request](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5508)
- [#5509: cloudflare_zone: Problematic Terraform behaviour with paused zones](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5509)
- [#5520: Resource 'cloudflare_magic_wan_static_route' is not working](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5520)
- [#5524: Optional fields cause crash in cloudflare_zero_trust_tunnel_cloudflared(s) when left null](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5524)
- [#5526: Provider v5 migration issue: no import method for cloudflare_zero_trust_device_default_profile_local_domain_fallback](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5526)
- [#5532: cloudflare_zero_trust_access_identity_provider detects changes on every plan](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5532)
- [#5561: cloudflare_zero_trust_tunnel_cloudflared: cannot rotate tunnel secret](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5561)
- [#5569: cloudflare_zero_trust_device_custom_profile_local_domain_fallback not allowing multiple DNS Server entries](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5569)
- [#5577: Panic modifying page_rule resource](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5577)
- [#5653: cloudflare_zone_setting resource schema confusion in 5.5.0: value vs enabled](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5653)
<p>If you have an unaddressed issue with the provider, we encourage you to check the
<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already
exist for what you are experiencing.</p>
<h4 id="2025-06-17-terraform-v5.6.0-provider-upgrading">Upgrading</h4>
<p>If you are evaluating a move from v4 to v5, please make use of the
<a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have
provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which
use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test
your changes before applying, and let us know if you encounter any additional issues by reporting to our
<a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-06-17-terraform-v5.6.0-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="cloudflare-user-groups-enhanced-permission-policies-are-now-in-beta"><a href="/changelog/post/2025-06-02-user-groups-beta/">Cloudflare User Groups & Enhanced Permission Policies are now in Beta</a></h2>
<p><em>2025-06-02</em></p>
<p>We're excited to announce the Public Beta launch of <strong>User Groups for Cloudflare Dashboard</strong> and <strong>System for Cross Domain Identity Management (SCIM) User Groups</strong>, expanding our RBAC capabilities to simplify user and group management at scale.</p>
<p>We've also visually overhauled the <strong>Permission Policies UI</strong> to make defining permissions more intuitive.</p>
<p><strong>What's New</strong></p>
<p><strong>User Groups [BETA]</strong>: <a href="/fundamentals/manage-members/user-groups/">User Groups</a> are a new Cloudflare IAM primitive that enable administrators to create collections of account members that are treated equally from an access control perspective. User Groups can be assigned permission policies, with individual members in the group inheriting all permissions granted to the User Group. User Groups can be created manually or via our APIs.</p>
<p><strong>SCIM User Groups [BETA]</strong>: Centralize &amp; simplify your user and group management at scale by syncing memberships directly from your upstream identity provider (like Okta or Entra ID) to the Cloudflare Platform. This ensures Cloudflare stays in sync with your identity provider, letting you apply Permission Policies to those synced groups directly within the Cloudflare Dashboard.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17726.md")</aside>
<p><strong>Revamped Permission Policies UI [BETA]</strong>: As Cloudflare's services have grown, so has the need for precise, role-based access control. We've given the Permission Policies builder a visual overhaul to make it much easier for administrators to find and define the exact permissions they want for specific principals.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-06-02-permissions-policy-ux.png" alt="Updated Permissions Policy UX" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17725.md")</aside>
<p>For more info:</p>
<ul>
<li><a href="/fundamentals/manage-members/user-groups/">Get started with User Groups</a></li>
<li><a href="/fundamentals/account/account-security/scim-setup/">Explore our SCIM integration guide</a></li>
</ul>


<h2 id="terraform-v5-5-0-now-available"><a href="/changelog/post/2025-05-19-terraform-v5.5.0-provider/">Terraform v5.5.0 now available</a></h2>
<p><em>2025-05-19</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.5.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.</p>
<h4 id="2025-05-19-terraform-v5.5.0-provider-changes">Changes</h4>
<ul>
<li>Broad fixes across resources with recurring diffs, including, but not limited to:
<ul>
<li><code>cloudflare_zero_trust_gateway_policy</code></li>
<li><code>cloudflare_zero_trust_access_application</code></li>
<li><code>cloudflare_zero_trust_tunnel_cloudflared_route</code></li>
<li><code>cloudflare_zone_setting</code></li>
<li><code>cloudflare_ruleset</code></li>
<li><code>cloudflare_page_rule</code></li>
</ul>
</li>
<li>Zone settings can be re-applied without client errors</li>
<li>Page rules conversion errors are fixed</li>
<li>Failure to apply changes to <code>cloudflare_zero_trust_tunnel_cloudflared_route</code></li>
<li>Other bug fixes</li>
</ul>
<p>For a more detailed look at all of the changes, see the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.5.0">changelog</a> in GitHub.</p>
<h4 id="2025-05-19-terraform-v5.5.0-provider-issues-closed">Issues Closed</h4>
- [#5304: Importing cloudflare_zero_trust_gateway_policy invalid attribute filter value](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5304)
- [#5303: cloudflare_page_rule import does not set values for all of the fields in terraform state](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5303)
- [#5178: cloudflare_page_rule Page rule creation with redirect fails](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5178)
- [#5336: cloudflare_turnstile_wwidget not able to update](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5336)
- [#5418: cloudflare_cloud_connector_rules: Provider returned invalid result object after apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5418)
- [#5423: cloudflare_zone_setting: "Invalid value for zone setting always_use_https"](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5423)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already exist for what you are experiencing.</p>
<h4 id="2025-05-19-terraform-v5.5.0-provider-upgrading">Upgrading</h4>
<p>If you are evaluating a move from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-05-19-terraform-v5.5.0-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="terraform-v5-4-0-now-available"><a href="/changelog/post/2025-05-06-terraform-v5.4.0-provider/">Terraform v5.4.0 now available</a></h2>
<p><em>2025-05-06</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.4.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.</p>
<h4 id="2025-05-06-terraform-v5.4.0-provider-changes">Changes</h4>
<ul>
<li>
<p>Removes the <code>worker_platforms_script_secret</code> resource from the provider (see <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade#cloudflare_worker_secret">migration guide</a> for alternatives—applicable to both Workers and Workers for Platforms)</p>
</li>
<li>
<p>Removes duplicated fields in <code>cloudflare_cloud_connector_rules</code> resource</p>
</li>
<li>
<p>Fixes <code>cloudflare_workers_route</code> id issues <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5134">#5134</a> <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5501">#5501</a></p>
</li>
<li>
<p>Fixes issue around refreshing resources that have unsupported response types</p>
<details>
<pre><code>&lt;summary&gt;Affected resources&lt;/summary&gt;
&lt;ul&gt;
</code></pre>
<pre><code>  &lt;li&gt;`cloudflare_certificate_pack`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_registrar_domain`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_stream_download`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_stream_webhook`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_user`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_workers_kv`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_workers_script`&lt;/li&gt;&#10;</code></pre>
<pre><code>&lt;/ul&gt;
</code></pre>
</details>
</li>
<li>
<p>Fixes <code>cloudflare_workers_kv</code> state refresh issues</p>
</li>
<li>
<p>Fixes issues around configurability of nested properties without computed values for the following resources</p>
<details>
<pre><code>&lt;summary&gt;Affected resources&lt;/summary&gt;
&lt;ul&gt;
</code></pre>
<pre><code>  &lt;li&gt;`cloudflare_account`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_account_dns_settings`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_account_token`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_api_token`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_cloud_connector_rules`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_custom_ssl`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_d1_database`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_dns_record`&lt;/li&gt;&#10;  &lt;li&gt;`email_security_trusted_domains`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_hyperdrive_config`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_keyless_certificate`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_list_item`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_load_balancer`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_logpush_dataset_job`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_network_monitoring_configuration`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_transit_site`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_transit_site_lan`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_transit_site_wan`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_wan_static_route`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_notification_policy`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_pages_project`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_queue`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_queue_consumer`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_cors`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_event_notification`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_lifecycle`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_lock`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_sippy`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_ruleset`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_snippet_rules`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_snippets`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_spectrum_application`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_workers_deployment`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_zero_trust_access_application`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_zero_trust_access_group`&lt;/li&gt;&#10;</code></pre>
<pre><code>&lt;/ul&gt;
</code></pre>
</details>
</li>
<li>
<p>Fixed defaults that made <code>cloudflare_workers_script</code> fail when using Assets</p>
</li>
<li>
<p>Fixed Workers Logpush setting in <code>cloudflare_workers_script</code> mistakenly being readonly</p>
</li>
<li>
<p>Fixed <code>cloudflare_pages_project</code> broken when using &quot;source&quot;</p>
</li>
</ul>
<p>The detailed <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.4.0">changelog</a> is available on GitHub.</p>
<h4 id="2025-05-06-terraform-v5.4.0-provider-upgrading">Upgrading</h4>
<p>If you are evaluating a move from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues either by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>, or by opening a <a href="https://www.support.cloudflare.com/s/?language=en_US">support ticket</a>.</p>
<h4 id="2025-05-06-terraform-v5.4.0-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="https://developers.cloudflare.com/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="updates-to-account-home-quick-actions-traffic-insights-workers-projects-and-more"><a href="/changelog/post/2025-03-26-account-home-updates/">Updates to Account Home - Quick actions, traffic insights, Workers projects, and more</a></h2>
<p><em>2025-03-26T06:00:00</em></p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-03-26-account-home-updates.png" alt="Updated Account Home" /></p>
<p>Recently, Account Home has been updated to streamline your workflows:</p>
<ul>
<li>
<p><strong>Recent Workers projects</strong>: You'll now find your projects readily accessible from a new <code>Developer Platform</code> tab on Account Home. See recently-modified projects and explore what you can work our developer-focused products.</p>
</li>
<li>
<p><strong>Traffic and security insights</strong>: Get a snapshot of domain performance at a glance with key metrics and trends.</p>
</li>
<li>
<p><strong>Quick actions</strong>: You can now perform common actions for your account, domains, and even Workers in just 1-2 clicks from the 3-dot menu.</p>
</li>
<li>
<p><strong>Keep starred domains front and center</strong>: Now, when you filter for starred domains on Account Home, we'll save your preference so you'll continue to only see starred domains by default.</p>
</li>
</ul>
<p>We can't wait for you to take the new Account Home for a spin.</p>
<p>For more info:</p>
<ul>
<li><a href="https://dash.cloudflare.com/">Try the updated Account Home</a></li>
<li><a href="/fundamentals/manage-domains/star-zones/">Documentation on starred domains</a></li>
</ul>


<h2 id="dozens-of-cloudflare-terraform-provider-resources-now-have-proper-drift-detection"><a href="/changelog/post/2025-03-21-resource-force-replacement-bug/">Dozens of Cloudflare Terraform Provider resources now have proper drift detection</a></h2>
<p><em>2025-03-21</em></p>
<p>In <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare Terraform Provider</a> versions 5.2.0 and above, dozens of resources now have proper drift detection. Before this fix, these resources would indicate they needed to be updated or replaced — even if there was no real change. Now, you can rely on your <code>terraform plan</code> to only show what resources are expected to change.</p>
<p>This issue affected <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">resources</a> related to these products and features:</p>
<ul>
<li>API Shield</li>
<li>Argo Smart Routing</li>
<li>Argo Tiered Caching</li>
<li>Bot Management</li>
<li>BYOIP</li>
<li>D1</li>
<li>DNS</li>
<li>Email Routing</li>
<li>Hyperdrive</li>
<li>Observatory</li>
<li>Pages</li>
<li>R2</li>
<li>Rules</li>
<li>SSL/TLS</li>
<li>Waiting Room</li>
<li>Workers</li>
<li>Zero Trust</li>
</ul>


<h2 id="cloudflare-terraform-provider-now-properly-redacts-sensitive-values"><a href="/changelog/post/2025-03-21-sensitive-values-redacted/">Cloudflare Terraform Provider now properly redacts sensitive values</a></h2>
<p><em>2025-03-21</em></p>
<p>In the <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare Terraform Provider</a> versions 5.2.0 and above, sensitive properties of resources are redacted in logs. Sensitive properties in <a href="https://raw.githubusercontent.com/cloudflare/api-schemas/refs/heads/main/openapi.yaml">Cloudflare's OpenAPI Schema</a> are now annotated with <code>x-sensitive: true</code>. This results in proper auto-generation of the corresponding Terraform resources, and prevents sensitive values from being shown when you run Terraform commands.</p>
<p>This issue affected <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">resources</a> related to these products and features:</p>
<ul>
<li>Alerts and Audit Logs</li>
<li>Device API</li>
<li>DLP</li>
<li>DNS</li>
<li>Magic Visibility</li>
<li>Magic WAN</li>
<li>TLS Certs and Hostnames</li>
<li>Tunnels</li>
<li>Turnstile</li>
<li>Workers</li>
<li>Zaraz</li>
</ul>


<h2 id="terraform-v5-provider-is-now-generally-available"><a href="/changelog/post/2025-02-03-terraform-v5-provider/">Terraform v5 Provider is now generally available</a></h2>
<p><em>2025-02-03</em></p>
<p><img src="/assets/upstream/images/changelog/2024-02-03-terraform-v5-screenshot.png" alt="Screenshot of Terraform defining a Zone" /></p>
<p>Cloudflare's v5 Terraform Provider is now generally available. With this release, Terraform resources are now automatically generated based on OpenAPI Schemas. This change brings alignment across our SDKs, API documentation, and now Terraform Provider. The new provider boosts coverage by increasing support for API properties to 100%, adding 25% more resources, and more than 200 additional data sources. Going forward, this will also reduce the barriers to bringing more resources into Terraform across the broader Cloudflare API. This is a small, but important step to making more of our platform manageable through GitOps, making it easier for you to manage Cloudflare just like you do your other infrastructure.</p>
<p>The Cloudflare Terraform Provider v5 is a ground-up rewrite of the provider and introduces breaking changes for some resource types. Please refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">upgrade guide</a> for best practices, or the <a href="https://blog.cloudflare.com/automatically-generating-cloudflares-terraform-provider/">blog post on automatically generating Cloudflare's Terraform Provider</a> for more information about the approach.</p>
<p>For more info</p>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="https://developers.cloudflare.com/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/docs-collections/2/">Previous</a><span>Page 3 of 3</span></nav>
