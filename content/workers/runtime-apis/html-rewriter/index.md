---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/html-rewriter/
  description: Build comprehensive and expressive HTML parsers inside of a Worker application.
  full_title: HTMLRewriter · Cloudflare Workers docs
  head_html: <title>HTMLRewriter · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Build comprehensive and expressive HTML parsers inside of a Worker application."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/html-rewriter/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/html-rewriter/index.md"><meta property="og:title" content="HTMLRewriter · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build comprehensive and expressive HTML parsers inside of a Worker application."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/html-rewriter/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/html-rewriter/#page","headline":"HTMLRewriter \u00b7 Cloudflare Workers docs","description":"Build comprehensive and expressive HTML parsers inside of a Worker application.","url":"https://developers.cloudflare.com/workers/runtime-apis/html-rewriter/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/html-rewriter/
  schema: 1
---
<h2 id="background">Background</h2>
<p>The <code>HTMLRewriter</code> class allows developers to build comprehensive and expressive HTML parsers inside of a Cloudflare Workers application. It can be thought of as a jQuery-like experience directly inside of your Workers application. Leaning on a powerful JavaScript API to parse and transform HTML, <code>HTMLRewriter</code> allows developers to build deeply functional applications.</p>
<p>The <code>HTMLRewriter</code> class should be instantiated once in your Workers script, with a number of handlers attached using the <code>on</code> and <code>onDocument</code> functions.</p>
<hr />
<h2 id="constructor">Constructor</h2>
<pre tabindex="0"><code class="language-js">new HTMLRewriter()&#10;	.on(&quot;*&quot;, new ElementHandler())&#10;	.onDocument(new DocumentHandler());&#10;</code></pre>
<hr />
<h2 id="global-types">Global types</h2>
<p>Throughout the <code>HTMLRewriter</code> API, there are a few consistent types that many properties and methods use:</p>
<ul>
<li>
<p><code>Content</code> string | Response | ReadableStream</p>
<ul>
<li>Content inserted in the output stream should be a string, <a href="/workers/runtime-apis/response/"><code>Response</code></a>, or <a href="/workers/runtime-apis/streams/readablestream/"><code>ReadableStream</code></a>.</li>
</ul>
</li>
<li>
<p><code>ContentOptions</code> Object</p>
<ul>
<li><code>{ html: Boolean }</code> Controls the way the HTMLRewriter treats inserted content. If the <code>html</code> boolean is set to true, content is treated as raw HTML. If the <code>html</code> boolean is set to false or not provided, content will be treated as text and proper HTML escaping will be applied to it.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="handlers">Handlers</h2>
<p>There are two handler types that can be used with <code>HTMLRewriter</code>: element handlers and document handlers.</p>
<h3 id="element-handlers">Element Handlers</h3>
<p>An element handler responds to any incoming element, when attached using the <code>.on</code> function of an <code>HTMLRewriter</code> instance. The element handler should respond to <code>element</code>, <code>comments</code>, and <code>text</code>. The example processes <code>div</code> elements with an <code>ElementHandler</code> class.</p>
<pre tabindex="0"><code class="language-js">class ElementHandler {&#10;	element(element) {&#10;		// An incoming element, such as `div`&#10;		console.log(`Incoming element: ${element.tagName}`);&#10;	}&#10;&#10;	comments(comment) {&#10;		// An incoming comment&#10;	}&#10;&#10;	text(text) {&#10;		// An incoming piece of text&#10;	}&#10;}&#10;&#10;async function handleRequest(req) {&#10;	const res = await fetch(req);&#10;&#10;	return new HTMLRewriter().on(&quot;div&quot;, new ElementHandler()).transform(res);&#10;}&#10;</code></pre>
<h3 id="document-handlers">Document Handlers</h3>
<p>A document handler represents the incoming HTML document. A number of functions can be defined on a document handler to query and manipulate a document’s <code>doctype</code>, <code>comments</code>, <code>text</code>, and <code>end</code>. Unlike an element handler, a document handler’s <code>doctype</code>, <code>comments</code>, <code>text</code>, and <code>end</code> functions are not scoped by a particular selector. A document handler's functions are called for all the content on the page including the content outside of the top-level HTML tag:</p>
<pre tabindex="0"><code class="language-js">class DocumentHandler {&#10;	doctype(doctype) {&#10;		// An incoming doctype, such as &lt;!DOCTYPE html&gt;&#10;	}&#10;&#10;	comments(comment) {&#10;		// An incoming comment&#10;	}&#10;&#10;	text(text) {&#10;		// An incoming piece of text&#10;	}&#10;&#10;	end(end) {&#10;		// The end of the document&#10;	}&#10;}&#10;</code></pre>
<h4 id="async-handlers">Async Handlers</h4>
<p>All functions defined on both element and document handlers can return either <code>void</code> or a <code>Promise&lt;void&gt;</code>. Making your handler function <code>async</code> allows you to access external resources such as an API via fetch, Workers KV, Durable Objects, or the cache.</p>
<pre tabindex="0"><code class="language-js">class UserElementHandler {&#10;	async element(element) {&#10;		let response = await fetch(new Request(&quot;/user&quot;));&#10;&#10;		// fill in user info using response&#10;	}&#10;}&#10;&#10;async function handleRequest(req) {&#10;	const res = await fetch(req);&#10;&#10;	// run the user element handler via HTMLRewriter on a div with ID `user_info`&#10;	return new HTMLRewriter()&#10;		.on(&quot;div#user_info&quot;, new UserElementHandler())&#10;		.transform(res);&#10;}&#10;</code></pre>
<h3 id="element">Element</h3>
<p>The <code>element</code> argument, used only in element handlers, is a representation of a DOM element. A number of methods exist on an element to query and manipulate it:</p>
<h4 id="properties">Properties</h4>
<ul>
<li>
<p><code>tagName</code> string</p>
<ul>
<li>The name of the tag, such as <code>&quot;h1&quot;</code> or <code>&quot;div&quot;</code>. This property can be assigned different values, to modify an element’s tag.</li>
</ul>
</li>
<li>
<p><code>attributes</code> Iterator read-only</p>
<ul>
<li>A <code>[name, value]</code> pair of the tag’s attributes.</li>
</ul>
</li>
<li>
<p><code>removed</code> boolean</p>
<ul>
<li>Indicates whether the element has been removed or replaced by one of the previous handlers.</li>
</ul>
</li>
<li>
<p><code>namespaceURI</code> string</p>
<ul>
<li>Represents the <a href="https://infra.spec.whatwg.org/#namespaces">namespace URI</a> of an element.</li>
</ul>
</li>
</ul>
<h4 id="methods">Methods</h4>
<ul>
<li>
<p><code>getAttribute(name <span class="nb-type">string</span>)</code> : <span class="nb-type">string | null</span></p>
<ul>
<li>Returns the value for a given attribute name on the element, or <code>null</code> if it is not found.</li>
</ul>
</li>
<li>
<p><code>hasAttribute(name <span class="nb-type">string</span>)</code> : <span class="nb-type">boolean</span></p>
<ul>
<li>Returns a boolean indicating whether an attribute exists on the element.</li>
</ul>
</li>
<li>
<p><code>setAttribute(name <span class="nb-type">string</span>, value <span class="nb-type">string</span>)</code> : <span class="nb-type">Element</span></p>
<ul>
<li>Sets an attribute to a provided value, creating the attribute if it does not exist.</li>
</ul>
</li>
<li>
<p><code>removeAttribute(name <span class="nb-type">string</span>)</code> : <span class="nb-type">Element</span></p>
<ul>
<li>Removes the attribute.</li>
</ul>
</li>
<li>
<p><code>before(content <span class="nb-type">Content</span>, contentOptions <span class="nb-type">ContentOptions</span> <span class="nb-metainfo">optional</span>)</code> : <span class="nb-type">Element</span></p>
<ul>
<li>Inserts content before the element.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="content-and-contentoptions">Content and ContentOptions</h3>
@markup("md", "content/.markup/bodies/16142.md")
</aside>
<ul>
<li>
<p><code>after(content <span class="nb-type">Content</span>, contentOptions <span class="nb-type">ContentOptions</span> <span class="nb-metainfo">optional</span>)</code> : <span class="nb-type">Element</span></p>
<ul>
<li>Inserts content right after the element.</li>
</ul>
</li>
<li>
<p><code>prepend(content <span class="nb-type">Content</span>, contentOptions <span class="nb-type">ContentOptions</span> <span class="nb-metainfo">optional</span>)</code> : <span class="nb-type">Element</span></p>
<ul>
<li>Inserts content right after the start tag of the element.</li>
</ul>
</li>
<li>
<p><code>append(content <span class="nb-type">Content</span>, contentOptions <span class="nb-type">ContentOptions</span> <span class="nb-metainfo">optional</span>)</code> : <span class="nb-type">Element</span></p>
<ul>
<li>Inserts content right before the end tag of the element.</li>
</ul>
</li>
<li>
<p><code>replace(content <span class="nb-type">Content</span>, contentOptions <span class="nb-type">ContentOptions</span> <span class="nb-metainfo">optional</span>)</code> : <span class="nb-type">Element</span></p>
<ul>
<li>Removes the element and inserts content in place of it.</li>
</ul>
</li>
<li>
<p><code>setInnerContent(content <span class="nb-type">Content</span>, contentOptions <span class="nb-type">ContentOptions</span> <span class="nb-metainfo">optional</span>)</code> : <span class="nb-type">Element</span></p>
<ul>
<li>Replaces content of the element.</li>
</ul>
</li>
<li>
<p><code>remove()</code> : <span class="nb-type">Element</span></p>
<ul>
<li>Removes the element with all its content.</li>
</ul>
</li>
<li>
<p><code>removeAndKeepContent()</code> : <span class="nb-type">Element</span></p>
<ul>
<li>Removes the start tag and end tag of the element but keeps its inner content intact.</li>
</ul>
</li>
<li>
<p><code>onEndTag(handler <span class="nb-type">Function&amp;lt;void&amp;gt;</span>)</code> : <span class="nb-type">void</span></p>
<ul>
<li>Registers a handler that is invoked when the end tag of the element is reached.</li>
</ul>
</li>
</ul>
<h3 id="endtag">EndTag</h3>
<p>The <code>endTag</code> argument, used only in handlers registered with <code>element.onEndTag</code>, is a limited representation of a DOM element.</p>
<h4 id="properties-1">Properties</h4>
<ul>
<li><code>name</code> string
<ul>
<li>The name of the tag, such as <code>&quot;h1&quot;</code> or <code>&quot;div&quot;</code>. This property can be assigned different values, to modify an element's tag.</li>
</ul>
</li>
</ul>
<h4 id="methods-1">Methods</h4>
<ul>
<li>
<p><code>before(content <span class="nb-type">Content</span>, contentOptions <span class="nb-type">ContentOptions</span> <span class="nb-metainfo">optional</span>)</code> : <span class="nb-type">EndTag</span></p>
<ul>
<li>Inserts content right before the end tag.</li>
</ul>
</li>
<li>
<p><code>after(content <span class="nb-type">Content</span>, contentOptions <span class="nb-type">ContentOptions</span> <span class="nb-metainfo">optional</span>)</code> : <span class="nb-type">EndTag</span></p>
<ul>
<li>Inserts content right after the end tag.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="content-and-contentoptions-1">Content and ContentOptions</h3>
@markup("md", "content/.markup/bodies/16141.md")
</aside>
<ul>
<li><code>remove()</code> : <span class="nb-type">EndTag</span>
<ul>
<li>Removes the element with all its content.</li>
</ul>
</li>
</ul>
<h3 id="text-chunks">Text chunks</h3>
<p>Since Cloudflare performs zero-copy streaming parsing, text chunks are not the same thing as text nodes in the lexical tree. A lexical tree text node can be represented by multiple chunks, as they arrive over the wire from the origin.</p>
<p>Consider the following markup: `<div>
Hey. How are you?</p>
</div>`. It is possible that the Workers script will not receive the entire text node from the origin at once; instead, the `text` element handler will be invoked for each received part of the text node. For example, the handler might be invoked with `"Hey. How "`, then `"are you?"`. When the last chunk arrives, the text's `lastInTextNode` property will be set to `true`. Developers should make sure to concatenate these chunks together.
<h4 id="properties-2">Properties</h4>
<ul>
<li>
<p><code>removed</code> boolean</p>
<ul>
<li>Indicates whether the element has been removed or replaced by one of the previous handlers.</li>
</ul>
</li>
<li>
<p><code>text</code> string read-only</p>
<ul>
<li>The text content of the chunk. Could be empty if the chunk is the last chunk of the text node.</li>
</ul>
</li>
<li>
<p><code>lastInTextNode</code> boolean read-only</p>
<ul>
<li>Specifies whether the chunk is the last chunk of the text node.</li>
</ul>
</li>
</ul>
<h4 id="methods-2">Methods</h4>
<ul>
<li><code>before(content <span class="nb-type">Content</span>, contentOptions <span class="nb-type">ContentOptions</span> <span class="nb-metainfo">optional</span>)</code> : <span class="nb-type">Element</span>
<ul>
<li>Inserts content before the element.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="content-and-contentoptions-2">Content and ContentOptions</h3>
@markup("md", "content/.markup/bodies/16140.md")
</aside>
<ul>
<li>
<p><code>after(content <span class="nb-type">Content</span>, contentOptions <span class="nb-type">ContentOptions</span> <span class="nb-metainfo">optional</span>)</code> : <span class="nb-type">Element</span></p>
<ul>
<li>Inserts content right after the element.</li>
</ul>
</li>
<li>
<p><code>replace(content <span class="nb-type">Content</span>, contentOptions <span class="nb-type">ContentOptions</span> <span class="nb-metainfo">optional</span>)</code> : <span class="nb-type">Element</span></p>
<ul>
<li>Removes the element and inserts content in place of it.</li>
</ul>
</li>
<li>
<p><code>remove()</code> : <span class="nb-type">Element</span></p>
<ul>
<li>Removes the element with all its content.</li>
</ul>
</li>
</ul>
<h3 id="comments">Comments</h3>
<p>The <code>comments</code> function on an element handler allows developers to query and manipulate HTML comment tags.</p>
<pre tabindex="0"><code class="language-js">class ElementHandler {&#10;	comments(comment) {&#10;		// An incoming comment element, such as &lt;!-- My comment --&gt;&#10;	}&#10;}&#10;</code></pre>
<h4 id="properties-3">Properties</h4>
<ul>
<li>
<p><code>comment.removed</code> boolean</p>
<ul>
<li>Indicates whether the element has been removed or replaced by one of the previous handlers.</li>
</ul>
</li>
<li>
<p><code>comment.text</code> string</p>
<ul>
<li>The text of the comment. This property can be assigned different values, to modify comment's text.</li>
</ul>
</li>
</ul>
<h4 id="methods-3">Methods</h4>
<ul>
<li><code>before(content <span class="nb-type">Content</span>, contentOptions <span class="nb-type">ContentOptions</span> <span class="nb-metainfo">optional</span>)</code> : <span class="nb-type">Element</span>
<ul>
<li>Inserts content before the element.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="content-and-contentoptions-3">Content and ContentOptions</h3>
@markup("md", "content/.markup/bodies/16139.md")
</aside>
<ul>
<li>
<p><code>after(content <span class="nb-type">Content</span>, contentOptions <span class="nb-type">ContentOptions</span> <span class="nb-metainfo">optional</span>)</code> : <span class="nb-type">Element</span></p>
<ul>
<li>Inserts content right after the element.</li>
</ul>
</li>
<li>
<p><code>replace(content <span class="nb-type">Content</span>, contentOptions <span class="nb-type">ContentOptions</span> <span class="nb-metainfo">optional</span>)</code> : <span class="nb-type">Element</span></p>
<ul>
<li>Removes the element and inserts content in place of it.</li>
</ul>
</li>
<li>
<p><code>remove()</code> : <span class="nb-type">Element</span></p>
<ul>
<li>Removes the element with all its content.</li>
</ul>
</li>
</ul>
<h3 id="doctype">Doctype</h3>
<p>The <code>doctype</code> function on a document handler allows developers to query a document's <a href="https://developer.mozilla.org/en-US/docs/Glossary/Doctype">doctype</a>.</p>
<pre tabindex="0"><code class="language-js">class DocumentHandler {&#10;	doctype(doctype) {&#10;		// An incoming doctype element, such as&#10;		// &lt;!DOCTYPE html PUBLIC &quot;-//W3C//DTD HTML 4.01//EN&quot; &quot;http://www.w3.org/TR/html4/strict.dtd&quot;&gt;&#10;	}&#10;}&#10;</code></pre>
<h4 id="properties-4">Properties</h4>
<ul>
<li>
<p><code>doctype.name</code> string | null read-only</p>
<ul>
<li>The doctype name.</li>
</ul>
</li>
<li>
<p><code>doctype.publicId</code> string | null read-only</p>
<ul>
<li>The quoted string in the doctype after the PUBLIC atom.</li>
</ul>
</li>
<li>
<p><code>doctype.systemId</code> string | null read-only</p>
<ul>
<li>The quoted string in the doctype after the SYSTEM atom or immediately after the <code>publicId</code>.</li>
</ul>
</li>
</ul>
<h3 id="end">End</h3>
<p>The <code>end</code> function on a document handler allows developers to append content to the end of a document.</p>
<pre tabindex="0"><code class="language-js">class DocumentHandler {&#10;	end(end) {&#10;		// The end of the document&#10;	}&#10;}&#10;</code></pre>
<h4 id="methods-4">Methods</h4>
<ul>
<li><code>append(content <span class="nb-type">Content</span>, contentOptions <span class="nb-type">ContentOptions</span> <span class="nb-metainfo">optional</span>)</code> : <span class="nb-type">DocumentEnd</span>
<ul>
<li>Inserts content after the end of the document.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="content-and-contentoptions-4">Content and ContentOptions</h3>
@markup("md", "content/.markup/bodies/16138.md")
</aside>
<hr />
<h2 id="selectors">Selectors</h2>
<p>This is what selectors are and what they are used for.</p>
<ul>
<li>
<p><code>*</code></p>
<ul>
<li>Any element.</li>
</ul>
</li>
<li>
<p><code>E</code></p>
<ul>
<li>Any element of type E.</li>
</ul>
</li>
<li>
<p><code>E:nth-child(n)</code></p>
<ul>
<li>An E element, the n-th child of its parent.</li>
</ul>
</li>
<li>
<p><code>E:first-child</code></p>
<ul>
<li>An E element, first child of its parent.</li>
</ul>
</li>
<li>
<p><code>E:nth-of-type(n)</code></p>
<ul>
<li>An E element, the n-th sibling of its type.</li>
</ul>
</li>
<li>
<p><code>E:first-of-type</code></p>
<ul>
<li>An E element, first sibling of its type.</li>
</ul>
</li>
<li>
<p><code>E:not(s)</code></p>
<ul>
<li>An E element that does not match either compound selectors.</li>
</ul>
</li>
<li>
<p><code>E.warning</code></p>
<ul>
<li>An E element belonging to the class warning.</li>
</ul>
</li>
<li>
<p><code>E#myid</code></p>
<ul>
<li>An E element with ID equal to myid.</li>
</ul>
</li>
<li>
<p><code>E[foo]</code></p>
<ul>
<li>An E element with a foo attribute.</li>
</ul>
</li>
<li>
<p><code>E[foo=&quot;bar&quot;]</code></p>
<ul>
<li>An E element whose foo attribute value is exactly equal to bar.</li>
</ul>
</li>
<li>
<p><code>E[foo=&quot;bar&quot; i]</code></p>
<ul>
<li>An E element whose foo attribute value is exactly equal to any (ASCII-range) case-permutation of bar.</li>
</ul>
</li>
<li>
<p><code>E[foo=&quot;bar&quot; s]</code></p>
<ul>
<li>An E element whose foo attribute value is exactly and case-sensitively equal to bar.</li>
</ul>
</li>
<li>
<p><code>E[foo~=&quot;bar&quot;]</code></p>
<ul>
<li>An E element whose foo attribute value is a list of whitespace-separated values, one of which is exactly equal to bar.</li>
</ul>
</li>
<li>
<p><code>E[foo^=&quot;bar&quot;]</code></p>
<ul>
<li>An E element whose foo attribute value begins exactly with the string bar.</li>
</ul>
</li>
<li>
<p><code>E[foo$=&quot;bar&quot;]</code></p>
<ul>
<li>An E element whose foo attribute value ends exactly with the string bar.</li>
</ul>
</li>
<li>
<p><code>E[foo*=&quot;bar&quot;]</code></p>
<ul>
<li>An E element whose foo attribute value contains the substring bar.</li>
</ul>
</li>
<li>
<p><code>E[foo|=&quot;en&quot;]</code></p>
<ul>
<li>An E element whose foo attribute value is a hyphen-separated list of values beginning with en.</li>
</ul>
</li>
<li>
<p><code>E F</code></p>
<ul>
<li>An F element descendant of an E element.</li>
</ul>
</li>
<li>
<p><code>E &gt; F</code></p>
<ul>
<li>An F element child of an E element.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="errors">Errors</h2>
<p>If a handler throws an exception, parsing is immediately halted, the transformed response body is errored with the thrown exception, and the untransformed response body is canceled (closed). If the transformed response body was already partially streamed back to the client, the client will see a truncated response.</p>
<pre tabindex="0"><code class="language-js">async function handle(request) {&#10;	let oldResponse = await fetch(request);&#10;	let newResponse = new HTMLRewriter()&#10;		.on(&quot;*&quot;, {&#10;			element(element) {&#10;				throw new Error(&quot;A really bad error.&quot;);&#10;			},&#10;		})&#10;		.transform(oldResponse);&#10;&#10;	// At this point, an expression like `await newResponse.text()`&#10;	// will throw `new Error(&quot;A really bad error.&quot;)`.&#10;	// Thereafter, any use of `newResponse.body` will throw the same error,&#10;	// and `oldResponse.body` will be closed.&#10;&#10;	// Alternatively, this will produce a truncated response to the client:&#10;	return newResponse;&#10;}&#10;</code></pre>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://blog.cloudflare.com/introducing-htmlrewriter/">Introducing <code>HTMLRewriter</code></a></li>
<li><a href="/pages/tutorials/localize-a-website/">Tutorial: Localize a Website</a></li>
<li><a href="/workers/examples/rewrite-links/">Example: rewrite links</a></li>
<li><a href="/workers/examples/turnstile-html-rewriter/">Example: Inject Turnstile</a></li>
<li><a href="/workers/examples/spa-shell/">Example: SPA shell with bootstrap data</a></li>
</ul>
