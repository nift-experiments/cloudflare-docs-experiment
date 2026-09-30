---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/minimax/h3/
  description: minimax/h3
  full_title: MiniMax H3 · Cloudflare AI docs
  head_html: <title>MiniMax H3 · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="minimax/h3"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/minimax/h3/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="MiniMax H3 · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="minimax/h3"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/minimax/h3/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/minimax/h3/#page","headline":"MiniMax H3 \u00b7 Cloudflare AI docs","description":"minimax/h3","url":"https://developers.cloudflare.com/ai/models/minimax/h3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/minimax/h3/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/minimax.svg" alt="Minimax logo" width="48" height="48">

<h1 id="minimax-h3">MiniMax H3</h1>

<p><code>minimax/h3</code></p>

A multimodal video generation model supporting text-to-video, first and last frame image-to-video, and reference-to-video generation with 768P and 2K output.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Video</td></tr>
<tr><th>Terms</th><td><a href="https://platform.minimax.io/docs/guides/terms-of-service.md">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Default (per second): 0.08, @768p (per second): 0.08, @2k (per second): 0.13</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Generate a cinematic 2K space-opera teaser from text.

<section class="model-example"><strong>Text to Video 2K</strong>
<p>Generate a cinematic 2K space-opera teaser from text.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;A cinematic space-opera teaser: a fleet jumps into hyperspace above a purple nebula while a lone captain watches from a glass observation deck.&quot;
      }
    ],
    &quot;duration&quot;: 5,
    &quot;ratio&quot;: &quot;16:9&quot;,
    &quot;resolution&quot;: &quot;2K&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3/text-to-video-2k.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;task&quot;: {
      &quot;id&quot;: &quot;441812275253329&quot;,
      &quot;model&quot;: &quot;MiniMax-H3&quot;,
      &quot;status&quot;: &quot;succeeded&quot;,
      &quot;created_at&quot;: 1789417263,
      &quot;updated_at&quot;: 1789417606,
      &quot;content&quot;: {
        &quot;url&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3/text-to-video-2k.mp4&quot;
      },
      &quot;resolution&quot;: &quot;2K&quot;,
      &quot;duration&quot;: 5,
      &quot;usage&quot;: {
        &quot;total_seconds&quot;: 5,
        &quot;input_seconds&quot;: 0,
        &quot;output_seconds&quot;: 5,
        &quot;input_image_count&quot;: 0,
        &quot;total_tokens&quot;: 260390,
        &quot;prompt_tokens&quot;: 0,
        &quot;completion_tokens&quot;: 260390
      },
      &quot;ratio&quot;: &quot;16:9&quot;,
      &quot;task_type&quot;: &quot;generation&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/h3&#x27;,
  {
    content: [
      {
        type: &#x27;text&#x27;,
        text: &#x27;A cinematic space-opera teaser: a fleet jumps into hyperspace above a purple nebula while a lone captain watches from a glass observation deck.&#x27;,
      },
    ],
    duration: 5,
    ratio: &#x27;16:9&#x27;,
    resolution: &#x27;2K&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/h3&quot;,
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;A cinematic space-opera teaser: a fleet jumps into hyperspace above a purple nebula while a lone captain watches from a glass observation deck.&quot;
      }
    ],
    &quot;duration&quot;: 5,
    &quot;ratio&quot;: &quot;16:9&quot;,
    &quot;resolution&quot;: &quot;2K&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>First Frame Image to Video</strong>
