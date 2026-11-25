/** @odoo-module **/
// Progressive enhancement only; native Odoo owns navigation and all commerce.
function initLaRosa() {
    const root = document.querySelector('.larosa-site');
    if (!root || !('IntersectionObserver' in window)
        || window.matchMedia('(prefers-reduced-motion: reduce)').matches
        || document.body.classList.contains('editor_enable')) return;
    const observer = new IntersectionObserver((entries) => {
        for (const entry of entries) {
            if (entry.isIntersecting) {
                entry.target.classList.remove('lr-wait');
                observer.unobserve(entry.target);
            }
        }
    }, { threshold: 0.06 });
    root.querySelectorAll('.lr-reveal').forEach((element) => {
        // Never hide content already in the initial viewport.
        if (element.getBoundingClientRect().top > window.innerHeight) {
            element.classList.add('lr-wait');
            observer.observe(element);
        }
    });
}
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLaRosa, { once: true });
} else {
    initLaRosa();
}
