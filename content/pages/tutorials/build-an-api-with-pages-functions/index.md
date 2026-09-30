---
cp9:
  canonical: https://developers.cloudflare.com/pages/tutorials/build-an-api-with-pages-functions/
  description: This tutorial builds a full-stack Pages application using the React framework.
  full_title: Build an API for your front end using Pages Functions · Cloudflare Pages docs
  head_html: <title>Build an API for your front end using Pages Functions · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial builds a full-stack Pages application using the React framework."><link rel="canonical" href="https://developers.cloudflare.com/pages/tutorials/build-an-api-with-pages-functions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/tutorials/build-an-api-with-pages-functions/index.md"><meta property="og:title" content="Build an API for your front end using Pages Functions · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial builds a full-stack Pages application using the React framework."><meta property="og:url" content="https://developers.cloudflare.com/pages/tutorials/build-an-api-with-pages-functions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Pages"><meta name="pcx_tags" content="JavaScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/tutorials/build-an-api-with-pages-functions/#page","headline":"Build an API for your front end using Pages Functions \u00b7 Cloudflare Pages docs","description":"This tutorial builds a full-stack Pages application using the React framework.","url":"https://developers.cloudflare.com/pages/tutorials/build-an-api-with-pages-functions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript"]}</script>
  markdown: true
  noindex: false
  route: /pages/tutorials/build-an-api-with-pages-functions/
  schema: 1
