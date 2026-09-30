<p>If you plan to direct your users to manually download and configure the Cloudflare One Client (formerly WARP), users will need to connect the client to your organization's Cloudflare Zero Trust instance.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Complete <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Zero Trust organization setup</a>, including subscription activation.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/">Set device enrollment permissions</a> to specify which users can connect.</li>
</ul>
<h2 id="windows-macos-and-linux">Windows, macOS, and Linux</h2>
<h3 id="enroll-using-the-gui">Enroll using the GUI</h3>
<p>To enroll your device using the client GUI:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6130.md")
</div></div>
<p>The device is now protected by your organization's Zero Trust policies.</p>
<h3 id="enroll-using-the-cli">Enroll using the CLI</h3>
<p>To enroll your device using the terminal:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/6139.md")
</div>
<p>The device is now protected by your organization's Zero Trust policies. For more information on all available commands, run <code>warp-cli --help</code>.</p>
<h2 id="ios-android-and-chromeos">iOS, Android, and ChromeOS</h2>
<h3 id="enroll-manually">Enroll manually</h3>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">Download</a> and install the Cloudflare One Agent app.</li>
<li>Launch the Cloudflare One Agent app.</li>
<li>Select <strong>Next</strong>.</li>
<li>Review the privacy policy and select <strong>Accept</strong>.</li>
<li>Enter your <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ol>
@markup("md", "content/.markup/bodies/6140.md")
</div>.
6. Complete the authentication steps required by your organization.
7. After authenticating, select **Install VPN Profile**.
8. In the **Connection request** popup window, select **OK**.
9. If you did not enable [auto-connect](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#auto-connect), manually turn on the switch to **Connected**.
<p>The device is now protected by your organization's Zero Trust policies.</p>
<h3 id="enroll-using-a-url">Enroll using a URL</h3>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6141.md")
</div></details>
<p>Administrators can provide users with a custom login URL that automatically fills in your organization's <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/6142.md")
</div> during device enrollment. Using a URL reduces the potential for error that comes with manual entry of the team name.
<p>The Cloudflare One Client supports URLs accessed through a direct link or with a URL handler such as a QR code. Direct links are currently only supported in Safari and Firefox. If your default browser is Chrome (or another unsupported browser), we recommend embedding the link in a QR code.</p>
<h4 id="generate-a-login-url">Generate a login URL</h4>
<p>To generate a URL for device enrollment:</p>
<ol>
<li>Copy the following link, replacing <code>&lt;your-team-name&gt;</code> with your Zero Trust <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ol>
@markup("md", "content/.markup/bodies/6143.md")
</div>:
<pre><code class="language-txt">cf1app://oneapp.cloudflare.com/team?name=&lt;your-team-name&gt;&#10;</code></pre>
<ol start="2">
<li>(Optional) Use any QR code generator to embed the link in a QR code.</li>
<li>Distribute the link or QR code to users.</li>
</ol>
<h4 id="use-the-login-url">Use the login URL</h4>
<p>To enroll a device using a login URL:</p>
<ol>
<li>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">Download</a> and install the Cloudflare One Agent app.</p>
</li>
<li>
<p>Go to the <a href="#generate-a-login-url">login URL</a> provided by your account administrator. To use a QR code, open the QR scanner app on your device and scan the QR code.</p>
<pre><code>The Cloudflare One Agent app will open and start the onboarding flow.&#10;</code></pre>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6125.md")
</aside>
<ol start="3">
<li>
<p>To complete the onboarding flow:</p>
<pre><code>a. Review the privacy policy and select **Accept**.&#10;</code></pre>
<p>b. On the <strong>Enter team name</strong> screen, confirm that the pre-populated <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
</li>
</ol>
@markup("md", "content/.markup/bodies/6144.md")
</div> matches your organization.
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="already-authenticated-error">`Already Authenticated` error</h3>
@markup("md", "content/.markup/bodies/6124.md")
</aside>
<pre><code>c. Complete the authentication steps required by your organization.&#10;&#10;    d. After authenticating, select **Install VPN Profile**.&#10;&#10;    e. In the **Connection request** popup window, select **OK**.&#10;</code></pre>
<ol start="4">
<li>If you did not enable <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#auto-connect">auto-connect</a>, manually turn on the switch to <strong>Connected</strong>.</li>
</ol>
<p>The device is now protected by your organization's Zero Trust policies.</p>
<h2 id="virtual-machines">Virtual machines</h2>
<p>By default, virtual machines (VMs) are subject to the device client settings of the host. If you want to deploy a separate instance of the Cloudflare One Client in a VM, you must configure the VM to operate in bridged networking mode.</p>
