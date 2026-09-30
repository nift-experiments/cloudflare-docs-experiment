<p>Organizations can deploy and manage the Cloudflare One Client (formerly WARP) across their fleet of devices in two complementary ways:</p>
<ul>
<li><strong>Through a mobility management solution (MDM)</strong> — Push the client installer and its deployment parameters using a tool such as <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/">Intune, JAMF, Kandji, or JumpCloud</a>, or by executing an <code>.msi</code> file on desktop machines. This page covers the MDM-driven workflow.</li>
<li><strong>From the Cloudflare dashboard</strong> — Manage client versions for groups of devices directly from the Zero Trust dashboard, without relying on a third-party MDM solution. For more information, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/">Client version assignments</a>.</li>
</ul>
<h2 id="mdm-policy-file">MDM policy file</h2>
<p>Refer to our <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/">managed deployment instructions</a> and create a <code>.plist</code>, <code>mdm.xml</code>, or <code>.msi</code> policy file based on your organization's software management tool.</p>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/">MDM parameters</a> that you specify in a local policy file will overrule any <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/">device client settings</a> configured in the dashboard.
Therefore, we recommend that your policy file only contain the organization name and potentially the onboarding flag, <a href="/learning-paths/secure-internet-traffic/configure-device-agent/device-profiles/">relying on the dashboard</a> to configure the remaining device settings.</p>
<pre><code class="language-xml">&lt;dict&gt;&#10;  &lt;key&gt;organization&lt;/key&gt;&#10;  &lt;string&gt;your-team-name&lt;/string&gt;&#10;  &lt;key&gt;onboarding&lt;/key&gt;&#10;  &lt;false/&gt;&#10;&lt;/dict&gt;&#10;</code></pre>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, select <strong>Zero Trust</strong>.</p>
</li>
<li>
<p>On the onboarding screen, choose a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
</li>
</ol>
@markup("md", "content/.markup/bodies/10048.md")
</div>. The team name is a unique, internal identifier for your Zero Trust organization. Users will enter this team name when they enroll their device manually, and it will be the subdomain for your App Launcher (as relevant). Your business name is the typical entry.
<p>You can find your team name in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> by going to <strong>Zero Trust</strong> &gt; <strong>Settings</strong>.</p>
<ol start="3">
<li>Complete your onboarding by selecting a subscription plan and entering your payment details. If you chose the <strong>Zero Trust Free plan</strong>, this step is still needed but you will not be charged.</li>
</ol>
<p>When you create your organization, Cloudflare automatically adds the <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">Cloudflare identity provider</a> as your default login method, so your users can sign in with their Cloudflare account credentials right away. You can add a <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time PIN</a> or connect a <a href="/cloudflare-one/integrations/identity-providers/">third-party identity provider</a> at any time.</p>
