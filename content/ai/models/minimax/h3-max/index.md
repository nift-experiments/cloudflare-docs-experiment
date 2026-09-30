<img src="/assets/upstream/images/workers-ai/minimax.svg" alt="Minimax logo" width="48" height="48">

<h1 id="minimax-h3-max">MiniMax H3 Max</h1>

<p><code>minimax/h3-max</code></p>

A fast multimodal video generation model supporting text-to-video and image-to-video generation at 480P and 768P.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://platform.minimax.io/docs/guides/terms-of-service.md">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.05, @480p (per second): 0.05, @768p (per second): 0.08</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate a fast 768P landscape video from text.

<section class="model-example"><strong>Balanced Text to Video</strong>
<p>Generate a fast 768P landscape video from text.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;A golden retriever runs along a beach at sunrise while the camera tracks beside it in a cinematic slow motion shot.&quot;
      }
    ],
    &quot;duration&quot;: 5,
    &quot;extra&quot;: {
      &quot;prompt_expansion_mode&quot;: &quot;balanced&quot;
    },
    &quot;ratio&quot;: &quot;16:9&quot;,
    &quot;resolution&quot;: &quot;768P&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3-max/balanced-text-to-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;task&quot;: {
      &quot;id&quot;: &quot;441805798383681&quot;,
      &quot;model&quot;: &quot;MiniMax-H3-Max&quot;,
      &quot;status&quot;: &quot;succeeded&quot;,
      &quot;created_at&quot;: 1789415547,
      &quot;updated_at&quot;: 1789415554,
      &quot;content&quot;: {
        &quot;url&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3-max/balanced-text-to-video.mp4&quot;
      },
      &quot;resolution&quot;: &quot;768P&quot;,
      &quot;duration&quot;: 5,
      &quot;usage&quot;: {
        &quot;total_seconds&quot;: 5,
        &quot;input_seconds&quot;: 0,
        &quot;output_seconds&quot;: 5,
        &quot;input_image_count&quot;: 0
      },
      &quot;ratio&quot;: &quot;16:9&quot;,
      &quot;task_type&quot;: &quot;generation&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/h3-max&#x27;,
  {
    content: [
      {
        type: &#x27;text&#x27;,
        text: &#x27;A golden retriever runs along a beach at sunrise while the camera tracks beside it in a cinematic slow motion shot.&#x27;,
      },
    ],
    duration: 5,
    extra: { prompt_expansion_mode: &#x27;balanced&#x27; },
    ratio: &#x27;16:9&#x27;,
    resolution: &#x27;768P&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/h3-max&quot;,
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;A golden retriever runs along a beach at sunrise while the camera tracks beside it in a cinematic slow motion shot.&quot;
      }
    ],
    &quot;duration&quot;: 5,
    &quot;extra&quot;: {
      &quot;prompt_expansion_mode&quot;: &quot;balanced&quot;
    },
    &quot;ratio&quot;: &quot;16:9&quot;,
    &quot;resolution&quot;: &quot;768P&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Disabled Prompt Expansion</strong>
<p>Generate a fast 480P vertical social video with prompt expansion disabled.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;A chef tosses vegetables in a wok in a bright street-food kitchen, energetic handheld camera.&quot;
      }
    ],
    &quot;duration&quot;: 5,
    &quot;extra&quot;: {
      &quot;prompt_expansion_mode&quot;: &quot;disabled&quot;
    },
    &quot;ratio&quot;: &quot;9:16&quot;,
    &quot;resolution&quot;: &quot;480P&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3-max/disabled-prompt-expansion.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;task&quot;: {
      &quot;id&quot;: &quot;441804654764158&quot;,
      &quot;model&quot;: &quot;MiniMax-H3-Max&quot;,
      &quot;status&quot;: &quot;succeeded&quot;,
      &quot;created_at&quot;: 1789415577,
      &quot;updated_at&quot;: 1789415583,
      &quot;content&quot;: {
        &quot;url&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3-max/disabled-prompt-expansion.mp4&quot;
      },
      &quot;resolution&quot;: &quot;480P&quot;,
      &quot;duration&quot;: 5,
      &quot;usage&quot;: {
        &quot;total_seconds&quot;: 5,
        &quot;input_seconds&quot;: 0,
        &quot;output_seconds&quot;: 5,
        &quot;input_image_count&quot;: 0
      },
      &quot;ratio&quot;: &quot;9:16&quot;,
      &quot;task_type&quot;: &quot;generation&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/h3-max&#x27;,
  {
    content: [
      {
        type: &#x27;text&#x27;,
        text: &#x27;A chef tosses vegetables in a wok in a bright street-food kitchen, energetic handheld camera.&#x27;,
      },
    ],
    duration: 5,
    extra: { prompt_expansion_mode: &#x27;disabled&#x27; },
    ratio: &#x27;9:16&#x27;,
    resolution: &#x27;480P&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/h3-max&quot;,
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;A chef tosses vegetables in a wok in a bright street-food kitchen, energetic handheld camera.&quot;
      }
    ],
    &quot;duration&quot;: 5,
    &quot;extra&quot;: {
      &quot;prompt_expansion_mode&quot;: &quot;disabled&quot;
    },
    &quot;ratio&quot;: &quot;9:16&quot;,
    &quot;resolution&quot;: &quot;480P&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Quality Prompt Expansion</strong>
<p>Prioritize prompt expansion quality for a detailed 768P scene.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;A detailed miniature railway travels through a glowing underground crystal cavern, with tiny passengers looking out of the windows.&quot;
      }
    ],
    &quot;duration&quot;: 8,
    &quot;extra&quot;: {
      &quot;prompt_expansion_mode&quot;: &quot;quality&quot;
    },
    &quot;ratio&quot;: &quot;21:9&quot;,
    &quot;resolution&quot;: &quot;768P&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3-max/quality-prompt-expansion.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;task&quot;: {
      &quot;id&quot;: &quot;441805071421550&quot;,
      &quot;model&quot;: &quot;MiniMax-H3-Max&quot;,
      &quot;status&quot;: &quot;succeeded&quot;,
      &quot;created_at&quot;: 1789415588,
      &quot;updated_at&quot;: 1789415659,
      &quot;content&quot;: {
        &quot;url&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3-max/quality-prompt-expansion.mp4&quot;
      },
      &quot;resolution&quot;: &quot;768P&quot;,
      &quot;duration&quot;: 8,
      &quot;usage&quot;: {
        &quot;total_seconds&quot;: 8,
        &quot;input_seconds&quot;: 0,
        &quot;output_seconds&quot;: 8,
        &quot;input_image_count&quot;: 0
      },
      &quot;ratio&quot;: &quot;21:9&quot;,
      &quot;task_type&quot;: &quot;generation&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/h3-max&#x27;,
  {
    content: [
      {
        type: &#x27;text&#x27;,
        text: &#x27;A detailed miniature railway travels through a glowing underground crystal cavern, with tiny passengers looking out of the windows.&#x27;,
      },
    ],
    duration: 8,
    extra: { prompt_expansion_mode: &#x27;quality&#x27; },
    ratio: &#x27;21:9&#x27;,
    resolution: &#x27;768P&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/h3-max&quot;,
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;A detailed miniature railway travels through a glowing underground crystal cavern, with tiny passengers looking out of the windows.&quot;
      }
    ],
    &quot;duration&quot;: 8,
    &quot;extra&quot;: {
      &quot;prompt_expansion_mode&quot;: &quot;quality&quot;
    },
    &quot;ratio&quot;: &quot;21:9&quot;,
    &quot;resolution&quot;: &quot;768P&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>H3 Max Image to Video</strong>
<p>Animate a supplied first-frame image at 480P.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;The camera slowly pans across the scene while fabric and hair move naturally in the wind.&quot;
      },
      {
        &quot;type&quot;: &quot;image_url&quot;,
        &quot;image_url&quot;: {
          &quot;url&quot;: &quot;https://filecdn.minimax.chat/public/85c96368-6ead-4eae-af9c-116be878eac3.png&quot;
        },
        &quot;role&quot;: &quot;first_frame&quot;
      }
    ],
    &quot;duration&quot;: 5,
    &quot;extra&quot;: {
      &quot;prompt_expansion_mode&quot;: &quot;balanced&quot;
    },
    &quot;ratio&quot;: &quot;adaptive&quot;,
    &quot;resolution&quot;: &quot;480P&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3-max/h3-max-image-to-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;task&quot;: {
      &quot;id&quot;: &quot;441804606931065&quot;,
      &quot;model&quot;: &quot;MiniMax-H3-Max&quot;,
      &quot;status&quot;: &quot;succeeded&quot;,
      &quot;created_at&quot;: 1789415661,
      &quot;updated_at&quot;: 1789415668,
      &quot;content&quot;: {
        &quot;url&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3-max/h3-max-image-to-video.mp4&quot;
      },
      &quot;resolution&quot;: &quot;480P&quot;,
      &quot;duration&quot;: 5,
      &quot;usage&quot;: {
        &quot;total_seconds&quot;: 5,
        &quot;input_seconds&quot;: 0,
        &quot;output_seconds&quot;: 5,
        &quot;input_image_count&quot;: 1
      },
      &quot;ratio&quot;: &quot;adaptive&quot;,
      &quot;task_type&quot;: &quot;generation&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/h3-max&#x27;,
  {
    content: [
      {
        type: &#x27;text&#x27;,
        text: &#x27;The camera slowly pans across the scene while fabric and hair move naturally in the wind.&#x27;,
      },
      {
        type: &#x27;image_url&#x27;,
        image_url: {
          url: &#x27;https://filecdn.minimax.chat/public/85c96368-6ead-4eae-af9c-116be878eac3.png&#x27;,
        },
        role: &#x27;first_frame&#x27;,
      },
    ],
    duration: 5,
    extra: { prompt_expansion_mode: &#x27;balanced&#x27; },
    ratio: &#x27;adaptive&#x27;,
    resolution: &#x27;480P&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/h3-max&quot;,
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;The camera slowly pans across the scene while fabric and hair move naturally in the wind.&quot;
      },
      {
        &quot;type&quot;: &quot;image_url&quot;,
        &quot;image_url&quot;: {
          &quot;url&quot;: &quot;https://filecdn.minimax.chat/public/85c96368-6ead-4eae-af9c-116be878eac3.png&quot;
        },
        &quot;role&quot;: &quot;first_frame&quot;
      }
    ],
    &quot;duration&quot;: 5,
    &quot;extra&quot;: {
      &quot;prompt_expansion_mode&quot;: &quot;balanced&quot;
    },
    &quot;ratio&quot;: &quot;adaptive&quot;,
    &quot;resolution&quot;: &quot;480P&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>H3 Max Reference Images</strong>
<p>Use multiple reference images to guide a fast character generation.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;Create a short cinematic portrait of the character walking through a modern gallery, preserving the face and clothing from the references.&quot;
      },
      {
        &quot;type&quot;: &quot;image_url&quot;,
        &quot;image_url&quot;: {
          &quot;url&quot;: &quot;https://cdn.hailuoai.com/prod/hailuo_demo/testsets/h3_promo_eval_ref2va/gallery/sr_v2p26_trio_seed42_20260724/inputs/9d5c7a33fa6e_01_%E5%9B%BE1_MHGgbVga3o_gpt4o-image-1780651118146.png&quot;
        },
        &quot;role&quot;: &quot;reference_image&quot;
      },
      {
        &quot;type&quot;: &quot;image_url&quot;,
        &quot;image_url&quot;: {
          &quot;url&quot;: &quot;https://cdn.hailuoai.com/prod/hailuo_demo/testsets/h3_promo_eval_ref2va/gallery/sr_v2p26_trio_seed42_20260724/inputs/7af326902315_00_%E5%9B%BE2_YqtKbY1jpo_u4391985813_Young_male_wearing_cream_hoodie_and_dark_brown_sh_45d56ed0-d626-4c37-9a5b-77f51f374982_1.png&quot;
        },
        &quot;role&quot;: &quot;reference_image&quot;
      }
    ],
    &quot;duration&quot;: 5,
    &quot;extra&quot;: {
      &quot;prompt_expansion_mode&quot;: &quot;balanced&quot;
    },
    &quot;resolution&quot;: &quot;768P&quot;,
    &quot;ratio&quot;: &quot;16:9&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3-max/h3-max-reference-images.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;task&quot;: {
      &quot;id&quot;: &quot;441805100810489&quot;,
      &quot;model&quot;: &quot;MiniMax-H3-Max&quot;,
      &quot;status&quot;: &quot;succeeded&quot;,
      &quot;created_at&quot;: 1789415671,
      &quot;updated_at&quot;: 1789415685,
      &quot;content&quot;: {
        &quot;url&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3-max/h3-max-reference-images.mp4&quot;
      },
      &quot;resolution&quot;: &quot;768P&quot;,
      &quot;duration&quot;: 5,
      &quot;usage&quot;: {
        &quot;total_seconds&quot;: 5,
        &quot;input_seconds&quot;: 0,
        &quot;output_seconds&quot;: 5,
        &quot;input_image_count&quot;: 2
      },
      &quot;ratio&quot;: &quot;16:9&quot;,
      &quot;task_type&quot;: &quot;generation&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/h3-max&#x27;,
  {
    content: [
      {
        type: &#x27;text&#x27;,
        text: &#x27;Create a short cinematic portrait of the character walking through a modern gallery, preserving the face and clothing from the references.&#x27;,
      },
      {
        type: &#x27;image_url&#x27;,
        image_url: {
          url: &#x27;https://cdn.hailuoai.com/prod/hailuo_demo/testsets/h3_promo_eval_ref2va/gallery/sr_v2p26_trio_seed42_20260724/inputs/9d5c7a33fa6e_01_%E5%9B%BE1_MHGgbVga3o_gpt4o-image-1780651118146.png&#x27;,
        },
        role: &#x27;reference_image&#x27;,
      },
      {
        type: &#x27;image_url&#x27;,
        image_url: {
          url: &#x27;https://cdn.hailuoai.com/prod/hailuo_demo/testsets/h3_promo_eval_ref2va/gallery/sr_v2p26_trio_seed42_20260724/inputs/7af326902315_00_%E5%9B%BE2_YqtKbY1jpo_u4391985813_Young_male_wearing_cream_hoodie_and_dark_brown_sh_45d56ed0-d626-4c37-9a5b-77f51f374982_1.png&#x27;,
        },
        role: &#x27;reference_image&#x27;,
      },
    ],
    duration: 5,
    extra: { prompt_expansion_mode: &#x27;balanced&#x27; },
    resolution: &#x27;768P&#x27;,
    ratio: &#x27;16:9&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/h3-max&quot;,
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;Create a short cinematic portrait of the character walking through a modern gallery, preserving the face and clothing from the references.&quot;
      },
      {
        &quot;type&quot;: &quot;image_url&quot;,
        &quot;image_url&quot;: {
          &quot;url&quot;: &quot;https://cdn.hailuoai.com/prod/hailuo_demo/testsets/h3_promo_eval_ref2va/gallery/sr_v2p26_trio_seed42_20260724/inputs/9d5c7a33fa6e_01_%E5%9B%BE1_MHGgbVga3o_gpt4o-image-1780651118146.png&quot;
        },
        &quot;role&quot;: &quot;reference_image&quot;
      },
      {
        &quot;type&quot;: &quot;image_url&quot;,
        &quot;image_url&quot;: {
          &quot;url&quot;: &quot;https://cdn.hailuoai.com/prod/hailuo_demo/testsets/h3_promo_eval_ref2va/gallery/sr_v2p26_trio_seed42_20260724/inputs/7af326902315_00_%E5%9B%BE2_YqtKbY1jpo_u4391985813_Young_male_wearing_cream_hoodie_and_dark_brown_sh_45d56ed0-d626-4c37-9a5b-77f51f374982_1.png&quot;
        },
        &quot;role&quot;: &quot;reference_image&quot;
      }
    ],
    &quot;duration&quot;: 5,
    &quot;extra&quot;: {
      &quot;prompt_expansion_mode&quot;: &quot;balanced&quot;
    },
    &quot;resolution&quot;: &quot;768P&quot;,
    &quot;ratio&quot;: &quot;16:9&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>content</code></td><td>array</td><td>Required.</td></tr><tr><td><code>content[].type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content[].text</code></td><td>string</td><td>Required. Minimum length: 1</td></tr><tr><td><code>content[].type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content[].image_url</code></td><td>object</td><td>Required.</td></tr><tr><td><code>content[].image_url.url</code></td><td>string</td><td>Required. Minimum length: 1</td></tr><tr><td><code>content[].role</code></td><td>string</td><td>Values: first_frame, last_frame, reference_image</td></tr><tr><td><code>content[].type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content[].video_url</code></td><td>object</td><td>Required.</td></tr><tr><td><code>content[].video_url.url</code></td><td>string</td><td>Required. Minimum length: 1</td></tr><tr><td><code>content[].role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content[].type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content[].audio_url</code></td><td>object</td><td>Required.</td></tr><tr><td><code>content[].audio_url.url</code></td><td>string</td><td>Required. Minimum length: 1</td></tr><tr><td><code>content[].role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>duration</code></td><td>integer</td><td>Required. Minimum: 5; Maximum: 15</td></tr><tr><td><code>ratio</code></td><td>string</td><td>Values: adaptive, 21:9, 16:9, 4:3, 1:1, 3:4, 9:16</td></tr><tr><td><code>callback_url</code></td><td>string</td><td></td></tr><tr><td><code>resolution</code></td><td>string</td><td>Required. Values: 480P, 768P</td></tr><tr><td><code>extra</code></td><td>object</td><td></td></tr><tr><td><code>extra.prompt_expansion_mode</code></td><td>string</td><td>Required. Default: balanced; Values: disabled, balanced, quality</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>task</code></td><td>object</td><td>Required.</td></tr><tr><td><code>task.id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>task.model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>task.status</code></td><td>string</td><td>Required. Values: queued, running, succeeded, failed, cancelled</td></tr><tr><td><code>task.error</code></td><td>object</td><td></td></tr><tr><td><code>task.error.code</code></td><td>string</td><td>Required.</td></tr><tr><td><code>task.error.message</code></td><td>string</td><td>Required.</td></tr><tr><td><code>task.created_at</code></td><td>integer</td><td>Required. Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.updated_at</code></td><td>integer</td><td>Required. Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.content</code></td><td>object</td><td></td></tr><tr><td><code>task.content.url</code></td><td>string</td><td></td></tr><tr><td><code>task.content.prompt</code></td><td>string</td><td></td></tr><tr><td><code>task.resolution</code></td><td>string</td><td></td></tr><tr><td><code>task.duration</code></td><td>integer</td><td>Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.usage</code></td><td>object</td><td></td></tr><tr><td><code>task.usage.total_seconds</code></td><td>integer</td><td>Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.usage.input_seconds</code></td><td>integer</td><td>Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.usage.output_seconds</code></td><td>integer</td><td>Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.usage.input_image_count</code></td><td>integer</td><td>Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.usage.input_audio_seconds</code></td><td>integer</td><td>Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.usage.total_tokens</code></td><td>integer</td><td>Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.usage.prompt_tokens</code></td><td>integer</td><td>Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.usage.completion_tokens</code></td><td>integer</td><td>Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.ratio</code></td><td>string</td><td></td></tr><tr><td><code>task.task_type</code></td><td>string</td><td>Values: generation, regeneration, h3_context_ir</td></tr><tr><td><code>task.modality</code></td><td>string</td><td>Values: video, text</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/minimax/h3-max/schema-input.json)
- [Output schema](/ai/models/minimax/h3-max/schema-output.json)

