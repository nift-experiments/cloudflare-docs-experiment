<p>The <code>@vercel/og</code> Pages Plugin is a middleware which renders social images for webpages. It also includes an API to create arbitrary images.</p>
<p>As the name suggests, it is powered by <a href="https://vercel.com/docs/concepts/functions/edge-functions/og-image-generation"><code>@vercel/og</code></a>. This plugin and its underlying <a href="https://github.com/vercel/satori">Satori</a> library was created by the Vercel team.</p>
<h2 id="install">Install</h2>
<p>To install the <code>@vercel/og</code> Pages Plugin, run:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/pages-plugin-vercel-og</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/pages-plugin-vercel-og" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/pages-plugin-vercel-og</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/pages-plugin-vercel-og" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/pages-plugin-vercel-og</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/pages-plugin-vercel-og" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/pages-plugin-vercel-og</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/pages-plugin-vercel-og" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="use">Use</h2>
<pre><code class="language-typescript">import React from &quot;react&quot;;&#10;import vercelOGPagesPlugin from &quot;@cloudflare/pages-plugin-vercel-og&quot;;&#10;&#10;interface Props {&#10;	ogTitle: string;&#10;}&#10;&#10;export const onRequest = vercelOGPagesPlugin&lt;Props&gt;({&#10;	imagePathSuffix: &quot;/social-image.png&quot;,&#10;	component: ({ ogTitle, pathname }) =&gt; {&#10;		return &lt;div style={{ display: &quot;flex&quot; }}&gt;{ogTitle}&lt;/div&gt;;&#10;	},&#10;	extractors: {&#10;		on: {&#10;			&#x27;meta[property=&quot;og:title&quot;]&#x27;: (props) =&gt; ({&#10;				element(element) {&#10;					props.ogTitle = element.getAttribute(&quot;content&quot;);&#10;				},&#10;			}),&#10;		},&#10;	},&#10;	autoInject: {&#10;		openGraph: true,&#10;	},&#10;});&#10;</code></pre>
<p>The Plugin takes an object with six properties:</p>
<ul>
<li>
<p><code>imagePathSuffix</code>: the path suffix to make the generate image available at. For example, if you mount this Plugin at <code>functions/blog/_middleware.ts</code>, set the <code>imagePathSuffix</code> as <code>/social-image.png</code> and have a <code>/blog/hello-world</code> page, the image will be available at <code>/blog/hello-world/social-image.png</code>.</p>
</li>
<li>
<p><code>component</code>: the React component that will be used to render the image. By default, the React component is given a <code>pathname</code> property equal to the pathname of the underlying webpage (for example, <code>/blog/hello-world</code>), but more dynamic properties can be provided with the <code>extractors</code> option.</p>
</li>
<li>
<p><code>extractors</code>: an optional object with two optional properties: <code>on</code> and <code>onDocument</code>. These properties can be set to a function which takes an object and returns a <a href="/workers/runtime-apis/html-rewriter/#element-handlers"><code>HTMLRewriter</code> element handler</a> or <a href="/workers/runtime-apis/html-rewriter/#document-handlers">document handler</a> respectively. The object parameter can be mutated in order to provide the React component with additional properties. In the example above, you will use an element handler to extract the <code>og:title</code> meta tag from the webpage and pass that to the React component as the <code>ogTitle</code> property. This is the primary mechanism you will use to create dynamic images which use values from the underlying webpage.</p>
</li>
<li>
<p><code>options</code>: <a href="https://vercel.com/docs/concepts/functions/edge-functions/og-image-generation/og-image-api">an optional object which is given directly to the <code>@vercel/og</code> library</a>.</p>
</li>
<li>
<p><code>onError</code>: an optional function which returns a <code>Response</code> or a promise of a <code>Response</code>. This function is called when a request is made to the <code>imagePathSuffix</code> and <code>extractors</code> are provided but the underlying webpage is not valid HTML. Defaults to returning a <code>404</code> response.</p>
</li>
<li>
<p><code>autoInject</code>: an optional object with an optional property: <code>openGraph</code>. If set to <code>true</code>, the Plugin will automatically set the <code>og:image</code>, <code>og:image:height</code> and <code>og:image:width</code> meta tags on the underlying webpage.</p>
</li>
</ul>
<h3 id="generate-arbitrary-images">Generate arbitrary images</h3>
<p>Use this Plugin's API to generate arbitrary images, not just as middleware.</p>
<p>For example, the below code will generate an image saying &quot;Hello, world!&quot; which is available at <code>/greet</code>.</p>
<pre><code class="language-typescript">import React from &quot;react&quot;;&#10;import { ImageResponse } from &quot;@cloudflare/pages-plugin-vercel-og/api&quot;;&#10;&#10;export const onRequest: PagesFunction = async () =&gt; {&#10;  return new ImageResponse(&#10;    &lt;div style={{ display: &quot;flex&quot; }}&gt;Hello, world!&lt;/div&gt;,&#10;    {&#10;      width: 1200,&#10;      height: 630,&#10;    }&#10;  );&#10;};&#10;</code></pre>
<p>This is the same API that the underlying <a href="https://vercel.com/docs/concepts/functions/edge-functions/og-image-generation/og-image-api"><code>@vercel/og</code> library</a> offers.</p>
