---
cp9:
  canonical: https://developers.cloudflare.com/constellation/platform/client-api/
  description: Interact with the Constellation inference engine via the client API.
  full_title: Client API · Constellation docs
  head_html: <title>Client API · Constellation docs</title><meta name="generator" content="Nift"><meta name="description" content="Interact with the Constellation inference engine via the client API."><link rel="canonical" href="https://developers.cloudflare.com/constellation/platform/client-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/constellation/platform/client-api/index.md"><meta property="og:title" content="Client API · Constellation docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Interact with the Constellation inference engine via the client API."><meta property="og:url" content="https://developers.cloudflare.com/constellation/platform/client-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Constellation"><meta name="algolia_product_filter" content="Constellation"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Constellation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/constellation/platform/client-api/#page","headline":"Client API \u00b7 Constellation docs","description":"Interact with the Constellation inference engine via the client API.","url":"https://developers.cloudflare.com/constellation/platform/client-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /constellation/platform/client-api/
  schema: 1
---
<p>The Constellation client API allows developers to interact with the inference engine using the models configured for each project. Inference is the process of running data inputs on a machine-learning model and generating an output, or otherwise known as a prediction.</p>
<p>Before you use the Constellation client API, you need to:</p>
<ul>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li>Enable Constellation by logging into the Cloudflare dashboard &gt; <strong>Workers &amp; Pages</strong> &gt; <strong>Constellation</strong>.</li>
<li>Create a Constellation project and configure the binding.</li>
<li>Import the <code>@cloudflare/constellation</code> library in your code:</li>
</ul>
<pre tabindex="0"><code class="language-javascript">import { Tensor, run } from &quot;@cloudflare/constellation&quot;;&#10;</code></pre>
<h2 id="tensor-class">Tensor class</h2>
<p>Tensors are essentially multidimensional numerical arrays used to represent any kind of data, like a piece of text, an image, or a time series. TensorFlow popularized the use of <a href="https://www.tensorflow.org/guide/tensor">Tensors</a> in machine learning (hence the name). Other frameworks and runtimes have since followed the same concept.</p>
<p>Constellation also uses Tensors for model input.</p>
<p>Tensors have a data type, a shape, the data, and a name.</p>
<pre tabindex="0"><code class="language-typescript">enum TensorType {&#10;    Bool = &quot;bool&quot;,&#10;    Float16 = &quot;float16&quot;,&#10;    Float32 = &quot;float32&quot;,&#10;    Int8 = &quot;int8&quot;,&#10;    Int16 = &quot;int16&quot;,&#10;    Int32 = &quot;int32&quot;,&#10;    Int64 = &quot;int64&quot;,&#10;}&#10;&#10;type TensorOpts = {&#10;  shape?: number[],&#10;  name?: string&#10;}&#10;&#10;declare class Tensor&lt;TensorType&gt; {&#10;  constructor(&#10;    type: T,&#10;    value: any | any[],&#10;    opts: TensorOpts = {}&#10;  )&#10;}&#10;</code></pre>
<h3 id="create-new-tensor">Create new Tensor</h3>
<pre tabindex="0"><code class="language-typescript">new Tensor(&#10;  type:TensorType,&#10;  value:any | any[],&#10;  options?:TensorOpts&#10;  )&#10;</code></pre>
<h4 id="type">type</h4>
<p>Defines the type of data represented in the Tensor. Options are:</p>
<ul>
<li>TensorType.Bool</li>
<li>TensorType.Float16</li>
<li>TensorType.Float32</li>
<li>TensorType.Int8</li>
<li>TensorType.Int16</li>
<li>TensorType.Int32</li>
<li>TensorType.Int64</li>
</ul>
<h4 id="value">value</h4>
<p>This is the tensor's data. Example tensor values can include:</p>
<ul>
<li>scalar: 4</li>
<li>vector: [1, 2, 3]</li>
<li>two-axes 3x2 matrix: [[1,2], [2,4], [5,6]]</li>
<li>three-axes 3x2 matrix [ [[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]] ]</li>
</ul>
<h4 id="options">options</h4>
<p>You can pass options to your tensor:</p>
<h5 id="shape">shape</h5>
<p>Tensors store multidimensional data. The shape of the data can be a scalar, a vector, a 2D matrix or multiple-axes matrixes. Some examples:</p>
<ul>
<li>[] - scalar data</li>
<li>[3] - vector with 3 elements</li>
<li>[3, 2] - two-axes 3x2 matrix</li>
<li>[3, 2, 2] - three-axis 2x2 matrix</li>
</ul>
<p>Refer to the <a href="https://www.tensorflow.org/guide/tensor">TensorFlow documentation</a> for more information about shapes.</p>
<p>If you don't pass the shape, then we try to infer it from the value object. If we can't, we thrown an error.</p>
<h5 id="name">name</h5>
<p>Naming a tensor is optional, it can be a useful key for mapping operations when building the tensor inputs.</p>
<h3 id="tensor-examples">Tensor examples</h3>
<h4 id="a-scalar">A scalar</h4>
<pre tabindex="0"><code class="language-javascript">  new Tensor(TensorType.Int16, 123);&#10;</code></pre>
<h4 id="arrays">Arrays</h4>
<pre tabindex="0"><code class="language-javascript">  new Tensor(TensorType.Int32, [1, 23]);&#10;  new Tensor(TensorType.Int32, [ [1, 2], [3, 4], ], { shape: [2, 2] });&#10;  new Tensor(TensorType.Int32, [1, 23], { shape: [1] });&#10;</code></pre>
<h4 id="named">Named</h4>
<pre tabindex="0"><code class="language-javascript">  new Tensor(TensorType.Int32, 1, { name: &quot;foo&quot; });&#10;</code></pre>
<h3 id="tensor-properties">Tensor properties</h3>
<p>You can read the tensor's properties after it has been created:</p>
<pre tabindex="0"><code class="language-javascript">const tensor = new Tensor(TensorType.Int32, [ [1, 2], [3, 4], ], { shape: [2, 2], name: &quot;test&quot; });&#10;&#10;console.log ( tensor.type );&#10;// TensorType.Int32&#10;&#10;console.log ( tensor.shape );&#10;// [2, 2]&#10;&#10;console.log ( tensor.name );&#10;// test&#10;&#10;console.log ( tensor.value );&#10;//  [ [1, 2], [3, 4], ]&#10;</code></pre>
<h3 id="tensor-methods">Tensor methods</h3>
<h4 id="async-tensor-tojson">async tensor.toJSON()</h4>
<p>Serializes the tensor to a JSON object:</p>
<pre tabindex="0"><code class="language-javascript">const tensor = new Tensor(TensorType.Int32, [ [1, 2], [3, 4], ], { shape: [2, 2], name: &quot;test&quot; });&#10;&#10;tensor.toJSON();&#10;&#10;{&#10;  type: TensorType.Int32,&#10;  name: &quot;test&quot;,&#10;  shape:  [2, 2],&#10;  value: [ [1, 2], [3, 4], ]&#10;}&#10;</code></pre>
<h4 id="async-tensor-fromjson">async tensor.fromJSON()</h4>
<p>Serializes a JSON object to a tensor:</p>
<pre tabindex="0"><code class="language-javascript">const tensor = Tensor.fromJSON(&#10;  {&#10;    type: TensorType.Int32,&#10;    name: &quot;test&quot;,&#10;    shape:  [2, 2],&#10;    value: [ [1, 2], [3, 4], ]&#10;  }&#10;);&#10;</code></pre>
<h2 id="inferencesession-class">InferenceSession class</h2>
<p>Constellation requires an inference session before you can run a task. A session is locked to a specific project, defined in your binding, and the project model.</p>
<p>You can, and should, if possible, run multiple tasks under the same inference session. Reusing the same session, means that we instantiate the runtime and load the model to memory once.</p>
<pre tabindex="0"><code class="language-typescript">export class InferenceSession {&#10;    constructor(binding: any, modelId: string, options: SessionOptions = {})&#10;}&#10;&#10;export type InferenceSession = {&#10;  binding: any;&#10;  model: string;&#10;  options: SessionOptions;&#10;};&#10;</code></pre>
<h3 id="inferencesession-methods">InferenceSession methods</h3>
<h4 id="new-inferencesession">new InferenceSession()</h4>
<p>To create a new session:</p>
<pre tabindex="0"><code class="language-javascript">import { InferenceSession } from &quot;@cloudflare/constellation&quot;;&#10;&#10;const session = new InferenceSession(&#10;  env.PROJECT,&#10;  &quot;0ae7bd14-a0df-4610-aa85-1928656d6e9e&quot;&#10;);&#10;</code></pre>
<ul>
<li><strong>env.PROJECT</strong> is the project binding defined in your Wrangler configuration.</li>
<li><strong>0ae7bd14...</strong> is the model ID inside the project. Use Wrangler to list the models and their IDs in a project.</li>
</ul>
<h4 id="async-session-run">async session.run()</h4>
<p>Runs a task in the created inference session. Takes a list of tensors as the input.</p>
<pre tabindex="0"><code class="language-javascript">import { Tensor, InferenceSession, TensorType } from &quot;@cloudflare/constellation&quot;;&#10;&#10;const session = new InferenceSession(&#10;  env.PROJECT,&#10;  &quot;0ae7bd14-a0df-4610-aa85-1998656d6e9e&quot;&#10;);&#10;&#10;const tensorInputArray = [ new Tensor(TensorType.Int32, 1), new Tensor(TensorType.Int32, 2), new Tensor(TensorType.Int32, 3) ];&#10;&#10;const out = await session.run(tensorInputArray);&#10;</code></pre>
<p>You can also use an object and name your tensors.</p>
<pre tabindex="0"><code class="language-javascript">const tensorInputNamed = {&#10;  &quot;tensor1&quot;: new Tensor(TensorType.Int32, 1),&#10;  &quot;tensor2&quot;: new Tensor(TensorType.Int32, 2),&#10;  &quot;tensor3&quot;: new Tensor(TensorType.Int32, 3)&#10;};&#10;&#10;out = await session.run(tensorInputNamed);&#10;</code></pre>
<p>This is the same as using the name option when you create a tensor.</p>
<pre tabindex="0"><code class="language-javascript">{ &quot;tensor1&quot;: new Tensor(TensorType.Int32, 1) } == [ new Tensor(TensorType.Int32, 1, { name: &quot;tensor1&quot; } ];&#10;</code></pre>
