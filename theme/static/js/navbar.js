document.getElementById('mobile-menu-button').addEventListener('click', function() {
    var menu = document.getElementById('mobile-menu');
    if (menu.classList.contains('hidden')) {
        menu.classList.remove('hidden');
        this.setAttribute('aria-expanded', 'true');
    } else {
        menu.classList.add('hidden');
        this.setAttribute('aria-expanded', 'false');
    }
});

document.addEventListener('DOMContentLoaded', () => {
// Assign the button click
document.querySelectorAll('.dropbtn').forEach(btn => {
    btn.addEventListener('click', e => {
        e.stopPropagation(); // Prevent click event from bubbling up
        const dropdownContent = e.target.closest('.dropdown').querySelector('.dropdown-content');
        const isClosed = dropdownContent.classList.contains('hidden')
        
        // First close all
        document.querySelectorAll('.dropdown-content').forEach(div => div.classList.add('hidden'));
        
        // Toggle the one you want which is CLOSEST
        if (isClosed) {
            dropdownContent.classList.remove('hidden');
        }
    });
  });
});
  
// Catch the click outside
document.addEventListener('click', e => {
  if (!e.target.closest('.dropbtn')) {
    document.querySelectorAll('.dropdown-content').forEach(div => div.classList.remove('show'));
  }
});
  