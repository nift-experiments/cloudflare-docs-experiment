<p>With Require Gateway, you can allow access to your applications only to devices enrolled in your Zero Trust organization. Unlike <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/require-warp/">Require WARP</a>, which will check for any WARP instance (including the consumer version), Require Gateway will only allow requests coming from devices whose traffic is filtered by your organization's Cloudflare Gateway configuration. This policy is best used when you want to protect company-owned assets by only allowing access to employees.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client Checks</a>.</p>
<h2 id="1-enable-the-gateway-check"><ol>
<li>Enable the Gateway check</li>
</ol></h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</p>
</li>
<li>
<p>Go to <strong>Cloudflare One Client checks</strong> and select <strong>Add a check</strong>.</p>
</li>
<li>
<p>Select <strong>Gateway</strong>, then select <strong>Save</strong>.</p>
</li>
</ol>
<h2 id="2-add-the-check-to-an-access-application"><ol start="2">
<li>Add the check to an Access application</li>
</ol></h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Locate the application for which you want to require Gateway. Select <strong>Configure</strong>.</p>
</li>
<li>
<p>In the <strong>Policies</strong> tab, create a new Access policy or edit an existing policy.</p>
</li>
<li>
<p>In the policy builder, add an Include or Require rule which uses the <em>Gateway</em> selector. Save the policy.</p>
</li>
<li>
<p>Save the Access application.</p>
</li>
</ol>
<p>Before granting access to the application, the policy will check that the device is running the Cloudflare One Client and enrolled in your Zero Trust organization.</p>
