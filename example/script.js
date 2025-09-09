// Simple JavaScript to demonstrate functionality
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Sprite CLI demo loaded successfully!');
    
    // Add some interactive behavior to feature cards
    const featureCards = document.querySelectorAll('.feature-card');
    
    featureCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.borderLeftColor = '#764ba2';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.borderLeftColor = '#667eea';
        });
    });
    
    // Add click handlers to command codes for copying
    const commandCodes = document.querySelectorAll('.command-list code');
    
    commandCodes.forEach(code => {
        code.style.cursor = 'pointer';
        code.title = 'Click to copy command';
        
        code.addEventListener('click', function() {
            const text = this.textContent;
            navigator.clipboard.writeText(text).then(() => {
                // Visual feedback
                const originalText = this.textContent;
                this.textContent = 'Copied!';
                this.style.background = '#48bb78';
                
                setTimeout(() => {
                    this.textContent = originalText;
                    this.style.background = '#2d3748';
                }, 1000);
            });
        });
    });
    
    // Display server info if available
    if (window.location.hostname) {
        console.log(`Server running on: ${window.location.origin}`);
    }
});

// Add some fun console messages
console.log(`
 ███████╗██████╗ ██████╗ ██╗████████╗███████╗
 ██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝██╔════╝
 ███████╗██████╔╝██████╔╝██║   ██║   █████╗  
 ╚════██║██╔═══╝ ██╔══██╗██║   ██║   ██╔══╝  
 ███████║██║     ██║  ██║██║   ██║   ███████╗
 ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝
 
 Welcome to Sprite CLI! 🚀
 Your static website server is running successfully.
`);