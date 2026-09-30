<p>With player enhancements, you can modify your video player to incorporate elements of your branding such as your logo, and customize additional options to present to your viewers.</p>
<p>The player enhancements are automatically applied to videos using the Stream Player, but you will need to add the details via the <code>publicDetails</code> property when using your own player.</p>
<h2 id="properties">Properties</h2>
<ul>
<li><code>title</code>: The title that appears when viewers hover over the video. The title may differ from the file name of the video.</li>
<li><code>share_link</code>: Provides the user with a click-to-copy option to easily share the video URL. This is commonly set to the URL of the page that the video is embedded on.</li>
<li><code>channel_link</code>: The URL users will be directed to when selecting the logo from the video player.</li>
<li><code>logo</code>: A valid HTTPS URL for the image of your logo.</li>
</ul>
<h2 id="customize-your-own-player">Customize your own player</h2>
<p>The example below includes every property you can set via <code>publicDetails</code>.</p>
<pre><code class="language-bash">curl --location --request POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;$ACCOUNT_ID&gt;/stream/&lt;$VIDEO_UID&gt;&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;$SECRET&gt;&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data-raw &#x27;{&#10;    &quot;publicDetails&quot;: {&#10;        &quot;title&quot;: &quot;Optional video title&quot;,&#10;        &quot;share_link&quot;: &quot;https://my-cool-share-link.cloudflare.com&quot;,&#10;        &quot;channel_link&quot;: &quot;https://www.cloudflare.com/products/cloudflare-stream/&quot;,&#10;        &quot;logo&quot;: &quot;https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Cloudflare_Logo.png/480px-Cloudflare_Logo.png&quot;&#10;    }&#10;}&#x27; | jq &quot;.result.publicDetails&quot;&#10;</code></pre>
<p>Because the <code>publicDetails</code> properties are optional, you can choose which properties to include. In the example below, only the <code>logo</code> is added to the video.</p>
<pre><code class="language-bash">curl --location --request POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;$ACCOUNT_ID&gt;/stream/&lt;$VIDEO_UID&gt;&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;$SECRET&gt;&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data-raw &#x27;{&#10;    &quot;publicDetails&quot;: {&#10;        &quot;logo&quot;: &quot;https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Cloudflare_Logo.png/480px-Cloudflare_Logo.png&quot;&#10;    }&#10;}&#x27;&#10;</code></pre>
<p>You can also pull the JSON by using the endpoint below.</p>
<p><code>https://customer-&lt;ID&gt;.cloudflarestream.com/&lt;VIDEO_ID&gt;/metadata/playerEnhancementInfo.json</code></p>
<h2 id="update-player-properties-via-the-cloudflare-dashboard">Update player properties via the Cloudflare dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Videos</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select a video from the list to edit it.</li>
<li>Select the <strong>Public Details</strong> tab.</li>
<li>From <strong>Public Details</strong>, enter information in the text fields for the properties you want to set.</li>
<li>When you are done, select <strong>Save</strong>.</li>
</ol>
