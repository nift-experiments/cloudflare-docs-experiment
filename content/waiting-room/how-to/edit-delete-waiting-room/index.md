<p>You can manage your waiting rooms using the <a href="/waiting-room/how-to/waiting-room-dashboard/">Waiting Room dashboard</a> or the <a href="/waiting-room/reference/waiting-room-api/">API</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15746.md")
</aside>
<h2 id="use-the-dashboard">Use the dashboard</h2>
<h3 id="edit-a-waiting-room">Edit a waiting room</h3>
<ol>
<li>In your application, go to <strong>Traffic</strong> &gt; <strong>Waiting Room</strong>.</li>
<li>On a record, select <strong>Edit</strong>.</li>
<li>Select <strong>Settings</strong>.</li>
<li>Edit the settings. For a description of settings, refer to <a href="/waiting-room/reference/configuration-settings/">Configuration settings</a>.</li>
<li>Select <strong>Next</strong>. If you have access to <a href="/waiting-room/how-to/customize-waiting-room/">customized templates</a>, you could also adjust the template.</li>
<li>Once you get to <strong>Review</strong>, select <strong>Save</strong>.</li>
</ol>
<h3 id="delete-a-waiting-room">Delete a waiting room</h3>
<ol>
<li>In your application, go to <strong>Traffic</strong> &gt; <strong>Waiting Room</strong>.</li>
<li>On a record, select <strong>Delete</strong>.</li>
<li>Select <strong>Delete</strong> again.</li>
</ol>
<h2 id="use-the-api">Use the API</h2>
<h3 id="edit-a-waiting-room-1">Edit a waiting room</h3>
<p><a href="https://api.cloudflare.com#waiting-room-update-waiting-room">Replace</a> a configured waiting room by appending the following endpoint to the Cloudflare API base URL.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/waiting_rooms/{waiting_room_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;webshop-waiting-room&quot;,&#10;  &quot;host&quot;: &quot;example.com&quot;,&#10;  &quot;new_users_per_minute&quot;: 200,&#10;  &quot;total_active_users&quot;: 300&#10;}&#x27;</code></pre>
<p><a href="https://api.cloudflare.com#waiting-room-patch-waiting-room">Update</a> a configured waiting room by appending the following endpoint to the Cloudflare API base URL.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/waiting_rooms/{waiting_room_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;webshop-waiting-room&quot;,&#10;  &quot;host&quot;: &quot;example.com&quot;,&#10;  &quot;new_users_per_minute&quot;: 200,&#10;  &quot;total_active_users&quot;: 300&#10;}&#x27;</code></pre>
<p>You only need to include the fields you want to update in the payload of the PATCH request.</p>
<h3 id="delete-a-waiting-room-1">Delete a waiting room</h3>
<p>Delete a waiting room by appending the following endpoint in the <a href="https://api.cloudflare.com#waiting-room-delete-waiting-room">Waiting Room API</a> to the Cloudflare API base URL.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/waiting_rooms/{waiting_room_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
