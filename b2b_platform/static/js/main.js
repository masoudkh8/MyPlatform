// Main JavaScript for B2B Traders Platform

document.addEventListener('DOMContentLoaded', function() {
  // Initialize tooltips if needed
  initTooltips();
  
  // Handle button click animations
  initButtonAnimations();
  
  // Handle tab switching
  initTabs();
  
  // Initialize search functionality
  initSearch();
  
  // Handle FAB (Floating Action Button)
  initFAB();
});

/**
 * Initialize button press animations
 */
function initButtonAnimations() {
  const buttons = document.querySelectorAll('.btn, .float-btn');
  
  buttons.forEach(button => {
    button.addEventListener('click', function(e) {
      // Add ripple effect or scale animation
      this.style.transform = 'scale(0.98)';
      setTimeout(() => {
        this.style.transform = 'scale(1)';
      }, 150);
    });
  });
}

/**
 * Initialize tab switching functionality
 */
function initTabs() {
  const tabs = document.querySelectorAll('.tab');
  
  tabs.forEach(tab => {
    tab.addEventListener('click', function(e) {
      e.preventDefault();
      
      // Remove active class from all tabs
      tabs.forEach(t => t.classList.remove('active'));
      
      // Add active class to clicked tab
      this.classList.add('active');
    });
  });
}

/**
 * Initialize search functionality
 */
function initSearch() {
  const searchInput = document.querySelector('.search-input');
  
  if (searchInput) {
    let timeoutId;
    
    searchInput.addEventListener('input', function(e) {
      clearTimeout(timeoutId);
      
      const query = this.value.trim();
      
      // Debounce search
      timeoutId = setTimeout(() => {
        if (query.length > 2) {
          performSearch(query);
        }
      }, 300);
    });
  }
}

/**
 * Perform search API call
 */
function performSearch(query) {
  // This would be implemented with actual API calls
  console.log('Searching for:', query);
  
  // Example: fetch(`/api/search?q=${encodeURIComponent(query)}`)
  //   .then(response => response.json())
  //   .then(data => updateSearchResults(data));
}

/**
 * Initialize Floating Action Button
 */
function initFAB() {
  const fab = document.querySelector('.fab');
  
  if (fab) {
    fab.addEventListener('click', function(e) {
      e.preventDefault();
      
      // Open AI assistant modal or navigate to AI page
      console.log('AI Assistant clicked');
      
      // Example: Show AI modal
      // showAIModal();
    });
  }
}

/**
 * Initialize tooltips (if needed)
 */
function initTooltips() {
  // Implementation for tooltips can be added here
  // Using a library like Tippy.js or custom implementation
}

/**
 * Update search results in the UI
 */
function updateSearchResults(results) {
  // Implementation for updating search results
  console.log('Search results:', results);
}

/**
 * Format date for display
 */
function formatDate(dateString) {
  const options = { year: 'numeric', month: 'short', day: 'numeric' };
  return new Date(dateString).toLocaleDateString('en-US', options);
}

/**
 * Format numbers with commas
 */
function formatNumber(num) {
  return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

/**
 * Show loading state
 */
function showLoading(element) {
  element.classList.add('loading');
  element.disabled = true;
}

/**
 * Hide loading state
 */
function hideLoading(element) {
  element.classList.remove('loading');
  element.disabled = false;
}

/**
 * Show toast notification
 */
function showToast(message, type = 'info') {
  // Create toast element
  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  toast.textContent = message;
  
  // Add styles
  toast.style.cssText = `
    position: fixed;
    bottom: 100px;
    left: 50%;
    transform: translateX(-50%);
    background: ${type === 'success' ? '#2ECC71' : type === 'error' ? '#E74C3C' : '#1E3A5F'};
    color: white;
    padding: 12px 24px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    z-index: 10000;
    animation: slideUp 0.3s ease;
  `;
  
  // Add animation keyframes
  if (!document.getElementById('toast-styles')) {
    const style = document.createElement('style');
    style.id = 'toast-styles';
    style.textContent = `
      @keyframes slideUp {
        from {
          opacity: 0;
          transform: translateX(-50%) translateY(20px);
        }
        to {
          opacity: 1;
          transform: translateX(-50%) translateY(0);
        }
      }
      @keyframes slideDown {
        from {
          opacity: 1;
          transform: translateX(-50%) translateY(0);
        }
        to {
          opacity: 0;
          transform: translateX(-50%) translateY(20px);
        }
      }
    `;
    document.head.appendChild(style);
  }
  
  document.body.appendChild(toast);
  
  // Remove after 3 seconds
  setTimeout(() => {
    toast.style.animation = 'slideDown 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}

/**
 * Handle infinite scroll for feed
 */
function initInfiniteScroll() {
  const feedContainer = document.querySelector('.posts-feed');
  
  if (feedContainer) {
    let isLoading = false;
    
    window.addEventListener('scroll', function() {
      if (isLoading) return;
      
      const scrollPosition = window.innerHeight + window.scrollY;
      const threshold = document.body.offsetHeight - 100;
      
      if (scrollPosition >= threshold) {
        isLoading = true;
        loadMorePosts();
      }
    });
  }
}

/**
 * Load more posts (pagination)
 */
function loadMorePosts() {
  // Implementation for loading more posts
  console.log('Loading more posts...');
  
  // Example: fetch('/api/posts?page=2')
  //   .then(response => response.json())
  //   .then(posts => appendPosts(posts))
  //   .finally(() => { isLoading = false; });
}

/**
 * Toggle like on posts
 */
function toggleLike(postId) {
  // Implementation for liking posts
  console.log('Toggle like for post:', postId);
  
  // Example: fetch(`/api/posts/${postId}/like`, { method: 'POST' })
  //   .then(response => response.json())
  //   .then(data => updateLikeCount(data));
}

/**
 * Save post
 */
function savePost(postId) {
  // Implementation for saving posts
  console.log('Save post:', postId);
  
  showToast('Post saved successfully', 'success');
  
  // Example: fetch(`/api/posts/${postId}/save`, { method: 'POST' })
}

// Export functions for global use
window.B2BPlatform = {
  showToast,
  formatDate,
  formatNumber,
  toggleLike,
  savePost
};
