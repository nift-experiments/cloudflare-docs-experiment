<p>Administrators can automate Cloudflare One Client (formerly WARP) registration on managed devices and minimize the number of clicks required from an end user.</p>
<p>During the default Cloudflare One Client enrollment process, end users typically need to complete several steps in order to login:</p>
<ol>
<li>Review Terms and Conditions in the Cloudflare One Client GUI and acknowledge your company's use of the Cloudflare One Client.</li>
<li>Select their identity provider from the Cloudflare Access login screen.</li>
<li>Complete the authentication steps required by the identity provider.</li>
<li>Interact with a browser popup requesting permission to launch the Cloudflare One Client.</li>
</ol>
<p>This guide covers how to eliminate steps 1, 2 and 4 from your Cloudflare One Client deployment.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="service-token-authentication">Service token authentication</h3>
@markup("md", "content/.markup/bodies/6344.md")
</aside>
<p>On iOS and Android / ChromeOS, end users will still be asked questions required by their platform such as accepting notifications or installing the VPN Profile.</p>
<h2 id="turn-off-onboarding-screens">Turn off onboarding screens</h2>
<p>To skip the Terms and Conditions screens that are usually presented to users, set the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/"><code>onboarding</code> parameter</a> to <code>false</code> in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/">MDM deployment file</a>. Here is an example <code>mdm.xml</code> file:</p>
<pre><code class="language-xml">&lt;dict&gt;&#10;  &lt;key&gt;organization&lt;/key&gt;&#10;  &lt;string&gt;your-team-name&lt;/string&gt;&#10;	&lt;key&gt;onboarding&lt;/key&gt;&#10;	&lt;false/&gt;&#10;&lt;/dict&gt;&#10;</code></pre>
<h2 id="turn-on-instant-authentication">Turn on instant authentication</h2>
<p>If you are only using one identity provider for device enrollment, turn on <strong>Apply instant authentication</strong> in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/#set-device-enrollment-permissions">device enrollment permissions</a>. This allow users to skip the Cloudflare Access login page and go directly to your SSO login event.</p>
<h2 id="allow-browser-to-launch-the-cloudflare-one-client">Allow browser to launch the Cloudflare One Client</h2>
<p>You can configure your browser to automatically launch the Cloudflare One Client application after a successful login and skip the <strong>Open Cloudflare WARP.app</strong> popup.</p>
<p><img src="/assets/upstream/images/cloudflare-one/connections/warp-protocol-handler.png" alt="Browser popup requesting permission to open the Cloudflare One Client" /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<h3 id="chromium-based-browsers">Chromium-based browsers</h3>
<p>Chromium-based browsers such as Google Chrome and Microsoft Edge have a policy setting called <a href="https://learn.microsoft.com/en-us/DeployEdge/microsoft-edge-policies#autolaunchprotocolsfromorigins">AutoLaunchProtocolsFromOrigins</a>. This setting takes in two parameters: a protocol for the browser to launch and the origins that are allowed to launch it. For the browser to launch the Cloudflare One Client, you need to set the protocol to <code>com.cloudflare.warp</code> and the origin to your <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/6345.md")
</div> (`https://<your-team-name>.cloudflareaccess.com`).
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6350.md")
</div></div>
