<p>Cloudflare One allows you to build Zero Trust rules based on device UUIDs supplied in an MDM file. You can create these rules so that access to applications is granted only to users connecting from company devices.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client Checks</a>.</p>
<h2 id="1-assign-uuids-to-devices"><ol>
<li>Assign UUIDs to devices</li>
</ol></h2>
<p>You will need to use a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/">managed deployment tool</a> to assign UUIDs. It is not possible to assign them manually.</p>
<ol>
<li>
<p>Generate a unique identifier for each corporate device. For best practices on choosing UUIDs, refer to the <a href="https://developer.android.com/training/articles/user-data-ids#best-practices-android-identifiers">Android documentation</a>.</p>
</li>
<li>
<p>Enter the UUIDs into your MDM configuration file using the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#unique_client_id"><code>unique_client_id</code> key</a>.</p>
</li>
</ol>
<h2 id="2-create-a-list-of-uuids"><ol start="2">
<li>Create a list of UUIDs</li>
</ol></h2>
<p>To create rules based on device UUIDs, you first need to create a <a href="/cloudflare-one/reusable-components/lists/">Gateway List</a> of UUIDs.</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Lists</strong>.</p>
</li>
<li>
<p>Select <strong>Create manual list</strong> or <strong>Upload CSV</strong>. For larger teams, we recommend uploading a CSV or using Cloudflare's <a href="/api/resources/zero_trust/subresources/gateway/subresources/lists/methods/list/">API endpoint</a>.</p>
</li>
<li>
<p>Give your list a descriptive name, as this name will appear when configuring your policies.</p>
</li>
<li>
<p>Set <strong>List Type</strong> to <em>Device IDs</em>.</p>
</li>
<li>
<p>Enter the UUIDs of the devices your team manages, or upload your CSV file.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5920.md")
</aside>
<h2 id="3-enable-the-posture-check"><ol start="3">
<li>Enable the posture check</li>
</ol></h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</p>
</li>
<li>
<p>Go to <strong>Cloudflare One Client checks</strong> and select <strong>Add a check</strong>.</p>
</li>
<li>
<p>Select <strong>Unique Client ID</strong>.</p>
</li>
<li>
<p>You will be prompted for the following information:</p>
<ul>
<li><strong>Name</strong>: Enter a unique name for this device posture check.</li>
<li><strong>Operating system</strong>: Select the operating system of the device.</li>
<li><strong>List</strong>: Select your <a href="#2-create-a-list-of-uuids">list of UUIDs</a>.</li>
</ul>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
<li>
<p><a href="/cloudflare-one/reusable-components/posture-checks/#2-verify-device-posture-checks">Verify</a> that the posture check is returning the expected results.</p>
</li>
</ol>
<p>You can now create an Access or Gateway device posture policy that checks if the device presents a UUID on your list.</p>
