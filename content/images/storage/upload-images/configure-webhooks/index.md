<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9479.md")
</aside>
<p>You can set up webhooks to receive notifications about your upload workflow. This will send an HTTP POST request to a specified endpoint when an image either successfully uploads or fails to upload.</p>
<p>Currently, webhooks are supported only for <a href="/images/storage/upload-images/direct-creator-upload/">direct creator uploads</a>.</p>
<p>To receive notifications for direct creator uploads:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> pages.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Destinations</strong>.</li>
<li>From the Webhooks card, select <strong>Create</strong>.</li>
<li>Enter information for your webhook and select <strong>Save and Test</strong>. The new webhook will appear in the <strong>Webhooks</strong> card and can be attached to notifications.</li>
<li>Next, go to <strong>Notifications</strong> &gt; <strong>All Notifications</strong> and select <strong>Add</strong>.</li>
<li>Under the list of products, locate <strong>Images</strong> and select <strong>Select</strong>.</li>
<li>Give your notification a name and optional description.</li>
<li>Under the <strong>Webhooks</strong> field, select the webhook that you recently created.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
