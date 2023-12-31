function toggleClass(event, currentId, otherId, sectionWrapper) {
    console.log(event)
    event.preventDefault()
    let currentElement = document.getElementById(currentId)
    let otherElement = document.getElementById(otherId)
    let mobileMenu = document.getElementById('mobileMenu')
    let logo = document.getElementById('navImg')

    if(!currentElement.classList.contains('inactive')) {
            currentElement.classList.replace('active', 'inactive')
            otherElement.classList.replace('inactive', 'active')
    } 
    if (currentId === 'ham') {
        mobileMenu.classList.replace('inactive', 'active')
        logo.style.visibility = 'hidden'
    } else {
        mobileMenu.classList.replace('active', 'inactive')
        logo.style.visibility = 'visible'
    }

    const section = document.getElementById(sectionWrapper)
    if (section) {
        section.scrollIntoView({behavior: 'smooth'})
    }
}