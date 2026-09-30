<p>Pages Functions provide support for several module types, much like <a href="https://blog.cloudflare.com/workers-javascript-modules/">Workers</a>. This means that you can import and use external modules such as WebAssembly (Wasm), <code>text</code> and <code>binary</code> files inside your Functions code.</p>
<p>This guide will instruct you on how to use these different module types inside your Pages Functions.</p>
<h2 id="ecmascript-modules">ECMAScript Modules</h2>
<p>ECMAScript modules (or in short ES Modules) is the official, <a href="https://tc39.es/ecma262/#sec-modules">standardized</a> module system for JavaScript. It is the recommended mechanism for writing modular and reusable JavaScript code.</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules">ES Modules</a> are defined by the use of <code>import</code> and <code>export</code> statements. Below is an example of a script written in ES Modules format, and a Pages Function that imports that module:</p>
<pre><code class="language-js">export function greeting(name: string): string {&#10;  return `Hello ${name}!`;&#10;}&#10;</code></pre>
<pre><code class="language-js">import { greeting } from &quot;../src/greeting.ts&quot;;&#10;&#10;export async function onRequest(context) {&#10;	return new Response(`${greeting(&quot;Pages Functions&quot;)}`);&#10;}&#10;</code></pre>
<h2 id="webassembly-modules">WebAssembly Modules</h2>
<p><a href="/workers/runtime-apis/webassembly/">WebAssembly</a> (abbreviated Wasm) allows you to compile languages like Rust, Go, or C to a binary format that can run in a wide variety of environments, including web browsers, Cloudflare Workers, Cloudflare Pages Functions, and other WebAssembly runtimes.</p>
<p>The distributable, loadable, and executable unit of code in WebAssembly is called a <a href="https://webassembly.github.io/spec/core/syntax/modules.html">module</a>.</p>
<p>Below is a basic example of how you can import Wasm Modules inside your Pages Functions code:</p>
<pre><code class="language-js">import addModule from &quot;add.wasm&quot;;&#10;&#10;export async function onRequest() {&#10;	const addInstance = await WebAssembly.instantiate(addModule);&#10;	return new Response(&#10;		`The meaning of life is ${addInstance.exports.add(20, 1)}`,&#10;	);&#10;}&#10;</code></pre>
<h2 id="text-modules">Text Modules</h2>
<p>Text Modules are a non-standardized means of importing resources such as HTML files as a <code>String</code>.</p>
<p>To import the below HTML file into your Pages Functions code:</p>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;&#10;&lt;html&gt;&#10;	&lt;body&gt;&#10;		&lt;h1&gt;Hello Pages Functions!&lt;/h1&gt;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<p>Use the following script:</p>
<pre><code class="language-js">import html from &quot;../index.html&quot;;&#10;&#10;export async function onRequest() {&#10;	return new Response(html, {&#10;		headers: { &quot;Content-Type&quot;: &quot;text/html&quot; },&#10;	});&#10;}&#10;</code></pre>
<h2 id="binary-modules">Binary Modules</h2>
<p>Binary Modules are a non-standardized way of importing binary data such as images as an <code>ArrayBuffer</code>.</p>
<p>Below is a basic example of how you can import the data from a binary file inside your Pages Functions code:</p>
<pre><code class="language-js">import data from &quot;../my-data.bin&quot;;&#10;&#10;export async function onRequest() {&#10;	return new Response(data, {&#10;		headers: { &quot;Content-Type&quot;: &quot;application/octet-stream&quot; },&#10;	});&#10;}&#10;</code></pre>
