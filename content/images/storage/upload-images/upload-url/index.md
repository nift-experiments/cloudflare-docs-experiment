<p>Before you upload an image, check the list of <a href="/images/get-started/limits">supported formats and dimensions</a> to confirm your image will be accepted.</p>
<p>You can use the Images API to use a URL of an image instead of uploading the data.</p>
<p>Make a <code>POST</code> request using the example below as reference. Keep in mind that the <code>--form 'file=&lt;FILE&gt;'</code> and <code>--form 'url=&lt;URL&gt;'</code> fields are mutually exclusive.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9477.md")
</aside>
<pre><code class="language-bash">curl --request POST \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1 \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-form &#x27;url=https://[user:password@]example.com/&lt;PATH_TO_IMAGE&gt;&#x27; \&#10;&#45;-form &#x27;metadata={&quot;key&quot;:&quot;value&quot;}&#x27; \&#10;&#45;-form &#x27;requireSignedURLs=false&#x27;&#10;</code></pre>
<p>After successfully uploading the image, you will receive a response similar to the example below.</p>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;2cdc28f0-017a-49c4-9ed7-87056c83901&quot;,&#10;		&quot;filename&quot;: &quot;image.jpeg&quot;,&#10;		&quot;metadata&quot;: {&#10;			&quot;key&quot;: &quot;value&quot;&#10;		},&#10;		&quot;uploaded&quot;: &quot;2022-01-31T16:39:28.458Z&quot;,&#10;		&quot;requireSignedURLs&quot;: false,&#10;		&quot;variants&quot;: [&#10;			&quot;https://imagedelivery.net/Vi7wi5KSItxGFsWRG2Us6Q/2cdc28f0-017a-49c4-9ed7-87056c83901/public&quot;,&#10;			&quot;https://imagedelivery.net/Vi7wi5KSItxGFsWRG2Us6Q/2cdc28f0-017a-49c4-9ed7-87056c83901/thumbnail&quot;&#10;		]&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>If your origin server returns an error while fetching the images, the API response will return a 4xx error.</p>
