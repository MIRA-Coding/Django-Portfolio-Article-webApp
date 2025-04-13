document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('scrollContainer');
    if (!container) {
        console.error('Element with ID "scrollContainer" not found.');
        return;
    }

    const items = container.children;
    const itemCount = items.length;

    // Clone items to create a seamless scrolling effect
    for (let i = 0; i < 2; i++) {
        for (let j = 0; j < itemCount; j++) {
            const clone = items[j].cloneNode(true);
            container.appendChild(clone);
        }
    }

    let scrollAmount = 0;
    const scrollSpeed = 0.5;

    function autoScroll() {
        scrollAmount += scrollSpeed;

        // Check if the scroll has reached the end of the original content
        if (scrollAmount >= container.scrollWidth / 3) {
            scrollAmount = 0; // Reset scroll position without causing a jump
        }

        container.scrollLeft = scrollAmount;
        requestAnimationFrame(autoScroll);
    }

    autoScroll();
});