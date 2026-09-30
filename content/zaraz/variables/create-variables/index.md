<p>Variables are reusable blocks of information. They allow you to have one source of data you can reuse across tools and triggers in the dashboard. You can then update this data in a single place.</p>
<p>For example, instead of typing a specific user ID in multiple fields, you can create a variable with that information instead. If there is a change and you have to update the user ID, you just need to update the variable and the change will be reflected across the dashboard.</p>
<p><a href="/zaraz/variables/worker-variables/">Worker Variables</a> are a special type of variable that generates value dynamically.</p>
<h2 id="create-a-new-variable">Create a new variable</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Tag setup</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Go to **Tools Configuration** > **Variables**.
3. Select **Create variable**, and give it a name.
4. In **Variable type** select between `String`, `Masked variable` or `Worker` from the drop-down menu. Use `Masked variable` when you have a private value that you do not want to share, such as an API token.
5. In **Variable value** enter the value of your variable.
6. Select **Save**.
<p>Your variable is now ready to be used with tools and triggers.</p>
<h2 id="next-steps">Next steps</h2>
<p>Refer to <a href="/zaraz/get-started/">Add a third-party tool</a> and <a href="/zaraz/custom-actions/create-trigger/">Create a trigger</a> for more information on how to add a variable to tools and triggers.</p>
<p>If you need to edit or delete variables, refer to <a href="/zaraz/variables/edit-variables/">Edit variables</a>.</p>
