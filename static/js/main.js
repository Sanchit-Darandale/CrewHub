/*
CrewHub JavaScript
Client-side functionality and interactivity
*/

// Auto-hide flash messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const flashMessages = document.querySelectorAll('.flash-message');
    
    flashMessages.forEach(function(message) {
        setTimeout(function() {
            message.style.animation = 'slideOut 0.3s ease';
            setTimeout(function() {
                message.remove();
            }, 300);
        }, 5000);
    });
});

// Animation for slide out
const style = document.createElement('style');
style.textContent = `
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Form validation helper
function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

function validateMobile(mobile) {
    const regex = /^[0-9]{10}$/;
    return regex.test(mobile);
}

function validatePincode(pincode) {
    const regex = /^[0-9]{6}$/;
    return regex.test(pincode);
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add loading state to forms on submit
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function() {
        const submitButton = this.querySelector('button[type="submit"]');
        if (submitButton) {
            submitButton.disabled = true;
            submitButton.textContent = 'Please wait...';
        }
    });
});

// Client-side form validation feedback
function addInputValidation() {
    // Email inputs
    const emailInputs = document.querySelectorAll('input[type="email"]');
    emailInputs.forEach(input => {
        input.addEventListener('blur', function() {
            if (this.value && !validateEmail(this.value)) {
                this.style.borderColor = 'var(--error-color)';
            } else {
                this.style.borderColor = 'var(--border-color)';
            }
        });
    });
    
    // Mobile inputs
    const mobileInputs = document.querySelectorAll('input[type="tel"]');
    mobileInputs.forEach(input => {
        input.addEventListener('input', function() {
            this.value = this.value.replace(/[^0-9]/g, '');
        });
        
        input.addEventListener('blur', function() {
            if (this.value && !validateMobile(this.value)) {
                this.style.borderColor = 'var(--error-color)';
            } else {
                this.style.borderColor = 'var(--border-color)';
            }
        });
    });
    
    // Pincode inputs
    const pincodeInputs = document.querySelectorAll('input[name="pincode"]');
    pincodeInputs.forEach(input => {
        input.addEventListener('input', function() {
            this.value = this.value.replace(/[^0-9]/g, '');
        });
        
        input.addEventListener('blur', function() {
            if (this.value && !validatePincode(this.value)) {
                this.style.borderColor = 'var(--error-color)';
            } else {
                this.style.borderColor = 'var(--border-color)';
            }
        });
    });
}

// Initialize validation on page load
document.addEventListener('DOMContentLoaded', addInputValidation);

// Prevent multiple form submissions
let formSubmitted = false;
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(e) {
        if (formSubmitted) {
            e.preventDefault();
            return false;
        }
        formSubmitted = true;
        
        // Reset after 3 seconds in case of error
        setTimeout(() => {
            formSubmitted = false;
        }, 3000);
    });
});

// Console log for debugging
console.log('CrewHub JavaScript loaded successfully');
