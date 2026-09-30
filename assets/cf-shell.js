/* CP7 progressive-enhancement controllers for the Cloudflare Docs -> Nift port. */
(function () {
  "use strict";

  var THEME_KEY = "ui-mode";
  var THEMES = ["light", "dark", "auto"];
  var media = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)");

  function themePreference() {
    var value = null;
    try { value = localStorage.getItem(THEME_KEY); } catch (_error) {}
    return THEMES.indexOf(value) >= 0 ? value : "auto";
  }

  function applyTheme(preference) {
    if (THEMES.indexOf(preference) < 0) preference = "auto";
    var resolved = preference === "auto" ? (media && media.matches ? "dark" : "light") : preference;
    var root = document.documentElement;
    if (resolved === "dark") root.setAttribute("data-mode", "dark");
    else root.removeAttribute("data-mode");
    root.setAttribute("data-theme", resolved);
    root.setAttribute("data-nb-pref", preference);
    root.setAttribute("data-nb-state", resolved);
    root.style.colorScheme = resolved;
    var labels = { light: "dark", dark: "auto", auto: "light" };
    document.querySelectorAll("[data-theme-toggle]").forEach(function (button) {
      button.setAttribute("aria-label", "Theme: " + preference + ". Activate to switch to " + labels[preference] + ".");
      button.textContent = preference === "auto" ? "Theme: auto" : "Theme: " + resolved;
    });
  }

  applyTheme(themePreference());
  if (media) {
    var mediaChanged = function () { if (themePreference() === "auto") applyTheme("auto"); };
    if (media.addEventListener) media.addEventListener("change", mediaChanged);
    else if (media.addListener) media.addListener(mediaChanged);
  }
  window.addEventListener("storage", function (event) {
    if (event.key === THEME_KEY) applyTheme(themePreference());
  });

  function normalizePath(path) {
    path = (path || "/").split(/[?#]/)[0];
    if (!path.startsWith("/")) path = "/" + path;
    return path === "/" ? "/" : path.replace(/\/+$/, "") + "/";
  }

  function setThemeToggle() {
    applyTheme(themePreference());
    document.addEventListener("click", function (event) {
      var button = event.target.closest && event.target.closest("[data-theme-toggle]");
      if (!button) return;
      var current = themePreference();
      var next = THEMES[(THEMES.indexOf(current) + 1) % THEMES.length];
      try { localStorage.setItem(THEME_KEY, next); } catch (_error) {}
      applyTheme(next);
    });
  }

  function renderTree(container, nodes, context, state) {
    var list = document.createElement("ul");
    list.className = "sidebar-list";
    nodes.forEach(function (node) {
      var item = document.createElement("li");
      item.dataset.sidebarNode = node.id;
      item.dataset.searchText = node.searchText || node.label.toLowerCase();
      if (node.kind === "group") {
        item.className = "sidebar-group";
        var button = document.createElement("button");
        button.type = "button";
        button.className = "sidebar-group-toggle";
        button.dataset.sidebarGroup = node.id;
        button.textContent = node.label;
        var children = renderTree(document.createElement("div"), node.children, context, state);
        var forced = context.activeAncestorIds && context.activeAncestorIds.indexOf(node.id) >= 0;
        var open = forced || state.open[node.id] === true;
        button.setAttribute("aria-expanded", String(open));
        children.hidden = !open;
        button.addEventListener("click", function () {
          var next = button.getAttribute("aria-expanded") !== "true";
          button.setAttribute("aria-expanded", String(next));
          children.hidden = !next;
          state.open[node.id] = next;
          state.save();
        });
        item.appendChild(button);
        item.appendChild(children);
      } else {
        var link = document.createElement("a");
        link.href = node.href;
        link.textContent = node.label;
        if (node.external) { link.target = "_blank"; link.rel = "noopener"; }
        if (node.id === context.activeNodeId) {
          link.classList.add("active");
          link.setAttribute("aria-current", "page");
        }
        if (node.badge && node.badge.text) {
          var badge = document.createElement("span");
          badge.className = "sidebar-badge sidebar-badge-" + node.badge.variant;
          badge.textContent = node.badge.text;
          link.appendChild(badge);
        }
        item.appendChild(link);
      }
      list.appendChild(item);
    });
    container.appendChild(list);
    return list;
  }

  function sidebarState(product) {
    var key = "cp7-sidebar-state:" + product.id + ":" + product.treeHash;
    var stored = {};
    try { stored = JSON.parse(sessionStorage.getItem(key) || "{}"); } catch (_error) {}
    var state = { open: stored.open || {}, scroll: Number(stored.scroll || 0) };
    state.save = function () {
      try { sessionStorage.setItem(key, JSON.stringify({ open: state.open, scroll: state.scroll })); } catch (_error) {}
    };
    return state;
  }

  function bindSidebarFilter(sidebar) {
    var input = sidebar.querySelector("[data-sidebar-filter]");
    if (!input) return;
    function filter() {
      var query = input.value.trim().toLowerCase();
      sidebar.querySelectorAll(".sidebar-group").forEach(function (group) {
        var toggle = group.querySelector(":scope > [data-sidebar-group]");
        if (!toggle) return;
        if (query && group.dataset.filterOpen === undefined) group.dataset.filterOpen = toggle.getAttribute("aria-expanded");
        if (!query && group.dataset.filterOpen !== undefined) {
          var list = group.querySelector(":scope > .sidebar-list");
          toggle.setAttribute("aria-expanded", group.dataset.filterOpen);
          if (list) list.hidden = group.dataset.filterOpen !== "true";
          delete group.dataset.filterOpen;
        }
      });
      sidebar.querySelectorAll("[data-sidebar-node]").forEach(function (item) {
        item.hidden = query && item.dataset.searchText.indexOf(query) < 0;
      });
      if (query) {
        sidebar.querySelectorAll(".sidebar-group").forEach(function (group) {
          if (group.querySelector("[data-sidebar-node]:not([hidden])")) {
            group.hidden = false;
            var toggle = group.querySelector(":scope > [data-sidebar-group]");
            var list = group.querySelector(":scope > .sidebar-list");
            if (toggle && list) { toggle.setAttribute("aria-expanded", "true"); list.hidden = false; }
          }
        });
      }
    }
    input.addEventListener("input", filter);
    input.addEventListener("keydown", function (event) {
      if (event.key === "Escape") { input.value = ""; filter(); input.blur(); }
    });
    document.addEventListener("keydown", function (event) {
      var target = event.target;
      if (event.key === "/" && !event.metaKey && !event.ctrlKey &&
          !/^(INPUT|TEXTAREA|SELECT)$/.test(target.tagName) && !target.isContentEditable) {
        event.preventDefault(); input.focus();
      }
    });
  }

  function applyNavigation(data) {
    var path = normalizePath(location.pathname);
    var context = data.routes[path] || { activeNodeId: null, activeAncestorIds: [] };
    var product = data.product;
    var sidebar = document.querySelector("[data-shared-sidebar-nav]");
    var tree = sidebar && sidebar.querySelector("[data-sidebar-tree]");
    if (sidebar && tree && product) {
      var state = sidebarState(product);
      var nodes = product.children;
      if (product.id === "learning-paths" && context.activeAncestorIds && context.activeAncestorIds.length) {
        var owner = findNavigationNode(nodes, context.activeAncestorIds[0]);
        if (owner) nodes = owner.children;
      }
      tree.textContent = "";
      renderTree(tree, nodes, context, state);
      var title = sidebar.querySelector("[data-sidebar-product]");
      if (title) title.textContent = owner ? owner.label + " (Learning Paths)" : product.label;
      sidebar.scrollTop = state.scroll;
      sidebar.addEventListener("scroll", function () { state.scroll = sidebar.scrollTop; state.save(); }, { passive: true });
      bindSidebarFilter(sidebar);
      var active = sidebar.querySelector('[aria-current="page"]');
      if (active && !state.scroll) {
        sidebar.scrollTop = Math.max(0, active.offsetTop - sidebar.clientHeight / 2);
      }
    }
    renderBreadcrumbs(product, context);
    var pagination = document.querySelector("[data-pagination]");
    if (pagination && context) {
      pagination.textContent = "";
      [["previous", "Previous"], ["next", "Next"]].forEach(function (entry) {
        var item = context[entry[0]];
        if (!item) return;
        var link = document.createElement("a");
        link.href = item.href;
        link.className = "pagination-" + entry[0];
        link.innerHTML = "<small>" + entry[1] + "</small><strong></strong>";
        link.querySelector("strong").textContent = item.label;
        pagination.appendChild(link);
      });
    }
    document.querySelectorAll(".top-nav a").forEach(function (link) {
      if (normalizePath(link.getAttribute("href")) === path) link.setAttribute("aria-current", "page");
    });
  }

  function findNavigationNode(nodes, id) {
    for (var i = 0; i < nodes.length; i += 1) {
      if (nodes[i].id === id) return nodes[i];
      if (nodes[i].children) {
        var match = findNavigationNode(nodes[i].children, id);
        if (match) return match;
      }
    }
    return null;
  }

  function renderBreadcrumbs(product, context) {
    var breadcrumbs = document.querySelector("[data-breadcrumbs]");
    if (!breadcrumbs || !product || !context) return;
    var active = findNavigationNode(product.children, context.activeNodeId);
    var entries = [{ label: "Docs", href: "/" }, { label: product.label, href: product.root }];
    (context.activeAncestorIds || []).forEach(function (id) {
      var node = findNavigationNode(product.children, id);
      if (node) entries.push({ label: node.label, href: node.href });
    });
    if (active && active.route === product.root && !(context.activeAncestorIds || []).length) {
      entries[1].href = null;
    } else if (active) {
      entries.push({ label: active.label.replace(/ ↗$/, ""), href: null });
    }
    breadcrumbs.textContent = "";
    entries.forEach(function (entry, index) {
      if (index) {
        var separator = document.createElement("span"); separator.setAttribute("aria-hidden", "true"); separator.textContent = "/";
        breadcrumbs.appendChild(separator);
      }
      var element;
      if (entry.href && index < entries.length - 1) {
        element = document.createElement("a"); element.href = entry.href;
      } else {
        element = document.createElement("span");
        if (index === entries.length - 1) element.setAttribute("aria-current", "page");
      }
      element.textContent = entry.label;
      breadcrumbs.appendChild(element);
    });
  }

  function initNavigation() {
    var product = normalizePath(location.pathname).split("/")[1];
    if (!product) {
      fetch("/assets/navigation.json", { credentials: "same-origin" })
        .then(function (response) { if (!response.ok) throw new Error("navigation unavailable"); return response.json(); })
        .then(function (data) {
          var tree = document.querySelector("[data-sidebar-tree]");
          var title = document.querySelector("[data-sidebar-product]");
          if (!tree) return;
          tree.textContent = "";
          data.home.forEach(function (group) {
            var heading = document.createElement("h3"); heading.textContent = group.label; tree.appendChild(heading);
            group.links.forEach(function (item, index) { var link = document.createElement("a"); link.href = item.href; link.textContent = item.label; link.dataset.sidebarNode = "home:" + group.label + ":" + index; link.dataset.searchText = item.label.toLowerCase(); tree.appendChild(link); });
          });
          if (title) title.textContent = "Cloudflare products";
          bindSidebarFilter(document.querySelector("[data-shared-sidebar-nav]"));
        });
      return;
    }
    fetch("/assets/navigation/" + encodeURIComponent(product) + ".json", { credentials: "same-origin" })
      .then(function (response) { if (!response.ok) throw new Error("navigation unavailable"); return response.json(); })
      .then(applyNavigation)
      .catch(function () {
        var tree = document.querySelector("[data-sidebar-tree]");
        if (tree) tree.setAttribute("data-navigation-fallback", "true");
      });
  }

  function initAgentCatalog() {
    var buttons = Array.from(document.querySelectorAll("[data-agent-filter]"));
    var cards = Array.from(document.querySelectorAll("[data-agent-card]"));
    if (!buttons.length || !cards.length) return;
    buttons.forEach(function (button) {
      button.addEventListener("click", function () {
        var filter = button.dataset.agentFilter;
        buttons.forEach(function (item) { item.setAttribute("aria-pressed", String(item === button)); });
        cards.forEach(function (card) {
          card.hidden = filter !== "all" && (card.dataset.match || "").split(/\s+/).indexOf(filter) < 0;
        });
      });
    });
  }

  function initCatalogs() {
    var search = document.querySelector("[data-catalog-search]");
    var items = Array.from(document.querySelectorAll("[data-catalog-item]"));
    var groups = Array.from(document.querySelectorAll("[data-directory-group]"));
    if (!items.length || (!search && !groups.length)) return;
    var more = document.querySelector("[data-catalog-more]");
    var expanded = false;
    function apply() {
      var query = search ? search.value.trim().toLowerCase() : "";
      var selected = groups.filter(function (input) { return input.checked; }).map(function (input) { return input.value; });
      items.forEach(function (item, index) {
        var textMatches = !query || (item.dataset.searchText || item.textContent.toLowerCase()).indexOf(query) >= 0;
        var itemGroups = (item.dataset.groups || "").split("|");
        var groupMatches = !selected.length || selected.some(function (group) { return itemGroups.indexOf(group) >= 0; });
        var withinInitialGlossary = !more || expanded || query || index < 10;
        item.hidden = !textMatches || !groupMatches || !withinInitialGlossary;
      });
      if (more) more.hidden = Boolean(query) || expanded;
    }
    if (search) search.addEventListener("input", apply);
    groups.forEach(function (input) { input.addEventListener("change", apply); });
    if (more) more.addEventListener("click", function () { expanded = true; apply(); });
  }

  function initMobileSidebar() {
    var dialog = document.querySelector("[data-mobile-sidebar]");
    var menu = document.querySelector("[data-menu-btn]");
    var close = dialog && dialog.querySelector("[data-close-sidebar]");
    var slot = dialog && dialog.querySelector("[data-mobile-sidebar-slot]");
    var home = document.querySelector("[data-sidebar-home]");
    var sidebar = document.querySelector("[data-shared-sidebar-nav]");
    if (!dialog || !menu || !close || !slot || !home || !sidebar) return;
    var restoreFocus = null;
    function restoreSidebar() { if (sidebar.parentNode !== home) home.appendChild(sidebar); }
    function shut() {
      if (dialog.open) dialog.close();
      dialog.dataset.state = "closed";
      menu.setAttribute("aria-expanded", "false");
      document.body.removeAttribute("data-scroll-locked");
      restoreSidebar();
      if (restoreFocus) restoreFocus.focus();
    }
    menu.addEventListener("click", function () {
      restoreFocus = document.activeElement;
      slot.appendChild(sidebar);
      dialog.dataset.state = "open";
      menu.setAttribute("aria-expanded", "true");
      document.body.setAttribute("data-scroll-locked", "true");
      dialog.showModal();
      close.focus();
    });
    close.addEventListener("click", shut);
    dialog.addEventListener("cancel", function (event) { event.preventDefault(); shut(); });
    dialog.addEventListener("click", function (event) { if (event.target === dialog) shut(); });
    var desktop = window.matchMedia("(min-width: 1024px)");
    var resize = function () { if (desktop.matches) shut(); };
    if (desktop.addEventListener) desktop.addEventListener("change", resize);
  }

  function selectTab(root, index, persist) {
    var tabs = Array.from(root.querySelectorAll(":scope > [data-nb-tabs-list] > [role=tab]"));
    var panels = Array.from(root.querySelectorAll(":scope > [data-nb-tabs-panels] > [data-nb-tabs-content]"));
    if (!tabs.length || index < 0 || index >= tabs.length) return;
    tabs.forEach(function (tab, i) { tab.setAttribute("aria-selected", String(i === index)); tab.tabIndex = i === index ? 0 : -1; });
    panels.forEach(function (panel, i) { panel.hidden = i !== index; });
    var key = root.dataset.nbSyncKey;
    if (persist && key) {
      try { localStorage.setItem("ui-synced-tabs__" + key, panels[index].dataset.nbTabLabel); } catch (_error) {}
      document.dispatchEvent(new CustomEvent("nb-tabs-sync", { detail: { key: key, label: panels[index].dataset.nbTabLabel } }));
    }
  }

  function initTabs() {
    document.querySelectorAll("[data-nb-tabs]").forEach(function (root, rootIndex) {
      if (root.dataset.cfBound) return;
      root.dataset.cfBound = "true";
      var list = root.querySelector(":scope > [data-nb-tabs-list]");
      var panels = Array.from(root.querySelectorAll(":scope > [data-nb-tabs-panels] > [data-nb-tabs-content]"));
      if (!list || !panels.length) return;
      panels.forEach(function (panel, index) {
        var tab = document.createElement("button");
        var tabId = "nb-tabs-" + rootIndex + "-tab-" + index;
        var panelId = "nb-tabs-" + rootIndex + "-panel-" + index;
        tab.type = "button"; tab.role = "tab"; tab.id = tabId; tab.textContent = panel.dataset.nbTabLabel || "Tab " + (index + 1);
        tab.setAttribute("aria-controls", panelId);
        panel.id = panelId; panel.setAttribute("aria-labelledby", tabId);
        tab.addEventListener("click", function () { selectTab(root, index, true); });
        tab.addEventListener("keydown", function (event) {
          var next = index;
          if (event.key === "ArrowRight") next = (index + 1) % panels.length;
          else if (event.key === "ArrowLeft") next = (index - 1 + panels.length) % panels.length;
          else if (event.key === "Home") next = 0;
          else if (event.key === "End") next = panels.length - 1;
          else return;
          event.preventDefault(); selectTab(root, next, true); list.children[next].focus();
        });
        list.appendChild(tab);
      });
      var initial = 0;
      if (root.dataset.nbSyncKey) {
        var saved = null;
        try { saved = localStorage.getItem("ui-synced-tabs__" + root.dataset.nbSyncKey); } catch (_error) {}
        panels.forEach(function (panel, i) { if (panel.dataset.nbTabLabel === saved) initial = i; });
      }
      selectTab(root, initial, false);
    });
    document.addEventListener("nb-tabs-sync", function (event) {
      document.querySelectorAll('[data-nb-sync-key="' + CSS.escape(event.detail.key) + '"]').forEach(function (root) {
        var panels = Array.from(root.querySelectorAll(":scope > [data-nb-tabs-panels] > [data-nb-tabs-content]"));
        panels.forEach(function (panel, index) { if (panel.dataset.nbTabLabel === event.detail.label) selectTab(root, index, false); });
      });
    });
  }

  function writeClipboard(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text).catch(function () { return legacyCopy(text); });
    }
    return legacyCopy(text);
  }

  function legacyCopy(text) {
    var area = document.createElement("textarea"); area.value = text; area.style.position = "fixed"; area.style.opacity = "0";
    document.body.appendChild(area); area.select(); document.execCommand("copy"); area.remove();
    return Promise.resolve();
  }

  function copiedState(button) {
    var original = button.textContent;
    button.textContent = "Copied"; button.dataset.state = "copied";
    setTimeout(function () { button.textContent = original; delete button.dataset.state; }, 1500);
  }

  function initPackageManagers() {
    document.querySelectorAll("[data-nb-pm]").forEach(function (root, rootIndex) {
      var tabs = Array.from(root.querySelectorAll("[data-nb-pm-tab]"));
      var panels = Array.from(root.querySelectorAll("[data-nb-pm-panel]"));
      function choose(index, save) {
        tabs.forEach(function (tab, i) { tab.setAttribute("aria-selected", String(i === index)); tab.tabIndex = i === index ? 0 : -1; });
        panels.forEach(function (panel, i) { panel.hidden = i !== index; });
        if (save) {
          var label = tabs[index].textContent.trim();
          try { sessionStorage.setItem("ui-pm-tab", label); } catch (_error) {}
          document.dispatchEvent(new CustomEvent("nb-pm-sync", { detail: { source: root, label: label } }));
        }
      }
      tabs.forEach(function (tab, index) {
        var tabId = "pm-" + rootIndex + "-tab-" + index, panelId = "pm-" + rootIndex + "-panel-" + index;
        tab.id = tabId; tab.setAttribute("aria-controls", panelId); panels[index].id = panelId; panels[index].setAttribute("aria-labelledby", tabId);
        tab.addEventListener("click", function () { choose(index, true); });
        tab.addEventListener("keydown", function (event) {
          var next = index;
          if (event.key === "ArrowRight") next = (index + 1) % tabs.length;
          else if (event.key === "ArrowLeft") next = (index - 1 + tabs.length) % tabs.length;
          else if (event.key === "Home") next = 0;
          else if (event.key === "End") next = tabs.length - 1;
          else return;
          event.preventDefault(); choose(next, true); tabs[next].focus();
        });
      });
      document.addEventListener("nb-pm-sync", function (event) {
        if (event.detail.source === root) return;
        var index = tabs.findIndex(function (tab) { return tab.textContent.trim() === event.detail.label; });
        if (index >= 0) choose(index, false);
      });
      var saved = null; try { saved = sessionStorage.getItem("ui-pm-tab"); } catch (_error) {}
      var initial = Math.max(0, tabs.findIndex(function (tab) { return tab.textContent.trim() === saved; }));
      if (tabs.length) choose(initial, false);
    });
  }

  function initCopy() {
    document.querySelectorAll(".docs-content pre").forEach(function (pre) {
      if (pre.closest("[data-nb-pm-panel]") || pre.querySelector(":scope > .nb-code-copy")) return;
      var code = pre.querySelector("code"); if (!code) return;
      var button = document.createElement("button"); button.type = "button"; button.className = "nb-code-copy"; button.textContent = "Copy"; button.setAttribute("aria-label", "Copy code to clipboard");
      button.addEventListener("click", function () { writeClipboard(code.textContent).then(function () { copiedState(button); }); });
      pre.appendChild(button);
    });
    document.addEventListener("click", function (event) {
      var pm = event.target.closest && event.target.closest("[data-nb-pm-copy]");
      if (pm) writeClipboard(pm.dataset.nbCommand || "").then(function () { copiedState(pm); });
    });
    var page = document.querySelector("[data-copy-page]");
    if (page) page.addEventListener("click", function () {
      var status = document.querySelector("[data-copy-page-status]");
      fetch("index.md").then(function (response) { if (!response.ok) throw new Error(); return response.text(); })
        .then(writeClipboard).then(function () { copiedState(page); if (status) status.textContent = "Page Markdown copied."; })
        .catch(function () { if (status) status.textContent = "Markdown source is unavailable for this generated page."; });
    });
  }

  function initStreamChapters() {
    document.addEventListener("click", function (event) {
      var button = event.target.closest && event.target.closest("[data-video-time]");
      if (!button) return;
      var details = button.closest(".video-chapters");
      var iframe = details && details.previousElementSibling && details.previousElementSibling.querySelector("iframe");
      if (!iframe) return;
      var seek = function () { if (window.Stream) window.Stream(iframe).currentTime = Number(button.dataset.videoTime); };
      if (window.Stream) { seek(); return; }
      var script = document.querySelector("[data-stream-sdk]");
      if (!script) {
        script = document.createElement("script");
        script.src = "https://embed.cloudflarestream.com/embed/sdk.latest.js";
        script.dataset.streamSdk = "";
        document.head.appendChild(script);
      }
      script.addEventListener("load", seek, { once: true });
    });
  }

  function initArticleTools() {
    var article = document.querySelector(".article-wrap");
    var heading = article && article.querySelector("h1");
    if (!article || !heading || article.querySelector("[data-article-tools]")) return;
    var tools = document.createElement("div");
    tools.className = "article-tools";
    tools.dataset.articleTools = "";
    tools.innerHTML = '<button type="button" data-copy-page>Copy as Markdown</button>' +
      '<span aria-hidden="true">|</span><a href="index.md" data-view-markdown>View as Markdown</a>' +
      '<span class="agent-setup-action" aria-hidden="true">|</span>' +
      '<a class="agent-setup-action" href="/agent-setup/">Agent setup</a>' +
      '<span class="sr-only" data-copy-page-status role="status" aria-live="polite"></span>';
    var headingContainer = heading.closest(".article-header") || heading;
    var summary = article.querySelector(".article-summary");
    if (summary) headingContainer.insertAdjacentElement("afterend", summary);
    (summary || headingContainer).insertAdjacentElement("afterend", tools);
    var mobileToc = document.querySelector("[data-mobile-toc]");
    if (mobileToc) tools.insertAdjacentElement("afterend", mobileToc);
  }

  function initTOC() {
    var headings = Array.from(document.querySelectorAll(".docs-content h2[id], .docs-content h3[id], .docs-content h4[id]"));
    var list = document.querySelector("[data-nb-toc-list]");
    var mobile = document.querySelector("[data-mobile-toc]");
    var select = document.querySelector("[data-mobile-toc-select]");
    if (!list || !select || !headings.length) return;
    list.textContent = ""; select.textContent = "";
    var overview = document.createElement("option");
    overview.value = "_top"; overview.textContent = "Overview"; select.appendChild(overview);
    headings.forEach(function (heading) {
      var item = document.createElement("li"); item.className = "toc-level-" + heading.tagName.slice(1);
      var link = document.createElement("a"); link.href = "#" + heading.id; link.textContent = heading.textContent; link.dataset.tocTarget = heading.id;
      item.appendChild(link); list.appendChild(item);
      var option = document.createElement("option"); option.value = heading.id; option.textContent = heading.textContent; select.appendChild(option);
    });
    if (mobile) mobile.hidden = false;
    select.addEventListener("change", function () { document.getElementById(select.value).scrollIntoView({ behavior: "smooth" }); });
    if (window.IntersectionObserver) {
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          list.querySelectorAll("a").forEach(function (link) { link.removeAttribute("aria-current"); });
          var current = list.querySelector('[data-toc-target="' + CSS.escape(entry.target.id) + '"]');
          if (current) current.setAttribute("aria-current", "location");
          select.value = entry.target.id;
        });
      }, { rootMargin: "-15% 0px -70% 0px" });
      headings.forEach(function (heading) { observer.observe(heading); });
    }
  }

  function initTables() {
    document.querySelectorAll(".docs-content table").forEach(function (table) {
      if (table.parentElement && table.parentElement.classList.contains("table-scroll")) return;
      var wrapper = document.createElement("div"); wrapper.className = "table-scroll"; wrapper.tabIndex = 0;
      wrapper.setAttribute("role", "region"); wrapper.setAttribute("aria-label", "Scrollable table");
      table.parentNode.insertBefore(wrapper, table); wrapper.appendChild(table);
    });
  }

  function initScrollableRegions() {
    document.querySelectorAll("pre, .home-card code, .mermaid, .video-transcript").forEach(function (region) {
      if (!region.hasAttribute("tabindex")) region.tabIndex = 0;
    });
  }

  function initSearch() {
    var dialog = document.querySelector("[data-search-dialog]");
    var input = dialog && dialog.querySelector("[data-search-input]");
    var trigger = document.querySelector("[data-search-trigger]");
    if (!dialog || !input || !trigger) return;
    var prior = null;
    function open() { prior = document.activeElement; dialog.showModal(); input.focus(); }
    function close() { dialog.close(); if (prior) prior.focus(); }
    trigger.addEventListener("click", open);
    dialog.querySelector("[data-search-close]").addEventListener("click", close);
    dialog.addEventListener("cancel", function (event) { event.preventDefault(); close(); });
    dialog.addEventListener("click", function (event) { if (event.target === dialog) close(); });
    document.addEventListener("keydown", function (event) {
      if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "k") { event.preventDefault(); if (!dialog.open) open(); }
    });
    dialog.querySelector("[data-search-form]").addEventListener("submit", function (event) {
      event.preventDefault();
      var query = input.value.trim();
      var results = dialog.querySelector("[data-search-results]");
      var status = dialog.querySelector("[data-search-status]");
      results.textContent = "";
      if (!query) { status.textContent = "Enter a search term."; return; }
      var item = document.createElement("li"), link = document.createElement("a");
      link.href = "https://developers.cloudflare.com/search/?q=" + encodeURIComponent(query);
      link.textContent = 'Search the hosted Cloudflare Docs index for "' + query + '"';
      item.appendChild(link); results.appendChild(item);
      status.textContent = "The frozen repository does not contain the hosted search index.";
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    setThemeToggle();
    initNavigation();
    initAgentCatalog();
    initCatalogs();
    initMobileSidebar();
    initTabs();
    initPackageManagers();
    initArticleTools();
    initCopy();
    initStreamChapters();
    initScrollableRegions();
    initTables();
    initTOC();
    initSearch();
  });
})();
