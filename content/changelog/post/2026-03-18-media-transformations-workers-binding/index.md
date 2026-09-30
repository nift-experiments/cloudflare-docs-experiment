<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 18, 2026</time><h2 id="post-title">Media Transformations binding for Workers</h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>You can now use a Workers binding to transform videos with Media Transformations. This allows you to resize, crop, extract frames, and extract audio from videos stored anywhere, even in private locations like R2 buckets.</p>
<p>The Media Transformations binding is useful when you want to:</p>
<ul>
<li>Transform videos stored in private or protected sources</li>
<li>Optimize videos and store the output directly back to R2 for re-use</li>
<li>Extract still frames for classification or description with Workers AI</li>
<li>Extract audio tracks for transcription using Workers AI</li>
</ul>
<p>To get started, add the Media binding to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17754.md")</div>
<p>Then use the binding in your Worker to transform videos:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17755.md")</div>
<p>Output modes include <code>video</code> for optimized MP4 clips, <code>frame</code> for still images, <code>spritesheet</code> for multiple frames, and <code>audio</code> for M4A extraction.</p>
<p>For more information, refer to the <a href="/stream/transform-videos/bindings/">Media Transformations binding documentation</a>.</p>
</div></article></div>
