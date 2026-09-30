---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/how-to/og-images-astro/
  description: Use Browser Run to automatically generate Open Graph social preview images for your Astro site pages.
  full_title: Generate OG images for Astro sites · Cloudflare Browser Run docs
  head_html: <title>Generate OG images for Astro sites · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Browser Run to automatically generate Open Graph social preview images for your Astro site pages."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/how-to/og-images-astro/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/how-to/og-images-astro/index.md"><meta property="og:title" content="Generate OG images for Astro sites · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Browser Run to automatically generate Open Graph social preview images for your Astro site pages."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/how-to/og-images-astro/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Browser Run,R2,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/how-to/og-images-astro/#page","headline":"Generate OG images for Astro sites \u00b7 Cloudflare Browser Run docs","description":"Use Browser Run to automatically generate Open Graph social preview images for your Astro site pages.","url":"https://developers.cloudflare.com/browser-run/how-to/og-images-astro/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/how-to/og-images-astro/
  schema: 1
---
<p>Open Graph (OG) images are the preview images that appear when you share a link on social media. Instead of manually creating these images for every blog post, you can use Cloudflare Browser Run to automatically generate branded social preview images from an Astro template.</p>
<p>In this tutorial, you will:</p>
<ol>
<li>Create an Astro page that renders your OG image design.</li>
<li>Use Browser Run to screenshot that page as a PNG.</li>
<li>Serve the generated images to social media crawlers.</li>
</ol>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A Cloudflare account with <a href="/browser-run/get-started/#quick-actions">Browser Run enabled</a></li>
<li>An Astro site deployed on <a href="/workers/framework-guides/web-apps/astro/">Cloudflare Workers</a></li>
<li>Basic familiarity with Astro and Cloudflare Workers</li>
</ul>
<h2 id="1-create-the-og-image-template"><ol>
<li>Create the OG image template</li>
</ol></h2>
<p>Create an Astro route that renders your OG image design. This page serves as the source of truth for your image layout.</p>
<p>Create <code>src/pages/social-card.astro</code>:</p>
<pre tabindex="0"><code class="language-astro">&#45;--&#10;export const prerender = false;&#10;&#10;const title = Astro.url.searchParams.get(&quot;title&quot;) || &quot;Untitled&quot;;&#10;const image = Astro.url.searchParams.get(&quot;image&quot;);&#10;const author = Astro.url.searchParams.get(&quot;author&quot;);&#10;&#45;--&#10;&#10;&lt;html&gt;&#10;	&lt;head&gt;&#10;		&lt;meta charset=&quot;utf-8&quot; /&gt;&#10;		&lt;style&gt;&#10;			&#42; {&#10;				margin: 0;&#10;				padding: 0;&#10;				box-sizing: border-box;&#10;			}&#10;			body {&#10;				width: 1200px;&#10;				height: 630px;&#10;				display: flex;&#10;				flex-direction: column;&#10;				justify-content: flex-end;&#10;				padding: 60px;&#10;				font-family: system-ui, sans-serif;&#10;				background: linear-gradient(135deg, #f38020 0%, #f9a825 100%);&#10;				color: white;&#10;			}&#10;			.title {&#10;				font-size: 64px;&#10;				font-weight: bold;&#10;				line-height: 1.1;&#10;				margin-bottom: 24px;&#10;			}&#10;			.author {&#10;				font-size: 24px;&#10;				opacity: 0.9;&#10;			}&#10;			.logo {&#10;				position: absolute;&#10;				top: 60px;&#10;				left: 60px;&#10;				height: 40px;&#10;			}&#10;		&lt;/style&gt;&#10;	&lt;/head&gt;&#10;	&lt;body&gt;&#10;		&lt;img class=&quot;logo&quot; src=&quot;/your-logo.png&quot; alt=&quot;Your logo&quot; /&gt;&#10;		&lt;h1 class=&quot;title&quot;&gt;{title}&lt;/h1&gt;&#10;		{author &amp;&amp; &lt;p class=&quot;author&quot;&gt;By {author}&lt;/p&gt;}&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<p>Start your Astro development server to test the template:</p>
<pre tabindex="0"><code class="language-sh">npm run dev&#10;</code></pre>
<p>Test locally by visiting <code>http://localhost:4321/social-card?title=My%20Blog%20Post&amp;author=Omar</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3676.md")
</aside>
<p>Before proceeding, deploy your site to ensure the <code>/social-card</code> route is live:</p>
<pre tabindex="0"><code class="language-sh">&#35; For Cloudflare Workers&#10;npx wrangler deploy&#10;</code></pre>
<p>Update the <code>BASE_URL</code> in the script below to match your deployed site URL.</p>
<h2 id="2-generate-og-images-at-build-time"><ol start="2">
<li>Generate OG images at build time</li>
</ol></h2>
<p>Generate all OG images during the Astro build process using Cloudflare Browser Run Quick Actions.</p>
<p>Create <code>scripts/generate-social-cards.ts</code>:</p>
<pre tabindex="0"><code class="language-ts">import {&#10;	existsSync,&#10;	mkdirSync,&#10;	readdirSync,&#10;	readFileSync,&#10;	writeFileSync,&#10;} from &quot;fs&quot;;&#10;import { join } from &quot;path&quot;;&#10;&#10;// Configuration&#10;const BASE_URL = &quot;https://your-site.com&quot;; // Your deployed site URL&#10;const CF_API = &quot;https://api.cloudflare.com/client/v4/accounts&quot;;&#10;const OUTPUT_DIR = &quot;public/social-cards&quot;; // Output directory for generated images&#10;const POSTS_DIR = &quot;src/data/posts&quot;; // Directory containing your markdown posts (adjust to match your project)&#10;&#10;interface Post {&#10;	slug: string;&#10;	title: string;&#10;	author?: string;&#10;}&#10;&#10;/** Extract a frontmatter field value from raw markdown content. */&#10;function getFrontmatterField(content: string, field: string): string | null {&#10;	const match = content.match(new RegExp(`^${field}:\\s*&quot;?([^&quot;\\n]+)&quot;?`, &quot;m&quot;));&#10;	return match ? match[1].trim() : null;&#10;}&#10;&#10;/**&#10; &#42; Read all post files and return { slug, title, author }[].&#10; &#42; This function scans the POSTS_DIR for markdown files, extracts frontmatter&#10; &#42; fields (slug, title, author), and returns an array of post objects.&#10; &#42; Falls back to filename for slug and slug for title if frontmatter is missing.&#10; &#42;/&#10;function readPosts(): Post[] {&#10;	if (!existsSync(POSTS_DIR)) return [];&#10;	const files = readdirSync(POSTS_DIR).filter((f) =&gt; f.endsWith(&quot;.md&quot;));&#10;	return files.map((file) =&gt; {&#10;		const raw = readFileSync(join(POSTS_DIR, file), &quot;utf-8&quot;);&#10;		const slug = getFrontmatterField(raw, &quot;slug&quot;) ?? file.replace(/\.md$/, &quot;&quot;);&#10;		const title = getFrontmatterField(raw, &quot;title&quot;) ?? slug;&#10;		const author = getFrontmatterField(raw, &quot;author&quot;) ?? undefined;&#10;		return { slug, title, author };&#10;	});&#10;}&#10;&#10;/**&#10; &#42; Capture a screenshot using Cloudflare Browser Run Quick Actions&#10; &#42;/&#10;async function captureScreenshot(&#10;	accountId: string,&#10;	apiToken: string,&#10;	pageUrl: string,&#10;): Promise&lt;ArrayBuffer&gt; {&#10;	const endpoint = `${CF_API}/${accountId}/browser-rendering/screenshot`;&#10;&#10;	const res = await fetch(endpoint, {&#10;		method: &quot;POST&quot;,&#10;		headers: {&#10;			Authorization: `Bearer ${apiToken}`,&#10;			&quot;Content-Type&quot;: &quot;application/json&quot;,&#10;		},&#10;		body: JSON.stringify({&#10;			url: pageUrl,&#10;			viewport: { width: 1200, height: 630 }, // Standard OG image size&#10;			gotoOptions: { waitUntil: &quot;networkidle0&quot; }, // Wait for page to fully load&#10;		}),&#10;	});&#10;&#10;	if (!res.ok) {&#10;		const text = await res.text();&#10;		throw new Error(`Screenshot API returned ${res.status}: ${text}`);&#10;	}&#10;&#10;	return res.arrayBuffer();&#10;}&#10;&#10;async function main() {&#10;	// Read credentials from environment variables&#10;	const accountId = process.env.CF_ACCOUNT_ID;&#10;	const apiToken = process.env.CF_API_TOKEN;&#10;&#10;	if (!accountId || !apiToken) {&#10;		console.error(&quot;Error: CF_ACCOUNT_ID and CF_API_TOKEN required&quot;);&#10;		process.exit(1);&#10;	}&#10;&#10;	// Check if --force flag is passed to regenerate all images&#10;	const force = process.argv.includes(&quot;--force&quot;);&#10;&#10;	// Read posts from markdown files&#10;	const posts = readPosts();&#10;&#10;	if (posts.length === 0) {&#10;		console.log(&quot;No posts found. Check your POSTS_DIR path.&quot;);&#10;		process.exit(0);&#10;	}&#10;&#10;	console.log(`Found ${posts.length} posts to process\n`);&#10;&#10;	// Ensure output directory exists&#10;	mkdirSync(OUTPUT_DIR, { recursive: true });&#10;&#10;	let generated = 0;&#10;	let skipped = 0;&#10;&#10;	// Generate social card for each post&#10;	for (let i = 0; i &lt; posts.length; i++) {&#10;		const post = posts[i];&#10;		const outPath = join(OUTPUT_DIR, `${post.slug}.png`);&#10;		const label = `[${i + 1}/${posts.length}]`;&#10;&#10;		// Skip if file exists and --force flag not set&#10;		if (!force &amp;&amp; existsSync(outPath)) {&#10;			console.log(`${label} ${post.slug}.png — skipped (exists)`);&#10;			skipped++;&#10;			continue;&#10;		}&#10;&#10;		// Build URL with query parameters for the OG template&#10;		const params = new URLSearchParams({&#10;			title: post.title,&#10;			author: post.author || &quot;&quot;,&#10;		});&#10;		const url = `${BASE_URL}/social-card?${params}`;&#10;&#10;		try {&#10;			// Capture screenshot and save to file&#10;			const png = await captureScreenshot(accountId, apiToken, url);&#10;			writeFileSync(outPath, Buffer.from(png));&#10;			console.log(`${label} ${post.slug}.png — done`);&#10;			generated++;&#10;		} catch (err) {&#10;			console.error(`${label} ${post.slug}.png — failed:`, err);&#10;		}&#10;&#10;		// Rate limiting: small delay between requests&#10;		if (i &lt; posts.length - 1) {&#10;			await new Promise((resolve) =&gt; setTimeout(resolve, 200));&#10;		}&#10;	}&#10;&#10;	console.log(`\nDone. Generated: ${generated}, Skipped: ${skipped}`);&#10;}&#10;&#10;main();&#10;</code></pre>
<p>Set your Cloudflare credentials as environment variables:</p>
<pre tabindex="0"><code class="language-sh">export CF_ACCOUNT_ID=your_account_id&#10;export CF_API_TOKEN=your_api_token&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3675.md")
</aside>
<p>Run the script to generate images:</p>
<pre tabindex="0"><code class="language-sh">&#35; Generate new images only&#10;bun scripts/generate-social-cards.ts&#10;&#10;&#35; Regenerate all images&#10;bun scripts/generate-social-cards.ts --force&#10;</code></pre>
<p>Optionally, add to your build script in <code>package.json</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;scripts&quot;: {&#10;		&quot;build&quot;: &quot;bun scripts/generate-social-cards.ts &amp;&amp; astro build&quot;&#10;	}&#10;}&#10;</code></pre>
<h2 id="3-add-og-meta-tags-to-your-pages"><ol start="3">
<li>Add OG meta tags to your pages</li>
</ol></h2>
<p>Update your blog post layout to reference the generated images:</p>
<pre tabindex="0"><code class="language-astro">&#45;--&#10;// src/layouts/BlogPost.astro&#10;const { title, slug, author } = Astro.props;&#10;const ogImageUrl = `/social-cards/${slug}.png`;&#10;&#45;--&#10;&#10;&lt;html&gt;&#10;	&lt;head&gt;&#10;		&lt;meta property=&quot;og:title&quot; content={title} /&gt;&#10;		&lt;meta property=&quot;og:image&quot; content={ogImageUrl} /&gt;&#10;		&lt;meta property=&quot;og:image:width&quot; content=&quot;1200&quot; /&gt;&#10;		&lt;meta property=&quot;og:image:height&quot; content=&quot;630&quot; /&gt;&#10;		&lt;meta name=&quot;twitter:card&quot; content=&quot;summary_large_image&quot; /&gt;&#10;		&lt;meta name=&quot;twitter:image&quot; content={ogImageUrl} /&gt;&#10;	&lt;/head&gt;&#10;	&lt;body&gt;&#10;		&lt;slot /&gt;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<h2 id="4-test-your-og-images"><ol start="4">
<li>Test your OG images</li>
</ol></h2>
<p>Before testing, make sure to deploy your site with the newly generated social card images:</p>
<pre tabindex="0"><code class="language-sh">&#35; For Cloudflare Workers&#10;npx wrangler deploy&#10;</code></pre>
<p>Use these tools to verify your OG images render correctly:</p>
<ul>
<li><a href="https://developers.facebook.com/tools/debug/">Facebook Sharing Debugger</a></li>
<li><a href="https://cards-dev.twitter.com/validator">Twitter Card Validator</a></li>
<li><a href="https://www.linkedin.com/post-inspector/">LinkedIn Post Inspector</a></li>
</ul>
<h2 id="customize-the-template">Customize the template</h2>
<h3 id="add-a-background-image">Add a background image</h3>
<pre tabindex="0"><code class="language-astro">&#45;--&#10;const title = Astro.url.searchParams.get(&quot;title&quot;) || &quot;Untitled&quot;;&#10;const image = Astro.url.searchParams.get(&quot;image&quot;);&#10;&#45;--&#10;&#10;&lt;body style={image ? `background-image: url(${image})` : undefined}&gt;&#10;	&lt;!-- content --&gt;&#10;&lt;/body&gt;&#10;</code></pre>
<h3 id="use-custom-fonts">Use custom fonts</h3>
<pre tabindex="0"><code class="language-astro">&lt;head&gt;&#10;	&lt;link&#10;		href=&quot;https://fonts.googleapis.com/css2?family=Inter:wght@700&amp;display=swap&quot;&#10;		rel=&quot;stylesheet&quot;&#10;	/&gt;&#10;	&lt;style&gt;&#10;		body {&#10;			font-family: &quot;Inter&quot;, sans-serif;&#10;		}&#10;	&lt;/style&gt;&#10;&lt;/head&gt;&#10;</code></pre>
<h3 id="add-tailwind-css">Add Tailwind CSS</h3>
<p>If your Astro site uses Tailwind, you can use it in your OG template:</p>
<pre tabindex="0"><code class="language-astro">&#45;--&#10;import &quot;../styles/global.css&quot;;&#10;&#45;--&#10;&#10;&lt;body&#10;	class=&quot;flex h-[630px] w-[1200px] flex-col justify-end bg-gradient-to-br from-orange-500 to-amber-500 p-16 text-white&quot;&#10;&gt;&#10;	&lt;h1 class=&quot;mb-6 text-6xl leading-tight font-bold&quot;&gt;{title}&lt;/h1&gt;&#10;&lt;/body&gt;&#10;</code></pre>
<h2 id="performance-considerations">Performance considerations</h2>
<h3 id="image-optimization">Image optimization</h3>
<p>Consider running generated images through Cloudflare Images or Image Resizing for additional optimization:</p>
<pre tabindex="0"><code class="language-ts">const optimizedUrl = `https://your-domain.com/cdn-cgi/image/width=1200,format=auto/social-cards/${slug}.png`;&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p>Your Astro site now automatically generates OG images using Browser Run. When you share a link on social media, crawlers will fetch the generated image from the static path.</p>
<p>From here, you can:</p>
<ul>
<li>Customize your template with <a href="#use-custom-fonts">custom fonts</a>, <a href="#add-tailwind-css">Tailwind CSS</a>, or <a href="#add-a-background-image">background images</a>.</li>
<li>Add cache invalidation logic to regenerate images when post content changes.</li>
<li>Use <a href="/images/">Cloudflare Images</a> or <a href="/images/optimization/transformations/overview/">Image Resizing</a> for additional optimization.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/browser-run/">Browser Run documentation</a></li>
<li><a href="/r2/">R2 storage</a></li>
<li><a href="/images/">Cloudflare Images</a></li>
</ul>
