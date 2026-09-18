/* CP2 theme contract shell JS for the Cloudflare Docs -> Nift port.
   Mirrors upstream BaseLayout.astro pre-paint preference handling:
   key ui-mode, values light|dark|auto, data-mode/data-theme attrs. */
(function () {
  var KEY = "ui-mode";
  function apply(mode) {
    var el = document.documentElement;
    var resolved = mode === "auto"
      ? (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light")
      : mode;
    el.setAttribute("data-mode", mode);
    el.setAttribute("data-theme", resolved);
    el.setAttribute("data-nb-pref", mode);
    el.setAttribute("data-nb-state", resolved);
  }
  var stored = null;
  try { stored = localStorage.getItem(KEY); } catch (e) {}
  apply(stored || "auto");
  document.addEventListener("click", function (ev) {
    var btn = ev.target.closest && ev.target.closest("[data-theme-toggle]");
    if (!btn) return;
    var order = ["auto", "light", "dark"];
    var cur = document.documentElement.getAttribute("data-mode") || "auto";
    var next = order[(order.indexOf(cur) + 1) % order.length];
    try { localStorage.setItem(KEY, next); } catch (e) {}
    apply(next);
  });
  if (window.matchMedia) {
    window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function () {
      var cur = document.documentElement.getAttribute("data-mode") || "auto";
      if (cur === "auto") apply("auto");
    });
  }
})();