<p>In this tutorial, you will learn how to programmatically generate a custom YouTube thumbnail using Cloudflare Workers and Cloudflare Image Resizing. You may want to generate a custom YouTube thumbnail to customize the thumbnail's design, call-to-actions and images used to encourage more viewers to watch your video.</p>
<p>This tutorial will help you understand how to work with <a href="/images/">Images</a>,<a href="/images/optimization/transformations/overview/">Image Resizing</a> and <a href="/workers/">Cloudflare Workers</a>.</p>
<h2 id="before-you-start">Before you start</h2>
<p>All of the tutorials assume you have already completed the <a href="/workers/get-started/guide/">Get started guide</a>, which gets you set up with a Cloudflare Workers account, <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a>, and <a href="/workers/wrangler/install-and-update/">Wrangler</a>.</p>
<p>To follow this tutorial, make sure you have Node, Cargo, and <a href="/workers/wrangler/install-and-update/">Wrangler</a> installed on your machine.</p>
<h2 id="learning-goals">Learning goals</h2>
<p>In this tutorial, you will learn how to:</p>
<ul>
<li>Upload Images to Cloudflare with the Cloudflare dashboard or API.</li>
<li>Set up a Worker project with Wrangler.</li>
<li>Manipulate images with image transformations in your Worker.</li>
</ul>
<h2 id="upload-your-image">Upload your image</h2>
<p>To generate a custom thumbnail image, you first need to upload a background image to Cloudflare Images. This will serve as the image you use for transformations to generate the thumbnails.</p>
<p>Cloudflare Images allows you to store, resize, optimize and deliver images in a fast and secure manner. To get started, upload your images to the Cloudflare dashboard or use the Upload API.</p>
<h3 id="upload-with-the-dashboard">Upload with the dashboard</h3>
<p>To upload an image using the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Transformations</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Use <strong>Quick Upload</strong> to either drag and drop an image or click to browse and choose a file from your local files.</li>
<li>After the image is uploaded, view it using the generated URL.</li>
</ol>
<h3 id="upload-with-the-api">Upload with the API</h3>
<p>To upload your image with the <a href="/images/storage/upload-images/upload-url/">Upload via URL</a> API, refer to the example below:</p>
<pre><code class="language-sh">curl --request POST \&#10; &#45;-url https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/images/v1 \&#10; &#45;-header &#x27;Authorization: Bearer &lt;API_TOKEN&gt;&#x27; \&#10; &#45;-form &#x27;url=&lt;PATH_TO_IMAGE&gt;&#x27; \&#10; &#45;-form &#x27;metadata={&quot;key&quot;:&quot;value&quot;}&#x27; \&#10; &#45;-form &#x27;requireSignedURLs=false&#x27;&#10;</code></pre>
<ul>
<li><code>ACCOUNT_ID</code>: The current user's account id which can be found in your account settings.</li>
<li><code>API_TOKEN</code>: Needs to be generated to scoping Images permission.</li>
<li><code>PATH_TO_IMAGE</code>: Indicates the URL for the image you want to upload.</li>
</ul>
<p>You will then receive a response similar to this:</p>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;2cdc28f0-017a-49c4-9ed7-87056c83901&quot;,&#10;		&quot;filename&quot;: &quot;image.jpeg&quot;,&#10;		&quot;metadata&quot;: {&#10;			&quot;key&quot;: &quot;value&quot;&#10;		},&#10;		&quot;uploaded&quot;: &quot;2022-01-31T16:39:28.458Z&quot;,&#10;		&quot;requireSignedURLs&quot;: false,&#10;		&quot;variants&quot;: [&#10;			&quot;https://imagedelivery.net/Vi7wi5KSItxGFsWRG2Us6Q/2cdc28f0-017a-49c4-9ed7-87056c83901/public&quot;,&#10;			&quot;https://imagedelivery.net/Vi7wi5KSItxGFsWRG2Us6Q/2cdc28f0-017a-49c4-9ed7-87056c83901/thumbnail&quot;&#10;		]&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>Now that you have uploaded your image, you will use it as the background image for your video's thumbnail.</p>
<h2 id="create-a-worker-to-transform-text-to-image">Create a Worker to transform text to image</h2>
<p>After uploading your image, create a Worker that will enable you to transform text to image. This image can be used as an overlay on the background image you uploaded. Use the <a href="https://github.com/cloudflare/workers-sdk/tree/main/templates/worker-rust">rustwasm-worker-template</a>.</p>
<p>You will need the following before you begin:</p>
<ul>
<li>A recent version of <a href="https://rustup.rs/">Rust</a>.</li>
<li>Access to the <code>cargo-generate</code> subcommand:</li>
</ul>
<pre><code class="language-sh">cargo install cargo-generate&#10;</code></pre>
<p>Create a new Worker project using the <code>worker-rust</code> template:</p>
<pre><code class="language-sh">cargo generate https://github.com/cloudflare/rustwasm-worker-template&#10;</code></pre>
<p>You will now make a few changes to the files in your project directory.</p>
<ol>
<li>In the <code>lib.rs</code> file, add the following code block:</li>
</ol>
<pre><code class="language-rs">use worker::*;&#10;mod utils;&#10;&#10;&#35;[event(fetch)]&#10;pub async fn main(req: Request, env: Env, _ctx: worker::Context) -&gt; Result&lt;Response&gt; {&#10;   // Optionally, get more helpful error messages written to the console in the case of a panic.&#10;   utils::set_panic_hook();&#10;&#10;   let router = Router::new();&#10;   router&#10;       .get(&quot;/&quot;, |_, _| Response::ok(&quot;Hello from Workers!&quot;))&#10;       .run(req, env)&#10;       .await&#10;}&#10;</code></pre>
<ol start="2">
<li>Update the <code>Cargo.toml</code> file in your <code>worker-to-text</code> project directory to use <a href="https://github.com/RookAndPawn/text-to-png">text-to-png</a>, a Rust package for rendering text to PNG. Add the package as a dependency by running:</li>
</ol>
<pre><code class="language-sh">cargo add text-to-png@0.2.0&#10;</code></pre>
<ol start="3">
<li>Import the <code>text_to_png</code> library into your <code>worker-to-text</code> project's <code>lib.rs</code> file.</li>
</ol>
<pre><code class="language-rs">use text_to_png::{TextPng, TextRenderer};&#10;use worker::*;&#10;mod utils;&#10;&#10;&#35;[event(fetch)]&#10;pub async fn main(req: Request, env: Env, _ctx: worker::Context) -&gt; Result&lt;Response&gt; {&#10;   // Optionally, get more helpful error messages written to the console in the case of a panic.&#10;   utils::set_panic_hook();&#10;&#10;   let router = Router::new();&#10;   router&#10;       .get(&quot;/&quot;, |_, _| Response::ok(&quot;Hello from Workers!&quot;))&#10;       .run(req, env)&#10;       .await&#10;}&#10;</code></pre>
<ol start="4">
<li>Update <code>lib.rs</code> to create a <code>handle-slash</code> function that will activate the image transformation based on the text passed to the URL as a query parameter.</li>
</ol>
<pre><code class="language-rs">use text_to_png::{TextPng, TextRenderer};&#10;use worker::*;&#10;mod utils;&#10;&#10;&#35;[event(fetch)]&#10;pub async fn main(req: Request, env: Env, _ctx: worker::Context) -&gt; Result&lt;Response&gt; {&#10;   // Optionally, get more helpful error messages written to the console in the case of a panic.&#10;   utils::set_panic_hook();&#10;&#10;   let router = Router::new();&#10;   router&#10;       .get(&quot;/&quot;, |_, _| Response::ok(&quot;Hello from Workers!&quot;))&#10;       .run(req, env)&#10;       .await&#10;}&#10;&#10;async fn handle_slash(text: String) -&gt; Result&lt;Response&gt; {}&#10;</code></pre>
<ol start="5">
<li>In the <code>handle-slash</code> function, call the <code>TextRenderer</code> by assigning it to a renderer value, specifying that you want to use a custom font. Then, use the <code>render_text_to_png_data</code> method to transform the text into image format. In this example, the custom font (<code>Inter-Bold.ttf</code>) is located in an <code>/assets</code> folder at the root of the project which will be used for generating the thumbnail. You must update this portion of the code to point to your custom font file.</li>
</ol>
<pre><code class="language-rs">use text_to_png::{TextPng, TextRenderer};&#10;use worker::*;&#10;mod utils;&#10;&#10;&#35;[event(fetch)]&#10;pub async fn main(req: Request, env: Env, _ctx: worker::Context) -&gt; Result&lt;Response&gt; {&#10;   // Optionally, get more helpful error messages written to the console in the case of a panic.&#10;   utils::set_panic_hook();&#10;&#10;   let router = Router::new();&#10;   router&#10;       .get(&quot;/&quot;, |_, _| Response::ok(&quot;Hello from Workers!&quot;))&#10;       .run(req, env)&#10;       .await&#10;}&#10;&#10;async fn handle_slash(text: String) -&gt; Result&lt;Response&gt; {&#10;  let renderer = TextRenderer::try_new_with_ttf_font_data(include_bytes!(&quot;/assets/upstream/Inter-Bold.ttf&quot;))&#10;    .expect(&quot;Example font is definitely loadable&quot;);&#10;&#10;  let text_png: TextPng = renderer.render_text_to_png_data(text.replace(&quot;+&quot;, &quot; &quot;), 60, &quot;003682&quot;).unwrap();&#10;}&#10;</code></pre>
<ol start="6">
<li>Rewrite the <code>Router</code> function to call <code>handle_slash</code> when a query is passed in the URL, otherwise return the <code>&quot;Hello Worker!&quot;</code> as the response.</li>
</ol>
<pre><code class="language-rs">use text_to_png::{TextPng, TextRenderer};&#10;use worker::*;&#10;mod utils;&#10;&#10;&#35;[event(fetch)]&#10;pub async fn main(req: Request, env: Env, _ctx: worker::Context) -&gt; Result&lt;Response&gt; {&#10;   // Optionally, get more helpful error messages written to the console in the case of a panic.&#10;   utils::set_panic_hook();&#10;&#10;  let router = Router::new();&#10;    router&#10;      .get_async(&quot;/&quot;, |req, _| async move {&#10;        if let Some(text) = req.url()?.query() {&#10;          handle_slash(text.into()).await&#10;        } else {&#10;          handle_slash(&quot;Hello Worker!&quot;.into()).await&#10;        }&#10;      })&#10;      .run(req, env)&#10;        .await&#10;}&#10;&#10;async fn handle_slash(text: String) -&gt; Result&lt;Response&gt; {&#10;  let renderer = TextRenderer::try_new_with_ttf_font_data(include_bytes!(&quot;/assets/upstream/Inter-Bold.ttf&quot;))&#10;    .expect(&quot;Example font is definitely loadable&quot;);&#10;&#10;  let text_png: TextPng = renderer.render_text_to_png_data(text.replace(&quot;+&quot;, &quot; &quot;), 60, &quot;003682&quot;).unwrap();&#10;}&#10;</code></pre>
<ol start="7">
<li>In your <code>lib.rs</code> file, set the headers to <code>content-type: image/png</code> so that the response is correctly rendered as a PNG image.</li>
</ol>
<pre><code class="language-rs">use text_to_png::{TextPng, TextRenderer};&#10;use worker::*;&#10;mod utils;&#10;&#10;&#35;[event(fetch)]&#10;pub async fn main(req: Request, env: Env, _ctx: worker::Context) -&gt; Result&lt;Response&gt; {&#10;   // Optionally, get more helpful error messages written to the console in the case of a panic.&#10;   utils::set_panic_hook();&#10;&#10;   let router = Router::new();&#10;    router&#10;      .get_async(&quot;/&quot;, |req, _| async move {&#10;        if let Some(text) = req.url()?.query() {&#10;          handle_slash(text.into()).await&#10;        } else {&#10;          handle_slash(&quot;Hello Worker!&quot;.into()).await&#10;        }&#10;      })&#10;      .run(req, env)&#10;        .await&#10;}&#10;&#10;async fn handle_slash(text: String) -&gt; Result&lt;Response&gt; {&#10;  let renderer = TextRenderer::try_new_with_ttf_font_data(include_bytes!(&quot;/assets/upstream/Inter-Bold.ttf&quot;))&#10;    .expect(&quot;Example font is definitely loadable&quot;);&#10;&#10;  let text_png: TextPng = renderer.render_text_to_png_data(text.replace(&quot;+&quot;, &quot; &quot;), 60, &quot;003682&quot;).unwrap();&#10;&#10;  let mut headers = Headers::new();&#10;  headers.set(&quot;content-type&quot;, &quot;image/png&quot;)?;&#10;&#10;  Ok(Response::from_bytes(text_png.data)?.with_headers(headers))&#10;}&#10;</code></pre>
<p>The final <code>lib.rs</code> file should look as follows. Find the full code as an example repository on <a href="https://github.com/cloudflare/workers-sdk/tree/main/templates/examples/worker-to-text">GitHub</a>.</p>
<pre><code class="language-rs">use text_to_png::{TextPng, TextRenderer};&#10;use worker::*;&#10;&#10;mod utils;&#10;&#10;&#35;[event(fetch)]&#10;pub async fn main(req: Request, env: Env, _ctx: worker::Context) -&gt; Result&lt;Response&gt; {&#10;    // Optionally, get more helpful error messages written to the console in the case of a panic.&#10;    utils::set_panic_hook();&#10;&#10;    let router = Router::new();&#10;&#10;    router&#10;        .get_async(&quot;/&quot;, |req, _| async move {&#10;            if let Some(text) = req.url()?.query() {&#10;                handle_slash(text.into()).await&#10;            } else {&#10;                handle_slash(&quot;Hello Worker!&quot;.into()).await&#10;            }&#10;        })&#10;        .run(req, env)&#10;        .await&#10;}&#10;&#10;async fn handle_slash(text: String) -&gt; Result&lt;Response&gt; {&#10;    let renderer = TextRenderer::try_new_with_ttf_font_data(include_bytes!(&quot;/assets/upstream/Inter-Bold.ttf&quot;))&#10;    .expect(&quot;Example font is definitely loadable&quot;);&#10;&#10;    let text = if text.len() &gt; 128 {&#10;        &quot;Nope&quot;.into()&#10;    } else {&#10;        text&#10;    };&#10;&#10;    let text = urlencoding::decode(&amp;text).map_err(|_| worker::Error::BadEncoding)?;&#10;&#10;    let text_png: TextPng = renderer.render_text_to_png_data(text.replace(&quot;+&quot;, &quot; &quot;), 60, &quot;003682&quot;).unwrap();&#10;&#10;    let mut headers = Headers::new();&#10;    headers.set(&quot;content-type&quot;, &quot;image/png&quot;)?;&#10;&#10;    Ok(Response::from_bytes(text_png.data)?.with_headers(headers))&#10;}&#10;</code></pre>
<p>After you have finished updating your project, start a local server for developing your Worker by running:</p>
<pre><code class="language-sh">npx wrangler dev&#10;</code></pre>
<p>This should spin up a <code>localhost</code> instance with the image displayed:</p>
<p><img src="/assets/upstream/images/workers/tutorials/youtube-thumbnails/hello-worker.png" alt="Run wrangler dev to start a local server for your Worker" /></p>
<p>Adding a query parameter with custom text, you should receive:</p>
<p><img src="/assets/upstream/images/workers/tutorials/youtube-thumbnails/build-serverles.png" alt="Follow the instructions above to receive an output image" /></p>
<p>To deploy your Worker, open your Wrangler file and update the <code>name</code> key with your project's name. Below is an example with this tutorial's project name:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16071.md")
</div>
<p>Then run the <code>npx wrangler deploy</code> command to deploy your Worker.</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>A <code>.workers.dev</code> domain will be generated for your Worker after running <code>wrangler deploy</code>. You will use this domain in the main thumbnail image.</p>
<h2 id="create-a-worker-to-display-the-original-image">Create a Worker to display the original image</h2>
<p>Create a Worker to serve the image you uploaded to Images by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- thumbnail-image</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- thumbnail-image" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare thumbnail-image</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare thumbnail-image" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest thumbnail-image</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest thumbnail-image" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>JavaScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>To start developing your Worker, <code>cd</code> into your new project directory:</p>
<pre><code class="language-sh">cd thumbnail-image&#10;</code></pre>
<p>This will create a new Worker project named <code>thumbnail-image</code>. In the <code>src/index.js</code> file, add the following code block:</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		const url = new URL(request.url);&#10;		if (url.pathname === &quot;/original-image&quot;) {&#10;			const image = await fetch(&#10;				`https://imagedelivery.net/${env.CLOUDFLARE_ACCOUNT_HASH}/${IMAGE_ID}/public`,&#10;			);&#10;			return image;&#10;		}&#10;		return new Response(&quot;Image Resizing with a Worker&quot;);&#10;	},&#10;};&#10;</code></pre>
<p>Update <code>env.CLOUDFLARE_ACCOUNT_HASH</code> with your <a href="/fundamentals/account/find-account-and-zone-ids/">Cloudflare account ID</a>. Update <code>env.IMAGE_ID</code> with your <a href="/images/get-started/">image ID</a>.</p>
<p>Run your Worker and go to the <code>/original-image</code> route to review your image.</p>
<h2 id="add-custom-text-on-your-image">Add custom text on your image</h2>
<p>You will now use <a href="/images/optimization/transformations/overview/">Cloudflare image transformations</a>, with the <code>fetch</code> method, to add your dynamic text image as an overlay on top of your background image. Start by displaying the resulting image on a different route. Call the new route <code>/thumbnail</code>.</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		const url = new URL(request.url);&#10;		if (url.pathname === &quot;/original-image&quot;) {&#10;			const image = await fetch(&#10;				`https://imagedelivery.net/${env.CLOUDFLARE_ACCOUNT_HASH}/${IMAGE_ID}/public`,&#10;			);&#10;			return image;&#10;		}&#10;&#10;		if (url.pathname === &quot;/thumbnail&quot;) {&#10;		}&#10;&#10;		return new Response(&quot;Image Resizing with a Worker&quot;);&#10;	},&#10;};&#10;</code></pre>
<p>Next, use the <code>fetch</code> method to apply the image transformation changes on top of the background image. The overlay options are nested in <code>options.cf.image</code>.</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		const url = new URL(request.url);&#10;&#10;		if (url.pathname === &quot;/original-image&quot;) {&#10;			const image = await fetch(&#10;				`https://imagedelivery.net/${env.CLOUDFLARE_ACCOUNT_HASH}/${IMAGE_ID}/public`,&#10;			);&#10;			return image;&#10;		}&#10;&#10;		if (url.pathname === &quot;/thumbnail&quot;) {&#10;			fetch(imageURL, {&#10;				cf: {&#10;					image: {},&#10;				},&#10;			});&#10;		}&#10;&#10;		return new Response(&quot;Image Resizing with a Worker&quot;);&#10;	},&#10;};&#10;</code></pre>
<p>The <code>imageURL</code> is the URL of the image you want to use as a background image. In the <code>cf.image</code> object, specify the options you want to apply to the background image.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16070.md")
</aside>
<p>Add your background image to an assets directory on GitHub and push your changes to GitHub. Copy the URL of the image upload by performing a left click on the image and selecting the <strong>Copy Remote File Url</strong> option.</p>
<p>Replace the <code>imageURL</code> value with the copied remote URL.</p>
<pre><code class="language-js">if (url.pathname === &quot;/thumbnail&quot;) {&#10;	const imageURL =&#10;		&quot;https://github.com/lauragift21/social-image-demo/blob/1ed9044463b891561b7438ecdecbdd9da48cdb03/assets/cover.png?raw=true&quot;;&#10;	fetch(imageURL, {&#10;		cf: {&#10;			image: {},&#10;		},&#10;	});&#10;}&#10;</code></pre>
<p>Next, add overlay options in the image object. Resize the image to the preferred width and height for YouTube thumbnails and use the <a href="/images/optimization/draw-overlays/">draw</a> option to add overlay text using the deployed URL of your <code>text-to-image</code> Worker.</p>
<pre><code class="language-js">fetch(imageURL, {&#10;	cf: {&#10;		image: {&#10;			width: 1280,&#10;			height: 720,&#10;			draw: [&#10;				{&#10;					url: &quot;https://text-to-image.examples.workers.dev&quot;,&#10;					left: 40,&#10;				},&#10;			],&#10;		},&#10;	},&#10;});&#10;</code></pre>
<p>Image transformations can only be tested when you deploy your Worker.</p>
<p>To deploy your Worker, open your Wrangler file and update the <code>name</code> key with your project's name. Below is an example with this tutorial's project name:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16072.md")
</div>
<p>Deploy your Worker by running:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>The command deploys your Worker to custom <code>workers.dev</code> subdomain. Go to your <code>.workers.dev</code> subdomain and go to the <code>/thumbnail</code> route.</p>
<p>You should see the resized image with the text <code>Hello Workers!</code>.</p>
<p><img src="/assets/upstream/images/workers/tutorials/youtube-thumbnails/thumbnail.png" alt="Follow the steps above to generate your resized image." /></p>
<p>You will now make text applied dynamic. Making your text dynamic will allow you change the text and have it update on the image automatically.</p>
<p>To add dynamic text, append any text attached to the <code>/thumbnail</code> URL using query parameters and pass it down to the <code>text-to-image</code> Worker URL as a parameter.</p>
<pre><code class="language-js">for (const title of url.searchParams.values()) {&#10;	try {&#10;		const editedImage = await fetch(imageURL, {&#10;			cf: {&#10;				image: {&#10;					width: 1280,&#10;					height: 720,&#10;					draw: [&#10;						{&#10;							url: `https://text-to-image.examples.workers.dev/?${title}`,&#10;							left: 50,&#10;						},&#10;					],&#10;				},&#10;			},&#10;		});&#10;		return editedImage;&#10;	} catch (error) {&#10;		console.log(error);&#10;	}&#10;}&#10;</code></pre>
<p>By completing this tutorial, you have successfully made a custom YouTube thumbnail generator.</p>
<h2 id="related-resources">Related resources</h2>
<p>In this tutorial, you learned how to use Cloudflare Workers and Cloudflare image transformations to generate custom YouTube thumbnails. To learn more about Cloudflare Workers and image transformations, refer to <a href="/images/optimization/transformations/transform-via-workers/">Resize an image with a Worker</a>.</p>
