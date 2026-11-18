// Big wordmark: letters rise in one after another (index pages only).
(() => {
  let n = 0;
  document.querySelectorAll(".mark--big span, .mark--big i").forEach(el => {
    [...el.childNodes].forEach(node => {
      if (node.nodeType !== 3) return;
      const frag = document.createDocumentFragment();
      for (const ch of node.textContent) {
        const b = document.createElement("b");
        b.textContent = ch;
        b.style.animationDelay = (n++ * 35) + "ms";
        frag.appendChild(b);
      }
      node.replaceWith(frag);
    });
  });
})();

// Live date, top right.
(() => {
  const d = new Date();
  const text =
    d.toLocaleDateString("en-US", { weekday: "long" }) + ", " +
    d.toLocaleDateString("en-US", { month: "short" }) + " " + d.getDate() + " " + d.getFullYear();
  document.querySelectorAll("[data-now]").forEach(el => (el.textContent = text));
})();

// Home: one ink sketch per section. A random one shows at rest; hovering a footer link swaps in its own.
(() => {
  const stage = document.getElementById("stage");
  if (!stage) return;
  const links = [...document.querySelectorAll(".foot a[data-sketch]")];
  const imgs = {};
  links.forEach(a => {
    const key = a.dataset.sketch;
    const img = document.createElement("img");
    img.src = "/theme/sketches/" + key + ".webp";
    img.alt = "";
    stage.appendChild(img);
    imgs[key] = img;
  });
  const fit = () => {
    const W = stage.clientWidth, H = stage.clientHeight;
    Object.values(imgs).forEach(img => {
      if (!img.naturalWidth) return;
      const s = Math.min(W / img.naturalWidth, H / img.naturalHeight);
      img.style.width = Math.round(img.naturalWidth * s) + "px";
      img.style.height = Math.round(img.naturalHeight * s) + "px";
    });
  };
  Object.values(imgs).forEach(img => img.addEventListener("load", fit));
  addEventListener("resize", fit);
  const rest = links[Math.floor(Math.random() * links.length)].dataset.sketch;
  const show = key => Object.entries(imgs).forEach(([k, img]) => img.classList.toggle("on", k === key));
  show(rest);
  links.forEach(a => {
    a.addEventListener("mouseenter", () => show(a.dataset.sketch));
    a.addEventListener("focus", () => show(a.dataset.sketch));
  });
  document.querySelector(".foot").addEventListener("mouseleave", () => show(rest));
})();
