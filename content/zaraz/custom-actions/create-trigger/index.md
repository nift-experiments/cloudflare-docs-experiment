<p>Triggers define the conditions under which a tool will start an action. Since a tool must have actions in order to work, and actions must have triggers, it is important to set up your website's triggers correctly. A trigger can be made out of one or more Rules. Zaraz supports <a href="/zaraz/reference/triggers/">multiple types of Trigger Rules</a>.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Tag setup</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Go to **Tools Configuration**.
3. Select the **Triggers** tab.
4. Select **Create trigger**.
5. In **Trigger Name** enter a descriptive name for your trigger.
6. In **Rule type**, choose from the actions available in the drop-down menu to start building your rule. Refer to [Triggers and rules](/zaraz/reference/triggers/) for more information on what each rule type means.
7. In **Variable name**, input the variable you want as the trigger. For example, use _Event Name_ if you are using [`zaraz.track()`](/zaraz/web-api/track/) in your website. If you want to use a variable you have previously [created in Variables](/zaraz/variables/create-variables/), select the `+` sign in the drop-down menu, scroll to **Variables**, and choose your variable.
8. Use the **Match operation** drop-down list to choose a comparison operator. For an expression to match, the value in **Variable name** and **Match string** must satisfy the comparison operator.
9. In **Match string**, input the string that completes the rule.
10. You can add more than one rule to your trigger. Select **Add rule** and repeat steps 5-8 to add another set of rules and conditions. If you add more than one rule, your trigger will only be valid when all conditions are true.
11. Select **Save**.
<p>Your trigger is now complete. If you go back to the main page you will see it listed under <strong>Triggers</strong>, as well as which tools use it. You can also <a href="/zaraz/custom-actions/edit-triggers/"><strong>Edit</strong> or <strong>Delete</strong> your trigger</a>.</p>
