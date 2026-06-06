document.addEventListener('DOMContentLoaded', () => {
    // Current year in footer
    const yearEl = document.getElementById('current-year');
    if(yearEl) yearEl.textContent = new Date().getFullYear();

    // Navigation logic (Sidebar Tabs)
    const navButtons = document.querySelectorAll('.nav-btn');
    const sections = document.querySelectorAll('.section');

    navButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove active class from all buttons and sections
            navButtons.forEach(btn => btn.classList.remove('active'));
            sections.forEach(sec => sec.classList.remove('active'));

            // Add active class to clicked button
            button.classList.add('active');

            // Show corresponding section
            const targetId = button.getAttribute('data-target');
            const targetSection = document.getElementById(targetId);
            
            if (targetSection) {
                targetSection.classList.add('active');
                window.scrollTo({ top: 0, behavior: 'smooth' });
                
                // Re-trigger animations for elements inside the section
                const animatedElements = targetSection.querySelectorAll('.fade-in, .fade-in-up, .smart-card');
                animatedElements.forEach(el => {
                    el.style.animation = 'none';
                    el.offsetHeight; /* trigger reflow */
                    el.style.animation = null; 
                });
            }
        });
    });
});
