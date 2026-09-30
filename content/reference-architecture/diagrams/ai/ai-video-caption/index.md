<h2 id="introduction">Introduction</h2>
<p>Automatic Speech Recognition (ASR) models have revolutionized the accessibility of video content by enabling the generation of subtitles and translations. These models utilize advanced algorithms to transcribe spoken words into text with high accuracy. By integrating ASR technology into video platforms, content creators, publishers, and distributors can reach a broader audience, including individuals with hearing impairments or those who prefer to consume content in different languages.</p>
<p>The process begins with capturing the audio from the video source, which is then fed into the ASR model. This model analyzes the audio waveform and converts it into a textual representation, capturing the spoken content in the form of subtitles. Furthermore, you can also use ASR models for language translation, enabling the creation of multilingual subtitles. Once the subtitles are generated, they can be displayed alongside the video, providing a synchronized text representation of the spoken content.</p>
<h2 id="automatic-captioning-on-upload">Automatic captioning on upload</h2>
<p><img src="/assets/upstream/images/reference-architecture/ai-auto-caption-architecture-diagrams/ai-auto-caption-architecture-diagram.svg" alt="Figure 1: Automatic captioning on upload" title="Figure 1:  Automatic captioning on upload" /></p>
<ol>
<li><strong>Client upload</strong>: Send POST request with both video and audio to API endpoint.</li>
<li><strong>Audio transcription</strong>: Generate timestamped transcriptions by calling <a href="/workers-ai/">Workers AI</a> <a href="/workers-ai/models/">automatic speech recognition (ARS) model</a> with audio as input. Use <a href="/workers/">Workers</a> to convert the output to a supported subtitled format.</li>
<li><strong>Store subtitles</strong>: Store the subtitle file(s) on <a href="/r2/">R2</a>.</li>
<li><strong>Store video</strong>: Store the video files on <a href="/r2/">R2</a>.</li>
<li><strong>Client request</strong>: Send GET requests for video and subtitle(s) to origin. Use global <a href="/cache/">Cache</a> to increase performance.</li>
<li><strong>Origin request</strong>: Fetch file(s) from <a href="/r2/">R2</a> on cache <code>MISS</code> by using <a href="/r2/buckets/public-buckets/">Public Buckets</a>.</li>
</ol>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://auto-caption.pages.dev/">Community project: automatic captioning demo</a></li>
<li><a href="/workers-ai/models/">Workers AI: Automatic speech recognition (ARS) model</a></li>
<li><a href="/r2/">R2: Object storage for all your data</a></li>
</ul>
