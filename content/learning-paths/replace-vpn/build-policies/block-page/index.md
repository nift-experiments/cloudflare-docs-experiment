<p>With Cloudflare Zero Trust, you can deliver actionable feedback to users when they are blocked by a Gateway policy. Custom block messages can reduce user confusion and decrease your IT ticket load.</p>
<p>There are two different ways to surface block messages:</p>
<ul>
<li><a href="#custom-block-page">Custom block page</a></li>
<li><a href="#cloudflare-one-client-block-notifications">Cloudflare One Client block notifications</a></li>
</ul>
<h2 id="custom-block-page">Custom block page</h2>
<p>You can display a custom block page in the browser when users are blocked by a Gateway DNS or HTTP policy. This is a static page that educates users on why they were blocked and how to contact IT.</p>
<p>The custom block page has a few drawbacks:</p>
<ul>
<li>To display the block page, you must install a <a href="/learning-paths/replace-vpn/configure-device-agent/enable-tls-decryption/#configure-user-side-certificates">user-side certificate</a> on the end user device.</li>
<li>The block page does not appear when users are blocked by a Gateway network policy.</li>
<li>The custom block page only displays when the user loads a site in a browser. If, for instance, the user is allowed to visit a site but not allowed to upload a file, the file upload would fail silently and the user would not get a block page.</li>
</ul>
<p>To work around these limitations, we recommend using <a href="#cloudflare-one-client-block-notifications">Cloudflare One Client block notifications</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9991.md")
</aside>
<h3 id="enable-the-block-page-for-dns-policies">Enable the block page for DNS policies</h3>
<p>For DNS policies, you will need to enable the block page on a per-policy basis.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9994.md")
</div></div>
<h3 id="customize-the-block-page">Customize the block page</h3>
<p>You can customize the Cloudflare-hosted block page by making global changes that Gateway will display every time a user reaches your block page. Customizations will apply regardless of the type of policy (DNS or HTTP) that blocks the traffic.</p>
<p>To customize your block page:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9997.md")
</div></div>
<p>Gateway will now display a custom Gateway block page when your users visit a blocked website.</p>
<h2 id="cloudflare-one-client-block-notifications">Cloudflare One Client block notifications</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9990.md")
</aside>
<p>For more granular user feedback, you can enable Cloudflare One Client block notifications on any Gateway DNS or Network <em>Block</em> policy. Blocked users will receive an operating system notification from the Cloudflare One Client with a custom message you set.</p>
<p>Client notifications provide additional functionality over the <a href="#custom-block-page">custom block page</a>:</p>
<ul>
<li>
<p>Client notifications work with network policies, which means you can surface feedback for all partial actions on user traffic including blocking a specific port, file upload, or protocol.</p>
</li>
<li>
<p>Client notifications allow you to direct users to a unique link per individual policy. For example, you could link users to your organization's acceptable use policy, data protection policy, or any existing IT troubleshooting infrastructure. If no infrastructure for this exists within your organization, you can quickly deploy an HTML site on <a href="/pages/">Cloudflare Pages</a>, put the site behind a <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access policy</a>, and provide dynamic feedback based on the identity and device posture values found in the user's <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/">Access JWT</a>.</p>
</li>
</ul>