<p>Animate a supplied image as the first frame.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;Slowly push in while the leaves move gently in the breeze and warm sunlight flickers through the branches.&quot;
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
    &quot;resolution&quot;: &quot;768P&quot;,
    &quot;ratio&quot;: &quot;adaptive&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3/first-frame-image-to-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;task&quot;: {
      &quot;id&quot;: &quot;441814879252673&quot;,
      &quot;model&quot;: &quot;MiniMax-H3&quot;,
      &quot;status&quot;: &quot;succeeded&quot;,
      &quot;created_at&quot;: 1789417772,
      &quot;updated_at&quot;: 1789417915,
      &quot;content&quot;: {
        &quot;url&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3/first-frame-image-to-video.mp4&quot;
      },
      &quot;resolution&quot;: &quot;768P&quot;,
      &quot;duration&quot;: 5,
      &quot;usage&quot;: {
        &quot;total_seconds&quot;: 5,
        &quot;input_seconds&quot;: 0,
        &quot;output_seconds&quot;: 5,
        &quot;input_image_count&quot;: 1,
        &quot;total_tokens&quot;: 175765,
        &quot;prompt_tokens&quot;: 13020,
        &quot;completion_tokens&quot;: 162745
      },
      &quot;ratio&quot;: &quot;adaptive&quot;,
      &quot;task_type&quot;: &quot;generation&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/h3&#x27;,
  {
    content: [
      {
        type: &#x27;text&#x27;,
        text: &#x27;Slowly push in while the leaves move gently in the breeze and warm sunlight flickers through the branches.&#x27;,
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
    resolution: &#x27;768P&#x27;,
    ratio: &#x27;adaptive&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/h3&quot;,
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;Slowly push in while the leaves move gently in the breeze and warm sunlight flickers through the branches.&quot;
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
    &quot;resolution&quot;: &quot;768P&quot;,
    &quot;ratio&quot;: &quot;adaptive&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Last Frame Image to Video</strong>
<p>Generate a transition that ends on a supplied image.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;A paper airplane flies through a city at sunset and gently lands on the desk shown in the final frame.&quot;
      },
      {
        &quot;type&quot;: &quot;image_url&quot;,
        &quot;image_url&quot;: {
          &quot;url&quot;: &quot;https://filecdn.minimax.chat/public/97b7cd08-764e-4b8b-a7bf-87a0bd898575.jpeg&quot;
        },
        &quot;role&quot;: &quot;last_frame&quot;
      }
    ],
    &quot;duration&quot;: 6,
    &quot;resolution&quot;: &quot;768P&quot;,
    &quot;ratio&quot;: &quot;adaptive&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3/last-frame-image-to-video.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;task&quot;: {
      &quot;id&quot;: &quot;441808217669932&quot;,
      &quot;model&quot;: &quot;MiniMax-H3&quot;,
      &quot;status&quot;: &quot;succeeded&quot;,
      &quot;created_at&quot;: 1789416497,
      &quot;updated_at&quot;: 1789416694,
      &quot;content&quot;: {
        &quot;url&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3/last-frame-image-to-video.mp4&quot;
      },
      &quot;resolution&quot;: &quot;768P&quot;,
      &quot;duration&quot;: 6,
      &quot;usage&quot;: {
        &quot;total_seconds&quot;: 6,
        &quot;input_seconds&quot;: 0,
        &quot;output_seconds&quot;: 6,
        &quot;input_image_count&quot;: 1,
        &quot;total_tokens&quot;: 208314,
        &quot;prompt_tokens&quot;: 13020,
        &quot;completion_tokens&quot;: 195294
      },
      &quot;ratio&quot;: &quot;adaptive&quot;,
      &quot;task_type&quot;: &quot;generation&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/h3&#x27;,
  {
    content: [
      {
        type: &#x27;text&#x27;,
        text: &#x27;A paper airplane flies through a city at sunset and gently lands on the desk shown in the final frame.&#x27;,
      },
      {
        type: &#x27;image_url&#x27;,
        image_url: {
          url: &#x27;https://filecdn.minimax.chat/public/97b7cd08-764e-4b8b-a7bf-87a0bd898575.jpeg&#x27;,
        },
        role: &#x27;last_frame&#x27;,
      },
    ],
    duration: 6,
    resolution: &#x27;768P&#x27;,
    ratio: &#x27;adaptive&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/h3&quot;,
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;A paper airplane flies through a city at sunset and gently lands on the desk shown in the final frame.&quot;
      },
      {
        &quot;type&quot;: &quot;image_url&quot;,
        &quot;image_url&quot;: {
          &quot;url&quot;: &quot;https://filecdn.minimax.chat/public/97b7cd08-764e-4b8b-a7bf-87a0bd898575.jpeg&quot;
        },
        &quot;role&quot;: &quot;last_frame&quot;
      }
    ],
    &quot;duration&quot;: 6,
    &quot;resolution&quot;: &quot;768P&quot;,
    &quot;ratio&quot;: &quot;adaptive&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>First and Last Frame</strong>
<p>Create a controlled transition between supplied first and last frames.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;Show the character growing from childhood into adulthood through a continuous, emotional camera move.&quot;
      },
      {
        &quot;type&quot;: &quot;image_url&quot;,
        &quot;image_url&quot;: {
          &quot;url&quot;: &quot;https://filecdn.minimax.chat/public/fe9d04da-f60e-444d-a2e0-18ae743add33.jpeg&quot;
        },
        &quot;role&quot;: &quot;first_frame&quot;
      },
      {
        &quot;type&quot;: &quot;image_url&quot;,
        &quot;image_url&quot;: {
          &quot;url&quot;: &quot;https://filecdn.minimax.chat/public/97b7cd08-764e-4b8b-a7bf-87a0bd898575.jpeg&quot;
        },
        &quot;role&quot;: &quot;last_frame&quot;
      }
    ],
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;2K&quot;,
    &quot;ratio&quot;: &quot;adaptive&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3/first-and-last-frame.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;task&quot;: {
      &quot;id&quot;: &quot;441811301478471&quot;,
      &quot;model&quot;: &quot;MiniMax-H3&quot;,
      &quot;status&quot;: &quot;succeeded&quot;,
      &quot;created_at&quot;: 1789416926,
      &quot;updated_at&quot;: 1789417242,
      &quot;content&quot;: {
        &quot;url&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3/first-and-last-frame.mp4&quot;
      },
      &quot;resolution&quot;: &quot;2K&quot;,
      &quot;duration&quot;: 5,
      &quot;usage&quot;: {
        &quot;total_seconds&quot;: 5,
        &quot;input_seconds&quot;: 0,
        &quot;output_seconds&quot;: 5,
        &quot;input_image_count&quot;: 2,
        &quot;total_tokens&quot;: 286430,
        &quot;prompt_tokens&quot;: 26040,
        &quot;completion_tokens&quot;: 260390
      },
      &quot;ratio&quot;: &quot;adaptive&quot;,
      &quot;task_type&quot;: &quot;generation&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/h3&#x27;,
  {
    content: [
      {
        type: &#x27;text&#x27;,
        text: &#x27;Show the character growing from childhood into adulthood through a continuous, emotional camera move.&#x27;,
      },
      {
        type: &#x27;image_url&#x27;,
        image_url: {
          url: &#x27;https://filecdn.minimax.chat/public/fe9d04da-f60e-444d-a2e0-18ae743add33.jpeg&#x27;,
        },
        role: &#x27;first_frame&#x27;,
      },
      {
        type: &#x27;image_url&#x27;,
        image_url: {
          url: &#x27;https://filecdn.minimax.chat/public/97b7cd08-764e-4b8b-a7bf-87a0bd898575.jpeg&#x27;,
        },
        role: &#x27;last_frame&#x27;,
      },
    ],
    duration: 5,
    resolution: &#x27;2K&#x27;,
    ratio: &#x27;adaptive&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/h3&quot;,
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;Show the character growing from childhood into adulthood through a continuous, emotional camera move.&quot;
      },
      {
        &quot;type&quot;: &quot;image_url&quot;,
        &quot;image_url&quot;: {
          &quot;url&quot;: &quot;https://filecdn.minimax.chat/public/fe9d04da-f60e-444d-a2e0-18ae743add33.jpeg&quot;
        },
        &quot;role&quot;: &quot;first_frame&quot;
      },
      {
        &quot;type&quot;: &quot;image_url&quot;,
        &quot;image_url&quot;: {
          &quot;url&quot;: &quot;https://filecdn.minimax.chat/public/97b7cd08-764e-4b8b-a7bf-87a0bd898575.jpeg&quot;
        },
        &quot;role&quot;: &quot;last_frame&quot;
      }
    ],
    &quot;duration&quot;: 5,
    &quot;resolution&quot;: &quot;2K&quot;,
    &quot;ratio&quot;: &quot;adaptive&quot;
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Multiple Reference Images</strong>
<p>Use multiple reference images to preserve character appearance and style.</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;The character walks through a rainy city street, preserving the character&#x27;s appearance from the first reference and the visual style from the second.&quot;
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
    &quot;resolution&quot;: &quot;2K&quot;,
    &quot;ratio&quot;: &quot;16:9&quot;
  },
  &quot;output&quot;: {
    &quot;video&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3/multiple-reference-images.mp4&quot;
  },
  &quot;raw_response&quot;: {
    &quot;task&quot;: {
      &quot;id&quot;: &quot;441814469210409&quot;,
      &quot;model&quot;: &quot;MiniMax-H3&quot;,
      &quot;status&quot;: &quot;succeeded&quot;,
      &quot;created_at&quot;: 1789417917,
      &quot;updated_at&quot;: 1789418171,
      &quot;content&quot;: {
        &quot;url&quot;: &quot;https://examples.aig.cloudflare.com/minimax/h3/multiple-reference-images.mp4&quot;
      },
      &quot;resolution&quot;: &quot;2K&quot;,
      &quot;duration&quot;: 5,
      &quot;usage&quot;: {
        &quot;total_seconds&quot;: 5,
        &quot;input_seconds&quot;: 0,
        &quot;output_seconds&quot;: 5,
        &quot;input_image_count&quot;: 2,
        &quot;total_tokens&quot;: 286430,
        &quot;prompt_tokens&quot;: 26040,
        &quot;completion_tokens&quot;: 260390
      },
      &quot;ratio&quot;: &quot;16:9&quot;,
      &quot;task_type&quot;: &quot;generation&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;minimax/h3&#x27;,
  {
    content: [
      {
        type: &#x27;text&#x27;,
        text: &quot;The character walks through a rainy city street, preserving the character&#x27;s appearance from the first reference and the visual style from the second.&quot;,
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
    resolution: &#x27;2K&#x27;,
    ratio: &#x27;16:9&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;minimax/h3&quot;,
  &quot;input&quot;: {
    &quot;content&quot;: [
      {
        &quot;type&quot;: &quot;text&quot;,
        &quot;text&quot;: &quot;The character walks through a rainy city street, preserving the character&#x27;\&#x27;&#x27;s appearance from the first reference and the visual style from the second.&quot;
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
    &quot;resolution&quot;: &quot;2K&quot;,
    &quot;ratio&quot;: &quot;16:9&quot;
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>content</code></td><td>array</td><td>Required.</td></tr><tr><td><code>content[].type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content[].text</code></td><td>string</td><td>Required. Minimum length: 1</td></tr><tr><td><code>content[].type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content[].image_url</code></td><td>object</td><td>Required.</td></tr><tr><td><code>content[].image_url.url</code></td><td>string</td><td>Required. Minimum length: 1</td></tr><tr><td><code>content[].role</code></td><td>string</td><td>Values: first_frame, last_frame, reference_image</td></tr><tr><td><code>content[].type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content[].video_url</code></td><td>object</td><td>Required.</td></tr><tr><td><code>content[].video_url.url</code></td><td>string</td><td>Required. Minimum length: 1</td></tr><tr><td><code>content[].role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content[].type</code></td><td>string</td><td>Required.</td></tr><tr><td><code>content[].audio_url</code></td><td>object</td><td>Required.</td></tr><tr><td><code>content[].audio_url.url</code></td><td>string</td><td>Required. Minimum length: 1</td></tr><tr><td><code>content[].role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>resolution</code></td><td>string</td><td>Required. Values: 768P, 2K</td></tr><tr><td><code>duration</code></td><td>integer</td><td>Required. Minimum: 4; Maximum: 15</td></tr><tr><td><code>ratio</code></td><td>string</td><td>Values: adaptive, 21:9, 16:9, 4:3, 1:1, 3:4, 9:16</td></tr><tr><td><code>callback_url</code></td><td>string</td><td></td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>task</code></td><td>object</td><td>Required.</td></tr><tr><td><code>task.id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>task.model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>task.status</code></td><td>string</td><td>Required. Values: queued, running, succeeded, failed, cancelled</td></tr><tr><td><code>task.error</code></td><td>object</td><td></td></tr><tr><td><code>task.error.code</code></td><td>string</td><td>Required.</td></tr><tr><td><code>task.error.message</code></td><td>string</td><td>Required.</td></tr><tr><td><code>task.created_at</code></td><td>integer</td><td>Required. Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.updated_at</code></td><td>integer</td><td>Required. Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.content</code></td><td>object</td><td></td></tr><tr><td><code>task.content.url</code></td><td>string</td><td></td></tr><tr><td><code>task.content.prompt</code></td><td>string</td><td></td></tr><tr><td><code>task.resolution</code></td><td>string</td><td></td></tr><tr><td><code>task.duration</code></td><td>integer</td><td>Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.usage</code></td><td>object</td><td></td></tr><tr><td><code>task.usage.total_seconds</code></td><td>integer</td><td>Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.usage.input_seconds</code></td><td>integer</td><td>Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.usage.output_seconds</code></td><td>integer</td><td>Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.usage.input_image_count</code></td><td>integer</td><td>Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.usage.input_audio_seconds</code></td><td>integer</td><td>Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.usage.total_tokens</code></td><td>integer</td><td>Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.usage.prompt_tokens</code></td><td>integer</td><td>Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.usage.completion_tokens</code></td><td>integer</td><td>Minimum: -9007199254740991; Maximum: 9007199254740991</td></tr><tr><td><code>task.ratio</code></td><td>string</td><td></td></tr><tr><td><code>task.task_type</code></td><td>string</td><td>Values: generation, regeneration, h3_context_ir</td></tr><tr><td><code>task.modality</code></td><td>string</td><td>Values: video, text</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/minimax/h3/schema-input.json)
- [Output schema](/ai/models/minimax/h3/schema-output.json)

