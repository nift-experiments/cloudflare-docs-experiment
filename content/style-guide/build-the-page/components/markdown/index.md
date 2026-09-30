<p>This component uses <a href="https://marked.js.org/"><code>marked</code></a> to render <a href="https://marked.js.org/#specifications">CommonMark and various other Markdown flavours</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14637.md")
</aside>
<pre><code class="language-mdx">import { Markdown } from &quot;~/components&quot;;&#10;&#10;&lt;Markdown text=&quot;**foo** &lt;br/&gt; [bar](/style-guide/build-the-page/components/markdown/)&quot; /&gt;&#10;</code></pre>
<h2 id="example-for-variables-in-partials">Example for variables in partials</h2>
<p>If you have a variable that needs to be formatted in any special way (for example, it needs to be a URL, an unordered list, or something else), you can wrap the variable with the markdown component in your partial file. For example:</p>
<pre><code class="language-mdx">&lt;Markdown text={props.foo} /&gt;&#10;</code></pre>
<p>Note that you need to wrap your variable in curly braces, as well as use <code>text=</code> or this will not work.</p>
<h2 id="multi-line-strings">Multi-line strings</h2>
<p>The Markdown component uses the <a href="https://www.npmjs.com/package/dedent"><code>dedent</code></a> library to remove indentation from multi-line strings.</p>
<p>This is because the <a href="https://spec.commonmark.org/0.22/#indented-code-blocks">CommonMark spec</a> treats indented text as code blocks, unlike <a href="https://mdxjs.com/docs/what-is-mdx/#:~:text=Indented%20code%20does%20not%20work%20in%20MDX%3A">MDX</a>.</p>
<pre><code class="language-mdx">import { Markdown } from &quot;~/components&quot;;&#10;&#10;&lt;&gt;&#10;  &lt;Markdown&#10;  	text={`&#10;    You need to purchase [Cloudflare WAN](https://www.cloudflare.com/magic-wan/) before you can purchase and use the Cloudflare One Appliance. The Cloudflare One Appliance can function as your primary edge device for your network, or be deployed in-line with existing network gear.&#10;&#10;  	You also need to purchase a Cloudflare One Appliance before you can start configuring your settings in the Cloudflare dashboard. After buying a Cloudflare One Appliance, the device will be registered with your Cloudflare account and show up in your Cloudflare dashboard.&#10;&#10;    Contact your account representative to learn more about purchasing options for the Cloudflare One Appliance device.&#10;    `}&#10;    inline={false}&#10;  /&gt;&#10;&lt;/&gt;&#10;</code></pre>
