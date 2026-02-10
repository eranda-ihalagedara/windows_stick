const socket = io();

const trackpad = document.getElementById('trackpad');
const scrollStrip = document.getElementById('scroll-strip');
const btnLeft = document.getElementById('btn-left');
const btnRight = document.getElementById('btn-right');

let lastX = 0;
let lastY = 0;
let isTrackpadActive = false;

// Trackpad
trackpad.addEventListener('touchstart', (e) => {
    isTrackpadActive = true;
    lastX = e.touches[0].clientX;
    lastY = e.touches[0].clientY;
}, { passive: false });

trackpad.addEventListener('touchmove', (e) => {
    if (!isTrackpadActive) return;

    // Prevent default to stop scrolling the page
    if (e.cancelable) e.preventDefault();

    const currentX = e.touches[0].clientX;
    const currentY = e.touches[0].clientY;

    const dx = currentX - lastX;
    const dy = currentY - lastY;

    socket.emit('mousemove', { dx: dx, dy: dy });

    lastX = currentX;
    lastY = currentY;
}, { passive: false });

trackpad.addEventListener('touchend', () => {
    isTrackpadActive = false;
});

let isScrolling = false;
let lastScrollY = 0;

// Scroll Strip
scrollStrip.addEventListener('touchstart', (e) => {
    isScrolling = true;
    lastScrollY = e.touches[0].clientY;
}, { passive: false });

scrollStrip.addEventListener('touchmove', (e) => {
    if (!isScrolling) return;
    if (e.cancelable) e.preventDefault();

    const currentY = e.touches[0].clientY;
    const dy = currentY - lastScrollY;

    // Send scroll event
    socket.emit('scroll', { dy: dy, dx: 0 });

    lastScrollY = currentY;
}, { passive: false });

scrollStrip.addEventListener('touchend', () => {
    isScrolling = false;
});

// Mouse Buttons
btnLeft.addEventListener('click', () => {
    socket.emit('mouseclick', { button: 'left' });
});

btnRight.addEventListener('click', () => {
    socket.emit('mouseclick', { button: 'right' });
});


