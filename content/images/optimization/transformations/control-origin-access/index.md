<p>You can serve resized images without giving access to the original image. Images can be hosted on another server outside of your zone, and the true source of the image can be entirely hidden. The origin server may require authentication to disclose the original image, without needing visitors to be aware of it. Access to the full-size image may be prevented by making it impossible to manipulate resizing parameters.</p>
<p>All these behaviors are completely customizable, because they are handled by custom code of a script running <a href="/images/optimization/transformations/transform-via-workers/">on the edge in a Cloudflare Worker</a>.</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		// Here you can compute arbitrary imageURL and&#10;		// resizingOptions from any request data ...&#10;		return fetch(imageURL, { cf: { image: resizingOptions } });&#10;	},&#10;};&#10;</code></pre>
<p>This code will be run for every request, but the source code will not be accessible to website visitors. This allows the code to perform security checks and contain secrets required to access the images in a controlled manner.</p>
<p>The examples below are only suggestions, and do not have to be followed exactly. You can compute image URLs and resizing options in many other ways.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/9465.md")
</aside>
<h2 id="hiding-the-image-server">Hiding the image server</h2>
<pre><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		const resizingOptions = {&#10;			/* resizing options will be demonstrated in the next example */&#10;		};&#10;&#10;		const hiddenImageOrigin = &quot;https://secret.example.com/hidden-directory&quot;;&#10;		const requestURL = new URL(request.url);&#10;		// Append the request path such as &quot;/assets/image1.jpg&quot; to the hiddenImageOrigin.&#10;		// You could also process the path to add or remove directories, modify filenames, etc.&#10;		const imageURL = hiddenImageOrigin + requestURL.pathname;&#10;		// This will fetch image from the given URL, but to the website&#x27;s visitors this&#10;		// will appear as a response to the original request. Visitor’s browser will&#10;		// not see this URL.&#10;		return fetch(imageURL, { cf: { image: resizingOptions } });&#10;	},&#10;};&#10;</code></pre>
<h2 id="preventing-access-to-full-size-images">Preventing access to full-size images</h2>
<p>On top of protecting the original image URL, you can also validate that only certain image sizes are allowed:</p>
<pre><code class="language-js">export default {&#10;  async fetch(request, env, ctx) {&#10;  const imageURL = … // detail omitted in this example, see the previous example&#10;&#10;  const requestURL = new URL(request.url)&#10;  const width = parseInt(requestURL.searchParams.get(&quot;width&quot;), 10);&#10;  const resizingOptions = { width }&#10;  // If someone tries to manipulate your image URLs to reveal higher-resolution images,&#10;  // you can catch that and refuse to serve the request (or enforce a smaller size, etc.)&#10;  if (resizingOptions.width &gt; 1000) {&#10;    return new Response(&quot;We don&#x27;t allow viewing images larger than 1000 pixels wide&quot;, { status: 400 })&#10;  }&#10;  return fetch(imageURL, {cf:{image:resizingOptions}})&#10;},};&#10;</code></pre>
<h2 id="avoid-image-dimensions-in-urls">Avoid image dimensions in URLs</h2>
<p>You do not have to include actual pixel dimensions in the URL. You can embed sizes in the Worker script, and select the size in some other way — for example, by naming a preset in the URL:</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		const requestURL = new URL(request.url);&#10;		const resizingOptions = {};&#10;&#10;		// The regex selects the first path component after the &quot;images&quot;&#10;		// prefix, and the rest of the path (e.g. &quot;/images/first/rest&quot;)&#10;		const match = requestURL.pathname.match(/images\/([^/]+)\/(.+)/);&#10;&#10;		// You can require the first path component to be one of the&#10;		// predefined sizes only, and set actual dimensions accordingly.&#10;		switch (match &amp;&amp; match[1]) {&#10;			case &quot;small&quot;:&#10;				resizingOptions.width = 300;&#10;				break;&#10;			case &quot;medium&quot;:&#10;				resizingOptions.width = 600;&#10;				break;&#10;			case &quot;large&quot;:&#10;				resizingOptions.width = 900;&#10;				break;&#10;			default:&#10;				throw Error(&quot;invalid size&quot;);&#10;		}&#10;&#10;		// The remainder of the path may be used to locate the original&#10;		// image, e.g. here &quot;/images/small/image1.jpg&quot; would map to&#10;		// &quot;https://storage.example.com/bucket/image1.jpg&quot; resized to 300px.&#10;		const imageURL = &quot;https://storage.example.com/bucket/&quot; + match[2];&#10;		return fetch(imageURL, { cf: { image: resizingOptions } });&#10;	},&#10;};&#10;</code></pre>
<h2 id="authenticated-origin">Authenticated origin</h2>
<p>Cloudflare image transformations cache resized images to aid performance. Images stored with restricted access are generally not recommended for resizing because sharing images customized for individual visitors is unsafe. However, in cases where the customer agrees to store such images in public cache, Cloudflare supports resizing images through Workers. At the moment, this is supported on authenticated AWS, Azure, Google Cloud, SecureAuth origins and origins behind Cloudflare Access.</p>
<pre><code class="language-js">// generate signed headers (application specific)&#10;const signedHeaders = generatedSignedHeaders();&#10;&#10;fetch(private_url, {&#10;	headers: signedHeaders,&#10;	cf: {&#10;		image: {&#10;			format: &quot;auto&quot;,&#10;			&quot;origin-auth&quot;: &quot;share-publicly&quot;,&#10;		},&#10;	},&#10;});&#10;</code></pre>
<p>When using this code, the following headers are passed through to the origin, and allow your request to be successful:</p>
<ul>
<li><code>Authorization</code></li>
<li><code>Cookie</code></li>
<li><code>x-amz-content-sha256</code></li>
<li><code>x-amz-date</code></li>
<li><code>x-ms-date</code></li>
<li><code>x-ms-version</code></li>
<li><code>x-sa-date</code></li>
<li><code>cf-access-client-id</code></li>
<li><code>cf-access-client-secret</code></li>
</ul>
<p>For more information, refer to:</p>
<ul>
<li><a href="https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html">AWS docs</a></li>
<li><a href="https://docs.microsoft.com/en-us/rest/api/storageservices/List-Containers2#request-headers">Azure docs</a></li>
<li><a href="https://cloud.google.com/storage/docs/aws-simple-migration">Google Cloud docs</a></li>
<li><a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Cloudflare Zero Trust docs</a></li>
<li><a href="https://docs.secureauth.com/2104/en/authentication-api-guide.html">SecureAuth docs</a></li>
</ul>
