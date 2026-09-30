<img src="/assets/upstream/images/workers-ai/alibaba.svg" alt="Alibaba logo" width="48" height="48">

<h1 id="happyhorse-1-0-i2v">HappyHorse 1.0 I2V</h1>

<p><code>alibaba/hh1-i2v</code></p>

Alibaba's HappyHorse 1.0 image-to-video model. Animates a reference image with an optional text prompt. Supports 720P and 1080P output with durations from 3 to 15 seconds.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Image-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://www.alibabacloud.com/help/en/legal">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.28, @720p (per second): 0.14, @1080p (per second): 0.28</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Animate a reference image with a short prompt

<section class="model-example"><strong>Simple Image-to-Video</strong>
<p>Animate a reference image with a short prompt</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;image&quot;: &quot;https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250925/wpimhv/rap.png&quot;,
    &quot;prompt&quot;: &quot;A gentle camera push-in on the scene with soft ambient lighting&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__hh1-i2v/simple-image-to-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__hh1-i2v/simple-image-to-video.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/hh1-i2v&#x27;,
  {
    image:
      &#x27;https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250925/wpimhv/rap.png&#x27;,
    prompt: &#x27;A gentle camera push-in on the scene with soft ambient lighting&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;alibaba/hh1-i2v&quot;,
  &quot;input&quot;: {
    &quot;image&quot;: &quot;https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250925/wpimhv/rap.png&quot;,
    &quot;prompt&quot;: &quot;A gentle camera push-in on the scene with soft ambient lighting&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>High Resolution</strong>
<p>Generate at 1080P with a longer duration</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;image&quot;: &quot;https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250925/wpimhv/rap.png&quot;,
    &quot;prompt&quot;: &quot;Subject begins rapping confidently to the beat, head bobbing&quot;,
    &quot;duration&quot;: 10,
    &quot;resolution&quot;: &quot;1080P&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__hh1-i2v/high-resolution.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__hh1-i2v/high-resolution.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/hh1-i2v&#x27;,
  {
    image:
      &#x27;https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250925/wpimhv/rap.png&#x27;,
    prompt: &#x27;Subject begins rapping confidently to the beat, head bobbing&#x27;,
    duration: 10,
    resolution: &#x27;1080P&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;alibaba/hh1-i2v&quot;,
  &quot;input&quot;: {
    &quot;image&quot;: &quot;https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250925/wpimhv/rap.png&quot;,
    &quot;prompt&quot;: &quot;Subject begins rapping confidently to the beat, head bobbing&quot;,
    &quot;duration&quot;: 10,
    &quot;resolution&quot;: &quot;1080P&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Reproducible Output</strong>
<p>Use a fixed seed for reproducibility</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;image&quot;: &quot;https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250925/wpimhv/rap.png&quot;,
    &quot;prompt&quot;: &quot;Camera orbits slowly around the subject under streetlamp light&quot;,
    &quot;duration&quot;: 8,
    &quot;resolution&quot;: &quot;720P&quot;,
    &quot;seed&quot;: 42
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__hh1-i2v/reproducible-output.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;result&quot;: {
      &quot;video&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/alibaba__hh1-i2v/reproducible-output.mp4&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;alibaba/hh1-i2v&#x27;,
  {
    image:
      &#x27;https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250925/wpimhv/rap.png&#x27;,
    prompt: &#x27;Camera orbits slowly around the subject under streetlamp light&#x27;,
    duration: 8,
    resolution: &#x27;720P&#x27;,
    seed: 42,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;alibaba/hh1-i2v&quot;,
  &quot;input&quot;: {
    &quot;image&quot;: &quot;https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250925/wpimhv/rap.png&quot;,
    &quot;prompt&quot;: &quot;Camera orbits slowly around the subject under streetlamp light&quot;,
    &quot;duration&quot;: 8,
    &quot;resolution&quot;: &quot;720P&quot;,
    &quot;seed&quot;: 42
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required.</td></tr><tr><td><code>prompt</code></td><td>string</td><td></td></tr><tr><td><code>negative_prompt</code></td><td>string</td><td></td></tr><tr><td><code>resolution</code></td><td>string</td><td>Values: 720P, 1080P</td></tr><tr><td><code>duration</code></td><td>integer</td><td>Minimum: 3; Maximum: 15</td></tr><tr><td><code>seed</code></td><td>integer</td><td>Minimum: 0; Maximum: 2147483647</td></tr><tr><td><code>watermark</code></td><td>boolean</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>video</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/alibaba/hh1-i2v/schema-input.json)
- [Output schema](/ai/models/alibaba/hh1-i2v/schema-output.json)

