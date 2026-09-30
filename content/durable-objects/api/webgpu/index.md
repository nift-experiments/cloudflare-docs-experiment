---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/api/webgpu/
  description: Use the WebGPU API for GPU access from within Durable Objects in local development.
  full_title: WebGPU · Cloudflare Durable Objects docs
  head_html: <title>WebGPU · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the WebGPU API for GPU access from within Durable Objects in local development."><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/api/webgpu/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/api/webgpu/index.md"><meta property="og:title" content="WebGPU · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the WebGPU API for GPU access from within Durable Objects in local development."><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/api/webgpu/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/durable-objects/api/webgpu/#page","headline":"WebGPU \u00b7 Cloudflare Durable Objects docs","description":"Use the WebGPU API for GPU access from within Durable Objects in local development.","url":"https://developers.cloudflare.com/durable-objects/api/webgpu/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /durable-objects/api/webgpu/
  schema: 1
---
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8313.md")
</aside>
<p>The <a href="https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API">WebGPU API</a> allows you to use the GPU directly from JavaScript.</p>
<p>The WebGPU API is only accessible from within <a href="/durable-objects/">Durable Objects</a>. You cannot use the WebGPU API from within Workers.</p>
<p>To use the WebGPU API in local development, enable the <code>experimental</code> and <code>webgpu</code> <a href="/workers/configuration/compatibility-flags/">compatibility flags</a> in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> of your Durable Object.</p>
<pre tabindex="0"><code>compatibility_flags = [&quot;experimental&quot;, &quot;webgpu&quot;]&#10;</code></pre>
<p>The following subset of the WebGPU API is available from within Durable Objects:</p>
<table>
<thead>
<tr>
<th>API</th>
<th>Supported?</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/Navigator/gpu"><code>navigator.gpu</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPU/requestAdapter"><code>GPU.requestAdapter</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUAdapterInfo"><code>GPUAdapterInfo</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUAdapter"><code>GPUAdapter</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUBindGroupLayout"><code>GPUBindGroupLayout</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUBindGroup"><code>GPUBindGroup</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUBuffer"><code>GPUBuffer</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUCommandBuffer"><code>GPUCommandBuffer</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUCommandEncoder"><code>GPUCommandEncoder</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUComputePassEncoder"><code>GPUComputePassEncoder</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUComputePipeline"><code>GPUComputePipeline</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUPipelineError"><code>GPUComputePipelineError</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUDevice"><code>GPUDevice</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUOutOfMemoryError"><code>GPUOutOfMemoryError</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUValidationError"><code>GPUValidationError</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUInternalError"><code>GPUInternalError</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUDeviceLostInfo"><code>GPUDeviceLostInfo</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUPipelineLayout"><code>GPUPipelineLayout</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUQuerySet"><code>GPUQuerySet</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUQueue"><code>GPUQueue</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUSampler"><code>GPUSampler</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUCompilationMessage"><code>GPUCompilationMessage</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUShaderModule"><code>GPUShaderModule</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUSupportedFeatures"><code>GPUSupportedFeatures</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUSupportedLimits"><code>GPUSupportedLimits</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API#reading_the_results_back_to_javascript"><code>GPUMapMode</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API#create_a_bind_group_layout"><code>GPUShaderStage</code></a></td>
<td>✅</td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUUncapturedErrorEvent"><code>GPUUncapturedErrorEvent</code></a></td>
<td>✅</td>
<td></td>
</tr>
</tbody>
</table>
<p>The following subset of the WebGPU API is not yet supported:</p>
<table>
<thead>
<tr>
<th>API</th>
<th>Supported?</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPU/getPreferredCanvasFormat"><code>GPU.getPreferredCanvasFormat</code></a></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPURenderBundle"><code>GPURenderBundle</code></a></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPURenderBundleEncoder"><code>GPURenderBundleEncoder</code></a></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPURenderPassEncoder"><code>GPURenderPassEncoder</code></a></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPURenderPipeline"><code>GPURenderPipeline</code></a></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUShaderModule"><code>GPUShaderModule</code></a></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUTexture"><code>GPUTexture</code></a></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUTextureView"><code>GPUTextureView</code></a></td>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/GPUExternalTexture"><code>GPUExternalTexture</code></a></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h2 id="examples">Examples</h2>
<ul>
<li><a href="https://github.com/cloudflare/workers-wonnx/">workers-wonnx</a> — Image classification, running on a GPU via the WebGPU API, using the <a href="https://github.com/webonnx/wonnx">wonnx</a> model inference runtime.</li>
</ul>
