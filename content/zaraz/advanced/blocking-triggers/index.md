<p>Blocking Triggers are triggers that instead of being used to define when to start an action, are used to define when to <em>not</em> start an action. You may need to block one or more actions in a tool from firing when a specific condition arises. For these cases, you can set Blocking Triggers.</p>
<p>Every tool action has Firing Triggers assigned to it. Blocking Triggers are optional and, if defined, will conditionally prevent the action from starting. When you add Blocking Triggers to an action, the action will not fire if any of its Blocking Triggers are true. If the tool has more than one action, other actions without these Blocking Triggers will still work.</p>
<p>To conditionally block all actions in a tool, you have to configure Blocking Triggers on every action that belongs to that tool. Note that when you use Blocking Triggers, Zaraz will still load on the page.</p>
<p>To use Blocking Triggers, start by <a href="/zaraz/custom-actions/create-trigger/">creating the trigger</a> with the conditions you want to use to block an event. Then:</p>
<ol>
<li>Go to <a href="https://dash.cloudflare.com/?to=/:account/:zone/zaraz"><strong>Zaraz</strong></a> &gt; <strong>Tools Configuration</strong>.</li>
<li>Under <strong>Third-party tools</strong>, locate the tool with the action you want to block and select <strong>Edit</strong>.</li>
<li>In <strong>Action Name</strong>, select the action you want to block.</li>
<li>In <strong>Blocking Triggers</strong>, use the dropdown menu to add a trigger to block the action.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17612.md")
</aside>
