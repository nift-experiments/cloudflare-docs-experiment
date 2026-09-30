<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5910.md")
</aside>
<p>Cloudflare One enables you to restrict access to your applications to devices running the Cloudflare One Client. This allows you to flexibly ensure that a user's traffic is secure and encrypted before allowing access to a resource protected behind Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client Checks</a>.</p>
<h2 id="1-enable-the-warp-check"><ol>
<li>Enable the WARP check</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>.</li>
<li>Ensure that <em>Allow Secure Web Gateway to proxy traffic</em>* is enabled.</li>
<li>Go to <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</li>
<li>In <strong>Cloudflare One Client checks</strong>, select <strong>Add a check</strong>.</li>
<li>Select <strong>WARP</strong>, then select <strong>Save</strong>.</li>
</ol>
<h2 id="2-add-the-check-to-an-access-policy"><ol start="2">
<li>Add the check to an Access policy</li>
</ol></h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Locate the application for which you want to require WARP. Select <strong>Configure</strong>.</p>
</li>
<li>
<p>In the <strong>Policies</strong> tab, create a new Access policy or edit an existing policy.</p>
</li>
<li>
<p>In the policy builder, add an Include or Require rule which uses the <em>WARP</em> selector. Save the policy.</p>
</li>
<li>
<p>Save the Access application.</p>
</li>
</ol>
<p>Before granting access to the application, the policy will check that the device is running the Cloudflare One Client.</p>
