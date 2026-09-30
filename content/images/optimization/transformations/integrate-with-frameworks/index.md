<h2 id="next-js">Next.js</h2>
<p>Image transformations can be used automatically with the Next.js <a href="https://nextjs.org/docs/api-reference/next/image"><code>&lt;Image /&gt;</code> component</a>.</p>
<p>To use image transformations, define a global image loader or multiple custom loaders for each <code>&lt;Image /&gt;</code> component.</p>
<p>Next.js will request the image with the correct parameters for width and quality.</p>
<p>Image transformations will be responsible for caching and serving an optimal format to the client.</p>
<h3 id="global-loader">Global Loader</h3>
<p>To use Images with <strong>all</strong> your app's images, define a global <a href="https://nextjs.org/docs/pages/api-reference/components/image#loaderfile">loaderFile</a> for your app.</p>
<p>Add the following settings to the <strong>next.config.js</strong> file located at the root of your Next.js application.</p>
<pre><code class="language-ts">module.exports = {&#10;	images: {&#10;		loader: &quot;custom&quot;,&#10;		loaderFile: &quot;./imageLoader.ts&quot;,&#10;	},&#10;};&#10;</code></pre>
<p>Next, create the <code>imageLoader.ts</code> file in the specified path (relative to the root of your Next.js application).</p>
<pre><code class="language-ts">import type { ImageLoaderProps } from &quot;next/image&quot;;&#10;&#10;const normalizeSrc = (src: string) =&gt; {&#10;	return src.startsWith(&quot;/&quot;) ? src.slice(1) : src;&#10;};&#10;&#10;export default function cloudflareLoader({&#10;	src,&#10;	width,&#10;	quality,&#10;}: ImageLoaderProps) {&#10;	const params = [`width=${width}`];&#10;	if (quality) {&#10;		params.push(`quality=${quality}`);&#10;	}&#10;	if (process.env.NODE_ENV === &quot;development&quot;) {&#10;		return `${src}?${params.join(&quot;&amp;&quot;)}`;&#10;	}&#10;	return `/cdn-cgi/image/${params.join(&quot;,&quot;)}/${normalizeSrc(src)}`;&#10;}&#10;</code></pre>
<h3 id="custom-loaders">Custom Loaders</h3>
<p>Alternatively, define a loader for each <code>&lt;Image /&gt;</code> component.</p>
<pre><code class="language-js">import Image from &quot;next/image&quot;;&#10;&#10;const normalizeSrc = (src) =&gt; {&#10;	return src.startsWith(&quot;/&quot;) ? src.slice(1) : src;&#10;};&#10;&#10;const cloudflareLoader = ({ src, width, quality }) =&gt; {&#10;	const params = [`width=${width}`];&#10;	if (quality) {&#10;		params.push(`quality=${quality}`);&#10;	}&#10;	if (process.env.NODE_ENV === &quot;development&quot;) {&#10;		return `${src}?${params.join(&quot;&amp;&quot;)}`;&#10;	}&#10;	return `/cdn-cgi/image/${params.join(&quot;,&quot;)}/${normalizeSrc(src)}`;&#10;};&#10;&#10;const MyImage = (props) =&gt; {&#10;	return (&#10;		&lt;Image&#10;			loader={cloudflareLoader}&#10;			src=&quot;/me.png&quot;&#10;			alt=&quot;Picture of the author&quot;&#10;			width={500}&#10;			height={500}&#10;			{...props}&#10;		/&gt;&#10;	);&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9463.md")
</aside>
