<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9685.md")
</aside>
<p><a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">Clientless Web Isolation</a> allows you to on-ramp user traffic to your private network without needing to install the Cloudflare One Client. Users access private applications by going to a prefixed URL:</p>
<p><code>https://&lt;your-team-name&gt;.cloudflareaccess.com/browser/&lt;URL&gt;</code></p>
<p>After the user authenticates to your IdP, Cloudflare will load the application in a secure remote browser and apply your Gateway firewall policies to user traffic.</p>
<h2 id="setup">Setup</h2>
<p>To configure Clientless Web Isolation to augment clientless access, refer to <a href="/cloudflare-one/tutorials/clientless-access-private-dns/">this tutorial</a>.</p>
<h2 id="best-practices">Best practices</h2>
<ul>
<li>For guidance on building Gateway policies for private network applications, refer to <a href="/learning-paths/replace-vpn/build-policies/create-policy/">Secure your first application</a>.</li>
<li>If you already deployed the Cloudflare One Client to some devices as part of a mixed-access methodology, ensure that your Gateway firewall policies do not rely on device posture checks. Because Clientless Web Isolation is not a machine in your fleet, it will not return any values for device posture checks.</li>
<li>You can standardize the user experience by making specific applications available in your App Launcher as <a href="/learning-paths/clientless-access/customize-ux/bookmarks/">bookmarks</a>. In this case, you would create a new bookmark for <code>https://&lt;team-name&gt;.cloudflareaccess.com/browser/https://internalresource.com</code>, which would take users directly to an isolated session with your application.</li>
</ul>
