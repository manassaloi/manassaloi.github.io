// The live date is filled in by an inline script in _includes/header.html, before the first paint.

// iOS only applies :active (the footer's press colour) on pages that listen for touches.
document.addEventListener("touchstart", () => {}, { passive: true });

// Home: one ink sketch per section. A random one shows at rest; hovering a footer link swaps in its own.
(() => {
  const stage = document.getElementById("stage");
  if (!stage) return;
  const links = [...document.querySelectorAll(".foot a[data-sketch]")];
  // Only a mouse or trackpad can hover, so only then are the other sketches ever shown.
  const canHover = matchMedia("(hover: hover) and (pointer: fine)").matches;
  const imgs = {};
  let wanted = null;

  // Each sketch is added once and decoded before it can be shown, so it fades in whole instead of
  // drawing in mid-download. CSS places and sizes it (.stage img in _sass/theme/_pages.scss).
  const load = (key, priority) => {
    if (!imgs[key]) {
      const img = new Image();
      img.alt = "";
      img.decoding = "async";
      if (priority) img.fetchPriority = priority;
      img.src = "/assets/img/home/" + key + ".webp";
      imgs[key] = img.decode().then(() => { stage.appendChild(img); return img; });
    }
    return imgs[key];
  };

  const show = key => {
    wanted = key;
    load(key).then(img => {
      if (wanted !== key) return; // the pointer moved on while it loaded
      stage.querySelectorAll("img").forEach(el => el.classList.toggle("on", el === img));
    }, () => {});
  };

  const rest = links[Math.floor(Math.random() * links.length)].dataset.sketch;
  load(rest, "high");
  show(rest);

  // With a mouse, fetch the rest once the first is in, so a hover swaps instantly. A phone never
  // shows them, so it never downloads them. (Keyboard focus still loads one on demand.)
  if (canHover) imgs[rest].finally(() => links.forEach(a => load(a.dataset.sketch, "low")));

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
