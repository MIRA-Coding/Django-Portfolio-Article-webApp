document.addEventListener("DOMContentLoaded", () => {
  const navbar = document.getElementById("site-nav");
  if (!navbar) return;

  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      navbar.style.transform = "translate(-50%, 5px)";
      navbar.style.background = "rgba(11, 15, 25, 0.92)";
    } else {
      navbar.style.transform = "translate(-50%, 0)";
      navbar.style.background = "rgba(15, 23, 42, 0.65)";
    }
  });
});
