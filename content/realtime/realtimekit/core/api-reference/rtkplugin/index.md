<!-- Auto Generated Below -->
<p><a name="module_RTKPlugin"></a></p>
<p>The RTKPlugin module represents a single plugin in the meeting.
A plugin can be obtained from one of the plugin arrays in <code>meeting.plugins</code>.
For example,</p>
<pre><code class="language-ts">const plugin1 = meeting.plugins.active.get(pluginId);&#10;const plugin2 = meeting.plugins.all.get(pluginId);&#10;</code></pre>
<ul>
<li><a href="#module_RTKPlugin">RTKPlugin</a>
<ul>
<li><a href="#module_RTKPlugin+component">.component</a></li>
<li><a href="#module_RTKPlugin+activateForSelf">.activateForSelf()</a></li>
<li><a href="#module_RTKPlugin+deactivateForSelf">.deactivateForSelf()</a></li>
<li><a href="#module_RTKPlugin+activate">.activate()</a></li>
<li><a href="#module_RTKPlugin+deactivate">.deactivate()</a></li>
</ul>
</li>
</ul>
<p><a name="module_RTKPlugin+component"></a></p>
<h3 id="plugin-component">plugin.component</h3>
The component for this plugin, as provided in the plugin config.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKPlugin"><code>RTKPlugin</code></a><br />
<a name="module_RTKPlugin+activateForSelf"></a></p>
<h3 id="plugin-activateforself">plugin.activateForSelf()</h3>
**Kind**: instance method of [<code>RTKPlugin</code>](#module_RTKPlugin)  
<a name="module_RTKPlugin+deactivateForSelf"></a>
<h3 id="plugin-deactivateforself">plugin.deactivateForSelf()</h3>
**Kind**: instance method of [<code>RTKPlugin</code>](#module_RTKPlugin)  
<a name="module_RTKPlugin+activate"></a>
<h3 id="plugin-activate">plugin.activate()</h3>
Activate this plugin for all participants.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKPlugin"><code>RTKPlugin</code></a><br />
<a name="module_RTKPlugin+deactivate"></a></p>
<h3 id="plugin-deactivate">plugin.deactivate()</h3>
Deactivate this plugin for all participants.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKPlugin"><code>RTKPlugin</code></a></p>
