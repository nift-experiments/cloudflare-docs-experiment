<p>RealtimeKit's UI Kit provides all the necessary UI components to allow complete customization of all its UI Kit components. You can customize your meeting icons such as chat, clock, leave meeting, mic on and off, and more.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To get started with customizing the icons for your meetings, you need to first integrate RealtimeKit's Web SDK into your web application.</p>
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<h2 id="customize-the-default-icon-pack">Customize the default icon pack</h2>
<p>RealtimeKit's default icon set is available at <a href="https://icons.realtime.cloudflare.com/">icons.realtime.cloudflare.com</a>. You can modify and generate your custom icon set from there.</p>
<p>To replace RealtimeKit's default icon set with your own, pass the link to your icon set in the UI component.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12651.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12652.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12653.md")
</div>
<h2 id="iconpack-reference">IconPack reference</h2>
<p>The IconPack is an object where:</p>
<ul>
<li><strong>Object key</strong> - Denotes the name of the icon</li>
<li><strong>Object value</strong> - Stores the SVG string</li>
</ul>
<h3 id="available-icons">Available icons</h3>
<p>The default icon pack includes the following icons:</p>
<ul>
<li><code>attach</code></li>
<li><code>call_end</code></li>
<li><code>chat</code></li>
<li><code>checkmark</code></li>
<li><code>chevron_down</code></li>
<li><code>chevron_left</code></li>
<li><code>chevron_right</code></li>
<li><code>chevron_up</code></li>
<li><code>clock</code></li>
<li><code>copy</code></li>
<li><code>disconnected</code></li>
<li><code>dismiss</code></li>
<li><code>download</code></li>
<li><code>emoji_multiple</code></li>
<li><code>full_screen_maximize</code></li>
<li><code>full_screen_minimize</code></li>
<li><code>image</code></li>
<li><code>image_off</code></li>
<li><code>join_stage</code></li>
<li><code>leave_stage</code></li>
<li><code>mic_off</code></li>
<li><code>mic_on</code></li>
<li><code>more_vertical</code></li>
<li><code>participants</code></li>
<li><code>people</code></li>
<li><code>pin</code></li>
<li><code>pin_off</code></li>
<li><code>poll</code></li>
<li><code>recording</code></li>
<li><code>rocket</code></li>
<li><code>search</code></li>
<li><code>send</code></li>
<li><code>settings</code></li>
<li><code>share</code></li>
<li><code>share_screen_person</code></li>
<li><code>share_screen_start</code></li>
<li><code>share_screen_stop</code></li>
<li><code>speaker</code></li>
<li><code>spinner</code></li>
<li><code>spotlight</code></li>
<li><code>stop_recording</code></li>
<li><code>subtract</code></li>
<li><code>vertical_scroll</code></li>
<li><code>vertical_scroll_disabled</code></li>
<li><code>video_off</code></li>
<li><code>video_on</code></li>
<li><code>wand</code></li>
<li><code>warning</code></li>
<li><code>wifi</code></li>
</ul>
<p>Each icon in your custom icon pack JSON file should be defined as a key-value pair where the key matches one of the icon names above, and the value is the SVG string for that icon.</p>
<h2 id="next-steps">Next steps</h2>
<p>Explore additional customization options:</p>
<ul>
<li><a href="/realtime/realtimekit/ui-kit/">Render Default Meeting UI</a> - Complete meeting experience out of the box</li>
<li><a href="/realtime/realtimekit/ui-kit/build-your-own-ui/">Build Your Own UI</a> - Create custom meeting interfaces</li>
</ul>
