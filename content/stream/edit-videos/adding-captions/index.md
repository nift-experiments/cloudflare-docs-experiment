<p>Adding captions and subtitles to your video library.</p>
<h2 id="add-or-modify-a-caption">Add or modify a caption</h2>
<p>There are two ways to add captions to a video: generating via AI or uploading a
caption file.</p>
<p>To create or modify a caption on a video a <a href="https://www.cloudflare.com/a/account/my-account">Cloudflare API Token</a> is required.</p>
<p>The <code>&lt;LANGUAGE_TAG&gt;</code> must adhere to the <a href="http://www.unicode.org/reports/tr35/#Unicode_Language_and_Locale_Identifiers">BCP 47 format</a>. For convenience, many common
language codes are provided <a href="#most-common-language-codes">at the bottom of this document</a>.
If the language you are adding is not included in the table, you can find the
value through the <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">The IANA registry</a>, which maintains a list of language codes. To find the
value to send, search for the language. Below is an example value from IANA when
we look for the value to send for a Turkish subtitle:</p>
<pre><code class="language-bash">%%&#10;&#10;Subtag: tr&#10;Description: Turkish&#10;Added: 2005-10-16&#10;Suppress-Script: Latn&#10;%%&#10;</code></pre>
<p>The <code>Subtag</code> code indicates a value of <code>tr</code>. This is the value you should send
as the <code>language</code> at the end of the HTTP request.</p>
<p>A label is generated from the provided language. The label will be visible for
user selection in the player. For example, if sent <code>tr</code>, the label <code>Türkçe</code> will
be created; if sent <code>de</code>, the label <code>Deutsch</code> will be created.</p>
<h3 id="generate-a-caption">Generate a caption</h3>
<p>Generated captions use artificial intelligence based speech-to-text technology
to generate closed captions for your videos.</p>
<p>A video must be uploaded and in a ready state before captions can be generated.
In the following example URLs, the video's UID is referenced as <code>&lt;VIDEO_UID&gt;</code>.
To receive webhooks when a video transitions to ready after upload, follow the
instructions provided in <a href="/stream/manage-video-library/using-webhooks/">using webhooks</a>.</p>
<p>Captions can be generated for the following languages:</p>
<ul>
<li><code>cs</code> - Czech</li>
<li><code>nl</code> - Dutch</li>
<li><code>en</code> - English</li>
<li><code>fr</code> - French</li>
<li><code>de</code> - German</li>
<li><code>it</code> - Italian</li>
<li><code>ja</code> - Japanese</li>
<li><code>ko</code> - Korean</li>
<li><code>pl</code> - Polish</li>
<li><code>pt</code> - Portuguese</li>
<li><code>ru</code> - Russian</li>
<li><code>es</code> - Spanish</li>
</ul>
<p>When generating captions, generate them for the spoken language in the audio.</p>
<p>Videos may include captions for several languages, but each language must be unique.
For example, a video may have English, French, and German captions associated
with it, but it cannot have two English captions. If you have already uploaded
an English language caption for a video, you must first delete it in order to
create an English generated caption. Instructions on how to delete a caption can be found below.</p>
<p>The <code>&lt;LANGUAGE_TAG&gt;</code> must adhere to the BCP 47 format. The tag for English is <code>en</code>.
You may specify a region in the tag, such as <code>en-GB</code>, which will render a label
that shows <code>British English</code> for the caption.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14560.md")
</div></div>
<p>Example response:</p>
<pre><code class="language-json">{&#10;  &quot;result&quot;: {&#10;    &quot;language&quot;: &quot;en&quot;,&#10;    &quot;label&quot;: &quot;English (auto-generated)&quot;,&#10;    &quot;generated&quot;: true,&#10;    &quot;status&quot;: &quot;inprogress&quot;&#10;  },&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>The result will provide a <code>status</code> denoting the progress of the caption generation.<br />
There are three statuses: inprogress, ready, and error. Note that
(auto-generated) is applied to the label.</p>
<p>Once the generated caption is ready, it will automatically appear in the video
player and video manifest.</p>
<p>If the caption enters an error state, you may attempt to re-generate it by
first deleting it and then using the endpoint listed above.
Instructions on deletion are provided below.</p>
<h3 id="upload-a-file">Upload a file</h3>
<p>Note two changes if you edit a generated caption: the generated field will
change to <code>false</code> and the (auto-generated) portion of the label will be removed.</p>
<p>To create or replace a caption file:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14569.md")
</div></div>
<h3 id="example-response-to-add-or-modify-a-caption">Example Response to Add or Modify a Caption</h3>
<pre><code class="language-json">{&#10;  &quot;result&quot;: {&#10;    &quot;language&quot;: &quot;en&quot;,&#10;    &quot;label&quot;: &quot;English&quot;,&#10;    &quot;generated&quot;: false,&#10;    &quot;status&quot;: &quot;ready&quot;&#10;  },&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="list-the-captions-associated-with-a-video">List the captions associated with a video</h2>
<p>To view captions associated with a video.
Note this results list will also include generated captions that are <code>inprogress</code>
and <code>error</code> status:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14578.md")
</div></div>
<h3 id="example-response-to-get-the-captions-associated-with-a-video">Example response to get the captions associated with a video</h3>
<pre><code class="language-json">{&#10;  &quot;result&quot;: [&#10;    {&#10;      &quot;language&quot;: &quot;en&quot;,&#10;      &quot;label&quot;: &quot;English (auto-generated)&quot;,&#10;      &quot;generated&quot;: true,&#10;      &quot;status&quot;: &quot;inprogress&quot;&#10;    },&#10;    {&#10;      &quot;language&quot;: &quot;de&quot;,&#10;      &quot;label&quot;: &quot;Deutsch&quot;,&#10;      &quot;generated&quot;: false,&#10;      &quot;status&quot;: &quot;ready&quot;&#10;    }&#10;  ],&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="fetch-a-caption-file">Fetch a caption file</h2>
<p>To view the WebVTT caption file, you may make a GET request:</p>
<pre><code class="language-bash">curl \&#10;&#45;H &#x27;Authorization: Bearer &lt;API_TOKEN&gt;&#x27; \&#10;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/stream/&lt;VIDEO_UID&gt;/captions/&lt;LANGUAGE_TAG&gt;/vtt&#10;</code></pre>
<h3 id="example-response-to-get-the-caption-file-for-a-video">Example response to get the caption file for a video</h3>
<pre><code class="language-text">WEBVTT&#10;&#10;1&#10;00:00:00.000 --&gt; 00:00:01.560&#10;This is an example of&#10;&#10;2&#10;00:00:01.560 --&gt; 00:00:03.880&#10;a WebVTT caption response.&#10;</code></pre>
<h2 id="delete-the-captions">Delete the captions</h2>
<p>To remove a caption associated with your video:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14587.md")
</div></div>
<p>If there is an entry in <code>errors</code> response field, the caption has not been
deleted.</p>
<h3 id="example-response-to-delete-the-caption">Example response to delete the caption</h3>
<pre><code class="language-json">{&#10;  &quot;result&quot;: &quot;&quot;,&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="limitations">Limitations</h2>
<ul>
<li>A video must be uploaded before a caption can be attached to it. In the following
example URLs, the video's ID is referenced as <code>media_id</code>.</li>
<li>Stream only supports <a href="https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API">WebVTT</a>
formatted caption files. If you have a differently formatted caption file,
use <a href="https://subtitletools.com/convert-to-vtt-online">a tool to convert your file to WebVTT</a>
prior to uploading it.</li>
<li>Videos may include several language captions, but each language must be unique.
For example, a video may have English, French, and German captions associated
with it, but it cannot have two French captions.</li>
<li>Each caption file is limited to 10 MB in size. <a href="/support/contacting-cloudflare-support/">Contact support</a>
if you need to upload a larger file.</li>
</ul>
<h2 id="most-common-language-codes">Most common language codes</h2>
<table>
<thead>
<tr>
<th>Language Code</th>
<th>Language</th>
</tr>
</thead>
<tbody>
<tr>
<td>zh</td>
<td>Mandarin Chinese</td>
</tr>
<tr>
<td>hi</td>
<td>Hindi</td>
</tr>
<tr>
<td>es</td>
<td>Spanish</td>
</tr>
<tr>
<td>en</td>
<td>English</td>
</tr>
<tr>
<td>ar</td>
<td>Arabic</td>
</tr>
<tr>
<td>pt</td>
<td>Portuguese</td>
</tr>
<tr>
<td>bn</td>
<td>Bengali</td>
</tr>
<tr>
<td>ru</td>
<td>Russian</td>
</tr>
<tr>
<td>ja</td>
<td>Japanese</td>
</tr>
<tr>
<td>de</td>
<td>German</td>
</tr>
<tr>
<td>pa</td>
<td>Panjabi</td>
</tr>
<tr>
<td>jv</td>
<td>Javanese</td>
</tr>
<tr>
<td>ko</td>
<td>Korean</td>
</tr>
<tr>
<td>vi</td>
<td>Vietnamese</td>
</tr>
<tr>
<td>fr</td>
<td>French</td>
</tr>
<tr>
<td>ur</td>
<td>Urdu</td>
</tr>
<tr>
<td>it</td>
<td>Italian</td>
</tr>
<tr>
<td>tr</td>
<td>Turkish</td>
</tr>
<tr>
<td>fa</td>
<td>Persian</td>
</tr>
<tr>
<td>pl</td>
<td>Polish</td>
</tr>
<tr>
<td>uk</td>
<td>Ukrainian</td>
</tr>
<tr>
<td>my</td>
<td>Burmese</td>
</tr>
<tr>
<td>th</td>
<td>Thai</td>
</tr>
</tbody>
</table>
