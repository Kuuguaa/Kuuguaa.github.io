// 滚动渐入动画：进入视口的区块加上 .visible
(function () {
  var blocks = document.querySelectorAll('.reveal');

  if (!('IntersectionObserver' in window)) {
    // 老浏览器直接全部显示
    blocks.forEach(function (el) { el.classList.add('visible'); });
    return;
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  blocks.forEach(function (el) { observer.observe(el); });
})();

// 滑过顶部横幅后，常驻按钮保持即可（无额外逻辑，纯 CSS 固定定位）
