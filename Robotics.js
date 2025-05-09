// JavaScript to handle form submission
document.getElementById('contact-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way
  
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;
  
    if (name && email && message) {
      alert(`Thank you for reaching out, ${name}! We'll get back to you soon.`);
    } else {
      alert('Please fill out all the fields.');
    }
  
    // Reset form
    document.getElementById('contact-form').reset();
  });
  


  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const targetId = this.getAttribute('href');
      const targetElement = document.querySelector(targetId);
      const offset = 120; // Adjust for header height
      const elementPosition = targetElement.offsetTop;
      const offsetPosition = elementPosition - offset;
  
      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });
    });

  // Shrink the header on scroll
window.addEventListener('scroll', function () {
  const header = document.querySelector('header');
  if (window.scrollY > 100) { // If the user scrolls down 100px or more
      header.classList.add('shrink');
  } else {
      header.classList.remove('shrink');
  }
});

// Toggle the mobile menu
const menuToggle = document.querySelector('.menu-toggle');
const menu = document.querySelector('nav ul');

menuToggle.addEventListener('click', () => {
  menu.classList.toggle('active');
});

    
  });
  
