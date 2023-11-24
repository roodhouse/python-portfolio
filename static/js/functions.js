function toggleClass(event, currentId, otherId) {
    console.log(currentId)
    let currentElement = document.getElementById(currentId)
    let otherElement = document.getElementById(otherId)
    let mobileMenu = document.getElementById('mobileMenu')
    if(!currentElement.classList.contains('inactive')) {
            currentElement.classList.replace('active', 'inactive')
            otherElement.classList.replace('inactive', 'active')
    }
    if (currentId === 'ham') {
        mobileMenu.classList.replace('inactive', 'active')
    } else {
        mobileMenu.classList.replace('active', 'inactive')
    }
}