---
<p>In this tutorial, you will build a full-stack Pages application. Your application will contain:</p>
<ul>
<li>A front end, built using Cloudflare Pages and the <a href="/pages/framework-guides/deploy-a-react-site/">React framework</a>.</li>
<li>A JSON API, built with <a href="/pages/functions/get-started/">Pages Functions</a>, that returns blog posts that can be retrieved and rendered in your front end.</li>
</ul>
<p>If you prefer to work with a headless CMS rather than an API to render your blog content, refer to the <a href="/pages/tutorials/build-a-blog-using-nuxt-and-sanity/">headless CMS tutorial</a>.</p>
<h2 id="video-tutorial">Video Tutorial</h2>
<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/3zTJL3M57rE" title="YouTube video" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h2 id="1-build-your-front-end"><ol>
<li>Build your front end</li>
</ol></h2>
<p>To begin, create a new Pages application using the React framework.</p>
<h3 id="create-a-new-react-project">Create a new React project</h3>
<p>In your terminal, create a new React project called <code>blog-frontend</code> using the <code>create-vite</code> command. Go into the newly created <code>blog-frontend</code> directory and start a local development server:</p>
<pre tabindex="0"><code class="language-sh">npx create-vite -t react blog-frontend&#10;cd blog-frontend&#10;npm install&#10;npm run dev&#10;</code></pre>
<h3 id="set-up-your-react-project">Set up your React project</h3>
<p>To set up your React project:</p>
<ol>
<li>Install the <a href="https://reactrouter.com/en/main/start/tutorial">React Router</a> in the root of your <code>blog-frontend</code> directory.</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i react-router-dom@6</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i react-router-dom@6" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add react-router-dom@6</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add react-router-dom@6" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add react-router-dom@6</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add react-router-dom@6" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add react-router-dom@6</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add react-router-dom@6" aria-label="Copy to clipboard">Copy</button></div></div>s
<ol start="2">
<li>Clear the contents of <code>src/App.js</code>. Copy and paste the following code to import the React Router into <code>App.js</code>, and set up a new router with two routes:</li>
</ol>
<pre tabindex="0"><code class="language-js">import { Routes, Route } from &quot;react-router-dom&quot;;&#10;&#10;import Posts from &quot;./components/posts&quot;;&#10;import Post from &quot;./components/post&quot;;&#10;&#10;function App() {&#10;	return (&#10;		&lt;Routes&gt;&#10;			&lt;Route path=&quot;/&quot; element={&lt;Posts /&gt;} /&gt;&#10;			&lt;Route path=&quot;/posts/:id&quot; element={&lt;Post /&gt;} /&gt;&#10;		&lt;/Routes&gt;&#10;	);&#10;}&#10;&#10;export default App;&#10;</code></pre>
<ol start="3">
<li>In the <code>src</code> directory, create a new folder called <code>components</code>.</li>
<li>In the <code>components</code> directory, create two files: <code>posts.js</code>, and <code>post.js</code>. These files will load the blog posts from your API, and render them.</li>
<li>Populate <code>posts.js</code> with the following code:</li>
</ol>
<pre tabindex="0"><code class="language-js">import React, { useEffect, useState } from &quot;react&quot;;&#10;import { Link } from &quot;react-router-dom&quot;;&#10;&#10;const Posts = () =&gt; {&#10;	const [posts, setPosts] = useState([]);&#10;&#10;	useEffect(() =&gt; {&#10;		const getPosts = async () =&gt; {&#10;			const resp = await fetch(&quot;/api/posts&quot;);&#10;			const postsResp = await resp.json();&#10;			setPosts(postsResp);&#10;		};&#10;&#10;		getPosts();&#10;	}, []);&#10;&#10;	return (&#10;		&lt;div&gt;&#10;			&lt;h1&gt;Posts&lt;/h1&gt;&#10;			{posts.map((post) =&gt; (&#10;				&lt;div key={post.id}&gt;&#10;					&lt;h2&gt;&#10;						&lt;Link to={`/posts/${post.id}`}&gt;{post.title}&lt;/Link&gt;&#10;					&lt;/h2&gt;&#10;				&lt;/div&gt;&#10;			))}&#10;		&lt;/div&gt;&#10;	);&#10;};&#10;&#10;export default Posts;&#10;</code></pre>
<ol start="6">
<li>Populate <code>post.js</code> with the following code:</li>
</ol>
<pre tabindex="0"><code class="language-js">import React, { useEffect, useState } from &quot;react&quot;;&#10;import { Link, useParams } from &quot;react-router-dom&quot;;&#10;&#10;const Post = () =&gt; {&#10;	const [post, setPost] = useState({});&#10;	const { id } = useParams();&#10;&#10;	useEffect(() =&gt; {&#10;		const getPost = async () =&gt; {&#10;			const resp = await fetch(`/api/post/${id}`);&#10;			const postResp = await resp.json();&#10;			setPost(postResp);&#10;		};&#10;&#10;		getPost();&#10;	}, [id]);&#10;&#10;	if (!Object.keys(post).length) return &lt;div /&gt;;&#10;&#10;	return (&#10;		&lt;div&gt;&#10;			&lt;h1&gt;{post.title}&lt;/h1&gt;&#10;			&lt;p&gt;{post.text}&lt;/p&gt;&#10;			&lt;p&gt;&#10;				&lt;em&gt;Published {new Date(post.published_at).toLocaleString()}&lt;/em&gt;&#10;			&lt;/p&gt;&#10;			&lt;p&gt;&#10;				&lt;Link to=&quot;/&quot;&gt;Go back&lt;/Link&gt;&#10;			&lt;/p&gt;&#10;		&lt;/div&gt;&#10;	);&#10;};&#10;&#10;export default Post;&#10;</code></pre>
<h2 id="2-build-your-api"><ol start="2">
<li>Build your API</li>
</ol></h2>
<p>You will now create a Pages Functions that stores your blog content and retrieves it via a JSON API.</p>
<h3 id="write-your-pages-function">Write your Pages Function</h3>
<p>To create the Pages Function that will act as your JSON API:</p>
<ol>
<li>Create a <code>functions</code> directory in your <code>blog-frontend</code> directory.</li>
<li>In <code>functions</code>, create a directory named <code>api</code>.</li>
<li>In <code>api</code>, create a <code>posts.js</code> file in the <code>api</code> directory.</li>
<li>Populate <code>posts.js</code> with the following code:</li>
</ol>
<pre tabindex="0"><code class="language-js">import posts from &quot;./post/data&quot;;&#10;&#10;export function onRequestGet() {&#10;	return Response.json(posts);&#10;}&#10;</code></pre>
<p>This code gets blog data (from <code>data.js</code>, which you will make in step 8) and returns it as a JSON response from the path <code>/api/posts</code>.</p>
<ol start="5">
<li>In the <code>api</code> directory, create a directory named <code>post</code>.</li>
<li>In the <code>post</code> directory, create a <code>data.js</code> file.</li>
<li>Populate <code>data.js</code> with the following code. This is where your blog content, blog title, and other information about your blog lives.</li>
</ol>
<pre tabindex="0"><code class="language-js">const posts = [&#10;	{&#10;		id: 1,&#10;		title: &quot;My first blog post&quot;,&#10;		text: &quot;Hello world! This is my first blog post on my new Cloudflare Workers + Pages blog.&quot;,&#10;		published_at: new Date(&quot;2020-10-23&quot;),&#10;	},&#10;	{&#10;		id: 2,&#10;		title: &quot;Updating my blog&quot;,&#10;		text: &quot;It&#x27;s my second blog post! I&#x27;m still writing and publishing using Cloudflare Workers + Pages :)&quot;,&#10;		published_at: new Date(&quot;2020-10-26&quot;),&#10;	},&#10;];&#10;&#10;export default posts;&#10;</code></pre>
<ol start="8">
<li>In the <code>post</code> directory, create an <code>[[id]].js</code> file.</li>
<li>Populate <code>[[id]].js</code> with the following code:</li>
</ol>
<pre tabindex="0"><code class="language-js">import posts from &quot;./data&quot;;&#10;&#10;export function onRequestGet(context) {&#10;	const id = context.params.id;&#10;&#10;	if (!id) {&#10;		return new Response(&quot;Not found&quot;, { status: 404 });&#10;	}&#10;&#10;	const post = posts.find((post) =&gt; post.id === Number(id));&#10;&#10;	if (!post) {&#10;		return new Response(&quot;Not found&quot;, { status: 404 });&#10;	}&#10;&#10;	return Response.json(post);&#10;}&#10;</code></pre>
<p><code>[[id]].js</code> is a <a href="/pages/functions/routing#dynamic-routes">dynamic route</a> which is used to accept a blog post <code>id</code>.</p>
<h2 id="3-deploy"><ol start="3">
<li>Deploy</li>
</ol></h2>
<p>After you have configured your Pages application and Pages Function, deploy your project using the Wrangler or via the dashboard.</p>
<h3 id="deploy-with-wrangler">Deploy with Wrangler</h3>
<p>In your <code>blog-frontend</code> directory, run <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler pages deploy</code></a> to deploy your project to the Cloudflare dashboard.</p>
<pre tabindex="0"><code class="language-sh">wrangler pages deploy blog-frontend&#10;</code></pre>
<h3 id="deploy-via-the-dashboard">Deploy via the dashboard</h3>
<p>To deploy via the Cloudflare dashboard, you will need to create a new Git repository for your Pages project and connect your Git repository to Cloudflare. This tutorial uses GitHub as its Git provider.</p>
<h4 id="create-a-new-repository">Create a new repository</h4>
<p>Create a new GitHub repository by visiting <a href="https://repo.new">repo.new</a>. After creating a new repository, prepare and push your local application to GitHub by running the following commands in your terminal:</p>
<pre tabindex="0"><code class="language-sh">git init&#10;git remote add origin https://github.com/&lt;YOUR-GH-USERNAME&gt;/&lt;REPOSITORY-NAME&gt;&#10;git add .&#10;git commit -m &quot;Initial commit&quot;&#10;git branch -M main&#10;git push -u origin main&#10;</code></pre>
<h4 id="deploy-with-cloudflare-pages">Deploy with Cloudflare Pages</h4>
<p>Deploy your application to Pages:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create application</strong> &gt; <strong>Pages</strong> &gt; <strong>Import an existing Git repository</strong>.</li>
<li>Select the new GitHub repository that you created and, in the <strong>Set up builds and deployments</strong> section, provide the following information:</li>
</ol>
<div>
<table>
<thead>
<tr>
<th>Configuration option</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Production branch</td>
<td><code>main</code></td>
</tr>
<tr>
<td>Build command</td>
<td><code>npm run build</code></td>
</tr>
<tr>
<td>Build directory</td>
<td><code>build</code></td>
</tr>
</tbody>
</table>
</div>
<p>After configuring your site, begin your first deploy. You should see Cloudflare Pages installing <code>blog-frontend</code>, your project dependencies, and building your site.</p>
<p>By completing this tutorial, you have created a full-stack Pages application.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>Learn about <a href="/pages/functions/routing">Pages Functions routing</a></li>
</ul>
