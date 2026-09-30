<p>With the Access App Launcher, users can open all applications that they have access to from a single dashboard.</p>
<p>The App Launcher is available at a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/4777.md")
</div> unique to your Cloudflare Zero Trust account, for example `mycompany.cloudflareaccess.com`.
<p>Users log in using one of the identity providers configured for the account. Once Access authenticates the user, the App Launcher displays applications they are authorized to use, in the form of application tiles. Selecting an application tile launches the application's hostname, sending the user to that tool as part of their SSO flow.</p>
<p><img src="/assets/upstream/images/cloudflare-one/applications/app-launcher.png" alt="App Launcher portal" /></p>
<h2 id="enable-the-app-launcher">Enable the App Launcher</h2>
<p>By default, the App Launcher is disabled. To enable it, you must configure a policy that defines which users can access the App Launcher.</p>
<p>To enable the App Launcher:</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Access settings</strong>.</p>
</li>
<li>
<p>Under the <strong>Manage your App Launcher</strong> card, select <strong>Manage</strong>.</p>
</li>
<li>
<p>On the <strong>Policies</strong> tab, <a href="/cloudflare-one/access-controls/policies/">build a policy</a> to define who can access your App Launcher portal. These rules do not impact permissions for the applications secured behind Access.</p>
</li>
<li>
<p>On the <strong>Authentication</strong> tab, choose the identity providers users can authenticate with.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>The App Launcher is now available at <code>&lt;your-team-name&gt;.cloudflareaccess.com</code>. You can always edit your App Launcher rules by going to <strong>Access controls</strong> &gt; <strong>Access settings</strong>.</p>
<h2 id="add-a-tile-to-the-app-launcher">Add a tile to the App Launcher</h2>
<p>Tiles have a one-to-one relationship with each application you create in Access. The tile names displayed in the Access App Launcher portal correspond to the application names listed under <strong>Access controls</strong> &gt; <strong>Applications</strong>. For example, if you create one application for general access to your Jira deployment and a separate application that restricts requests to a particular Jira path, a user authorized for both will see separate tiles for each. If you add multiple hostnames to a single application, the user will only see the domain selected in the application's <strong>App Launcher</strong> settings.</p>
<p>To show an Access application in the App Launcher:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select an application and select <strong>Configure</strong>.</li>
<li>Go to <strong>Experience settings</strong>.</li>
<li>Select <strong>Show application in App Launcher</strong>. The App Launcher link will only appear for users who are allowed by your Access policies. Blocked users will not see the app in their App Launcher.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4776.md")
</aside>
<ol start="5">
<li>(Optional) To use a custom logo for the application tile, select <strong>Use custom logo</strong> and enter a link to your desired image.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4775.md")
</aside>
<ol start="6">
<li>
<p>In <strong>Application domains</strong>, choose a domain to use for the App Launcher link.</p>
</li>
<li>
<p>(Optional) In <strong>Tags</strong>, add <a href="/cloudflare-one/reusable-components/tags/">custom tags</a> so that users can more easily find the application in their App Launcher.</p>
</li>
</ol>
<h2 id="customize-app-launcher-appearance">Customize App Launcher appearance</h2>
<p>To customize the App Launcher with your own branding, messages, and links, refer to the <a href="/cloudflare-one/reusable-components/custom-pages/app-launcher-customization/">Custom pages documentation</a>.</p>
