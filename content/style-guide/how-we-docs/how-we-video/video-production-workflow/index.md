<p>We follow a specific workflow and formatting specifications for our videos to ensure they are accurate, engaging, scalable and align with the Cloudflare Docs style guide.</p>
<h2 id="formatting-specifications">Formatting specifications</h2>
<p>We use the following formatting specifications to uphold quality and consistency across our videos.</p>
<h3 id="resolution">Resolution</h3>
<p>Videos should be recorded at 4K UHD. If 4K UHD is unavailable, Full HD footage may be accepted on a case-by-case basis. Footage below Full HD will not be used. Final video exports must be at least Full HD.</p>
<p><strong>Acceptable resolutions:</strong></p>
<ul>
<li>4K Ultra HD: 2160p (3840x2160)</li>
<li>2K Quad HD: 1440p (2560x1440)</li>
<li>Full HD: 1080p (1920x1080)</li>
</ul>
<p><strong>Frame rate:</strong> 25 frames per second (FPS)</p>
<h3 id="screen-recording-resolution">Screen recording resolution</h3>
<p>Screen recordings should be done on the largest monitor possible, with the highest resolution available to the recording software (minimum 1920x1080). Ensure that any text visible on your screen is large enough that it can be easily read in the final video.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/14672.md")
</aside>
<h3 id="aspect-ratios">Aspect ratios</h3>
<p>Aspect ratio is important for the viewing experience. The more a video fills the screen, the more immersive an experience it provides.</p>
<p><strong>Desktop aspect ratio</strong></p>
<p>The most common screens and online platforms, such as YouTube and Vimeo, use a 16:9 ratio, so the majority of videos should be produced in a 16:9 ratio.</p>
<p><strong>Mobile aspect ratio</strong></p>
<p>Social media platforms, like Instagram or Facebook, are typically accessed on mobile devices and usually require a 9x16 aspect ratio. Efficiency calls for a 1:1 aspect ratio, which works on all, but not as great.</p>
<h3 id="subtitles">Subtitles</h3>
<p>Subtitles are always published in English in SubRip format <code>.srt</code>.</p>
<p><strong>Guidelines for subtitles:</strong></p>
<ul>
<li>Maximum 45 characters per line.</li>
<li>Split over 2 lines when necessary.</li>
<li>Displayed for no longer than 10 seconds per subtitle.</li>
</ul>
<h3 id="music">Music</h3>
<p>To maintain a balanced audio mix:</p>
<ul>
<li>Music should be about 20dB lower than speaking volume.</li>
<li>Background music must be instrumental, ensuring it does not overpower the speaker.</li>
</ul>
<h2 id="preparation-for-your-shoot">Preparation for your shoot</h2>
<h3 id="audio">Audio</h3>
<p><strong>Microphone placement</strong>: Clear and high quality audio is key to a good video. When setting up a microphone, it is best to have it as close to the speakers as possible to capture clear audio, and out of the frame so you cannot see it in the footage.</p>
<ul>
<li><strong>Shotgun microphones</strong>: Place the microphone over your head, just outside of the frame.</li>
<li><strong>Lavalier microphones</strong>: Hide cords and cables, but the microphone can be visible.</li>
</ul>
<p><strong>Background noise</strong>:
Choose a quiet and furnished room with soft surfaces to record your audio. Avoid locations with background noise and echo to the best of your ability. For example, avoid areas with fans, air-conditioning, and chatters, as these tend to get picked up by microphones.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="beware-of-echoes">Beware of echoes</h3>
@markup("md", "content/.markup/bodies/14671.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="check-for-echoes">Check for echoes</h3>
@markup("md", "content/.markup/bodies/14670.md")
</aside>
<h3 id="presenter">Presenter</h3>
<p><strong>Frame</strong></p>
<p>When setting up the presenter frame, the presenter should position themselves in the center of the shot with some distance from the wall behind them to create depth. They should ensure their eyeline is directly towards the lens, engaging with the audience, and avoid any reflections on their glasses that could distract from the presentation. This will help maintain a clear and professional look throughout the video.</p>
<p><strong>Dress Code</strong></p>
<p>To create the most professional and consistent appearance, the Video Experience team follows these dress code guidelines:</p>
<ul>
<li>Wear smart casual tops, like a Cloudflare T-shirt, polo, casual shirt, or sweater. Stick to solid, black and white, and jewel tones (for example, dark orange, emerald green, navy, burgundy).</li>
<li>Avoid distracting patterns, accessories, or flashy jewelry.</li>
<li>Do not wear non-affiliated branded clothing, especially from non-open-source companies.</li>
</ul>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="best-practices">Best practices</h3>
@markup("md", "content/.markup/bodies/14669.md")
</aside>
<h3 id="room-atmosphere">Room atmosphere</h3>
<p>For the best video quality, consider the following options for setting up your space:</p>
<ul>
<li>Option A: Choose a location with natural light and minimal echo. Add extra lighting if needed.</li>
<li>Option B: Set up a green screen. Ensure proper lighting to minimize shadows for the cleanest background.</li>
</ul>
<h2 id="production">Production</h2>
<h3 id="ai-assisted-video-production">AI-assisted video production</h3>
<p>We use AI as a tool across our workflow to accelerate and remove friction in various production stages (scripting, voiceovers, animations, metadata, and review), not to fully automate. We elaborate on how we use AI in each production stage in the respective pages. Refer to <a href="/style-guide/how-we-docs/how-we-ai/">How we AI</a> to understand more about our approach.</p>
<h3 id="topic-selection">Topic selection</h3>
<p>We create videos strategically when it improves users' understanding of the written documentation. Refer to <a href="/style-guide/how-we-docs/how-we-video/why-and-when-we-use-videos/">Why and when we use videos</a> to understand our approach to video content.
We also consider page views, support tickets, and community feedback when selecting video topics. Our videos always map back to a specific documentation need and refer to written documentation as the source of truth.</p>
<h3 id="script">Script</h3>
<p>Scripts are the blueprint for every video, guiding narration, on-screen text, and visual assets like animated illustration and diagrams. We use Cloudflare documentation as our source material to write scripts.</p>
<p>At Cloudflare, we use Gemini to accelerate script creation, followed by human review and editing the AI-generated draft to align with Cloudflare's voice, accuracy requirements, and visuals. The high-level process looks like the following:</p>
<ol>
<li>Generate initial script drafts based on an existing doc.</li>
<li>Experiment with tone, style, and length of narration.</li>
<li>Create variations for review, making editing faster than writing from scratch.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-1">Note</h3>
@markup("md", "content/.markup/bodies/14668.md")
</aside>
<h3 id="voiceover">Voiceover</h3>
<p>Voiceovers are an essential part of our video documentation workflow. They provide clarity, pacing, and engagement, complementing on-screen text and visuals. At Cloudflare, we leverage AI-assisted voice generation to streamline this process.</p>
<p>We use ElevenLabs, an AI voice generation tool, to produce natural-sounding voiceovers to:</p>
<ul>
<li>Quickly hear how your script sounds in real time.</li>
<li>Understand the cadence, timing, and clarity of narration</li>
<li>Speed up the stakeholder review process</li>
<li>Allows teams to create videos without a microphone</li>
<li>Supports early testing of pacing and integration with on-screen visuals</li>
</ul>
<h3 id="visuals">Visuals</h3>
<p>Visuals are the core of videos, providing context, reinforcing key concepts, and guiding the viewer through workflows. At Cloudflare, visuals include diagrams, animations, screen recording and talking head footage, all designed to complement the script and voiceover.</p>
<h4 id="diagrams">Diagrams</h4>
<p>Diagrams are used to clarify complex concepts or show relationships that are difficult to convey through text alone. Diagrams are referenced in the script and visually timed to appear alongside the corresponding narration.</p>
<h4 id="animation">Animation</h4>
<p>Animations bring diagrams and processes to life, helping users visualize dynamic workflows. Traditionally, creating animations involves keyframing, which requires specifying how objects move frame by frame. This is time-consuming and technical.</p>
<p>To speed up animation creation, we use AI:</p>
<ul>
<li>A simple prompt can generate the movement of objects without manually keyframing each frame.</li>
<li>AI-generated motion can be reused across multiple animations, saving time.</li>
<li>This approach allows motion graphics artists to focus on creative design rather than repetitive technical work.</li>
</ul>
<h4 id="screen-recording">Screen recording</h4>
<p>We use screen recordings when demonstrating real product interactions by capturing UI-driven workflows directly from Cloudflare dashboards or developer tools.</p>
<p>Best practices:</p>
<ul>
<li>Highlight relevant UI elements with callouts or overlays.</li>
<li>Voiceover should match to guide the viewer through steps.</li>
<li>Make sure UI elements shown are up-to-date.</li>
<li>Blur sensitive data.</li>
</ul>
<h4 id="talking-head">Talking head</h4>
<p>We use talking head footage when a human presence adds clarity, engagement and warmth, such as:</p>
<ul>
<li>Introducing a workflow or video segment</li>
<li>Providing context, emphasis, or commentary</li>
<li>Reinforcing Cloudflare branding and approachability</li>
</ul>
<p>Talking head footage is especially useful when voiceover alone cannot convey tone or emphasis, helping users connect with the content.</p>
<h2 id="review-and-quality-assurance">Review and quality assurance</h2>
<p>Every Cloudflare video undergoes a two-stage review process to ensure accuracy, clarity, and consistency with documentation standards. We leverage both human reviewers and AI tools to maintain high quality while enabling scalable production.</p>
<p>Scripts are reviewed before production to ensure:</p>
<ul>
<li>Technical accuracy – Explanations of concepts, workflows, and product behavior are correct.</li>
<li>UI and workflow accuracy – Steps described match the actual product.</li>
<li>Terminology alignment – Language matches Cloudflare documentation and branding.</li>
</ul>
<p>Once a video is produced, it undergoes a visual review to verify:</p>
<ul>
<li>Illustration matches narration – Diagrams, animations, and callouts align with spoken content.</li>
<li>Diagram accuracy – Architecture and conceptual diagrams correctly reflect the product.</li>
<li>Screen recording accuracy – UI navigation, workflows, and system outputs are correct.</li>
</ul>
<p>Cloudflare uses AI to enhance quality assurance by using saved prompts that remember your review preferences and focus areas, acting as a reviewer to ensuring consistent checks across projects:</p>
<ul>
<li>Immediate turnaround, even when human reviewers are unavailable</li>
<li>Reduces risk of errors and outdated information</li>
<li>Advanced image recognition supports maintenance by re-checking existing videos to see if UI or information has changed</li>
</ul>
<h2 id="metadata-and-discoverability">Metadata and discoverability</h2>
<p>Creating videos is only part of the story. To ensure our videos are findable, useful, and accessible, we apply structured metadata and AI-assisted tools to maximize discoverability for both human users and AI systems.</p>
<p>Before publishing, we generate rich metadata for each video:</p>
<ul>
<li>Title: Clear, descriptive, and aligned with documentation terminology</li>
<li>Description: Summarizes the content and context of the video</li>
<li>Chapters: Breaks the video into logical segments to improve understanding by AI</li>
<li>Transcripts and subtitles: Videos are hosted on Cloudflare Stream, we can generate captions automatically and download caption files <code>.vtt</code> as transcripts.</li>
</ul>
<p>This enables:</p>
<ul>
<li>Search indexing</li>
<li>AI retrieval</li>
<li>Generative Engine Optimization (GEO)</li>
</ul>
