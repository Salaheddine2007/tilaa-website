(function(){
  var hamburger = document.getElementById('hamburger');
  var mobileNav = document.getElementById('mobileNav');
  var mobileClose = document.getElementById('mobileClose');
  if(!hamburger || !mobileNav) return;
  hamburger.addEventListener('click', function(){
    mobileNav.classList.add('open');
    hamburger.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  });
  function closeMobileNav(){
    mobileNav.classList.remove('open');
    hamburger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }
  if(mobileClose) mobileClose.addEventListener('click', closeMobileNav);
  mobileNav.querySelectorAll('a').forEach(function(a){
    a.addEventListener('click', closeMobileNav);
  });
})();
