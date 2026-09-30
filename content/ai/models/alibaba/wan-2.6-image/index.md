<img src="/assets/upstream/images/workers-ai/alibaba.svg" alt="Alibaba logo" width="48" height="48">

<h1 id="wan-2-6-image">Wan 2.6 Image</h1>

<p><code>alibaba/wan-2.6-image</code></p>

Alibaba's Wan 2.6 text-to-image model generating images from text prompts with optional negative prompts and customizable dimensions.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://www.alibabacloud.com/help/en/legal">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per image: 0.03</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic text-to-image generation

<section class="model-example"><strong>Simple Generation</strong>
<p>Basic text-to-image generation</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever puppy playing in autumn leaves&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__wan-2.6-image/simple-generation.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://dashscope-463f.oss-accelerate.aliyuncs.com/1d/66/20260417/c057796c/32701268-BbftSa6r_189314ac1a36.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/wan-2.6-image&#x27;,
  { prompt: &#x27;A golden retriever puppy playing in autumn leaves&#x27; },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;alibaba/wan-2.6-image&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A golden retriever puppy playing in autumn leaves&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__wan-2.6-image/simple-generation.png" alt="Simple Generation">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Custom Dimensions</strong>
<p>Specify image size in WxH format</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A vast alien desert landscape with two suns setting on the horizon, ancient ruins in the foreground&quot;,
    &quot;size&quot;: &quot;1024x768&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__wan-2.6-image/custom-dimensions.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://dashscope-463f.oss-accelerate.aliyuncs.com/1d/35/20260417/c057796c/3257252-vy1GbNI6_bc223e38c5b4.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/wan-2.6-image&#x27;,
  {
    prompt:
      &#x27;A vast alien desert landscape with two suns setting on the horizon, ancient ruins in the foreground&#x27;,
    size: &#x27;1024x768&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;alibaba/wan-2.6-image&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A vast alien desert landscape with two suns setting on the horizon, ancient ruins in the foreground&quot;,
    &quot;size&quot;: &quot;1024x768&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__wan-2.6-image/custom-dimensions.png" alt="Custom Dimensions">
</section>

<section class="model-example"><strong>Square Format</strong>
<p>Square image for social media or product photos</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A sleek wireless headphone on a minimalist white marble surface with soft studio lighting&quot;,
    &quot;size&quot;: &quot;1024x1024&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__wan-2.6-image/square-format.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://dashscope-463f.oss-accelerate.aliyuncs.com/1d/84/20260417/c057796c/18355039-RFkWcHgG_0dcb1c1d6d95.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/wan-2.6-image&#x27;,
  {
    prompt:
      &#x27;A sleek wireless headphone on a minimalist white marble surface with soft studio lighting&#x27;,
    size: &#x27;1024x1024&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;alibaba/wan-2.6-image&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A sleek wireless headphone on a minimalist white marble surface with soft studio lighting&quot;,
    &quot;size&quot;: &quot;1024x1024&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__wan-2.6-image/square-format.png" alt="Square Format">
</section>

<section class="model-example"><strong>Negative Prompt</strong>
<p>Guide generation away from unwanted elements</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed oil painting portrait of a Renaissance nobleman with intricate lace collar&quot;,
    &quot;negative_prompt&quot;: &quot;modern clothing, photograph, blurry, low quality&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__wan-2.6-image/negative-prompt.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://dashscope-463f.oss-accelerate.aliyuncs.com/1d/53/20260417/c057796c/26097304-eVhNm6uS_edc041cd5e2b.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/wan-2.6-image&#x27;,
  {
    prompt: &#x27;A detailed oil painting portrait of a Renaissance nobleman with intricate lace collar&#x27;,
    negative_prompt: &#x27;modern clothing, photograph, blurry, low quality&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;alibaba/wan-2.6-image&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed oil painting portrait of a Renaissance nobleman with intricate lace collar&quot;,
    &quot;negative_prompt&quot;: &quot;modern clothing, photograph, blurry, low quality&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__wan-2.6-image/negative-prompt.png" alt="Negative Prompt">
</section>

<section class="model-example"><strong>Portrait Format</strong>
<p>Tall vertical image for portraits</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An elegant Art Deco poster featuring a jazz singer under a spotlight&quot;,
    &quot;size&quot;: &quot;768x1024&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__wan-2.6-image/portrait-format.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://dashscope-463f.oss-accelerate.aliyuncs.com/1d/5a/20260417/c057796c/79957405-YTXQsRY6_8d8a6631f1d6.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/wan-2.6-image&#x27;,
  {
    prompt: &#x27;An elegant Art Deco poster featuring a jazz singer under a spotlight&#x27;,
    size: &#x27;768x1024&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;alibaba/wan-2.6-image&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;An elegant Art Deco poster featuring a jazz singer under a spotlight&quot;,
    &quot;size&quot;: &quot;768x1024&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__wan-2.6-image/portrait-format.png" alt="Portrait Format">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required.</td></tr><tr><td><code>size</code></td><td>string</td><td></td></tr><tr><td><code>negative_prompt</code></td><td>string</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/alibaba/wan-2.6-image/schema-input.json)
- [Output schema](/ai/models/alibaba/wan-2.6-image/schema-output.json)

