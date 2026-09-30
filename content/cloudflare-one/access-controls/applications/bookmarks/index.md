<p>With Cloudflare One, you can show applications on the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a> even if those applications are not secured behind Access. This way, users can access all the applications they need to work, all in one place — regardless of whether those applications are protected by Access.</p>
<p>Links to applications not protected by Access can be added as bookmarks. You can assign <a href="/cloudflare-one/access-controls/policies/">Access policies</a> to control which users see the bookmark in the App Launcher. Users who do not match an Allow policy will not see the bookmark tile. Unlike policies for other Access application types, bookmark policies only affect visibility in the App Launcher and do not control access to the destination URL.</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Select <strong>Create new application</strong> &gt; <strong>Bookmarks</strong>.</p>
</li>
<li>
<p>Name your application.</p>
</li>
<li>
<p>Enter your <strong>Application URL</strong>, for example <code>https://mybookmark.com</code>.</p>
</li>
<li>
<p>(Optional) To restrict who can see the bookmark, select an existing policy or create a new one. If you do not add any policies, the bookmark is visible to all users in your organization.</p>
<ul>
<li>To use an existing policy, select <strong>Select existing policies</strong> and choose the policies you want to apply. Refer to <a href="#supported-policies">supported policies</a> for policy limitations.</li>
<li>To create a new policy, select <strong>Create new policy</strong> and <a href="/cloudflare-one/access-controls/policies/">build your policy rules</a>.</li>
</ul>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>Turn on <strong>App Launcher visibility</strong> if you want the application to be visible in the App Launcher. The toggle does not impact the ability for users to reach the application.</p>
</li>
<li>
<p>(Optional) To add a custom logo for your application, select <strong>Custom</strong> and enter the image URL.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4688.md")
</aside>
<ol start="9">
<li>Select <strong>Save</strong>.</li>
</ol>
<p>The application will show up on the Applications page labeled as <code>BOOKMARK</code>. You can always edit or delete your bookmarks, as you would any other application.</p>
<h2 id="authentication-logs">Authentication logs</h2>
<p>Bookmark applications do not generate individual <a href="/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/#authentication-logs">Access authentication logs</a> when a user selects the bookmark tile. Only the authentication event to the App Launcher itself is logged.</p>
<h2 id="supported-bookmark-policies">Supported bookmark policies</h2>
<p>Bookmark policies support all <a href="/cloudflare-one/access-controls/policies/#selectors">Access policy selectors</a>, including</p>
<ul>
<li>Identity-based selectors (such as emails, email domains, or identity provider groups)</li>
<li>Location-based selectors (such as country or IP ranges)</li>
<li>Device posture checks (requires installing the Cloudflare One Client)</li>
</ul>
<p>The following policy features are not supported for bookmark applications:</p>
<ul>
<li><a href="/cloudflare-one/access-controls/policies/isolate-application/">Isolate application</a></li>
<li><a href="/cloudflare-one/access-controls/policies/require-purpose-justification/">Purpose justification</a></li>
<li><a href="/cloudflare-one/access-controls/policies/temporary-auth/">Temporary authentication</a></li>
</ul>
<p>If you attempt to assign a policy that uses an unsupported feature, the dashboard will display an error.</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="device-posture-policies">Device posture policies</h3>
@markup("md", "content/.markup/bodies/4687.md")
</aside>
