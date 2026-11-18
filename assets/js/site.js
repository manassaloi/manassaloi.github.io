// Live date, top right, day before month: "Wednesday, 18 Nov 2026".
// The order is set here; en-US only supplies the names (three-letter months, "Sep" not "Sept").
(() => {
  const d = new Date();
  const text =
    d.toLocaleDateString("en-US", { weekday: "long" }) + ", " +
    d.getDate() + " " + d.toLocaleDateString("en-US", { month: "short" }) + " " + d.getFullYear();
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
    img.src = "/assets/img/home/" + key + ".webp";
    img.alt = "";
    stage.appendChild(img);
    imgs[key] = img;
  });
  // Size each sketch to fit the stage exactly, so the edge fade lands on the drawing itself.
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
  // Only a real mouse hover or keyboard focus swaps the sketch. A tap on a phone fires the same
  // mouseenter and focus as a hover, just before the click, so the drawing used to change before
  // the next page loaded (and stayed changed when going back). Pointer events say what the
  // pointer is, and :focus-visible is true for Tab but not for a tap.
  links.forEach(a => {
    a.addEventListener("pointerenter", e => { if (e.pointerType === "mouse") show(a.dataset.sketch); });
    a.addEventListener("focus", () => { if (a.matches(":focus-visible")) show(a.dataset.sketch); });
  });
  document.querySelector(".foot").addEventListener("pointerleave", e => { if (e.pointerType === "mouse") show(rest); });
})();
