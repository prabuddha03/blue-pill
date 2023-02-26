console.log('working');
let hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

hamburger.addEventListener('click', mobileMenu);
function mobileMenu() {
	hamburger.classList.toggle('active');
	navMenu.classList.toggle('active');
}

let navColor = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
	if (window.scrollY > 40) {
		navColor.style.backgroundColor = '#432fc3';
	} else {
		navColor.style.backgroundColor = 'transparent';
	}
});

let buttonExplore = document .querySelectorAll('a[href^="#"]')

buttonExplore.forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
})
