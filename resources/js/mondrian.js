const grid = document.querySelector(".mondrian-wrapper")


function resizeGrid() {
    grid.style.height = `${grid.clientWidth}px`
}

//on load set height to width
resizeGrid();

// on window resize
window.addEventListener('resize', resizeGrid);