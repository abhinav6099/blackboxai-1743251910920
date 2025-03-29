// Main application controller
document.addEventListener('DOMContentLoaded', () => {
    // Initialize components
    initNavigation();
    initAudioPlayers();
});

function initNavigation() {
    // Handle mobile menu toggle
    const menuBtn = document.getElementById('menu-btn');
    if (menuBtn) {
        menuBtn.addEventListener('click', () => {
            const menu = document.getElementById('mobile-menu');
            menu.classList.toggle('hidden');
        });
    }
}

function initAudioPlayers() {
    // Initialize all audio players on page
    document.querySelectorAll('audio').forEach(player => {
        player.addEventListener('play', () => {
            // Pause other players when one starts
            document.querySelectorAll('audio').forEach(p => {
                if (p !== player && !p.paused) p.pause();
            });
        });
    });
}

// Utility functions
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `fixed bottom-4 right-4 px-4 py-2 rounded-md shadow-lg text-white ${
        type === 'error' ? 'bg-red-500' : 
        type === 'success' ? 'bg-green-500' : 'bg-blue-500'
    }`;
    toast.textContent = message;
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.remove();
    }, 3000);
}

// Export for module usage if needed
export { initNavigation, initAudioPlayers, showToast };